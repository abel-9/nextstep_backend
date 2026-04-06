# Interface
from src.context.chat.domain.ports import IProfileDocumentRepository


class ProfileQdrantRepository(IProfileDocumentRepository):
    def __init__(self):
        pass

    def save(self, education):
        pass

    def update(self, education):
        pass
