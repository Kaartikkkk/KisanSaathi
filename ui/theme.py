"""Complete Light Theme & Design System Stylesheet for KisanSaathi.
Enforces warm ivory #F7F8F4, forest green #174B35, natural green #2F8A57, soft sage #E7F1E8,
in-flow sticky top navbar, centered tab navigation, 1240px container max-width,
responsive layouts (1440px to 375px), and zero CSS conflicts.
"""

CSS_LIGHT_THEME = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --bg-primary: #F7F9F3;
    --bg-card: #FFFFFF;
    --border-color: #DFE9DF;
    --border-focus: #124C35;
    --color-primary: #124C35;
    --color-primary-hover: #0D3726;
    --color-secondary: #238451;
    --color-accent: #E2EFE2;
    --color-accent-subtle: #65A94E;
    --text-primary: #18392D;
    --text-secondary: #4A5B52;
    --text-muted: #64746B;
    --font-main: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

/* 1. FORCE COMPLETE VIEWPORT & ROOT CONTAINERS TO WARM IVORY #F7F8F4 */
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

/* Off-screen invisible component controller iframe (keeps JS engine running without layout impact) */
iframe[title="streamlit_components_v1.html"],
iframe[src*="component"] {
    position: fixed !important;
    top: -9999px !important;
    left: -9999px !important;
    width: 1px !important;
    height: 1px !important;
    opacity: 0.01 !important;
    pointer-events: none !important;
}

div[data-testid="stCustomComponentV1"] {
    position: fixed !important;
    top: -9999px !important;
    left: -9999px !important;
    width: 0px !important;
    height: 0px !important;
    overflow: hidden !important;
    margin: 0 !important;
    padding: 0 !important;
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

/* 2. IN-FLOW STICKY FULL-WIDTH TOP NAVBAR (REPRODUCING REFERENCE SPECIFICATION) */
.ks-navbar {
    position: sticky !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    width: 100% !important;
    height: 68px !important;
    background-color: #FFFFFF !important;
    background: #FFFFFF !important;
    border-bottom: 1.5px solid var(--border-color) !important;
    z-index: 9999 !important;
    padding: 0 2rem !important;
    box-sizing: border-box !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    box-shadow: 0 2px 10px rgba(18, 76, 53, 0.04) !important;
}

.ks-nav-left {
    display: flex !important;
    align-items: center !important;
    flex-shrink: 0 !important;
}

.ks-nav-brand {
    display: flex !important;
    align-items: center !important;
    text-decoration: none !important;
    cursor: pointer !important;
    flex-shrink: 0 !important;
    user-select: none !important;
}

.ks-nav-brand svg {
    height: 38px !important;
    width: auto !important;
    max-width: 180px !important;
    display: block !important;
}

.ks-nav-divider {
    width: 1px !important;
    height: 22px !important;
    background-color: var(--border-color) !important;
    margin: 0 1.25rem 0 1.25rem !important;
    flex-shrink: 0 !important;
}

.ks-nav-links {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 8px !important;
    flex: 1 !important;
    max-width: 720px !important;
    margin: 0 auto !important;
}

.ks-nav-btn {
    background: transparent !important;
    background-color: transparent !important;
    color: var(--text-primary) !important;
    border: none !important;
    border-radius: 999px !important;
    padding: 7px 16px !important;
    font-size: 0.90rem !important;
    font-weight: 500 !important;
    font-family: var(--font-main) !important;
    cursor: pointer !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 7px !important;
    transition: all 0.18s ease !important;
    text-decoration: none !important;
    white-space: nowrap !important;
    user-select: none !important;
    outline: none !important;
}

.ks-nav-btn svg {
    width: 16px !important;
    height: 16px !important;
    stroke: var(--text-primary) !important;
    transition: stroke 0.18s ease !important;
    vertical-align: middle !important;
    flex-shrink: 0 !important;
}

.ks-nav-btn:hover {
    background-color: rgba(18, 76, 53, 0.05) !important;
    color: var(--color-primary) !important;
}

/* Active Page highlighted with pale green background and dark green text */
.ks-nav-btn.active {
    background-color: var(--color-accent) !important;
    background: var(--color-accent) !important;
    color: var(--color-primary) !important;
    font-weight: 700 !important;
    border-radius: 999px !important;
    box-shadow: none !important;
}

.ks-nav-btn.active svg {
    stroke: var(--color-primary) !important;
}

.ks-nav-btn.active span {
    color: var(--color-primary) !important;
}

.ks-nav-lang {
    display: flex !important;
    align-items: center !important;
    justify-content: flex-end !important;
    flex-shrink: 0 !important;
    width: 140px !important;
}

.ks-lang-pill {
    background: #FFFFFF !important;
    color: var(--text-primary) !important;
    border: 1.5px solid var(--border-color) !important;
    border-radius: 999px !important;
    padding: 0.42rem 1rem !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 0.45rem !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.03) !important;
    flex-shrink: 0 !important;
}

/* 3. OFF-SCREEN ACCESSIBLE NATIVE TABS (Hidden from view, 100% active React click listener) */
div[data-testid="stTabs"] {
    margin-top: 0 !important;
    padding-top: 0 !important;
}

div[data-baseweb="tab-list"],
.stTabs [data-baseweb="tab-list"],
[data-baseweb="tab-list"] {
    position: absolute !important;
    top: -9999px !important;
    left: -9999px !important;
    width: 1px !important;
    height: 1px !important;
    overflow: hidden !important;
    opacity: 0 !important;
    pointer-events: auto !important;
    visibility: visible !important;
}

/* Hide Default Streamlit Underline Highlights & Borders Completely */
div[data-baseweb="tab-highlight"],
div[data-baseweb="tab-border"],
[data-baseweb="tab-highlight"],
[data-baseweb="tab-border"] {
    display: none !important;
    height: 0px !important;
    border: none !important;
    background: transparent !important;
    opacity: 0 !important;
    visibility: hidden !important;
}

/* Constrain all decorative and foliage SVGs to prevent viewport overflow */
.ks-hero-card svg,
.ks-ask-corner-foliage svg,
.ks-decorative-svg svg {
    max-width: 100% !important;
    height: auto !important;
    display: block !important;
}

/* =========================================================================
   HOMEPAGE EXACT RECREATION (HERO, COUNTRYSIDE HORIZON, 4 FEATURE CARDS)
   ========================================================================= */
.ks-hero-container {
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    gap: 2.5rem !important;
    flex-wrap: wrap !important;
    padding-top: 1.25rem !important;
    margin-bottom: 1.5rem !important;
}

.ks-hero-left {
    flex: 1 1 480px !important;
    max-width: 540px !important;
}

.ks-hero-badge {
    display: inline-flex !important;
    align-items: center !important;
    gap: 0.45rem !important;
    padding: 0.4rem 1.15rem !important;
    background-color: var(--color-accent) !important;
    background: var(--color-accent) !important;
    color: var(--color-primary) !important;
    border-radius: 999px !important;
    font-size: 0.78rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.06em !important;
    text-transform: uppercase !important;
    margin-bottom: 1.25rem !important;
    border: 1px solid #D2E4D2 !important;
}

.ks-hero-badge svg {
    width: 15px !important;
    height: 15px !important;
    stroke: var(--color-primary) !important;
}

.ks-hero-title {
    font-size: clamp(2.4rem, 3.3vw, 3.2rem) !important;
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
    max-width: 500px !important;
    margin: 0 0 2rem 0 !important;
}

.ks-hero-actions {
    display: flex !important;
    align-items: center !important;
    gap: 1rem !important;
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
    box-shadow: 0 4px 14px rgba(18, 76, 53, 0.22) !important;
    transition: all 0.2s ease !important;
    outline: none !important;
    user-select: none !important;
}

.ks-btn-primary:hover {
    background-color: var(--color-primary-hover) !important;
    background: var(--color-primary-hover) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 18px rgba(18, 76, 53, 0.30) !important;
}

.ks-btn-primary svg {
    stroke: #FFFFFF !important;
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
    transition: all 0.2s ease !important;
    outline: none !important;
    user-select: none !important;
}

.ks-btn-secondary:hover {
    background-color: #F4F8F4 !important;
    background: #F4F8F4 !important;
    transform: translateY(-1px) !important;
}

.ks-btn-secondary svg {
    stroke: var(--color-primary) !important;
}

.ks-hero-right {
    flex: 1 1 420px !important;
    max-width: 490px !important;
    display: flex !important;
    justify-content: center !important;
}

.ks-hero-farmer-frame {
    width: 100% !important;
    max-width: 480px !important;
    aspect-ratio: 16 / 10.5 !important;
    border-radius: 28px !important;
    overflow: hidden !important;
    border: 4px solid #FFFFFF !important;
    box-shadow: 0 16px 36px rgba(18, 76, 53, 0.10) !important;
    background: #FFFFFF !important;
}

.ks-hero-farmer-frame img {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    object-position: center 22% !important;
    display: block !important;
}

/* Countryside Landscape Horizon Decoration */
.ks-landscape-horizon {
    width: 100% !important;
    height: 75px !important;
    margin: 0.4rem 0 1.25rem 0 !important;
    overflow: hidden !important;
    pointer-events: none !important;
}

.ks-landscape-horizon img {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    object-position: center center !important;
    display: block !important;
}

/* 4 Feature Cards Grid */
.ks-feature-cards-grid {
    display: grid !important;
    grid-template-columns: repeat(4, 1fr) !important;
    gap: 1.25rem !important;
    margin-bottom: 2.5rem !important;
    width: 100% !important;
    box-sizing: border-box !important;
}

.ks-feature-card {
    background-color: #FFFFFF !important;
    background: #FFFFFF !important;
    border: 1.5px solid var(--border-color) !important;
    border-radius: 16px !important;
    padding: 1.2rem 1.35rem 1.35rem 1.35rem !important;
    box-shadow: 0 2px 10px rgba(18, 76, 53, 0.03) !important;
    position: relative !important;
    overflow: hidden !important;
    display: flex !important;
    align-items: flex-start !important;
    gap: 0.85rem !important;
    transition: transform 0.2s ease, box-shadow 0.2s ease !important;
}

.ks-feature-card:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 18px rgba(18, 76, 53, 0.08) !important;
}

.ks-feature-icon-box {
    width: 44px !important;
    height: 44px !important;
    border-radius: 12px !important;
    background-color: #E8F3E8 !important;
    background: #E8F3E8 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    flex-shrink: 0 !important;
}

.ks-feature-icon-box svg {
    width: 20px !important;
    height: 20px !important;
    stroke: var(--color-primary) !important;
}

.ks-feature-text {
    flex: 1 !important;
}

.ks-feature-title {
    font-size: 0.96rem !important;
    font-weight: 700 !important;
    color: var(--text-primary) !important;
    margin-bottom: 3px !important;
    line-height: 1.2 !important;
}

.ks-feature-desc {
    font-size: 0.80rem !important;
    color: var(--text-muted) !important;
    line-height: 1.45 !important;
    margin: 0 !important;
}

.ks-feature-accent-line {
    position: absolute !important;
    bottom: 0 !important;
    left: 20px !important;
    width: 48px !important;
    height: 3px !important;
    background-color: var(--color-secondary) !important;
    background: var(--color-secondary) !important;
    border-radius: 2px !important;
}

/* 4. TAB PANELS CONTAINER (Comfortable 1240px container, natural document flow) */
div[data-baseweb="tab-panel"] {
    padding-top: 1.75rem !important;
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
    padding-bottom: 2.5rem !important;
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
    border: 1.5px solid var(--border-color) !important;
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

/* Quick-Fill Preset Buttons: Explicit key scoping to prevent tooltip pollution */
.st-key-qf_tomato button,
.st-key-qf_rice button,
.st-key-qf_wheat button,
.st-key-qf_potato button {
    background-color: var(--color-primary) !important;
    background: var(--color-primary) !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    font-size: 0.88rem !important;
    border-radius: 999px !important;
    border: 1.5px solid var(--color-primary) !important;
    padding: 0.55rem 1.1rem !important;
    box-shadow: 0 2px 8px rgba(23, 75, 53, 0.18) !important;
    transition: all 0.2s ease !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 6px !important;
    white-space: nowrap !important;
}

.st-key-qf_tomato button:hover,
.st-key-qf_rice button:hover,
.st-key-qf_wheat button:hover,
.st-key-qf_potato button:hover {
    background-color: var(--color-primary-hover) !important;
    background: var(--color-primary-hover) !important;
    border-color: var(--color-primary-hover) !important;
    color: #FFFFFF !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 12px rgba(23, 75, 53, 0.25) !important;
}

.st-key-qf_tomato button *,
.st-key-qf_rice button *,
.st-key-qf_wheat button *,
.st-key-qf_potato button * {
    color: #FFFFFF !important;
    font-weight: 700 !important;
}

/* Preset Button 5 (Reset): White Pill with #174B35 Border and Text */
.st-key-qf_reset button {
    background-color: #FFFFFF !important;
    background: #FFFFFF !important;
    color: var(--color-primary) !important;
    font-weight: 700 !important;
    font-size: 0.88rem !important;
    border-radius: 999px !important;
    border: 1.5px solid var(--color-primary) !important;
    padding: 0.55rem 1.1rem !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04) !important;
    transition: all 0.2s ease !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 6px !important;
    white-space: nowrap !important;
}

.st-key-qf_reset button:hover {
    background-color: #F4F8F4 !important;
    background: #F4F8F4 !important;
    border-color: var(--color-primary-hover) !important;
    color: var(--color-primary-hover) !important;
    transform: translateY(-1px) !important;
}

.st-key-qf_reset button * {
    color: var(--color-primary) !important;
    font-weight: 700 !important;
}

/* Preset Icons */
.st-key-qf_tomato button::before {
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

.st-key-qf_rice button::before {
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

.st-key-qf_wheat button::before {
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

.st-key-qf_potato button::before {
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

.st-key-qf_reset button::before {
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

/* ABSOLUTE RESET: Streamlit Tooltip Hover Target Buttons & Help Icons must never be styled as pills */
div.stTooltipHoverTarget,
div.stTooltipHoverTarget button,
.stTooltipHoverTarget,
.stTooltipHoverTarget button,
[data-testid="stTooltipHoverTarget"],
[data-testid="stTooltipHoverTarget"] button {
    background: transparent !important;
    background-color: transparent !important;
    border: none !important;
    border-radius: 0 !important;
    padding: 0 !important;
    margin: 0 !important;
    box-shadow: none !important;
    width: auto !important;
    height: auto !important;
    display: inline-flex !important;
    transform: none !important;
}

div.stTooltipHoverTarget button::before,
.stTooltipHoverTarget button::before,
[data-testid="stTooltipHoverTarget"] button::before {
    display: none !important;
    content: none !important;
}

div.stTooltipHoverTarget svg,
[data-testid="stTooltipHoverTarget"] svg {
    width: 16px !important;
    height: 16px !important;
    opacity: 0.6 !important;
    fill: none !important;
    stroke: var(--text-muted) !important;
}

div.stTooltipHoverTarget:hover svg,
[data-testid="stTooltipHoverTarget"]:hover svg {
    opacity: 1 !important;
    stroke: var(--color-primary) !important;
}

/* Form Inputs */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div {
    background-color: #FFFFFF !important;
    border: 1.5px solid var(--border-color) !important;
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

/* Primary Button (Analyze Crop Problem) */
.st-key-btn_analyze_crop button,
button[kind="primary"],
div[data-testid="stBaseButton-primary"] button {
    background-color: var(--color-primary) !important;
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
    display: flex !important;
    flex-direction: row !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 8px !important;
}

.st-key-btn_analyze_crop button > div,
button[kind="primary"] > div,
div[data-testid="stBaseButton-primary"] button > div {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: auto !important;
}

.st-key-btn_analyze_crop button:hover,
button[kind="primary"]:hover,
div[data-testid="stBaseButton-primary"] button:hover {
    background-color: var(--color-primary-hover) !important;
    background: var(--color-primary-hover) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 18px rgba(23, 75, 53, 0.32) !important;
}

.st-key-btn_analyze_crop button *,
button[kind="primary"] *,
div[data-testid="stBaseButton-primary"] button * {
    color: #FFFFFF !important;
    font-weight: 700 !important;
}

/* Primary Button (Analyze Crop Problem) leaf icon */
.st-key-btn_analyze_crop button::before,
button[kind="primary"]::before,
div[data-testid="stBaseButton-primary"] button::before {
    content: "";
    display: inline-block !important;
    flex-shrink: 0 !important;
    width: 18px !important;
    height: 18px !important;
    margin-right: 6px !important;
    background-size: contain !important;
    background-repeat: no-repeat !important;
    background-position: center !important;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23FFFFFF' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z'/%3E%3Cpath d='M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12'/%3E%3C/svg%3E") !important;
    vertical-align: middle;
}

/* 6. ARCHITECTURE & SAFETY CARDS (Compact equal-height layout without vertical overflow) */
.ks-how-it-works-page,
.ks-safety-page {
    position: relative !important;
    width: 100% !important;
    overflow: hidden !important;
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
    min-height: 290px !important;
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
    margin-bottom: 0.85rem !important;
}

.ks-arch-card-title {
    font-size: 1.15rem !important;
    font-weight: 800 !important;
    color: var(--color-primary) !important;
    margin: 0 0 0.45rem 0 !important;
    letter-spacing: -0.02em !important;
    line-height: 1.2 !important;
}

.ks-arch-card-desc {
    font-size: 0.88rem !important;
    color: var(--text-muted) !important;
    line-height: 1.5 !important;
    margin: 0 0 0.85rem 0 !important;
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
    max-height: 95px !important;
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

/* 8. RESPONSIVE DESIGN (1440px, 1280px, 992px, 768px, 375px) */
@media (max-width: 992px) {
    .ks-navbar {
        height: auto !important;
        min-height: 58px !important;
        padding: 0.5rem 1rem !important;
        flex-wrap: wrap !important;
        gap: 0.5rem !important;
    }

    .ks-nav-left {
        order: 1 !important;
        width: auto !important;
    }

    .ks-nav-brand {
        width: auto !important;
    }

    .ks-nav-divider {
        display: none !important;
    }

    .ks-nav-lang {
        order: 2 !important;
        width: auto !important;
    }

    .ks-nav-links {
        order: 3 !important;
        width: 100% !important;
        max-width: 100% !important;
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch !important;
        justify-content: flex-start !important;
        padding: 0.25rem 0 !important;
    }

    .ks-nav-btn {
        padding: 5px 13px !important;
        font-size: 0.84rem !important;
    }

    div[data-baseweb="tab-panel"] {
        padding-top: 1.25rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }

    .ks-hero-container {
        flex-direction: column !important;
        align-items: stretch !important;
        gap: 1.5rem !important;
    }

    .ks-hero-left, .ks-hero-right {
        max-width: 100% !important;
    }

    .ks-hero-farmer-frame {
        max-width: 100% !important;
    }

    .ks-feature-cards-grid {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 1rem !important;
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
        min-height: auto !important;
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
    .ks-hero-title {
        font-size: 2.1rem !important;
    }
    .ks-hero-actions {
        flex-direction: column !important;
        align-items: stretch !important;
    }
    .ks-btn-primary, .ks-btn-secondary {
        width: 100% !important;
        justify-content: center !important;
    }
    .ks-feature-cards-grid {
        grid-template-columns: 1fr !important;
    }
}
</style>
"""
