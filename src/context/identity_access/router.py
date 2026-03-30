from fastapi import APIRouter

# Context Routes
from src.context.identity_access.api.routes.auth import router as auth_router
from src.context.identity_access.api.routes.users import router as user_router

router = APIRouter()

router.include_router(router=auth_router)
router.include_router(router=user_router)
