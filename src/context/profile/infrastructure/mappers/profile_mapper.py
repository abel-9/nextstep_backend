from src.context.profile.domain.entities import Education, Profile, WorkExperience
from src.context.profile.domain.value_objects import (
    EducationId,
    ProfileId,
    WorkExperienceId,
)
from src.context.profile.infrastructure.models import (
    EducationModel,
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
                    id=work_experience.id.value,
                    company=work_experience.company,
                    position=work_experience.position,
                    description=work_experience.description,
                    start_date=work_experience.start_date,
                    end_date=work_experience.end_date,
                )
            )

        educations: list[EducationModel] = []
        for education in profile.educations:
            educations.append(
                EducationModel(
                    id=education.id.value,
                    major=education.major,
                    description=education.description,
                    start_date=education.start_date,
                    end_date=education.end_date,
                )
            )

        return ProfileModel(
            id=profile.id.value,
            user_id=profile.user_id.value,
            work_experiences=work_experiences,
            educations=educations,
        )

    @staticmethod
    def from_beanie_profile(profile_model: ProfileModel) -> Profile:
        work_experiences: list[WorkExperience] = []
        for work_experience_model in profile_model.work_experiences:
            work_experiences.append(
                WorkExperience(
                    id=WorkExperienceId(work_experience_model.id),
                    company=work_experience_model.company,
                    position=work_experience_model.position,
                    description=work_experience_model.description,
                    start_date=work_experience_model.start_date,
                    end_date=work_experience_model.end_date,
                )
            )

        educations: list[Education] = []
        for education_model in profile_model.educations:
            educations.append(
                Education(
                    id=EducationId(education_model.id),
                    major=education_model.major,
                    description=education_model.description,
                    start_date=education_model.start_date,
                    end_date=education_model.end_date,
                )
            )

        return Profile(
            id=ProfileId(profile_model.id),
            user_id=UserId(profile_model.user_id),
            work_experiences=work_experiences,
            educations=educations,
        )
