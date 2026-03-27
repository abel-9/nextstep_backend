from src.context.shared_kernel.infrastructure.exceptions import InfrastructureException


class TokenExpiredError(InfrastructureException):
    def __init__(self):
        super().__init__("Token has expired")
