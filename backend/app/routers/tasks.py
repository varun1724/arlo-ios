from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_current_user, get_db
from app.models.task_event import TaskEvent
from app.models.user import User
from app.schemas.task import TaskEventRequest, TaskEventResponse

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/event", response_model=TaskEventResponse, status_code=201)
async def log_task_event(
    body: TaskEventRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> TaskEventResponse:
    event = TaskEvent(
        user_id=current_user.id,
        task_category=body.task_category,
        task_title=body.task_title,
        plan_date=body.plan_date,
        status=body.status,
    )
    db.add(event)
    await db.commit()
    await db.refresh(event)
    return TaskEventResponse.model_validate(event)
