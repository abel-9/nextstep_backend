from src.context.shared_kernel.domain.value_objects.id import Id


class WorkExperienceId(Id["WorkExperienceId"]):
    def __init__(self, value):
        super().__init__(value=value)
