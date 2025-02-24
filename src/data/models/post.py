import uuid
from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Column, DateTime, func
from datetime import datetime

class Post(SQLModel, table=True):
    __tablename__ = "post"
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    text : str = Field()
    user_id : int = Field(foreign_key="user.id") # type: ignore
    user : "User" = Relationship(back_populates="posts") # type: ignore
    created_at : datetime = Field(sa_column=Column(DateTime, default=func.now()))

