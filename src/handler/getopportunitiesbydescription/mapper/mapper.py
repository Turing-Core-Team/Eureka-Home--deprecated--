from abc import ABC

from internal.opportunities.core.query.get_request import GetRequest
from src.handler.getopportunitiesbydescription.contract.request import Params
from src.handler.getopportunitiesbydescription.ports import MapperInterface


class Mapper(MapperInterface, ABC):
    def request_to_query(self, request_params: Params) -> GetRequest:
        return GetRequest(
            request_params.description,
            request_params.tags,
        )