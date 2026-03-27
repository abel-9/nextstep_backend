import secrets
import string

# Base Value Object
from src.context.shared_kernel.domain.value_objects.value_object import ValueObject


class VerificationToken(ValueObject[str]):
    def __init__(self, value: str):
        super().__init__(value=value)

    @classmethod
    def generate_otp(cls) -> "VerificationToken":
        # Generate a 6-digit OTP
        otp = "".join(secrets.choice(string.digits) for _ in range(6))
        return cls(value=otp)

    @classmethod
    def generate_url_token(cls) -> "VerificationToken":
        return cls(value=secrets.token_urlsafe(16))
