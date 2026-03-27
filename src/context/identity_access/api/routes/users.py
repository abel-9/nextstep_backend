from fastapi import APIRouter, Depends, Query
from typing import Annotated

# shared dependencies
from src.core.mediator import get_mediator, IMediator

# Queries
from src.context.identity_access.application.query.queries import (
    GetUsersQuery,
    GetUserByIdQuery,
)

# Response
from src.context.identity_access.api.schemas.responses import UserResponse

# Requests
from src.context.identity_access.api.schemas.requests import GetUsersRequest

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("", response_model=list[UserResponse])
async def get_users(
    query: Annotated[GetUsersRequest, Query()],
    mediator: Annotated[IMediator, Depends(get_mediator)],
):
    return await mediator.send(
        GetUsersQuery(
            page=query.page, page_size=query.size, is_verified=query.is_verified
        )
    )


@router.get("/{user_id}", response_model=UserResponse | None)
async def get_user(user_id: str, mediator: Annotated[IMediator, Depends(get_mediator)]):
    return await mediator.send(GetUserByIdQuery(user_id=user_id))
