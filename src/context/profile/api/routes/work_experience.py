from fastapi import APIRouter

# Request Objects
from src.context.profile.api.schemas.request import AddWorkExperienceRequest

# commands
from src.context.profile.application.command.commands import AddWorkExperienceCommand

# Mediator Dependency
from src.core.mediator import Mediator
from src.core.oauth import TOKEN

router = APIRouter(prefix="/{profile_id}/work-experience")


@router.get("/{work_exp_id}")
def get_all_work_experiences(profile_id: str, work_exp_id: str):
    return {"data": "all work experience"}


@router.post("")
async def add_work_experiences(
    token: TOKEN, profile_id: str, req: AddWorkExperienceRequest, mediator: Mediator
):
    cmd = AddWorkExperienceCommand(
        token=token,
        profile_id=profile_id,
        description=req.description,
        company=req.company,
        position=req.position,
        start_date=req.start_date,
        end_date=req.end_date,
    )
    return await mediator.send(request=cmd)
