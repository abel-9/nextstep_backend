from pydantic import BaseModel, EmailStr, Field


class SignupRequest(BaseModel):
    # Basic validation using Field
    email: EmailStr
    password: str = Field(min_length=8)


from fastapi import Form


class SigninRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

    @classmethod
    def as_form(
        cls,
        username: str = Form(...),  # OAuth2 standard field name
        password: str = Form(...),
    ):
        # We treat the 'username' input as the 'email'
        return cls(email=username, password=password)


class VerifyEmailRequest(BaseModel):
    email: EmailStr
    otp: str = Field(max_length=6, min_length=6)


class GetUsersRequest(BaseModel):
    page: int = Field(default=1, ge=1)
    size: int = Field(default=10, ge=1, le=100)
    is_verified: bool | None = None
