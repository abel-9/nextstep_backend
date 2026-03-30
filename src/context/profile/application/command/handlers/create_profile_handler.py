import json

# Broker Interface
from src.context.profile.application.command.use_case import CreateProfileUseCase

# Command
from src.context.profile.application.command.commands import CreateProfileCommand


def create_profile_handler(use_case: CreateProfileUseCase):
    """The actual logic that bridges RabbitMQ to the Application Use Case."""

    async def callback(data: dict):
        # 1. Parse raw message
        payload: dict = data.get("data", {})
        user_id = payload.get("user_id")
        email = payload.get("email")

        # 2. Pass data to the Use Case
        cmd = CreateProfileCommand(user_id=user_id, email=email)
        await use_case.execute(cmd=cmd)

    return callback
