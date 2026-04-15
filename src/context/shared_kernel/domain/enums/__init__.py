from enum import Enum


class UserEventType(str, Enum):
    SIGNED_IN = "user.signed_in"
    REGISTERED = "user.registered"
    SIGNED_OUT = "user.signed_out"
    USER_VERIFIED = "user.verified"


class EducationEventType(str, Enum):
    CREATED = "education.created"


class WorkExperienceEventType(str, Enum):
    CREATED = "work_experience.created"


class ScholarshipEventType(str, Enum):
    CREATED = "scholarship.created"
