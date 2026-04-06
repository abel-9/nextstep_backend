from enum import Enum


class SourceType(str, Enum):
    MANUAL = "manual"
    SCRAPED = "scraped"
    API = "api"
