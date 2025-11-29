"""Docstring for shared_library."""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    """App Configuration."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="app_",
        env_nested_max_split=1,
        env_nested_delimiter="_",
        env_parse_enums=True,
        case_sensitive=False,
        extra="ignore",
    )

    log_level: int | str = Field(
        default="INFO", description="Logging level for the application", frozen=True
    )


__all__ = ["AppConfig"]
