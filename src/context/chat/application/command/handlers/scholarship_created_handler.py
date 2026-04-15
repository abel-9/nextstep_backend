from src.core.interfaces import IMediator

from src.context.shared_kernel.domain.events import EventMessage, ScholarshipCreated
from src.context.chat.application.command.commands import (
    CreateScholarshipDocumentCommand,
)


def scholarship_created_handler(mediator: IMediator):
    async def callback(data: dict):
        event_message: EventMessage[ScholarshipCreated] = EventMessage.from_dict(
            event_message=data, payload_type=ScholarshipCreated
        )

        cmd = CreateScholarshipDocumentCommand(
            listing_id=event_message.payload.listing_id,
            title=event_message.payload.title,
            description=event_message.payload.description,
            eligibility_summary=event_message.payload.eligibility_summary,
            provider_name=event_message.payload.provider_name,
            tags=event_message.payload.tags,
            deadline=event_message.payload.deadline,
        )

        await mediator.publish(event=cmd)

    return callback
