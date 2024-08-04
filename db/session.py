from __future__ import annotations

from functools import lru_cache
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)

from config import settings

engine = create_engine(settings.database_url, pool_pre_ping=True)


def get_session() -> Generator[scoped_session, None, None]:
    Session = create_session()
    try:
        yield Session
    finally:
        Session.remove()


@lru_cache
def create_session() -> scoped_session:
    Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    return Session
