from pydantic import BaseModel
from datetime import datetime


class GetProfileRequest(BaseModel):
    pass


class AddWorkExperienceRequest(BaseModel):
    company: str
    position: str
    description: str | None
    start_date: datetime
    end_date: datetime


class AddEducationRequest(BaseModel):
    major: str
    description: str | None
    start_date: datetime
    end_date: datetime
