# Profile context Container
from src.context.chat.api.bootstrap.container import ChatContainer


async def register_chat_handlers(container: ChatContainer):
    register_chat_command_handlers(container)


def register_chat_command_handlers(container: ChatContainer):
    container.app_container.mediator.get_event_bus().register(
        container.get_create_education_document_use_case()
    )
