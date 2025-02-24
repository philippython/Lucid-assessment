# Limit payload size to 1 MB (1,048,576 bytes)
MAX_PAYLOAD_SIZE = 1 * 1024 * 1024  # 1MB


@app.post("/posts/")
def create_post(request: Request):
    """
    Adds a new post after validating payload size (≤1MB).
    Saves in memory and returns postID.
    """

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

@app.get("/posts/")
def get_posts(token: str = Depends(get_current_user)):
    """
    Returns all user posts with a cache (5 min).
    """
    pass

@app.delete("/posts/{post_id}")
def delete_post(post_id: str, token: str = Depends(get_current_user)):
    """
    Deletes a post if it exists.
    """