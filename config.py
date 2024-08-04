from __future__ import annotations

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class DevSettings(BaseSettings):
    database_url: str
    splitwise_oauth2_api_key: str
    superset_secret_key: str
    superset_admin_username: str
    superset_admin_email: str
    superset_admin_password: str
    superset_table_row_limit: str
    echo_sql: bool = True
    test: bool = True
    project_name: str = "Splitwise Dashboarding"

    model_config = SettingsConfigDict(env_file=".env")


settings = DevSettings()
