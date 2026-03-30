# Ports
from src.context.shared_kernel.application.ports import ITokenService

# query Ports
from src.context.profile.application.query.ports import IProfileQuery

# Queries
from src.context.profile.application.query.queries import GetMyProfileQuery

# Read models
from src.context.profile.application.query.read_models import ProfileReadModel


class GetMyProfileQueryHandler:
    def __init__(self, token_service: ITokenService, profile_query: IProfileQuery):
        self.__token_service = token_service
        self.__profile_query = profile_query

    async def __call__(self, query: GetMyProfileQuery) -> ProfileReadModel:
        payload = await self.__token_service.verify(query.token)
        profile = await self.__profile_query.get_by_user_id(user_id=payload.get("sub"))
        return profile
