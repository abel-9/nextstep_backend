# Ports
from src.context.shared_kernel.application.ports import ITokenService

# query Ports
from src.context.profile.application.query.ports import IProfileQuery

# Queries
from src.context.profile.application.query.queries import GetAllWorkExperiencesQuery

# Read models
from src.context.profile.application.query.read_models.profile_read_model import (
    WorkExperience,
)


class GetAllWorkExperiencesQueryHandler:
    def __init__(self, token_service: ITokenService, profile_query: IProfileQuery):
        self.__token_service = token_service
        self.__profile_query = profile_query

    async def __call__(self, query: GetAllWorkExperiencesQuery) -> list[WorkExperience]:
        payload = await self.__token_service.verify(query.token)
        profile = await self.__profile_query.get_by_user_id(user_id=payload.get("sub"))

        if not profile:
            raise Exception("No Profile...")

        return profile.work_experiences
