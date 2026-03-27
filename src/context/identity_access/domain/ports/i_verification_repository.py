# Base Repository
from src.context.shared_kernel.domain.repository import Repository

# Aggregates
from src.context.identity_access.domain.entities import Verification

# Value Objects
from src.context.identity_access.domain.value_objects import (
    EmailStr,
    VerificationType,
    VerificationToken,
)


class IVerificationRepository(Repository[Verification]):
    async def get_all_by_identity(self, identity: EmailStr) -> list[Verification]:
        pass

    async def get_all_by_email_and_type(
        self, email: EmailStr, type: VerificationType
    ) -> list[Verification]:
        pass

    async def get_one_by_identity_type_token(
        self, identity: EmailStr, type: VerificationType, token: VerificationToken
    ) -> Verification | None:
        pass
