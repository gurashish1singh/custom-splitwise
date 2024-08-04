#!/bin/bash
FROM python:3.9

RUN apt-get update \
    && apt-get upgrade -y

RUN mkdir -p /usr/app
WORKDIR /usr/app
COPY . /usr/app
RUN pip install --no-cache-dir -r requirements.txt
