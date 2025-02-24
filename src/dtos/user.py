from pydantic import BaseModel
from datetime import datetime
from dtos.post import PostDTO
from typing import List

class UserDTO(BaseModel):
    id : int
    email : str
    posts : List[PostDTO]
    created_at : datetime
    class Config():
        orm_mode = True