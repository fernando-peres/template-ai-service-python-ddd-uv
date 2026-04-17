from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from service.interface.api import health_router
from service.shared import ColorPalette as CP
from service.shared import ServiceRegistry as SR
from service.shared import get_logger


def create_service() -> FastAPI:
    """
    Create the FastAPI application with configured lifespan and routes.
    This function sets up the application lifecycle, including resource initialization
    and cleanup, and includes the necessary API routes.
    """

    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
        """
        Lifespan context manager for FastAPI application.
        Lazy load: initialize shared resources here in the future.
        """
        SR.initialize_resources()
        logger = get_logger()
        logger.info("✅ Service is ready to accept requests")
        print(f"{CP.PRIMARY}─" * 80 + f" {CP.RESET}")
        yield
        SR.cleanup_resources()
        logger.info("🧹 Service resources cleaned up successfully")
        print("")

    app = FastAPI(lifespan=lifespan)
    app.include_router(health_router)

    return app


create_service()
