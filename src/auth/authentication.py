from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from dtos.token import TokenDTO
from typing import Annotated
from sqlmodel import Session
from data.database import 
from auth.oauth2 import create_access_token, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta

router = APIRouter(
    tags=["Authentication"]
)

@router.post('/token')
def generate_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], session : Annotated[Session, Depends(get_cloud_db_session)]):
    user = authenticate_user(form_data.username, form_data.password, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "activated": user.activated}, expires_delta=access_token_expires
    )
    return TokenDTO(access_token=access_token, token_type="bearer")

