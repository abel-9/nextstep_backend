# Commands
from src.context.profile.application.command.commands import AddWorkExperienceCommand

# Repository
from src.context.profile.domain.ports import IProfileRepository

# Global Ports
from src.context.shared_kernel.application.ports import ITokenService
from src.core.interfaces.i_message_broker import IMessageBroker

# Value Objects
from src.context.shared_kernel.domain.value_objects import UserId
from src.context.shared_kernel.domain.enums import WorkExperienceEventType

# Core deps
from src.core.mediator import IMediator


class AddWorkExperienceUseCase:
    def __init__(
        self,
        profile_repository: IProfileRepository,
        token_service: ITokenService,
        message_broker: IMessageBroker,
    ):
        self.__profile_repository = profile_repository
        self.__token_service = token_service
        self.__message_broker = message_broker

    async def __call__(self, cmd: AddWorkExperienceCommand):
        payload = await self.__token_service.verify(token=cmd.token)
        profile = await self.__profile_repository.get_by_user_id(payload.get("sub"))
        if not profile:
            raise Exception("No Profile...")

        if not profile.is_for_user(UserId(payload.get("sub"))):
            raise Exception("Not yours...")

        work_experience_created = profile.add_work_experience(
            company=cmd.company,
            position=cmd.position,
            description=cmd.description,
            start_date=cmd.start_date,
            end_date=cmd.end_date,
        )
        await self.__profile_repository.update(profile)
        await self.__message_broker.publish(
            event_type=WorkExperienceEventType.CREATED,
            event_message=work_experience_created.to_event_message(),
        )
