from fastapi import APIRouter, Request

# Request Objects
from src.context.profile.api.schemas.request import AddEducationRequest

# commands
from src.context.profile.application.command.commands import AddEducationCommand

# queries
from src.context.profile.application.query.queries import (
    GetAllEducationsQuery,
    GetEducationQuery,
)

# Mediator Dependency
from src.core.oauth import TOKEN

router = APIRouter(prefix="/profile/education")


@router.get("")
async def get_all_educations(token: TOKEN, request: Request):
    query = GetAllEducationsQuery(token=token)
    return await request.app.state.container.mediator.send(request=query)


@router.get("/{education_id}")
async def get_education(
    education_id: str,
    token: TOKEN,
    request: Request,
):
    query = GetEducationQuery(token=token, education_id=education_id)
    return await request.app.state.container.mediator.send(request=query)


@router.post("")
async def add_educations(
    token: TOKEN,
    req: AddEducationRequest,
    request: Request,
):
    cmd = AddEducationCommand(
        token=token,
        major=req.major,
        description=req.description,
        start_date=req.start_date,
        end_date=req.end_date,
    )
    return await request.app.state.container.mediator.send(request=cmd)
