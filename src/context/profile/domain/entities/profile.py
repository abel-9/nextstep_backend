# Base Entity class
from src.context.shared_kernel.domain.entities.entity import Entity

# Entities
from src.context.profile.domain.entities.work_experience import WorkExperience
from src.context.profile.domain.entities.education import Education

# ValueObjects
from src.context.profile.domain.value_objects import ProfileId

# Shared Kernel Value Objects
from src.context.shared_kernel.domain.value_objects.user_id import UserId


class Profile(Entity[ProfileId]):
    def __init__(
        self,
        id: ProfileId,
        user_id: UserId,
        work_experiences: list[WorkExperience],
        educations: list[Education],
    ):
        super().__init__(id=id)
        self.__user_id = user_id
        self.__work_experiences = work_experiences
        self.__educations = educations

    @property
    def user_id(self) -> UserId:
        return self.__user_id

    @property
    def work_experiences(self) -> list[WorkExperience]:
        return self.__work_experiences

    @property
    def educations(self) -> list[Education]:
        return self.__educations

    @classmethod
    def create(cls, user_id: UserId) -> "Profile":
        # Here you can add any domain logic related to profile creation
        profile_id = ProfileId.generate()  # Generate a new unique ID for the profile
        return cls(id=profile_id, user_id=user_id, work_experiences=[], educations=[])

    def add_work_experience(
        self,
        company,
        position,
        description,
        start_date,
        end_date,
    ):
        work_exp = WorkExperience.create(
            company,
            position,
            description,
            start_date,
            end_date,
        )

        self.__work_experiences.append(work_exp)

    def add_education(
        self,
        major,
        description,
        start_date,
        end_date,
    ):
        education = Education.create(
            major,
            description,
            start_date,
            end_date,
        )

        self.__educations.append(education)

    def is_for_user(self, user_id: UserId) -> bool:
        return self.__user_id == user_id
