from dataclasses import dataclass


@dataclass
class SignInCommand:
    email: str
    password: str


@dataclass
class SignUpCommand:
    email: str
    password: str


@dataclass
class VerifyEmailCommand:
    email: str
    otp: str


@dataclass
class CreateSessionCommand:
    user_id: str
