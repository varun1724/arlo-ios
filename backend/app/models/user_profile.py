import uuid
from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, Text, func
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class UserProfile(Base):
    __tablename__ = "user_profiles"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), primary_key=True
    )
    workout_split: Mapped[list[str]] = mapped_column(ARRAY(Text), nullable=False, server_default="{}")
    step_target: Mapped[int] = mapped_column(Integer, nullable=False, server_default="10000")
    meal_style: Mapped[str] = mapped_column(Text, nullable=False, server_default="homeCookedMostly")
    posture_minutes: Mapped[int] = mapped_column(Integer, nullable=False, server_default="8")
    learning_interests: Mapped[list[str]] = mapped_column(ARRAY(Text), nullable=False, server_default="{}")
    gym_name: Mapped[str | None] = mapped_column(Text)
    gym_lat: Mapped[float | None] = mapped_column(Float)
    gym_lon: Mapped[float | None] = mapped_column(Float)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    user: Mapped["User"] = relationship("User", back_populates="profile")
