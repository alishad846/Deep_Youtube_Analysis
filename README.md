# 📊 YouTube Channel Insights Dashboard

An advanced Streamlit-based web app for extracting, analyzing, and visualizing YouTube channel data using the YouTube Data API and MongoDB. This project enables creators and analysts to monitor channel performance, extract video data, view sentiment analysis, receive growth suggestions, and get channel recommendations.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-ff4b4b?logo=streamlit)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-47A248?logo=mongodb)
![License](https://img.shields.io/badge/License-MIT-green)
![Open Source](https://img.shields.io/badge/Open%20Source-Yes-brightgreen)

---

## 🚀 Features

- 🔍 **Channel Insights** – Retrieve and display YouTube channel stats (subs, views, videos).
- 📦 **MongoDB Integration** – Store all harvested channel data for re-analysis.
- 📊 **Graphical Visualizations** – Line graphs and tables for channel metrics.
- 🧠 **Sentiment Analysis** – Analyze text or comment sentiment using TextBlob.
- 🎯 **Recommendations** – Fetch similar or related YouTube channels based on a keyword.
- 💡 **Growth Suggestions** – Actionable content and SEO strategies to grow a channel.

---

## 🛠️ Tech Stack

| Layer              | Technology Used                        |
|--------------------|----------------------------------------|
| Frontend           | `Streamlit`                            |
| Backend            | `YouTube Data API v3`, `Google API`    |
| ML/NLP             | `TextBlob` for Sentiment Analysis      |
| Data Storage       | `MongoDB` via `pymongo`                |
| Visualization      | `Matplotlib`, `Pandas`                 |
| Programming Lang   | `Python 3.12.4`                        |

---

## 📸 Screenshots

| Channel Insights | Sentiment Analysis | Recommendations | Graph View |
|------------------|--------------------|------------------|-------------|
| ![1](https://via.placeholder.com/300x180?text=Insights) | ![2](https://via.placeholder.com/300x180?text=Sentiment) | ![3](https://via.placeholder.com/300x180?text=Recs) | ![4](https://via.placeholder.com/300x180?text=Graph) |

---

## ⚙️ Installation & Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/youtube-insights-dashboard.git
cd youtube-insights-dashboard
2. Set up a virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Set up your API Key
Replace "YOUR_API_KEY" in your code or use .env and python-dotenv:

ini
Copy
Edit
YOUTUBE_API_KEY=your_actual_api_key
5. Run the Streamlit app
bash
Copy
Edit
streamlit run app.py
📁 Project Structure
bash
Copy
Edit
youtube-insights-dashboard/
│
├── app.py                      # Streamlit UI
├── harvest/
│   └── youtube_api.py          # Functions to fetch YouTube data
├── database/
│   └── mongo_connector.py      # MongoDB logic
├── analytics/
│   └── insights.py             # Data analytics and formatting
├── requirements.txt
└── README.md
🤝 Contributing
Feel free to fork, open issues, or submit pull requests!
For major changes, open an issue first to discuss what you’d like to change.

📄 License
This project is licensed under the MIT License.

🙌 Acknowledgments
Streamlit

Google YouTube Data API

TextBlob

MongoDB
