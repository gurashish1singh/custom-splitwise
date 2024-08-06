FROM python:3.9-slim

RUN pip install --no-cache-dir --upgrade requests python-dotenv

COPY .env \
    /superset/dashboard/ \
    ./

CMD [ "python3", "/scripts/create_dashboard.py"]
