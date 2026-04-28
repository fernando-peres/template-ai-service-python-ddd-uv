import logging

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    service_name: str = "no-service-name-defined"
    openrouter_api_key: str = ""
    open_ai_key: str = ""
    perplexity_api_key: str = ""
    host_ip: str = "127.0.0.1"
    port: int = 8080
    logger_level: int = logging.INFO
    third_party_loggers_level: int = logging.WARNING

    @field_validator("logger_level", "third_party_loggers_level", mode="before")
    @classmethod
    def parse_log_level(cls, v: str | int) -> int:
        if isinstance(v, str):
            return logging.getLevelNamesMapping()[v.upper()]
        return v
