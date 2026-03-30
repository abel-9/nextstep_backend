# Interface
from src.context.profile.application.query.ports import IProfileQuery

# Beanie Models
from src.context.profile.infrastructure.models import ProfileModel

# Read Models
from src.context.profile.application.query.read_models import ProfileReadModel


class ProfileBeanieQuery(IProfileQuery):
    async def get_all(self, query):
        pass

    async def get_by_id(self, id):
        pass

    async def save(self, entity):
        pass

    async def remove(self, entity):
        pass

    async def update(self, entity):
        pass

    async def get_by_user_id(self, user_id: str) -> ProfileReadModel:
        profile = await ProfileModel.find_one(ProfileModel.user_id == user_id).project(
            ProfileReadModel
        )
        return profile
