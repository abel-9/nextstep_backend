from functools import lru_cache
from fastapi import Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from motor.motor_asyncio import AsyncIOMotorDatabase

# Usecases
from src.context.identity_access.application.command.use_cases import (
    SignUpLocalUseCase,
    SignInLocalUseCase,
    VerifyEmailUseCase,
)

# Query Handlers
from src.context.identity_access.application.query.handlers import (
    GetUsersQueryHandler,
    GetUserByIdQueryHandler,
)

# Ports
from src.context.identity_access.domain.ports import (
    IUserRepository,
    IVerificationRepository,
)

# Query Ports
from src.context.identity_access.application.query.ports import IUserQueryRepository

# Application Service Ports
from src.context.identity_access.application.ports import (
    IHashService,
    ITokenService,
)

# adapters
from src.context.identity_access.infrastructure.adapters import (
    UserBeanieRepository,
    VerificationBeanieRepository,
    Argon2Hasher,
    PyJwtService,
)

# Query addapters
from src.context.identity_access.infrastructure.adapters.queries import (
    MongoUserRepository,
)

# Dependency Injection for FastAPI
from src.core.mediator import get_mediator


# Repositories
@lru_cache()
def get_user_repository() -> IUserRepository:
    return UserBeanieRepository()


@lru_cache()
def get_verification_repository() -> IVerificationRepository:
    return VerificationBeanieRepository()


@lru_cache()
def get_hash_service() -> IHashService:
    return Argon2Hasher()


@lru_cache
def get_token_service() -> ITokenService:
    return PyJwtService()


@lru_cache
def get_user_query_repository() -> IUserQueryRepository:
    return MongoUserRepository()


# Use Cases
@lru_cache()
def get_sign_up_use_case():
    return SignUpLocalUseCase(
        user_repository=get_user_repository(),
        hash_service=get_hash_service(),
        verification_repository=get_verification_repository(),
    )


@lru_cache()
def get_sign_in_use_case():
    return SignInLocalUseCase(
        user_repository=get_user_repository(),
        hash_service=get_hash_service(),
        event_bus=get_mediator(),
    )


@lru_cache()
def get_verify_email_use_case():
    return VerifyEmailUseCase(
        verification_repository=get_verification_repository(), event_bus=get_mediator()
    )


@lru_cache
def get_get_users_query_handler(
    user_query_repository: IUserQueryRepository = Depends(get_user_query_repository),
) -> GetUsersQueryHandler:
    return GetUsersQueryHandler(user_query_repository=user_query_repository)


@lru_cache
def get_get_user_by_id_query_handler(
    user_query_repository: IUserQueryRepository = Depends(get_user_query_repository),
) -> GetUserByIdQueryHandler:
    return GetUserByIdQueryHandler(user_query_repository=user_query_repository)


SignUpLocalDep = Annotated[SignUpLocalUseCase, Depends(get_sign_up_use_case)]
SignInLocalDep = Annotated[SignInLocalUseCase, Depends(get_sign_in_use_case)]
VerifyEmailDep = Annotated[VerifyEmailUseCase, Depends(get_verify_email_use_case)]

GetUsersDep = Annotated[GetUsersQueryHandler, Depends(get_get_users_query_handler)]
GetUserByIdDep = Annotated[
    GetUserByIdQueryHandler, Depends(get_get_user_by_id_query_handler)
]


OAUTH_SCHEMA = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/signin")
TOKEN = Annotated[str, Depends(OAUTH_SCHEMA)]
