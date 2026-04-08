from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_current_user, get_db
from app.models.user import User
from app.schemas.profile import UserProfileResponse, UserProfileUpdate

router = APIRouter(prefix="/profile", tags=["profile"])


@router.get("", response_model=UserProfileResponse)
async def get_profile(current_user: User = Depends(get_current_user)) -> UserProfileResponse:
    return UserProfileResponse.model_validate(current_user.profile)


@router.put("", response_model=UserProfileResponse)
async def update_profile(
    body: UserProfileUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> UserProfileResponse:
    profile = current_user.profile
    update_data = body.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(profile, field, value)

    await db.commit()
    await db.refresh(profile)
    return UserProfileResponse.model_validate(profile)
