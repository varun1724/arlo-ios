import uuid
from datetime import datetime

from sqlalchemy import DateTime, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # SHA-256 hash of the device_id — raw device_id is never stored
    device_id_hash: Mapped[str] = mapped_column(Text, unique=True, nullable=False)
    # Opaque bearer token issued at registration. Replace this column with a
    # proper auth_methods table when adding Sign in with Apple or email auth.
    token: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), unique=True, nullable=False, default=uuid.uuid4)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    profile: Mapped["UserProfile"] = relationship("UserProfile", back_populates="user", uselist=False, cascade="all, delete-orphan")
    task_events: Mapped[list["TaskEvent"]] = relationship("TaskEvent", back_populates="user", cascade="all, delete-orphan")
