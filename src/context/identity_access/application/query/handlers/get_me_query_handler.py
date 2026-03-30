# ports
from src.context.shared_kernel.application.ports import ITokenService
from src.context.identity_access.application.query.ports import IUserQueryRepository

# Query
from src.context.identity_access.application.query.queries import GetMeQuery


class GetMeQueryHandler:
    def __init__(
        self, user_query_repository: IUserQueryRepository, token_service: ITokenService
    ):
        self.__token_service = token_service
        self.__user_query_repository = user_query_repository

    async def __call__(self, query: GetMeQuery):
        payload = await self.__token_service.verify(query.token)
        user = await self.__user_query_repository.get_by_id(payload.get("sub"))

        return user
