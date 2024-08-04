from __future__ import annotations

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class DevSettings(BaseSettings):
    database_url: str
    splitwise_oauth2_api_key: str
    echo_sql: bool = True
    test: bool = True
    project_name: str = "Splitwise Dashboarding"

    model_config = SettingsConfigDict(env_file=".env")


settings = DevSettings()
