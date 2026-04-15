from src.core.interfaces import IMediator

from src.context.shared_kernel.domain.events import EventMessage, WorkExperienceCreated
from src.context.chat.application.command.commands import CreateWorkExperienceCommand


def work_experience_created_handler(mediator: IMediator):
    async def callback(data: dict):
        event_message: EventMessage[WorkExperienceCreated] = EventMessage.from_dict(
            event_message=data, payload_type=WorkExperienceCreated
        )

        cmd = CreateWorkExperienceCommand(
            work_experience_id=event_message.payload.work_experience_id,
            profile_id=event_message.payload.profile_id,
            user_id=event_message.payload.user_id,
            company=event_message.payload.company,
            position=event_message.payload.position,
            description=event_message.payload.description,
        )

        await mediator.publish(event=cmd)

    return callback
