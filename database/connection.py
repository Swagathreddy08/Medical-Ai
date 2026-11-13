import os
from dotenv import load_dotenv
from pymongo import MongoClient
load_dotenv()
MONGO_URI = os.getenv("mongo")
if not MONGO_URI:
    raise ValueError("MONGO_URI is missing from .env file")
client = MongoClient(MONGO_URI)
database = client["mediguide"]
patients_collection = database["patients"]
symptoms_collection = database["symptoms"]
