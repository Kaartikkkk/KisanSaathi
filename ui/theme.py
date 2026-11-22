"""Light Theme & Design System Stylesheet for KisanSaathi.
Enforces warm ivory #F7F9F4, primary forest green #124C36, secondary green #238B52,
soft sage #E8F3E9, border #DDE8DE, text #183B2D and #64756C.
Matches the target visual reference image with precision.
"""

CSS_DESIGN_SYSTEM = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap');

:root {
    --bg-page: #F7F9F4;
    --bg-card: #FFFFFF;
    --border-color: #DDE8DE;
    --color-primary: #124C36;
    --color-primary-hover: #0B3324;
    --color-secondary: #238B52;
    --color-accent: #E8F3E9;
    --color-accent-border: #C8DEC9;
    --text-primary: #183B2D;
    --text-secondary: #4A5D54;
    --text-muted: #64756C;
    --font-heading: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    --font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* 1. ROOT CANVAS & GLOBAL RESET */
html, body, #root, .stApp,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewRoot"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"],
section[data-testid="stMain"],
section.main, .main,
.block-container,
.main .block-container {
    background-color: var(--bg-page) !important;
    background: var(--bg-page) !important;
    color: var(--text-primary) !important;
    font-family: var(--font-body) !important;
    overflow-x: hidden !important;
}

/* Hide default Streamlit chrome header */
[data-testid="stHeader"],
header[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"] {
    display: none !important;
    height: 0px !important;
}

/* Strip top padding from main container so navbar touches top */
.block-container,
[data-testid="block-container"],
[data-testid="stMainBlockContainer"] {
    padding-top: 0rem !important;
    padding-left: 0rem !important;
    padding-right: 0rem !important;
    padding-bottom: 2rem !important;
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
    width: 100vw !important;
    max-width: 100% !important;
    height: 70px !important;
    background: #FFFFFF !important;
    background-color: #FFFFFF !important;
    border-bottom: 1.5px solid var(--border-color) !important;
    z-index: 10000 !important;
    padding: 0 2rem !important;
    box-sizing: border-box !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    box-shadow: 0 2px 12px rgba(18, 76, 54, 0.04) !important;
}

.ks-nav-left {
    display: flex !important;
    align-items: center !important;
    gap: 0.85rem !important;
    flex-shrink: 0 !important;
}

.ks-nav-brand {
    display: flex !important;
    align-items: center !important;
    gap: 0.75rem !important;
    text-decoration: none !important;
    cursor: pointer !important;
    user-select: none !important;
}

.ks-nav-logo-box {
    width: 36px !important;
    height: 36px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    flex-shrink: 0 !important;
}

.ks-nav-logo-box svg,
.ks-nav-logo-box img {
    width: 100% !important;
    height: 100% !important;
    object-fit: contain !important;
    display: block !important;
}

.ks-nav-brand-text {
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
}

.ks-brand-title {
    font-family: var(--font-heading) !important;
    font-size: 1.35rem !important;
    font-weight: 800 !important;
    color: var(--color-primary) !important;
    line-height: 1.1 !important;
    letter-spacing: -0.02em !important;
}

.ks-brand-subtitle {
    font-size: 0.76rem !important;
    color: var(--text-muted) !important;
    font-weight: 500 !important;
    line-height: 1.1 !important;
    margin-top: 2px !important;
}

.ks-nav-divider {
    width: 1px !important;
    height: 24px !important;
    background-color: var(--border-color) !important;
    margin: 0 0.5rem !important;
}

.ks-nav-lang {
    display: flex !important;
    align-items: center !important;
    justify-content: flex-end !important;
    flex-shrink: 0 !important;
}

.ks-lang-pill {
    background: #FFFFFF !important;
    color: var(--text-primary) !important;
    border: 1.5px solid var(--border-color) !important;
    border-radius: 999px !important;
    padding: 0.42rem 1.1rem !important;
    font-size: 0.86rem !important;
    font-weight: 600 !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 0.45rem !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.02) !important;
    cursor: default !important;
    user-select: none !important;
}

/* 3. CENTERED TOP NAVBAR TABS (Native Streamlit Tabs embedded in Navbar) */
div[data-testid="stTabs"] {
    margin-top: 0 !important;
    padding-top: 0 !important;
}

[data-baseweb="tab-list"],
div[data-testid="stTabs"] [data-baseweb="tab-list"],
[role="tablist"] {
    position: fixed !important;
    top: 14px !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    z-index: 10005 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 8px !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    margin: 0 !important;
    height: 42px !important;
    pointer-events: auto !important;
}

[data-baseweb="tab-list"] button[role="tab"],
div[data-testid="stTabs"] button[role="tab"],
[data-testid="stTab"] {
    background: transparent !important;
    color: var(--text-primary) !important;
    border: none !important;
    border-radius: 999px !important;
    padding: 7px 18px !important;
    font-size: 0.92rem !important;
    font-weight: 500 !important;
    font-family: var(--font-body) !important;
    cursor: pointer !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 6px !important;
    transition: all 0.18s ease !important;
    text-decoration: none !important;
    white-space: nowrap !important;
    outline: none !important;
    box-shadow: none !important;
    height: 40px !important;
    margin: 0 !important;
}

[data-baseweb="tab-list"] button[role="tab"]:hover,
div[data-testid="stTabs"] button[role="tab"]:hover,
[data-testid="stTab"]:hover {
    background-color: rgba(18, 76, 54, 0.05) !important;
    color: var(--color-primary) !important;
}

/* Active Navigation Tab matching reference: Light green pill background + dark green text */
[data-baseweb="tab-list"] button[role="tab"][aria-selected="true"],
div[data-testid="stTabs"] button[role="tab"][aria-selected="true"],
[data-testid="stTab"][aria-selected="true"] {
    background-color: var(--color-accent) !important;
    background: var(--color-accent) !important;
    color: var(--color-primary) !important;
    font-weight: 700 !important;
    border: 1px solid var(--color-accent-border) !important;
    border-radius: 999px !important;
}

[data-baseweb="tab-list"] button[role="tab"][aria-selected="true"] *,
div[data-testid="stTabs"] button[role="tab"][aria-selected="true"] *,
[data-testid="stTab"][aria-selected="true"] * {
    color: var(--color-primary) !important;
    font-weight: 700 !important;
}

/* Remove default Streamlit tab highlight underline */
div[data-baseweb="tab-highlight"],
div[data-baseweb="tab-border"],
[data-baseweb="tab-highlight"],
[data-baseweb="tab-border"] {
    display: none !important;
    height: 0px !important;
    visibility: hidden !important;
}

/* Tab Icons */
[data-baseweb="tab-list"] button[role="tab"]::before,
div[data-testid="stTabs"] button[role="tab"]::before,
[data-testid="stTab"]::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    margin-right: 6px;
    flex-shrink: 0;
}

/* Tab 1: Home */
[data-baseweb="tab-list"] button[role="tab"]:nth-of-type(1)::before,
div[data-testid="stTabs"] button[role="tab"]:nth-of-type(1)::before {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23124C36' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z'/%3E%3Cpolyline points='9 22 9 12 15 12 15 22'/%3E%3C/svg%3E");
}

/* Tab 2: Ask AI */
[data-baseweb="tab-list"] button[role="tab"]:nth-of-type(2)::before,
div[data-testid="stTabs"] button[role="tab"]:nth-of-type(2)::before {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23124C36' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z'/%3E%3C/svg%3E");
}

/* Tab 3: How It Works */
[data-baseweb="tab-list"] button[role="tab"]:nth-of-type(3)::before,
div[data-testid="stTabs"] button[role="tab"]:nth-of-type(3)::before {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23124C36' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolygon points='12 2 2 7 12 12 22 7 12 2'/%3E%3Cpolyline points='2 17 12 22 22 17'/%3E%3Cpolyline points='2 12 12 17 22 12'/%3E%3C/svg%3E");
}

/* Tab 4: Safety Guardrails */
[data-baseweb="tab-list"] button[role="tab"]:nth-of-type(4)::before,
div[data-testid="stTabs"] button[role="tab"]:nth-of-type(4)::before {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23124C36' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z'/%3E%3Cpolyline points='9 12 11 14 15 10'/%3E%3C/svg%3E");
}

/* Tab 5: Evaluation */
[data-baseweb="tab-list"] button[role="tab"]:nth-of-type(5)::before,
div[data-testid="stTabs"] button[role="tab"]:nth-of-type(5)::before {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23124C36' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='18' y1='20' x2='18' y2='10'/%3E%3Cline x1='12' y1='20' x2='12' y2='4'/%3E%3Cline x1='6' y1='20' x2='6' y2='14'/%3E%3C/svg%3E");
}

/* 4. MAIN PAGE CONTAINER PADDING */
div[data-baseweb="tab-panel"] {
    padding-top: 96px !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
    padding-bottom: 2.5rem !important;
    max-width: 1260px !important;
    margin-left: auto !important;
    margin-right: auto !important;
    box-sizing: border-box !important;
}

/* 5. HERO SECTION STYLES (Matching Visual Reference) */
.ks-hero-container {
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    gap: 3.5rem !important;
    position: relative !important;
    padding: 0.5rem 0 1.5rem 0 !important;
    z-index: 2 !important;
}

.ks-hero-left {
    flex: 1 1 520px !important;
    max-width: 580px !important;
}

.ks-hero-badge {
    display: inline-flex !important;
    align-items: center !important;
    gap: 0.45rem !important;
    padding: 0.42rem 1.15rem !important;
    background-color: var(--color-accent) !important;
    color: var(--color-primary) !important;
    border-radius: 999px !important;
    font-size: 0.78rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.06em !important;
    text-transform: uppercase !important;
    margin-bottom: 1.25rem !important;
    border: 1px solid var(--color-accent-border) !important;
}

.ks-hero-title {
    font-family: var(--font-heading) !important;
    font-size: clamp(2.5rem, 3.8vw, 3.5rem) !important;
    font-weight: 800 !important;
    line-height: 1.15 !important;
    letter-spacing: -0.03em !important;
    margin: 0 0 1.25rem 0 !important;
}

.ks-hero-title-line1 {
    color: var(--color-primary) !important;
    display: block !important;
}

.ks-hero-title-line2 {
    color: var(--color-secondary) !important;
    display: block !important;
}

.ks-hero-desc {
    font-size: 1.05rem !important;
    color: var(--text-muted) !important;
    line-height: 1.65 !important;
    max-width: 510px !important;
    margin: 0 0 2rem 0 !important;
}

.ks-hero-actions {
    display: flex !important;
    align-items: center !important;
    gap: 1.15rem !important;
    flex-wrap: wrap !important;
}

.ks-btn-primary {
    background-color: var(--color-primary) !important;
    background: var(--color-primary) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 999px !important;
    padding: 0.85rem 1.85rem !important;
    font-size: 0.98rem !important;
    font-weight: 700 !important;
    cursor: pointer !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 0.55rem !important;
    box-shadow: 0 4px 16px rgba(18, 76, 54, 0.22) !important;
    transition: all 0.2s ease !important;
    outline: none !important;
    text-decoration: none !important;
    user-select: none !important;
}

.ks-btn-primary:hover {
    background-color: var(--color-primary-hover) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(18, 76, 54, 0.30) !important;
}

.ks-btn-secondary {
    background-color: #FFFFFF !important;
    background: #FFFFFF !important;
    color: var(--color-primary) !important;
    border: 1.8px solid var(--color-primary) !important;
    border-radius: 999px !important;
    padding: 0.80rem 1.85rem !important;
    font-size: 0.98rem !important;
    font-weight: 700 !important;
    cursor: pointer !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 0.55rem !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.03) !important;
    transition: all 0.2s ease !important;
    outline: none !important;
    text-decoration: none !important;
    user-select: none !important;
}

.ks-btn-secondary:hover {
    background-color: var(--color-accent) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 4px 14px rgba(18, 76, 54, 0.12) !important;
}

/* Framed Farmer Photograph (Matching Reference Card) */
.ks-hero-right {
    flex: 1 1 480px !important;
    display: flex !important;
    justify-content: flex-end !important;
    position: relative !important;
}

.ks-hero-farmer-frame {
    position: relative !important;
    width: 100% !important;
    max-width: 530px !important;
    border-radius: 30px !important;
    border: 6px solid #FFFFFF !important;
    box-shadow: 0 12px 36px rgba(18, 76, 54, 0.12), 0 2px 8px rgba(0,0,0,0.04) !important;
    overflow: hidden !important;
    background: #FFFFFF !important;
    line-height: 0 !important;
}

.ks-hero-farmer-frame img {
    width: 100% !important;
    height: 330px !important;
    object-fit: cover !important;
    object-position: center 20% !important;
    display: block !important;
}

/* Green Sprout Badge on bottom-right of photo */
.ks-farmer-sprout-badge {
    position: absolute !important;
    bottom: -10px !important;
    right: -10px !important;
    width: 56px !important;
    height: 56px !important;
    background: #FFFFFF !important;
    border-radius: 16px !important;
    border: 3px solid #E8F3E9 !important;
    box-shadow: 0 6px 18px rgba(18, 76, 54, 0.15) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    z-index: 10 !important;
}

/* 6. COUNTRYSIDE HORIZON DECORATION */
.ks-landscape-horizon {
    width: 100% !important;
    line-height: 0 !important;
    margin: 1.25rem 0 1.5rem 0 !important;
    position: relative !important;
    z-index: 1 !important;
    opacity: 0.95 !important;
}

.ks-landscape-horizon img {
    width: 100% !important;
    height: auto !important;
    max-height: 95px !important;
    object-fit: cover !important;
    object-position: center bottom !important;
    display: block !important;
}

/* 7. FOUR FEATURE CARDS GRID (Exact match to reference) */
.ks-feature-cards-grid {
    display: grid !important;
    grid-template-columns: repeat(4, 1fr) !important;
    gap: 1.35rem !important;
    position: relative !important;
    z-index: 2 !important;
}

.ks-feature-card {
    background: #FFFFFF !important;
    border: 1.5px solid var(--border-color) !important;
    border-radius: 18px !important;
    padding: 1.45rem 1.35rem 1.35rem 1.35rem !important;
    box-shadow: 0 2px 10px rgba(18, 76, 54, 0.03) !important;
    transition: transform 0.2s ease, box-shadow 0.2s ease !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    min-height: 130px !important;
}

.ks-feature-card:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 8px 24px rgba(18, 76, 54, 0.08) !important;
    border-color: #BED8BF !important;
}

.ks-feature-icon-box {
    width: 44px !important;
    height: 44px !important;
    border-radius: 12px !important;
    background: var(--color-accent) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    margin-bottom: 0.85rem !important;
    flex-shrink: 0 !important;
}

.ks-feature-title {
    font-family: var(--font-heading) !important;
    font-size: 1.05rem !important;
    font-weight: 700 !important;
    color: var(--text-primary) !important;
    margin: 0 0 0.35rem 0 !important;
    line-height: 1.25 !important;
}

.ks-feature-desc {
    font-size: 0.85rem !important;
    color: var(--text-muted) !important;
    line-height: 1.5 !important;
    margin: 0 !important;
}

.ks-feature-accent-line {
    width: 32px !important;
    height: 3.5px !important;
    background: var(--color-secondary) !important;
    border-radius: 2px !important;
    margin-top: 1rem !important;
}

/* 8. ARCHITECTURE & SAFETY CARDS (3-stage layouts) */
.ks-arch-container {
    display: flex !important;
    align-items: stretch !important;
    justify-content: space-between !important;
    gap: 1.15rem !important;
    margin: 1.75rem 0 !important;
}

.ks-arch-card {
    background: #FFFFFF !important;
    border: 1.5px solid var(--border-color) !important;
    border-radius: 20px !important;
    padding: 1.5rem !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    flex: 1 1 0 !important;
    min-width: 250px !important;
    min-height: 310px !important;
    box-shadow: 0 4px 18px rgba(18, 76, 54, 0.04) !important;
    transition: transform 0.2s ease, box-shadow 0.2s ease !important;
}

.ks-arch-card:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 24px rgba(18, 76, 54, 0.08) !important;
}

.ks-arch-arrow {
    width: 34px !important;
    height: 34px !important;
    border-radius: 50% !important;
    background: var(--color-accent) !important;
    border: 1.5px solid var(--color-accent-border) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    flex-shrink: 0 !important;
    align-self: center !important;
}

/* 9. GENERAL CARDS, BADGES & FOOTER */
.ks-card {
    background: #FFFFFF !important;
    border: 1.5px solid var(--border-color) !important;
    border-radius: 18px !important;
    padding: 1.6rem !important;
    box-shadow: 0 2px 10px rgba(18, 76, 54, 0.03) !important;
}

.ks-pill-badge {
    background: var(--color-accent) !important;
    color: var(--color-primary) !important;
    border: 1px solid var(--color-accent-border) !important;
    border-radius: 999px !important;
    padding: 0.35rem 1rem !important;
    font-size: 0.78rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.05em !important;
    text-transform: uppercase !important;
}

.ks-footer {
    border-top: 1.5px solid var(--border-color) !important;
    padding: 2.25rem 1.5rem 1.5rem 1.5rem !important;
    margin-top: 3rem !important;
    text-align: center !important;
    max-width: 1260px !important;
    margin-left: auto !important;
    margin-right: auto !important;
}

/* 10. RESPONSIVE DESIGN (1440, 1366, 1024, 768, 390) */
@media (max-width: 1024px) {
    .ks-feature-cards-grid {
        grid-template-columns: repeat(2, 1fr) !important;
    }
}

@media (max-width: 900px) {
    .ks-hero-container {
        flex-direction: column !important;
        align-items: stretch !important;
        gap: 2rem !important;
    }
    .ks-hero-left, .ks-hero-right {
        max-width: 100% !important;
    }
    .ks-arch-container {
        flex-direction: column !important;
    }
    .ks-arch-arrow {
        transform: rotate(90deg) !important;
        margin: 0.5rem auto !important;
    }
}

@media (max-width: 600px) {
    .ks-feature-cards-grid {
        grid-template-columns: 1fr !important;
    }
    .ks-navbar {
        padding: 0 1rem !important;
    }
}
</style>
"""
