"""KisanSaathi — AI Crop Advisory Assistant.
Grounded agronomic guidance with zero chemical dosage hallucination.
Recreated from visual reference media_1795344704327_f7649893.jpg.
"""

import streamlit as st
from dotenv import load_dotenv

from ui.theme import CSS_DESIGN_SYSTEM
from ui.navbar import render_top_navbar
from ui.page_home import render_page_home
from ui.page_ask import render_page_ask
from ui.page_how import render_page_how
from ui.page_safety import render_page_safety
from ui.page_eval import render_page_eval
from ui.footer import render_footer
from ui.sidebar import render_sidebar

load_dotenv(override=True)

st.set_page_config(
    page_title="KisanSaathi | AI Crop Advisory Assistant",
    page_icon="assets/logos/kisansaathi-icon.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Apply global design system stylesheet
st.markdown(CSS_DESIGN_SYSTEM, unsafe_allow_html=True)

# Initialize Session State
if "result" not in st.session_state:
    st.session_state.result = None
if "follow_up_history" not in st.session_state:
    st.session_state.follow_up_history = []
if "follow_up_answer" not in st.session_state:
    st.session_state.follow_up_answer = ""
if "original_form" not in st.session_state:
    st.session_state.original_form = {
        "crop": "",
        "region": "Select your state",
        "stage": "Select growth stage",
        "query": "",
        "spread": "Not sure",
        "language": "English",
    }

# Render Sidebar and resolve API credentials
resolved_api_key, resolved_model_name = render_sidebar()

# Render Pinned Full-Width Top Navbar
current_lang = st.session_state.original_form.get("language", "English")
if current_lang == "Select language":
    current_lang = "English"
render_top_navbar(language=current_lang)

# Integrated Navigation Tabs (Centered inside pinned navbar)
tab_home, tab_ask, tab_how, tab_safety, tab_eval = st.tabs([
    "Home",
    "Ask AI",
    "How It Works",
    "Safety Guardrails",
    "Evaluation",
])

with tab_home:
    render_page_home()

with tab_ask:
    render_page_ask(resolved_api_key, resolved_model_name)

with tab_how:
    render_page_how()

with tab_safety:
    render_page_safety()

with tab_eval:
    render_page_eval()

# Render Single Unified Footer across all views
render_footer()
