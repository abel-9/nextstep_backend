from src.context.shared_kernel.domain.exceptions import DomainException


class AccountAlreadyExists(DomainException):
    def __init__(self, provider: str):
        super().__init__(f"An account with provider '{provider}' already exists.")
