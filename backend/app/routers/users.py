import hashlib
import uuid

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db
from app.models.user import User
from app.models.user_profile import UserProfile
from app.schemas.user import RegisterRequest, RegisterResponse

router = APIRouter(prefix="/users", tags=["users"])


def _hash_device_id(device_id: str) -> str:
    return hashlib.sha256(device_id.encode()).hexdigest()


@router.post("/register", response_model=RegisterResponse)
async def register(body: RegisterRequest, db: AsyncSession = Depends(get_db)) -> RegisterResponse:
    """
    Bootstrap an anonymous user from a device ID.

    Idempotent: the same device_id always returns the same user and token.
    The raw device_id is never stored — only its SHA-256 hash.

    When real auth is added (Sign in with Apple, email), link the new auth
    method to the existing user_id rather than creating a new user.
    """
    hashed = _hash_device_id(body.device_id)

    result = await db.execute(select(User).where(User.device_id_hash == hashed))
    existing = result.scalar_one_or_none()

    if existing:
        return RegisterResponse(user_id=existing.id, token=existing.token, is_new=False)

    user = User(device_id_hash=hashed, token=uuid.uuid4())
    db.add(user)
    await db.flush()  # get user.id before creating profile

    profile = UserProfile(user_id=user.id)
    db.add(profile)
    await db.commit()
    await db.refresh(user)

    return RegisterResponse(user_id=user.id, token=user.token, is_new=True)
