from qdrant_client.http import models

from src.context.chat.domain.entities import ProfileAggregate, EducationDocument
from src.context.chat.domain.enums import PointKindEnums
from src.context.chat.domain.value_objects import EducationMetadata, VectorId


class EducationQdrantMapper:
    @staticmethod
    def to_qdrant_points(aggregate: ProfileAggregate) -> list[models.PointStruct]:
        points: list[models.PointStruct] = []
        for education in aggregate.education_document:
            points.append(
                models.PointStruct(
                    id=education.id.value,
                    vector=education.vector,
                    payload={
                        "kind": education.metadata.Kind,
                        "education_id": education.metadata.education_id,
                        "profile_id": education.metadata.profile_id,
                        "user_id": education.metadata.user_id,
                        "major": education.metadata.major,
                        "description": education.metadata.description,
                    },
                )
            )

        return points

    @staticmethod
    def from_qdrant_point(
        point: models.Record,
        profile_id: str,
        user_id: str,
    ) -> EducationDocument | None:
        payload = point.payload or {}
        if payload.get("kind") != PointKindEnums.EDUCATION.value:
            return None

        vector = point.vector
        if isinstance(vector, dict):
            vector = next(iter(vector.values()), [])

        metadata = EducationMetadata(
            education_id=payload.get("education_id", ""),
            profile_id=payload.get("profile_id", profile_id),
            user_id=payload.get("user_id", user_id),
            major=payload.get("major", ""),
            description=payload.get("description", ""),
        )

        return EducationDocument(
            id=VectorId(str(point.id)),
            vector=vector or [],
            education_metadata=metadata,
        )
