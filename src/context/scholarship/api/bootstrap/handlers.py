from src.context.scholarship.api.bootstrap.container import ScholarshipContainer


def register_scholarship_handlers(container: ScholarshipContainer):
    register_scholarship_command_handlers(container)
    register_scholarship_query_handlers(container)


def register_scholarship_command_handlers(container: ScholarshipContainer):
    container.app_container.mediator.get_request_bus().register(
        container.get_create_scholarship_listing_use_case()
    )


def register_scholarship_query_handlers(container: ScholarshipContainer):
    container.app_container.mediator.get_request_bus().register(
        container.get_scholarship_listing_query_handler()
    )
    container.app_container.mediator.get_request_bus().register(
        container.get_scholarship_listings_query_handler()
    )
