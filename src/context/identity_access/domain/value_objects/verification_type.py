from datetime import timedelta

# Base Value Object
from src.context.shared_kernel.domain.value_objects.value_object import ValueObject

# Enums
from src.context.identity_access.domain.enums import VerificationTypeEnums


class VerificationType(ValueObject[VerificationTypeEnums]):
    def __init__(self, value: VerificationTypeEnums):
        if not isinstance(value, VerificationTypeEnums):
            valid_options = ", ".join([e.name for e in VerificationTypeEnums])
            raise ValueError(
                f"Invalid verification type: {value}. Must be a member of {valid_options}."
            )
        super().__init__(value=value)

    def deltatime(self) -> timedelta:
        if self.value == VerificationTypeEnums.EMAIL_CONFIRMATION:
            return timedelta(minutes=5)
        elif self.value == VerificationTypeEnums.PASSWORD_RESET:
            return timedelta(minutes=5)
        elif self.value == VerificationTypeEnums.MFA_CODE:
            return timedelta(minutes=5)
