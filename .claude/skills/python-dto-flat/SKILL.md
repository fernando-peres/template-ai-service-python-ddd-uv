---
name: dto
description: DTO (Data Transfer Objects) definitions.
Enforces DTO naming conventions based on context use cases use *Command/*Result, gateways and HTTP endpoints use *Request/*Response. Use when creating, renaming, or reviewing DTOs in application/, infrastructure/gateway/, or api/interfaces/ layers.
---
# DTO Folder/file

## DTO Location

All DTOs live in `/service/application/dto.py`.
Naming is governed by usage context.
All DTOs live in the same file (Flat)

In the file `/service/application/dto.py` separate by sections

```python

#--------------------------------------------------------------------
# Command Use Case or Workflow DTOs (input to use cases)
#--------------------------------------------------------------------
...

#--------------------------------------------------------------------
# Result Use Case or Workflow DTOs (output from use cases)
#--------------------------------------------------------------------
...

#--------------------------------------------------------------------
# Response DTOs for API Endpoints and External Gateways
# (output from endpoints/gateways)
#--------------------------------------------------------------------
...

#--------------------------------------------------------------------
# Requestas DTOs for API Endpoints and External Gateways
# (input to endpoints/gateways)
#--------------------------------------------------------------------
...


```

# DTO Naming Conventions

The naming suffix is determined by **where the DTO is used**, not where it is stored.

## Rules

| Layer | Input DTO | Output DTO |
|---|---|---|
| Use Cases (`application/usecase/`) | `*Command` | `*Result` |
| Gateways (`infrastructure/gateway/`) | `*Request` | `*Response` |
| Endpoints (`api/` or `interfaces/`) | `*Request` | `*Response` |

## Use Case and Workflow DTOs

```python
class CreatePredictionCommand(BaseModel):
    title: str
    description: str

class CreatePredictionResult(BaseModel):
    id: str
    title: str
    created_at: datetime
```

```python
class CreatePredictionUseCase:
    def execute(self, command: CreatePredictionCommand) -> CreatePredictionResult: ...
```

## Gateway DTOs

```python
class GetTokenTruthSocialRequest(BaseModel):
    username: str
    password: str

class GetTokenTruthSocialResponse(BaseModel):
    access_token: str
    token_type: str
```

## Endpoint DTOs

```python
class CreateUserRequest(BaseModel):
    email: EmailStr
    name: str

class CreateUserResponse(BaseModel):
    id: UUID
    email: str
    created_at: datetime
```

## Anti-Patterns

```python
# ❌ WRONG — use case DTOs named like gateway/endpoint DTOs
class CreatePredictionRequest(BaseModel): ...   # must be Command
class CreatePredictionResponse(BaseModel): ...  # must be Result

# ❌ WRONG — gateway DTOs named like use case DTOs
class GetTokenTruthSocialCommand(BaseModel): ...  # must be Request
class GetTokenTruthSocialResult(BaseModel): ...   # must be Response
```


