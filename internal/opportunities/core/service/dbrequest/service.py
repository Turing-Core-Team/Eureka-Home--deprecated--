from typing import List

from internal.opportunities.core.entity.opportunities import Opportunities
from internal.opportunities.core.entity.path import Path
from internal.opportunities.core.usecase.ports import GetopportunitiesServiceInterface
from internal.opportunities.infrastructure.request.process import Processopportunities


class ServiceRequest(GetopportunitiesServiceInterface):
    request_service = Processopportunities()

    def get_opportunities(self, path: List[Path]) -> List[opportunities]:
        # TODO mirar otras opciones por rendimiento
        # TODO límite de request por response
        # TODO as list comprehension para multiples paths

        # TODO utilizar yield para mejorar rendimiento
        # TODO Try cathc

        opportunities = []
        for single_path in path:
            if self.request_service.validate_url(single_path.base_url):
                # TODO as a map for saving resources
                opportunities.append(self.request_service.get(single_path))
            else:
                # TODO catch error
                pass

        return opportunities