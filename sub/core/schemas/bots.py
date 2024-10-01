from pydantic import BaseModel
from pydantic import ConfigDict

from core.models.bot import ActiveBot


class BotBase(BaseModel):
    web_server_host: str
    web_server_port: int
    description: str
    active: ActiveBot
    token_tg: str
    # url_bwh_id: int


class BotCreate(BotBase):
    pass


class BotRead(BotBase):
    model_config = ConfigDict(from_attributes=True)  # можно не указывать
    id: int


# class UserCreate(UserBase):
#     pass
#
#
# class UserRead(UserBase):
#     model_config = ConfigDict(
#         from_attributes=True,
#     )
#
#     id: int
# ==============================
# = Field(
# ..., description="Токен ТГ, к которому привязан функционал бота"
# )
# = Field(default=1, foreign_key="base_webhook_url.id")


# ==============================
