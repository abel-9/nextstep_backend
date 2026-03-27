# Queries
from src.context.identity_access.application.query.queries import GetUserByIdQuery

# Read Models
from src.context.identity_access.application.query.read_models import UserReadModel

# Query Repositories
from src.context.identity_access.application.query.ports import IUserQueryRepository


class GetUserByIdQueryHandler:
    def __init__(self, user_query_repository: IUserQueryRepository):
        self._user_query_repository = user_query_repository

    async def __call__(self, query: GetUserByIdQuery) -> UserReadModel | None:
        return await self._user_query_repository.get_by_id(query.user_id)
