from __future__ import annotations

import click
from dotenv import load_dotenv

from constants import (
    SPLITWISE_GET_EXPENSES,
    SPLITWISE_GET_USER,
)
from models import (
    Expense,
    User,
)
from utils import (
    _get_api_key,
    _make_request,
)

# Load env file
load_dotenv()


@click.group()
def cli():
    ...


@cli.command("user")
def get_current_user() -> None:
    click.secho("Getting information about current user")
    response = _make_request(SPLITWISE_GET_USER, method="GET", api_key=_get_api_key())
    user = User(**response.json()["user"])
    click.secho(user, fg="cyan")


@cli.command("expenses")
def get_all_expenses() -> None:
    click.secho("Getting all epxenses for the current user")
    response = _make_request(SPLITWISE_GET_EXPENSES, method="GET", api_key=_get_api_key())
    # Limit of 20 from server
    all_expenses = response.json()["expenses"]
    for i, expense in enumerate(all_expenses, start=1):
        click.secho(f"Expense number {i}", fg="green")
        expense_model = Expense(**expense)
        click.secho(expense_model, fg="yellow")


if __name__ == "__main__":
    cli()
