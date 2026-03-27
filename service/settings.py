from functools import lru_cache

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


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
