from fastapi import APIRouter

from .scholarship import router as scholarship_router

router = APIRouter()

router.include_router(scholarship_router)
