# 🎥 AI YouTube Video Analyzer

An interactive web application that extracts structured overviews, precise timestamps, and key insights from any YouTube video instantly, powered by the **Agno** agent framework, **Google Gemini**, and **Streamlit**.

---

## ✨ Features
- **Video Overview**: Automatically extracts metadata, video length, and content type structure.
- **Smart Timestamp Creation**: Generates precise, meaningful timestamps grouped by major topic transitions and key demonstrations.
- **Content Organization**: Tracks topic progression, highlights key learning points, and flags important references with custom emoji tagging.
- **Web Interface**: Clean, user-friendly UI built with Streamlit.

---

## 🛠️ Tech Stack
- **Agent Framework**: [Agno](https://github.com/agno-agi/agno)
- **AI Model**: Google Gemini (`gemini-3.8-flash`)
- **Frontend UI**: Streamlit
- **Tools**: `youtube-transcript-api`, `yt-dlp`

---

## 🚀 Getting Started Locally

### 1. Clone the Repository
```bash
git clone https://github.com/AnujSable/youtube-video-analyzer.git
cd youtube-video-analyzer
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the root directory and add your Google Gemini API key:
```env
GOOGLE_API_KEY=your_actual_api_key_here
```

### 4. Run the Streamlit App
```bash
streamlit run app.py
```

---

## ☁️ Deployment on Streamlit Community Cloud
1. Push your repository to GitHub (ensure `.env` is excluded via `.gitignore`).
2. Head to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Connect your repository (`youtube-video-analyzer`), set branch to `main`, and main file path to `app.py`.
4. In **Advanced Settings / Secrets**, add your API key:
   ```toml
   GOOGLE_API_KEY = "your_actual_api_key_here"
   ```
5. Click **Deploy!**