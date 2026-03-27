# Aggregetes
from src.context.identity_access.domain.entities import User, Account

# Value Objects
from src.context.identity_access.domain.value_objects import (
    EmailStr,
    Provider,
    AccountId,
)

# Shared Kernel Value Objects
from src.context.shared_kernel.domain.value_objects.user_id import UserId

# Enums
from src.context.identity_access.domain.enums import ProviderEnums

# Beanie Models
from src.context.identity_access.infrastructure.models import UserModel, AccountModel


class UserMapper:
    @staticmethod
    def to_beanie_user(user: User) -> UserModel:
        accounts = []
        for account in user.accounts:
            accounts.append(
                AccountModel(
                    id=account.id.value,
                    provider=account.provider.value,
                    provider_id=account.provider_id,
                    secret=account.secret,
                    is_active=account.is_active,
                    is_verified=account.is_verified,
                )
            )

        return UserModel(
            id=user.id.value,
            email=user.email.value,
            accounts=accounts,
        )

    @staticmethod
    def from_beanie_user(user_model: UserModel) -> User:
        accounts = []
        for account_model in user_model.accounts:
            accounts.append(
                Account(
                    id=AccountId(account_model.id),
                    provider=Provider(ProviderEnums(account_model.provider)),
                    provider_id=account_model.provider_id,
                    secret=account_model.secret,
                    is_active=account_model.is_active,
                    is_verified=account_model.is_verified,
                )
            )

        return User(
            id=UserId(user_model.id),
            email=EmailStr(value=user_model.email),
            accounts=accounts,
        )
