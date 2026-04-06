from src.core.container import AppContainer

# shared container
from src.context.shared_kernel.bootstrap.container import SharedContainer


async def bootstrap_shared_container(app_container: AppContainer) -> SharedContainer:
    container = SharedContainer(app_container=app_container)
    return container
