from qdrant_client.http import models

# Domain entities
from src.context.chat.domain.entities import (
    ProfileAggregate,
    ProfileDocument,
    EducationDocument,
    WorkExperienceDocument,
)

# Value objects
from src.context.chat.domain.enums import PointKindEnums
from src.context.chat.domain.value_objects import (
    ProfileId,
    UserId,
    ProfileMetadata,
    VectorId,
)
from src.context.chat.infrastructure.mappers.education_qdrant_mapper import (
    EducationQdrantMapper,
)
from src.context.chat.infrastructure.mappers.work_experience_qdrant_mapper import (
    WorkExperienceQdrantMapper,
)


class ProfileQdrantMapper:
    @staticmethod
    def to_qdrant_points(aggregate: ProfileAggregate) -> list[models.PointStruct]:
        if not aggregate.profile_document:
            return []

        document = aggregate.profile_document
        return [
            models.PointStruct(
                id=document.id.value,
                vector=document.vector,
                payload={
                    "kind": PointKindEnums.PROFILE.value,
                    "profile_id": document.metadata.profile_id,
                    "user_id": document.metadata.user_id,
                    "content": document.metadata.content,
                },
            )
        ]

    @staticmethod
    def from_qdrant_points(
        points: list[models.Record],
        profile_id: str,
        user_id: str,
    ) -> ProfileAggregate:
        educations: list[EducationDocument] = []
        work_experiences: list[WorkExperienceDocument] = []
        profile_document: ProfileDocument | None = None
        for point in points:
            payload = point.payload or {}

            if payload.get("kind") == PointKindEnums.PROFILE.value:
                vector = point.vector
                if isinstance(vector, dict):
                    vector = next(iter(vector.values()), [])

                profile_metadata = ProfileMetadata(
                    profile_id=payload.get("profile_id", profile_id),
                    user_id=payload.get("user_id", user_id),
                    content=payload.get("content", ""),
                )
                profile_document = ProfileDocument(
                    id=VectorId(str(point.id)),
                    vector=vector or [],
                    metadata=profile_metadata,
                )
                continue

            work_experience = WorkExperienceQdrantMapper.from_qdrant_point(
                point=point,
                profile_id=profile_id,
                user_id=user_id,
            )
            if work_experience is not None:
                work_experiences.append(work_experience)
                continue

            education = EducationQdrantMapper.from_qdrant_point(
                point=point,
                profile_id=profile_id,
                user_id=user_id,
            )
            if education is not None:
                educations.append(education)

        return ProfileAggregate(
            profile_id=ProfileId(value=profile_id),
            user_id=UserId(value=user_id),
            education_documents=educations,
            work_experience_documents=work_experiences,
            profile_document=profile_document,
        )
