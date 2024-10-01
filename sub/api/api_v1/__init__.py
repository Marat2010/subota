from fastapi import APIRouter

from core.config import settings

from .bots import router as bots_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(
    bots_router,
    prefix=settings.api.v1.bots,
)
