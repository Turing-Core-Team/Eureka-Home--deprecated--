from typing import List

from internal.opportunities.core.entity.opportunities import Opportunities
from internal.opportunities.core.query.get_request import GetOpportunities
from internal.opportunities.core.service.readpath.configfile.service import ServiceGetByConfig
from internal.opportunities.core.service.request.service import ServiceRequest
from src.handler.getopportunitiesbyconfig.ports import UseCaseInterface


class UseCaseGetByConfig(UseCaseInterface):

    get_config_service = ServiceGetByConfig()
    get_opportunities_service = ServiceRequest()

    def execute(self, query: GetOpportunities) -> List[Opportunities]:

        paths = self.get_config_service.get_path(query)
        full_opportunities = self.get_opportunities_service.get_opportunities(paths)

        return full_opportunities