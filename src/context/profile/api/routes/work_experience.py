from fastapi import APIRouter

# Request Objects
from src.context.profile.api.schemas.request import AddWorkExperienceRequest

# commands
from src.context.profile.application.command.commands import AddWorkExperienceCommand

# queries
from src.context.profile.application.query.queries import (
    GetAllWorkExperiencesQuery,
    GetWorkExperienceQuery,
)

# Mediator Dependency
from src.core.mediator import Mediator
from src.core.oauth import TOKEN

router = APIRouter(prefix="/profile/work-experience")


@router.get("")
async def get_all_work_experiences(token: TOKEN, mediator: Mediator):
    query = GetAllWorkExperiencesQuery(token=token)
    return await mediator.send(request=query)


@router.get("/{work_exp_id}")
async def get_work_experience(work_exp_id: str, token: TOKEN, mediator: Mediator):
    query = GetWorkExperienceQuery(token=token, work_exp_id=work_exp_id)
    return await mediator.send(request=query)


@router.post("")
async def add_work_experiences(
    token: TOKEN, req: AddWorkExperienceRequest, mediator: Mediator
):
    cmd = AddWorkExperienceCommand(
        token=token,
        description=req.description,
        company=req.company,
        position=req.position,
        start_date=req.start_date,
        end_date=req.end_date,
    )
    return await mediator.send(request=cmd)
