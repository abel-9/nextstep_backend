from fastapi import APIRouter, Request

# Queries
from src.context.profile.application.query.queries import GetMyProfileQuery

# Dependencies
from src.core.oauth import TOKEN

router = APIRouter(prefix="/profile")


@router.get("")
async def get_profile(token: TOKEN, request: Request):
    query = GetMyProfileQuery(token=token)
    return await request.app.state.container.mediator.send(request=query)
