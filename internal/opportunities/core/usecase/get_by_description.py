from typing import List

from internal.opportunities.core.entity.opportunities import Opportunities
from internal.opportunities.core.query.get_request import GetRequest
from internal.opportunities.core.service.cleanrequest.service import ServiceCleanRequest
from internal.opportunities.core.service.dbrequest.service import ServiceRequest
from src.handler.getopportunitiesbydescription.ports import UseCaseInterface


class UseCaseGetByDescription(UseCaseInterface):
    clean_request = ServiceCleanRequest()
    get_opportunities_service = ServiceRequest()

    def execute(self, query: GetRequest) -> List[Opportunities]:
        request = self.clean_request.create_request(query)
        full_opportunities = self.get_opportunities_service.get_opportunities(request)

        return full_opportunities
