import requests
import os
from dotenv import load_dotenv
import pytest

# Load environment variables from .env file
load_dotenv()

# Get the API key from the .env file
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
def get_channel_data(channel_id, api_key):
    url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={channel_id}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    print("API Response:", data)  # Print the response to understand the error
    return data

def get_channel_data(channel_id, api_key):
    url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={channel_id}&key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code, "message": response.text}


# Test function for pytest
def test_get_channel_data():
    # Use a valid YouTube channel ID for testing
    channel_id = "UCXgGY0w2J1oQmWJp1UmTg"  # Example channel ID
    data = get_channel_data(channel_id, YOUTUBE_API_KEY)

    # Debugging output for the response data
    print("API Response Data:", data)

    # Assertions to verify the response structure
    assert "error" not in data, f"API call failed: {data['message'] if 'message' in data else 'Unknown error'}"

    # Check if 'items' is present, even if empty, and handle empty results
    if "items" in data:
        assert len(data["items"]) > 0, "No items found in the response"
    else:
        assert "items" not in data, "'items' key is missing, no results were returned"


# Run the test when executing the script
if __name__ == "__main__":
    pytest.main()
