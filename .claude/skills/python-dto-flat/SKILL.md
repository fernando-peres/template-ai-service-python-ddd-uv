---
name: dto
description: DTO (Data Transfer Objects) definitions. Enforces DTO naming conventions: workflows use *Command/*Result, gateways and HTTP endpoints use *Request/*Response. Use when creating, renaming, or reviewing DTOs in application/, infrastructure/gateway/, or api/interfaces/ layers.
---

# DTO Folder/File

## DTO Location

All DTOs live in `service/application/dtos.py`.  
All DTOs live in the **same file** (flat), separated by sections.

```python
# -----------------------------------------------------------------------------
# Workflow and Use Case DTOs — input to workflows/use cases
# -----------------------------------------------------------------------------
...

# -----------------------------------------------------------------------------
# Result DTOs — output from workflows/use cases
# -----------------------------------------------------------------------------
...

# -----------------------------------------------------------------------------
# Response DTOs — output from API endpoints and external gateways
# -----------------------------------------------------------------------------
...

# -----------------------------------------------------------------------------
# Request DTOs — input to API endpoints and external gateways
# -----------------------------------------------------------------------------
...
```

---

# DTO Naming Conventions

The naming suffix is determined by **where the DTO is used**, not where it is stored.

## Rules

| Layer | Input DTO | Output DTO |
|---|---|---|
| Workflows / Use Cases (`application/workflows/`, `application/usecases/`) | `*Command` | `*Result` |
| Gateways (`infrastructure/gateway/`) | `*Request` | `*Response` |
| Endpoints (`api/` or `interfaces/`) | `*Request` | `*Response` |

---

## Workflow and Use Case DTOs

```python
class CreateTSAccountImagesCommand:
    message_id: str | None
    account_id: str | None
    category: str
    sub_category: str
    account_name: str
    account_bio: str
    prompt: str | None

class CreateTSAccountImagesResult:
    account_id: str
    s3_avatar_url: str
    s3_banner_url: str
```

```python
class CreateTSAccountImagesWorkflow:
    def execute(self, command: CreateTSAccountImagesCommand) -> CreateTSAccountImagesResult: ...
```

> **Important:** `*Command` DTOs are **not** mapped from entities — they contain only what the caller explicitly provides. See `python-mappers` skill for conversion rules.

---

## Gateway DTOs

```python
class GetTokenTruthSocialRequest:
    username: str
    password: str

class GetTokenTruthSocialResponse:
    access_token: str
    token_type: str
```

---

## Endpoint / API DTOs

```python
class TSAccountResponse:
    id: str
    username: str
    display_name: str
    s3_avatar_url: str
    s3_banner_url: str
```

---

## Anti-Patterns

```python
# ❌ WRONG — workflow DTOs named like gateway/endpoint DTOs
class CreateTSAccountImagesRequest: ...   # must be *Command
class CreateTSAccountImagesResponse: ...  # must be *Result

# ❌ WRONG — gateway DTOs named like workflow DTOs
class GetTokenTruthSocialCommand: ...  # must be *Request
class GetTokenTruthSocialResult: ...   # must be *Response

# ❌ WRONG — mapping a *Command from an entity (see python-mappers skill)
TSAccountMapper.from_entity_to_command(entity)
```
