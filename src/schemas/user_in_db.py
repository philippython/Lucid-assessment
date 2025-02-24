from schemas.user import UserSchema

class UserInDB(UserSchema):
    """Schema for storing user details (hashed password)."""
    id: str
    hashed_password: str