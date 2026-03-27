from abc import abstractmethod

# Base Repisitory
from src.context.shared_kernel.domain.repository import Repository

# Aggregete
from src.context.identity_access.domain.entities import User


class IUserRepository(Repository[User]):
    @abstractmethod
    async def get_by_email(self, email: str) -> User:
        pass
