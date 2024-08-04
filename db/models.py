from __future__ import annotations

from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    Float,
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
    email = Column(String, nullable=True)
    default_currency = Column(String, nullable=True)


class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    expense_id = Column(BigInteger, index=True)
    group_id = Column(BigInteger, index=True)
    description = Column(String)
    details = Column(String, nullable=True)
    category = Column(String, index=True)
    cost = Column(Float)
    currency_code = Column(String, nullable=True)
    transaction_method = Column(String, nullable=True)
    date = Column(DateTime)
    created_at = Column(DateTime, nullable=True)
    created_by = Column(String)
    creation_method = Column(String, nullable=True)
    updated_at = Column(DateTime, nullable=True)
    updated_by = Column(String, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    deleted_by = Column(String, nullable=True)
