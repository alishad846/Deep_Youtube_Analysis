import pandas as pd

def clean_channel_data(channel_data):
    """
    Clean and transform the fetched channel data for MongoDB insertion.
    """
    try:
        # Sample cleaning process (extend as needed)
        cleaned_data = {
            "channel_id": channel_data[0],
            "title": channel_data[1],
            "subscribers": channel_data[2].get("subscriberCount", 0),
            "views": channel_data[2].get("viewCount", 0),
            "videos": channel_data[2].get("videoCount", 0),
        }
        return cleaned_data
    except Exception as e:
        print(f"Error cleaning channel data: {e}")
        return None
