# Commands
from src.context.profile.application.command.commands import AddEducationCommand

# Repository
from src.context.profile.domain.ports import IProfileRepository

# Global Ports
from src.context.shared_kernel.application.ports import ITokenService

# Value Objects
from src.context.shared_kernel.domain.value_objects import UserId


class AddEducationUseCase:
    def __init__(
        self, profile_repository: IProfileRepository, token_service: ITokenService
    ):
        self.__profile_repository = profile_repository
        self.__token_service = token_service

    async def __call__(self, cmd: AddEducationCommand):
        payload = await self.__token_service.verify(token=cmd.token)
        profile = await self.__profile_repository.get_by_id(cmd.profile_id)
        if not profile:
            raise Exception("No Profile...")

        if not profile.is_for_user(UserId(payload.get("sub"))):
            raise Exception("Not yours...")

        profile.add_education(
            major=cmd.major,
            description=cmd.description,
            start_date=cmd.start_date,
            end_date=cmd.end_date,
        )
        await self.__profile_repository.update(profile)
