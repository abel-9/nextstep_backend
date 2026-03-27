# the jwt main lib
import jwt

# settings
from src.core.settings import settings

# The interface
from src.context.identity_access.application.ports import ITokenService

# Infrastructure Exceptions
from src.context.identity_access.infrastructure.exceptions import (
    TokenExpiredError,
    InvalidTokenError,
)


class PyJwtService(ITokenService):
    def __init__(self):
        self.__secret_key = settings.JWT_SECRET_KEY
        self.__algorithm = settings.JWT_ALGORITHM

    async def sign(self, payload: dict) -> str:
        return jwt.encode(
            payload=payload,
            algorithm=self.__algorithm,
            key=self.__secret_key,
        )

    async def verify(self, token) -> dict:
        try:
            payload = jwt.decode(
                jwt=token,
                key=self.__secret_key,
                algorithms=[self.__algorithm],
            )
            return payload
        except jwt.ExpiredSignatureError:
            raise TokenExpiredError()
        except jwt.InvalidTokenError:
            raise InvalidTokenError()
