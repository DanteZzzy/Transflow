import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://root:example@mongo:27017")
MONGO_DB = os.getenv("MONGO_DB", "mensageria")

client = MongoClient(f"{MONGO_URL}/{MONGO_DB}?authSource=admin")
mongo_db = client[MONGO_DB]
