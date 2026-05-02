from pydantic import BaseModel, computed_field, Field, constr

PROFICIENCY_LEVELS: list[tuple[int, str]] = [
    (80, 'Expert'),
    (70, 'Very Comfortable'),
    (55, 'Comfortable'),
    (40, 'Basic'),
]


def get_proficiency_label(score: int) -> str:
    # Sorting ensures the logic doesn't break if the list order changes
    sorted_levels = sorted(PROFICIENCY_LEVELS, key=lambda x: x, reverse=True)
    thresholds = (label for threshold, label in sorted_levels if score >= threshold)
    return next(thresholds, 'Beginner')


class Skill(BaseModel):
    model_config = {"frozen": True}
    name: str
    proficiency: int = Field(gt=0, le=100)

    @computed_field
    @property
    def proficiency_label(self) -> str:
        label = get_proficiency_label(self.proficiency)
        return f"{label} ({self.proficiency}%)"
