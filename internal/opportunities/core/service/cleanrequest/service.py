from typing import List

from internal.opportunities.core.entity.path import Path
from internal.opportunities.core.query.get_config import GetConfig
from internal.opportunities.core.usecase.ports import CleanRequestServiceInterface
from internal.opportunities.infrastructure.getpath.config.process import ProcessPathConfig


class ServiceCleanRequest(CleanRequestServiceInterface):
    path_config = ProcessPathConfig()

    def create_request(self, query: GetConfig) -> List[Path]:
        return self.path_config.get(query)
