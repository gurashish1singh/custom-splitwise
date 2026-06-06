FROM python:3.9-slim

RUN pip install --no-cache-dir --upgrade requests python-dotenv pydantic_settings

COPY superset/.env \
    /superset/dashboard/scripts \
    /app/

COPY superset/superset_config.py \
    /app/


CMD [ "python3", "/app/create_dashboard.py"]
