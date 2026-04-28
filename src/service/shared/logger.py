import copy
import logging

import colorlog

from service.settings import Settings
from service.shared.terminal import ColorPalette as CP

_RESET = "\033[0m"

_LOGGER: logging.Logger | None = None


class _UvicornStyleFormatter(colorlog.ColoredFormatter):
    """
    Formats log levels as `LEVELNAME:     ` matching Uvicorn's output style.
    """

    def format(self, record: logging.LogRecord) -> str:
        record = copy.copy(record)
        separator = " " * (9 - len(record.levelname))
        # _RESET ends the level color so `:` and separator render in white
        record.levelprefix = record.levelname + _RESET + ":" + separator
        return str(super().format(record))


class LoggerSetup:
    @staticmethod
    def setup_third_party_loggers(level: int = logging.INFO) -> None:
        """
        Set up the third party loggers.
        Add the loggers of third-party libraries to the logging
        to default logging level.
        """
        for logger in logging.getLogger().manager.loggerDict:
            logging.getLogger(logger).setLevel(level)

    @staticmethod
    def setup_service_logger() -> None:
        """
        Configure root logger so all modules inherit this configuration
        """
        global _LOGGER
        settings = Settings()

        root_logger = logging.getLogger(name=settings.service_name)
        root_logger.setLevel(settings.logger_level)

        handler = colorlog.StreamHandler()
        handler.setFormatter(
            _UvicornStyleFormatter(
                "%(log_color)s%(levelprefix)s%(reset)s%(message)s",
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

        _LOGGER = logging.getLogger(settings.service_name)
        _LOGGER.info(
            f"Service logger configured with level: {CP.PRIMARY}%s{CP.RESET}",
            logging.getLevelName(settings.logger_level),
        )


def get_logger() -> logging.Logger:
    global _LOGGER
    settings = Settings()
    if _LOGGER is None:
        return logging.getLogger(settings.service_name)
    return _LOGGER
