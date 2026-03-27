# Skill: python-logger

## When to use
Adding or reviewing logging in any Python file; checking whether logger usage follows project conventions.

---

## Rules

### 1. Never call `logging.getLogger()` in service/domain code
Direct calls to `logging.getLogger()` outside of `Registry` couple the module to the logging infrastructure and make the logger available before it has been configured.

**Wrong:**
```python
# module level
logger = logging.getLogger(__name__)

class MyService:
    def do_something(self) -> None:
        logger.info("doing something")
```

**Wrong:**
```python
class MyService:
    self.logger = logging.getLogger(__name__)  # class attribute
```

### 2. Never store a logger as a class attribute (`self.logger`)
Logger state is global; there is no benefit to holding a reference on `self`. It also makes it harder to see when the logger was configured.

### 3. Obtain the logger at method level, after resources are initialized
The logger must be fetched **inside** the method that uses it, and only after `Registry.initialize_resources()` has been called. This guarantees the logger is fully configured (handlers, formatters, level) before first use.

**Correct:**
```python
def my_function() -> None:
    logger = Registry.get_logger()
    logger.info("doing something")
```

**Correct (FastAPI lifespan):**
```python
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    Registry.initialize_resources()   # configure logging first
    logger = Registry.get_logger()    # then obtain the logger
    logger.info("Service is starting up...")
    yield
```

### 4. `Registry` is the only place allowed to call `logging.getLogger()`
`Registry.get_logger()` and the helper functions in `service/registry.py` (`setup_service_logger`, `setup_third_party_loggers`) are the sole owners of `logging.getLogger()` calls. All other modules must go through `Registry.get_logger()`.

---

## Summary table

| Pattern | Allowed |
|---|---|
| `logging.getLogger()` in domain/service code | No |
| `self.logger = ...` | No |
| Module-level `logger = ...` | No |
| `Registry.get_logger()` inside a method | Yes |
| `logging.getLogger()` inside `service/registry.py` | Yes |