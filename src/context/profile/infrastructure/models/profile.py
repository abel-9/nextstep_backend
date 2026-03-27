from datetime import datetime
from typing import Optional

from beanie import Document
from pydantic import BaseModel, Field


class WorkExperience(BaseModel):
    company: str
    position: str
    start_date: datetime
    end_date: Optional[datetime] = None


class Profile(Document):
    id: str = Field(alias="_id")
    user_id: str
    work_experiences: list[WorkExperience] = []

    class Settings:
        name = "profiles"
