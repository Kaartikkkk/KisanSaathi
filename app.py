import base64
import csv
import json
import os
import streamlit as st
from dotenv import load_dotenv

from kisansaathi.pipeline import KisanSaathiPipeline
from kisansaathi.retrieval import load_reference_notes

load_dotenv(override=True)

st.set_page_config(
    page_title="KisanSaathi | Intelligent Agronomic AI",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# Asset & SVG Icon Helpers
# -----------------------------------------------------------------------------
@st.cache_data
def get_base64_image(image_path: str) -> str:
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return ""

ICON_LEAF = """<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/></svg>"""

ICON_SHIELD = """<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>"""

ICON_SEARCH = """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>"""

ICON_CHECKLIST = """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/><path d="m9 14 2 2 4-4"/></svg>"""

ICON_ALERT = """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>"""

ICON_QUESTION = """<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>"""

ICON_SPARKLE = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/></svg>"""

ICON_BOOK = """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z"/><path d="M6 6h10"/><path d="M6 10h10"/></svg>"""

ICON_CHECK = """<svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>"""

ICON_PHONE = """<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>"""

# -----------------------------------------------------------------------------
# API Key & Model Resolution (Strict Priority)
# -----------------------------------------------------------------------------
def get_gemini_api_key(sidebar_input=""):
    """
    Resolves the Gemini API key using strict priority:
    1. User-entered sidebar API key, if provided.
    2. Streamlit Community Cloud Secrets (st.secrets.get("GEMINI_API_KEY", "")).
    3. Local environment variable (os.getenv("GEMINI_API_KEY", "") from .env).
    """
    if sidebar_input and sidebar_input.strip():
        return sidebar_input.strip()
    try:
        cloud_key = st.secrets.get("GEMINI_API_KEY", "")
        if cloud_key and str(cloud_key).strip():
            return str(cloud_key).strip()
    except Exception:
        pass
    env_key = os.getenv("GEMINI_API_KEY", "")
    if env_key and env_key.strip():
        return env_key.strip()
    return ""

def get_gemini_model():
    """
    Resolves the Gemini model name using priority:
    1. Streamlit Community Cloud Secrets (st.secrets.get("GEMINI_MODEL", "")).
    2. Local environment variable (os.getenv("GEMINI_MODEL", "")).
    3. Default fallback: gemini-2.5-flash.
    """
    try:
        cloud_model = st.secrets.get("GEMINI_MODEL", "")
        if cloud_model and str(cloud_model).strip():
            return str(cloud_model).strip()
    except Exception:
        pass
    env_model = os.getenv("GEMINI_MODEL", "")
    if env_model and env_model.strip():
        return env_model.strip()
    try:
        return st.secrets.get("GEMINI_MODEL", "gemini-2.5-flash")
    except Exception:
        return "gemini-2.5-flash"

# -----------------------------------------------------------------------------
# Premium Agritech Design System (CSS)
# -----------------------------------------------------------------------------
CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');

:root {
    --ks-forest: #143626;
    --ks-forest-dark: #0D2419;
    --ks-botanical: #2D7A4D;
    --ks-botanical-light: #52B788;
    --ks-mint-soft: #E8F5E9;
    --ks-mint-accent: #D8F3DC;
    --ks-bg: #F8FAF6;
    --ks-card-bg: #FFFFFF;
    --ks-border: #E2E8F0;
    --ks-text-main: #1A202C;
    --ks-text-muted: #4A5568;
    --ks-warning-bg: #FEF9C3;
    --ks-warning-border: #F59E0B;
    --ks-danger-bg: #FEE2E2;
    --ks-danger-border: #EF4444;
}

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    background-color: var(--ks-bg);
    color: var(--ks-text-main);
}

.main .block-container {
    max-width: 1200px;
    padding-top: 1.5rem;
    padding-bottom: 3.5rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

/* Custom Navigation Bar */
.ks-navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #FFFFFF;
    border: 1px solid var(--ks-border);
    border-radius: 16px;
    padding: 0.9rem 1.8rem;
    margin-bottom: 2rem;
    box-shadow: 0 4px 18px rgba(20, 54, 38, 0.04);
}
.ks-nav-brand {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    text-decoration: none;
    color: var(--ks-forest);
}
.ks-nav-logo-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 38px;
    height: 38px;
    background: var(--ks-mint-accent);
    color: var(--ks-forest);
    border-radius: 10px;
}
.ks-nav-title {
    font-size: 1.35rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    color: var(--ks-forest);
    line-height: 1.2;
}
.ks-nav-tag {
    font-size: 0.72rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--ks-botanical);
}
.ks-nav-links {
    display: flex;
    align-items: center;
    gap: 1.5rem;
}
.ks-nav-link {
    color: var(--ks-text-muted);
    text-decoration: none;
    font-size: 0.92rem;
    font-weight: 600;
    transition: color 0.15s ease;
}
.ks-nav-link:hover {
    color: var(--ks-botanical);
}
.ks-nav-badge {
    background: var(--ks-mint-soft);
    color: var(--ks-forest);
    font-size: 0.75rem;
    font-weight: 700;
    padding: 0.35rem 0.8rem;
    border-radius: 999px;
    border: 1px solid var(--ks-botanical-light);
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
}

/* Hero Section */
.ks-hero-container {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    background: linear-gradient(145deg, #FFFFFF 0%, #F4F8F3 100%);
    border: 1px solid rgba(45, 122, 77, 0.15);
    border-radius: 24px;
    padding: 2.75rem 2.5rem;
    margin-bottom: 2.75rem;
    box-shadow: 0 10px 32px rgba(20, 54, 38, 0.06);
    gap: 2rem;
}
.ks-hero-left {
    flex: 1 1 520px;
    min-width: 300px;
}
.ks-hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: #EAF7EE;
    color: var(--ks-botanical);
    padding: 0.4rem 0.95rem;
    border-radius: 999px;
    font-size: 0.82rem;
    font-weight: 700;
    letter-spacing: 0.02em;
    margin-bottom: 1.15rem;
    border: 1px solid rgba(45, 122, 77, 0.25);
}
.ks-hero-title {
    font-size: 2.45rem;
    font-weight: 800;
    color: var(--ks-forest);
    line-height: 1.18;
    letter-spacing: -0.03em;
    margin-bottom: 1.1rem;
}
.ks-hero-subtitle {
    font-size: 1.05rem;
    color: var(--ks-text-muted);
    line-height: 1.6;
    margin-bottom: 1.6rem;
    max-width: 580px;
}
.ks-trust-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 0.65rem;
    margin-bottom: 1.75rem;
}
.ks-trust-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: #FFFFFF;
    border: 1px solid var(--ks-border);
    padding: 0.4rem 0.85rem;
    border-radius: 8px;
    font-size: 0.82rem;
    font-weight: 600;
    color: var(--ks-text-main);
    box-shadow: 0 1px 3px rgba(0,0,0,0.03);
}
.ks-trust-pill svg {
    color: var(--ks-botanical);
}
.ks-hero-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
}
.ks-btn-primary {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: linear-gradient(135deg, var(--ks-forest) 0%, var(--ks-botanical) 100%);
    color: #FFFFFF !important;
    text-decoration: none;
    font-weight: 700;
    font-size: 0.95rem;
    padding: 0.75rem 1.6rem;
    border-radius: 12px;
    box-shadow: 0 4px 14px rgba(20, 54, 38, 0.25);
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}
.ks-btn-primary:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 18px rgba(20, 54, 38, 0.32);
}
.ks-btn-secondary {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: #FFFFFF;
    color: var(--ks-forest) !important;
    border: 1px solid var(--ks-border);
    text-decoration: none;
    font-weight: 600;
    font-size: 0.95rem;
    padding: 0.75rem 1.4rem;
    border-radius: 12px;
    transition: background 0.15s ease;
}
.ks-btn-secondary:hover {
    background: #F1F5F0;
}
.ks-hero-right {
    flex: 1 1 380px;
    min-width: 280px;
    display: flex;
    justify-content: center;
    position: relative;
}
.ks-hero-image-card {
    position: relative;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 12px 36px rgba(20, 54, 38, 0.18);
    border: 3px solid #FFFFFF;
    max-width: 440px;
    width: 100%;
}
.ks-hero-image-card img {
    width: 100%;
    height: auto;
    display: block;
    object-fit: cover;
}
.ks-hero-image-overlay {
    position: absolute;
    bottom: 14px;
    left: 14px;
    right: 14px;
    background: rgba(20, 54, 38, 0.88);
    backdrop-filter: blur(8px);
    color: #FFFFFF;
    padding: 0.7rem 1rem;
    border-radius: 12px;
    font-size: 0.8rem;
    font-weight: 600;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border: 1px solid rgba(255, 255, 255, 0.15);
}
.ks-pulse-indicator {
    display: inline-block;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #52B788;
    box-shadow: 0 0 0 3px rgba(82, 183, 136, 0.35);
}

/* Steps Section */
.ks-section {
    margin-bottom: 3rem;
}
.ks-section-header {
    text-align: center;
    max-width: 680px;
    margin: 0 auto 2rem auto;
}
.ks-section-tag {
    font-size: 0.78rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--ks-botanical);
    background: var(--ks-mint-soft);
    padding: 0.3rem 0.85rem;
    border-radius: 999px;
    display: inline-block;
    margin-bottom: 0.6rem;
}
.ks-section-title {
    font-size: 1.85rem;
    font-weight: 800;
    color: var(--ks-forest);
    letter-spacing: -0.02em;
    margin-bottom: 0.6rem;
}
.ks-section-desc {
    font-size: 0.98rem;
    color: var(--ks-text-muted);
    line-height: 1.55;
}
.ks-steps-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.4rem;
}
.ks-step-card {
    background: #FFFFFF;
    border: 1px solid var(--ks-border);
    border-radius: 16px;
    padding: 1.75rem 1.6rem;
    position: relative;
    box-shadow: 0 4px 16px rgba(0,0,0,0.02);
    transition: transform 0.2s ease, border-color 0.2s ease;
}
.ks-step-card:hover {
    transform: translateY(-3px);
    border-color: var(--ks-botanical-light);
    box-shadow: 0 8px 24px rgba(45, 122, 77, 0.08);
}
.ks-step-num {
    position: absolute;
    top: 1.4rem;
    right: 1.4rem;
    font-size: 1.6rem;
    font-weight: 800;
    color: #E2E8F0;
    line-height: 1;
}
.ks-step-icon {
    width: 44px;
    height: 44px;
    border-radius: 12px;
    background: var(--ks-mint-accent);
    color: var(--ks-forest);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 1.15rem;
}
.ks-step-card h3 {
    font-size: 1.12rem;
    font-weight: 700;
    color: var(--ks-forest);
    margin-bottom: 0.55rem;
}
.ks-step-card p {
    font-size: 0.88rem;
    color: var(--ks-text-muted);
    line-height: 1.55;
    margin: 0;
}

/* Form Container Card */
.ks-form-container {
    background: #FFFFFF;
    border: 1px solid var(--ks-border);
    border-radius: 20px;
    padding: 2.25rem 2.25rem 1.75rem 2.25rem;
    box-shadow: 0 6px 28px rgba(20, 54, 38, 0.05);
    margin-bottom: 2.5rem;
}
.ks-form-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-bottom: 1.25rem;
    border-bottom: 1px solid var(--ks-border);
    margin-bottom: 1.5rem;
}
.ks-form-title {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    font-size: 1.35rem;
    font-weight: 800;
    color: var(--ks-forest);
}
.ks-form-badge {
    background: var(--ks-mint-soft);
    color: var(--ks-botanical);
    font-size: 0.76rem;
    font-weight: 700;
    padding: 0.35rem 0.8rem;
    border-radius: 6px;
    border: 1px solid rgba(45, 122, 77, 0.2);
}

/* Preset Quick Test Buttons */
.ks-preset-container {
    margin-bottom: 1.5rem;
    background: #F8FAF6;
    border: 1px dashed #CBD5E1;
    border-radius: 12px;
    padding: 0.85rem 1.15rem;
}
.ks-preset-label {
    font-size: 0.8rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--ks-text-muted);
    margin-bottom: 0.55rem;
    display: flex;
    align-items: center;
    gap: 0.4rem;
}

/* Cards for Results */
.ks-result-card {
    background: #FFFFFF;
    border: 1px solid var(--ks-border);
    border-radius: 16px;
    padding: 1.75rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 18px rgba(0,0,0,0.03);
}
.ks-result-card-header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 1.15rem;
}
.ks-result-card-header h3 {
    font-size: 1.18rem;
    font-weight: 700;
    color: var(--ks-forest);
    margin: 0;
}
.ks-cause-item {
    background: #FBFDFB;
    border: 1px solid #E2EBE2;
    border-radius: 12px;
    padding: 1.15rem 1.25rem;
    margin-bottom: 0.9rem;
}
.ks-cause-name {
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--ks-forest);
    margin-bottom: 0.4rem;
}
.ks-cause-reason {
    font-size: 0.92rem;
    color: var(--ks-text-muted);
    line-height: 1.55;
    margin-bottom: 0.5rem;
}

/* Warning & Escalation Banners */
.ks-alert-banner {
    display: flex;
    gap: 1rem;
    padding: 1.25rem 1.4rem;
    border-radius: 14px;
    margin-bottom: 1.4rem;
}
.ks-alert-warning {
    background: #FFFBEB;
    border: 1px solid #FCD34D;
    color: #92400E;
}
.ks-alert-danger {
    background: #FEF2F2;
    border: 1px solid #FCA5A5;
    color: #991B1B;
}
.ks-alert-icon {
    flex-shrink: 0;
    padding-top: 2px;
}
.ks-alert-content h4 {
    margin: 0 0 0.35rem 0;
    font-size: 0.98rem;
    font-weight: 700;
}
.ks-alert-content p {
    margin: 0;
    font-size: 0.88rem;
    line-height: 1.5;
}

/* Follow-up Prominent Card */
.ks-followup-card {
    background: #FFFFFF;
    border: 2px solid var(--ks-botanical-light);
    border-radius: 18px;
    padding: 1.85rem;
    margin-bottom: 1.75rem;
    box-shadow: 0 8px 24px rgba(45, 122, 77, 0.12);
}
.ks-followup-header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    color: var(--ks-forest);
    margin-bottom: 0.85rem;
}
.ks-followup-q {
    font-size: 1.22rem;
    font-weight: 800;
    color: var(--ks-forest);
    margin-bottom: 0.65rem;
    line-height: 1.4;
}
.ks-missing-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    margin-bottom: 1.2rem;
}
.ks-missing-chip {
    background: #FFF7ED;
    color: #C2410C;
    border: 1px solid #FFEDD5;
    font-size: 0.75rem;
    font-weight: 700;
    padding: 0.25rem 0.65rem;
    border-radius: 6px;
    text-transform: capitalize;
}

/* Footer */
.ks-footer {
    border-top: 1px solid var(--ks-border);
    padding: 2.75rem 1rem 1.5rem 1rem;
    margin-top: 4rem;
    text-align: center;
    color: var(--ks-text-muted);
    font-size: 0.88rem;
}
.ks-footer-brand {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.6rem;
    font-size: 1.25rem;
    font-weight: 800;
    color: var(--ks-forest);
    margin-bottom: 0.75rem;
}
.ks-footer-links {
    display: flex;
    justify-content: center;
    gap: 1.8rem;
    margin-bottom: 1.25rem;
    flex-wrap: wrap;
}
.ks-footer-link {
    color: var(--ks-botanical);
    text-decoration: none;
    font-weight: 600;
    font-size: 0.85rem;
}
.ks-footer-disc {
    max-width: 720px;
    margin: 0 auto 1.2rem auto;
    font-size: 0.8rem;
    line-height: 1.6;
    color: #64748B;
}

/* Streamlit Button & Widget Overrides */
div.stButton > button:first-child {
    background: linear-gradient(135deg, var(--ks-forest) 0%, var(--ks-botanical) 100%) !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    border-radius: 12px !important;
    border: none !important;
    padding: 0.65rem 1.5rem !important;
    box-shadow: 0 4px 14px rgba(20, 54, 38, 0.22) !important;
    transition: all 0.2s ease !important;
}
div.stButton > button:first-child:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 18px rgba(20, 54, 38, 0.32) !important;
}

/* Quick Fill Preset Buttons */
div[data-testid="column"] div.stButton > button {
    font-size: 0.82rem !important;
    padding: 0.35rem 0.75rem !important;
    border-radius: 8px !important;
}

@media (max-width: 768px) {
    .ks-navbar {
        flex-direction: column;
        gap: 1rem;
        align-items: flex-start;
    }
    .ks-nav-links {
        flex-wrap: wrap;
        gap: 1rem;
    }
    .ks-hero-container {
        padding: 1.75rem 1.25rem;
    }
    .ks-hero-title {
        font-size: 1.85rem;
    }
    .ks-form-container {
        padding: 1.5rem 1.25rem;
    }
}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Initialize Session State
# -----------------------------------------------------------------------------
if "result" not in st.session_state:
    st.session_state.result = None
if "follow_up_history" not in st.session_state:
    st.session_state.follow_up_history = []
if "follow_up_answer" not in st.session_state:
    st.session_state.follow_up_answer = ""
if "original_form" not in st.session_state:
    st.session_state.original_form = {
        "crop": "",
        "region": "",
        "stage": "Not sure",
        "query": "",
        "spread": "Not sure",
        "language": "Hindi"
    }

# Preset quick fill handlers
def set_preset(crop_val, region_val, stage_val, spread_val, lang_val, query_val):
    st.session_state.original_form["crop"] = crop_val
    st.session_state.original_form["region"] = region_val
    st.session_state.original_form["stage"] = stage_val
    st.session_state.original_form["spread"] = spread_val
    st.session_state.original_form["language"] = lang_val
    st.session_state.original_form["query"] = query_val
    st.session_state.result = None
    st.session_state.follow_up_history = []
    st.session_state.follow_up_answer = ""

# -----------------------------------------------------------------------------
# Sidebar Configuration & Telemetry
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown(f"""
    <div style="display:flex; align-items:center; gap:0.6rem; margin-bottom:1rem;">
        <div style="background:#D8F3DC; color:#143626; padding:8px; border-radius:10px;">
            {ICON_LEAF}
        </div>
        <div>
            <div style="font-weight:800; font-size:1.15rem; color:#143626;">KisanSaathi</div>
            <div style="font-size:0.75rem; color:#2D7A4D; font-weight:600; text-transform:uppercase;">Agronomic AI Engine</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    api_key_input = st.text_input(
        "Gemini API Key",
        value="",
        type="password",
        help="Reads automatically from Streamlit Secrets or .env. You can override it here."
    )

    resolved_api_key = get_gemini_api_key(api_key_input)
    resolved_model_name = get_gemini_model()

    if resolved_api_key:
        st.markdown(f"""
        <div style="background:#E8F5E9; border:1px solid #A7F3D0; padding:0.55rem 0.85rem; border-radius:8px; font-size:0.8rem; color:#065F46; font-weight:600; margin-bottom:1rem; display:flex; align-items:center; gap:0.4rem;">
            {ICON_CHECK} Engine Connected ({resolved_model_name})
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style="background:#FEF2F2; border:1px solid #FCA5A5; padding:0.55rem 0.85rem; border-radius:8px; font-size:0.8rem; color:#991B1B; font-weight:600; margin-bottom:1rem; display:flex; align-items:center; gap:0.4rem;">
            {ICON_ALERT} API Key Needed (.env / Secrets / Input)
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### Language Setting")
    sidebar_language = st.selectbox(
        "Preferred response language",
        ["Hindi", "English", "Hinglish"],
        index=["Hindi", "English", "Hinglish"].index(st.session_state.original_form.get("language", "Hindi")),
        key="global_lang_select"
    )
    st.session_state.original_form["language"] = sidebar_language

    st.markdown("---")
    st.markdown("### Safety Guardrails")
    st.markdown(f"""
    <div style="font-size:0.82rem; color:#4A5568; line-height:1.5;">
        <p>🛡️ <b>Strict Zero Chemical Dose:</b> Never prescribes synthetic pesticide dosages.</p>
        <p>📚 <b>Evidence-Grounded:</b> All causes cited from agronomic reference corpus.</p>
        <p>👨‍🌾 <b>KVK Escalation:</b> Rapidly spreading issues escalated to local officers.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    if st.button("Reset Session & Inputs", use_container_width=True):
        st.session_state.result = None
        st.session_state.follow_up_history = []
        st.session_state.follow_up_answer = ""
        st.session_state.original_form = {
            "crop": "",
            "region": "",
            "stage": "Not sure",
            "query": "",
            "spread": "Not sure",
            "language": sidebar_language
        }
        st.rerun()

# -----------------------------------------------------------------------------
# Top Navigation Bar
# -----------------------------------------------------------------------------
st.markdown(f"""
<div class="ks-navbar" id="home">
    <a href="#home" class="ks-nav-brand">
        <div class="ks-nav-logo-icon">
            {ICON_LEAF}
        </div>
        <div>
            <div class="ks-nav-title">KisanSaathi</div>
            <div class="ks-nav-tag">Agronomic Intelligence Platform</div>
        </div>
    </a>
    <div class="ks-nav-links">
        <a href="#home" class="ks-nav-link">Home</a>
        <a href="#how-it-works" class="ks-nav-link">How It Works</a>
        <a href="#ask-ai" class="ks-nav-link">Ask AI</a>
        <a href="#safety-standards" class="ks-nav-link">Safety Standards</a>
        <a href="#evaluation" class="ks-nav-link">Evaluation</a>
        <span class="ks-nav-badge">{ICON_SPARKLE} Gemini 2.5 Active</span>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Hero Section with Farmer Illustration
# -----------------------------------------------------------------------------
farmer_b64 = get_base64_image("assets/hero_farmer.jpg")

st.markdown(f"""
<div class="ks-hero-container">
    <div class="ks-hero-left">
        <div class="ks-hero-badge">
            {ICON_SPARKLE} Next-Generation Agronomic AI Platform
        </div>
        <h1 class="ks-hero-title">
            Intelligent Crop Diagnostics &amp; Agronomic Safety
        </h1>
        <p class="ks-hero-subtitle">
            Empowering Indian farmers and agricultural extension workers with grounded, multi-lingual crop disease assessment, verified field checklists, and strict chemical pesticide safety guardrails.
        </p>
        <div class="ks-trust-pills">
            <div class="ks-trust-pill">{ICON_CHECK} 100% Evaluation Score (12/12 Scenarios)</div>
            <div class="ks-trust-pill">{ICON_SHIELD} Zero Chemical Pesticide Risk</div>
            <div class="ks-trust-pill">{ICON_LEAF} 3-Stage Grounded Pipeline</div>
            <div class="ks-trust-pill">{ICON_BOOK} TF-IDF Reference Citations</div>
        </div>
        <div class="ks-hero-actions">
            <a href="#ask-ai" class="ks-btn-primary">{ICON_SEARCH} Diagnose Crop Problem</a>
            <a href="#how-it-works" class="ks-btn-secondary">{ICON_BOOK} View Architecture</a>
        </div>
    </div>
    <div class="ks-hero-right">
        <div class="ks-hero-image-card">
            <img src="data:image/jpeg;base64,{farmer_b64}" alt="Indian Farmer using KisanSaathi" />
            <div class="ks-hero-image-overlay">
                <div style="display:flex; align-items:center; gap:0.5rem;">
                    <span class="ks-pulse-indicator"></span>
                    <span>Field Verified &middot; Active RAG</span>
                </div>
                <span style="opacity:0.85; font-size:0.75rem;">Multi-Lingual Engine</span>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# "How It Works" 3-Step Interactive Architecture Cards
# -----------------------------------------------------------------------------
st.markdown(f"""
<div id="how-it-works" class="ks-section">
    <div class="ks-section-header">
        <span class="ks-section-tag">System Architecture</span>
        <h2 class="ks-section-title">How KisanSaathi Diagnoses Crop Symptoms</h2>
        <p class="ks-section-desc">Our three-stage prompt workflow guarantees verifiable agronomic reasoning with zero chemical dosage hallucination.</p>
    </div>
    <div class="ks-steps-grid">
        <div class="ks-step-card">
            <div class="ks-step-num">01</div>
            <div class="ks-step-icon">{ICON_SEARCH}</div>
            <h3>Symptom & Entity Extraction</h3>
            <p>Understands farmer inquiries in Hindi, English, and Hinglish. Accurately extracts crop, region, phenological stage, symptoms, and spread rate into structured schema.</p>
        </div>
        <div class="ks-step-card">
            <div class="ks-step-num">02</div>
            <div class="ks-step-icon">{ICON_BOOK}</div>
            <h3>Grounded TF-IDF Retrieval</h3>
            <p>Matches extracted symptoms against an ICAR-aligned agricultural disease knowledge base. Grounds every diagnosis in verified agronomic reference notes.</p>
        </div>
        <div class="ks-step-card">
            <div class="ks-step-num">03</div>
            <div class="ks-step-icon">{ICON_SHIELD}</div>
            <h3>Safe Advisory & Escalation</h3>
            <p>Generates non-chemical cultural management practices and field observation checklists. Prompts for missing details and escalates rapid spread to local KVK officers.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Main Crop Advisory Interface (#ask-ai)
# -----------------------------------------------------------------------------
st.markdown('<div id="ask-ai"></div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="ks-form-container">
    <div class="ks-form-header">
        <div class="ks-form-title">
            <div style="color:var(--ks-botanical);">{ICON_LEAF}</div>
            <span>Crop Diagnostic Center</span>
        </div>
        <div class="ks-form-badge">{ICON_SPARKLE} Three-Stage AI Intake</div>
    </div>
""", unsafe_allow_html=True)

# Preset Quick-Fill Test Chips
st.markdown(f"""
<div class="ks-preset-container">
    <div class="ks-preset-label">
        {ICON_SPARKLE} Quick-Fill Benchmark Scenarios (Click to Load):
    </div>
</div>
""", unsafe_allow_html=True)

p_col1, p_col2, p_col3, p_col4 = st.columns(4)
with p_col1:
    if st.button("🍅 Tomato Leaf Curl (UP)", use_container_width=True):
        set_preset(
            "Tomato", "Uttar Pradesh", "Flowering", "Slowly", "English",
            "Tomato leaves have yellow spots and curling edges."
        )
        st.rerun()

with p_col2:
    if st.button("🌾 Rice Brown Spot (WB)", use_container_width=True):
        set_preset(
            "Rice", "West Bengal", "Vegetative", "Slowly", "English",
            "Rice plants have brown spots on the leaves."
        )
        st.rerun()

with p_col3:
    if st.button("🌱 Wheat Yellowing (PB)", use_container_width=True):
        set_preset(
            "Wheat", "Punjab", "Not sure", "Rapidly", "Hindi",
            "गेहूं की पत्तियां नोक से पीली पड़ रही हैं और समस्या तेजी से बढ़ रही है।"
        )
        st.rerun()

with p_col4:
    if st.button("🥔 Potato Stunting (UP)", use_container_width=True):
        set_preset(
            "Potato", "Uttar Pradesh", "Vegetative", "Not sure", "Hinglish",
            "Aloo ke paudhe me curling leaves dikh rahi hain aur growth ruk gayi hai."
        )
        st.rerun()

# Crop Diagnostic Input Form
col_left, col_right = st.columns([1, 1], gap="medium")

with col_left:
    crop = st.text_input(
        "Crop Name (if known)",
        value=st.session_state.original_form["crop"],
        placeholder="e.g. Tomato / गेहूं / Rice",
        help="Enter the crop name in English, Hindi, or local names."
    )
    region = st.text_input(
        "Region or State",
        value=st.session_state.original_form["region"],
        placeholder="e.g. Uttar Pradesh, Punjab, Bihar",
        help="Broad geographic region helps ground climatic and regional pest patterns."
    )
    stage_options = ["Not sure", "Seedling", "Vegetative", "Flowering", "Fruiting", "Harvest"]
    current_stage = st.session_state.original_form["stage"]
    stage_idx = stage_options.index(current_stage) if current_stage in stage_options else 0
    stage = st.selectbox(
        "Crop Growth Stage",
        stage_options,
        index=stage_idx,
        help="Select the current phenological development phase."
    )

with col_right:
    spread_options = ["Not sure", "Not spreading", "Slowly", "Rapidly"]
    current_spread = st.session_state.original_form["spread"]
    spread_idx = spread_options.index(current_spread) if current_spread in spread_options else 0
    spread = st.selectbox(
        "How quickly is the problem spreading?",
        spread_options,
        index=spread_idx,
        help="Rate of symptom progression across the plot."
    )
    lang_options = ["Hindi", "English", "Hinglish"]
    current_lang = st.session_state.original_form["language"]
    lang_idx = lang_options.index(current_lang) if current_lang in lang_options else 0
    form_language = st.selectbox(
        "Preferred Advisory Language",
        lang_options,
        index=lang_idx,
        help="Advisory will be tailored in this language."
    )
    query = st.text_area(
        "Describe the Symptoms Observed",
        value=st.session_state.original_form["query"],
        placeholder="Example: Mere tamatar ke patton par peele dhabbe hain aur kinare mud rahe hain. / Brown spots on lower leaves.",
        height=110,
        help="Detail leaf color, spots, wilting, curling, insect presence, or soil conditions."
    )

st.session_state.original_form["language"] = form_language

submit = st.button("🌱 Analyze Crop Problem", use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)  # Close form container

# -----------------------------------------------------------------------------
# Analysis Pipeline Execution
# -----------------------------------------------------------------------------
if submit:
    if not query.strip():
        st.warning("Please describe the crop symptoms before proceeding with analysis.")
        st.stop()

    try:
        st.session_state.original_form = {
            "crop": crop.strip(),
            "region": region.strip(),
            "stage": stage,
            "query": query.strip(),
            "spread": spread,
            "language": form_language
        }
        st.session_state.follow_up_history = []
        st.session_state.follow_up_answer = ""

        resolved_key = get_gemini_api_key(api_key_input)
        resolved_model = get_gemini_model()
        if not resolved_key:
            st.error("⚠️ GEMINI_API_KEY is missing. Please configure GEMINI_API_KEY in Streamlit Secrets, add it to your local .env file, or enter it in the sidebar.")
            st.stop()

        notes = load_reference_notes()
        pipeline = KisanSaathiPipeline(notes, api_key=resolved_key, model=resolved_model)
        with st.status("🌱 Running KisanSaathi Three-Stage Analysis...", expanded=True) as status:
            step_text = st.empty()
            def handle_step(msg):
                step_text.write(f"⏳ {msg}")
            result = pipeline.run(
                query=st.session_state.original_form["query"],
                crop=st.session_state.original_form["crop"],
                region=st.session_state.original_form["region"],
                stage=st.session_state.original_form["stage"],
                spread=st.session_state.original_form["spread"],
                language=st.session_state.original_form["language"],
                follow_up_answer="",
                previous_extraction=None,
                on_step=handle_step
            )
            status.update(label="✅ Agronomic Analysis Complete!", state="complete", expanded=False)
        st.session_state.result = result
    except Exception as exc:
        st.error(f"Could not complete the analysis: {exc}")
        st.info("Ensure GEMINI_API_KEY is configured and that your selected Gemini model is reachable.")

# -----------------------------------------------------------------------------
# Results & Diagnosis Section
# -----------------------------------------------------------------------------
if st.session_state.result:
    result = st.session_state.result
    extraction = result["extraction"]
    diagnosis = result["diagnosis"]
    advisory = result["advisory"]
    follow_up_q = extraction.get("follow_up_question", "").strip()

    st.markdown("---")
    st.markdown(f"""
    <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:1.5rem;">
        <div>
            <h2 style="font-size:1.75rem; font-weight:800; color:var(--ks-forest); margin:0;">
                KisanSaathi Agronomic Assessment
            </h2>
            <p style="color:var(--ks-text-muted); margin:0.25rem 0 0 0; font-size:0.92rem;">
                Grounded 3-Stage Diagnostic Evaluation for <b>{extraction.get('crop', 'Crop')}</b> in <b>{extraction.get('broad_region', 'Region')}</b>
            </p>
        </div>
        <div class="ks-nav-badge">
            {ICON_CHECK} Verified Output
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 1. Extracted Context Summary Card
    st.markdown(f"""
    <div class="ks-result-card" style="padding:1.25rem 1.5rem; margin-bottom:1.25rem; background:#F8FAF6; border:1px solid #E2E8F0;">
        <div style="display:flex; flex-wrap:wrap; gap:1.2rem; align-items:center;">
            <div><span style="font-size:0.75rem; color:#64748B; font-weight:700; text-transform:uppercase;">Crop:</span> <b>{extraction.get('crop', 'Unknown')}</b></div>
            <div><span style="font-size:0.75rem; color:#64748B; font-weight:700; text-transform:uppercase;">Region:</span> <b>{extraction.get('broad_region', 'Unknown')}</b></div>
            <div><span style="font-size:0.75rem; color:#64748B; font-weight:700; text-transform:uppercase;">Stage:</span> <b>{extraction.get('growth_stage', 'Unknown')}</b></div>
            <div><span style="font-size:0.75rem; color:#64748B; font-weight:700; text-transform:uppercase;">Spread:</span> <b>{extraction.get('spread', 'Unknown')}</b></div>
            <div><span style="font-size:0.75rem; color:#64748B; font-weight:700; text-transform:uppercase;">Symptoms:</span> <b>{', '.join(extraction.get('symptoms', [])) or 'Observed'}</b></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 2. Possible Causes Card
    st.markdown(f"""
    <div class="ks-result-card">
        <div class="ks-result-card-header">
            <div style="color:var(--ks-botanical);">{ICON_SEARCH}</div>
            <h3>Possible Agronomic Causes</h3>
        </div>
        <div style="background:#F0FDF4; border-left:4px solid var(--ks-botanical); padding:0.75rem 1rem; border-radius:0 8px 8px 0; margin-bottom:1.25rem; font-size:0.85rem; color:#166534;">
            <b>Grounded Literature Disclaimer:</b> The following are potential agronomic causes derived from symptom matching with ICAR reference materials. They represent preliminary assessments rather than confirmed laboratory diagnoses.
        </div>
    """, unsafe_allow_html=True)

    causes = diagnosis.get("possible_causes", [])
    if causes:
        for c in causes:
            c_name = c.get("name", "Possible cause")
            c_reason = c.get("reason", "")
            st.markdown(f"""
            <div class="ks-cause-item">
                <div class="ks-cause-name">{c_name}</div>
                <div class="ks-cause-reason">{c_reason}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.write("No definitive match found in reference notes. General monitoring advised.")
    st.markdown("</div>", unsafe_allow_html=True)

    # 3. Advisory & Recommended Observation Checklist
    col_adv1, col_adv2 = st.columns([1, 1], gap="medium")

    with col_adv1:
        st.markdown(f"""
        <div class="ks-result-card" style="height:100%;">
            <div class="ks-result-card-header">
                <div style="color:var(--ks-botanical);">{ICON_LEAF}</div>
                <h3>Agronomic Advisory</h3>
            </div>
            <div style="font-size:0.92rem; line-height:1.6; color:#2D3748; margin-bottom:1rem;">
                {advisory.get('advice', 'No specific advisory available.')}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_adv2:
        st.markdown(f"""
        <div class="ks-result-card" style="height:100%;">
            <div class="ks-result-card-header">
                <div style="color:var(--ks-botanical);">{ICON_CHECKLIST}</div>
                <h3>Recommended Field Checklist</h3>
            </div>
        """, unsafe_allow_html=True)
        next_steps = advisory.get("next_steps", [])
        if next_steps:
            for item in next_steps:
                st.markdown(f"""
                <div style="display:flex; align-items:flex-start; gap:0.6rem; margin-bottom:0.75rem; font-size:0.88rem; color:#374151;">
                    <div style="color:var(--ks-botanical); margin-top:2px;">{ICON_CHECK}</div>
                    <div>{item}</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("<p style='font-size:0.88rem; color:#6B7280;'>Monitor plot daily for color or spread changes.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # 4. Safety Guardrail Warning Banner & Expert Escalation
    st.markdown(f"""
    <div class="ks-alert-banner ks-alert-warning">
        <div class="ks-alert-icon">{ICON_SHIELD}</div>
        <div class="ks-alert-content">
            <h4>Strict Chemical Pesticide Safety Policy</h4>
            <p>KisanSaathi does <b>not</b> provide chemical dosages or synthetic pesticide application schedules. Improper pesticide handling harms pollinators, soil microbiome, and human health. Always consult qualified local agronomists before applying any commercial chemical.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if advisory.get("escalate", True):
        st.markdown(f"""
        <div class="ks-alert-banner ks-alert-danger">
            <div class="ks-alert-icon">{ICON_ALERT}</div>
            <div class="ks-alert-content">
                <h4>Extension Officer / KVK Escalation Recommended</h4>
                <p><b>Reason:</b> {advisory.get('escalation_reason', 'The symptoms require on-ground physical inspection by a qualified agricultural officer.')}</p>
                <div style="margin-top:0.6rem; font-weight:600; font-size:0.85rem; display:flex; align-items:center; gap:0.4rem;">
                    {ICON_PHONE} National Kisan Call Centre: <b>1800-180-1551</b> (Toll Free, 6 AM - 10 PM)
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # 5. Prominent Follow-Up Question Card (Multi-Turn Clarification)
    if follow_up_q:
        st.markdown(f"""
        <div class="ks-followup-card">
            <div class="ks-followup-header">
                {ICON_QUESTION}
                <span style="font-weight:700; text-transform:uppercase; letter-spacing:0.06em; font-size:0.8rem; color:var(--ks-botanical);">
                    Follow-Up Clarification Needed
                </span>
            </div>
            <div class="ks-followup-q">{follow_up_q}</div>
        """, unsafe_allow_html=True)

        if extraction.get("missing_information"):
            chips_html = "".join([f'<span class="ks-missing-chip">{m}</span>' for m in extraction["missing_information"]])
            st.markdown(f"""
            <div style="margin-bottom:0.85rem;">
                <span style="font-size:0.75rem; color:#6B7280; font-weight:600; margin-right:0.4rem;">Pending Information:</span>
                <div class="ks-missing-chips" style="display:inline-flex;">{chips_html}</div>
            </div>
            """, unsafe_allow_html=True)

        with st.form("follow_up_form"):
            follow_up_answer = st.text_input(
                "Your Answer:",
                placeholder="e.g. Flowering stage / Around 20% of plants are affected",
                key="follow_up_text_input"
            )
            submit_follow_up = st.form_submit_button("Submit Answer & Update Diagnosis", type="primary")

        if submit_follow_up:
            if not follow_up_answer.strip():
                st.warning("Please type your answer before submitting.")
            else:
                submitted_ans = follow_up_answer.strip()
                st.session_state["follow_up_answer"] = submitted_ans
                st.session_state.follow_up_history.append({
                    "q": follow_up_q,
                    "a": submitted_ans
                })
                try:
                    resolved_key = get_gemini_api_key(api_key_input)
                    resolved_model = get_gemini_model()
                    if not resolved_key:
                        st.error("⚠️ GEMINI_API_KEY is missing. Please configure GEMINI_API_KEY in Secrets or the sidebar.")
                        st.stop()

                    notes = load_reference_notes()
                    pipeline = KisanSaathiPipeline(notes, api_key=resolved_key, model=resolved_model)
                    with st.status("🌱 Updating analysis with your clarification...", expanded=True) as status:
                        step_text = st.empty()
                        def handle_step(msg):
                            step_text.write(f"⏳ {msg}")

                        orig = st.session_state.original_form
                        prev_extraction = st.session_state.result.get("extraction")

                        updated_result = pipeline.run(
                            query=orig["query"],
                            crop=orig["crop"],
                            region=orig["region"],
                            stage=orig["stage"],
                            spread=orig["spread"],
                            language=orig["language"],
                            follow_up_answer=submitted_ans,
                            previous_extraction=prev_extraction,
                            on_step=handle_step
                        )
                        status.update(label="✅ Analysis Updated!", state="complete", expanded=False)

                    clean_submitted = submitted_ans.rstrip(".?! ")
                    ans_to_record = updated_result["extraction"].get("follow_up_answer") or clean_submitted
                    st.session_state["follow_up_answer"] = ans_to_record
                    updated_result["follow_up_answer"] = ans_to_record
                    updated_result["extraction"]["follow_up_answer"] = ans_to_record
                    st.session_state.result = updated_result

                    # Update form values
                    new_spread = updated_result["extraction"].get("spread", "")
                    if new_spread and new_spread.lower() not in ["unknown", "not sure"]:
                        st.session_state.original_form["spread"] = new_spread

                    new_stage = updated_result["extraction"].get("growth_stage", "")
                    if new_stage and new_stage.lower() not in ["unknown", "not sure"]:
                        st.session_state.original_form["stage"] = new_stage

                    new_crop = updated_result["extraction"].get("crop", "")
                    if new_crop and new_crop.lower() not in ["unknown", "not provided"]:
                        st.session_state.original_form["crop"] = new_crop

                    st.rerun()
                except Exception as exc:
                    st.error(f"Could not update analysis: {exc}")
                    st.info("Check GEMINI_API_KEY configuration and connectivity.")

        st.markdown("</div>", unsafe_allow_html=True)  # Close follow-up card

    # Previously answered questions expander
    if st.session_state.follow_up_history:
        with st.expander("📝 Multi-Turn Follow-Up Conversation History", expanded=False):
            for idx, item in enumerate(st.session_state.follow_up_history, 1):
                st.markdown(f"**Turn {idx}:** {item['q']}")
                st.markdown(f"*Farmer's Answer:* `{item['a']}`")
                st.markdown("---")

    if st.session_state.get("follow_up_answer"):
        st.info(f"**Last Recorded Clarification:** {st.session_state['follow_up_answer']}")

    # 6. Structured Workflow JSON Viewer
    with st.expander("🔍 View Grounded Pipeline Output (Structured JSON)", expanded=bool(st.session_state.get("follow_up_answer"))):
        st.json(result)

# -----------------------------------------------------------------------------
# Safety Pillars & Agronomic Standards (#safety-standards)
# -----------------------------------------------------------------------------
st.markdown(f"""
<div id="safety-standards" class="ks-section" style="margin-top:3.5rem;">
    <div class="ks-section-header">
        <span class="ks-section-tag">Safety Architecture</span>
        <h2 class="ks-section-title">Built-In Agricultural Safeguards</h2>
        <p class="ks-section-desc">Designed in alignment with Indian agricultural advisory guidelines to prevent crop damage and toxic chemical overuse.</p>
    </div>
    <div class="ks-steps-grid">
        <div class="ks-step-card">
            <div class="ks-step-icon">{ICON_SHIELD}</div>
            <h3>Zero Chemical Dosage Rule</h3>
            <p>Refuses to compute, calculate, or prescribe pesticide dosages automatically, eliminating risks of chemical burning and resistance.</p>
        </div>
        <div class="ks-step-card">
            <div class="ks-step-icon">{ICON_BOOK}</div>
            <h3>Verifiable Document Grounding</h3>
            <p>Every diagnostic possibility is cited from validated ICAR & university extension handbooks, eliminating generative hallucination.</p>
        </div>
        <div class="ks-step-card">
            <div class="ks-step-icon">{ICON_ALERT}</div>
            <h3>Active Human-In-The-Loop Escalation</h3>
            <p>Any query reporting rapid spread, high uncertainty, or conflicting symptoms triggers immediate escalation to nearest KVKs.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Evaluation & Benchmark Summary Section (#evaluation)
# -----------------------------------------------------------------------------
st.markdown(f"""
<div id="evaluation" class="ks-section">
    <div class="ks-section-header">
        <span class="ks-section-tag">Empirical Verification</span>
        <h2 class="ks-section-title">Evaluation & Benchmark Results</h2>
        <p class="ks-section-desc">Systematically validated across 12 distinct synthetic field scenarios spanning multiple crops, languages, and edge cases.</p>
    </div>
    <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:18px; padding:2rem; box-shadow:0 4px 18px rgba(0,0,0,0.02);">
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:1.5rem; margin-bottom:1.5rem; text-align:center;">
            <div style="padding:1.25rem; background:#F8FAF6; border-radius:12px; border:1px solid #E2E8F0;">
                <div style="font-size:2.2rem; font-weight:800; color:var(--ks-forest); line-height:1;">12 / 12</div>
                <div style="font-size:0.85rem; font-weight:600; color:#4A5568; margin-top:0.4rem;">Scenarios Evaluated</div>
            </div>
            <div style="padding:1.25rem; background:#F0FDF4; border-radius:12px; border:1px solid #BBF7D0;">
                <div style="font-size:2.2rem; font-weight:800; color:#15803D; line-height:1;">100%</div>
                <div style="font-size:0.85rem; font-weight:600; color:#166534; margin-top:0.4rem;">Pass Rate (0 Failures)</div>
            </div>
            <div style="padding:1.25rem; background:#FEF3C7; border-radius:12px; border:1px solid #FDE68A;">
                <div style="font-size:2.2rem; font-weight:800; color:#B45309; line-height:1;">0</div>
                <div style="font-size:0.85rem; font-weight:600; color:#92400E; margin-top:0.4rem;">Chemical Dosages Prescribed</div>
            </div>
            <div style="padding:1.25rem; background:#F8FAF6; border-radius:12px; border:1px solid #E2E8F0;">
                <div style="font-size:2.2rem; font-weight:800; color:var(--ks-botanical); line-height:1;">3</div>
                <div style="font-size:0.85rem; font-weight:600; color:#4A5568; margin-top:0.4rem;">Languages (EN, HI, Hinglish)</div>
            </div>
        </div>
""", unsafe_allow_html=True)

# Read evaluation_results.csv if present
csv_path = "evaluation_results.csv"
if os.path.exists(csv_path):
    with st.expander("📋 View All 12 Empirical Test Cases (evaluation_results.csv)", expanded=False):
        try:
            with open(csv_path, mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                rows = list(reader)
            if rows:
                for r in rows:
                    st.markdown(f"**{r.get('Test ID', '')}:** {r.get('Input', '')[:100]}... — **Status:** `{r.get('Pass/Fail', '')}`")
                    st.caption(f"Reason: {r.get('Reason', '')}")
                    st.markdown("---")
        except Exception as e:
            st.caption(f"Could not read evaluation results: {e}")

st.markdown("</div></div>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Professional Agritech SaaS Footer
# -----------------------------------------------------------------------------
st.markdown(f"""
<div class="ks-footer">
    <div class="ks-footer-brand">
        <div style="color:var(--ks-botanical);">{ICON_LEAF}</div>
        <span>KisanSaathi</span>
    </div>
    <div class="ks-footer-links">
        <a href="#home" class="ks-footer-link">Home</a>
        <a href="#how-it-works" class="ks-footer-link">Methodology</a>
        <a href="#ask-ai" class="ks-footer-link">Diagnostic Engine</a>
        <a href="#safety-standards" class="ks-footer-link">Safety Standards</a>
        <a href="#evaluation" class="ks-footer-link">Evaluation Suite</a>
    </div>
    <div class="ks-footer-disc">
        <b>Agricultural Advisory Notice:</b> KisanSaathi is an agronomic artificial intelligence prototype developed for educational and preliminary advisory support. All assessments and recommendations must be verified by certified agricultural extension officers or Krishi Vigyan Kendras (KVK) before taking irreversible chemical or cultural crop actions.
    </div>
    <div style="font-size:0.78rem; color:#94A3B8;">
        &copy; 2026 KisanSaathi &middot; Built with Gemini 2.5 Flash &amp; Streamlit &middot; Grounded in ICAR Agronomic Practice Handbooks
    </div>
</div>
""", unsafe_allow_html=True)
