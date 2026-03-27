# Docker

All Docker files live in `docker/`. Commands must be run from the **project root** so the build context resolves correctly.

## Files

| File | Purpose |
|------|---------|
| `Dockerfile` | Multi-stage build (builder → production) using Python 3.13-slim-alpine and `uv` |
| `docker-compose.yaml` | Defines the `api` service and an optional local `postgres` service |

## Prerequisites

- Docker with BuildKit enabled (Docker 23+ has it on by default)
- A `.env` file at the project root (copy from `.env.example`)

```bash
cp .env.example .env
# fill in your API keys and variables
```

## Build

```bash
# Build the image from the project root
docker build \
  --ssh default \
  -f docker/Dockerfile \
  -t template-ai-service .
```

## Run with Docker Compose

All `docker compose` commands are run from the **project root** using `-f` to point at the compose file.

> **Note:** Always pass `--env-file .env` so Docker Compose can interpolate `${SERVICE_NAME}`, `${HOST_IP}`, and `${PORT}` from the project root `.env`. Without it, those variables are blank because Compose looks for `.env` next to the compose file (`docker/`), not the project root.
>
> **Why two separate `.env` references?**
> - `--env-file .env` (CLI flag) — used by Docker Compose **at parse time** to substitute `${VAR}` placeholders in `docker-compose.yaml` (e.g. `container_name`, `ports`). Compose resolves this relative to your working directory.
> - `env_file: ../.env` (inside the service) — used by Docker **at runtime** to inject variables into the container's environment. Compose resolves this relative to the compose file.
> Both are needed: the CLI flag drives compose-level interpolation; the service `env_file` makes the same variables available to the running application.

### API only (external Postgres)

```bash
docker compose -f docker/docker-compose.yaml --env-file .env up
```

### API + local Postgres

The `postgres` service is gated behind the `local` profile:

```bash
docker compose -f docker/docker-compose.yaml --env-file .env --profile local up
```

### Build and start in one step

```bash
docker compose -f docker/docker-compose.yaml --env-file .env --profile local up --build
```

### Stop and remove containers

```bash
docker compose -f docker/docker-compose.yaml --env-file .env down
```

### Stop and also remove the Postgres volume

```bash
docker compose -f docker/docker-compose.yaml --env-file .env down -v
```

## Environment variables

The compose file loads `.env` from the project root. Required variables are documented in [.env.example](../.env.example).
