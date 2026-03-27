from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from service import Settings
from service.interface.api import health_router
from service.shared.registry import ServiceRegistry as SR

settings = Settings()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    # Lazyload: initialize shared resources here in the future
    SR.initialize_resources()
    logger = SR.get_logger()
    logger.info("Service is starting up...")
    yield
    # Teardown: clean up resources here in the future


app = FastAPI(lifespan=lifespan)
app.include_router(health_router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.host_ip,
        port=settings.port,
        reload=True,
    )
