from fastapi import APIRouter

from .education import router as education_router
from .profile import router as profile_router
from .work_experience import router as work_experience_router

router = APIRouter()

router.include_router(profile_router)
router.include_router(work_experience_router)
router.include_router(education_router)
