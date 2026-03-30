from fastapi import APIRouter, Depends
from typing import Annotated

# Queries
from src.context.profile.application.query.queries import GetMyProfileQuery

# Dependencies
from src.core.mediator import get_mediator, IMediator
from src.core.oauth import TOKEN

router = APIRouter(prefix="/profile")


@router.get("")
async def get_profile(
    token: TOKEN, mediator: Annotated[IMediator, Depends(get_mediator)]
):
    query = GetMyProfileQuery(token=token)
    return await mediator.send(request=query)


@router.delete("")
def delete_profile(profile_id: str):
    return {"message": f"Profile with id {profile_id} deleted successfully"}
