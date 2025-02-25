import uuid
from schemas.user import UserSchema
from fastapi import HTTPException
from auth.oauth2 import create_access_token
from schemas.user_in_db import UserInDB
from utils.hash import *
from data.database import users_db  # Import shared storage


def create_user(user: UserSchema) -> dict:
    if user.email in users_db:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user.password)
    user_id = str(uuid.uuid4())
    users_db[user.email] = UserInDB(id=user_id, email=user.email, password=user.password, hashed_password=hashed_password)

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

def validate_user(email : str, password : str) -> dict:
    user = users_db.get(email)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}