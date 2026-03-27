# Base Entity
from src.context.shared_kernel.domain.entities.entity import Entity

# Entities
from src.context.identity_access.domain.entities.account import Account

# Value Objects
from src.context.identity_access.domain.value_objects import EmailStr, Provider

# Shared Kernel Value Objects
from src.context.shared_kernel.domain.value_objects import UserId

# Enums
from src.context.identity_access.domain.enums.provider_enums import ProviderEnums

# Exceptions
from src.context.identity_access.domain.exceptions import AccountAlreadyExists
from src.context.identity_access.domain.exceptions import AccountNotFound


class User(Entity[UserId]):
    def __init__(self, id: UserId, email: EmailStr, accounts: list[Account]):
        super().__init__(id=id)
        self.__email = email
        self.__accounts = accounts

    @property
    def email(self) -> EmailStr:
        return self.__email

    @property
    def accounts(self) -> list[Account]:
        return self.__accounts

    @classmethod
    def create(cls, email: EmailStr) -> "User":
        return cls(id=UserId.generate(), email=email, accounts=[])

    def __add_account(self, account: Account) -> None:
        self.__accounts.append(account)

    def __register_account(
        self,
        provider: Provider,
        provider_id: str,
        secret: str | None,
        is_active: bool,
        is_verified: bool,
    ) -> Account:
        account = Account.create(
            provider=provider,
            provider_id=provider_id,
            secret=secret,
            is_active=is_active,
            is_verified=is_verified,
        )
        self.__add_account(account)
        return account

    def register_local_account(
        self,
        secret: str,
    ) -> Account:
        local_account = next(
            (account for account in self.__accounts if account.is_local()), None
        )
        if local_account and local_account.is_verified:
            raise AccountAlreadyExists(ProviderEnums.LOCAL.value)
        elif local_account and not local_account.is_verified:
            self.__accounts.remove(local_account)

        return self.__register_account(
            provider=Provider(ProviderEnums.LOCAL),
            provider_id=self.id.value,
            secret=secret,
            is_active=True,
            is_verified=False,
        )

    def register_social_account(self, provider: Provider, provider_id: str):
        social_provider_exists = False
        for account in self.__accounts:
            if account.is_social(provider):
                social_provider_exists = True
                break

        if social_provider_exists:
            return

        return self.__register_account(
            provider=provider,
            provider_id=provider_id,
            secret=None,
            is_active=True,
            is_verified=True,
        )

    def compare_local_account_secret(self, secret: str) -> bool:
        local_account = next(
            (account for account in self.__accounts if account.is_local()), None
        )
        if not local_account:
            raise AccountNotFound(ProviderEnums.LOCAL.value)

        return local_account.secret == secret

    def verify_local_email(self) -> None:
        local_account = next(
            (account for account in self.__accounts if account.is_local()), None
        )
        if not local_account:
            raise AccountNotFound(ProviderEnums.LOCAL.value)

        local_account.verify()
