from src.core.interfaces import IMediator

# event Message
from src.context.shared_kernel.domain.events import EventMessage, EducationCreated

# commands
from src.context.chat.application.command.commands import CreateEducationDocumentCommand


def education_created_handler(mediator: IMediator):
    async def callback(data: dict):
        event_message: EventMessage[EducationCreated] = EventMessage.from_dict(
            event_message=data, payload_type=EducationCreated
        )

        cmd = CreateEducationDocumentCommand(
            education_id=event_message.payload.education_id,
            profile_id=event_message.payload.profile_id,
            user_id=event_message.payload.user_id,
            major=event_message.payload.major,
            description=event_message.payload.description,
        )

        await mediator.publish(event=cmd)

    return callback
