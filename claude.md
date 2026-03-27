# Claude Code configuration for this project

Rules and skills in the `.cursor/` folder guide the AI. **Rules** are applied automatically when relevant; **skills** are discovered from descriptions and can be invoked with `/skill-name` or when the task matches.

---

## Rules (`.cursor/rules/`)

Read these before starting any task. They are included in context by Cursor when they apply.

| File | Purpose |
|------|--------|
| `.cursor/rules/python.mdc` | Python standards: ruff (format/lint), mypy, pytest, line length 98, double quotes, **uv** for deps. Applies to `**/*.py`. |
| `.cursor/rules/specs-consultation.mdc` | Always consult `docs/specs/` before implementing; create or update specs when code changes; check `docs/adr/` for architecture decisions. |

---

## Skills (`.cursor/skills/`)

Consult when the task matches the description. The AI uses skill descriptions to decide relevance.

| Skill | Path | When to use |
|-------|------|-------------|
| **edit-mermaid-markdown** | `.cursor/skills/edit-mermaid-markdown/SKILL.md` | Mermaid diagrams, flowcharts, sequence diagrams, documenting flows/architecture; fixing Mermaid parse errors in markdown. |
| **python-logger** | `.cursor/skills/python-logger/SKILL.md` | Adding or reviewing logging; avoid `logging.getLogger()` and `self.logger`; use injected logger at method level. |
| **python-uv** | `.cursor/skills/python-uv/SKILL.md` | Running Python, installing dependencies, setting up the venv; project uses `uv` (see `pyproject.toml`, `uv.lock`). |
| **python-fastapi** | `.cursor/skills/python-fastapi/SKILL.md` | Creating or reviewing FastAPI endpoints, use cases, or DTOs; Clean Architecture; `request.app.state.container`, no `Depends()`. |
| **python-postgres-repository** | `.cursor/skills/python-postgres-repository/SKILL.md` | Postgres repositories with SQLAlchemy (sync); session per method via `get_session()`; ORM→entity mapping; domain exceptions. |
| **python-repository** | `.cursor/skills/python-repository/SKILL.md` | Repository pattern: try-except-finally, session injection, commit/rollback, raising domain exceptions from repositories. |
| **mcp** | `.cursor/skills/mcp/SKILL.md` | Adding or moving MCP servers (interface) or clients (infrastructure); integrating with Anthropic/FastMCP. |
| **python-dto-naming** | `.cursor/skills/python-dto-naming/SKILL.md` | DTO naming: use cases → `*Command`/`*Result`; gateways/endpoints → `*Request`/`*Response`. |
| **python-dev-use-case** | `.cursor/skills/python-dev-use-case/SKILL.md` | Implementing or adding a use case; working from specs in `docs/specs/usecases/`; spec-first workflow. |
| **python-exceptions** | `.cursor/skills/python-exceptions/SKILL.md` | Domain exceptions in `service/shared/exceptions.py`; not-found in repositories; mapping exceptions to HTTP in FastAPI. |
| **pytest** | `.cursor/skills/pytest/SKILL.md` | Writing, reviewing, or running tests; `conftest.py`; pytest markers and `parametrize`; project test commands. |

---

## Using this configuration

- **Rules**: Cursor includes rule files in the model context when they match (e.g. `python.mdc` for `.py` files). You can also say: *"Before we start, read all files in .cursor/rules/ and .cursor/skills/."*
- **Skills**: The agent discovers skills from `.cursor/skills/` and uses their descriptions to choose when to read a skill. You can invoke one explicitly in chat with `/skill-name` (e.g. `/python-fastapi`).
- This setup works **when you use Cursor in this repo**: rules and skills under `.cursor/` are picked up by Cursor’s AI so it can follow project conventions and use the documented workflows online during your session.
