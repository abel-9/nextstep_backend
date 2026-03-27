from typing import List, Optional
from pydantic import BaseModel, Field


class AccountReadModel(BaseModel):
    id: str
    provider: str
    provider_id: str
    # secret: Optional[str] = None
    is_active: bool = True
    is_verified: bool = False


class UserReadModel(BaseModel):
    id: str = Field(validation_alias="_id")
    email: str
    accounts: List[AccountReadModel]
