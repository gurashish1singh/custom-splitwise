from __future__ import annotations

from typing import Any

from fastapi import (
    FastAPI,
)

from controller import (
    ExpenseController,
    GroupController,
    FriendController,
    UserController,
)


app = FastAPI()


# User related
@app.get("/user")
async def get_current_user_info():
    controller = UserController()
    return controller.get_current_user_information()


@app.get("/user/{user_id}")
async def get_user_info(user_id: int):
    controller = UserController()
    return controller.get_user_information(user_id=user_id)


# Friend related
@app.get("/get_friends")
async def get_current_user_friends():
    controller = UserController()
    return controller.current_user_friends()


@app.get("/get_friend/{friend_id}")
async def get_friend_info(friend_id: int):
    controller = FriendController()
    return controller.get_friend_info(friend_id=friend_id)


# Group related
@app.get("/get_groups")
async def get_current_user_groups():
    controller = UserController()
    return controller.get_current_user_groups()


@app.get("/get_group/{group_id}")
async def get_group_info(group_id: int):
    controller = GroupController()
    return controller.get_group_info(group_id=group_id)


# Expense related
@app.get("/expense")
async def get_user_expenses(params: dict[str, Any] = {}):
    controller = ExpenseController()
    return controller.get_all_expenses(params=params)


@app.get("/expense/{expense_id}")
async def get_expense(expense_id: int):
    controller = ExpenseController()
    return controller.get_expense(expense_id=expense_id)
