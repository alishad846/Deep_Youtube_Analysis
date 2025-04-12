from googleapiclient.discovery import build
import os

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "YOUR_API_KEY")
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)


def get_channel_details(channel_input):
    # Use YouTube search API to resolve channel name to ID
    try:
        search_response = youtube.search().list(
            q=channel_input,
            type="channel",
            part="snippet",
            maxResults=1
        ).execute()

        if not search_response["items"]:
            print("No channel found with the provided name.")
            return None

        channel = search_response["items"][0]
        channel_id = channel["snippet"]["channelId"]
        title = channel["snippet"]["title"]

        # Now fetch full stats using channelId
        stats_response = youtube.channels().list(
            part="statistics",
            id=channel_id
        ).execute()

        statistics = stats_response["items"][0]["statistics"]
        return channel_id, title, statistics

    except Exception as e:
        print(f"Error fetching channel data: {e}")
        return None


def search_similar_channels(keyword):
    try:
        search_response = youtube.search().list(
            q=keyword,
            type="channel",
            part="snippet",
            maxResults=5
        ).execute()

        return search_response["items"]
    except Exception as e:
        print(f"Error fetching similar channels: {e}")
        return []
