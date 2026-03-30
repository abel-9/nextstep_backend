from fastapi import APIRouter

# Request Objects
from src.context.profile.api.schemas.request import AddEducationRequest

# commands
from src.context.profile.application.command.commands import AddEducationCommand

# Mediator Dependency
from src.core.mediator import Mediator
from src.core.oauth import TOKEN

router = APIRouter(prefix="/{profile_id}/education")


@router.get("/{education_id}")
def get_all_educations(profile_id: str, education_id: str):
    return {"data": "all education"}


@router.post("")
async def add_educations(
    token: TOKEN, profile_id: str, req: AddEducationRequest, mediator: Mediator
):
    cmd = AddEducationCommand(
        token=token,
        profile_id=profile_id,
        major=req.major,
        description=req.description,
        start_date=req.start_date,
        end_date=req.end_date,
    )
    return await mediator.send(request=cmd)
