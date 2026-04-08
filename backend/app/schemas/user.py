import uuid

from pydantic import BaseModel


class RegisterRequest(BaseModel):
    device_id: str


class RegisterResponse(BaseModel):
    user_id: uuid.UUID
    token: uuid.UUID
    is_new: bool
