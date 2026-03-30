from abc import abstractmethod

# base Repository
from src.context.shared_kernel.domain.repository import Repository

# read models
from src.context.profile.application.query.read_models import ProfileReadModel


class IProfileQuery(Repository[ProfileReadModel]):
    @abstractmethod
    async def get_by_user_id(self, user_id: str) -> ProfileReadModel:
        pass
