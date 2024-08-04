from __future__ import annotations

from dotenv import load_dotenv
from sqlalchemy.orm import Session

from app.constants import (
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
from db.operations import add_user_info
from utils import _make_request

# Load env file
load_dotenv()


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

    def add_user_to_db(self, session: Session):
        user_info = self.get_current_user_information()
        return add_user_info(session=session, user=user_info)


class ExpenseController:
    def get_all_expenses(self, params: dict[str, str]) -> list[Expense]:
        response = _make_request(url=SPLITWISE_GET_EXPENSES, method="GET", params=params)
        all_expenses = []
        for expense in response.json()["expenses"]:
            all_expenses.append(Expense(**expense))
        return all_expenses

    def get_expense(self, expense_id: int) -> Expense:
        response = _make_request(f"{SPLITWISE_GET_EXPENSE}/{expense_id}", method="GET")
        return Expense(**response.json()["expense"])


class GroupController:
    def get_group_info(slef, group_id: int) -> Group:
        response = _make_request(url=f"{SPLITWISE_GET_GROUP}/{group_id}", method="GET")
        return Group(**response.json()["group"])


class FriendController:
    def get_friend_info(self, friend_id: int) -> Friend:
        response = _make_request(url=f"{SPLITWISE_GET_FRIEND}/{friend_id}", method="GET")
        return Friend(**response.json()["friend"])
