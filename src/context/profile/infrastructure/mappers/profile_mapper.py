from src.context.profile.domain.entities import Profile, WorkExperience
from src.context.profile.domain.value_objects import ProfileId
from src.context.profile.infrustructure.models import (
    ProfileModel,
    WorkExperienceModel,
)
from src.context.shared_kernel.domain.value_objects import UserId


class ProfileMapper:
    @staticmethod
    def to_beanie_profile(profile: Profile) -> ProfileModel:
        work_experiences: list[WorkExperienceModel] = []
        for work_experience in profile.work_experiences:
            work_experiences.append(
                WorkExperienceModel(
                    company=work_experience.company,
                    position=work_experience.position,
                    start_date=work_experience.start_date,
                    end_date=work_experience.end_date,
                )
            )

        return ProfileModel(
            id=profile.id.value,
            user_id=profile.user_id.value,
            work_experiences=work_experiences,
        )

    @staticmethod
    def from_beanie_profile(profile_model: ProfileModel) -> Profile:
        work_experiences: list[WorkExperience] = []
        for work_experience_model in profile_model.work_experiences:
            work_experiences.append(
                WorkExperience(
                    company=work_experience_model.company,
                    position=work_experience_model.position,
                    start_date=work_experience_model.start_date,
                    end_date=work_experience_model.end_date,
                )
            )

        return Profile(
            id=ProfileId(profile_model.id),
            user_id=UserId(profile_model.user_id),
            work_experiences=work_experiences,
        )
