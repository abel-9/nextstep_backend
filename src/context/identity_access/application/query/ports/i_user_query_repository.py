# Base Repository
from src.context.shared_kernel.domain.repository import Repository

# Read Models
from src.context.identity_access.application.query.read_models import UserReadModel


class IUserQueryRepository(Repository[UserReadModel]):
    pass
