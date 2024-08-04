from __future__ import annotations

from typing import Optional

from fastapi import (
    Depends,
    FastAPI,
)
from sqlalchemy.orm import Session

from app.controller import (
    ExpenseController,
    FriendController,
    GroupController,
    UserController,
)
from app.models import (
    Expense,
    Friend,
    Friends,
    Group,
    Groups,
    User,
)
from app.response import (
    ExpenseResponse,
    UserResponse,
)
from db.session import get_session

app = FastAPI()


# User related
@app.get("/user", response_model=User, name="Get current user info from splitwise")
async def get_current_user_info():
    controller = UserController()
    return controller.get_current_user_information()


@app.get("/user/{user_id}", response_model=User, name="Get user info from splitwise")
async def get_user_info(user_id: int):
    controller = UserController()
    return controller.get_user_information(user_id=user_id)


@app.post("/user", response_model=UserResponse, name="Save current user info from splitwise to internal db")
async def save_user_info(session: Session = Depends(get_session)):
    controller = UserController()
    return controller.add_user_to_db(session)


# Friend related
@app.get("/get_friends", response_model=Friends)
async def get_current_user_friends():
    controller = UserController()
    return controller.current_user_friends()


@app.get("/get_friend/{friend_id}", response_model=Friend)
async def get_friend_info(friend_id: int):
    controller = FriendController()
    return controller.get_friend_info(friend_id=friend_id)


# Group related
@app.get("/get_groups", response_model=Groups)
async def get_current_user_groups():
    controller = UserController()
    return controller.get_current_user_groups()


@app.get("/get_group/{group_id}", response_model=Group)
async def get_group_info(group_id: int):
    controller = GroupController()
    return controller.get_group_info(group_id=group_id)


# Expense related
@app.get("/expense", response_model=list[Expense])
async def get_user_expenses(
    group_id: Optional[int] = None,
    friend_id: Optional[int] = None,
    dated_after: Optional[str] = None,
    dated_before: Optional[str] = None,
    updated_after: Optional[str] = None,
    updated_before: Optional[str] = None,
    limit: Optional[str] = 50,
    offset: Optional[str] = 0,
):
    # Group id and friend id are mutually exclusive (only one will be returned)
    params = {
        "group_id": group_id,
        "friend_id": friend_id,
        "dated_after": dated_after,
        "dated_before": dated_before,
        "updated_after": updated_after,
        "updated_before": updated_before,
        "limit": limit,
        "offset": offset,
    }
    # Clean params before passing to splitwise api
    params = {k: v for k, v in params.items() if v is not None}
    controller = ExpenseController()
    return controller.get_all_expenses(params=params)


@app.get("/expense/{expense_id}", response_model=Expense)
async def get_expense(expense_id: int):
    controller = ExpenseController()
    return controller.get_expense(expense_id=expense_id)


@app.post("/expense", response_model=list[ExpenseResponse])
async def add_user_expenses_to_db(
    session: Session = Depends(get_session),
    group_id: Optional[int] = None,
    friend_id: Optional[int] = None,
    dated_after: Optional[str] = None,
    dated_before: Optional[str] = None,
    updated_after: Optional[str] = None,
    updated_before: Optional[str] = None,
    limit: Optional[str] = 50,
    offset: Optional[str] = 0,
):
    # Group id and friend id are mutually exclusive (only one will be returned)
    params = {
        "group_id": group_id,
        "friend_id": friend_id,
        "dated_after": dated_after,
        "dated_before": dated_before,
        "updated_after": updated_after,
        "updated_before": updated_before,
        "limit": limit,
        "offset": offset,
    }
    # Clean params before passing to splitwise api
    params = {k: v for k, v in params.items() if v is not None}
    controller = ExpenseController()
    return controller.add_all_expenses_to_db(session=session, params=params)
