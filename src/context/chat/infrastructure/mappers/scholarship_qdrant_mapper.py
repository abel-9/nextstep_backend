from qdrant_client.http import models

from src.context.chat.domain.entities import ScholarshipAggregate, ScholarshipDocument
from src.context.chat.domain.value_objects import ScholarshipMetadata, VectorId


class ScholarshipQdrantMapper:
    @staticmethod
    def to_qdrant_points(aggregate: ScholarshipAggregate) -> list[models.PointStruct]:
        if not aggregate.document:
            return []

        document = aggregate.document
        return [
            models.PointStruct(
                id=document.id.value,
                vector=document.vector,
                payload={
                    "kind": document.metadata.Kind,
                    "listing_id": document.metadata.listing_id,
                    "title": document.metadata.title,
                    "description": document.metadata.description,
                    "eligibility_summary": document.metadata.eligibility_summary,
                    "provider_name": document.metadata.provider_name,
                    "tags": document.metadata.tags,
                    "deadline": document.metadata.deadline,
                },
            )
        ]

    @staticmethod
    def from_qdrant_points(
        points: list[models.Record],
        listing_id: str,
    ) -> ScholarshipAggregate:
        document: ScholarshipDocument | None = None

        for point in points:
            payload = point.payload or {}
            vector = point.vector
            if isinstance(vector, dict):
                vector = next(iter(vector.values()), [])

            metadata = ScholarshipMetadata(
                listing_id=payload.get("listing_id", listing_id),
                title=payload.get("title", ""),
                description=payload.get("description", ""),
                eligibility_summary=payload.get("eligibility_summary", ""),
                provider_name=payload.get("provider_name", ""),
                tags=payload.get("tags", []),
                deadline=payload.get("deadline"),
            )
            document = ScholarshipDocument(
                id=VectorId(str(point.id)),
                vector=vector or [],
                scholarship_metadata=metadata,
            )
            break

        return ScholarshipAggregate(
            listing_id=listing_id,
            document=document,
        )
