from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb+srv://poojithanamu_db_user:poojitha%4023@cluster0.w9yrukr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = AsyncIOMotorClient(MONGO_URL)  # <-- create client instance

db = client["mydatabase"]
collection = db["persons"]  # your collection
