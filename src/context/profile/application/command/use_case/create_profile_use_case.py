# Command Use Case
from src.context.profile.application.command.commands import CreateProfileCommand

# repository Interface
from src.context.profile.domain.ports import IProfileRepository

# domain entities
from src.context.profile.domain.entities import Profile

# Global Value Objects
from src.context.shared_kernel.domain.value_objects import UserId


class CreateProfileUseCase:
    def __init__(self, profile_repository: IProfileRepository):
        self.__profile_repository = profile_repository

    async def execute(self, cmd: CreateProfileCommand):
        # Here you would typically create a profile in the database\
        print(f"Creating profile for user_id: {cmd.user_id} with email: {cmd.email}")
        profile = Profile.create(user_id=UserId(cmd.user_id))
        await self.__profile_repository.save(profile)
