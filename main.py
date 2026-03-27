from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from service import get_settings
from service.interface.api import health_router

settings = get_settings()


def create_service() -> FastAPI:
    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
        # Lazyload: initialize shared resources here in the future
        # e.g. app.state.container = build_container(settings)
        yield
        # Teardown: clean up resources here in the future

    app = FastAPI(lifespan=lifespan)
    app.include_router(health_router)

    return app


# if __name__ == "__main__":
#     uvicorn.run(
#         "main:app",
#         host=settings.host_ip,
#         port=settings.port,
#         reload=True,
#     )

create_service()
