# Custom Splitwise Dashboard API

A custom wrapper over Splitwise API to create charts and better visualize expenses built using FastAPI and Pydantic.

## Usage

### Installation

#### Initial setup
    - Create a .env file: `touch .env`
        - It is imperative that you register your app on splitwise and get the API token (OAuth2 onwards):
            - API key (Store in .env file as SPLITWISE_OAUTH2_API_KEY)
        - Store DATABASE_URL in the .env file
    - Create a local.env file under the db package: `touch db/local.env`
        - Put the db credentials that you would be using to interact with locally:
            - POSTGRES_USER
            - POSTGRES_PASSWORD
            - POSTGRES_DB
    - Create a Python virtualenv using `python3 -m venv .venv`
    - Activate the environment using `source .venv/bin/activate`

#### Local testing
    - Run `bash local_setup.sh`
        - This installs all requirements, commit hooks, and starts the app in dev mode

#### Docker testing
    - Ensure docker engine is installed and running. Follow the steps: https://docs.docker.com/engine/install/
    - Run the bash file: `bash run.sh`
        - This will run the app within the docker continer that can be accessed by going to `http://localhost:80/docs`
        - The pgadmin UI can be access by going to `http://localhost:50/`
            - Login email and password are given in the docker-compose file
