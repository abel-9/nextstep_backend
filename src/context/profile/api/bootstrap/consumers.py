# profile Container
from src.context.profile.api.bootstrap.container import ProfileContainer

# Enums
from src.context.shared_kernel.domain.enums import UserEventType

# Handlers
from src.context.profile.application.command.handlers import email_verified_handler


async def register_profile_consumers(container: ProfileContainer):
    await container.app_container.message_broker.consume(
        event_type=UserEventType.USER_VERIFIED,
        callback=email_verified_handler(
            use_case=container.get_create_profile_use_case(),
        ),
    )
