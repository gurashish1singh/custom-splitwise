from __future__ import annotations

from dotenv import load_dotenv

from constants import (
    SPLITWISE_GET_CURRENT_USER,
    SPLITWISE_GET_EXPENSE,
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


class UserController:

    def get_current_user_information(self) -> User:
        response = _make_request(SPLITWISE_GET_CURRENT_USER, method="GET", api_key=_get_api_key())
        if response.ok:
            return User(**response.json()["user"])
        response.raise_for_status()

    def get_user_information(self, user_id: int) -> User:
        response = _make_request(f"{SPLITWISE_GET_USER}/{user_id}", method="GET", api_key=_get_api_key())
        if response.ok:
            return User(**response.json()["user"])
        response.raise_for_status()


class ExpenseController:

    def get_all_expenses(self, params: dict[str, str]) -> list[Expense]:
        response = _make_request(
            url=SPLITWISE_GET_EXPENSES,
            method="GET",
            api_key=_get_api_key(),
            params=params,
        )
        if response.ok:
            all_expenses = []
            for expense in response.json()["expenses"]:
                all_expenses.append(Expense(**expense))
            return all_expenses
        response.raise_for_status()

    def get_expense(self, expense_id: int) -> Expense:
        response = _make_request(
            f"{SPLITWISE_GET_EXPENSE}/{expense_id}",
            method="GET",
            api_key=_get_api_key(),
        )
        if response.ok:
            return Expense(**response.json()["expense"])
        response.raise_for_status()


class GroupExpenseController:
    def get_group_expenses(slef, group_id: int):
        response = _make_request(
            url=...,
            method="GET",
            api_key=_get_api_key(),
        )
        if response.ok:
            ...
        response.raise_for_status()
