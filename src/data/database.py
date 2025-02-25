from sqlmodel import Session, SQLModel, create_engine
from typing import Dict
from schemas.user_in_db import UserInDB

# Simulated in-memory database (should be replaced with a real database)
users_db: Dict[str, UserInDB] = {}

sqlite_file_name = "lucid.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session