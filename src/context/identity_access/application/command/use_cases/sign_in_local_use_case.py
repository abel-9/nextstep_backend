# DTOS
from src.context.identity_access.application.command.dtos import TokenResponseDto

# Commands
from src.context.identity_access.application.command.commands import SignInCommand

# Repository
from src.context.identity_access.domain.ports import IUserRepository
from src.context.identity_access.domain.exceptions import UserNotFoundError

# Application Domains
from src.context.identity_access.application.ports import IHashService

# Global Request bus
from src.context.shared_kernel.application.ports import IMediator, IMessageBroker

# Commands
from src.context.identity_access.application.command.commands import (
    CreateSessionCommand,
)


class SignInLocalUseCase:
    def __init__(
        self,
        user_repository: IUserRepository,
        hash_service: IHashService,
        event_bus: IMediator,
        message_broker: IMessageBroker,
    ):
        self.__user_repository = user_repository
        self.__hash_service = hash_service
        self.__event_bus = event_bus
        self.__message_broker = message_broker

    async def __call__(self, cmd: SignInCommand) -> TokenResponseDto:
        user = await self.__user_repository.get_by_email(cmd.email)
        if not user:
            raise UserNotFoundError(cmd.email)
        hased_pwd = self.__hash_service.hash(cmd.password)
        user.compare_local_account_secret(hased_pwd)

        token = await self.__event_bus.send(CreateSessionCommand(user_id=user.id.value))
        self.__message_broker.publish(
            event_type="user.signed_in",
            message={"user_id": user.id.value, "email": user.email.value},
        )
        return token
