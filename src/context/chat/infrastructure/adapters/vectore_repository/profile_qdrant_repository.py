from qdrant_client.http import models

# Interface
from src.core.interfaces import IVectorDB
from src.context.chat.domain.ports import IProfileDocumentRepository
from src.context.chat.domain.enums import PointKindEnums

# Domain entities
from src.context.chat.domain.entities import ProfileAggregate

# Mapper
from src.context.chat.infrastructure.mappers import (
    ProfileQdrantMapper,
    EducationQdrantMapper,
    WorkExperienceQdrantMapper,
)


class ProfileQdrantRepository(IProfileDocumentRepository):
    def __init__(self, vector_db: IVectorDB):
        self.__vector_db = vector_db

    async def get_by_profile_id(
        self, profile_id: str, user_id: str
    ) -> ProfileAggregate | None:
        client = self.__vector_db.get_client()
        points, _ = await client.scroll(
            collection_name=self.__vector_db.collection_name,
            scroll_filter=models.Filter(
                must=[
                    models.FieldCondition(
                        key="kind",
                        match=models.MatchAny(
                            any=[
                                PointKindEnums.EDUCATION.value,
                                PointKindEnums.WORK_EXPERIENCE.value,
                                PointKindEnums.PROFILE.value,
                            ]
                        ),
                    ),
                    models.FieldCondition(
                        key="profile_id",
                        match=models.MatchValue(value=profile_id),
                    ),
                    models.FieldCondition(
                        key="user_id",
                        match=models.MatchValue(value=user_id),
                    ),
                ]
            ),
            with_payload=True,
            with_vectors=True,
            limit=1000,
        )

        if not points:
            return None

        return ProfileQdrantMapper.from_qdrant_points(
            points=points,
            profile_id=profile_id,
            user_id=user_id,
        )

    async def save(self, profile_aggregate: ProfileAggregate) -> None:
        await self.__upsert_education_documents(profile_aggregate)
        await self.__upsert_work_experience_documents(profile_aggregate)
        await self.__upsert_profile_document(profile_aggregate)

    async def update(self, profile_aggregate: ProfileAggregate) -> None:
        await self.__upsert_education_documents(profile_aggregate)
        await self.__upsert_work_experience_documents(profile_aggregate)
        await self.__upsert_profile_document(profile_aggregate)

    async def __upsert_education_documents(self, aggregate: ProfileAggregate) -> None:
        points = EducationQdrantMapper.to_qdrant_points(aggregate=aggregate)

        if not points:
            return

        client = self.__vector_db.get_client()
        await client.upsert(
            collection_name=self.__vector_db.collection_name,
            points=points,
        )

    async def __upsert_profile_document(self, aggregate: ProfileAggregate) -> None:
        points = ProfileQdrantMapper.to_qdrant_points(aggregate=aggregate)

        if not points:
            return

        client = self.__vector_db.get_client()
        await client.upsert(
            collection_name=self.__vector_db.collection_name,
            points=points,
        )

    async def __upsert_work_experience_documents(
        self, aggregate: ProfileAggregate
    ) -> None:
        points = WorkExperienceQdrantMapper.to_qdrant_points(aggregate=aggregate)

        if not points:
            return

        client = self.__vector_db.get_client()
        await client.upsert(
            collection_name=self.__vector_db.collection_name,
            points=points,
        )
