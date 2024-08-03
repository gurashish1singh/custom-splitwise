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
    - Install packages using the requirements file `pip3 install -r requirements.txt`
    - Install pre-commit hooks: `pre-commit install --hook-type pre-commit --hook-type pre-push`
    - Start the local FastAPI app: `fastapi dev`

#### Docker testing
    - Ensure docker engine is installed and running. Follow the steps: https://docs.docker.com/engine/install/
    - Run the bash file: `bash run.sh`
        - This will run the app within the docker continer that can be accessed by going to `http://localhost:80/docs`
