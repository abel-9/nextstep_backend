# mediators
from src.core.mediator import request_bus

# Queries
from src.context.identity_access.application.query.queries import GetUsersQuery

# Read Models
from src.context.identity_access.application.query.read_models import UserReadModel

# Query Repositories
from src.context.identity_access.application.query.ports import IUserQueryRepository


class GetUsersQueryHandler:
    def __init__(self, user_query_repository: IUserQueryRepository):
        self._user_query_repository = user_query_repository

    async def __call__(self, query: GetUsersQuery) -> list[UserReadModel]:
        users = await self._user_query_repository.get_all(query)
        return users
