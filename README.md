# [Project Name]

**TODO:** Read [setup-todo.md](./setup-to-do.md) and Update this intro and Topic 1 to describe the service.

**TODO:** Describe...

This service is a GenAI solution for generating ...

Scope of work:
- feature 1

## 1. Related Business and Technical definitions

**TODO:** Describe...

## 2. Repository Technical Features

A modern Python project template preconfigured with Ruff for linting and formatting, and MyPy for static type checking. It also uses pre-commit to enforce code quality before each commit.

🚀 Features:

- **Ruff**: Blazing-fast linter and formatter

- **MyPy**: Static type checking for Python

- **pre-commit**: Automated checks before every commit

- **Easy setup**: Fast environment provisioning with `uv`

---

## 3. Setup in Local Environment

> ***
>
> ⚠️ **<u> Before start check these notes:</u>**
>
> Before running the following commands, check if `uv` is installed.
>
> This repository uses `uv` to manage dependencies. So, you need to install `uv` on your computer.
> 
> 💡 **Tips**: 
>  - To install uv check: [uv-installation](./_docs/setup/uv-installation.md)
>       - Check if the current Python version is the same in the `pyproject.toml`.
> 
> - For further information, check: [uv-python version management](./_docs/setup/uv-python-version-management.md)
> 
> - For more information about pre-commit, check [pre-commit](./_docs/setup/pre-commit.md)
>
> - For further information about mypy and ruff configuration in pyproject read [readme-mypy-ruff-conig.md](./_docs/readme/readme-mypy-ruff.config.md)
> ***



### 3.1 Setup Python Environment

**Step 1**: Install all dependencies

```bash
uv sync --all-groups
```

> Installs all dependencies, including core packages and additional groups such as dev
> (e.g., pytest, which is only required for development).
> In uv, you can organize dependencies into different groups, similar to how it’s done with npm/yarn/bun.

**Step 2**: Activate the virtual environment (macOS/Linux)

```bash
source .venv/bin/activate
```

**Step 3**: Install pre-commit hooks

```bash
pre-commit install  
```

💡 Read: pre-commit explanation [readme-pre-commit](./_docs/readme/readme-precommit.md)


#### Customization

* Configure PyTest, Ruff and MyPy via `pyproject.toml`.

* Add or remove `pre-commit` hooks in `.pre-commit-config.yaml

##### Add a Python Package

```sh
uv add <package-name>
```

### 3.2 Add a Package as a Development Dependency

```sh
uv add --dev <package-name>
```

💡 Development dependencies are only installed in development environments and are excluded from production builds.

---


## 4. Setup in Remote Environment

Scope: `Dev`, `Staging`, `Prod`

Install only the required production dependencies:

```bash
uv sync
```

> This will create the `.venv/` folder and install all required production (core) dependencies.

## 5. Tests

The project uses **pytest** with coverage. Run the test suite with:

```sh
pytest
```

Run with detailed coverage:

```sh
pytest --cov=service --cov-report=term-missing
```

Pytest is configured in `pyproject.toml`. A pytest hook is also available as a **manual** pre-commit hook


## 6. Folder Structure

```
├── _docs/                # documentation for humans
├── _specs/               # specifications for spec-driven development and vibe coding (AI-oriented context and instructions)
├── data/                 # local database
├── docker/               # Docker images
├── service/              # core service code organized by DDD layers
│   ├── application/      # use cases, workflows, and orchestration logic
│   ├── config/           # application configuration (settings, env handling)
│   ├── domain/           # business logic (entities, value objects, domain services)
│   ├── infra/            # infrastructure implementations (DB, APIs, external services)
│   ├── interface/        # entry points (HTTP routes, CLI, message consumers)
│   └── shared/           # shared utilities and cross-cutting concerns
├── tests/                # tests
├── utils/                # maintenance and utilities
├── main.py               # application entry point (startup and wiring)
```


## 7. Keys and Variables

🔐 They are defined in the file [readme-evn-keys-n-vars](./_docs/readme/readme-env-keys-n-vars.md) and [.env.example](.env.example)