---
name: python-mappers
description: Mapper class conventions for converting between DB models, domain entities, and Response DTOs. Use when creating, updating, or reviewing mapper classes in service/application/mappers.py, or when a entity, model, or *Response DTO field changes.
---

# Mapper Conventions

## Single Source of Truth

All conversions between layers live in `service/application/mappers.py`.  
Never convert between layers outside of this file.

**Trigger:** Whenever an entity, DB model, or `*Response` DTO adds, renames, or removes a field — update the corresponding mapper method(s) in the same change.

---

## Allowed Conversions

| Method | From | To |
|---|---|---|
| `from_model_to_entity` | `*Model` (DB) | Entity |
| `from_entity_to_model` | Entity | `*Model` (DB) |
| `from_entity_to_response` | Entity | `*Response` DTO |

### Forbidden Paths

```
# ❌ DB model → *Response directly (must pass through entity first)
TSAccountMapper.from_model_to_response(model)  # does not exist

# ❌ Entity → *Command (Commands are workflow inputs, never mapped from entities)
TSAccountMapper.from_entity_to_command(entity)  # does not exist
```

---

## Mapper Class Pattern

One mapper class per domain object. All methods are `@staticmethod`.

```python
class TSAccountMapper:
    @staticmethod
    def from_model_to_entity(model: TruthSocialAccountModel) -> TruthSocialAccount:
        return TruthSocialAccount(
            id=model.id,
            username=model.username,
            ...
        )

    @staticmethod
    def from_entity_to_model(entity: TruthSocialAccount) -> TruthSocialAccountModel:
        return TruthSocialAccountModel(
            id=entity.id,
            username=entity.username,
            ...
        )

    @staticmethod
    def from_entity_to_response(entity: TruthSocialAccount) -> TSAccountResponse:
        return TSAccountResponse(
            id=entity.id,
            username=entity.username,
            ...
        )
```

---

## Layer Rules

```
DB Layer       Application Layer     API Layer
----------     -----------------     ---------
*Model    <--> Entity           -->  *Response DTO

*Command  -->  Workflow/UseCase  -->  *Result
(no entity mapping)
```

- `*Command` DTOs are workflow inputs — they contain only what the caller provides (e.g. `message_id`, `prompt`). They are **not** mapped from entities.
- `*Result` DTOs are workflow outputs — map from entity or from aggregated data.
- `*Response` DTOs are API outputs — always mapped from entity, never from model.

---

## Naming

| Class | Maps |
|---|---|
| `TSAccountMapper` | `TruthSocialAccount` ↔ `TruthSocialAccountModel` / `TSAccountResponse` |
| `TSGroupMapper` | `TruthSocialGroup` ↔ `TruthSocialGroupModel` / `TSGroupResponse` |
| `TSPredictionEventMapper` | `TruthSocialPredictionEvent` ↔ model / response |

---

## Adding a New `*Response` DTO

When a new `*Response` DTO is defined, add `from_entity_to_response` to the corresponding mapper:

```python
# service/application/dtos.py
class TSAccountResponse:
    id: str
    username: str
    display_name: str
    s3_avatar_url: str
    s3_banner_url: str

# service/application/mappers.py
class TSAccountMapper:
    @staticmethod
    def from_entity_to_response(entity: TruthSocialAccount) -> TSAccountResponse:
        dto = TSAccountResponse()
        dto.id = entity.id
        dto.username = entity.username
        dto.display_name = entity.display_name
        dto.s3_avatar_url = entity.s3_avatar_url
        dto.s3_banner_url = entity.s3_banner_url
        return dto
```
