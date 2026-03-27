from motor.motor_asyncio import AsyncIOMotorDatabase

# Interface
from src.context.identity_access.application.query.ports import IUserQueryRepository

# Queries
from src.context.identity_access.application.query.queries import GetUsersQuery

# Read Models
from src.context.identity_access.application.query.read_models import UserReadModel

# Databse Models
from src.context.identity_access.infrastructure.models import UserModel


class MongoUserRepository(IUserQueryRepository):
    async def get_all(self, query: GetUsersQuery) -> list[UserReadModel]:
        filters = {}
        # if query.is_verified is not None:
        #     filters["is_verified"] = query.is_verified

        # Beanie find syntax
        users = (
            await UserModel.find(filters)
            .skip((query.page - 1) * query.page_size)
            .limit(query.page_size)
            .project(UserReadModel)
            .to_list()
        )
        return users

    async def get_by_id(self, id: str) -> UserReadModel | None:
        user = await UserModel.find_one(UserModel.id == id).project(UserReadModel)
        return user

    async def save(self, entity):
        pass

    async def update(self, entity):
        pass

    async def remove(self, entity):
        pass
