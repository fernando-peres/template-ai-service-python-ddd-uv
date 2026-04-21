# CLAUDE.md

## Setup

```bash
uv sync --all-groups       # Install all dependencies
source .venv/bin/activate  # Activate virtual environment
pre-commit install         # Install git hooks
cp .env.example .env       # Configure environment variables
```

## Running the Service

```bash
./run.sh                   # Start locally (reads .env, validates required vars)
```

Required env vars: `SERVICE_NAME`, `HOST_IP`, `PORT`

## Development Commands

```bash
uv run ruff check .        # Lint
uv run ruff format .       # Format
uv run mypy .              # Type check (strict mode)
uv run pytest              # Run tests with coverage
```

## Docker

```bash
# Standard
docker compose -f docker/docker-compose.yaml --env-file .env up --build

# With PostgreSQL
docker compose -f docker/docker-compose-with-psql.yaml --env-file .env --profile local up --build

# Teardown
docker compose -f docker/docker-compose.yaml --env-file .env down -v
```

## Architecture (DDD)

```
service/
├── domain/        # Domain logic — entities, value objects, domain services
├── application/   # Use cases — orchestrates domain, defines DTOs
├── infra/         # Infrastructure — DB models, external adapters
├── interface/     # Entry points — FastAPI routers (api/), CLI
└── shared/        # Cross-cutting — ServiceRegistry (DI), logger, exceptions
```

**Dependency direction:** `interface` → `application` → `domain` ← `infra`

- Add new routes in `service/interface/api/`
- Add use cases in `service/application/`
- Add domain logic in `service/domain/`
- Add DB models in `service/infra/db/models.py`
- Register shared resources in `service/shared/registry.py`

## Key Conventions

- **Python 3.13+**, strict MyPy — all code must be fully typed
- **Line length:** 98 (Ruff)
- **Imports:** sorted by Ruff (isort-compatible)
- **Async:** `asyncio_mode = auto` — pytest tests can be async by default
- **Settings:** all config via `service/settings.py` (Pydantic Settings), never hardcode
- **Logging:** use `setup_service_logger` from `service/shared`; don't use `print()`

## Adding Dependencies

```bash
uv add <package>           # Production dependency
uv add --dev <package>     # Dev-only dependency
```

## Pre-commit Hooks

Runs automatically on `git commit`: ruff lint → ruff format → mypy → pytest (manual stage).

To run manually:
```bash
pre-commit run --all-files
pre-commit run --hook-stage manual  # includes pytest
```

## When task is completed

When you finish a task inform in claude code extentions or CLI

Print:
╔═══════════════════════════════════════════════════════════╗
║  🤖  Claude  ·  ✅  All tasks executed successfully        ║
╚═══════════════════════════════════════════════════════════╝