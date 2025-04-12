import streamlit as st
from harvest.youtube_api import get_channel_details, search_similar_channels
from database.mongo_connector import insert_channel_data  # Assuming this function exists
from analytics.insights import get_channel_insights  # Assuming this function exists
from textblob import TextBlob
import matplotlib.pyplot as plt
import pandas as pd
from googleapiclient.discovery import build
import os

# Load API key
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "YOUR_API_KEY")  # Replace with your key or use dotenv
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

# Streamlit UI
st.title("📊 YouTube Channel Insights Dashboard")

# Sidebar for navigation
st.sidebar.title("Navigation")
option = st.sidebar.selectbox(
    "Choose activity",
    ("YouTube Channel Insights", "Sentiment Analysis", "Recommendations", "Graphical View", "Suggestions")
)

# Section 1: YouTube Channel Insights
if option == "YouTube Channel Insights":
    st.write("### Enter the YouTube channel name or link to retrieve insights.")
    channel_input = st.text_input("Enter YouTube Channel Name/URL")

    if st.button("Fetch Insights"):
        if channel_input:
            channel_data = get_channel_details(channel_input)

            if channel_data:
                channel_id, title, stats = channel_data
                insert_channel_data(channel_id, title, stats)

                st.write(f"**Channel ID**: {channel_id}")
                st.write(f"**Channel Title**: {title}")
                st.write(f"**Subscribers**: {stats.get('subscriberCount', 'N/A')}")
                st.write(f"**Total Views**: {stats.get('viewCount', 'N/A')}")
                st.write(f"**Total Videos**: {stats.get('videoCount', 'N/A')}")

                channel_insights = get_channel_insights(channel_id)
                st.write("**Channel Insights:**")
                st.write(channel_insights)

            else:
                st.error("❌ Could not retrieve data for the provided channel.")
        else:
            st.error("❌ Please provide a valid YouTube channel name or URL.")

# Section 2: Sentiment Analysis
elif option == "Sentiment Analysis":
    st.write("### Enter a text for sentiment analysis.")
    text_input = st.text_area("Enter Text")

    if st.button("Analyze Sentiment"):
        if text_input:
            blob = TextBlob(text_input)
            sentiment = blob.sentiment.polarity

            st.write(f"Sentiment Score: {sentiment}")
            if sentiment > 0:
                st.write("Sentiment: Positive")
            elif sentiment < 0:
                st.write("Sentiment: Negative")
            else:
                st.write("Sentiment: Neutral")
        else:
            st.error("❌ Please provide some text for analysis.")

# Section 3: Recommendations
elif option == "Recommendations":
    st.write("### Enter a YouTube channel or video to get recommendations.")
    query_input = st.text_input("Enter YouTube Channel or Video Name")

    if st.button("Get Recommendations"):
        if query_input:
            try:
                search_response = youtube.search().list(
                    q=query_input,
                    type="channel",
                    part="snippet",
                    maxResults=5
                ).execute()

                st.write(f"🔎 Recommendations based on: `{query_input}`")
                for item in search_response.get("items", []):
                    title = item["snippet"]["title"]
                    channel_id = item["snippet"]["channelId"]
                    channel_url = f"https://www.youtube.com/channel/{channel_id}"
                    st.markdown(f"▶️ [{title}]({channel_url})")

            except Exception as e:
                st.error(f"❌ Error fetching recommendations: {e}")
        else:
            st.error("❌ Please provide a valid channel or video.")

# Section 4: Graphical View
elif option == "Graphical View":
    st.write("### Displaying graphical data of channel insights.")
    data = {"Months": ["Jan", "Feb", "Mar", "Apr", "May"], "Views": [1000, 1500, 1300, 1600, 1800]}
    df = pd.DataFrame(data)
    st.write(df)

    st.write("### Views Over Time")
    fig, ax = plt.subplots()
    ax.plot(df["Months"], df["Views"], marker="o")
    ax.set_title("Channel Views Over Time")
    ax.set_xlabel("Month")
    ax.set_ylabel("Views")
    st.pyplot(fig)

# Section 5: Suggestions
elif option == "Suggestions":
    st.write("### Suggestions to Increase Views and Engagement")

    st.write("""
    1. **Create Consistent Content**: Posting videos regularly can increase engagement.
    2. **Optimize Video Titles and Thumbnails**: Make sure they are attractive and relevant to your audience.
    3. **Engage with Your Audience**: Respond to comments, ask questions, and create polls.
    4. **Use SEO**: Use relevant keywords in your descriptions and tags to help your content get discovered.
    5. **Collaborate**: Collaborating with other creators can bring more visibility.
    """)
