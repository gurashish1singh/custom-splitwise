from __future__ import annotations

import logging
from typing import (
    Optional,
    Union,
)

from sqlalchemy.orm import Session

from app import models as schema
from db.models import (
    Expense,
    User,
)
from exceptions import EntityExistsError

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)


def add_user_info(session: Session, user: schema.User) -> User:
    existiing_user = read_user_info(session=session, first_name=user.first_name)
    if existiing_user:
        raise EntityExistsError(f"User {user.first_name!r} already exists.")

    user_id = user.id
    user_dict = user.dict()
    user_dict.pop("id")
    user_model = User(user_id=user_id, **user_dict)

    return _add_to_db(session=session, model=user_model)


def read_user_info(session: Session, first_name: int, user_id: Optional[int] = None) -> User:
    user = session.query(User).filter(User.first_name == first_name)
    if user_id:
        user = user.filter(User.user_id == user_id)
    return user.first()


def add_expenses(session: Session, expenses: list[schema.Expense]) -> list[Expense]:
    expense_models = []
    for expense in expenses:
        expense_models.append(add_expense(session=session, expense=expense))
    return expense_models


def add_expense(session: Session, expense: schema.Expense) -> Expense:
    # defaults
    updated_by = None
    deleted_by = None

    expense_id = expense.id
    existing_expense = read_expense(session=session, expense_id=expense_id)
    if existing_expense:
        LOG.warning(f"Expense with id: {expense_id!r} already exists. Skip adding this expense.")
        return existing_expense

    # map nexted structs to top-level
    expense_category = expense.category.name
    created_by = expense.created_by.first_name
    if expense.updated_by:
        updated_by = expense.updated_by.first_name
    if expense.deleted_by:
        deleted_by = expense.deleted_by.first_name

    expense_dict = expense.dict()
    for k in (
        "id",
        "category",
        "created_by",
        "users",  # TODO: create a relationship with users table
    ):
        expense_dict.pop(k)

    # Convert extra vars to model
    expense_model = Expense(**expense_dict)
    expense_model.expense_id = expense_id
    expense_model.category = expense_category
    expense_model.created_by = created_by
    if updated_by:
        expense_model.updated_by = updated_by
    if deleted_by:
        expense_model.deleted_by = deleted_by

    return _add_to_db(session=session, model=expense_model)


def read_expense(session: Session, expense_id: int) -> Expense:
    return session.query(Expense).filter(Expense.expense_id == expense_id).first()


def _add_to_db(session: Session, model: Union[User, Expense]) -> Union[User, Expense]:
    session.add(model)
    session.commit()
    return model
