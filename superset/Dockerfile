FROM apache/superset:latest

USER root

RUN pip install mysqlclient pydantic_settings psycopg2

ENV SUPERSET_ADMIN_USERNAME $SUPERSET_ADMIN_USERNAME
ENV SUPERSET_ADMIN_EMAIL $SUPERSET_ADMIN_EMAIL
ENV SUPERSET_ADMIN_PASSWORD $SUPERSET_ADMIN_PASSWORD

COPY ./superset/superset-init.sh ./superset-init.sh

COPY ./superset/superset_config.py \
    config.py   \
    .env \
    /app/

ENV SUPERSET_CONFIG_PATH /app/superset_config.py

USER superset
ENTRYPOINT [ "./superset-init.sh" ]
