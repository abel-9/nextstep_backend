from src.context.shared_kernel.domain.exceptions import DomainException


class UserNotFoundError(DomainException):
    def __init__(self, email: str):
        super().__init__(f"User with email '{email}' was not found.")
