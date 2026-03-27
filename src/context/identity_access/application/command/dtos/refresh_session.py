from dataclasses import dataclass
from datetime import datetime


@dataclass
class RefreshSession:
    sub: str
    jti: str
    exp: datetime
    iat: datetime
