from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Bot
from core.schemas.bots import BotCreate


async def get_all_bots(session: AsyncSession) -> Sequence[Bot]:
    stmt = select(Bot).order_by(Bot.id)
    result = await session.scalars(stmt)
    return result.all()


async def create_bot(session: AsyncSession, bot_create: BotCreate) -> Bot:
    bot = Bot(**bot_create.model_dump())
    session.add(bot)
    await session.commit()
    # await session.refresh(bot)
    return bot
