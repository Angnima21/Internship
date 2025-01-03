from fastapi import FastAPI, HTTPException

app = FastAPI()

def validate_password(password: str):
    """Check if the password meets the required criteria."""
    if len(password) < 8:
        raise HTTPException(status_code=400, detail="Password too short")

def validate_email(email: str):
    """Check if the email is valid."""
    if "@" not in email:
        raise HTTPException(status_code=400, detail="Invalid email")

@app.post("/users/")
async def create_user(name: str, email: str, password: str):
    validate_password(password)
    validate_email(email)
    return {"name": name, "email": email}

@app.put("/users/")
async def update_user(name: str, email: str, password: str):
    validate_password(password)
    validate_email(email)
    return {"name": name, "email": email}
    

#What Was Wrong
#1. Repeated Code: Validation logic for email and password was duplicated in both functions.
#2. Poor Error Handling: Used "ValueError" instead of proper API-friendly errors.

#What I Improved
#1. Removed Duplication: Moved repeated logic into "validate_password" and "validate_email" functions.
#2. Better Errors: Used "HTTPException" for clear API responses.
#3. Cleaner Code: Shorter, easier-to-read, and maintainable functions.


#To run this python file in ur computer do the following:

#If u have already run the task1 you don't need to install these again
#1. If you haven't already installed:
#pip install fastapi
#pip install uvicorn

#2. uvicorn task4:app --reload
#Run the no2 line in ur terminal. Replace task4 with the name of your Python file (excluding the .py extension). 

#Access the API: Open your browser and go to:
#Swagger UI for interactive API documentation: http://127.0.0.1:8000/docs

