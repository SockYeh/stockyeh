"""Module for configuration settings."""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings for the application."""

    DATABASE_URL: str = Field()
    AUTH_SECRET: str = Field()
    SMTP_EMAIL: str = Field()
    SMTP_PASSWORD: str = Field()
    SMTP_HOST: str = Field()
    SMTP_PORT: int = Field()

    model_config = SettingsConfigDict(env_file=".env")


env = Settings()
