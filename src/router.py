from fastapi import APIRouter

from src.context.identity_access.api.routes.auth import router as auth_router
from src.context.identity_access.api.routes.users import router as users_router
from src.context.profile.api.routes.profile import router as profile_router

router = APIRouter(prefix="/api/v1")

router.include_router(
    router=auth_router,
)
router.include_router(
    router=users_router,
)
router.include_router(
    router=profile_router,
)
