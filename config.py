from __future__ import annotations

from pydantic_settings import BaseSettings


class DevSettings(BaseSettings):
    database_url: str
    echo_sql: bool = True
    test: bool = False
    project_name: str = "Splitwise dashboarding"
    oauth_token_secret: str = "my_dev_secret"


settings = DevSettings()
