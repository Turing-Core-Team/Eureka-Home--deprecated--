from abc import abstractmethod, ABCMeta
from typing import List

from internal.opportunities.core.entity.opportunities import Opportunities
from internal.opportunities.core.query.get_config import GetConfig
from src.handler.getopportunitiesbyconfig.contract.request import Params


class UseCaseInterface(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, query: GetConfig) -> List[Opportunities]:
        pass


class MapperInterface(metaclass=ABCMeta):
    @abstractmethod
    def request_to_query(self, request_params: Params) -> GetConfig:
        pass