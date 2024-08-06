from __future__ import annotations

from config import settings

ROW_LIMIT = settings.superset_table_row_limit
SECRET_KEY = settings.superset_secret_key
# ONLY FOR DEV!!!
WTF_CSRF_ENABLED = False
