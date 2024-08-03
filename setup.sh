#!/bin/bash
set -eou pipefail

PRETTY_LINES=$(printf "=%.0s" {1..80})

msg()
{
    echo "$PRETTY_LINES"
    echo "$1"
    echo "$PRETTY_LINES"
}

setup_env()
{
    msg "Installing requirements"
    pip3 install --no-cache-dir -r requirements.txt
    msg "Installed all necessary packages"
    echo
}

start_app()
{
    msg "Starting dev fastapi app"
    # have docker run the app on port 80
    fastapi dev --port 80
    echo
}

msg "Starting project setup"
setup_env
start_app
