from src.context.identity_access.api.bootstrap.consumers import (
    register_identity_access_consumers,
)
from src.context.identity_access.api.bootstrap.handlers import (
    register_identity_access_handlers,
)

# core Container
from src.core.container import AppContainer
from src.context.shared_kernel.bootstrap.container import SharedContainer


from src.context.identity_access.api.bootstrap.container import IdentityAccessContainer


async def bootstrap_identity_access_module(
    app_container: AppContainer, shared_container: SharedContainer
):
    identity_access_container = IdentityAccessContainer(
        app_container=app_container, shared_container=shared_container
    )
    register_identity_access_consumers(container=identity_access_container)
    register_identity_access_handlers(container=identity_access_container)
