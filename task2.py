from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, Field
from typing import List

# Defining a model for blog posts using Pydantic
class BlogPost(BaseModel):
    title: str = Field(..., example="Python Programming", description="The title of the blog post")
    content: str = Field(..., example="A language used by python snakes?.", description="The main content of the blog post")
    author: str = Field(..., example="Python snakes ancesstors", description="The author of the blog post")

# Defining a model for error responses
class ErrorResponse(BaseModel):
    detail: str = Field(..., example="Post not found.")

# Initializing FastAPI application
app = FastAPI(
    title="Blog Management API",
    description="An API for managing a simple blog. Where you can create, retrieve, update, and delete blog posts."
)

# Use a simple list to store blog posts
blog_posts = []

# Endpoint to create a new blog post
@app.post(
    "/posts/",
    response_model=BlogPost,
    summary="Create a new blog post",
    description="Adds a new blog post to the collection. The title must be unique.",
    responses={
        200: {"description": "The newly created blog post.", "model": BlogPost},
        400: {"description": "A blog post with the same title already exists.", "model": ErrorResponse},
    },
)
def create_post(post: BlogPost):
    for existing_post in blog_posts:
        if existing_post.title == post.title:
            raise HTTPException(status_code=400, detail="Post with this title already exists.")
    blog_posts.append(post)  # Add the new post to the list
    return post

# Endpoint to retrieve all blog posts
@app.get(
    "/posts/",
    response_model=List[BlogPost],
    summary="Get all blog posts",
    description="Fetches all the blog posts available in the collection.",
    responses={
        200: {"description": "A list of all blog posts.", "model": List[BlogPost]},
    },
)
def retrieve_posts():
    return blog_posts

# Endpoint to update a blog post by its title
@app.put(
    "/posts/{title}",
    response_model=BlogPost,
    summary="Update a blog post",
    description="Updates an existing blog post identified by its title.",
    responses={
        200: {"description": "The updated blog post.", "model": BlogPost},
        404: {"description": "No blog post found with the specified title.", "model": ErrorResponse},
    },
)
def update_post(
    title: str = Path(..., example="My First Blog", description="The title of the blog post to update"),
    updated_post: BlogPost = None,
):
    for index, existing_post in enumerate(blog_posts):
        if existing_post.title == title:
            blog_posts[index] = updated_post  # Update the post in the list
            return updated_post
    raise HTTPException(status_code=404, detail="Post not found.")

# Endpoint to delete a blog post by its title
@app.delete(
    "/posts/{title}",
    summary="Delete a blog post",
    description="Deletes a blog post identified by its title.",
    responses={
        200: {"description": "A success message confirming deletion.", "content": {"application/json": {"example": {"message": "Post deleted successfully."}}}},
        404: {"description": "No blog post found with the specified title.", "model": ErrorResponse},
    },
)
def delete_post(
    title: str = Path(..., example="My First Blog", description="The title of the blog post to delete"),
):
    for index, existing_post in enumerate(blog_posts):
        if existing_post.title == title:
            blog_posts.pop(index)  # Remove the post from the list
            return {"message": "Post deleted successfully."}
    raise HTTPException(status_code=404, detail="Post not found.")


#To run this python file in ur computer do the following:

#If u have already run the task1 you don't need to install these again
#1. If you haven't already installed:
#pip install fastapi
#pip install uvicorn

#2. uvicorn task2:app --reload
#Run the no2 line in ur terminal. Replace task2 with the name of your Python file (excluding the .py extension). 

#Access the API: Open your browser and go to:
#Swagger UI for interactive API documentation: http://127.0.0.1:8000/docs
