import streamlit as st
from textwrap import dedent
import time
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.youtube import YouTubeTools

load_dotenv()

st.set_page_config(page_title="AI YouTube Video Analyzer", page_icon="🎥", layout="wide")

st.title("🎥 AI Based YouTube Video Analyzer")
st.write("Extract structured overviews, precise timestamps, and key insights from any YouTube video instantly!")

st.sidebar.header("⚙️ Analysis Settings")
analysis_mode = st.sidebar.selectbox(
    "Choose Analysis Style",
    [
        "Comprehensive & Timestamps",
        "Quick Executive Summary",
        "Key Study Notes & Takeaways"
    ]
)

if analysis_mode == "Quick Executive Summary":
    custom_instructions = "Provide a concise executive summary of the video, highlighting the top 3-5 core takeaways without long timestamp breakdowns."
elif analysis_mode == "Key Study Notes & Takeaways":
    custom_instructions = "Focus heavily on educational value, listing structured study notes, definitions, and bulleted takeaways."
else:
    custom_instructions = dedent("""\
        You are an expert YouTube content analyst with a keen eye for detail! 🎓
        Follow these steps for comprehensive video analysis:
        1. Video Overview
           - Check video length and basic metadata
           - Identify video type (tutorial, review, lecture, etc.)
           - Note the content structure
        2. Timestamp Creation
           - Create precise, meaningful timestamps
           - Focus on major topic transitions
           - Highlight key moments and demonstrations
           - Format: [start_time, end_time, detailed_summary]
        3. Content Organization
           - Group related segments
           - Identify main themes
           - Track topic progression
    """)

video_url = st.text_input("Enter YouTube Video URL:", placeholder="https://www.youtube.com/watch?v=...")

# Robust fallback model list to bypass 503 capacity spikes
GEMINI_MODELS = ["gemini-3.8-flash", "gemini-2.0-flash", "gemini-1.5-flash"]

if st.button("Analyze Video", type="primary"):
    if video_url:
        with st.spinner("Analyzing video content... If servers are busy, this will try alternative models ⏳"):
            response_content = None
            last_error = None

            for model_id in GEMINI_MODELS:
                for attempt in range(2):
                    try:
                        agent = Agent(
                            name="YouTube Agent",
                            model=Gemini(id=model_id),
                            tools=[YouTubeTools()],
                            instructions=custom_instructions,
                            add_datetime_to_context=True,
                            markdown=True,
                        )
                        res = agent.run(f"Analyze this video: {video_url}")
                        response_content = res.content
                        break
                    except Exception as e:
                        last_error = e
                        time.sleep(1.5)
                
                if response_content:
                    break

            if response_content:
                st.success("Analysis Complete!")
                st.markdown("---")
                st.markdown(response_content)

                st.download_button(
                    label="📥 Download Analysis Report",
                    data=response_content,
                    file_name="youtube_analysis_report.md",
                    mime="text/markdown",
                )
            else:
                st.error("Google Gemini is experiencing high traffic across all fallback models. Please wait 15 seconds and click 'Analyze Video' again.")
    else:
        st.warning("Please enter a valid YouTube URL before clicking analyze.")
