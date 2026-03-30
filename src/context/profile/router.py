from fastapi import APIRouter

# Routes
from src.context.profile.api.routes.profile import router as profile_router
from src.context.profile.api.routes.work_experience import (
    router as work_experience_router,
)
from src.context.profile.api.routes.education import router as education_router

router = APIRouter(tags=["Profile Context"])

router.include_router(router=profile_router)
router.include_router(router=work_experience_router)
router.include_router(router=education_router)
