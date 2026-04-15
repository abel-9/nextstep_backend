# Document Entities
from src.context.chat.domain.entities.education_document import EducationDocument
from src.context.chat.domain.entities.work_experience_document import (
    WorkExperienceDocument,
)
from src.context.chat.domain.entities.profile_document import ProfileDocument

# Shared Kernel Value Objects
from src.context.chat.domain.value_objects import (
    UserId,
    ProfileId,
    EducationMetadata,
    WorkExperienceMetadata,
    ProfileMetadata,
)


class ProfileAggregate:
    def __init__(
        self,
        profile_id: ProfileId,
        user_id: UserId,
        education_documents: list[EducationDocument],
        work_experience_documents: list[WorkExperienceDocument],
        profile_document: ProfileDocument | None,
    ):
        self.__profile_id = profile_id
        self.__user_id = user_id
        self.__education_documents = education_documents
        self.__work_experience_documents = work_experience_documents
        self.__profile_document = profile_document

    @property
    def profile_id(self) -> ProfileId:
        return self.__profile_id

    @property
    def user_id(self) -> UserId:
        return self.__user_id

    @property
    def education_document(self) -> list[EducationDocument]:
        return self.__education_documents

    @property
    def work_experience_documents(self) -> list[WorkExperienceDocument]:
        return self.__work_experience_documents

    @property
    def profile_document(self) -> ProfileDocument:
        return self.__profile_document

    def compose_profile_content(self) -> str:
        education_lines = [
            f"- {education.content().replace(chr(10), ' | ')}"
            for education in self.__education_documents
        ]
        work_experience_lines = [
            f"- {work_experience.content().replace(chr(10), ' | ')}"
            for work_experience in self.__work_experience_documents
        ]

        education_section = (
            "Education:\n" + "\n".join(education_lines)
            if education_lines
            else "Education:\n- None"
        )
        work_experience_section = (
            "Work Experience:\n" + "\n".join(work_experience_lines)
            if work_experience_lines
            else "Work Experience:\n- None"
        )

        return (
            f"Profile ID: {self.__profile_id.value}\n"
            f"User ID: {self.__user_id.value}\n\n"
            f"{education_section}\n\n{work_experience_section}"
        )

    def upsert_profile_document(self, vector: list[float]) -> None:
        metadata = ProfileMetadata(
            profile_id=self.__profile_id.value,
            user_id=self.__user_id.value,
            content=self.compose_profile_content(),
        )

        if self.__profile_document:
            self.__profile_document.update_metadata(metadata=metadata, vector=vector)
            return

        self.__profile_document = ProfileDocument.create(
            vector=vector,
            metadata=metadata,
        )

    def upsert_education(
        self,
        metadata: EducationMetadata,
        vector: list[float],
    ) -> None:
        self.__assert_metadata_belongs_to_aggregate(metadata)

        existing = self.__find_education(metadata.education_id)
        if existing:
            existing.update_metadata(metadata=metadata, vector=vector)
            return

        self.__education_documents.append(
            EducationDocument.create(
                vector=vector,
                education_metadata=metadata,
            )
        )

    def upsert_work_experience(
        self,
        metadata: WorkExperienceMetadata,
        vector: list[float],
    ) -> None:
        self.__assert_metadata_belongs_to_aggregate(metadata)

        existing = self.__find_work_experience(metadata.work_experience_id)
        if existing:
            existing.update_metadata(metadata=metadata, vector=vector)
            return

        self.__work_experience_documents.append(
            WorkExperienceDocument.create(
                vector=vector,
                work_experience_metadata=metadata,
            )
        )

    @classmethod
    def create(
        cls,
        profile_id: ProfileId,
        user_id: UserId,
        education_documents: list[EducationDocument],
        work_experience_documents: list[WorkExperienceDocument],
    ):
        new_profile_metadata = ProfileMetadata(
            profile_id=profile_id.value, user_id=user_id.value, content=""
        )
        new_profile_document = ProfileDocument.create(
            vector=[],
            metadata=new_profile_metadata,
        )
        return cls(
            profile_id,
            user_id,
            education_documents,
            work_experience_documents,
            new_profile_document,
        )

    def __find_education(self, education_id: str) -> EducationDocument | None:
        for education in self.__education_documents:
            if education.metadata.education_id == education_id:
                return education
        return None

    def __find_work_experience(
        self, work_experience_id: str
    ) -> WorkExperienceDocument | None:
        for work_experience in self.__work_experience_documents:
            if work_experience.metadata.work_experience_id == work_experience_id:
                return work_experience
        return None

    def __assert_metadata_belongs_to_aggregate(
        self, metadata: EducationMetadata | WorkExperienceMetadata
    ) -> None:
        if metadata.profile_id != self.__profile_id.value:
            raise Exception("Profile mismatch")

        if metadata.user_id != self.__user_id.value:
            raise Exception("User mismatch")
