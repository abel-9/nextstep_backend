from src.context.chat.api.bootstrap.container import ChatContainer

# Event types
from src.context.shared_kernel.domain.enums import (
    EducationEventType,
    WorkExperienceEventType,
    ScholarshipEventType,
)

# event handler
from src.context.chat.application.command.handlers import (
    education_created_handler,
    work_experience_created_handler,
    scholarship_created_handler,
)


async def register_chat_consumers(container: ChatContainer):
    await container.app_container.message_broker.consume(
        event_type=EducationEventType.CREATED,
        callback=education_created_handler(mediator=container.app_container.mediator),
    )

    await container.app_container.message_broker.consume(
        event_type=WorkExperienceEventType.CREATED,
        callback=work_experience_created_handler(
            mediator=container.app_container.mediator
        ),
    )

    await container.app_container.message_broker.consume(
        event_type=ScholarshipEventType.CREATED,
        callback=scholarship_created_handler(mediator=container.app_container.mediator),
    )
