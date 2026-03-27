# the bus instance
from src.core.mediator import event_bus, request_bus

# handlers
from src.context.identity_access.application.command.handlers import (
    VerifyUserHandler,
    CreateSessionHandler,
)

# query handlers
from src.context.identity_access.application.query.handlers import (
    GetUsersQueryHandler,
    GetUserByIdQueryHandler,
)

# Dependencies
from .dependencies import (
    get_user_repository,
    get_token_service,
    get_user_query_repository,
)


# Events Buses
event_bus.register(VerifyUserHandler(user_repository=get_user_repository()))

# Requests
request_bus.register(CreateSessionHandler(token_service=get_token_service()))
request_bus.register(
    GetUsersQueryHandler(user_query_repository=get_user_query_repository())
)
request_bus.register(
    GetUserByIdQueryHandler(user_query_repository=get_user_query_repository())
)
