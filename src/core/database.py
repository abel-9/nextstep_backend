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

# Create a global client to reuse connection pooling
client = AsyncIOMotorClient(settings.DB_URL)


async def lifespan(app: FastAPI):
    db = client[settings.WRITE_DB_NAME]
    await init_beanie(
        database=db, document_models=[UserModel, VerificationModel, ProfileModel]
    )
    print("Database connection established.")
    print("Beanie initialized")
    yield
    print("Shutting down application.")
    client.close()
    print("Database connection closed.")


async def get_db():
    """Dependency that yields the MongoDB database instance."""
    db = client[settings.WRITE_DB_NAME]
    try:
        yield db
    finally:
        # For MongoDB/Motor, you generally don't need to close
        # the client after every request, but you can add cleanup here.
        pass
