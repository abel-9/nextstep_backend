from datetime import datetime
from dataclasses import dataclass


@dataclass
class AddEducationCommand:
    token: str
    major: str
    description: str | None
    start_date: datetime
    end_date: datetime | None
