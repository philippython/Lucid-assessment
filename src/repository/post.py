import uuid
import time
from fastapi import HTTPException, Depends, Request
from auth.oauth2 import get_current_user
from dtos.post import PostDTO

# In memory storage for posts & cache
posts_db = {}
cache = {}


# Limit payload size to 1 MB (1,048,576 bytes)
MAX_PAYLOAD_SIZE = 1 * 1024 * 1024  # 1MB


def add_post(request: Request):

    # Enforce payload size limit
    content_length = request.headers.get("content-length")
    if content_length and int(content_length) > MAX_PAYLOAD_SIZE:
        raise HTTPException(status_code=413, detail="Payload size exceeds 1MB limit")

    # Parse request data
    post_data = request.json()

    # Validate post data using Pydantic
    post = PostDTO(**post_data)

    # Generate a unique post ID
    post_id = str(uuid.uuid4())

    # Save the post in memory
    posts_db[post_id] = post.dict()

    return {"postID": post_id, "message": "Post saved successfully!"}

def get_posts(token: str = Depends(get_current_user)):
    current_time = time.time()
    
    # Return cached response if available and valid
    if token in cache and current_time - cache[token]["timestamp"] < 300:
        return cache[token]["data"]

    user_posts = posts_db.get(token, [])

    # Cache response
    cache[token] = {"data": user_posts, "timestamp": current_time}

    return user_posts


def delete_post(post_id: str, token: str = Depends(get_current_user)):
    user_posts = posts_db.get(token, [])
    for post in user_posts:
        if post["postID"] == post_id:
            user_posts.remove(post)
            return {"message": "Post deleted successfully!"}

    raise HTTPException(status_code=404, detail="Post not found")


