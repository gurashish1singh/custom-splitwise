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

setup_pre_commit()
{
    msg "Installing pre-commit hooks"
    pre-commit install --hook-type pre-commit --hook-type pre-push
    msg "Finished installing hooks"
    echo
}

start_app()
{
    msg "Starting dev fastapi app"
    # have docker run the app on port 80
    fastapi dev --port 8000 --host 0.0.0.0
    echo
}

msg "Starting project setup"
setup_env
setup_pre_commit
start_app
