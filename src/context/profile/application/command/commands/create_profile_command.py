from dataclasses import dataclass


@dataclass
class CreateProfileCommand:
    user_id: str
    email: str
