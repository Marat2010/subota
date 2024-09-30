import datetime
import enum
from typing import Annotated

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

str_256 = Annotated[str, 256]
created_at = Annotated[datetime.datetime, mapped_column(server_default=func.now())]

updated_at = Annotated[
    datetime.datetime,
    mapped_column(server_default=func.now(), onupdate=datetime.datetime.utcnow),
]


class ActiveBot(enum.Enum):
    Yes = "Да"
    No = "Нет"


class Bot(Base):
    # __tablename__ = 'bot'
    web_server_host: Mapped[str_256] = mapped_column(nullable=False)
    web_server_port: Mapped[int] = mapped_column(nullable=False, unique=True)
    description: Mapped[str_256 | None]
    active: Mapped[ActiveBot] = mapped_column(default="No")
    token_tg: Mapped[str_256] = mapped_column(nullable=False, unique=True)
    bot_username: Mapped[str_256] = mapped_column(nullable=True)
    # url_bwh_id: Mapped[int] = mapped_column(ForeignKey("base_webhook_url.id"))
    # url_bwh: Mapped["BaseWebhookUrlOrm"] = relationship(back_populates="bots")

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
