from fastapi import APIRouter, Depends, Request
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

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/signup")
async def signup(
    payload: SignupRequest,
    req: Request,
):
    cmd = SignUpCommand(email=payload.email, password=payload.password)
    await req.app.state.container.mediator.send(request=cmd)


@router.post("/verify-email")
async def verify_email(
    payload: VerifyEmailRequest,
    req: Request,
):
    cmd = VerifyEmailCommand(email=payload.email, otp=payload.otp)
    await req.app.state.container.mediator.send(request=cmd)


@router.post("/signin", response_model=TokenResponse | None)
async def signin(
    payload: Annotated[SigninRequest, Depends(SigninRequest.as_form)],
    req: Request,
):
    cmd = SignInCommand(email=payload.email, password=payload.password)
    return await req.app.state.container.mediator.send(request=cmd)
