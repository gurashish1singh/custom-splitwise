from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    user_id: int
    first_name: str
    last_name: str
    default_currency: Optional[str] = None


class ExpenseResponse(BaseModel):
    id: int
    expense_id: int
    group_id: int
    description: str
    details: Optional[str]
    category: Optional[str]
    cost: float
    currency_code: str
    transaction_method: str
    date: datetime
    created_at: datetime
    created_by: str
    creation_method: str
    updated_at: datetime
    updated_by: Optional[str]
    deleted_at: Optional[datetime]
    deleted_by: Optional[str]
