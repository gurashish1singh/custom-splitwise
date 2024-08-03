from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import (
    BaseModel,
    Field,
    AliasChoices,
)


class BaseUser(BaseModel):
    id: int
    first_name: str
    last_name: Optional[str]

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class User(BaseUser):
    email: str
    default_currency: Optional[str] = None


class Balance(BaseModel):
    currency_code: str
    amount: float


class GroupUser(BaseUser):
    email: str
    balance: list[Balance]


class Debt(BaseModel):
    to: int
    from_: int = Field(validation_alias=AliasChoices("from"))
    amount: float
    currency_code: str


class Group(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime
    members: list[GroupUser]
    original_debts: list[Debt]
    simplified_debts: list[Debt]


class Groups(BaseModel):
    groups: list[Group]


class FriendGroup(BaseModel):
    group_id: int
    balance: list[Balance]


class Friend(BaseUser):
    groups: list[FriendGroup]
    balance: list[Balance]
    updated_at: datetime


class Friends(BaseModel):
    friends: list[Friend]


class ExpenseUserMetadata(BaseModel):
    user_id: int
    paid_share: float
    owed_share: float
    net_balance: float
    user: BaseUser


class ExpenseCategory(BaseModel):
    id: int
    name: str


class Expense(BaseModel):
    id: int
    group_id: int
    description: str
    details: Optional[str]
    category: ExpenseCategory
    cost: float
    currency_code: str
    transaction_method: str
    date: datetime
    created_at: datetime
    created_by: BaseUser
    creation_method: str
    updated_at: datetime
    updated_by: Optional[BaseUser]
    deleted_at: Optional[datetime]
    deleted_by: Optional[User]
    users: list[ExpenseUserMetadata]
