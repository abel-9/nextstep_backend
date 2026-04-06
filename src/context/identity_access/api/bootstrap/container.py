from functools import lru_cache

# Containers
from src.core.container import AppContainer
from src.context.shared_kernel.bootstrap.container import SharedContainer

from src.context.identity_access.domain.ports import (
    IUserRepository,
    IVerificationRepository,
)
from src.context.identity_access.application.query.ports import IUserQueryRepository
from src.context.identity_access.application.ports import IHashService

from src.context.identity_access.infrastructure.adapters import (
    UserBeanieRepository,
    VerificationBeanieRepository,
    Argon2Hasher,
)
from src.context.identity_access.infrastructure.adapters.queries import (
    MongoUserRepository,
)

from src.context.identity_access.application.command.handlers import (
    EmailVerifiedHandler,
    CreateSessionHandler,
)
from src.context.identity_access.application.command.use_cases import (
    SignUpLocalUseCase,
    SignInLocalUseCase,
    VerifyEmailUseCase,
)
from src.context.identity_access.application.query.handlers import (
    GetUsersQueryHandler,
    GetUserByIdQueryHandler,
    GetMeQueryHandler,
)


class IdentityAccessContainer:
    def __init__(self, app_container: AppContainer, shared_container: SharedContainer):
        self.app_container = app_container
        self.shared_container = shared_container

    @lru_cache()
    def get_user_repository(self) -> IUserRepository:
        return UserBeanieRepository()

    @lru_cache()
    def get_verification_repository(self) -> IVerificationRepository:
        return VerificationBeanieRepository()

    @lru_cache()
    def get_hash_service(self) -> IHashService:
        return Argon2Hasher()

    @lru_cache()
    def get_user_query_repository(self) -> IUserQueryRepository:
        return MongoUserRepository()

    @lru_cache()
    def get_verify_user_handler(self) -> EmailVerifiedHandler:
        return EmailVerifiedHandler(
            user_repository=self.get_user_repository(),
            message_broker=self.app_container.message_broker,
        )

    @lru_cache()
    def get_create_session_handler(self) -> CreateSessionHandler:
        return CreateSessionHandler(
            token_service=self.shared_container.get_token_service()
        )

    @lru_cache()
    def get_sign_up_local_use_case(self) -> SignUpLocalUseCase:
        return SignUpLocalUseCase(
            user_repository=self.get_user_repository(),
            hash_service=self.get_hash_service(),
            verification_repository=self.get_verification_repository(),
        )

    @lru_cache()
    def get_sign_in_local_use_case(self) -> SignInLocalUseCase:
        return SignInLocalUseCase(
            user_repository=self.get_user_repository(),
            hash_service=self.get_hash_service(),
            mediator=self.app_container.mediator,
        )

    @lru_cache()
    def get_verify_email_use_case(self) -> VerifyEmailUseCase:
        return VerifyEmailUseCase(
            verification_repository=self.get_verification_repository(),
            user_repository=self.get_user_repository(),
            message_broker=self.app_container.message_broker,
        )

    @lru_cache()
    def get_users_query_handler(self) -> GetUsersQueryHandler:
        return GetUsersQueryHandler(
            user_query_repository=self.get_user_query_repository()
        )

    @lru_cache()
    def get_user_by_id_query_handler(self) -> GetUserByIdQueryHandler:
        return GetUserByIdQueryHandler(
            user_query_repository=self.get_user_query_repository()
        )

    @lru_cache()
    def get_me_query_handler(self) -> GetMeQueryHandler:
        return GetMeQueryHandler(
            user_query_repository=self.get_user_query_repository(),
            token_service=self.shared_container.get_token_service(),
        )
