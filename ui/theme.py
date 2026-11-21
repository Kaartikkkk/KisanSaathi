"""Complete Light Theme & Design System Stylesheet for KisanSaathi.
Enforces warm ivory #F7F8F2, forest green #174B35, edge-to-edge top navbar,
centered tab navigation, responsive layouts (1440px to 375px), and zero CSS conflicts.
"""

CSS_LIGHT_THEME = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --bg-primary: #F7F8F2;
    --bg-card: #FFFFFF;
    --border-color: #E2E9E1;
    --border-focus: #174B35;
    --color-primary: #174B35;
    --color-primary-hover: #123D2B;
    --color-secondary: #2E7D50;
    --color-accent: #E7F2E8;
    --text-primary: #25352D;
    --text-secondary: #4A5B52;
    --text-muted: #5A6860;
    --font-main: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
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
    background-color: var(--bg-primary) !important;
    background: var(--bg-primary) !important;
    color: var(--text-primary) !important;
    font-family: var(--font-main) !important;
    overflow-x: hidden !important;
}

/* Strip default Streamlit header bar completely */
[data-testid="stHeader"],
header[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"] {
    display: none !important;
    height: 0px !important;
}

/* Strip main block padding so top navbar touches true top edge-to-edge */
.block-container,
[data-testid="block-container"],
[data-testid="stMainBlockContainer"] {
    padding-top: 0rem !important;
    padding-left: 0rem !important;
    padding-right: 0rem !important;
    padding-bottom: 2.5rem !important;
    max-width: 100% !important;
    width: 100% !important;
    margin: 0 !important;
}

/* 2. PINNED FULL-WIDTH TOP NAVBAR */
.ks-navbar {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    width: 100% !important;
    height: 70px !important;
    background: #FFFFFF !important;
    border-bottom: 1.5px solid var(--border-color) !important;
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
    color: var(--color-primary) !important;
    line-height: 1.1 !important;
    letter-spacing: -0.02em !important;
}

.ks-nav-brand-sub {
    font-size: 0.75rem !important;
    color: var(--text-muted) !important;
    font-weight: 500 !important;
    line-height: 1.1 !important;
}

.ks-lang-pill {
    background: #FFFFFF !important;
    color: var(--text-primary) !important;
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

[data-baseweb="tab-list"],
div[data-testid="stTabs"] [data-baseweb="tab-list"],
.stTabs [data-baseweb="tab-list"] {
    position: fixed !important;
    top: 14px !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    z-index: 10001 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 6px !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

/* Hide default underline border and indicator */
div[data-baseweb="tab-border"],
div[data-baseweb="tab-highlight"],
[data-baseweb="tab-border"],
[data-baseweb="tab-highlight"] {
    display: none !important;
    height: 0px !important;
    border: none !important;
}

/* Tab button styling */
button[data-baseweb="tab"],
div[data-baseweb="tab-list"] button,
.stTabs [data-baseweb="tab"] {
    background-color: transparent !important;
    color: var(--text-primary) !important;
    font-family: var(--font-main) !important;
    font-size: 0.92rem !important;
    font-weight: 500 !important;
    padding: 8px 18px !important;
    border-radius: 999px !important;
    border: none !important;
    transition: all 0.2s ease !important;
    cursor: pointer !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 6px !important;
    outline: none !important;
    box-shadow: none !important;
}

button[data-baseweb="tab"]:hover,
div[data-baseweb="tab-list"] button:hover,
.stTabs [data-baseweb="tab"]:hover {
    background-color: rgba(23, 75, 53, 0.06) !important;
    color: var(--color-primary) !important;
}

/* Active tab: solid forest green pill */
button[data-baseweb="tab"][aria-selected="true"],
div[data-baseweb="tab-list"] button[aria-selected="true"],
.stTabs [data-baseweb="tab"][aria-selected="true"] {
    background-color: var(--color-primary) !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 14px rgba(23, 75, 53, 0.25) !important;
}

/* Vector line icons on tabs via CSS ::before */
button[data-baseweb="tab"]::before,
div[data-baseweb="tab-list"] button::before,
.stTabs [data-baseweb="tab"]::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
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

/* 4. TAB PANELS CONTAINER WITH COMFORTABLE TOP OFFSET */
div[data-baseweb="tab-panel"] {
    padding-top: 92px !important;
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
    padding-bottom: 2.5rem !important;
    max-width: 1240px !important;
    margin-left: auto !important;
    margin-right: auto !important;
    box-sizing: border-box !important;
}

/* 5. CROP DIAGNOSTIC CENTER (CARD STYLING) */
.ks-ask-card {
    background: #FFFFFF !important;
    border: 1.5px solid var(--border-color) !important;
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
    color: var(--color-primary) !important;
    line-height: 1.2 !important;
    margin: 0 0 0.35rem 0 !important;
    display: flex !important;
    align-items: center !important;
    gap: 0.65rem !important;
}

.ks-ask-subtitle {
    font-size: 0.95rem !important;
    color: var(--text-muted) !important;
    margin: 0 !important;
}

.ks-ask-badge {
    background: var(--color-accent) !important;
    color: var(--color-primary) !important;
    font-size: 0.82rem !important;
    font-weight: 700 !important;
    border-radius: 999px !important;
    padding: 6px 16px !important;
    border: 1px solid #D0E7D4 !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 0.4rem !important;
}

/* Preset Scenarios */
.ks-preset-section-title {
    font-size: 1rem !important;
    font-weight: 700 !important;
    color: var(--color-primary) !important;
    margin-bottom: 0.85rem !important;
    display: flex !important;
    align-items: center !important;
    gap: 0.5rem !important;
}

.ks-preset-col button {
    background: var(--color-primary) !important;
    color: #FFFFFF !important;
    font-weight: 600 !important;
    font-size: 0.86rem !important;
    border-radius: 999px !important;
    border: none !important;
    padding: 0.55rem 1rem !important;
    box-shadow: 0 2px 6px rgba(23, 75, 53, 0.15) !important;
    transition: all 0.2s ease !important;
}
.ks-preset-col button:hover {
    background: var(--color-primary-hover) !important;
    transform: translateY(-1px) !important;
}

.ks-reset-col button {
    background: #FFFFFF !important;
    color: var(--color-primary) !important;
    font-weight: 600 !important;
    font-size: 0.86rem !important;
    border-radius: 999px !important;
    border: 1.5px solid #DCE5DB !important;
    padding: 0.55rem 1rem !important;
    transition: all 0.2s ease !important;
}
.ks-reset-col button:hover {
    background: #F4F8F4 !important;
    border-color: var(--color-primary) !important;
}

/* Form Inputs */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div {
    background-color: #FFFFFF !important;
    border: 1.5px solid #DCE5DB !important;
    border-radius: 12px !important;
    color: var(--text-primary) !important;
    font-family: var(--font-main) !important;
    font-size: 0.95rem !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: var(--color-primary) !important;
    box-shadow: 0 0 0 2px rgba(23, 75, 53, 0.15) !important;
}

.stTextInput label,
.stSelectbox label,
.stTextArea label {
    font-size: 0.92rem !important;
    font-weight: 700 !important;
    color: var(--color-primary) !important;
    margin-bottom: 0.35rem !important;
}

/* Full-width Analyze button */
.ks-analyze-btn button {
    background: var(--color-primary) !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    font-size: 1.05rem !important;
    border-radius: 999px !important;
    border: none !important;
    padding: 0.85rem 2rem !important;
    box-shadow: 0 4px 14px rgba(23, 75, 53, 0.25) !important;
    width: 100% !important;
    margin-top: 1rem !important;
    transition: all 0.2s ease !important;
}
.ks-analyze-btn button:hover {
    background: var(--color-primary-hover) !important;
    transform: translateY(-1px) !important;
}

/* 6. CARDS, SECTIONS & BADGES */
.ks-card {
    background-color: #FFFFFF !important;
    border: 1.5px solid var(--border-color) !important;
    border-radius: 20px !important;
    padding: 2rem 2.25rem !important;
    margin-bottom: 1.5rem !important;
    box-shadow: 0 4px 22px rgba(23, 75, 53, 0.04) !important;
}

.ks-pill-badge {
    display: inline-block;
    padding: 0.35rem 1rem;
    background: var(--color-accent);
    color: var(--color-primary);
    border-radius: 999px;
    font-size: 0.76rem;
    font-weight: 800;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 0.75rem;
}

/* PASS / FAIL Badges */
.ks-badge-pass {
    background: #E8F5E9 !important;
    color: #174B35 !important;
    border: 1.5px solid #2E7D50 !important;
    font-weight: 700 !important;
    font-size: 0.82rem !important;
    border-radius: 999px !important;
    padding: 4px 14px !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 4px !important;
}

.ks-badge-fail {
    background: #FFEBEE !important;
    color: #C62828 !important;
    border: 1.5px solid #D32F2F !important;
    font-weight: 700 !important;
    font-size: 0.82rem !important;
    border-radius: 999px !important;
    padding: 4px 14px !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 4px !important;
}

/* Shared Footer */
.ks-footer {
    border-top: 1.5px solid var(--border-color);
    padding: 2.5rem 1.5rem 1.5rem 1.5rem;
    margin-top: 3.5rem;
    text-align: center;
    background: transparent;
}
.ks-footer a {
    color: var(--color-primary);
    text-decoration: none;
    font-weight: 600;
}
.ks-footer a:hover {
    text-decoration: underline;
}

/* 7. RESPONSIVE DESIGN (1440px, 1280px, 768px, 375px) */
@media (max-width: 992px) {
    [data-baseweb="tab-list"],
    div[data-testid="stTabs"] [data-baseweb="tab-list"],
    .stTabs [data-baseweb="tab-list"] {
        position: static !important;
        transform: none !important;
        overflow-x: auto !important;
        width: 100% !important;
        justify-content: flex-start !important;
        padding: 0.65rem 1rem !important;
        background: #FFFFFF !important;
        border-bottom: 1.5px solid var(--border-color) !important;
        border-radius: 0 !important;
    }

    .ks-navbar {
        position: static !important;
        height: auto !important;
        padding: 0.85rem 1.25rem !important;
        flex-wrap: wrap !important;
        gap: 0.75rem !important;
    }

    div[data-baseweb="tab-panel"] {
        padding-top: 1.5rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }

    .ks-ask-card {
        padding: 1.75rem 1.25rem !important;
    }
}

@media (max-width: 600px) {
    .ks-ask-header {
        flex-direction: column !important;
        gap: 0.75rem !important;
    }
    .ks-ask-title {
        font-size: 1.35rem !important;
    }
}
</style>
"""
