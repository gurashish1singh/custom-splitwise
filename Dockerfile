FROM python:3.9

RUN apt-get update \
    && apt-get upgrade -y

COPY . /usr/app/

WORKDIR /usr/app

RUN ls -lah

RUN chmod +x ./setup.sh
ENTRYPOINT ["./setup.sh"]
