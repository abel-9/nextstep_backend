from abc import abstractmethod

from src.context.profile.domain.entities import Profile
from src.context.shared_kernel.domain.repository import Repository


class IProfileRepository(Repository[Profile]):
    @abstractmethod
    async def get_by_user_id(self, user_id: str) -> Profile | None:
        pass
