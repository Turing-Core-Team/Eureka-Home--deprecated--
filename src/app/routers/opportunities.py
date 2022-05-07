
from fastapi import APIRouter

from src.handler.getopportunitiesbydescription.contract.request import Params
from src.handler.getopportunitiesbydescription.handler import Handler as HandlerOpportunitiesByDescription

opportunities_router = APIRouter()


@opportunities_router.get("/eureka/opportunities/{description}/{tags}")
async def opportunities_by_description(description: str, tags: str):
    params = Params(description, tags)

    return HandlerOpportunitiesByDescription().handler(params)
