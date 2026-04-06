from dataclasses import dataclass


@dataclass(frozen=True)
class CreateEducationDocumentCommand:
    education_id: str
    profile_id: str
    user_id: str
    major: str
    description: str
