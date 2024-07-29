from __future__ import annotations

from typing import Any

from fastapi import FastAPI

from controller import (
    ExpenseController,
    UserController,
)

app = FastAPI()


@app.get("/user")
async def get_current_user_info():
    controller = UserController()
    return controller.get_current_user_information()


@app.get("/user/{user_id}")
async def get_user_info(user_id: int):
    controller = UserController()
    return controller.get_user_information(user_id=user_id)


@app.get("/expense")
async def get_user_expenses(params: dict[str, Any] = {}):
    controller = ExpenseController()
    return controller.get_all_expenses(params=params)


@app.get("/expense/{expense_id}")
async def get_expense(expense_id: int):
    controller = ExpenseController()
    return controller.get_expense(expense_id=expense_id)
