from fastapi import APIRouter, Request, Query
from typing import Annotated

# shared dependencies
from src.core.oauth import TOKEN

# Queries
from src.context.identity_access.application.query.queries import (
    GetUsersQuery,
    GetUserByIdQuery,
    GetMeQuery,
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
    request: Request,
):
    return await request.app.state.container.mediator.send(
        GetUsersQuery(
            page=query.page, page_size=query.size, is_verified=query.is_verified
        )
    )


@router.get("/me", response_model=UserResponse)
async def get_me(token: TOKEN, request: Request):
    query = GetMeQuery(token=token)
    return await request.app.state.container.mediator.send(query)


@router.get("/{user_id}", response_model=UserResponse | None)
async def get_user(user_id: str, request: Request):
    return await request.app.state.container.mediator.send(
        GetUserByIdQuery(user_id=user_id)
    )
