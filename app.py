"""KisanSaathi — AI Crop Advisory Assistant.
Clean foundation prepared for complete frontend rebuild.
The backend pipeline, TF-IDF retrieval, and evaluation modules remain fully operational.
"""

import streamlit as st
from dotenv import load_dotenv

from kisansaathi.pipeline import KisanSaathiPipeline
from kisansaathi.retrieval import load_reference_notes

load_dotenv(override=True)

st.set_page_config(
    page_title="KisanSaathi | AI Crop Advisory Assistant",
    page_icon="🌱",
    layout="wide",
)

# Initialize clean session state
if "result" not in st.session_state:
    st.session_state.result = None
if "follow_up_history" not in st.session_state:
    st.session_state.follow_up_history = []

st.title("KisanSaathi — AI Crop Advisory Assistant")
st.caption("Clean foundation prepared for frontend reconstruction. Backend and evaluation systems active.")
