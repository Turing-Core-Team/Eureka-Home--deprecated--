from typing import Optional

from fastapi import APIRouter

from src.handler.getopportunitiesbyconfig.contract.request import Params
from src.handler.getopportunitiesbyconfig.handler import Handler as HandlerOpportunitiesByDescription

opportunities_router = APIRouter()


@opportunities_router.get("/eureka/opportunities/{description}")
async def opportunities_by_description(description: str, tags: Optional[str] = None):
    params = Params(description, tags)

    return HandlerOpportunitiesByDescription().handler(params)
