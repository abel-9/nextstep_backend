from fastapi import FastAPI

from src.core.settings import settings
from .router import router

# Events
from .bootstrap import *

app = FastAPI(
    title=settings.TITLE,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    lifespan=lifespan,
)

app.include_router(router=router)
