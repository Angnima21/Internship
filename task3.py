from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Dummy database for demonstration
items_db = {
    1: {"name": "Apple", "price": 0.5},
    2: {"name": "Banana", "price": 0.3},
}

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
async def create_item(item: Item):
    if item.price < 0:
        # Raise an HTTPException instead of ValueError for proper error handling
        raise HTTPException(status_code=400, detail="Price cannot be negative")
    return {"name": item.name, "price": item.price}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # Implementation of get_item_by_id
    item = items_db.get(item_id)
    if not item:
        # Raise HTTPException if the item is not found
        raise HTTPException(status_code=404, detail="Item not found")
    return item


#Issues Fixed:
#1. Error Handling: Changed ValueError to HTTPException for proper HTTP responses.
#2. Missing Function: Implemented get_item_by_id using a mock database.
#3. Graceful Errors: Added 404 Not Found for missing items.

#Improvements:
#1. Errors now return clear messages instead of crashing.
#2. App fully works to fetch items by ID.
#3. Code is cleaner and beginner-friendly.


#To run this python file in ur computer do the following:

#If u have already run the task1 you don't need to install these again
#1. If you haven't already installed:
#pip install fastapi
#pip install uvicorn

#2. uvicorn task3:app --reload
#Run the no2 line in ur terminal. Replace task3 with the name of your Python file (excluding the .py extension). 

#Access the API: Open your browser and go to:
#Swagger UI for interactive API documentation: http://127.0.0.1:8000/docs