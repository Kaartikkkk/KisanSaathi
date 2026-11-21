"""Sidebar component for KisanSaathi.
Handles API key configuration, active model status, and agronomic knowledge base telemetry.
"""

import os
import streamlit as st
from ui.assets import ICONS

def get_gemini_api_key(sidebar_input: str = "") -> str:
    """Resolve Gemini API key with priority: sidebar input > Streamlit secrets > .env."""
    if sidebar_input and sidebar_input.strip():
        return sidebar_input.strip()
    try:
        cloud_key = st.secrets.get("GEMINI_API_KEY", "")
        if cloud_key and str(cloud_key).strip():
            return str(cloud_key).strip()
    except Exception:
        pass
    env_key = os.getenv("GEMINI_API_KEY", "")
    return env_key.strip() if env_key else ""

def get_gemini_model() -> str:
    """Resolve Gemini Model name with priority: secrets > .env > default."""
    try:
        cloud_model = st.secrets.get("GEMINI_MODEL", "")
        if cloud_model and str(cloud_model).strip():
            return str(cloud_model).strip()
    except Exception:
        pass
    env_model = os.getenv("GEMINI_MODEL", "")
    if env_model and env_model.strip():
        return env_model.strip()
    return "gemini-2.5-flash"

def render_sidebar() -> tuple[str, str]:
    """Render sidebar controls and return (api_key, model_name)."""
    with st.sidebar:
        st.markdown(f"""
        <div style="display:flex; align-items:center; gap:0.6rem; margin-bottom:1.25rem;">
            <div style="background:#E7F2E8; padding:8px; border-radius:10px;">
                {ICONS['leaf_brand']}
            </div>
            <div>
                <div style="font-weight:800; font-size:1.15rem; color:#174B35;">KisanSaathi</div>
                <div style="font-size:0.75rem; color:#2E7D50; font-weight:600;">AI Crop Advisory Assistant</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        api_key_input = st.text_input(
            "Gemini API Key",
            value="",
            type="password",
            help="Automatically reads from Streamlit Secrets or .env. Override here if needed.",
        )

        resolved_api_key = get_gemini_api_key(api_key_input)
        resolved_model_name = get_gemini_model()

        if resolved_api_key:
            st.markdown(f"""
            <div style="background:#E7F2E8; border:1px solid #B6D9BC; padding:0.5rem 0.8rem; border-radius:8px; font-size:0.8rem; color:#0B5A2A; font-weight:600; margin-bottom:1rem; display:flex; align-items:center; gap:0.4rem;">
                {ICONS['check_green']} Engine Connected ({resolved_model_name})
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="background:#FEF2F2; border:1px solid #FCA5A5; padding:0.5rem 0.8rem; border-radius:8px; font-size:0.8rem; color:#991B1B; font-weight:600; margin-bottom:1rem; display:flex; align-items:center; gap:0.4rem;">
                {ICONS['alert_amber']} API Key Required
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("""
        <div style="font-size:0.85rem; color:#5A6860; line-height:1.6;">
            <b>Agricultural Knowledge Base:</b><br>
            • ICAR agronomic profiles<br>
            • State Agriculture Universities<br>
            • Zero synthetic chemical dosages<br>
            • Multi-lingual tokenization (EN, HI, Hinglish)
        </div>
        """, unsafe_allow_html=True)

        return resolved_api_key, resolved_model_name
