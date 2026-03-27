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

# Dependencies
from src.context.identity_access.api.dependencies import (
    SignUpLocalDep,
    SignInLocalDep,
    VerifyEmailDep,
)

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/signup")
async def signup(request: SignupRequest, use_case: SignUpLocalDep):
    cmd = SignUpCommand(email=request.email, password=request.password)
    await use_case.handle(cmd=cmd)


@router.post("/verify-email")
async def verify_email(request: VerifyEmailRequest, use_case: VerifyEmailDep):
    cmd = VerifyEmailCommand(email=request.email, otp=request.otp)
    await use_case.handle(cmd=cmd)


@router.post("/signin", response_model=TokenResponse | None)
async def signin(
    request: Annotated[SigninRequest, Depends(SigninRequest.as_form)],
    use_case: SignInLocalDep,
):
    cmd = SignInCommand(email=request.email, password=request.password)
    res = await use_case.handle(cmd=cmd)
    return res
