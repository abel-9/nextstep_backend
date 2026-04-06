# Document Entities
from src.context.chat.domain.entities.education_document import EducationDocument

# Shared Kernel Value Objects
from src.context.chat.domain.value_objects import UserId, ProfileId


class ProfileAggregate:
    def __init__(
        self,
        profile_id: ProfileId,
        user_id: UserId,
        education_documents: list[EducationDocument],
    ):
        self.__profile_id = profile_id
        self.__user_id = user_id
        self.__education_documents = education_documents

    @property
    def profile_id(self) -> ProfileId:
        return self.__profile_id

    @property
    def user_id(self) -> UserId:
        return self.__user_id

    @property
    def education_document(self) -> list[EducationDocument]:
        return self.__education_documents

    @classmethod
    def create(
        cls,
        profile_id: ProfileId,
        user_id: UserId,
        education_documents: list[EducationDocument],
    ):
        return cls(
            profile_id,
            user_id,
            education_documents,
        )
