from enum import Enum


class ListingStatus(str, Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"
    EXPIRED = "expired"
