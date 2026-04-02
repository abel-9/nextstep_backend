from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class WorkExperience(BaseModel):
    id: str
    company: str
    position: str
    description: str | None
    start_date: datetime
    end_date: Optional[datetime] = None


class Education(BaseModel):
    id: str
    major: str
    description: str | None
    start_date: datetime
    end_date: Optional[datetime] = None


class ProfileReadModel(BaseModel):
    id: str = Field(validation_alias="_id")
    user_id: str
    work_experiences: list[WorkExperience]
    educations: list[Education]
