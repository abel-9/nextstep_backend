from fastapi import FastAPI

# Core Lifespan
from src.core.broker import broker_lifespan
from src.core.database import database_lifespan
from src.core.vector_db import vector_db_lifespan

# Context Lifespan
from src.context.identity_access.bootstrap import register_identity_handlers
from src.context.profile.bootstrap import (
    register_profile_consumers,
    register_profile_handlers,
)

from contextlib import AsyncExitStack, asynccontextmanager
from src.context.identity_access.bootstrap import *


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with AsyncExitStack() as stack:
        # This "enters" both context managers in order
        await stack.enter_async_context(database_lifespan(app))
        vector_db = await stack.enter_async_context(vector_db_lifespan(app))
        broker = await stack.enter_async_context(broker_lifespan(app))
        # Register handlers after all resources are ready
        register_identity_handlers(broker=broker)

        await register_profile_consumers(broker=broker)
        register_profile_handlers(vector_db=vector_db)

        print("🚀 All systems online")
        yield
