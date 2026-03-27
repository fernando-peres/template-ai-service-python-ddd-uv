# Ruff & Mypy Configuration Reference

Quick reference for each option configured in `pyproject.toml`.

* 🔗 [How to: Automate a clean code base with Ruff and Mypy.](https://medium.com/@fernando.peres/how-to-automate-a-clean-code-base-with-ruff-and-mypy-ff7d9fa51e86) 


---

## Ruff

### `[tool.ruff]` — Core Settings

| Option | Value | Explanation |
|--------|-------|-------------|
| `line-length` | `98` | Max characters per line. Slightly wider than Black's default (88) to reduce unnecessary line breaks. |
| `target-version` | `py313` | Enables linting rules appropriate for Python 3.13+; suppresses warnings about syntax available only in newer versions. |
| `fix` | `true` | Auto-applies safe fixes during linting (e.g. sorting imports, removing unused variables). Unsafe fixes still require `--unsafe-fixes`. |
| `exclude` | `[...]` | Paths ruff never touches: virtual env, build artifacts, config files (`.toml`, `.yaml`), notebooks, and IDE folders. |
| `src` | `[".", "service", "tests"]` | Source roots ruff uses to distinguish first-party imports from third-party ones. Required for correct isort ordering. |

---

### `[tool.ruff.format]` — Formatter

| Option | Value | Explanation |
|--------|-------|-------------|
| `indent-style` | `"space"` | Uses spaces for indentation (not tabs), consistent with PEP 8 and Black. |
| `quote-style` | `"double"` | Enforces double quotes for all strings, matching Black's style. |
| `skip-magic-trailing-comma` | `false` | When `false`, a trailing comma in a collection forces multi-line formatting — preserving intentional line breaks. |

---

### `[tool.ruff.lint]` — Linting Rules

#### `select` — Enabled Rule Sets

| Code | Plugin | What it catches |
|------|--------|-----------------|
| `E` | pycodestyle | PEP 8 style errors (indentation, whitespace, blank lines) |
| `F` | Pyflakes | Undefined names, unused imports, redefined variables |
| `B` | flake8-bugbear | Likely bugs and design issues (mutable defaults, assert misuse, etc.) |
| `I` | isort | Import order violations |

#### `extend-select` — Additional Rule Sets

| Code | Plugin | What it catches |
|------|--------|-----------------|
| `UP` | pyupgrade | Outdated syntax that can be modernized (e.g. `Union[X, Y]` → `X \| Y`) |
| `SIM` | flake8-simplify | Overly complex patterns that can be simplified (e.g. `if x == True:` → `if x:`) |
| `C90` | mccabe | Functions exceeding cyclomatic complexity threshold (default: 10) |

---

### `[tool.ruff.lint.isort]` — Import Sorting

| Option | Value | Explanation |
|--------|-------|-------------|
| `known-first-party` | `["main_lib", "main"]` | Tells isort these modules belong to the project. They are grouped separately from third-party imports and sorted accordingly. |

---

### `[tool.ruff.lint.pycodestyle]` — Style Checks

| Option | Value | Explanation |
|--------|-------|-------------|
| `max-doc-length` | `200` | Maximum line length allowed inside docstrings and comments. More lenient than code to accommodate long URLs or detailed descriptions. |

---

## Mypy

### `[tool.mypy]` — Type Checking

| Option | Value | Explanation |
|--------|-------|-------------|
| `python_version` | `"3.13"` | Type checking is evaluated against Python 3.13 semantics and standard library stubs. |
| `strict` | `true` | Activates all optional strictness flags: `disallow_untyped_defs`, `disallow_incomplete_defs`, `warn_return_any`, `no_implicit_optional`, and more. |
| `exclude` | `[...]` | Paths mypy skips: venv, scripts, and anything outside `src/`, `tests/`, `main.py`, or `config.py`. |
| `ignore_missing_imports` | `true` | Silences errors when mypy can't find type stubs for third-party packages (e.g. packages without `py.typed` or `*.pyi` stubs). |
| `explicit_package_bases` | `true` | Resolves module names relative to declared source roots only, preventing ambiguous dotted paths when packages lack `__init__.py`. |
| `mypy_path` | `"/service"` | Adds `/service` as an extra search path so mypy can locate modules under that directory without needing them on `PYTHONPATH`. |
| `disable_error_code` | `["misc"]` | Suppresses the `misc` error code — a catch-all for errors that don't fit a named category, often from decorator or metaclass inference issues. |
