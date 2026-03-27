from src.context.identity_access.domain.entities import Verification
from src.context.identity_access.domain.enums import (
    VerificationDeliveryMethodEnums,
    VerificationTypeEnums,
)
from src.context.identity_access.domain.value_objects import (
    EmailStr,
    VerificationId,
    VerificationToken,
)
from src.context.identity_access.infrastructure.models import VerificationModel


class VerificationMapper:
    @staticmethod
    def to_beanie_verification(verification: Verification) -> VerificationModel:
        return VerificationModel(
            id=verification.id.value,
            identity=verification.identity.value,
            type=verification.type.value,
            delivery_method=verification.delivery_method.value,
            token=verification.token.value,
            expires_at=verification.expires_at,
            is_used=verification.is_used,
        )

    @staticmethod
    def from_beanie_verification(verification_model: VerificationModel) -> Verification:
        verification = Verification(
            id=VerificationId(verification_model.id),
            identity=EmailStr(value=verification_model.identity),
            type=VerificationTypeEnums(verification_model.type),
            delivery_method=VerificationDeliveryMethodEnums(
                verification_model.delivery_method
            ),
            token=VerificationToken(verification_model.token),
            expires_at=verification_model.expires_at,
        )
        if verification_model.is_used:
            verification._Verification__is_used = True
        return verification
