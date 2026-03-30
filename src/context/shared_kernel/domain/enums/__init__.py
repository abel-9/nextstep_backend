from enum import Enum


class UserEventType(str, Enum):
    SIGNED_IN = "user.signed_in"
    REGISTERED = "user.registered"
    SIGNED_OUT = "user.signed_out"
    USER_VERIFIED = "user.verified"
