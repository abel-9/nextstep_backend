# Base Entity
from src.context.shared_kernel.domain.entities.entity import Entity

# Value Objects
from src.context.identity_access.domain.value_objects import AccountId, Provider

# Shared Kernel Value Objects
from src.context.shared_kernel.domain.value_objects.user_id import UserId

# Enums
from src.context.identity_access.domain.enums.provider_enums import ProviderEnums


class Account(Entity[AccountId]):
    def __init__(
        self,
        id: AccountId,
        provider: Provider,
        provider_id: str,
        secret: str | None,
        is_active: bool,
        is_verified: bool,
    ):
        super().__init__(id=id)
        self.__provider = provider
        self.__provider_id = provider_id
        self.__secret = secret
        self.__is_active = is_active
        self.__is_verified = is_verified

    @property
    def provider(self) -> Provider:
        return self.__provider

    @property
    def provider_id(self) -> str:
        return self.__provider_id

    @property
    def secret(self) -> str | None:
        return self.__secret

    @property
    def is_active(self) -> bool:
        return self.__is_active

    @property
    def is_verified(self) -> bool:
        return self.__is_verified

    @classmethod
    def create(
        cls,
        provider: Provider,
        provider_id: str,
        secret: str | None,
        is_active: bool,
        is_verified: bool,
    ) -> "Account":
        return cls(
            id=AccountId.generate(),
            provider=provider,
            provider_id=provider_id,
            secret=secret,
            is_active=is_active,
            is_verified=is_verified,
        )

    @classmethod
    def create_local(
        cls,
        user_id: UserId,
        secret: str,
    ) -> "Account":
        return cls.create(
            provider=Provider(ProviderEnums.LOCAL),
            provider_id=str(user_id.value),
            secret=secret,
            is_active=True,
            is_verified=False,
        )

    def activate(self) -> None:
        self.__is_active = True

    def deactivate(self) -> None:
        self.__is_active = False

    def verify(self) -> None:
        self.__is_verified = True

    def change_secret(self, new_secret: str) -> None:
        self.__secret = new_secret

    def is_local(self) -> bool:
        return self.__provider == Provider(ProviderEnums.LOCAL)

    def is_social(self, provider: Provider) -> bool:
        return self.__provider == provider
