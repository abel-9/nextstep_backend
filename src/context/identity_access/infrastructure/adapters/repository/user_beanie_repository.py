# Repository
from src.context.identity_access.domain.ports import IUserRepository

# Domain Aggregates
from src.context.identity_access.domain.entities import User

# Mappers
from src.context.identity_access.infrastructure.mappers.user_mapper import UserMapper

# Beanie Models
from src.context.identity_access.infrastructure.models import UserModel


class UserBeanieRepository(IUserRepository):
    async def get_all(self):
        pass

    async def get_by_id(self, id):
        pass

    async def remove(self, entity):
        pass

    async def update(self, entity):
        user_model = UserMapper.to_beanie_user(entity)
        await user_model.replace()

    async def save(self, entity) -> None:
        user_model = UserMapper.to_beanie_user(entity)
        await user_model.insert()

    async def get_by_email(self, email) -> User | None:
        user_model = await UserModel.find_one(UserModel.email == email)
        if user_model:
            return UserMapper.from_beanie_user(user_model)
        return None
