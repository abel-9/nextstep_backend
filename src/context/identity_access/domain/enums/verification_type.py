from enum import Enum


class VerificationTypeEnums(str, Enum):
    EMAIL_CONFIRMATION = "email_confirmation"
    PASSWORD_RESET = "password_reset"
    MFA_CODE = "mfa_code"
