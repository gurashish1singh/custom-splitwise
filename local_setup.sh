#!/bin/bash
set -eou pipefail

PRETTY_LINES=$(printf "=%.0s" {1..80})

msg()
{
    echo "$PRETTY_LINES"
    echo "$1"
    echo "$PRETTY_LINES"
    echo
}

setup_env()
{
    msg "Setting up local development environment"
    install_and_activate_venv
    msg "Installing pacakages"
    pip3 install --no-cache-dir -r requirements.txt
    msg "Created a new virtualenv, activated it and installed all necessary packages"
    echo
}

install_and_activate_venv()
{
    msg "Creating and activating virtual environment"
    python3 -m venv .venv
    if [ -d ".venv/Scripts/" ]; then
        source .venv/Scripts/activate
    fi

    if [ -d ".venv/bin/" ]; then
        source .venv/bin/activate
    fi
}

setup_pre_commit()
{
    msg "Installing pre-commit hooks"
    pre-commit install --hook-type pre-commit --hook-type pre-push
    msg "Finished installing hooks"
    echo
}

copy_env_files()
{
    msg "Copying example env files"
    if [ ! -f .env ]; then
        cp .env.example .env
    fi
    if [ ! -f ./db/local.env ]; then
        cp ./db/local.env.example ./db/local.env
    fi
    msg "Copied example env files. Please update both .env and ./db/local/.env files."
}

msg "Starting project setup"
setup_env
setup_pre_commit
copy_env_files
