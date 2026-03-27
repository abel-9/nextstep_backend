from beanie import Document
from typing import Optional, List
from pydantic import BaseModel, Field


class Account(BaseModel):
    # In an embedded setup, the account usually doesn't need 'user_id'
    # because it lives inside the User document already.
    id: str
    provider: str
    provider_id: str
    secret: Optional[str] = None
    is_active: bool = True
    is_verified: bool = False


class User(Document):
    # Beanie uses 'id' for the MongoDB _id.
    # You can map your UserId to it.
    id: str = Field(alias="_id")
    email: str
    accounts: List[Account] = []

    class Settings:
        name = "users"
        # This allows Beanie to work with your custom init or private logic
        # use_revision = True
