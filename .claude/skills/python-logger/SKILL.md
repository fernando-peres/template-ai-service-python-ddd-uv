---
name: python-logger
description: Logger injection conventions for this project. Use when adding logging to any class or method, or when reviewing code that uses logging.getLogger() or self.logger (both are forbidden patterns).
---

# Logger Injection

## Rule

**Always inject the logger at the method level. Never store it as a class attribute.**

```python
from service.shared import ServiceRegistry

class MyService:
    async def connect(self) -> None:
        logger = ServiceRegistry.get_logger()
        try:
            self.connection = await create_connection()
            logger.info("Connected successfully")
        except Exception as e:
            logger.error(f"Connection failed: {e}", exc_info=True)
            raise

    async def process(self, data: dict) -> None:
        logger = inject(ResourceName.LOGGER)
        logger.debug(f"Processing: {data}")
        logger.info("Done")
```

## Forbidden Patterns

```python
# ❌ WRONG — logger as class attribute
class MyService:
    def __init__(self) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)

    async def process(self) -> None:
        self.logger.info("message")  # WRONG

# ❌ WRONG — direct logging.getLogger()
async def process(self) -> None:
    logger = logging.getLogger(__name__)  # WRONG
    logger.info("message")
```

## Checklist

- [ ] `logger = inject(ResourceName.LOGGER)` at the top of each logging method
- [ ] Imports: `from service.shared.registry import inject` and `from service.shared.vocabulary import ResourceName`
- [ ] No `self.logger` anywhere
- [ ] No `logging.getLogger()` anywhere
- [ ] Logger is never passed as a parameter
