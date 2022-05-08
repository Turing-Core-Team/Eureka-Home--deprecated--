from typing import List


from internal.opportunities.core.query.get_request import GetRequest
from internal.opportunities.core.usecase.ports import CleanRequestServiceInterface

from internal.opportunities.infrastructure.cleanrequest.process import ProcessCleanRequest


class ServiceCleanRequest(CleanRequestServiceInterface):
    request = ProcessCleanRequest()

    def create_request(self, query: GetRequest) -> List[Path]:
        return self.request.get(query)
