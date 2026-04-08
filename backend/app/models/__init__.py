# Import all models here so Alembic can discover them via Base.metadata
from app.models.user import User
from app.models.user_profile import UserProfile
from app.models.task_event import TaskEvent

__all__ = ["User", "UserProfile", "TaskEvent"]
