from fastapi import APIRouter

# Context routes
from src.context.profile.router import router as profile_context_router
from src.context.identity_access.router import router as identity_access_context_router

router = APIRouter(prefix="/api/v1")

router.include_router(router=identity_access_context_router)
router.include_router(
    router=profile_context_router,
)
