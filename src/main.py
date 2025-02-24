from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from auth import authentication
from routers import post_router
from data.database import create_db_and_tables


app = FastAPI()

@app.exception_handler(IntegrityError)
async def integrity_exception_handler(request: Request, exc: IntegrityError):
    error_message = str(exc.orig)  # Extract the original database error message

    if "email" in error_message.lower():
        message = "Email already exists"
    elif "contact_num" in error_message.lower():
        message = "Contact number already exists"
    else:
        message = error_message

    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"detail": message}),
    )

app.include_router(authentication.router)
app.include_router(auth_user.router)
app.include_router(venue.router)
app.include_router(user.router)
app.include_router(photo.router)


create_db_and_tables()