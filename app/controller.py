from __future__ import annotations

from typing import Union

from sqlalchemy.orm import Session

from app.constants import (
    DEFAULT_PAGE_LIMIT,
    SPLITWISE_GET_CURRENT_USER,
    SPLITWISE_GET_CURRENT_USER_FRIENDS,
    SPLITWISE_GET_CURRENT_USER_GROUPS,
    SPLITWISE_GET_EXPENSE,
    SPLITWISE_GET_EXPENSES,
    SPLITWISE_GET_FRIEND,
    SPLITWISE_GET_GROUP,
    SPLITWISE_GET_USER,
)
from app.models import (
    Expense,
    Friend,
    Friends,
    Group,
    Groups,
    User,
)
from db.operations import (
    add_expenses,
    add_user_info,
)
from utils import _make_request


class UserController:
    def get_current_user_information(self) -> User:
        response = _make_request(url=SPLITWISE_GET_CURRENT_USER, method="GET")
        return User(**response.json()["user"])

    def get_user_information(self, user_id: int) -> User:
        response = _make_request(url=f"{SPLITWISE_GET_USER}/{user_id}", method="GET")
        return User(**response.json()["user"])

    def get_current_user_groups(self) -> Groups:
        response = _make_request(url=f"{SPLITWISE_GET_CURRENT_USER_GROUPS}", method="GET")
        return Groups(**response.json())

    def current_user_friends(self) -> Friends:
        response = _make_request(url=SPLITWISE_GET_CURRENT_USER_FRIENDS, method="GET")
        return Friends(**response.json())

    def add_user_to_db(self, session: Session) -> User:
        user_info = self.get_current_user_information()
        return add_user_info(session=session, user=user_info)


class ExpenseController:

    def get_all_expenses(self, params: dict[str, Union[int, str]], unlimited: bool = False) -> list[Expense]:
        cleaned_expenses = []
        expenses = []
        page_limit = int(params.get("limit", DEFAULT_PAGE_LIMIT))

        while True:
            response = _make_request(url=SPLITWISE_GET_EXPENSES, method="GET", params=params)
            interim_expenses = response.json()["expenses"]
            expenses.extend(interim_expenses)
            if not unlimited or len(interim_expenses) == 0:
                break

            # This is used to get all expenses since the beginning of the account
            params["offset"] += page_limit

        for expense in expenses:
            cleaned_expenses.append(Expense(**expense))
        return cleaned_expenses

    def get_expense(self, expense_id: int) -> Expense:
        response = _make_request(f"{SPLITWISE_GET_EXPENSE}/{expense_id}", method="GET")
        return Expense(**response.json()["expense"])

    def add_all_expenses_to_db(self, session: Session, params: dict[str, str], unlimited: bool = False):
        all_user_expenses = self.get_all_expenses(params=params, unlimited=unlimited)
        return add_expenses(session=session, expenses=all_user_expenses)


class GroupController:
    def get_group_info(self, group_id: int) -> Group:
        response = _make_request(url=f"{SPLITWISE_GET_GROUP}/{group_id}", method="GET")
        return Group(**response.json()["group"])


class FriendController:
    def get_friend_info(self, friend_id: int) -> Friend:
        response = _make_request(url=f"{SPLITWISE_GET_FRIEND}/{friend_id}", method="GET")
        return Friend(**response.json()["friend"])
