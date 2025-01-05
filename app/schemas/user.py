from __future__ import annotations

# from datetime import datetime
from typing import Optional

from pydantic import BaseModel  # AliasChoices,; Field,


class BaseUser(BaseModel):
    id: int
    first_name: str
    last_name: Optional[str]

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
