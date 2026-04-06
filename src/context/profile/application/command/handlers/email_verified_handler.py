import json

# Broker Interface
from src.context.profile.application.command.use_case import CreateProfileUseCase

# Command
from src.context.profile.application.command.commands import CreateProfileCommand

# Base Event Messages
from src.context.shared_kernel.domain.events import EventMessage

# Events
from src.context.shared_kernel.domain.events import EmailVerifiedEvent


def email_verified_handler(use_case: CreateProfileUseCase):
    """The actual logic that bridges RabbitMQ to the Application Use Case."""

    async def callback(data: dict):
        # 1. Parse raw message
        event_message: EventMessage[EmailVerifiedEvent] = EventMessage.from_dict(
            event_message=data, payload_type=EmailVerifiedEvent
        )
        # print(event_message)
        # 2. Pass data to the Use Case
        cmd = CreateProfileCommand(
            user_id=event_message.payload.user_id, email=event_message.payload.email
        )
        await use_case.execute(cmd=cmd)

    return callback
