from datetime import datetime

# Base Entiry
from src.context.shared_kernel.domain.entities.entity import Entity

# Value Objects
from src.context.profile.domain.value_objects import WorkExperienceId


class WorkExperience(Entity[WorkExperienceId]):
    def __init__(
        self,
        id: WorkExperienceId,
        company: str,
        position: str,
        description: str,
        start_date: datetime,
        end_date: datetime | None = None,
    ):
        super().__init__(id=id)
        self.__company = company
        self.__position = position
        self.__description = description
        self.__start_date = start_date
        self.__end_date = end_date

    @property
    def company(self) -> str:
        return self.__company

    @property
    def position(self) -> str:
        return self.__position

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
        company,
        position,
        description,
        start_date,
        end_date,
    ) -> "WorkExperience":
        work_exp_id = WorkExperienceId.generate()
        return cls(
            id=work_exp_id,
            description=description,
            company=company,
            position=position,
            start_date=start_date,
            end_date=end_date,
        )
