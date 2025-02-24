from pydantic import BaseModel
from datetime import datetime

class PostDTO(BaseModel):
    id : str
    text : str
    # created_at : datetime -> incase we need to return the created datetime 
    class Config():
        orm_mode = True
