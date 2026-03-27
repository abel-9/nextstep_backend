from dataclasses import dataclass


@dataclass
class EmailVerifiedEvent:
    email: str
