from fastapi import APIRouter

from src.context.scholarship.api.routes.scholarship import router as scholarship_router

router = APIRouter(tags=["Scholarship Context"])
router.include_router(router=scholarship_router)
