"""Complete Light Theme & Design System Stylesheet for KisanSaathi.
Enforces #F7F8F2 globally, pinned top edge-to-edge navbar, and integrated tabs.
"""

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
section[data-testid="stMain"],
section.main,
.main,
.block-container,
.main .block-container {
    background-color: #F7F8F2 !important;
    background: #F7F8F2 !important;
    color: #25352D !important;
}

/* Strip top header & side margin so top navbar is 100% full width from edge to edge */
[data-testid="stHeader"],
header[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"] {
    display: none !important;
    height: 0px !important;
}

.block-container,
[data-testid="block-container"],
[data-testid="stMainBlockContainer"] {
    padding-top: 0rem !important;
    padding-left: 0rem !important;
    padding-right: 0rem !important;
    padding-bottom: 3rem !important;
    max-width: 100% !important;
    width: 100% !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
}

/* 2. PINNED EDGE-TO-EDGE TOP NAVBAR */
.ks-navbar {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    width: 100% !important;
    height: 70px !important;
    background: #FFFFFF !important;
    border-bottom: 1.5px solid #E2E9E1 !important;
    z-index: 9999 !important;
    padding: 0 2.5rem !important;
    box-sizing: border-box !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    box-shadow: 0 2px 10px rgba(23, 75, 53, 0.03) !important;
}

.ks-nav-brand {
    display: flex !important;
    align-items: center !important;
    gap: 0.75rem !important;
    text-decoration: none !important;
}

.ks-nav-brand-title {
    font-size: 1.35rem !important;
    font-weight: 800 !important;
    color: #174B35 !important;
    line-height: 1.1 !important;
    letter-spacing: -0.02em !important;
}

.ks-nav-brand-sub {
    font-size: 0.75rem !important;
    color: #68756C !important;
    font-weight: 500 !important;
    line-height: 1.1 !important;
}

.ks-lang-pill {
    background: #FFFFFF !important;
    color: #25352D !important;
    border: 1.5px solid #DCE5DB !important;
    border-radius: 999px !important;
    padding: 0.45rem 1.1rem !important;
    font-size: 0.88rem !important;
    font-weight: 600 !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 0.45rem !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.03) !important;
}

/* 3. PINNED STREAMLIT TABS DIRECTLY IN NAVBAR CENTER */
div[data-testid="stTabs"] {
    border: none !important;
}

div[data-testid="stTabs"] > div[data-baseweb="tab-list"] {
    position: fixed !important;
    top: 14px !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    z-index: 10001 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 8px !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

/* Hide default underline border */
div[data-baseweb="tab-border"],
div[data-baseweb="tab-highlight"] {
    display: none !important;
}

/* Clean tab pill buttons */
button[data-baseweb="tab"] {
    background-color: transparent !important;
    color: #25352D !important;
    font-family: 'Inter', -apple-system, sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 500 !important;
    padding: 8px 18px !important;
    border-radius: 999px !important;
    border: none !important;
    transition: all 0.2s ease !important;
    cursor: pointer !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 6px !important;
}

button[data-baseweb="tab"]:hover {
    background-color: rgba(23, 75, 53, 0.06) !important;
    color: #174B35 !important;
}

/* Active tab: dark green pill */
button[data-baseweb="tab"][aria-selected="true"] {
    background-color: #174B35 !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 14px rgba(23, 75, 53, 0.25) !important;
}

/* Vector Outline Icons on tabs via CSS ::before */
button[data-baseweb="tab"]::before {
    content: "";
    display: inline-block;
    width: 17px;
    height: 17px;
    margin-right: 6px;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    vertical-align: middle;
}

/* Tab 1: Home (House outline) */
button[data-baseweb="tab"]:nth-child(1)::before {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%2325352D' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z'%3E%3C/path%3E%3Cpolyline points='9 22 9 12 15 12 15 22'%3E%3C/polyline%3E%3C/svg%3E");
}
button[data-baseweb="tab"]:nth-child(1)[aria-selected="true"]::before {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23FFFFFF' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z'%3E%3C/path%3E%3Cpolyline points='9 22 9 12 15 12 15 22'%3E%3C/polyline%3E%3C/svg%3E");
}

/* Tab 2: How It Works (Layers outline) */
button[data-baseweb="tab"]:nth-child(2)::before {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%2325352D' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolygon points='12 2 2 7 12 12 22 7 12 2'%3E%3C/polygon%3E%3Cpolyline points='2 17 12 22 22 17'%3E%3Cpolyline points='2 12 12 17 22 12'%3E%3C/svg%3E");
}
button[data-baseweb="tab"]:nth-child(2)[aria-selected="true"]::before {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23FFFFFF' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolygon points='12 2 2 7 12 12 22 7 12 2'%3E%3C/polygon%3E%3Cpolyline points='2 17 12 22 22 17'%3E%3Cpolyline points='2 12 12 17 22 12'%3E%3C/svg%3E");
}

/* Tab 3: Ask AI (Leaf outline) */
button[data-baseweb="tab"]:nth-child(3)::before {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%2325352D' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z'%3E%3C/path%3E%3Cpath d='M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12'%3E%3C/path%3E%3C/svg%3E");
}
button[data-baseweb="tab"]:nth-child(3)[aria-selected="true"]::before {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23FFFFFF' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z'%3E%3C/path%3E%3Cpath d='M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12'%3E%3C/path%3E%3C/svg%3E");
}

/* Tab 4: Safety (Shield outline) */
button[data-baseweb="tab"]:nth-child(4)::before {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%2325352D' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z'%3E%3C/path%3E%3C/svg%3E");
}
button[data-baseweb="tab"]:nth-child(4)[aria-selected="true"]::before {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23FFFFFF' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z'%3E%3C/path%3E%3C/svg%3E");
}

/* Tab 5: Evaluation (Bar Chart outline) */
button[data-baseweb="tab"]:nth-child(5)::before {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%2325352D' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M18 20V10M12 20V4M6 20v-6' stroke='%2325352D' stroke-width='2' stroke-linecap='round'/%3E%3C/svg%3E");
}
button[data-baseweb="tab"]:nth-child(5)[aria-selected="true"]::before {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23FFFFFF' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M18 20V10M12 20V4M6 20v-6' stroke='%23FFFFFF' stroke-width='2' stroke-linecap='round'/%3E%3C/svg%3E");
}

/* 4. TAB PANELS CONTAINER WITH CLEAN TOP OFFSET */
div[data-baseweb="tab-panel"] {
    padding-top: 92px !important;
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
    padding-bottom: 2.5rem !important;
    max-width: 1220px !important;
    margin-left: auto !important;
    margin-right: auto !important;
    box-sizing: border-box !important;
}

/* 5. CROP DIAGNOSTIC CENTER (MOCKUP 7 PIXEL-PERFECT CARD) */
.ks-ask-card {
    background: #FFFFFF !important;
    border: 1.5px solid #E2E9E1 !important;
    border-radius: 24px !important;
    padding: 2.5rem 2.75rem !important;
    position: relative !important;
    overflow: hidden !important;
    box-shadow: 0 4px 22px rgba(23, 75, 53, 0.04) !important;
    margin-bottom: 2rem !important;
}

.ks-ask-corner-foliage {
    position: absolute !important;
    top: 0 !important;
    right: 0 !important;
    width: 170px !important;
    height: 140px !important;
    pointer-events: none !important;
    z-index: 1 !important;
}

.ks-ask-header {
    display: flex !important;
    align-items: flex-start !important;
    justify-content: space-between !important;
    margin-bottom: 1.75rem !important;
    position: relative !important;
    z-index: 2 !important;
}

.ks-ask-title {
    font-size: 1.6rem !important;
    font-weight: 800 !important;
    color: #174B35 !important;
    line-height: 1.2 !important;
    margin: 0 0 0.35rem 0 !important;
    display: flex !important;
    align-items: center !important;
    gap: 0.65rem !important;
}

.ks-ask-subtitle {
    font-size: 0.95rem !important;
    color: #68756C !important;
    margin: 0 !important;
}

.ks-ask-badge {
    background: #E8F5E9 !important;
    color: #174B35 !important;
    font-size: 0.85rem !important;
    font-weight: 700 !important;
    border-radius: 999px !important;
    padding: 6px 18px !important;
    border: 1px solid #D0E7D4 !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 0.4rem !important;
}

/* Quick Fill Preset Section */
.ks-preset-section-title {
    font-size: 1.02rem !important;
    font-weight: 700 !important;
    color: #174B35 !important;
    margin-bottom: 0.85rem !important;
    display: flex !important;
    align-items: center !important;
    gap: 0.5rem !important;
}

/* Preset buttons styling */
.ks-preset-col button {
    background: #174B35 !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    font-size: 0.88rem !important;
    border-radius: 999px !important;
    border: none !important;
    padding: 0.55rem 1rem !important;
    box-shadow: 0 2px 6px rgba(23, 75, 53, 0.15) !important;
    transition: all 0.2s ease !important;
}
.ks-preset-col button:hover {
    background: #1e5a41 !important;
    transform: translateY(-1px) !important;
}

/* Reset Inputs button styling */
.ks-reset-col button {
    background: #FFFFFF !important;
    color: #174B35 !important;
    font-weight: 700 !important;
    font-size: 0.88rem !important;
    border-radius: 999px !important;
    border: 1.5px solid #DCE5DB !important;
    padding: 0.55rem 1rem !important;
    transition: all 0.2s ease !important;
}
.ks-reset-col button:hover {
    background: #F4F8F4 !important;
    border-color: #174B35 !important;
}

/* Form Inputs Styling */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div {
    background-color: #FFFFFF !important;
    border: 1.5px solid #DCE5DB !important;
    border-radius: 12px !important;
    color: #25352D !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.95rem !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #174B35 !important;
    box-shadow: 0 0 0 2px rgba(23, 75, 53, 0.15) !important;
}

.stTextInput label,
.stSelectbox label,
.stTextArea label {
    font-size: 0.95rem !important;
    font-weight: 700 !important;
    color: #174B35 !important;
    margin-bottom: 0.35rem !important;
}

/* Analyze Button: Solid Green Pill */
.ks-analyze-btn button {
    background: #174B35 !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    font-size: 1.08rem !important;
    border-radius: 999px !important;
    border: none !important;
    padding: 0.85rem 2rem !important;
    box-shadow: 0 4px 14px rgba(23, 75, 53, 0.25) !important;
    width: 100% !important;
    margin-top: 1rem !important;
    transition: all 0.2s ease !important;
}
.ks-analyze-btn button:hover {
    background: #123d2b !important;
    transform: translateY(-1px) !important;
}

/* 6. GENERAL CARDS, PILLS & SECTIONS */
.ks-card {
    background-color: #FFFFFF !important;
    border: 1.5px solid #E2E9E1 !important;
    border-radius: 20px !important;
    padding: 2.25rem 2.4rem !important;
    margin-bottom: 1.5rem !important;
    box-shadow: 0 4px 22px rgba(23, 75, 53, 0.04) !important;
}

.ks-pill-badge {
    display: inline-block;
    padding: 0.3rem 0.95rem;
    background: #E7F2E8;
    color: #174B35;
    border-radius: 999px;
    font-size: 0.76rem;
    font-weight: 800;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 0.75rem;
}

.ks-section-header {
    text-align: center;
    margin-bottom: 2.75rem;
}
.ks-section-title {
    font-size: 2.45rem;
    font-weight: 800;
    color: #174B35;
    letter-spacing: -0.025em;
    margin-bottom: 0.65rem;
}
.ks-section-sub {
    font-size: 1.05rem;
    color: #68756C;
    max-width: 680px;
    margin: 0 auto;
    line-height: 1.6;
}

.ks-bottom-wave-wrap {
    width: 100%;
    margin-top: 2rem;
    margin-bottom: -2.5rem;
}

/* Evaluation Table Rows */
.ks-eval-card {
    background: #FFFFFF;
    border: 1px solid #E2E9E1;
    border-radius: 14px;
    padding: 1.15rem 1.4rem;
    margin-bottom: 0.85rem;
}
.ks-eval-badge {
    background: #E7F2E8;
    color: #0B5A2A;
    padding: 0.25rem 0.7rem;
    border-radius: 999px;
    font-size: 0.78rem;
    font-weight: 700;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background-color: #FFFFFF !important;
    border-right: 1.5px solid #E2E9E1 !important;
}

@media (max-width: 900px) {
    div[data-testid="stTabs"] > div[data-baseweb="tab-list"] {
        position: static !important;
        transform: none !important;
        overflow-x: auto !important;
    }
    .ks-navbar {
        position: static !important;
    }
    div[data-baseweb="tab-panel"] {
        padding-top: 1rem !important;
    }
}
</style>
"""
