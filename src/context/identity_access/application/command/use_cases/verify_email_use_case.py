import secrets

# Commands
from src.context.identity_access.application.command.commands import VerifyEmailCommand

# shared Interface
from src.context.shared_kernel.application.ports import IMediator

# Repository Interface
from src.context.identity_access.domain.ports import IVerificationRepository

# Value Objects
from src.context.identity_access.domain.value_objects import (
    VerificationType,
    EmailStr,
    VerificationToken,
)

# Enums
from src.context.identity_access.domain.enums import VerificationTypeEnums

# Domain Events
from src.context.identity_access.domain.events.email_verified import EmailVerifiedEvent

# Application Exceptions
from src.context.identity_access.application.exceptions import (
    InvalidOtpError,
    OtpExpiredError,
)


class VerifyEmailUseCase:
    def __init__(
        self, verification_repository: IVerificationRepository, event_bus: IMediator
    ):
        self._verification_repository = verification_repository
        self._event_bus = event_bus

    async def handle(self, cmd: VerifyEmailCommand):
        verification_entity = (
            await self._verification_repository.get_one_by_identity_type_token(
                identity=EmailStr(cmd.email),
                type=VerificationType(VerificationTypeEnums.EMAIL_CONFIRMATION),
                token=VerificationToken(cmd.otp),
            )
        )

        if not verification_entity or not secrets.compare_digest(
            cmd.otp, verification_entity.token.value
        ):
            raise InvalidOtpError()
        if not verification_entity.is_valid():
            raise OtpExpiredError()

        verification_entity.mark_as_used()
        await self._verification_repository.update(verification_entity)
        await self._event_bus.publish(EmailVerifiedEvent(email=cmd.email))
