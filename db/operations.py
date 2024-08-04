from __future__ import annotations

from sqlalchemy.orm import Session

from app import models as schema
from db.models import User


def add_user_info(session: Session, user: schema.User) -> User:
    user_id = user.id
    user_dict = user.dict()
    user_dict.pop("id")
    user = User(user_id=user_id, **user_dict)

    session.add(user)
    session.commit()
    return user
