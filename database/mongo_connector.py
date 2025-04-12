from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["advanced_insights"]

def insert_channel_data(channel_id, title, stats):
    collection = db["channels"]
    channel_data = {
        "channel_id": channel_id,
        "title": title,
        "stats": stats
    }
    # Insert the channel data
    collection.update_one({"channel_id": channel_id}, {"$set": channel_data}, upsert=True)
    print("Data inserted successfully.")
