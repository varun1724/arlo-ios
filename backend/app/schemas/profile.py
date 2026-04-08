from datetime import datetime

from pydantic import BaseModel


class UserProfileResponse(BaseModel):
    workout_split: list[str]
    step_target: int
    meal_style: str
    posture_minutes: int
    learning_interests: list[str]
    gym_name: str | None
    gym_lat: float | None
    gym_lon: float | None
    updated_at: datetime | None

    model_config = {"from_attributes": True}


class UserProfileUpdate(BaseModel):
    """All fields optional — only provided fields are updated."""
    workout_split: list[str] | None = None
    step_target: int | None = None
    meal_style: str | None = None
    posture_minutes: int | None = None
    learning_interests: list[str] | None = None
    gym_name: str | None = None
    gym_lat: float | None = None
    gym_lon: float | None = None
