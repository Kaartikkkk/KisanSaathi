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

/* 2. PINNED FULL-WIDTH TOP NAVBAR (100% VISIBLE WITH BRAND, TABS, AND LANGUAGE) */
.ks-navbar {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    width: 100% !important;
    height: 70px !important;
    background-color: #FFFFFF !important;
    background: #FFFFFF !important;
    border-bottom: 1.5px solid var(--border-color) !important;
    z-index: 99998 !important;
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
    cursor: pointer !important;
    flex-shrink: 0 !important;
    z-index: 100000 !important;
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

.ks-nav-lang {
    display: flex !important;
    align-items: center !important;
    gap: 0.75rem !important;
    flex-shrink: 0 !important;
    z-index: 100000 !important;
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
    flex-shrink: 0 !important;
}

/* PIN NATIVE STREAMLIT TABS INTO NAVBAR CENTER */
div[data-testid="stTabs"] {
    background: transparent !important;
    border: none !important;
}

[data-baseweb="tab-list"],
div[data-testid="stTabs"] [data-baseweb="tab-list"],
.stTabs [data-baseweb="tab-list"] {
    position: fixed !important;
    top: 14px !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    z-index: 99999 !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 8px !important;
    background: transparent !important;
    background-color: transparent !important;
    border: none !important;
    border-bottom: none !important;
    box-shadow: none !important;
    margin: 0 !important;
    padding: 0 !important;
    height: 42px !important;
    max-width: 650px !important;
}

/* Individual Tab Buttons */
div[data-baseweb="tab-list"] button[role="tab"],
.stTabs [data-baseweb="tab-list"] button {
    background-color: transparent !important;
    background: transparent !important;
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
    white-space: nowrap !important;
    height: 38px !important;
}

div[data-baseweb="tab-list"] button[role="tab"]:hover,
.stTabs [data-baseweb="tab-list"] button:hover {
    background-color: rgba(23, 75, 53, 0.06) !important;
    color: var(--color-primary) !important;
}

/* Active Tab: Solid Forest Green Pill with White Text */
div[data-baseweb="tab-list"] button[role="tab"][aria-selected="true"],
.stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
    background-color: var(--color-primary) !important;
    background: var(--color-primary) !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 14px rgba(23, 75, 53, 0.22) !important;
}

div[data-baseweb="tab-list"] button[role="tab"][aria-selected="true"] *,
.stTabs [data-baseweb="tab-list"] button[aria-selected="true"] * {
    color: #FFFFFF !important;
    font-weight: 700 !important;
}

/* Hide Default Streamlit Underline Highlights & Borders */
div[data-baseweb="tab-highlight"],
div[data-baseweb="tab-border"],
[data-baseweb="tab-highlight"],
[data-baseweb="tab-border"] {
    display: none !important;
    height: 0px !important;
    border: none !important;
    background: transparent !important;
}

/* Tab Icons via ::before */
div[data-baseweb="tab-list"] button[role="tab"]::before,
.stTabs [data-baseweb="tab-list"] button::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    background-repeat: no-repeat;
    background-position: center;
    background-size: contain;
    flex-shrink: 0;
}

/* Tab 1: Home */
div[data-baseweb="tab-list"] button[role="tab"]:nth-of-type(1)::before {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23174B35' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z'/%3E%3Cpolyline points='9 22 9 12 15 12 15 22'/%3E%3C/svg%3E");
}

/* Tab 2: How It Works */
div[data-baseweb="tab-list"] button[role="tab"]:nth-of-type(2)::before {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23174B35' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolygon points='12 2 2 7 12 12 22 7 12 2'/%3E%3Cpolyline points='2 17 12 22 22 17'/%3E%3Cpolyline points='2 12 12 17 22 12'/%3E%3C/svg%3E");
}

/* Tab 3: Ask AI */
div[data-baseweb="tab-list"] button[role="tab"]:nth-of-type(3)::before {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23174B35' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z'/%3E%3Cpath d='M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12'/%3E%3C/svg%3E");
}

/* Tab 4: Safety */
div[data-baseweb="tab-list"] button[role="tab"]:nth-of-type(4)::before {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23174B35' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z'/%3E%3Cpolyline points='9 12 11 14 15 10'/%3E%3C/svg%3E");
}

/* Tab 5: Evaluation */
div[data-baseweb="tab-list"] button[role="tab"]:nth-of-type(5)::before {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23174B35' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='18' y1='20' x2='18' y2='10'/%3E%3Cline x1='12' y1='20' x2='12' y2='4'/%3E%3Cline x1='6' y1='20' x2='6' y2='14'/%3E%3C/svg%3E");
}

/* Invert icon color to pure white when tab is active */
div[data-baseweb="tab-list"] button[role="tab"][aria-selected="true"]::before,
.stTabs [data-baseweb="tab-list"] button[aria-selected="true"]::before {
    filter: brightness(0) invert(1) !important;
}

/* 4. TAB PANELS CONTAINER (Comfortable top offset matching 70px navbar) */
div[data-baseweb="tab-panel"] {
    padding-top: 84px !important;
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
    padding-bottom: 2rem !important;
    max-width: 1240px !important;
    margin-left: auto !important;
    margin-right: auto !important;
    box-sizing: border-box !important;
}

/* 5. CROP DIAGNOSTIC CENTER (CARD STYLING) */
div[data-testid="stVerticalBlockBorderWrapper"],
.ks-ask-card {
    background: #FFFFFF !important;
    background-color: #FFFFFF !important;
    border: 1.5px solid #E2EBE2 !important;
    border-radius: 24px !important;
    padding: 2.25rem 2.8rem !important;
    position: relative !important;
    overflow: hidden !important;
    box-shadow: 0 4px 24px rgba(23, 75, 53, 0.05) !important;
    margin-bottom: 2rem !important;
}

div[data-testid="stVerticalBlockBorderWrapper"] > div {
    gap: 0.85rem !important;
}

.ks-ask-corner-foliage {
    position: absolute !important;
    top: 0 !important;
    right: 0 !important;
    width: 140px !important;
    height: 110px !important;
    pointer-events: none !important;
    z-index: 1 !important;
}

.ks-ask-header {
    display: flex !important;
    align-items: flex-start !important;
    justify-content: space-between !important;
    margin-bottom: 1.5rem !important;
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

/* Quick-Fill Preset Buttons: Columns 1-4 Solid Forest Green Pill with White Text */
div[data-testid="stHorizontalBlock"] div[data-testid="stColumn"]:nth-child(-n+4) div[data-testid="stButton"] button,
div[data-testid="stHorizontalBlock"] div[data-testid="stColumn"]:nth-child(-n+4) button,
div[data-testid="stHorizontalBlock"] .stColumn:nth-child(-n+4) button,
div[data-testid="stColumn"]:nth-child(-n+4) div[data-testid="stButton"] button {
    background-color: #174B35 !important;
    background: #174B35 !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    font-size: 0.88rem !important;
    border-radius: 999px !important;
    border: 1.5px solid #174B35 !important;
    padding: 0.55rem 1rem !important;
    box-shadow: 0 2px 8px rgba(23, 75, 53, 0.18) !important;
    transition: all 0.2s ease !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 6px !important;
}

div[data-testid="stHorizontalBlock"] div[data-testid="stColumn"]:nth-child(-n+4) button:hover,
div[data-testid="stHorizontalBlock"] .stColumn:nth-child(-n+4) button:hover,
div[data-testid="stColumn"]:nth-child(-n+4) div[data-testid="stButton"] button:hover {
    background-color: #123D2B !important;
    background: #123D2B !important;
    border-color: #123D2B !important;
    color: #FFFFFF !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 12px rgba(23, 75, 53, 0.25) !important;
}

div[data-testid="stHorizontalBlock"] div[data-testid="stColumn"]:nth-child(-n+4) button *,
div[data-testid="stHorizontalBlock"] .stColumn:nth-child(-n+4) button *,
div[data-testid="stColumn"]:nth-child(-n+4) button * {
    color: #FFFFFF !important;
    font-weight: 700 !important;
}

/* Preset Button 5 (Reset): White Pill with #174B35 Border and Text */
div[data-testid="stHorizontalBlock"] div[data-testid="stColumn"]:nth-child(5) div[data-testid="stButton"] button,
div[data-testid="stHorizontalBlock"] div[data-testid="stColumn"]:nth-child(5) button,
div[data-testid="stHorizontalBlock"] .stColumn:nth-child(5) button,
div[data-testid="stColumn"]:nth-child(5) div[data-testid="stButton"] button {
    background-color: #FFFFFF !important;
    background: #FFFFFF !important;
    color: #174B35 !important;
    font-weight: 700 !important;
    font-size: 0.88rem !important;
    border-radius: 999px !important;
    border: 1.5px solid #174B35 !important;
    padding: 0.55rem 1rem !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04) !important;
    transition: all 0.2s ease !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 6px !important;
}

div[data-testid="stHorizontalBlock"] div[data-testid="stColumn"]:nth-child(5) button:hover,
div[data-testid="stHorizontalBlock"] .stColumn:nth-child(5) button:hover,
div[data-testid="stColumn"]:nth-child(5) div[data-testid="stButton"] button:hover {
    background-color: #F4F8F4 !important;
    background: #F4F8F4 !important;
    border-color: #123D2B !important;
    color: #123D2B !important;
    transform: translateY(-1px) !important;
}

div[data-testid="stHorizontalBlock"] div[data-testid="stColumn"]:nth-child(5) button *,
div[data-testid="stHorizontalBlock"] .stColumn:nth-child(5) button *,
div[data-testid="stColumn"]:nth-child(5) button * {
    color: #174B35 !important;
    font-weight: 700 !important;
}

/* Preset Button 1 Icon (Leaf) */
div[data-testid="stHorizontalBlock"] div[data-testid="stColumn"]:nth-child(1) button::before,
div[data-testid="stHorizontalBlock"] .stColumn:nth-child(1) button::before {
    content: "";
    display: inline-block;
    width: 15px;
    height: 15px;
    margin-right: 6px;
    flex-shrink: 0;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23FFFFFF' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z'/%3E%3Cpath d='M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12'/%3E%3C/svg%3E");
}

/* Preset Button 2 Icon (Rice/Grain) */
div[data-testid="stHorizontalBlock"] div[data-testid="stColumn"]:nth-child(2) button::before,
div[data-testid="stHorizontalBlock"] .stColumn:nth-child(2) button::before {
    content: "";
    display: inline-block;
    width: 15px;
    height: 15px;
    margin-right: 6px;
    flex-shrink: 0;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23FFFFFF' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M7 20h10'/%3E%3Cpath d='M10 20c5.5-2.5.8-6.4 3-10'/%3E%3Cpath d='M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5.4-4.8-.3-1.2-.6-2.3-1.9-3-4.2 2.8-.5 4.4.1 5.5.8z'/%3E%3Cpath d='M14.1 6a7 7 0 0 0-1.1 4c1.9-.1 3.3-.6 4.3-1.4 1-1 1.6-2.3 1.7-4.6-2.7.1-4.1 1-4.9 2z'/%3E%3C/svg%3E");
}

/* Preset Button 3 Icon (Wheat Sprout) */
div[data-testid="stHorizontalBlock"] div[data-testid="stColumn"]:nth-child(3) button::before,
div[data-testid="stHorizontalBlock"] .stColumn:nth-child(3) button::before {
    content: "";
    display: inline-block;
    width: 15px;
    height: 15px;
    margin-right: 6px;
    flex-shrink: 0;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23FFFFFF' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M12 22v-9'/%3E%3Cpath d='M9 15c-3-1-3-4-1-6 2 2 3 4 3 6'/%3E%3Cpath d='M15 15c3-1 3-4 1-6-2 2-3 4-3 6'/%3E%3Cpath d='M9 9c-2-1-2-3 0-5 2 2 2 3 2 5'/%3E%3Cpath d='M15 9c2-1 2-3 0-5-2 2-2 3-2 5'/%3E%3C/svg%3E");
}

/* Preset Button 4 Icon (Potato/Tuber dots) */
div[data-testid="stHorizontalBlock"] div[data-testid="stColumn"]:nth-child(4) button::before,
div[data-testid="stHorizontalBlock"] .stColumn:nth-child(4) button::before {
    content: "";
    display: inline-block;
    width: 15px;
    height: 15px;
    margin-right: 6px;
    flex-shrink: 0;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23FFFFFF' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cellipse cx='12' cy='12' rx='9' ry='6'/%3E%3Ccircle cx='9' cy='11' r='0.5' fill='%23FFFFFF'/%3E%3Ccircle cx='14' cy='13' r='0.5' fill='%23FFFFFF'/%3E%3Ccircle cx='12' cy='10' r='0.5' fill='%23FFFFFF'/%3E%3C/svg%3E");
}

/* Preset Button 5 Icon (Reset Outline Circle) */
div[data-testid="stHorizontalBlock"] div[data-testid="stColumn"]:nth-child(5) button::before,
div[data-testid="stHorizontalBlock"] .stColumn:nth-child(5) button::before {
    content: "";
    display: inline-block;
    width: 14px;
    height: 14px;
    margin-right: 6px;
    flex-shrink: 0;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23174B35' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='8'/%3E%3C/svg%3E");
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
    display: flex !important;
    align-items: center !important;
}

/* Form Input Label Icons via ::before from Asset Pack */
div[data-testid="stHorizontalBlock"] div[data-testid="stColumn"]:nth-child(1) div[data-testid="stTextInput"] label::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    margin-right: 6px;
    vertical-align: middle;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23174B35' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 4c-8 0-14 3-14 10a6 6 0 0 0 6 6c7 0 8-8 8-16Z'/%3E%3Cpath d='M4 21c2-5 6-8 12-11'/%3E%3C/svg%3E");
}

div[data-testid="stHorizontalBlock"] div[data-testid="stColumn"]:nth-child(1) > div:nth-child(2) label::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    margin-right: 6px;
    vertical-align: middle;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23174B35' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z'/%3E%3Ccircle cx='12' cy='10' r='3'/%3E%3C/svg%3E");
}

div[data-testid="stHorizontalBlock"] div[data-testid="stColumn"]:nth-child(1) > div:nth-child(3) label::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    margin-right: 6px;
    vertical-align: middle;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23174B35' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M7 20h10'/%3E%3Cpath d='M10 20c5.5-2.5.8-6.4 3-10'/%3E%3Cpath d='M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5.4-4.8-.3-1.2-.6-2.3-1.9-3-4.2 2.8-.5 4.4.1 5.5.8z'/%3E%3Cpath d='M14.1 6a7 7 0 0 0-1.1 4c1.9-.1 3.3-.6 4.3-1.4 1-1 1.6-2.3 1.7-4.6-2.7.1-4.1 1-4.9 2z'/%3E%3C/svg%3E");
}

div[data-testid="stHorizontalBlock"] div[data-testid="stColumn"]:nth-child(2) > div:nth-child(1) label::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    margin-right: 6px;
    vertical-align: middle;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23174B35' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='m12 3 10 18H2L12 3Z'/%3E%3Cpath d='M12 9v5m0 3h.01'/%3E%3C/svg%3E");
}

div[data-testid="stHorizontalBlock"] div[data-testid="stColumn"]:nth-child(2) > div:nth-child(2) label::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    margin-right: 6px;
    vertical-align: middle;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23174B35' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='m5 8 6 6'/%3E%3Cpath d='m4 14 6-6 2-3'/%3E%3Cpath d='M2 5h12'/%3E%3Cpath d='M7 2h1'/%3E%3Cpath d='m22 22-5-10-5 10'/%3E%3Cpath d='M14 18h6'/%3E%3C/svg%3E");
}

div[data-testid="stHorizontalBlock"] div[data-testid="stColumn"]:nth-child(2) > div:nth-child(3) label::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    margin-right: 6px;
    vertical-align: middle;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23174B35' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z'/%3E%3C/svg%3E");
}

/* Primary Button (Analyze Crop Problem) */
button[kind="primary"],
div[data-testid="stBaseButton-primary"] button,
div.ks-analyze-btn button {
    background-color: #174B35 !important;
    background: #174B35 !important;
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
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 8px !important;
}

button[kind="primary"]:hover,
div[data-testid="stBaseButton-primary"] button:hover,
div.ks-analyze-btn button:hover {
    background-color: #123D2B !important;
    background: #123D2B !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 18px rgba(23, 75, 53, 0.32) !important;
}

button[kind="primary"] *,
div[data-testid="stBaseButton-primary"] button *,
div.ks-analyze-btn button * {
    color: #FFFFFF !important;
    font-weight: 700 !important;
}

/* Primary Button (Analyze Crop Problem) leaf icon */
div.ks-analyze-btn button::before,
button[kind="primary"]::before,
div[data-testid="stBaseButton-primary"] button::before {
    content: "";
    display: inline-block;
    width: 18px;
    height: 18px;
    margin-right: 8px;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23FFFFFF' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z'/%3E%3Cpath d='M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12'/%3E%3C/svg%3E");
    vertical-align: middle;
}

/* 6. ARCHITECTURE & SAFETY CARDS (Compact layout to fit on a single screen without vertical scrolling) */
.ks-how-it-works-page,
.ks-safety-page {
    position: relative !important;
    width: 100% !important;
    overflow: hidden !important;
}

.ks-bg-foliage-left {
    position: absolute !important;
    top: 10px !important;
    left: 0 !important;
    width: 100px !important;
    height: 120px !important;
    max-width: 100px !important;
    max-height: 120px !important;
    pointer-events: none !important;
    z-index: 1 !important;
    opacity: 0.45 !important;
}

.ks-bg-foliage-right {
    position: absolute !important;
    top: 10px !important;
    right: 0 !important;
    width: 100px !important;
    height: 120px !important;
    max-width: 100px !important;
    max-height: 120px !important;
    pointer-events: none !important;
    z-index: 1 !important;
    opacity: 0.45 !important;
}

.ks-arch-container {
    display: flex !important;
    align-items: stretch !important;
    justify-content: space-between !important;
    gap: 1.15rem !important;
    position: relative !important;
    z-index: 2 !important;
    margin-bottom: 1.5rem !important;
}

.ks-arch-card {
    background: #FFFFFF !important;
    border: 1.5px solid var(--border-color) !important;
    border-radius: 20px !important;
    padding: 1.4rem 1.5rem 1.15rem 1.5rem !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    flex: 1 1 0 !important;
    min-width: 250px !important;
    box-shadow: 0 4px 20px rgba(23, 75, 53, 0.04) !important;
    transition: transform 0.2s ease, box-shadow 0.2s ease !important;
}

.ks-arch-card:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 26px rgba(23, 75, 53, 0.08) !important;
}

.ks-arch-icon-box {
    width: 42px !important;
    height: 42px !important;
    border-radius: 12px !important;
    background: var(--color-accent) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    margin-bottom: 1rem !important;
}

.ks-arch-card-title {
    font-size: 1.15rem !important;
    font-weight: 800 !important;
    color: var(--color-primary) !important;
    margin: 0 0 0.5rem 0 !important;
    letter-spacing: -0.02em !important;
    line-height: 1.2 !important;
}

.ks-arch-card-desc {
    font-size: 0.88rem !important;
    color: var(--text-muted) !important;
    line-height: 1.5 !important;
    margin: 0 0 1rem 0 !important;
}

.ks-arch-illus {
    margin-top: auto !important;
    display: flex !important;
    justify-content: center !important;
    align-items: flex-end !important;
    padding-top: 0.5rem !important;
}

.ks-arch-illus svg {
    max-width: 100% !important;
    height: auto !important;
    max-height: 110px !important;
    display: block !important;
}

.ks-arch-arrow {
    width: 34px !important;
    height: 34px !important;
    border-radius: 50% !important;
    background: var(--color-accent) !important;
    border: 1.5px solid #D0E7D4 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    flex-shrink: 0 !important;
    align-self: center !important;
    margin: 0 0.2rem !important;
}

/* 7. GENERAL CARDS, SECTIONS & BADGES */
.ks-card {
    background-color: #FFFFFF !important;
    border: 1.5px solid var(--border-color) !important;
    border-radius: 20px !important;
    padding: 1.8rem 2rem !important;
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
    padding: 2.25rem 1.5rem 1.5rem 1.5rem;
    margin-top: 2.5rem;
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

/* 8. RESPONSIVE DESIGN (1440px, 1280px, 768px, 375px) */
@media (max-width: 992px) {
    .ks-navbar {
        height: auto !important;
        padding: 0.65rem 1rem !important;
        flex-wrap: wrap !important;
        gap: 0.5rem !important;
    }

    [data-baseweb="tab-list"],
    div[data-testid="stTabs"] [data-baseweb="tab-list"],
    .stTabs [data-baseweb="tab-list"] {
        top: 60px !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        width: 100% !important;
        max-width: 100% !important;
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch !important;
        justify-content: flex-start !important;
        padding: 0.25rem 0.75rem !important;
        background: #FFFFFF !important;
    }

    div[data-baseweb="tab-panel"] {
        padding-top: 115px !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }

    div[data-testid="stVerticalBlockBorderWrapper"],
    .ks-ask-card {
        padding: 1.5rem 1.25rem !important;
    }

    .ks-arch-container {
        flex-direction: column !important;
        align-items: stretch !important;
    }

    .ks-arch-arrow {
        transform: rotate(90deg) !important;
        margin: 0.5rem auto !important;
    }

    .ks-arch-card {
        width: 100% !important;
        min-width: 0 !important;
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
