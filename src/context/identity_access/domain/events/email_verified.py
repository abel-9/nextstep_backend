from dataclasses import dataclass


@dataclass
class EmailVerifiedEvent:
    user_id: str
    email: str
