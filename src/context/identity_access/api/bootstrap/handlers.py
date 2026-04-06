from src.context.identity_access.api.bootstrap.container import IdentityAccessContainer


def register_identity_access_handlers(container: IdentityAccessContainer):
    register_identity_access_event_handlers(container)
    register_identity_access_command_handlers(container)
    register_identity_access_query_handlers(container)


def register_identity_access_event_handlers(container: IdentityAccessContainer):
    # event_bus.register(container.get_verify_user_handler())
    _ = container


def register_identity_access_command_handlers(container: IdentityAccessContainer):
    container.app_container.mediator.get_request_bus().register(
        container.get_create_session_handler()
    )
    container.app_container.mediator.get_request_bus().register(
        container.get_sign_up_local_use_case()
    )
    container.app_container.mediator.get_request_bus().register(
        container.get_sign_in_local_use_case()
    )
    container.app_container.mediator.get_request_bus().register(
        container.get_verify_email_use_case()
    )


def register_identity_access_query_handlers(container: IdentityAccessContainer):
    container.app_container.mediator.get_request_bus().register(
        container.get_users_query_handler()
    )
    container.app_container.mediator.get_request_bus().register(
        container.get_user_by_id_query_handler()
    )
    container.app_container.mediator.get_request_bus().register(
        container.get_me_query_handler()
    )
