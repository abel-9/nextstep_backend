from datetime import date

from src.context.shared_kernel.domain.entities.entity import Entity
from src.context.scholarship.domain.enums import ListingStatus
from src.context.scholarship.domain.value_object import (
    ListingId,
    Location,
    Money,
    Provider,
    Source,
    Url,
)


class ScholarshipListing(Entity[ListingId]):
    def __init__(
        self,
        id: ListingId,
        title: str,
        description: str,
        provider: Provider,
        external_url: Url,
        amount: Money | None,
        deadline: date | None,
        eligibility_summary: str,
        tags: list[str],
        location: Location,
        status: ListingStatus,
        source: Source,
        created_at: date,
        updated_at: date,
    ):
        super().__init__(id=id)
        self.__title = title
        self.__description = description
        self.__provider = provider
        self.__external_url = external_url
        self.__amount = amount
        self.__deadline = deadline
        self.__eligibility_summary = eligibility_summary
        self.__tags = self.__normalize_tags(tags)
        self.__location = location
        self.__status = status
        self.__source = source
        self.__created_at = created_at
        self.__updated_at = updated_at

    @property
    def title(self) -> str:
        return self.__title

    @property
    def description(self) -> str:
        return self.__description

    @property
    def provider(self) -> Provider:
        return self.__provider

    @property
    def external_url(self) -> Url:
        return self.__external_url

    @property
    def amount(self) -> Money | None:
        return self.__amount

    @property
    def deadline(self) -> date | None:
        return self.__deadline

    @property
    def eligibility_summary(self) -> str:
        return self.__eligibility_summary

    @property
    def tags(self) -> list[str]:
        return self.__tags

    @property
    def location(self) -> Location:
        return self.__location

    @property
    def status(self) -> ListingStatus:
        return self.__status

    @property
    def source(self) -> Source:
        return self.__source

    @property
    def created_at(self) -> date:
        return self.__created_at

    @property
    def updated_at(self) -> date:
        return self.__updated_at

    @classmethod
    def create(
        cls,
        title: str,
        description: str,
        provider: Provider,
        external_url: Url,
        eligibility_summary: str,
        tags: list[str],
        location: Location,
        source: Source,
        amount: Money | None = None,
        deadline: date | None = None,
    ) -> "ScholarshipListing":
        today = date.today()
        validated_title = cls.__validate_non_empty(title, "title")
        validated_description = cls.__validate_non_empty(description, "description")
        validated_eligibility_summary = cls.__validate_non_empty(
            eligibility_summary, "eligibility_summary"
        )
        normalized_tags = cls.__normalize_tags(tags)
        return cls(
            id=ListingId.generate(),
            title=validated_title,
            description=validated_description,
            provider=provider,
            external_url=external_url,
            amount=amount,
            deadline=deadline,
            eligibility_summary=validated_eligibility_summary,
            tags=normalized_tags,
            location=location,
            status=ListingStatus.DRAFT,
            source=source,
            created_at=today,
            updated_at=today,
        )

    def publish(self) -> None:
        if self.__status in {ListingStatus.ARCHIVED, ListingStatus.EXPIRED}:
            raise ValueError("Archived or expired listings cannot be published.")
        self.__status = ListingStatus.PUBLISHED
        self.__touch()

    def archive(self) -> None:
        self.__status = ListingStatus.ARCHIVED
        self.__touch()

    def update_metadata(
        self,
        title: str | None = None,
        description: str | None = None,
        external_url: Url | None = None,
        amount: Money | None = None,
        deadline: date | None = None,
        eligibility_summary: str | None = None,
        tags: list[str] | None = None,
        location: Location | None = None,
    ) -> None:
        if title is not None:
            self.__title = self.__validate_non_empty(title, "title")
        if description is not None:
            self.__description = self.__validate_non_empty(description, "description")
        if external_url is not None:
            self.__external_url = external_url
        if amount is not None:
            self.__amount = amount
        if deadline is not None:
            self.__deadline = deadline
        if eligibility_summary is not None:
            self.__eligibility_summary = self.__validate_non_empty(
                eligibility_summary, "eligibility_summary"
            )
        if tags is not None:
            self.__tags = self.__normalize_tags(tags)
        if location is not None:
            self.__location = location
        self.__touch()

    def refresh_from_source(
        self,
        source: Source,
        title: str | None = None,
        description: str | None = None,
        amount: Money | None = None,
        deadline: date | None = None,
        eligibility_summary: str | None = None,
        tags: list[str] | None = None,
        external_url: Url | None = None,
    ) -> None:
        self.__source = source
        self.update_metadata(
            title=title,
            description=description,
            external_url=external_url,
            amount=amount,
            deadline=deadline,
            eligibility_summary=eligibility_summary,
            tags=tags,
        )

    def mark_expired(self) -> None:
        if self.__status == ListingStatus.ARCHIVED:
            return
        if self.__deadline is not None and self.__deadline <= date.today():
            self.__status = ListingStatus.EXPIRED
            self.__touch()

    def validate_link(self) -> bool:
        try:
            Url(self.__external_url.value)
            return True
        except ValueError:
            return False

    def __touch(self) -> None:
        self.__updated_at = date.today()

    @staticmethod
    def __validate_non_empty(value: str, field_name: str) -> str:
        normalized = value.strip()
        if not normalized:
            raise ValueError(f"{field_name} cannot be empty.")
        return normalized

    def __normalize_tags(self, tags: list[str]) -> list[str]:
        cleaned_tags = []
        for tag in tags:
            normalized = tag.strip().lower()
            if normalized and normalized not in cleaned_tags:
                cleaned_tags.append(normalized)
        return cleaned_tags
