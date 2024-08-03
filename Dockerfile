#!/bin/bash
FROM python:3.9

RUN apt-get update \
    && apt-get upgrade -y

# Only copy the reqs and install the dependencies.
# For local development we attach the volume to docker container.
RUN mkdir -p /usr/app
WORKDIR /usr/app
COPY requirements.txt /usr/app
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "fastapi", "dev", "--host=0.0.0.0", "--port=80" ]
