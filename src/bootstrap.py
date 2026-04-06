from fastapi import FastAPI

# Core Container
from src.core.container import AppContainer

# Core Lifespan
from src.core.mediator import mediator_lifespan
from src.core.broker import broker_lifespan
from src.core.database import database_lifespan
from src.core.vector_db import vector_db_lifespan

# Context Lifespan
# from src.context.identity_access.bootstrap import register_identity_handlers
from src.context.identity_access.api.bootstrap import bootstrap_identity_access_module
from src.context.scholarship.api.bootstrap import bootstrap_scholarship_module
from src.context.profile.api.bootstrap import bootstrap_profile_module
from src.context.chat.api.bootstrap import bootstrap_chat_module
from src.context.shared_kernel.bootstrap import bootstrap_shared_container

# from src.context.scholarship.bootstrap import register_scholarship_handlers

from contextlib import AsyncExitStack, asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    app_container = AppContainer()
    async with AsyncExitStack() as stack:
        # Core Application Container
        # This "enters" both context managers in order
        await stack.enter_async_context(database_lifespan(container=app_container))
        await stack.enter_async_context(vector_db_lifespan(container=app_container))
        await stack.enter_async_context(broker_lifespan(container=app_container))
        await stack.enter_async_context(mediator_lifespan(container=app_container))
        # Register handlers after all resources are ready

        shared_container = await bootstrap_shared_container(app_container=app_container)
        await bootstrap_identity_access_module(
            app_container=app_container, shared_container=shared_container
        )
        await bootstrap_profile_module(
            app_container=app_container, shared_container=shared_container
        )
        await bootstrap_scholarship_module(
            app_container=app_container, shared_container=shared_container
        )
        await bootstrap_chat_module(
            app_container=app_container, shared_container=shared_container
        )

        app.state.container = app_container

        print("🚀 All systems online")
        yield
