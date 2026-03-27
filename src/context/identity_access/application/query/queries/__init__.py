from dataclasses import dataclass


@dataclass
class GetUsersQuery:
    page: int = 1
    page_size: int = 10
    is_verified: bool = None


@dataclass
class GetUserByIdQuery:
    user_id: str
