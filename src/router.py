from fastapi import APIRouter

# Context routes
from src.context.profile.api.routes import router as profile_context_router
from src.context.identity_access.api.routes import (
    router as identity_access_context_router,
)
from src.context.scholarship.api.routes import router as scholarship_context_router
from src.context.chat.api.routes import router as chat_context_router

router = APIRouter(prefix="/api/v1")

router.include_router(router=identity_access_context_router)
router.include_router(
    router=profile_context_router,
)
router.include_router(router=scholarship_context_router)
router.include_router(router=chat_context_router)
