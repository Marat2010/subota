from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.models import bot, db_helper
from core.schemas.bots import BotRead, BotCreate
from crud import bots as bots_crud

router = APIRouter(tags=["Bots"])


@router.get("", response_model=list[BotRead])
async def get_bots(
    # session: AsyncSession = Depends(db_helper.session_getter),
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    bots = await bots_crud.get_all_bots(session=session)
    return bots


@router.post("", response_model=BotRead)
async def create_bot(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    bot_create: BotCreate,
):
    bot = await bots_crud.create_bot(session=session, bot_create=bot_create)
    return bot
