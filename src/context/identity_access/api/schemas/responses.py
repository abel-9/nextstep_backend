from typing import Optional

from pydantic import BaseModel


class TokenResponse(BaseModel):
    access_token: str
    # refresh_token: str
    token_type: str = "bearer"


class ProfileResponse(BaseModel):
    id: str
    email: str


class AccountResponse(BaseModel):
    id: str
    provider: str
    provider_id: str
    # secret: Optional[str] = None
    is_active: bool = True
    is_verified: bool = False


class UserResponse(BaseModel):
    id: str
    email: str
    accounts: list[AccountResponse]
