from src.context.profile.domain.entities import Profile
from src.context.profile.domain.ports import IProfileRepository
from src.context.profile.infrustructure.mappers import ProfileMapper
from src.context.profile.infrustructure.models import ProfileModel


class ProfileBeanieRepository(IProfileRepository):
    async def get_all(self):
        pass

    async def get_by_id(self, id):
        pass

    async def remove(self, entity):
        pass

    async def update(self, entity: Profile) -> None:
        profile_model = ProfileMapper.to_beanie_profile(entity)
        await profile_model.replace()

    async def save(self, entity: Profile) -> None:
        profile_model = ProfileMapper.to_beanie_profile(entity)
        await profile_model.insert()

    async def get_by_user_id(self, user_id: str) -> Profile | None:
        profile_model = await ProfileModel.find_one(ProfileModel.user_id == user_id)
        if profile_model:
            return ProfileMapper.from_beanie_profile(profile_model)
        return None
