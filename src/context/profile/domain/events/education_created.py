from dataclasses import dataclass
from datetime import datetime


@dataclass
class EducationCreated:
    id: str
    major: str
    description: str
    start_date: datetime
    end_date: datetime | None = None
