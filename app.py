import streamlit as st
from textwrap import dedent
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.youtube import YouTubeTools

# Load environment variables (.env file)
load_dotenv()

# Streamlit Page Setup
st.set_page_config(page_title="AI YouTube Video Analyzer", page_icon="🎥", layout="wide")

st.title("🎥 AI YouTube Video Analyzer")
st.write("Extract structured overviews, precise timestamps, and key insights from any YouTube video instantly!")

# Input field for YouTube URL
video_url = st.text_input("Enter YouTube Video URL:", placeholder="https://www.youtube.com/watch?v=...")

if st.button("Analyze Video", type="primary"):
    if video_url:
        with st.spinner("Analyzing video content... This may take a few seconds ⏳"):
            try:
                # Initialize Agent with the working model ID
                youtube_agent = Agent(
                    name="YouTube Agent",
                    model=Gemini(id="gemini-3.8-flash"),
                    tools=[YouTubeTools()],
                    instructions=dedent("""\
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

                        Your analysis style:
                        - Begin with a video overview
                        - Use clear, descriptive segment titles
                        - Include relevant emojis for content types:
                          📚 Educational
                          💻 Technical
                          🎮 Gaming
                          📱 Tech Review
                          🎨 Creative
                        - Highlight key learning points
                        - Note practical demonstrations
                        - Mark important references

                        Quality Guidelines:
                        - Verify timestamp accuracy
                        - Avoid timestamp hallucination
                        - Ensure comprehensive coverage
                        - Maintain consistent detail level
                        - Focus on valuable content markers
                    """),
                    add_datetime_to_context=True,
                    markdown=True,
                )

                # Run the agent and get response content
                response = youtube_agent.run(f"Analyze this video: {video_url}")

                # Display Results in Streamlit
                st.success("Analysis Complete!")
                st.markdown("---")
                st.markdown(response.content)

            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid YouTube URL before clicking analyze.")