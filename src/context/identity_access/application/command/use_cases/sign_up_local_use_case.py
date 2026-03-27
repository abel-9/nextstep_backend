# Commands
from src.context.identity_access.application.command.commands import SignUpCommand

# Aggregates
from src.context.identity_access.domain.entities import User, Verification

# Value Objects
from src.context.identity_access.domain.value_objects import EmailStr

# Repositories
from src.context.identity_access.domain.ports import (
    IUserRepository,
    IVerificationRepository,
)

# Services
from src.context.identity_access.application.ports import IHashService


class SignUpLocalUseCase:
    def __init__(
        self,
        user_repository: IUserRepository,
        verification_repository: IVerificationRepository,
        hash_service: IHashService,
    ):
        self.__user_repository = user_repository
        self.__verification_repository = verification_repository
        self.__hash_service = hash_service

    async def handle(self, cmd: SignUpCommand):
        user = await self.__user_repository.get_by_email(cmd.email)
        user_exists = True
        if not user:
            user = User.create(email=EmailStr(value=cmd.email))
            user_exists = False

        hashed_password = self.__hash_service.hash(cmd.password)
        user.register_local_account(secret=hashed_password)
        verification = Verification.create_email_verification(email=user.email)
        if not user_exists:
            await self.__user_repository.save(user)
        else:
            await self.__user_repository.update(user)
        await self.__verification_repository.save(verification)
