from fastapi import Depends
from typing import Annotated

# the bus instance
from src.core.mediator import event_bus, get_mediator, request_bus
from src.core.broker import IMessageBroker

# handlers
from src.context.identity_access.application.command.handlers import (
    VerifyUserHandler,
    CreateSessionHandler,
)

# Use Cases
from src.context.identity_access.application.command.use_cases import (
    SignUpLocalUseCase,
    SignInLocalUseCase,
    VerifyEmailUseCase,
)

# query handlers
from src.context.identity_access.application.query.handlers import (
    GetUsersQueryHandler,
    GetUserByIdQueryHandler,
    GetMeQueryHandler,
)

# Dependencies
from .dependencies import (
    get_user_repository,
    get_user_query_repository,
    get_hash_service,
    get_verification_repository,
)

# Global Deps
from src.context.shared_kernel.dependencies import get_token_service


def register_identity_handlers(broker: IMessageBroker):
    # Events Buses
    event_bus.register(
        VerifyUserHandler(user_repository=get_user_repository(), message_broker=broker)
    )

    # Command Handlers
    request_bus.register(CreateSessionHandler(token_service=get_token_service()))

    request_bus.register(
        SignUpLocalUseCase(
            user_repository=get_user_repository(),
            hash_service=get_hash_service(),
            verification_repository=get_verification_repository(),
        )
    )

    # Inject the REAL broker instance here
    request_bus.register(
        SignInLocalUseCase(
            user_repository=get_user_repository(),
            hash_service=get_hash_service(),
            event_bus=get_mediator(),
            message_broker=broker,
        )
    )

    request_bus.register(
        VerifyEmailUseCase(
            verification_repository=get_verification_repository(),
            event_bus=get_mediator(),
        )
    )

    # Query Handlers
    request_bus.register(
        GetUsersQueryHandler(user_query_repository=get_user_query_repository())
    )
    request_bus.register(
        GetUserByIdQueryHandler(user_query_repository=get_user_query_repository())
    )
    request_bus.register(
        GetMeQueryHandler(
            user_query_repository=get_user_query_repository(),
            token_service=get_token_service(),
        )
    )
