from contextlib import asynccontextmanager
from fastapi import FastAPI
from beanie import init_beanie

# Settings
from src.core.settings import settings

# Application Container
from src.core.container import AppContainer

# Models
from src.context.identity_access.infrastructure.models import (
    UserModel,
    VerificationModel,
)
from src.context.profile.infrastructure.models import ProfileModel
from src.context.scholarship.infrastructure.models import ScholarshipListingModel

from src.context.shared_kernel.infrastructure.addapters import MotorDBAdapter


@asynccontextmanager
async def database_lifespan(container: AppContainer):
    motor_db = MotorDBAdapter(
        url=settings.DB_URL,
        default_db_name=settings.WRITE_DB_NAME,
    )
    await motor_db.connect()
    db = motor_db.get_database()
    await init_beanie(
        database=db,
        document_models=[
            UserModel,
            VerificationModel,
            ProfileModel,
            ScholarshipListingModel,
        ],
    )

    container.set_database(motor_db)
    print("✅ Database initialized")
    try:
        yield motor_db
    finally:
        await motor_db.close()
        print("🛑 Database closed")


# async def get_db(request: Request):
#     db = request.app.state.db_client[settings.WRITE_DB_NAME]
#     try:
#         yield db
#     finally:
#         pass
