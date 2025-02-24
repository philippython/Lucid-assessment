from fastapi import APIRouter, Depends, Request
from auth.oauth2 import get_current_user
from utils.hash import *
from repository import post

router = APIRouter(
    prefix="/post",
    tags=["Posts"]
)


@router.post("/posts/")
def create_post(request: Request, token: str = Depends(get_current_user)):
    """
    Adds a new post after validating payload size (≤1MB).
    Saves in memory and returns postID.
    """
    return post.add_post(request)

@router.get("/posts/")
def get_posts(token: str = Depends(get_current_user)):
    """
    Returns all user posts with a cache (5 min).
    """
    return post.get_posts(token)

@router.delete("/posts/{post_id}")
def delete_post(post_id: str, token: str = Depends(get_current_user)):
    """
    Deletes a post if it exists.
    """
    return post.delete_post(post_id)