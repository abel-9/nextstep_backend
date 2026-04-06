# Profile context Container
from src.context.profile.api.bootstrap.container import ProfileContainer


async def register_profile_handlers(container: ProfileContainer):
    register_profile_command_handlers(container)
    register_profile_query_handlers(container)


def register_profile_command_handlers(container: ProfileContainer):
    container.app_container.mediator.get_request_bus().register(
        container.get_add_work_experience_use_case()
    )
    container.app_container.mediator.get_request_bus().register(
        container.get_add_education_use_case()
    )


def register_profile_query_handlers(container: ProfileContainer):
    container.app_container.mediator.get_request_bus().register(
        container.get_my_profile_query_handler()
    )
    container.app_container.mediator.get_request_bus().register(
        container.get_education_query_handler()
    )
    container.app_container.mediator.get_request_bus().register(
        container.get_all_educations_query_handler()
    )
    container.app_container.mediator.get_request_bus().register(
        container.get_all_work_experiences_query_handler()
    )
    container.app_container.mediator.get_request_bus().register(
        container.get_work_experience_query_handler()
    )
