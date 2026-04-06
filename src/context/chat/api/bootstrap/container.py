# interfaces
from src.context.chat.domain.ports import IProfileDocumentRepository

# Adapters
from src.context.chat.infrastructure.adapters import ProfileQdrantRepository

# use cases
from src.context.chat.application.command.use_case import CreateEducationDocumentUseCase

# Containers
from src.core.container import AppContainer
from src.context.shared_kernel.bootstrap.container import SharedContainer


class ChatContainer:
    def __init__(self, app_container: AppContainer, shared_container: SharedContainer):
        self.app_container = app_container
        self.shared_container = shared_container

    def get_education_repository(self) -> IProfileDocumentRepository:
        return ProfileQdrantRepository()

    def get_create_education_document_use_case(self) -> CreateEducationDocumentUseCase:
        return CreateEducationDocumentUseCase()
