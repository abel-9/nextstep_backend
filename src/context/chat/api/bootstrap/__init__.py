# Containers
from src.core.container import AppContainer
from src.context.shared_kernel.bootstrap.container import SharedContainer
from src.context.chat.api.bootstrap.container import ChatContainer

# bootstrap functions
from src.context.chat.api.bootstrap.consumers import register_chat_consumers
from src.context.chat.api.bootstrap.handlers import register_chat_handlers


async def bootstrap_chat_module(
    app_container: AppContainer, shared_container: SharedContainer
):
    chat_container = ChatContainer(app_container, shared_container)
    await register_chat_consumers(chat_container)
    await register_chat_handlers(chat_container)
