from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

# Settings
from src.core.settings import settings

# Models
from src.context.identity_access.infrastructure.models import (
    UserModel,
    VerificationModel,
)
from src.context.profile.infrastructure.models import ProfileModel

from motor.motor_asyncio import AsyncIOMotorClient


@asynccontextmanager
async def database_lifespan(app: FastAPI):
    client = AsyncIOMotorClient(settings.DB_URL)
    db = client[settings.WRITE_DB_NAME]
    await init_beanie(
        database=db, document_models=[UserModel, VerificationModel, ProfileModel]
    )

    app.state.db_client = client
    print("✅ Database initialized")
    try:
        yield client
    finally:
        client.close()
        print("🛑 Database closed")


async def get_db(request: Request):
    db = request.app.state.db_client[settings.WRITE_DB_NAME]
    try:
        yield db
    finally:
        pass
