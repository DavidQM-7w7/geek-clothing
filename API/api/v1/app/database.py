from pymongo import MongoClient

MONGO_URI = "mongodb+srv://dquesadam74_db_user:PhoenixZ3ro-7w7@davidqm-7w7.wmaxgyt.mongodb.net/?appName=DavidQM-7w7"

client = MongoClient(MONGO_URI)

db = client["database"]