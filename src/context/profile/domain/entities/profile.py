# Base Entity class
from src.context.shared_kernel.domain.entities.entity import Entity

# Entities
from src.context.profile.domain.entities.work_experience import WorkExperience

# ValueObjects
from src.context.profile.domain.value_objects.profile_id import ProfileId

# Shared Kernel Value Objects
from src.context.shared_kernel.domain.value_objects.user_id import UserId


class Profile(Entity[ProfileId]):
    def __init__(
        self,
        id: ProfileId,
        user_id: UserId,
        work_experiences: list[WorkExperience],
    ):
        super().__init__(id=id)
        self.__user_id = user_id
        self.__work_experiences = work_experiences

    @property
    def user_id(self) -> UserId:
        return self.__user_id

    @property
    def work_experiences(self) -> list[WorkExperience]:
        return self.__work_experiences

    def add_work_experience(self, work_experience: WorkExperience):
        self.__work_experiences.append(work_experience)
