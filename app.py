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
    page_title="KisanSaathi | AI Crop Advisory Assistant",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------------------------------------------------------
# Complete Light Theme CSS (Forces #F7F8F2 Globally — Zero Dark Margins)
# -----------------------------------------------------------------------------
CSS_LIGHT_THEME = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root,
html,
body,
[data-theme="dark"],
[data-theme="light"],
.stApp {
    color-scheme: light !important;
    --background-color: #F7F8F2 !important;
    --secondary-background-color: #E7F2E8 !important;
    --text-color: #25352D !important;
    --primary-color: #174B35 !important;
}

/* 1. FORCE COMPLETE VIEWPORT & ROOT CONTAINERS TO WARM IVORY #F7F8F2 */
html,
body,
#root,
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewRoot"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"],
[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stBottom"],
[data-testid="stDecoration"],
[data-testid="stSidebarCollapseButton"],
section[data-testid="stMain"],
section.main,
.main,
.block-container,
.main .block-container {
    background-color: #F7F8F2 !important;
    background: #F7F8F2 !important;
    color: #25352D !important;
}

/* Overwrite dark mode media queries from browser or Streamlit Cloud */
@media (prefers-color-scheme: dark) {
    :root,
    html,
    body,
    #root,
    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stAppViewRoot"],
    [data-testid="stMain"],
    [data-testid="stMainBlockContainer"],
    [data-testid="stHeader"],
    [data-testid="stToolbar"],
    [data-testid="stBottom"],
    section[data-testid="stMain"],
    section.main,
    .main,
    .block-container {
        background-color: #F7F8F2 !important;
        background: #F7F8F2 !important;
        color: #25352D !important;
    }
    [data-testid="stSidebar"],
    [data-testid="stSidebarContent"],
    section[data-testid="stSidebar"],
    section[data-testid="stSidebar"] > div {
        background-color: #FFFFFF !important;
        background: #FFFFFF !important;
        color: #25352D !important;
    }
}

/* Containers with border (like intake form & follow-up card) */
[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: transparent !important;
    border: none !important;
    padding: 0 !important;
    margin-bottom: 2rem !important;
}
[data-testid="stVerticalBlockBorderWrapper"] > div {
    background-color: #FFFFFF !important;
    background: #FFFFFF !important;
    border: 1.5px solid #E2E9E1 !important;
    border-radius: 20px !important;
    padding: 2.25rem 2.4rem !important;
    box-shadow: 0 4px 22px rgba(23, 75, 53, 0.04) !important;
}

/* Regular vertical and horizontal blocks stay transparent */
[data-testid="stVerticalBlock"]:not([data-testid="stVerticalBlockBorderWrapper"]),
[data-testid="stHorizontalBlock"],
[data-testid="column"],
div[data-testid="column"] {
    background-color: transparent !important;
    background: transparent !important;
}

/* 2. SIDEBAR LIGHT STYLING */
[data-testid="stSidebar"],
[data-testid="stSidebarContent"],
section[data-testid="stSidebar"],
section[data-testid="stSidebar"] > div {
    background-color: #FFFFFF !important;
    background: #FFFFFF !important;
    border-right: 1px solid #E2E9E1 !important;
    color: #25352D !important;
}

/* 3. TYPOGRAPHY & RESET */
html, body, [class*="css"], .stMarkdown, .stTextInput label,
.stSelectbox label, .stTextArea label, .stButton button {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
}

.block-container,
.main .block-container,
[data-testid="stMainBlockContainer"],
[data-testid="block-container"],
.stMainBlockContainer,
section[data-testid="stMain"] > div:first-child,
div[data-testid="stAppViewContainer"] > section > div {
    max-width: 100% !important;
    width: 100% !important;
    padding-top: 0 !important;
    padding-bottom: 3.5rem !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
}

header[data-testid="stHeader"],
[data-testid="stHeader"],
.stApp > header {
    display: none !important;
    height: 0 !important;
    min-height: 0 !important;
    padding: 0 !important;
    margin: 0 !important;
}

[data-testid="stHeaderActionElements"],
a.header-anchor,
.stMarkdown h1 a,
.stMarkdown h2 a,
.stMarkdown h3 a {
    display: none !important;
}

/* Remove default blue link styling and underlines */
a,
a:visited,
a:hover,
a:active,
.stMarkdown a,
[data-testid="stMarkdownContainer"] a {
    color: #25352D !important;
    text-decoration: none !important;
}
a:hover,
.stMarkdown a:hover,
[data-testid="stMarkdownContainer"] a:hover {
    color: #2E7D50 !important;
    text-decoration: none !important;
}

/* 4. TOP NAVIGATION BAR (FULL WIDTH, INTEGRATED TABS, NO MARGINS) */
.ks-navbar {
    width: 100% !important;
    height: 68px !important;
    background: #FFFFFF !important;
    border-top: none !important;
    border-left: none !important;
    border-right: none !important;
    border-bottom: 1.5px solid #E2E9E1 !important;
    border-radius: 0 !important;
    padding: 0 !important;
    margin: 0 !important;
    display: flex !important;
    align-items: center !important;
    box-shadow: 0 1px 8px rgba(23, 75, 53, 0.04) !important;
    position: relative !important;
    z-index: 99 !important;
}
.ks-navbar-inner {
    max-width: 1360px;
    margin: 0 auto;
    padding: 0 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    height: 100%;
}
.ks-nav-brand {
    display: flex;
    align-items: center;
    gap: 0.65rem;
    text-decoration: none !important;
}
.ks-nav-brand-title {
    font-size: 1.4rem;
    font-weight: 800;
    color: #174B35 !important;
    letter-spacing: -0.02em;
    line-height: 1.15;
}
.ks-nav-brand-sub {
    font-size: 0.75rem;
    font-weight: 600;
    color: #68756C;
}
.ks-nav-links {
    display: flex;
    align-items: center;
    gap: 1.4rem;
}
.ks-nav-link {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    font-size: 0.9rem;
    font-weight: 600;
    color: #25352D !important;
}
.ks-nav-link:hover {
    color: #2E7D50 !important;
}
.ks-nav-btn-active {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: #174B35 !important;
    color: #FFFFFF !important;
    font-size: 0.9rem;
    font-weight: 700;
    padding: 0.45rem 1.15rem;
    border-radius: 999px;
    box-shadow: 0 2px 8px rgba(23, 75, 53, 0.2);
    text-decoration: none !important;
}
.ks-lang-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    border: 1.5px solid #E2E9E1;
    padding: 0.4rem 0.95rem;
    border-radius: 999px;
    font-size: 0.85rem;
    font-weight: 600;
    color: #25352D;
    background: #FFFFFF;
}

/* 4.5. MODERN TABS INTEGRATED IN TOP BAR */
.stTabs {
    width: 100% !important;
    max-width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
    position: relative !important;
}
.stTabs [data-baseweb="tab-list"] {
    position: absolute !important;
    top: -53px !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    z-index: 1000 !important;
    display: flex !important;
    align-items: center !important;
    gap: 0.6rem !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    margin: 0 !important;
}
.stTabs [data-baseweb="tab"] {
    height: 38px !important;
    border-radius: 999px !important;
    padding: 0 1.25rem !important;
    background-color: transparent !important;
    color: #25352D !important;
    font-weight: 600 !important;
    font-size: 0.92rem !important;
    border: none !important;
    cursor: pointer !important;
    transition: all 0.15s ease !important;
}
.stTabs [data-baseweb="tab"]:hover {
    color: #174B35 !important;
    background-color: #E7F2E8 !important;
}
.stTabs [aria-selected="true"] {
    background-color: #174B35 !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    box-shadow: 0 2px 8px rgba(23, 75, 53, 0.22) !important;
}
.stTabs [data-baseweb="tab-highlight"],
.stTabs [data-baseweb="tab-border"] {
    display: none !important;
}
.stTabs [data-baseweb="tab-panel"] {
    width: 100% !important;
    padding: 0 !important;
}
@media (max-width: 992px) {
    .stTabs [data-baseweb="tab-list"] {
        position: static !important;
        transform: none !important;
        margin: 1rem auto !important;
        background: #FFFFFF !important;
        border: 1.5px solid #E2E9E1 !important;
        border-radius: 999px !important;
        padding: 0.4rem 0.6rem !important;
        box-shadow: 0 2px 10px rgba(23, 75, 53, 0.05) !important;
        max-width: fit-content !important;
    }
}
.ks-content-container {
    max-width: 1240px;
    margin: 0 auto;
    padding: 0 1.5rem;
    width: 100%;
}

/* Centered layout for content cards & forms across tabs */
[data-testid="stVerticalBlockBorderWrapper"],
.ks-card,
.ks-alert,
.ks-feature-strip,
div[id="how-it-works"],
div[id="safety"],
.stTabs [data-testid="stHorizontalBlock"] {
    max-width: 1240px !important;
    margin-left: auto !important;
    margin-right: auto !important;
    width: 100% !important;
}

/* 4.8. ARCHITECTURE / HOW IT WORKS PAGE (EXACT REFERENCE MOCKUP) */
.ks-how-it-works-page {
    position: relative;
    width: 100%;
    padding: 2.5rem 0 0 0;
    overflow: hidden;
    background-color: #F7F8F2;
}
.ks-bg-foliage-left {
    position: absolute;
    top: 30px;
    left: -10px;
    width: 140px;
    height: 160px;
    pointer-events: none;
    z-index: 1;
}
.ks-bg-foliage-right {
    position: absolute;
    top: 30px;
    right: -10px;
    width: 140px;
    height: 160px;
    pointer-events: none;
    z-index: 1;
}
.ks-arch-container {
    max-width: 1260px;
    margin: 0 auto;
    padding: 0 2rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1.25rem;
    position: relative;
    z-index: 2;
}
.ks-arch-card {
    flex: 1 1 340px;
    background: #FFFFFF;
    border: 1.5px solid #E2E9E1;
    border-radius: 24px;
    padding: 2.2rem 2rem 1.8rem 2rem;
    box-shadow: 0 6px 24px rgba(23, 75, 53, 0.04);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 450px;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.ks-arch-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(23, 75, 53, 0.08);
}
.ks-arch-icon-box {
    width: 48px;
    height: 48px;
    border-radius: 14px;
    background: #E7F2E8;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 1.25rem;
}
.ks-arch-card-title {
    font-size: 1.25rem;
    font-weight: 800;
    color: #174B35;
    margin: 0 0 0.65rem 0;
    line-height: 1.25;
}
.ks-arch-card-desc {
    font-size: 0.92rem;
    color: #68756C;
    line-height: 1.6;
    margin: 0 0 1.5rem 0;
}
.ks-arch-illus {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: auto;
    padding-top: 1rem;
}
.ks-arch-arrow {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 38px;
    height: 38px;
    border-radius: 50%;
    background: #FFFFFF;
    border: 1.5px solid #E2E9E1;
    box-shadow: 0 2px 8px rgba(23, 75, 53, 0.06);
    flex-shrink: 0;
    z-index: 3;
}
@media (max-width: 960px) {
    .ks-arch-container {
        flex-direction: column;
        gap: 1.5rem;
    }
    .ks-arch-arrow {
        transform: rotate(90deg);
    }
}

/* 5. FULL-PAGE HERO SECTION */
.ks-hero-card {
    position: relative;
    width: 100% !important;
    min-height: 72vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #FFFFFF !important;
    background: radial-gradient(circle at 10% 20%, #EEF7EF 0%, #FFFFFF 65%) !important;
    border-top: none !important;
    border-left: none !important;
    border-right: none !important;
    border-bottom: 1.5px solid #E2E9E1 !important;
    border-radius: 0 !important;
    padding: 4.5rem 0 !important;
    margin: 0 0 3rem 0 !important;
    box-shadow: 0 4px 20px rgba(23, 75, 53, 0.03) !important;
    overflow: hidden;
}
.ks-hero-inner {
    max-width: 1320px;
    margin: 0 auto;
    padding: 0 3rem;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 4rem;
    width: 100%;
}
.ks-foliage-svg {
    position: absolute;
    top: 0;
    left: 0;
    width: 160px;
    height: 120px;
    pointer-events: none;
    opacity: 0.5;
    z-index: 1;
}
.ks-hero-left {
    position: relative;
    z-index: 2;
    flex: 1 1 540px;
    min-width: 320px;
}
.ks-hero-h1 {
    font-size: 3.6rem !important;
    font-weight: 800 !important;
    color: #174B35 !important;
    line-height: 1.12 !important;
    letter-spacing: -0.03em !important;
    margin: 0 0 1rem 0 !important;
}
.ks-hero-accent-bar {
    width: 72px;
    height: 5px;
    background: #2E7D50;
    border-radius: 3px;
    margin-bottom: 1.5rem;
}
.ks-hero-desc {
    font-size: 1.18rem !important;
    color: #68756C !important;
    line-height: 1.65 !important;
    margin-bottom: 2.2rem !important;
    max-width: 560px;
}
.ks-hero-actions {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 1.2rem;
}
.ks-btn-primary {
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    background: #174B35 !important;
    color: #FFFFFF !important;
    font-weight: 700;
    font-size: 1.05rem;
    padding: 0.95rem 2.2rem;
    border-radius: 999px;
    box-shadow: 0 4px 16px rgba(23, 75, 53, 0.24);
    transition: all 0.15s ease;
    text-decoration: none !important;
}
.ks-btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 22px rgba(23, 75, 53, 0.32);
    background: #133E2B !important;
    color: #FFFFFF !important;
}
.ks-btn-outline {
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    background: #FFFFFF !important;
    color: #174B35 !important;
    border: 1.8px solid #174B35 !important;
    font-weight: 700;
    font-size: 1.05rem;
    padding: 0.92rem 2.1rem;
    border-radius: 999px;
    transition: all 0.15s ease;
    text-decoration: none !important;
}
.ks-btn-outline:hover {
    background: #E7F2E8 !important;
    color: #174B35 !important;
}
.ks-hero-right {
    position: relative;
    z-index: 2;
    flex: 1 1 440px;
    min-width: 300px;
    display: flex;
    justify-content: center;
}
.ks-farmer-frame {
    position: relative;
    max-width: 480px;
    width: 100%;
    border-radius: 32px;
    overflow: hidden;
    box-shadow: 0 20px 48px rgba(23, 75, 53, 0.14);
    border: 5px solid #FFFFFF;
    background: #E7F2E8;
}
.ks-farmer-frame img {
    width: 100%;
    height: auto;
    display: block;
    object-fit: cover;
}

/* 6. 4-PILLAR FEATURE STRIP */
.ks-feature-strip {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    background: #FFFFFF;
    border: 1px solid #E2E9E1;
    border-radius: 20px;
    margin-bottom: 3rem;
    box-shadow: 0 4px 18px rgba(23, 75, 53, 0.03);
}
.ks-feature-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 1.4rem 1rem;
    text-align: center;
    border-right: 1px solid #E2E9E1;
}
.ks-feature-item:last-child {
    border-right: none;
}
.ks-feature-icon {
    margin-bottom: 0.45rem;
}
.ks-feature-title {
    font-size: 0.95rem;
    font-weight: 700;
    color: #174B35;
}

/* 7. CARDS & CONTAINERS */
.ks-card {
    background: #FFFFFF;
    border: 1px solid #E2E9E1;
    border-radius: 18px;
    padding: 1.75rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 2px 14px rgba(23, 75, 53, 0.025);
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}
.ks-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(23, 75, 53, 0.06);
}
.ks-card h3 {
    font-size: 1.15rem;
    font-weight: 700;
    color: #174B35;
    margin-bottom: 0.45rem;
}
.ks-card p {
    font-size: 0.9rem;
    color: #68756C;
    line-height: 1.6;
    margin: 0;
}
.ks-card-icon-box {
    width: 48px;
    height: 48px;
    border-radius: 12px;
    background: #E7F2E8;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 1.15rem;
}

/* 8. FORM WRAPPER */
.ks-form-container {
    background: #FFFFFF;
    border: 1px solid #E2E9E1;
    border-radius: 20px;
    padding: 2.25rem 2.4rem;
    margin-bottom: 2.5rem;
    box-shadow: 0 4px 22px rgba(23, 75, 53, 0.04);
}
.ks-form-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid #E2E9E1;
    padding-bottom: 1.15rem;
    margin-bottom: 1.5rem;
}
.ks-form-title {
    font-size: 1.35rem;
    font-weight: 800;
    color: #174B35;
    display: flex;
    align-items: center;
    gap: 0.55rem;
}

/* 9. INPUTS, BUTTONS & STREAMLIT OVERRIDES */
.stTextInput > div > div,
.stTextArea > div > div,
.stSelectbox > div > div {
    background-color: #FFFFFF !important;
    border: 1.5px solid #E2E9E1 !important;
    border-radius: 10px !important;
    color: #25352D !important;
}
.stTextInput input,
.stTextArea textarea {
    color: #25352D !important;
    background-color: #FFFFFF !important;
}
.stTextInput > div > div:focus-within,
.stTextArea > div > div:focus-within,
.stSelectbox > div > div:focus-within {
    border-color: #2E7D50 !important;
    box-shadow: 0 0 0 2px rgba(46, 125, 80, 0.15) !important;
}
/* Secondary Buttons (Chips, Presets, Actions) */
.stButton > button,
.stButton > button[kind="secondary"],
.stButton > button:not([kind="primary"]) {
    background-color: #FFFFFF !important;
    color: #174B35 !important;
    border: 1.5px solid #E2E9E1 !important;
    border-radius: 999px !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    padding: 0.5rem 1.15rem !important;
    box-shadow: 0 2px 6px rgba(23, 75, 53, 0.04) !important;
    transition: all 0.15s ease !important;
}
.stButton > button:hover,
.stButton > button[kind="secondary"]:hover,
.stButton > button:not([kind="primary"]:hover) {
    background-color: #E7F2E8 !important;
    border-color: #2E7D50 !important;
    color: #174B35 !important;
    transform: translateY(-1px) !important;
}

/* Primary Submit Button */
.stButton > button[kind="primary"],
.stButton > button[data-testid="baseButton-primary"] {
    background-color: #174B35 !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 999px !important;
    font-weight: 700 !important;
    font-size: 1.05rem !important;
    padding: 0.85rem 2rem !important;
    box-shadow: 0 4px 16px rgba(23, 75, 53, 0.25) !important;
    transition: all 0.2s ease !important;
}
.stButton > button[kind="primary"]:hover,
.stButton > button[data-testid="baseButton-primary"]:hover {
    background-color: #133E2B !important;
    color: #FFFFFF !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 22px rgba(23, 75, 53, 0.35) !important;
}
[data-testid="stSidebar"] .stButton > button {
    background-color: #FFFFFF !important;
    color: #174B35 !important;
    border: 1.5px solid #E2E9E1 !important;
    box-shadow: none !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
    background-color: #E7F2E8 !important;
    border-color: #2E7D50 !important;
}

/* 10. DIAGNOSTIC RESULTS & ALERTS */
.ks-cause-box {
    background: #FAFCF9;
    border: 1px solid #E2E9E1;
    border-radius: 12px;
    padding: 1.15rem 1.25rem;
    margin-bottom: 0.85rem;
}
.ks-alert {
    display: flex;
    gap: 1rem;
    padding: 1.25rem 1.4rem;
    border-radius: 14px;
    margin-bottom: 1.4rem;
}
.ks-alert-warn {
    background: #FFFBEB;
    border: 1px solid #FCD34D;
    color: #78600A;
}
.ks-alert-danger {
    background: #FEF2F2;
    border: 1px solid #FCA5A5;
    color: #991B1B;
}

/* Follow-Up Clarification Box */
.ks-followup-card {
    background: #FFFFFF;
    border: 2px solid #2E7D50;
    border-radius: 18px;
    padding: 2rem;
    margin-bottom: 1.75rem;
    box-shadow: 0 6px 22px rgba(46, 125, 80, 0.1);
}

/* Footer */
.ks-footer {
    border-top: 1px solid #E2E9E1;
    padding: 3rem 1rem 1.75rem 1rem;
    margin-top: 4.5rem;
    text-align: center;
    color: #68756C;
}

@media (max-width: 860px) {
    .ks-feature-strip {
        grid-template-columns: repeat(2, 1fr);
    }
    .ks-feature-item {
        border-right: none;
        border-bottom: 1px solid #E2E9E1;
    }
    .ks-hero-h1 {
        font-size: 2.2rem;
    }
    .ks-nav-links {
        display: none;
    }
    .ks-navbar {
        padding: 0.6rem 1rem;
    }
}
</style>
"""

# Force light theme immediately at start of render
st.markdown(CSS_LIGHT_THEME, unsafe_allow_html=True)
st.html("""
<script>
(function() {
    function forceLightTheme() {
        try {
            localStorage.setItem("stActiveTheme", JSON.stringify({
                base: "light",
                primaryColor: "#174B35",
                backgroundColor: "#F7F8F2",
                secondaryBackgroundColor: "#E7F2E8",
                textColor: "#25352D"
            }));
            document.documentElement.style.backgroundColor = "#F7F8F2";
            document.body.style.backgroundColor = "#F7F8F2";
            var stApp = document.querySelector(".stApp");
            if (stApp) stApp.style.backgroundColor = "#F7F8F2";
            var stMain = document.querySelector('[data-testid="stMain"]');
            if (stMain) stMain.style.backgroundColor = "#F7F8F2";
        } catch(e) {}
    }
    function forceFullWidth() {
        try {
            var blocks = document.querySelectorAll('[data-testid="stMainBlockContainer"], .block-container, [data-testid="block-container"]');
            blocks.forEach(function(b) {
                b.style.paddingTop = '0px';
                b.style.paddingLeft = '0px';
                b.style.paddingRight = '0px';
                b.style.maxWidth = '100%';
                b.style.width = '100%';
                b.style.marginLeft = '0px';
                b.style.marginRight = '0px';
            });
            var hdrs = document.querySelectorAll('[data-testid="stHeader"], header');
            hdrs.forEach(function(h) {
                h.style.display = 'none';
                h.style.height = '0px';
            });
        } catch(e) {}
    }
    forceLightTheme();
    forceFullWidth();
    window.addEventListener("load", function() {
        forceLightTheme();
        forceFullWidth();
    });
    setInterval(function() {
        forceLightTheme();
        forceFullWidth();
    }, 400);
})();
</script>
""")

# -----------------------------------------------------------------------------
# Asset & Image Helper
# -----------------------------------------------------------------------------
@st.cache_data
def get_base64_image(image_path: str) -> str:
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return ""

# -----------------------------------------------------------------------------
# Clean SVG Icons (Consistent 24x24 viewBox, stroke-width 2.2)
# -----------------------------------------------------------------------------
def svg_icon(path_data: str, size: int = 20, color: str = "currentColor", sw: str = "2.2") -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" '
        f'viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" '
        f'stroke-linecap="round" stroke-linejoin="round">{path_data}</svg>'
    )

P_LEAF = '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>'
P_SHIELD = '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>'
P_SHIELD_CHECK = '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>'
P_SEARCH = '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>'
P_SEARCH_LEAF = '<circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/><path d="M11 8c-1.5 1.5-1.5 3.5 0 5"/>'
P_CHECK = '<polyline points="20 6 9 17 4 12"/>'
P_ALERT = '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>'
P_PHONE = '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.84.36 1.86.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.95.34 1.97.57 2.81.7A2 2 0 0 1 22 16.92z"/>'
P_QUESTION = '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/>'
P_GLOBE = '<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>'
P_HOME = '<path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>'
P_LAYERS = '<polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>'
P_CHAT = '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>'
P_LANG = '<path d="m5 8 6 6"/><path d="m4 14 6-6 2-3"/><path d="M2 5h12"/><path d="M7 2h1"/><path d="m22 22-5-10-5 10"/><path d="M14 18h6"/>'

ICONS = {
    "leaf_brand": svg_icon(P_LEAF, 26, "#174B35"),
    "leaf_green": svg_icon(P_LEAF, 20, "#2E7D50"),
    "leaf_white": svg_icon(P_LEAF, 18, "#FFFFFF"),
    "circle_icon": svg_icon('<circle cx="12" cy="12" r="9"/>', 16, "#174B35", "2.2"),
    "leaf_pillar": svg_icon(P_LEAF, 28, "#2E7D50"),
    "search_pillar": svg_icon(P_SEARCH_LEAF, 28, "#2E7D50"),
    "shield_pillar": svg_icon(P_SHIELD_CHECK, 28, "#2E7D50"),
    "lang_pillar": svg_icon(P_LANG, 28, "#2E7D50"),
    "home_white": svg_icon(P_HOME, 16, "#FFFFFF"),
    "layers": svg_icon(P_LAYERS, 16, "currentColor"),
    "chat": svg_icon(P_CHAT, 16, "currentColor"),
    "shield": svg_icon(P_SHIELD, 16, "currentColor"),
    "globe": svg_icon(P_GLOBE, 15, "currentColor"),
    "check_green": svg_icon(P_CHECK, 16, "#2E7D50", "2.5"),
    "search": svg_icon(P_SEARCH, 20, "#174B35"),
    "alert": svg_icon(P_ALERT, 20, "currentColor"),
    "phone": svg_icon(P_PHONE, 18, "currentColor"),
    "question": svg_icon(P_QUESTION, 22, "#174B35"),
}

# -----------------------------------------------------------------------------
# API Key & Model Resolution (Strict Priority)
# -----------------------------------------------------------------------------
def get_gemini_api_key(sidebar_input=""):
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

def get_gemini_model():
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
        "language": "English",
    }

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
# Sidebar Configuration
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown(f"""
    <div style="display:flex; align-items:center; gap:0.6rem; margin-bottom:1rem;">
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
        help="Reads automatically from Streamlit Secrets or .env. Override here.",
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
        st.markdown("""
        <div style="background:#FEF2F2; border:1px solid #FCA5A5; padding:0.5rem 0.8rem; border-radius:8px; font-size:0.8rem; color:#991B1B; font-weight:600; margin-bottom:1rem;">
            ⚠️ API Key Needed (.env / Secrets / Input)
        </div>
        """, unsafe_allow_html=True)

    sidebar_language = st.selectbox(
        "Preferred Advisory Language",
        ["English", "Hindi", "Hinglish"],
        index=["English", "Hindi", "Hinglish"].index(st.session_state.original_form.get("language", "English")),
        key="global_lang_select",
    )
    st.session_state.original_form["language"] = sidebar_language

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
            "language": sidebar_language,
        }
        st.rerun()

# -----------------------------------------------------------------------------
# 1. Navigation Bar & Multi-Tab Routing
# -----------------------------------------------------------------------------
st.markdown(f"""
<div class="ks-navbar">
    <div class="ks-navbar-inner">
        <div class="ks-nav-brand">
            <div>{ICONS['leaf_brand']}</div>
            <div>
                <div class="ks-nav-brand-title">KisanSaathi</div>
                <div class="ks-nav-brand-sub">AI Crop Advisory Assistant</div>
            </div>
        </div>
        <div style="display:flex; align-items:center; gap:0.75rem;">
            <span class="ks-lang-pill">{ICONS['globe']} {st.session_state.original_form['language']}</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

tab_home, tab_how, tab_ask, tab_safety, tab_eval = st.tabs([
    "🏠 Home",
    "🥞 How It Works",
    "🌿 Ask AI",
    "🛡️ Safety",
    "📊 Evaluation",
])
with tab_ask:
    # -----------------------------------------------------------------------------
    # 5. Crop Diagnostic Intake Form (#ask-ai)
    # -----------------------------------------------------------------------------
    st.markdown('<div id="ask-ai"></div>', unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown(f"""
        <div class="ks-form-header">
            <div class="ks-form-title">
                {ICONS['leaf_brand']}
                <span>Crop Diagnostic Center</span>
            </div>
            <span style="font-size:0.78rem; font-weight:700; color:#2E7D50; background:#E7F2E8; padding:0.35rem 0.9rem; border-radius:999px;">
                AI Symptom Intake
            </span>
        </div>
        """, unsafe_allow_html=True)

        # Benchmark scenario quick-fill buttons
        st.caption("🧪 **Quick-Fill Benchmark Scenarios:**")
        p1, p2, p3, p4, p5 = st.columns([1, 1, 1, 1, 0.85])
        with p1:
            if st.button("🍅 Tomato Curl (UP)", use_container_width=True):
                set_preset("Tomato", "Uttar Pradesh", "Flowering", "Slowly", "English", "Tomato leaves have yellow spots and curling edges.")
                st.rerun()
        with p2:
            if st.button("🌾 Rice Spot (WB)", use_container_width=True):
                set_preset("Rice", "West Bengal", "Vegetative", "Slowly", "English", "Rice plants have brown spots on the leaves.")
                st.rerun()
        with p3:
            if st.button("🌱 Wheat Yellow (PB)", use_container_width=True):
                set_preset("Wheat", "Punjab", "Not sure", "Rapidly", "Hindi", "गेहूं की पत्तियां नोक से पीली पड़ रही हैं और समस्या तेजी से बढ़ रही है।")
                st.rerun()
        with p4:
            if st.button("🥔 Potato Stunt (UP)", use_container_width=True):
                set_preset("Potato", "Uttar Pradesh", "Vegetative", "Not sure", "Hinglish", "Aloo ke paudhe me curling leaves dikh rahi hain aur growth ruk gayi hai.")
                st.rerun()
        with p5:
            if st.button("🔄 Reset", use_container_width=True):
                st.session_state.result = None
                st.session_state.follow_up_history = []
                st.session_state.follow_up_answer = ""
                st.session_state.original_form = {
                    "crop": "",
                    "region": "",
                    "stage": "Not sure",
                    "query": "",
                    "spread": "Not sure",
                    "language": st.session_state.original_form.get("language", "English"),
                }
                st.rerun()

        st.markdown("<div style='height: 0.75rem;'></div>", unsafe_allow_html=True)
        OF = st.session_state.original_form

        # Row 1: Crop Name & Region
        r1_c1, r1_c2 = st.columns(2, gap="medium")
        with r1_c1:
            crop = st.text_input("Crop Name", value=OF["crop"], placeholder="e.g. Tomato / Rice / गेहूं")
        with r1_c2:
            region = st.text_input("Region / State", value=OF["region"], placeholder="e.g. Uttar Pradesh, Punjab")

        # Row 2: Growth Stage, Problem Spreading, Advisory Language
        r2_c1, r2_c2, r2_c3 = st.columns(3, gap="medium")
        with r2_c1:
            stage_opts = ["Not sure", "Seedling", "Vegetative", "Flowering", "Fruiting", "Harvest"]
            current_stage = OF["stage"]
            stage = st.selectbox("Growth Stage", stage_opts, index=stage_opts.index(current_stage) if current_stage in stage_opts else 0)
        with r2_c2:
            spread_opts = ["Not sure", "Not spreading", "Slowly", "Rapidly"]
            current_spread = OF["spread"]
            spread = st.selectbox("Problem Spreading?", spread_opts, index=spread_opts.index(current_spread) if current_spread in spread_opts else 0)
        with r2_c3:
            lang_opts = ["English", "Hindi", "Hinglish"]
            current_lang = OF["language"]
            form_lang = st.selectbox("Advisory Language", lang_opts, index=lang_opts.index(current_lang) if current_lang in lang_opts else 0)

        # Row 3: Symptoms Observed (Full Width)
        query = st.text_area(
            "Describe Symptoms Observed",
            value=OF["query"],
            placeholder="Describe color change, leaf curling, spots, insect presence, etc.",
            height=110,
        )

        OF["language"] = form_lang

        st.markdown("<div style='height: 0.75rem;'></div>", unsafe_allow_html=True)
        submit = st.button("🌿 Get Crop Advice", type="primary", use_container_width=True)

    # -----------------------------------------------------------------------------
    # 6. Pipeline Execution
    # -----------------------------------------------------------------------------
    if submit:
        if not query.strip():
            st.warning("Please describe the crop symptoms before proceeding.")
            st.stop()

        try:
            st.session_state.original_form = {
                "crop": crop.strip(),
                "region": region.strip(),
                "stage": stage,
                "query": query.strip(),
                "spread": spread,
                "language": form_lang,
            }
            st.session_state.follow_up_history = []
            st.session_state.follow_up_answer = ""

            rk = get_gemini_api_key(api_key_input)
            rm = get_gemini_model()
            if not rk:
                st.error("⚠️ GEMINI_API_KEY is missing. Add it to Streamlit Secrets, .env, or the sidebar.")
                st.stop()

            notes = load_reference_notes()
            pipeline = KisanSaathiPipeline(notes, api_key=rk, model=rm)
            with st.status("🌱 Running Grounded Agronomic Analysis...", expanded=True) as status:
                step_text = st.empty()
                def handle_step(msg):
                    step_text.write(f"⏳ {msg}")
                o = st.session_state.original_form
                result = pipeline.run(
                    query=o["query"],
                    crop=o["crop"],
                    region=o["region"],
                    stage=o["stage"],
                    spread=o["spread"],
                    language=o["language"],
                    follow_up_answer="",
                    previous_extraction=None,
                    on_step=handle_step,
                )
                status.update(label="✅ Analysis Complete!", state="complete", expanded=False)
            st.session_state.result = result
        except Exception as exc:
            st.error(f"Could not complete the analysis: {exc}")
            st.info("Check GEMINI_API_KEY configuration and connectivity.")

    # -----------------------------------------------------------------------------
    # 7. Diagnostic Assessment Results Display
    # -----------------------------------------------------------------------------
    if st.session_state.result:
        result = st.session_state.result
        extraction = result["extraction"]
        diagnosis = result["diagnosis"]
        advisory = result["advisory"]
        follow_up_q = extraction.get("follow_up_question", "").strip()

        st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)
        st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:1.5rem;">
            <div>
                <h2 style="font-size:1.85rem; font-weight:800; color:#174B35; margin:0;">
                    KisanSaathi Assessment Results
                </h2>
                <p style="color:#68756C; margin:0.25rem 0 0 0; font-size:0.95rem;">
                    Grounded diagnostic evaluation for <b>{extraction.get('crop', 'Crop')}</b> in <b>{extraction.get('broad_region', 'Region')}</b>
                </p>
            </div>
            <span style="background:#E7F2E8; color:#0B5A2A; padding:0.4rem 0.95rem; border-radius:999px; font-weight:700; font-size:0.8rem;">
                {ICONS['check_green']} Verified Advisory
            </span>
        </div>
        """, unsafe_allow_html=True)

        # Context badge strip
        st.markdown(f"""
        <div class="ks-card" style="padding:1.15rem 1.5rem; background:#FFFFFF; margin-bottom:1.25rem;">
            <div style="display:flex; flex-wrap:wrap; gap:1.4rem; align-items:center;">
                <div><span style="font-size:0.75rem; color:#68756C; font-weight:700; text-transform:uppercase;">Crop:</span> <b>{extraction.get('crop', 'Unknown')}</b></div>
                <div><span style="font-size:0.75rem; color:#68756C; font-weight:700; text-transform:uppercase;">Region:</span> <b>{extraction.get('broad_region', 'Unknown')}</b></div>
                <div><span style="font-size:0.75rem; color:#68756C; font-weight:700; text-transform:uppercase;">Stage:</span> <b>{extraction.get('growth_stage', 'Unknown')}</b></div>
                <div><span style="font-size:0.75rem; color:#68756C; font-weight:700; text-transform:uppercase;">Spread:</span> <b>{extraction.get('spread', 'Unknown')}</b></div>
                <div><span style="font-size:0.75rem; color:#68756C; font-weight:700; text-transform:uppercase;">Symptoms:</span> <b>{', '.join(extraction.get('symptoms', [])) or 'Observed'}</b></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Possible causes card
        causes = diagnosis.get("possible_causes", [])
        if causes:
            causes_html = "".join([f"""
            <div class="ks-cause-box">
                <div style="font-size:1.05rem; font-weight:700; color:#174B35; margin-bottom:0.35rem;">{c.get('name', 'Possible cause')}</div>
                <div style="font-size:0.92rem; color:#68756C; line-height:1.55;">{c.get('reason', '')}</div>
            </div>
            """ for c in causes])
        else:
            causes_html = "<p style='color:#68756C; font-size:0.9rem;'>No definitive match in reference notes. Continued observation recommended.</p>"

        st.markdown(f"""
        <div class="ks-card">
            <h3 style="font-size:1.25rem; font-weight:800; color:#174B35; margin-bottom:0.75rem;">
                Possible Agronomic Causes
            </h3>
            <div style="background:#F0FDF4; border-left:4px solid #2E7D50; padding:0.75rem 1rem; border-radius:0 8px 8px 0; margin-bottom:1.25rem; font-size:0.85rem; color:#166534;">
                <b>Grounded Literature Disclaimer:</b> The following are potential agronomic causes derived from symptom matching with ICAR reference materials. They represent preliminary assessments rather than confirmed laboratory diagnoses.
            </div>
            {causes_html}
        </div>
        """, unsafe_allow_html=True)

        # Advisory & Field Checklist in 2 equal columns
        res_col1, res_col2 = st.columns(2, gap="medium")
        with res_col1:
            st.markdown(f"""
            <div class="ks-card" style="height:100%;">
                <h3 style="font-size:1.2rem; font-weight:800; color:#174B35; margin-bottom:0.75rem;">Agronomic Advisory</h3>
                <div style="font-size:0.92rem; line-height:1.6; color:#25352D;">
                    {advisory.get('advice', 'No specific advisory available.')}
                </div>
            </div>
            """, unsafe_allow_html=True)

        with res_col2:
            next_steps = advisory.get("next_steps", [])
            if next_steps:
                steps_html = "".join([f"""
                <div style="display:flex; align-items:flex-start; gap:0.6rem; margin-bottom:0.75rem; font-size:0.88rem; color:#25352D;">
                    <div style="margin-top:2px;">{ICONS['check_green']}</div>
                    <div>{item}</div>
                </div>
                """ for item in next_steps])
            else:
                steps_html = "<p style='color:#68756C;'>No specific checklist steps provided.</p>"

            st.markdown(f"""
            <div class="ks-card" style="height:100%;">
                <h3 style="font-size:1.2rem; font-weight:800; color:#174B35; margin-bottom:0.75rem;">Recommended Field Checklist</h3>
                {steps_html}
            </div>
            """, unsafe_allow_html=True)

        # Safety Warning Banner
        st.markdown(f"""
        <div class="ks-alert ks-alert-warn">
            <div style="flex-shrink:0; padding-top:2px;">{ICONS['shield']}</div>
            <div>
                <h4 style="margin:0 0 0.35rem 0; font-size:0.98rem; font-weight:700;">Strict Zero Chemical Dosage Policy</h4>
                <p style="margin:0; font-size:0.88rem; line-height:1.5;">KisanSaathi does <b>not</b> provide chemical pesticide dosages. Always consult qualified local agronomists or your nearest Krishi Vigyan Kendra before applying synthetic chemicals.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

        if advisory.get("escalate", True):
            st.markdown(f"""
            <div class="ks-alert ks-alert-danger">
                <div style="flex-shrink:0; padding-top:2px;">{ICONS['alert']}</div>
                <div>
                    <h4 style="margin:0 0 0.35rem 0; font-size:0.98rem; font-weight:700;">Extension Officer / KVK Escalation Recommended</h4>
                    <p style="margin:0; font-size:0.88rem; line-height:1.5;"><b>Reason:</b> {advisory.get('escalation_reason', 'Physical on-ground inspection required.')}</p>
                    <div style="margin-top:0.6rem; font-weight:600; font-size:0.85rem; display:flex; align-items:center; gap:0.4rem;">
                        {ICONS['phone']} National Kisan Call Centre: <b>1800-180-1551</b> (Toll-Free, 6 AM - 10 PM)
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Follow-Up Question Card
        if follow_up_q:
            with st.container(border=True):
                st.markdown(f"""
                <div style="display:flex; align-items:center; gap:0.6rem; color:#2E7D50; margin-bottom:0.6rem; font-weight:700; text-transform:uppercase; font-size:0.82rem;">
                    {ICONS['question']} Follow-Up Clarification Needed
                </div>
                <div style="font-size:1.25rem; font-weight:800; color:#174B35; margin-bottom:0.75rem; line-height:1.4;">
                    {follow_up_q}
                </div>
                """, unsafe_allow_html=True)

                if extraction.get("missing_information"):
                    st.caption(f"Pending Information: {', '.join(extraction['missing_information'])}")

                with st.form("follow_up_form"):
                    follow_up_answer = st.text_input(
                        "Your Clarification:",
                        placeholder="e.g. Flowering stage / Around 20% of plants are affected",
                        key="follow_up_text_input",
                    )
                    submit_follow_up = st.form_submit_button("Submit Clarification & Update Diagnosis")

                if submit_follow_up:
                    if not follow_up_answer.strip():
                        st.warning("Please type your answer before submitting.")
                    else:
                        submitted_ans = follow_up_answer.strip()
                        st.session_state["follow_up_answer"] = submitted_ans
                        st.session_state.follow_up_history.append({"q": follow_up_q, "a": submitted_ans})
                        try:
                            rk = get_gemini_api_key(api_key_input)
                            rm = get_gemini_model()
                            if not rk:
                                st.error("⚠️ GEMINI_API_KEY is missing.")
                                st.stop()

                            notes = load_reference_notes()
                            pipeline = KisanSaathiPipeline(notes, api_key=rk, model=rm)
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
                                    on_step=handle_step,
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

        if st.session_state.follow_up_history:
            with st.expander("📝 Multi-Turn Conversation History", expanded=False):
                for idx, item in enumerate(st.session_state.follow_up_history, 1):
                    st.markdown(f"**Turn {idx}:** {item['q']}")
                    st.markdown(f"*Farmer's Answer:* `{item['a']}`")
                    st.markdown("---")

        with st.expander("🔍 View Structured Pipeline Output (JSON)", expanded=bool(st.session_state.get("follow_up_answer"))):
            st.json(result)

with tab_home:
    # -----------------------------------------------------------------------------
    # 2. Hero Section (Clean 2-Column, No Overlapping Logos, Sharp Farmer Photo)
    # -----------------------------------------------------------------------------
    farmer_b64 = get_base64_image("assets/farmer_portrait_hd.jpg") or get_base64_image("assets/farmer_clean_hd.jpg")

    st.markdown(f"""
    <div class="ks-hero-card">
        <svg class="ks-foliage-svg" viewBox="0 0 160 120" fill="none" xmlns="http://www.w3.org/2000/svg" style="opacity:0.4;">
            <path d="M-10 -10 C 20 20, 60 40, 120 45" stroke="#2E7D50" stroke-width="2.5" stroke-linecap="round"/>
            <path d="M25 24 C 15 15, 20 0, 35 5 C 45 10, 40 25, 25 24 Z" fill="#2E7D50" opacity="0.8"/>
            <path d="M55 35 C 50 20, 65 10, 78 18 C 85 28, 70 40, 55 35 Z" fill="#3B925E" opacity="0.85"/>
            <path d="M85 41 C 85 25, 102 22, 110 32 C 115 42, 98 50, 85 41 Z" fill="#2E7D50" opacity="0.75"/>
            <path d="M40 32 C 30 45, 15 45, 18 32 C 22 22, 35 25, 40 32 Z" fill="#256C42" opacity="0.7"/>
            <path d="M72 40 C 65 55, 50 56, 52 42 C 55 32, 68 32, 72 40 Z" fill="#2E7D50" opacity="0.8"/>
            <path d="M105 45 C 102 60, 88 62, 88 48 C 90 38, 102 38, 105 45 Z" fill="#3B925E" opacity="0.75"/>
        </svg>
        <div class="ks-hero-inner">
            <div class="ks-hero-left">
                <h1 class="ks-hero-h1">
                    Better Crop Decisions.<br>
                    <span style="color:#174B35;">Better Farming.</span>
                </h1>
                <div class="ks-hero-accent-bar"></div>
                <p class="ks-hero-desc">
                    Describe your crop problem in your preferred language and receive clear, cautious guidance to help you take the next step.
                </p>
                <div class="ks-hero-actions">
                    <a href="#ask-ai" class="ks-btn-primary">
                        {ICONS['leaf_white']} Get Crop Advice &rarr;
                    </a>
                    <a href="#how-it-works" class="ks-btn-outline">
                        {ICONS['circle_icon']} How It Works
                    </a>
                </div>
            </div>
            <div class="ks-hero-right">
                <div class="ks-farmer-frame">
                    <img src="data:image/jpeg;base64,{farmer_b64}" alt="Indian farmer using smartphone in green field" />
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # -----------------------------------------------------------------------------
    # 3. 4-Pillar Feature Strip (Matching Reference Mockup)
    # -----------------------------------------------------------------------------
    st.markdown(f"""
    <div class="ks-feature-strip">
        <div class="ks-feature-item">
            <div class="ks-feature-icon">{ICONS['leaf_pillar']}</div>
            <div class="ks-feature-title">Crop Guidance</div>
        </div>
        <div class="ks-feature-item">
            <div class="ks-feature-icon">{ICONS['search_pillar']}</div>
            <div class="ks-feature-title">Problem Identification</div>
        </div>
        <div class="ks-feature-item">
            <div class="ks-feature-icon">{ICONS['shield_pillar']}</div>
            <div class="ks-feature-title">Safe Recommendations</div>
        </div>
        <div class="ks-feature-item">
            <div class="ks-feature-icon">{ICONS['lang_pillar']}</div>
            <div class="ks-feature-title">Multi-language Support</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab_how:
    # -----------------------------------------------------------------------------
    # 4. How It Works Section (Exact Reference Mockup Layout)
    # -----------------------------------------------------------------------------
    st.markdown("""
    <div class="ks-how-it-works-page">
        <!-- Floating Foliage Background SVGs -->
        <svg class="ks-bg-foliage-left" viewBox="0 0 140 160" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M-10 20 C 30 40, 70 80, 100 130" stroke="#7BA887" stroke-width="2.5" stroke-linecap="round" opacity="0.6"/>
            <path d="M28 35 C 10 25, 12 5, 28 8 C 42 12, 45 28, 28 35 Z" fill="#7BA887" opacity="0.55"/>
            <path d="M60 55 C 50 40, 62 25, 78 30 C 88 40, 80 58, 60 55 Z" fill="#6B9978" opacity="0.6"/>
            <path d="M75 90 C 65 72, 85 62, 98 72 C 102 85, 90 100, 75 90 Z" fill="#7BA887" opacity="0.55"/>
            <path d="M42 65 C 28 75, 15 68, 20 54 C 26 42, 42 48, 42 65 Z" fill="#6B9978" opacity="0.5"/>
            <path d="M78 120 C 62 130, 52 118, 58 104 C 64 92, 82 98, 78 120 Z" fill="#7BA887" opacity="0.55"/>
        </svg>
        <svg class="ks-bg-foliage-right" viewBox="0 0 140 160" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M150 20 C 110 40, 70 80, 40 130" stroke="#7BA887" stroke-width="2.5" stroke-linecap="round" opacity="0.6"/>
            <path d="M112 35 C 130 25, 128 5, 112 8 C 98 12, 95 28, 112 35 Z" fill="#7BA887" opacity="0.55"/>
            <path d="M80 55 C 90 40, 78 25, 62 30 C 52 40, 60 58, 80 55 Z" fill="#6B9978" opacity="0.6"/>
            <path d="M65 90 C 75 72, 55 62, 42 72 C 38 85, 50 100, 65 90 Z" fill="#7BA887" opacity="0.55"/>
            <path d="M98 65 C 112 75, 125 68, 120 54 C 114 42, 98 48, 98 65 Z" fill="#6B9978" opacity="0.5"/>
            <path d="M62 120 C 78 130, 88 118, 82 104 C 76 92, 58 98, 62 120 Z" fill="#7BA887" opacity="0.55"/>
        </svg>

        <!-- Section Header -->
        <div style="text-align:center; max-width:760px; margin:0 auto 3.2rem auto; position:relative; z-index:2;">
            <div style="display:inline-block; margin-bottom:0.85rem;">
                <span style="font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:0.08em; color:#2E7D50; background:#E7F2E8; padding:0.4rem 1.15rem; border-radius:999px;">
                    SYSTEM ARCHITECTURE
                </span>
            </div>
            <h1 style="font-size:2.8rem; font-weight:800; color:#174B35; margin:0 0 0.85rem 0; letter-spacing:-0.03em;">
                How KisanSaathi Works
            </h1>
            <p style="color:#68756C; font-size:1.08rem; line-height:1.6; margin:0;">
                A grounded three-stage prompt workflow ensuring verified agronomic advice with zero chemical dosage hallucination.
            </p>
        </div>

        <!-- 3 Cards with Connecting Arrows -->
        <div class="ks-arch-container">
            <!-- Card 1 -->
            <div class="ks-arch-card">
                <div>
                    <div class="ks-arch-icon-box">
                        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#174B35" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                            <circle cx="11" cy="11" r="8"></circle>
                            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                        </svg>
                    </div>
                    <h3 class="ks-arch-card-title">1. Multi-Lingual Extraction</h3>
                    <p class="ks-arch-card-desc">
                        Understands farmer queries in English, Hindi, and Hinglish. Extracts crop, region, phenological stage, symptoms, and spread rate.
                    </p>
                </div>
                <!-- Illustration 1: Document with speech bubbles -->
                <div class="ks-arch-illus">
                    <svg width="230" height="135" viewBox="0 0 230 135" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <rect x="80" y="24" width="70" height="96" rx="8" fill="#FFFFFF" stroke="#2E7D50" stroke-width="2.2"/>
                        <line x1="94" y1="44" x2="136" y2="44" stroke="#2E7D50" stroke-width="2.2" stroke-linecap="round"/>
                        <line x1="94" y1="58" x2="136" y2="58" stroke="#2E7D50" stroke-width="2.2" stroke-linecap="round"/>
                        <line x1="94" y1="72" x2="124" y2="72" stroke="#2E7D50" stroke-width="2.2" stroke-linecap="round"/>
                        <line x1="94" y1="86" x2="136" y2="86" stroke="#2E7D50" stroke-width="2.2" stroke-linecap="round"/>
                        <line x1="94" y1="100" x2="116" y2="100" stroke="#2E7D50" stroke-width="2.2" stroke-linecap="round"/>
                        <!-- Bubble: Hindi -->
                        <g>
                            <rect x="18" y="20" width="56" height="28" rx="14" fill="#E7F2E8" stroke="#2E7D50" stroke-width="1.5"/>
                            <text x="46" y="38" font-family="Inter, sans-serif" font-size="11.5" font-weight="700" fill="#174B35" text-anchor="middle">Hindi</text>
                            <path d="M52 47 L60 56 L64 47 Z" fill="#E7F2E8" stroke="#2E7D50" stroke-width="1.5"/>
                            <line x1="53" y1="47" x2="63" y2="47" stroke="#E7F2E8" stroke-width="2"/>
                        </g>
                        <!-- Bubble: English -->
                        <g>
                            <rect x="146" y="14" width="66" height="28" rx="14" fill="#E7F2E8" stroke="#2E7D50" stroke-width="1.5"/>
                            <text x="179" y="32" font-family="Inter, sans-serif" font-size="11.5" font-weight="700" fill="#174B35" text-anchor="middle">English</text>
                            <path d="M156 41 L148 50 L162 43 Z" fill="#E7F2E8" stroke="#2E7D50" stroke-width="1.5"/>
                            <line x1="154" y1="41" x2="161" y2="41" stroke="#E7F2E8" stroke-width="2"/>
                        </g>
                        <!-- Bubble: Hinglish -->
                        <g>
                            <rect x="148" y="76" width="68" height="28" rx="14" fill="#E7F2E8" stroke="#2E7D50" stroke-width="1.5"/>
                            <text x="182" y="94" font-family="Inter, sans-serif" font-size="11.5" font-weight="700" fill="#174B35" text-anchor="middle">Hinglish</text>
                            <path d="M158 77 L148 70 L160 76 Z" fill="#E7F2E8" stroke="#2E7D50" stroke-width="1.5"/>
                            <line x1="156" y1="77" x2="161" y2="77" stroke="#E7F2E8" stroke-width="2"/>
                        </g>
                    </svg>
                </div>
            </div>

            <!-- Arrow 1 -> 2 -->
            <div class="ks-arch-arrow">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#2E7D50" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="5" y1="12" x2="19" y2="12"></line>
                    <polyline points="12 5 19 12 12 19"></polyline>
                </svg>
            </div>

            <!-- Card 2 -->
            <div class="ks-arch-card">
                <div>
                    <div class="ks-arch-icon-box">
                        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#174B35" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                            <polygon points="12 2 2 7 12 12 22 7 12 2"></polygon>
                            <polyline points="2 17 12 22 22 17"></polyline>
                            <polyline points="2 12 12 17 22 12"></polyline>
                        </svg>
                    </div>
                    <h3 class="ks-arch-card-title">2. Grounded TF-IDF Retrieval</h3>
                    <p class="ks-arch-card-desc">
                        Matches symptom profiles against ICAR agronomic reference materials. Every diagnosis is grounded in verified literature citations.
                    </p>
                </div>
                <!-- Illustration 2: 3D ICAR Book -->
                <div class="ks-arch-illus">
                    <svg width="230" height="135" viewBox="0 0 230 135" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <ellipse cx="115" cy="116" rx="78" ry="12" fill="#E2E9E1"/>
                        <path d="M52 84 L114 106 L178 84 L178 72 L114 94 L52 72 Z" fill="#D6E8D8"/>
                        <path d="M52 78 L114 100 L178 78 L178 68 L114 90 L52 68 Z" fill="#F7F8F2" stroke="#D6E8D8"/>
                        <path d="M50 72 L114 94 L180 72 L116 50 Z" fill="#2E7D50"/>
                        <path d="M50 70 L114 92 L180 70 L116 48 Z" fill="#3B925E"/>
                        <g transform="rotate(18, 114, 68) skewX(-24)">
                            <text x="86" y="73" font-family="Inter, sans-serif" font-size="14.5" font-weight="800" fill="#FFFFFF" letter-spacing="2">ICAR</text>
                        </g>
                        <path d="M112 92 L112 112 L117 107 L122 112 L122 92 Z" fill="#D97706"/>
                    </svg>
                </div>
            </div>

            <!-- Arrow 2 -> 3 -->
            <div class="ks-arch-arrow">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#2E7D50" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="5" y1="12" x2="19" y2="12"></line>
                    <polyline points="12 5 19 12 12 19"></polyline>
                </svg>
            </div>

            <!-- Card 3 -->
            <div class="ks-arch-card">
                <div>
                    <div class="ks-arch-icon-box">
                        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#174B35" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                            <polyline points="9 12 11 14 15 10"></polyline>
                        </svg>
                    </div>
                    <h3 class="ks-arch-card-title">3. Safe Advisory & Escalation</h3>
                    <p class="ks-arch-card-desc">
                        Generates cultural management checklists, asks follow-up questions for missing details, and escalates to KVK experts when needed.
                    </p>
                </div>
                <!-- Illustration 3: Clipboard Checklist & Leaf -->
                <div class="ks-arch-illus">
                    <svg width="230" height="135" viewBox="0 0 230 135" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <rect x="80" y="22" width="70" height="96" rx="8" fill="#FFFFFF" stroke="#2E7D50" stroke-width="2.2"/>
                        <rect x="96" y="14" width="38" height="16" rx="4" fill="#174B35"/>
                        <rect x="104" y="18" width="22" height="6" rx="2" fill="#E7F2E8"/>
                        <!-- Checkmark 1 -->
                        <path d="M90 48 L95 53 L104 43" stroke="#2E7D50" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
                        <line x1="110" y1="48" x2="138" y2="48" stroke="#2E7D50" stroke-width="2" stroke-linecap="round"/>
                        <!-- Checkmark 2 -->
                        <path d="M90 66 L95 71 L104 61" stroke="#2E7D50" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
                        <line x1="110" y1="66" x2="138" y2="66" stroke="#2E7D50" stroke-width="2" stroke-linecap="round"/>
                        <!-- Checkmark 3 -->
                        <path d="M90 84 L95 89 L104 79" stroke="#2E7D50" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
                        <line x1="110" y1="84" x2="138" y2="84" stroke="#2E7D50" stroke-width="2" stroke-linecap="round"/>
                        <!-- Dot line 4 -->
                        <circle cx="95" cy="100" r="3.5" fill="#2E7D50"/>
                        <line x1="110" y1="100" x2="130" y2="100" stroke="#2E7D50" stroke-width="2" stroke-linecap="round"/>
                        <!-- Leaf Sprout on Right -->
                        <path d="M156 108 C 154 92, 166 84, 172 75 C 174 86, 165 98, 160 108" fill="#3B925E"/>
                        <path d="M158 95 C 168 90, 180 90, 184 97 C 178 101, 165 101, 158 95" fill="#2E7D50"/>
                        <path d="M158 102 C 148 98, 140 102, 138 108 C 144 110, 153 106, 158 102" fill="#3B925E"/>
                    </svg>
                </div>
            </div>
        </div>

        <!-- Bottom Landscape Wave -->
        <div style="width:100%; overflow:hidden; line-height:0; margin-top:4rem;">
            <svg viewBox="0 0 1440 90" fill="none" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto;">
                <path d="M0 45 C 360 85, 720 15, 1080 65 C 1260 85, 1380 60, 1440 50 L 1440 90 L 0 90 Z" fill="#DCEBDE" opacity="0.6"/>
                <path d="M0 65 C 400 95, 800 35, 1200 75 L 1440 60 L 1440 90 L 0 90 Z" fill="#C7DFC8" opacity="0.75"/>
            </svg>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab_safety:
    # -----------------------------------------------------------------------------
    # 8. Safety Architecture Section (#safety)
    # -----------------------------------------------------------------------------
    st.markdown("""
    <div id="safety" style="margin-top:4rem; margin-bottom:3rem;">
        <div style="text-align:center; max-width:680px; margin:0 auto 2rem auto;">
            <span style="font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:0.08em; color:#2E7D50; background:#E7F2E8; padding:0.3rem 0.85rem; border-radius:999px; display:inline-block; margin-bottom:0.6rem;">
                Safety Architecture
            </span>
            <h2 style="font-size:2rem; font-weight:800; color:#174B35; margin-bottom:0.5rem;">
                Safety-First Agricultural Guardrails
            </h2>
            <p style="color:#68756C; font-size:1rem; line-height:1.6;">
                Protecting crop health, soil vitality, and farmer safety through strict computational guardrails.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    saf_col1, saf_col2, saf_col3 = st.columns(3)
    with saf_col1:
        st.markdown(f"""
        <div class="ks-card">
            <div class="ks-card-icon-box">{ICONS['shield_pillar']}</div>
            <h3>Zero Chemical Dosage</h3>
            <p>Never computes or prescribes synthetic pesticide spraying doses, preventing crop phytotoxicity and pollinator poisoning.</p>
        </div>
        """, unsafe_allow_html=True)

    with saf_col2:
        st.markdown(f"""
        <div class="ks-card">
            <div class="ks-card-icon-box">{ICONS['leaf_brand']}</div>
            <h3>Evidence Grounding</h3>
            <p>All possible causes are grounded in ICAR and state university agronomy reference manuals, eliminating ungrounded speculation.</p>
        </div>
        """, unsafe_allow_html=True)

    with saf_col3:
        st.markdown(f"""
        <div class="ks-card">
            <div class="ks-card-icon-box">{ICONS['search']}</div>
            <h3>Human-In-The-Loop</h3>
            <p>Uncertain symptoms or rapidly spreading plots automatically trigger escalation recommendations to local extension officers.</p>
        </div>
        """, unsafe_allow_html=True)

with tab_eval:
    # -----------------------------------------------------------------------------
    # 9. Evaluation Benchmark Summary
    # -----------------------------------------------------------------------------
    st.markdown("""
    <div class="ks-card" style="margin-top:1rem;">
        <div style="text-align:center; margin-bottom:1.5rem;">
            <h3 style="font-size:1.45rem; font-weight:800; color:#174B35; margin-bottom:0.35rem;">
                Empirical Benchmark Verification
            </h3>
            <p style="color:#68756C; font-size:0.9rem; margin:0;">
                Evaluated across 12 distinct synthetic field scenarios with zero failures.
            </p>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(170px, 1fr)); gap:1rem; text-align:center;">
            <div style="padding:1.1rem; background:#F7F8F2; border-radius:12px; border:1px solid #E2E9E1;">
                <div style="font-size:1.9rem; font-weight:800; color:#174B35; line-height:1;">12 / 12</div>
                <div style="font-size:0.8rem; font-weight:600; color:#68756C; margin-top:0.35rem;">Scenarios Evaluated</div>
            </div>
            <div style="padding:1.1rem; background:#F0FDF4; border-radius:12px; border:1px solid #BBF7D0;">
                <div style="font-size:1.9rem; font-weight:800; color:#15803D; line-height:1;">100%</div>
                <div style="font-size:0.8rem; font-weight:600; color:#166534; margin-top:0.35rem;">Pass Rate</div>
            </div>
            <div style="padding:1.1rem; background:#FEF3C7; border-radius:12px; border:1px solid #FDE68A;">
                <div style="font-size:1.9rem; font-weight:800; color:#B45309; line-height:1;">0</div>
                <div style="font-size:0.8rem; font-weight:600; color:#92400E; margin-top:0.35rem;">Dosages Prescribed</div>
            </div>
            <div style="padding:1.1rem; background:#F7F8F2; border-radius:12px; border:1px solid #E2E9E1;">
                <div style="font-size:1.9rem; font-weight:800; color:#2E7D50; line-height:1;">3</div>
                <div style="font-size:0.8rem; font-weight:600; color:#68756C; margin-top:0.35rem;">Languages Supported</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    csv_path = "evaluation_results.csv"
    if os.path.exists(csv_path):
        with st.expander("📋 View All 12 Test Cases (evaluation_results.csv)", expanded=False):
            try:
                with open(csv_path, encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    for r in reader:
                        st.markdown(f"**{r.get('Test ID', '')}:** {r.get('Input', '')[:100]}... — **Status:** `{r.get('Pass/Fail', '')}`")
                        st.caption(f"Reason: {r.get('Reason', '')}")
                        st.markdown("---")
            except Exception as e:
                st.caption(f"Could not read CSV: {e}")

# -----------------------------------------------------------------------------
# 10. Footer (Clean, High-Quality Light Theme)
# -----------------------------------------------------------------------------
st.markdown(f"""
<div class="ks-footer">
    <div style="display:flex; align-items:center; justify-content:center; gap:0.5rem; font-size:1.3rem; font-weight:800; color:#174B35; margin-bottom:0.75rem;">
        {ICONS['leaf_brand']} KisanSaathi
    </div>
    <div style="display:flex; justify-content:center; gap:1.8rem; margin-bottom:1rem; font-weight:600; font-size:0.88rem;">
        <a href="#home">Home</a>
        <a href="#how-it-works">How It Works</a>
        <a href="#ask-ai">Ask AI</a>
        <a href="#safety">Safety Guardrails</a>
    </div>
    <div style="max-width:720px; margin:0 auto 1rem auto; font-size:0.8rem; line-height:1.6; color:#68756C;">
        <b>Agricultural Advisory Notice:</b> KisanSaathi is an agronomic artificial intelligence prototype developed for preliminary educational and advisory support. All assessments and recommendations must be physically verified by certified agricultural extension officers or Krishi Vigyan Kendras (KVK).
    </div>
    <div style="font-size:0.75rem; color:#94A3B8;">
        &copy; 2026 KisanSaathi &middot; Built with Gemini 2.5 Flash &amp; Streamlit &middot; Grounded in ICAR Agronomic Practice Standards
    </div>
</div>
""", unsafe_allow_html=True)
