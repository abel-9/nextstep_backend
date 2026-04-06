# Commands
from src.context.chat.application.command.commands import CreateEducationDocumentCommand


class CreateEducationDocumentUseCase:
    def __init__(self):
        pass

    async def __call__(self, cmd: CreateEducationDocumentCommand):
        print(cmd)
