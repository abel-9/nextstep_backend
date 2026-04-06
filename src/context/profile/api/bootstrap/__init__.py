from src.context.profile.api.bootstrap.consumers import register_profile_consumers
from src.context.profile.api.bootstrap.handlers import register_profile_handlers
from src.context.shared_kernel.application.ports.I_message_broker import IMessageBroker

# Application Container
from src.core.container import AppContainer
from src.context.shared_kernel.bootstrap.container import SharedContainer

# Container
from src.context.profile.api.bootstrap.container import ProfileContainer


async def bootstrap_profile_module(
    app_container: AppContainer, shared_container: SharedContainer
):
    profile_container = ProfileContainer(
        app_container=app_container, shared_container=shared_container
    )
    await register_profile_consumers(container=profile_container)
    await register_profile_handlers(container=profile_container)
