from qdrant_client.http import models

from src.context.chat.domain.entities import ProfileAggregate, WorkExperienceDocument
from src.context.chat.domain.enums import PointKindEnums
from src.context.chat.domain.value_objects import WorkExperienceMetadata, VectorId


class WorkExperienceQdrantMapper:
    @staticmethod
    def to_qdrant_points(aggregate: ProfileAggregate) -> list[models.PointStruct]:
        points: list[models.PointStruct] = []
        for work_experience in aggregate.work_experience_documents:
            points.append(
                models.PointStruct(
                    id=work_experience.id.value,
                    vector=work_experience.vector,
                    payload={
                        "kind": work_experience.metadata.Kind,
                        "work_experience_id": work_experience.metadata.work_experience_id,
                        "profile_id": work_experience.metadata.profile_id,
                        "user_id": work_experience.metadata.user_id,
                        "company": work_experience.metadata.company,
                        "position": work_experience.metadata.position,
                        "description": work_experience.metadata.description,
                    },
                )
            )

        return points

    @staticmethod
    def from_qdrant_point(
        point: models.Record,
        profile_id: str,
        user_id: str,
    ) -> WorkExperienceDocument | None:
        payload = point.payload or {}
        if payload.get("kind") != PointKindEnums.WORK_EXPERIENCE.value:
            return None

        vector = point.vector
        if isinstance(vector, dict):
            vector = next(iter(vector.values()), [])

        metadata = WorkExperienceMetadata(
            work_experience_id=payload.get("work_experience_id", ""),
            profile_id=payload.get("profile_id", profile_id),
            user_id=payload.get("user_id", user_id),
            company=payload.get("company", ""),
            position=payload.get("position", ""),
            description=payload.get("description", ""),
        )

        return WorkExperienceDocument(
            id=VectorId(str(point.id)),
            vector=vector or [],
            work_experience_metadata=metadata,
        )
