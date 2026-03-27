from src.context.shared_kernel.infrastructure.exceptions import InfrastructureException


class InvalidTokenError(InfrastructureException):
    def __init__(self):
        super().__init__("Invalid token")
