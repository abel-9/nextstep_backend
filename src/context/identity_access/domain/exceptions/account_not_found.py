from src.context.shared_kernel.domain.exceptions import DomainException


class AccountNotFound(DomainException):
    def __init__(self, provider: str):
        super().__init__(f"No account found for provider '{provider}'.")
