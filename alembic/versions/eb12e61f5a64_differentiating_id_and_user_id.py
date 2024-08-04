"""Differentiating id and user_id

Revision ID: eb12e61f5a64
Revises: b4627881c2e5
Create Date: 2024-08-04 02:29:22.525435

"""

from __future__ import annotations

from typing import (
    Sequence,
    Union,
)

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "eb12e61f5a64"
down_revision: Union[str, None] = "b4627881c2e5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("user_id", sa.Integer(), nullable=True))
    op.create_index(op.f("ix_users_user_id"), "users", ["user_id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_users_user_id"), table_name="users")
    op.drop_column("users", "user_id")
    # ### end Alembic commands ###