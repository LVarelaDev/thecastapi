from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models.user import User

import os

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
DATABASE_NAME = os.getenv("MONGODB_DB", "cat_api_db")

async def init_db():
    client = AsyncIOMotorClient(MONGODB_URI)
    db = client[DATABASE_NAME]
    await init_beanie(database=db, document_models=[User])
  