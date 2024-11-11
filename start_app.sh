#!/bin/bash
set -eou pipefail

PORT=${1-80}

start_app()
{

    echo "Starting dev fastapi app on port $PORT"
    # have docker run the app on input port
    fastapi dev --port $PORT --host 0.0.0.0
    echo
}

activate_venv()
{
    echo "Activating virtual environment"
    if [ -d ".venv/Scripts/" ]; then
        source .venv/Scripts/activate
    fi

    if [ -d ".venv/bin/" ]; then
        source .venv/bin/activate
    fi
}

activate_venv
start_app
