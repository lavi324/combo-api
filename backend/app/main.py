from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
import os

# Read MongoDB connection details from environment variables (with defaults for local testing)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "sportsdb")

# Initialize MongoDB client and database
client = MongoClient(MONGO_URI)
db = client[MONGO_DB]

app = FastAPI(title="Football Standings API")

@app.get("/api/standings/{league_name}")
def get_standings(league_name: str):
    """Retrieve standings for the given league_name from MongoDB."""
    # Access the collection for the specified league
    collection = db[league_name]

    # Fetch all documents in the collection (standings entries). Exclude the internal "_id" field for clarity.
    try:
        standings = list(collection.find({}, {"_id": 0}))
    except Exception as e:
        # If there's a database error (e.g., connection issue), return an HTTP 500 error
        raise HTTPException(status_code=500, detail="Database error: unable to retrieve standings")

    # If no data found, return a 404 not found error
    if not standings:
        raise HTTPException(status_code=404, detail="League not found or no standings data available")

    # Return the standings as a list of dictionaries (FastAPI will serialize this to JSON)
    return standings
