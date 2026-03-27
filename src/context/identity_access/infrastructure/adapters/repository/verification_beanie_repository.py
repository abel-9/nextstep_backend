# Repository Interface
from src.context.identity_access.domain.ports import IVerificationRepository

# Aggregate
from src.context.identity_access.domain.entities import Verification

# Value Objects
from src.context.identity_access.domain.value_objects import EmailStr, VerificationType

# Mappers
from src.context.identity_access.infrastructure.mappers import VerificationMapper

# Beanie Models
from src.context.identity_access.infrastructure.models import VerificationModel


class VerificationBeanieRepository(IVerificationRepository):
    async def get_by_id(self, id):
        verification_model = await VerificationModel.find_one(
            VerificationModel.id == id
        )
        if verification_model:
            return VerificationMapper.from_beanie_verification(verification_model)
        return None

    async def get_all(self):
        verification_models = await VerificationModel.find_all().to_list()
        return [
            VerificationMapper.from_beanie_verification(verification_model)
            for verification_model in verification_models
        ]

    async def remove(self, entity):
        verification_model = await VerificationModel.find_one(
            VerificationModel.id == entity.id.value
        )
        if verification_model:
            await verification_model.delete()

    async def update(self, entity: Verification):
        verification_model = VerificationMapper.to_beanie_verification(entity)
        await verification_model.replace()

    async def save(self, entity: Verification):
        verification_model = VerificationMapper.to_beanie_verification(entity)
        await verification_model.insert()

    async def get_all_by_identity(self, identity: EmailStr) -> list[Verification]:
        verification_models = await VerificationModel.find(
            VerificationModel.identity == identity.value
        ).to_list()
        return [
            VerificationMapper.from_beanie_verification(verification_model)
            for verification_model in verification_models
        ]

    async def get_all_by_email_and_type(
        self, email: EmailStr, type: VerificationType
    ) -> list[Verification]:
        verification_models = await VerificationModel.find(
            (VerificationModel.identity == email.value),
            (VerificationModel.type == type.value),
        ).to_list()
        return [
            VerificationMapper.from_beanie_verification(verification_model)
            for verification_model in verification_models
        ]

    async def get_one_by_identity_type_token(self, identity, type, token):
        verification_model = await VerificationModel.find_one(
            (VerificationModel.identity == identity.value),
            (VerificationModel.type == type.value),
            (VerificationModel.token == token.value),
        )
        if verification_model:
            return VerificationMapper.from_beanie_verification(verification_model)
        return None
