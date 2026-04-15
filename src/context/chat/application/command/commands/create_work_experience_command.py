from dataclasses import dataclass


@dataclass
class CreateWorkExperienceCommand:
    work_experience_id: str
    profile_id: str
    user_id: str
    company: str
    position: str
    description: str
