from dataclasses import dataclass


@dataclass
class UserRegisteredEvent:
    user_id: str
    email: str
