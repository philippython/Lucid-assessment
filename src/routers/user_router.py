from fastapi.security import OAuth2PasswordRequestForm
from schemas.token import Token
from schemas.user import UserSchema
from schemas.user_in_db import UserInDB
from fastapi import APIRouter, Depends
from repository import user as user_repo
from auth.oauth2 import *
from utils.hash import *

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

#  In-Memory User Store
users_db = {}

@router.post("/signup/", response_model=Token)
def signup(user: UserSchema):
    """
    Registers a new user.
    - Hashes the password.
    - Stores user in memory.
    - Returns a JWT token.
    """
    return user_repo.create_user(user)


@router.post("/login/", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Authenticates a user.
    - Checks email and password.
    - Returns a JWT token if valid.
    """
    email = form_data.username # username is actually email in OAuth2PasswordRequestForm
    password = form_data.password
    return user_repo.validate_user(email, password)


@router.get("/users/me/")
def get_profile(user: UserInDB = Depends(get_current_user)):
    """
    Returns the authenticated user's profile.
    """
    return {"id": user.id, "email": user.email}
