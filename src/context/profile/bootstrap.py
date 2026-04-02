# broker Interface
from src.context.shared_kernel.application.ports import IMessageBroker

# Handlers
from src.context.profile.application.command.handlers import create_profile_handler

# Use Cases
from src.context.profile.application.command.use_case import CreateProfileUseCase

# Query Handlers
from src.context.profile.application.query.handlers import (
    GetAllWorkExperiencesQueryHandler,
    GetAllEducationsQueryHandler,
    GetEducationQueryHandler,
    GetMyProfileQueryHandler,
    GetWorkExperienceQueryHandler,
)

# Enums
from src.context.shared_kernel.domain.enums import UserEventType

# Dependencies
from src.context.profile.dependencies import get_profile_repository, get_profile_query

# Shared Deps
from src.context.shared_kernel.dependencies import get_token_service

# Core dependencies
from src.core.mediator import request_bus

# Use Cases
from src.context.profile.application.command.use_case import (
    AddEducationUseCase,
    AddWorkExperienceUseCase,
)


async def register_profile_consumers(broker: IMessageBroker):
    await broker.consume(
        event_type=UserEventType.USER_VERIFIED,
        callback=create_profile_handler(
            use_case=CreateProfileUseCase(profile_repository=get_profile_repository())
        ),
    )


def register_profile_handlers():
    # Use Cases
    request_bus.register(
        AddWorkExperienceUseCase(
            profile_repository=get_profile_repository(),
            token_service=get_token_service(),
        )
    )
    request_bus.register(
        AddEducationUseCase(
            profile_repository=get_profile_repository(),
            token_service=get_token_service(),
        )
    )

    # Query Handlers
    request_bus.register(
        GetMyProfileQueryHandler(
            token_service=get_token_service(), profile_query=get_profile_query()
        )
    )
    request_bus.register(
        GetEducationQueryHandler(
            token_service=get_token_service(), profile_query=get_profile_query()
        )
    )
    request_bus.register(
        GetAllEducationsQueryHandler(
            token_service=get_token_service(), profile_query=get_profile_query()
        )
    )
    request_bus.register(
        GetAllWorkExperiencesQueryHandler(
            token_service=get_token_service(), profile_query=get_profile_query()
        )
    )
    request_bus.register(
        GetWorkExperienceQueryHandler(
            token_service=get_token_service(), profile_query=get_profile_query()
        )
    )
