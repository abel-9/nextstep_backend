from functools import lru_cache

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
)

# adapters
from src.context.identity_access.infrastructure.adapters import (
    UserBeanieRepository,
    VerificationBeanieRepository,
    Argon2Hasher,
)

# Query addapters
from src.context.identity_access.infrastructure.adapters.queries import (
    MongoUserRepository,
)


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
def get_user_query_repository() -> IUserQueryRepository:
    return MongoUserRepository()
