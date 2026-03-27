from dataclasses import dataclass
from datetime import datetime, timedelta
from src.core.settings import settings


@dataclass
class AccessSession:
    sub: str
    exp: datetime
    iat: datetime

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            sub=data["sub"],
            exp=datetime.fromtimestamp(data["exp"]),
            iat=datetime.fromtimestamp(data["iat"]),
        )

    @classmethod
    def from_jwt(cls, jwt_payload: dict):
        return cls(
            sub=jwt_payload["sub"],
            exp=datetime.fromtimestamp(jwt_payload["exp"]),
            iat=datetime.fromtimestamp(jwt_payload["iat"]),
        )

    @staticmethod
    def get_exp_timedelta():
        return timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
