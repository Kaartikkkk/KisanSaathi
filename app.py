"""KisanSaathi — AI Crop Advisory Assistant.
Grounded agronomic guidance with zero chemical dosage hallucination.
Modular UI architecture structured across ui/ package.
"""

import streamlit as st
from dotenv import load_dotenv

from ui.theme import CSS_LIGHT_THEME
from ui.navbar import render_pinned_navbar
from ui.tab_home import render_tab_home
from ui.tab_how import render_tab_how
from ui.tab_ask import render_tab_ask
from ui.tab_safety import render_tab_safety
from ui.tab_eval import render_tab_eval
from ui.footer import render_footer
from ui.sidebar import render_sidebar

load_dotenv(override=True)

st.set_page_config(
    page_title="KisanSaathi | AI Crop Advisory Assistant",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Apply global light theme, edge-to-edge layout, and tab styling
st.markdown(CSS_LIGHT_THEME, unsafe_allow_html=True)

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
render_pinned_navbar(language=current_lang)

# Integrated Navigation Tabs (Centered inside pinned navbar)
tab_home, tab_ask, tab_how, tab_safety, tab_eval = st.tabs([
    "Home",
    "Ask AI",
    "How It Works",
    "Safety Guardrails",
    "Evaluation",
])

with tab_home:
    render_tab_home()

with tab_ask:
    render_tab_ask(resolved_api_key, resolved_model_name)

with tab_how:
    render_tab_how()

with tab_safety:
    render_tab_safety()

with tab_eval:
    render_tab_eval()

# Render Single Unified Footer across all views
render_footer()
