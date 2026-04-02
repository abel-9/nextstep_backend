# Ports
from src.context.shared_kernel.application.ports import ITokenService

# query Ports
from src.context.profile.application.query.ports import IProfileQuery

# Queries
from src.context.profile.application.query.queries import GetWorkExperienceQuery

# Read models
from src.context.profile.application.query.read_models.profile_read_model import (
    WorkExperience,
)


class GetWorkExperienceQueryHandler:
    def __init__(self, token_service: ITokenService, profile_query: IProfileQuery):
        self.__token_service = token_service
        self.__profile_query = profile_query

    async def __call__(self, query: GetWorkExperienceQuery) -> WorkExperience:
        payload = await self.__token_service.verify(query.token)
        profile = await self.__profile_query.get_by_user_id(user_id=payload.get("sub"))

        if not profile:
            raise Exception("No Profile...")

        for work_experience in profile.work_experiences:
            if work_experience.id == query.work_exp_id:
                return work_experience

        raise Exception("No Work Experience...")  # Ports


from src.context.shared_kernel.application.ports import ITokenService

# query Ports
from src.context.profile.application.query.ports import IProfileQuery

# Queries
from src.context.profile.application.query.queries import GetWorkExperienceQuery

# Read models
from src.context.profile.application.query.read_models.profile_read_model import (
    WorkExperience,
)


class GetWorkExperienceQueryHandler:
    def __init__(self, token_service: ITokenService, profile_query: IProfileQuery):
        self.__token_service = token_service
        self.__profile_query = profile_query

    async def __call__(self, query: GetWorkExperienceQuery) -> WorkExperience:
        payload = await self.__token_service.verify(query.token)
        profile = await self.__profile_query.get_by_user_id(user_id=payload.get("sub"))

        if not profile:
            raise Exception("No Profile...")

        for work_experience in profile.work_experiences:
            if work_experience.id == query.work_exp_id:
                return work_experience

        raise Exception("No Work Experience...")
