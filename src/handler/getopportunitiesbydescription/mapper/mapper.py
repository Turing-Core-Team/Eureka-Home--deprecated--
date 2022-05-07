from abc import ABC

from internal.opportunities.core.query.get_config import GetConfig
from src.handler.getopportunitiesbydescription.contract.request import Params
from src.handler.getopportunitiesbydescription.ports import MapperInterface


class Mapper(MapperInterface, ABC):
    def request_to_query(self, request_params: Params) -> GetConfig:
        return GetConfig(
            request_params.language,
            request_params.config_name,
        )