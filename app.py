from fastapi import FastAPI, Query
from pymongo import MongoClient
import os

app = FastAPI()

MONGO_URI = os.environ.get("MONGODB_URI") or "YOUR_MONGO_CONNECTION_STRING"

client = MongoClient(MONGO_URI)
db = client["Codegnan_DIET_App"]

@app.get("/collections")
def list_collections():
    return {"collections": db.list_collection_names()}

@app.get("/find")
def find_data(collection: str, field: str = None, value: str = None):
    col = db[collection]
    if field and value:
        docs = list(col.find({field: value}, {"_id": 0}))
    else:
        docs = list(col.find({}, {"_id": 0}))
    return {"data": docs}
