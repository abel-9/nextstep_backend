# interfaces
from src.context.chat.domain.ports import (
    IProfileDocumentRepository,
    IScholarshipDocumentRepository,
)

# Adapters
from src.context.chat.infrastructure.adapters import (
    ProfileQdrantRepository,
    ScholarshipQdrantRepository,
)

# use cases
from src.context.chat.application.command.use_case import (
    CreateEducationDocumentUseCase,
    CreateWorkExperienceDocumentUseCase,
    CreateScholarshipDocumentUseCase,
)

# Containers
from src.core.container import AppContainer
from src.context.shared_kernel.bootstrap.container import SharedContainer


class ChatContainer:
    def __init__(self, app_container: AppContainer, shared_container: SharedContainer):
        self.app_container = app_container
        self.shared_container = shared_container

    def get_profile_repository(self) -> IProfileDocumentRepository:
        if not self.app_container.vector_db:
            raise Exception("VectorDB is not initialized")
        return ProfileQdrantRepository(vector_db=self.app_container.vector_db)

    def get_create_education_document_use_case(self) -> CreateEducationDocumentUseCase:
        return CreateEducationDocumentUseCase(
            profile_document_repository=self.get_profile_repository(),
            embedding=self.shared_container.get_embeder(),
        )

    def get_create_work_experience_document_use_case(
        self,
    ) -> CreateWorkExperienceDocumentUseCase:
        return CreateWorkExperienceDocumentUseCase(
            profile_document_repository=self.get_profile_repository(),
            embedding=self.shared_container.get_embeder(),
        )

    def get_scholarship_repository(self) -> IScholarshipDocumentRepository:
        if not self.app_container.vector_db:
            raise Exception("VectorDB is not initialized")
        return ScholarshipQdrantRepository(vector_db=self.app_container.vector_db)

    def get_create_scholarship_document_use_case(
        self,
    ) -> CreateScholarshipDocumentUseCase:
        return CreateScholarshipDocumentUseCase(
            scholarship_document_repository=self.get_scholarship_repository(),
            embedding=self.shared_container.get_embeder(),
        )
