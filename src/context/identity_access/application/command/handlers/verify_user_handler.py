# Domain Ports
from src.context.identity_access.domain.ports import IUserRepository

# shared Interface
from src.context.shared_kernel.application.ports.I_message_broker import IMessageBroker

# Event handlers
from src.context.identity_access.domain.events import EmailVerifiedEvent


class VerifyUserHandler:
    def __init__(
        self, user_repository: IUserRepository, message_broker: IMessageBroker
    ):
        self._user_repository = user_repository
        self._message_broker = message_broker

    async def __call__(self, event: EmailVerifiedEvent):
        user = await self._user_repository.get_by_email(event.email)
        if user:
            user.verify_local_email()
            await self._user_repository.update(user)
            await self._message_broker.publish(
                event_type="user.verified",
                message={"email": user.email.value, "user_id": user.id.value},
            )
