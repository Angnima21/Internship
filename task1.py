from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel
from typing import List

# Define a model for blog posts using Pydantic
class BlogPost(BaseModel):
    title: str
    content: str
    author: str

# Initialize FastAPI application
app = FastAPI()

# Use a simple list to store blog posts
blog_posts = []

# Endpoint to create a new blog post
@app.post("/posts/")
def create_post(post: BlogPost):
    # Check if a post with the same title already exists
    for existing_post in blog_posts:
        if existing_post.title == post.title:
            raise HTTPException(status_code=400, detail="Post with this title already exists.")
    blog_posts.append(post)  # Add the new post to the list
    return post

# Endpoint to retrieve all blog posts
@app.get("/posts/")
def retrive_posts():
    return blog_posts  # Return the list of posts

# Endpoint to update a blog post by its title
@app.put("/posts/{title}")
def update_post(title: str, updated_post: BlogPost):
    for index, existing_post in enumerate(blog_posts):
        if existing_post.title == title:
            blog_posts[index] = updated_post  # Update the post in the list
            return updated_post
    raise HTTPException(status_code=404, detail="Post not found.")

# Endpoint to delete a blog post by its title
@app.delete("/posts/{title}")
def delete_post(title: str):
    for index, existing_post in enumerate(blog_posts):
        if existing_post.title == title:
            blog_posts.pop(index)  # Remove the post from the list
            return {"message": "Post deleted successfully."}
    raise HTTPException(status_code=404, detail="Post not found.")



#To run this python file in ur computer do the following:


#1. If you haven't already installed:
#pip install fastapi
#pip install uvicorn

#2. uvicorn task1:app --reload
#Run the no2 line in ur terminal. Replace task1 with the name of your Python file (excluding the .py extension). 

#Access the API: Open your browser and go to:
#Swagger UI for interactive API documentation: http://127.0.0.1:8000/docs
