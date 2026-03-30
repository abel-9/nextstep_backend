from functools import lru_cache

# Repository Interface
from src.context.profile.domain.ports import IProfileRepository

# Adapters
from src.context.profile.infrastructure.adapters.repository.profile_beanie_repository import (
    ProfileBeanieRepository,
)

# Query Interfaces
from src.context.profile.application.query.ports import IProfileQuery

# Query Adapters
from src.context.profile.infrastructure.adapters.query import ProfileBeanieQuery


@lru_cache()
def get_profile_repository() -> IProfileRepository:
    """Factory function to get the Profile Repository instance."""
    return ProfileBeanieRepository()


@lru_cache()
def get_profile_query() -> IProfileQuery:
    return ProfileBeanieQuery()
