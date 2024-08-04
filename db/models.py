from __future__ import annotations

from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, nullable=True)
    email = Column(String)
    default_currency = Column(String, nullable=True)
