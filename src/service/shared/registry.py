from __future__ import annotations

import logging

from service.settings import Settings
from service.shared.logger import LoggerSetup, get_logger
from service.shared.terminal import ColorPalette as CP

"""
FastAPI application configuration & initialization.
- setup logging
- setup third party loggers
- initialize resources
"""


class ServiceRegistry:
    def get_XXXX_repository(self) -> None:
        """
        Get the account repository for the service.
        """
        return  # AccountRepositoryFactory.create()

    @staticmethod
    def initialize_resources() -> None:
        """
        Register the resources for the application/service.
        """
        settings = Settings()
        LoggerSetup.setup_third_party_loggers()
        LoggerSetup.setup_service_logger()
        logger = get_logger()
        logger.info(
            f"Third-party loggers set to level: {CP.PRIMARY}%s{CP.RESET}",
            logging.getLevelName(settings.third_party_loggers_level),
        )
        logger.info("Initializing resources...")

    @staticmethod
    def cleanup_resources() -> None:
        """
        Clean up the resources for the application/service.
        """
        pass
