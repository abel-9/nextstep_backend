from dataclasses import dataclass


@dataclass
class TokenResponseDto:
    access_token: str
    # refresh_token: str
    token_type: str
