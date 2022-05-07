from internal.opportunities.core.entity.opportunities import Opportunities
from internal.opportunities.core.usecase.get_by_config import UseCaseGetByDescription
from src.handler.getopportunitiesbydescription.contract.request import Params
from src.handler.getopportunitiesbydescription.mapper.mapper import Mapper


class Handler:
    mapper = Mapper()
    use_case = UseCaseGetByDescription()

    def handler(self, request_params: Params) -> list[Opportunities]:
        query = self.mapper.request_to_query(request_params)
        return self.use_case.execute(query)
