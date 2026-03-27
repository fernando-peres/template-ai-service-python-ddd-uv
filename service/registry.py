import logging
from functools import lru_cache

import colorlog

from service.settings import Settings

"""
FastAPI application configuration & initialization.
- setup logging
- setup third party loggers
- initialize resources
"""


def setup_third_party_loggers(level: int = logging.INFO) -> None:
    """
    Set up the third party loggers.
    Add the loggers of third-party libraries to the logging
    to default logging level.
    """
    for logger in logging.getLogger().manager.loggerDict:
        logging.getLogger(logger).setLevel(level)


def setup_service_logger(
    level: int = logging.INFO, service_name: str = "service"
) -> logging.Logger:
    """
    Configure root logger so all modules inherit this configuration
    """
    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    handler = colorlog.StreamHandler()
    handler.setFormatter(
        colorlog.ColoredFormatter(
            "%(log_color)s%(levelname)-9s%(reset)s %(message)s",
            log_colors={
                "DEBUG": "blue",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "bold_red",
            },
        )
    )
    root_logger.addHandler(handler)

    logger = logging.getLogger(service_name)
    logger.info(
        "Service logger configured with level: %s and service name: %s", level, service_name
    )
    return logger


class Registry:
    @staticmethod
    def get_logger() -> logging.Logger:
        """
        Get the logger for the service.
        """
        return logging.getLogger(Registry.get_settings().service_name)

    @staticmethod
    @lru_cache(maxsize=1)
    def get_settings() -> Settings:
        return Settings()

    @staticmethod
    def initialize_resources() -> None:
        """
        Register the resources for the application/service.
        """
        settings = Registry.get_settings()
        logger = setup_service_logger(
            level=settings.logger_level,
            service_name=settings.service_name,
        )
        logger.info("Initializing resources...")
        setup_third_party_loggers(level=settings.third_party_loggers_level)
