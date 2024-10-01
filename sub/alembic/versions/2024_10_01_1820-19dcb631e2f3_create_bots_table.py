"""create bots table

Revision ID: 19dcb631e2f3
Revises: 
Create Date: 2024-10-01 18:20:29.455489

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "19dcb631e2f3"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "bots",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("web_server_host", sa.String(), nullable=False),
        sa.Column("web_server_port", sa.Integer(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("active", sa.Enum("Yes", "No", name="activebot"), nullable=False),
        sa.Column("token_tg", sa.String(), nullable=False),
        sa.Column("bot_username", sa.String(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_bots")),
        sa.UniqueConstraint("token_tg", name=op.f("uq_bots_token_tg")),
        sa.UniqueConstraint("web_server_port", name=op.f("uq_bots_web_server_port")),
    )


def downgrade() -> None:
    op.drop_table("bots")
