from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from typing import Annotated
from src.core.settings import settings


OAUTH_SCHEMA = OAuth2PasswordBearer(tokenUrl=settings.OAUTH_TOKEN_URL)
TOKEN = Annotated[str, Depends(OAUTH_SCHEMA)]
