from fastapi import APIRouter, Depends
from typing_extensions import Annotated

# Request schemas
from src.context.identity_access.api.schemas.responses import TokenResponse

# Response schemas
from src.context.identity_access.api.schemas.requests import (
    SigninRequest,
    SignupRequest,
    VerifyEmailRequest,
)

# Commands
from src.context.identity_access.application.command.commands import (
    SignUpCommand,
    SignInCommand,
    VerifyEmailCommand,
)

# # Dependencies
# from src.context.identity_access.api.dependencies import (
#     SignUpLocalDep,
#     SignInLocalDep,
#     VerifyEmailDep,
# )

from src.core.mediator import Mediator

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/signup")
async def signup(request: SignupRequest, mediator: Mediator):
    cmd = SignUpCommand(email=request.email, password=request.password)
    await mediator.send(request=cmd)


@router.post("/verify-email")
async def verify_email(request: VerifyEmailRequest, mediator: Mediator):
    cmd = VerifyEmailCommand(email=request.email, otp=request.otp)
    await mediator.send(request=cmd)


@router.post("/signin", response_model=TokenResponse | None)
async def signin(
    request: Annotated[SigninRequest, Depends(SigninRequest.as_form)],
    mediator: Mediator,
):
    cmd = SignInCommand(email=request.email, password=request.password)
    return await mediator.send(request=cmd)
