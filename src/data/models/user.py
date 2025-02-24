from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Column, DateTime, func
from datetime import datetime
from typing import List

class User(SQLModel, table=True):
    __tablename__ = "user"
    id: int = Field(primary_key=True)
    email : str = Field(le=255, unique=True)
    password : str = Field(le=255)
    posts : List["Post"] = Relationship(back_populates="user") # type: ignore
    created_at : datetime = Field(sa_column=Column(DateTime, default=func.now()))

