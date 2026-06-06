FROM apache/superset:latest

USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
    pkg-config \
    default-libmysqlclient-dev \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN /app/.venv/bin/python -m ensurepip --upgrade
RUN /app/.venv/bin/python -m pip install --upgrade pip
RUN /app/.venv/bin/python -m pip install --no-cache-dir mysqlclient psycopg2 pydantic-settings


RUN apt-get remove -y gcc \
    && apt-get autoremove -y

COPY superset/superset-init.sh ./superset-init.sh
COPY superset/superset_config.py \
    superset/.env \
    /app/

ENV SUPERSET_CONFIG_PATH=/app/superset_config.py

USER superset
ENTRYPOINT [ "./superset-init.sh" ]
