from datetime import datetime

# Base Entity
from src.context.shared_kernel.domain.entities.entity import Entity

# Value Objects
from src.context.profile.domain.value_objects import EducationId


class Education(Entity[EducationId]):
    def __init__(
        self,
        id: EducationId,
        major: str,
        description: str,
        start_date: datetime,
        end_date: datetime | None = None,
    ):
        super().__init__(id=id)
        self.__major = major
        self.__description = description
        self.__start_date = start_date
        self.__end_date = end_date

    @property
    def major(self) -> str:
        return self.__major

    @property
    def start_date(self) -> datetime:
        return self.__start_date

    @property
    def end_date(self) -> datetime | None:
        return self.__end_date

    @property
    def description(self) -> str:
        return self.__description

    @classmethod
    def create(
        cls,
        major,
        description,
        start_date,
        end_date,
    ) -> "Education":
        education_id = EducationId.generate()
        return cls(
            id=education_id,
            description=description,
            major=major,
            start_date=start_date,
            end_date=end_date,
        )
