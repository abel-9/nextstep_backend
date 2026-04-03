from dataclasses import dataclass


@dataclass
class GetEducationQuery:
    token: str
    education_id: str
