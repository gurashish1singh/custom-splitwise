from __future__ import annotations

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)

class DevSettings(BaseSettings):
    database_url: str
    superset_secret_key: str
    superset_admin_username: str
    superset_admin_email: str
    superset_admin_password: str
    superset_table_row_limit: int
    superset_port: int
    echo_sql: bool = True
    test: bool = True

    model_config = SettingsConfigDict(env_file=".env")


settings = DevSettings()

ROW_LIMIT = settings.superset_table_row_limit
SECRET_KEY = settings.superset_secret_key
# ONLY FOR DEV!!!
WTF_CSRF_ENABLED = False
