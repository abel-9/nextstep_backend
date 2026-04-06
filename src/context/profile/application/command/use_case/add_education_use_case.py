# Commands
from src.context.profile.application.command.commands import AddEducationCommand

# Repository
from src.context.profile.domain.ports import IProfileRepository

# Global Ports
from src.context.shared_kernel.application.ports import ITokenService
from src.core.interfaces.i_message_broker import IMessageBroker

# Value Objects
from src.context.shared_kernel.domain.value_objects import UserId

# Event types
from src.context.shared_kernel.domain.enums import EducationEventType

# base event message class
from src.context.shared_kernel.domain.events.event_message import EventMessage


class AddEducationUseCase:
    def __init__(
        self,
        profile_repository: IProfileRepository,
        token_service: ITokenService,
        message_broker: IMessageBroker,
    ):
        self.__profile_repository = profile_repository
        self.__token_service = token_service
        self.__message_broker = message_broker

    async def __call__(self, cmd: AddEducationCommand):
        payload = await self.__token_service.verify(token=cmd.token)
        profile = await self.__profile_repository.get_by_user_id(payload.get("sub"))
        if not profile:
            raise Exception("No Profile...")

        if not profile.is_for_user(UserId(payload.get("sub"))):
            raise Exception("Not yours...")

        education_created = profile.add_education(
            major=cmd.major,
            description=cmd.description,
            start_date=cmd.start_date,
            end_date=cmd.end_date,
        )
        await self.__profile_repository.update(profile)
        await self.__message_broker.publish(
            event_type=EducationEventType.CREATED,
            event_message=education_created.to_event_message(),
        )
