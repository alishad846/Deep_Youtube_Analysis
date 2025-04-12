import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve values from .env
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# Check if the variables are loaded correctly
print(f"API Key Loaded: {YOUTUBE_API_KEY is not None}")
print(f"Mongo URI: {MONGO_URI}")
