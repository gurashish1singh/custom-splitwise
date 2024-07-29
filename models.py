from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


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
