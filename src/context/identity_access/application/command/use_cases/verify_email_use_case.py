import secrets

# Commands
from src.context.identity_access.application.command.commands import VerifyEmailCommand

# Repository Interface
from src.context.identity_access.domain.ports import (
    IVerificationRepository,
    IUserRepository,
)

# shared Interfaces
from src.context.shared_kernel.application.ports import IMessageBroker

# shared types
from src.context.shared_kernel.domain.enums import UserEventType

# Value Objects
from src.context.identity_access.domain.value_objects import (
    VerificationType,
    EmailStr,
    VerificationToken,
)

# Enums
from src.context.identity_access.domain.enums import VerificationTypeEnums

# Based Event Messages
from src.context.shared_kernel.domain.events.event_message import EventMessage

# Events
from src.context.shared_kernel.domain.events import EmailVerifiedEvent

# Application Exceptions
from src.context.identity_access.application.exceptions import (
    InvalidOtpError,
    OtpExpiredError,
)


class VerifyEmailUseCase:
    def __init__(
        self,
        verification_repository: IVerificationRepository,
        user_repository: IUserRepository,
        message_broker: IMessageBroker,
    ):
        self._verification_repository = verification_repository
        self._user_repository = user_repository
        self._message_broker = message_broker

    async def __call__(self, cmd: VerifyEmailCommand):
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
        user_entity = await self._user_repository.get_by_email(email=cmd.email)
        if not user_entity:
            # This should never happen, but just in case
            raise InvalidOtpError()

        user_entity.verify_local_email()
        await self._user_repository.update(user_entity)
        await self._verification_repository.update(verification_entity)

        event = EmailVerifiedEvent(
            email=cmd.email,
            user_id=user_entity.id.value,
        )
        await self._message_broker.publish(
            event_type=UserEventType.USER_VERIFIED,
            event_message=event.to_event_message(),
        )
