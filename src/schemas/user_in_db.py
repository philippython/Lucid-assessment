from schemas.user import UserSchema

class UserInDB(UserSchema):
    """Schema for storing user details (hashed password)."""
    id: str
    email : str
    hashed_password: str