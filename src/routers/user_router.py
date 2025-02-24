from fastapi import APIRouter, Depends, Query, status
from dtos.user import UserDTO
from schemas.user import UserSchema
from data.database import get_session
from sqlmodel import Session
from repository import user
from typing import List, Annotated
from auth.oauth2 import require_role
from data.models.user import User

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.post("/create", response_model=UserDTO)
def create_user(request: UserSchema, session : Session = Depends(get_session), current_user : User = Depends(require_role("renter"))):
    return user.create_user(request, current_user, session)