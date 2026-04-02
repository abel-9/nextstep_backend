from dataclasses import dataclass
from datetime import datetime


@dataclass
class AddWorkExperienceCommand:
    token: str
    company: str
    position: str
    description: str
    start_date: datetime
    end_date: datetime | None
