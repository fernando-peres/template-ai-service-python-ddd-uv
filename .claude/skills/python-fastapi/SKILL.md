---
name: python-fastapi
description: FastAPI backend architecture rules: Clean Architecture layering, three-layer DTO separation, request-to-command mapping, dependency injection via app.state.container (never Depends). Use when creating or reviewing FastAPI endpoints, use cases, or DTO structures.
---

# FastAPI Backend Architecture

## Core Principles

- **Dependency Flow**: Endpoints → Use Cases → Repositories
- **Container access**: `request.app.state.container` — never `Depends()`
- **DTO isolation**: Domain entities never exposed to the HTTP layer

## Three-Layer DTO Separation

| Layer | Files | Types |
|---|---|---|
| HTTP | `requests.py`, `responses.py` | `*Request`, `*Response` |
| Application | `commands_queries.py`, `results.py` | `*Command`, `*Query`, `*Result` |
| Domain | `domain/entities/` | Internal entities only |

## Complete Request Flow

```
HTTP Request (*Request)
  ↓ map to
Command or Query (*Command / *Query)
  ↓ use case executes
Result DTO (*Result)
  ↓ map to
HTTP Response (*Response)
```

## Endpoint Pattern

```python
@router.post("/users", response_model=UserResponse, status_code=201)
async def create_user(payload: CreateUserRequest, request: Request):
    container = request.app.state.container

    # Map HTTP → Command
    command = CreateUserCommand(email=payload.email, name=payload.name)

    # Execute use case
    try:
        user_dto = await CreateUserUseCase(container.user_repository()).execute(command)
    except DomainValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except EntityNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

    # Map Result → Response
    return UserResponse(**user_dto.model_dump())
```

## HTTP Methods & Status Codes

```python
@router.post("/users", status_code=201)        # Create
@router.get("/users/{id}")                     # Read single
@router.get("/users")                          # Read list
@router.patch("/users/{id}")                   # Partial update
@router.delete("/users/{id}", status_code=204) # Delete
```

## Parameter Naming

```python
async def create_user(payload: CreateUserRequest): ...
async def login(credentials: LoginRequest): ...
async def update_user(updates: UpdateUserRequest): ...
async def list_users(filters: ListUsersRequest): ...
```

## App Bootstrap

```python
def create_app() -> FastAPI:
    app = FastAPI()
    db = Database(settings.DATABASE_URL)
    app.state.container = Container(db)
    return app
```

## Checklist

✅ All DTOs in `application/dtos/`  
✅ Map HTTP requests → commands/queries before use case  
✅ Map use case results → HTTP responses after use case  
✅ Always specify `response_model` and status codes  
✅ Handle domain exceptions → HTTP errors in endpoint  
❌ Never use `Depends()` for use cases or repositories  
❌ Never return domain entities directly from endpoints  
❌ Never put business logic in route handlers  
