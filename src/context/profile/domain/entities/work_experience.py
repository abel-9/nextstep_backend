from datetime import datetime


class WorkExperience:
    def __init__(
        self,
        company: str,
        position: str,
        start_date: datetime,
        end_date: datetime | None = None,
    ):
        self.__company = company
        self.__position = position
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
