from fastapi import FastAPI
from routers import post_router
from routers import user_router
from data.database import create_db_and_tables


app = FastAPI()


app.include_router(user_router.router)
app.include_router(post_router.router)