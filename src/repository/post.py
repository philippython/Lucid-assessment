from fastapi import FastAPI, Depends, HTTPException, Request
from pydantic import BaseModel, Field
from datetime import datetime, timedelta
from sqlalchemy.ext.declarative import declarative_base
import uuid
import time


def add_post(request: Request, token: str = Depends(get_current_user)):

    post_data = request.json()
    post = PostDTO(**post_data)

    post_id = str(uuid.uuid4())
    if token not in posts_db:
        posts_db[token] = []
    posts_db[token].append({"postID": post_id, "text": post.text, "created_at": datetime.utcnow()})

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


