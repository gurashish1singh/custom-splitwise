# Custom Splitwise Dashboard API

A custom wrapper over Splitwise API to create charts and better visualize expenses built using FastAPI and Pydantic.

## Usage

### Installation

#### Local testing
    - Create a .env file: `touch .env`
        - It is imperative that you register your app on splitwise and get the API token (OAuth2 onwards):
            - API key (Store in .env file as SPLITWISE_OAUTH2_API_KEY)
    - Create a Python virtualenv using `python3 -m venv .venv`
    - Activate the environment using `source .venv/bin/activate`
    - Run `bash local_setup.sh`
        - This installs all requirements, commit hooks, and starts the app in dev mode

#### Docker testing
    - Ensure docker engine is installed and running. Follow the steps: https://docs.docker.com/engine/install/
    - Run the bash file: `bash run.sh`
        - This will run the app within the docker continer that can be accessed by going to `http://localhost:80/docs`
