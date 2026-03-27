from datetime import datetime, timezone
import secrets

# base Aggregate
from src.context.shared_kernel.domain.entities.entity import Entity

# Value Objects
from src.context.identity_access.domain.value_objects import (
    VerificationId,
    EmailStr,
    VerificationToken,
    VerificationType,
)

# Enums
from src.context.identity_access.domain.enums import (
    VerificationTypeEnums,
    VerificationDeliveryMethodEnums,
)


class Verification(Entity[VerificationId]):
    def __init__(
        self,
        id: VerificationId,
        identity: EmailStr,
        type: VerificationTypeEnums,
        delivery_method: VerificationDeliveryMethodEnums,
        token: VerificationToken,
        expires_at: datetime,
    ):
        super().__init__(id)
        self.__identity = identity
        self.__type = type
        self.__delivery_method = delivery_method
        self.__token = token
        self.__expires_at = expires_at
        self.__is_used = False

    @property
    def identity(self) -> EmailStr:
        return self.__identity

    @property
    def type(self) -> VerificationTypeEnums:
        return self.__type

    @property
    def delivery_method(self) -> VerificationDeliveryMethodEnums:
        return self.__delivery_method

    @property
    def token(self) -> VerificationToken:
        return self.__token

    @property
    def expires_at(self) -> datetime:
        return self.__expires_at

    @property
    def is_used(self) -> bool:
        return self.__is_used

    @classmethod
    def create_email_verification(cls, email: EmailStr) -> "Verification":
        now = datetime.now(timezone.utc)
        type = VerificationType(VerificationTypeEnums.EMAIL_CONFIRMATION)
        delivery_method = VerificationDeliveryMethodEnums.OTP
        token = VerificationToken.generate_otp()
        expires_at = now + type.deltatime()
        return cls(
            id=VerificationId.generate(),
            identity=email,
            type=type.value,
            delivery_method=delivery_method,
            token=token,
            expires_at=expires_at,
        )

    def mark_as_used(self):
        self.__is_used = True

    def is_valid(self) -> bool:
        now = datetime.now(timezone.utc)
        return not self.__is_used and now < self.__expires_at
