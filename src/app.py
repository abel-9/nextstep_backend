from fastapi import FastAPI

from src.core.settings import settings
from .router import router
from src.core.database import lifespan

# Events
from src.context.identity_access.api.events import *

app = FastAPI(
    title=settings.TITLE,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    lifespan=lifespan,
)

app.include_router(router=router)
