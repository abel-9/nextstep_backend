from functools import lru_cache

# Containers
from src.core.container import AppContainer
from src.context.shared_kernel.bootstrap.container import SharedContainer

# Interfaces
from src.context.profile.domain.ports import IProfileRepository
from src.context.profile.application.query.ports import IProfileQuery


# Use Cases
from src.context.profile.application.command.use_case import (
    AddEducationUseCase,
    AddWorkExperienceUseCase,
    CreateProfileUseCase,
)

# Query Handlers
from src.context.profile.application.query.handlers import (
    GetAllEducationsQueryHandler,
    GetAllWorkExperiencesQueryHandler,
    GetEducationQueryHandler,
    GetMyProfileQueryHandler,
    GetWorkExperienceQueryHandler,
)

# Implementations
from src.context.profile.infrastructure.adapters.repository import (
    ProfileBeanieRepository,
)
from src.context.profile.infrastructure.adapters.query import ProfileBeanieQuery


class ProfileContainer:
    def __init__(self, app_container: AppContainer, shared_container: SharedContainer):
        self.app_container = app_container
        self.shared_container = shared_container

    @lru_cache()
    def get_profile_repository(self) -> IProfileRepository:
        return ProfileBeanieRepository()

    @lru_cache()
    def get_profile_query(self) -> IProfileQuery:
        return ProfileBeanieQuery()

    @lru_cache()
    def get_create_profile_use_case(self) -> CreateProfileUseCase:
        return CreateProfileUseCase(profile_repository=self.get_profile_repository())

    @lru_cache()
    def get_add_work_experience_use_case(self) -> AddWorkExperienceUseCase:
        return AddWorkExperienceUseCase(
            profile_repository=self.get_profile_repository(),
            token_service=self.shared_container.get_token_service(),
            message_broker=self.app_container.message_broker,
        )

    @lru_cache()
    def get_add_education_use_case(self) -> AddEducationUseCase:
        return AddEducationUseCase(
            profile_repository=self.get_profile_repository(),
            token_service=self.shared_container.get_token_service(),
            message_broker=self.app_container.message_broker,
        )

    @lru_cache()
    def get_my_profile_query_handler(self) -> GetMyProfileQueryHandler:
        return GetMyProfileQueryHandler(
            token_service=self.shared_container.get_token_service(),
            profile_query=self.get_profile_query(),
        )

    @lru_cache()
    def get_education_query_handler(self) -> GetEducationQueryHandler:
        return GetEducationQueryHandler(
            token_service=self.shared_container.get_token_service(),
            profile_query=self.get_profile_query(),
        )

    @lru_cache()
    def get_all_educations_query_handler(self) -> GetAllEducationsQueryHandler:
        return GetAllEducationsQueryHandler(
            token_service=self.shared_container.get_token_service(),
            profile_query=self.get_profile_query(),
        )

    @lru_cache()
    def get_all_work_experiences_query_handler(
        self,
    ) -> GetAllWorkExperiencesQueryHandler:
        return GetAllWorkExperiencesQueryHandler(
            token_service=self.shared_container.get_token_service(),
            profile_query=self.get_profile_query(),
        )

    @lru_cache()
    def get_work_experience_query_handler(self) -> GetWorkExperienceQueryHandler:
        return GetWorkExperienceQueryHandler(
            token_service=self.shared_container.get_token_service(),
            profile_query=self.get_profile_query(),
        )
