# Custom Splitwise Dashboard API

A custom wrapper over Splitwise API to create charts and better visualize expenses built using FastAPI and Pydantic.

## Usage

### Installation

#### Initial setup
    - Run `source local_setup.sh`. This script:
        - installs a vritual python environment and activates it
        - installs all requirements and commit hooks
        - creates env files
    - Update .env file with the following
        - SPLITWISE_OAUTH2_API_KEY: str
            - It is imperative that you register your app on splitwise and get the API token (OAuth2 onwards)
        - DATABASE_URL: str
        - SUPERSET_SECRET_KEY: str
        - SUPERSET_ADMIN_USERNAME: str
        - SUPERSET_ADMIN_EMAIL: str
        - SUPERSET_ADMIN_PASSWORD: str
        - SUPERSET_TABLE_ROW_LIMIT: int
        - SUPERSET_PORT: int
    - Update db/local.env file
        - Put the db credentials that you would be using to interact with locally:
            - POSTGRES_USER
            - POSTGRES_PASSWORD
            - POSTGRES_DB

#### Local testing
    - Run `bash start_app.sh`. This script:
        - assumes user has run `source local_setup.sh`
        - can be run with an optional PORT number (defaults to 80)
    - Local app run will be available at `http://localhost:80/docs`

#### Docker testing
    - Ensure docker engine is installed and running. Follow the steps: https://docs.docker.com/engine/install/
    - Run the bash file: `bash run.sh`
        - This will run the app within the docker continer that can be accessed by going to `http://localhost:8000/docs`
        - Superset UI will be available at `http://localhost:8088`
        - The pgadmin UI can be access by going to `http://localhost:5050/`
            - Login email and password are given in the docker-compose file
