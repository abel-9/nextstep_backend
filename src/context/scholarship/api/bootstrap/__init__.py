from src.context.scholarship.api.bootstrap.consumers import (
    register_scholarship_consumers,
)
from src.context.scholarship.api.bootstrap.handlers import register_scholarship_handlers
from src.context.scholarship.api.bootstrap.container import ScholarshipContainer
from src.core.container import AppContainer
from src.context.shared_kernel.bootstrap.container import SharedContainer


async def bootstrap_scholarship_module(
    app_container: AppContainer, shared_container: SharedContainer
):
    scholarship_container = ScholarshipContainer(
        app_container=app_container, shared_container=shared_container
    )
    register_scholarship_consumers(container=scholarship_container)
    register_scholarship_handlers(container=scholarship_container)
