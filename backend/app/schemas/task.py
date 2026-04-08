import uuid
from datetime import date, datetime

from pydantic import BaseModel


class TaskEventRequest(BaseModel):
    task_category: str
    task_title: str
    plan_date: date
    status: str  # "done" | "skipped" | "snoozed"


class TaskEventResponse(BaseModel):
    id: uuid.UUID
    recorded_at: datetime

    model_config = {"from_attributes": True}
