# Domain Ports
from src.context.identity_access.domain.ports import IUserRepository

# Event handlers
from src.context.identity_access.domain.events import EmailVerifiedEvent


class VerifyUserHandler:
    def __init__(self, user_repository: IUserRepository):
        self._user_repository = user_repository

    async def __call__(self, event: EmailVerifiedEvent):
        user = await self._user_repository.get_by_email(event.email)
        if user:
            user.verify_local_email()
            await self._user_repository.update(user)
