#!bin/bash

set -eou pipefail

function cleanup(){
    docker-compose stop
    docker-compose down -v
}

trap cleanup EXIT

docker-compose -f docker-compose.yml up -d --build

read -n1 -rsp $'\nPress any key to exit....\n'
