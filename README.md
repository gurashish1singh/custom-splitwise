# Splitwise API

Testing splitwise API methods to later build dashboards upon.

## CLI

Created a basic cli using click and pydantic models. Currently only get_user and get_expenses are supported. More methods to come.

## Usage

### Installation

- Create a Python virtualenv using `python3 -m venv .venv`
- Install packages using the requirements file `pip3 install -r requirements.txt`
- Create a .env file: `touch env`
    - It is imperative that you register your app on splitwise and get the following tokens:
        - Consumer Key (Store in .env file as SPLITWISE_CONSUMER_KEY)
        - Consumer Secret (Store in .env file as SPLITWISE_CONSUMER_SECRET)
        - API key (Store in .env file as SPLITWISE_OAUTH2_API_KEY)
- Play around with the CLI using: `python3 main.py`
