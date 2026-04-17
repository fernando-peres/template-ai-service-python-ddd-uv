---
name: python-exceptions
description: Custom exception conventions for this project. Use when creating, locating, naming, or raising exceptions in domain/, application/, or interface/ layers. Covers DDD layering rules, file locations, class template, and re-raise vs wrap rules.
---

# Python Exceptions — DDD Layering

## Decision Rule

Ask: "Would this rule/condition still exist in a batch job with no UI and no database?"

- **Yes** → **Domain** exception (`service/domain/exceptions.py`)
- **No** → **Application** exception (`service/application/exceptions.py`)

Never create exceptions in the interface or infra layers — those layers **map** exceptions to HTTP status codes or error responses; they do not define new ones.

---

## File Locations

| Layer | File | Examples |
|---|---|---|
| Domain | `service/domain/exceptions.py` | `InvalidEmail`, `InsufficientFunds`, `OrderAlreadyPaid` |
| Application | `service/application/exceptions.py` | `AccountNotFound`, `GroupNotFound`, `WorkflowStepFailed` |
| Interface | *(no exceptions — only mapping)* | HTTP 404, 409, 400 |

---

## Domain Exceptions

Thrown by **entities, value objects, or domain services** when a business invariant is violated.

```python
# service/domain/exceptions.py

class InvalidEmail(ValueError):
    """Email does not meet format requirements."""

    def __init__(self, email: str) -> None:
        super().__init__(f"Invalid email address: '{email}'.")
        self.email = email


class InsufficientFunds(Exception):
    """Account balance is too low for the requested operation."""

    def __init__(self, available: float, required: float) -> None:
        super().__init__(
            f"Insufficient funds: available={available}, required={required}."
        )
        self.available = available
        self.required = required
```

**Rules:**
- Inherit from `Exception` (or a semantic built-in like `ValueError` for format violations).
- Store relevant fields as instance attributes.
- One-line docstring stating the invariant being enforced.
- Do **not** import from `service/application/` or `service/infra/`.

---

## Application Exceptions

Thrown by **workflows or use cases** when an orchestration concern fails.

```python
# service/application/exceptions.py

# ------------------------------------------------------------
# Account Exceptions
# ------------------------------------------------------------
class AccountNotFound(Exception):
    """Account not found by slug (username) or display_name."""

    def __init__(self, identifier: str) -> None:
        super().__init__(f"Account '{identifier}' not found.")
        self.identifier = identifier


# ------------------------------------------------------------
# Group Exceptions
# ------------------------------------------------------------
class GroupNotFound(Exception):
    """Group not found by slug."""

    def __init__(self, identifier: str) -> None:
        super().__init__(f"Group '{identifier}' not found.")
        self.identifier = identifier
```

**Rules:**
- Group by entity using `# --- Entity Exceptions ---` section comments.
- `*NotFound` exceptions store the identifier used for the lookup.
- `service/application/exceptions.py` is the **single flat file** for all application exceptions.

---

## Naming Conventions

| Concern | Suffix | Example |
|---|---|---|
| Resource not found | `*NotFound` | `AccountNotFound`, `GroupNotFound` |
| Already exists | `*AlreadyExists` | `EventAlreadyExists` |
| Bad data format | `*BadFormat` | `EventBadFormat` |
| Business invariant | descriptive noun phrase | `InsufficientFunds`, `InvalidEmail` |
| Workflow / step failure | `*Failed` | `WorkflowStepFailed` |
| External provider error | `*Failed` / `*Error` | `AIProviderAuthenticationFailed` |

---

## Error Handling Rules

In repositories and workflows, **always** follow this pattern:

```python
try:
    ...
except GroupNotFound:
    raise                               # ✅ re-raise domain/application exceptions as-is
except Exception as exc:
    raise RuntimeError("...") from exc  # ✅ wrap unexpected errors with context
```

```python
# ❌ WRONG — swallows GroupNotFound inside the generic handler
except Exception as exc:
    raise RuntimeError("Unexpected error") from exc  # loses NotFound semantics
```

---

## Interface Layer — Mapping Only

The interface layer (FastAPI routers) does **not** define new exceptions. It maps existing ones to HTTP responses:

```python
# service/interface/api/my_router.py

from fastapi import HTTPException
from service.application.exceptions import GroupNotFound, AccountNotFound

@router.get("/{slug}")
def get_group(slug: str):
    try:
        return service.get_group(slug)
    except GroupNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc))
```

Common mappings:

| Exception | HTTP Status |
|---|---|
| `*NotFound` | 404 |
| `*AlreadyExists` | 409 |
| `*BadFormat` / `InvalidEmail` | 400 |
| `InsufficientFunds` | 409 |
| `AIProviderAuthenticationFailed` | 502 |

---

## Checklist — Adding a New Exception

- [ ] Classify: domain invariant or application orchestration concern?
- [ ] Domain → add to `service/domain/exceptions.py`
- [ ] Application → add to `service/application/exceptions.py` under the correct section comment
- [ ] Inherit from `Exception` (or `ValueError` for format violations)
- [ ] Store relevant fields as `self.*` instance attributes
- [ ] Write a one-line docstring describing the violation
- [ ] In repositories: re-raise the exception, do not wrap it in `RuntimeError`
- [ ] In the interface layer: map to HTTP status, do not define new exceptions
