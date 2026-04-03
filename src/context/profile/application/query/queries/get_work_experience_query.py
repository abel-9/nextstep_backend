from dataclasses import dataclass


@dataclass
class GetWorkExperienceQuery:
    token: str
    work_exp_id: str
