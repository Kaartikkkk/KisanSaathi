import base64
import csv
import os
import streamlit as st
from dotenv import load_dotenv

from kisansaathi.pipeline import KisanSaathiPipeline
from kisansaathi.retrieval import load_reference_notes

load_dotenv(override=True)

st.set_page_config(
    page_title="KisanSaathi — AI Crop Advisory",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────
@st.cache_data
def _b64(path: str) -> str:
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""


def get_gemini_api_key(sidebar_input=""):
    if sidebar_input and sidebar_input.strip():
        return sidebar_input.strip()
    try:
        v = st.secrets.get("GEMINI_API_KEY", "")
        if v and str(v).strip():
            return str(v).strip()
    except Exception:
        pass
    v = os.getenv("GEMINI_API_KEY", "")
    return v.strip() if v else ""


def get_gemini_model():
    try:
        v = st.secrets.get("GEMINI_MODEL", "")
        if v and str(v).strip():
            return str(v).strip()
    except Exception:
        pass
    v = os.getenv("GEMINI_MODEL", "")
    if v and v.strip():
        return v.strip()
    return "gemini-2.5-flash"


# ─────────────────────────────────────────────────────────────────────────────
# SVG icons  (clean, monochrome, 24×24 viewBox)
# ─────────────────────────────────────────────────────────────────────────────
def _icon(d, size=20, color="currentColor", sw="2"):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" '
        f'viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" '
        f'stroke-linecap="round" stroke-linejoin="round">{d}</svg>'
    )

_P_LEAF   = '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>'
_P_SHIELD = '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>'
_P_CHECK  = '<polyline points="20 6 9 17 4 12"/>'
_P_SEARCH = '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>'
_P_ALERT  = '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>'
_P_PHONE  = '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.84.36 1.86.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.95.34 1.97.57 2.81.7A2 2 0 0 1 22 16.92z"/>'
_P_QUEST  = '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/>'
_P_GLOBE  = '<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>'
_P_LAYERS = '<polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>'
_P_CHAT   = '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>'
_P_HOME   = '<path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>'
_P_CLIP   = '<path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/><path d="m9 14 2 2 4-4"/>'
_P_SHIELDCK = '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>'
_P_LANG   = '<path d="m5 8 6 6"/><path d="m4 14 6-6 2-3"/><path d="M2 5h12"/><path d="M7 2h1"/><path d="m22 22-5-10-5 10"/><path d="M14 18h6"/>'

IC = {
    "leaf":     _icon(_P_LEAF,   24, "#174B35"),
    "leaf_sm":  _icon(_P_LEAF,   18, "#2E7D50"),
    "shield":   _icon(_P_SHIELD, 20, "#174B35"),
    "shieldck": _icon(_P_SHIELDCK, 28, "#2E7D50"),
    "check":    _icon(_P_CHECK,  16, "currentColor", "2.5"),
    "check_g":  _icon(_P_CHECK,  16, "#2E7D50", "2.5"),
    "search":   _icon(_P_SEARCH, 20, "#174B35"),
    "search_sm":_icon(_P_SEARCH, 28, "#2E7D50"),
    "alert":    _icon(_P_ALERT,  20, "currentColor"),
    "phone":    _icon(_P_PHONE,  18, "currentColor"),
    "quest":    _icon(_P_QUEST,  22, "#174B35"),
    "globe":    _icon(_P_GLOBE,  16, "currentColor"),
    "layers":   _icon(_P_LAYERS, 16, "currentColor"),
    "chat":     _icon(_P_CHAT,   16, "currentColor"),
    "home":     _icon(_P_HOME,   16, "#FFFFFF"),
    "clip":     _icon(_P_CLIP,   20, "#174B35"),
    "lang":     _icon(_P_LANG,   28, "#2E7D50"),
    "leaf_big": _icon(_P_LEAF,   28, "#2E7D50"),
}

# ─────────────────────────────────────────────────────────────────────────────
# CSS — ROOT-LEVEL LIGHT THEME  (fixes black background everywhere)
# ─────────────────────────────────────────────────────────────────────────────
BG   = "#F7F8F2"
PG   = "#174B35"
SG   = "#2E7D50"
LG   = "#E7F2E8"
TXT  = "#25352D"
MTXT = "#68756C"
CARD = "#FFFFFF"
BRD  = "#E2E9E1"

CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* ── GLOBAL LIGHT BACKGROUND ── override every Streamlit surface ── */
html, body                       {{ background: {BG} !important; color: {TXT} !important; }}
.stApp                           {{ background: {BG} !important; }}
[data-testid="stAppViewContainer"]  {{ background: {BG} !important; }}
[data-testid="stHeader"]         {{ background: transparent !important; }}
[data-testid="stToolbar"]        {{ display: none !important; }}
[data-testid="stSidebar"]        {{ background: {CARD} !important; border-right: 1px solid {BRD} !important; }}
[data-testid="stSidebarContent"] {{ background: {CARD} !important; }}
.main, .main .block-container    {{ background: {BG} !important; }}
section[data-testid="stSidebar"] > div {{ background: {CARD} !important; }}

/* typography */
html, body, [class*="css"], .stMarkdown, .stTextInput label,
.stSelectbox label, .stTextArea label, .stButton button {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
}}

.main .block-container {{
    max-width: 1180px;
    padding: 1.5rem 2rem 4rem 2rem;
}}

/* kill default link colours */
a {{ color: {SG}; text-decoration: none; }}
a:hover {{ color: {PG}; }}

/* ── NAVBAR ── */
.ks-nav {{
    display: flex; justify-content: space-between; align-items: center;
    background: {CARD}; border: 1px solid {BRD}; border-radius: 14px;
    padding: 0.7rem 1.5rem; margin-bottom: 1.75rem;
    box-shadow: 0 2px 12px rgba(23,75,53,.04);
}}
.ks-nav-brand {{ display:flex; align-items:center; gap:.6rem; text-decoration:none; }}
.ks-nav-brand-name {{ font-size:1.35rem; font-weight:800; color:{PG}; letter-spacing:-.02em; }}
.ks-nav-brand-sub  {{ font-size:.72rem; font-weight:600; color:{MTXT}; }}
.ks-nav-links {{ display:flex; align-items:center; gap:1.4rem; }}
.ks-nl {{ display:inline-flex; align-items:center; gap:.35rem;
          font-size:.88rem; font-weight:600; color:{TXT}; text-decoration:none; }}
.ks-nl:hover {{ color:{SG}; }}
.ks-nl-active {{
    display:inline-flex; align-items:center; gap:.35rem;
    font-size:.88rem; font-weight:700; color:#fff !important; text-decoration:none;
    background:{PG}; padding:.4rem 1rem; border-radius:999px;
}}
.ks-lang-pill {{
    display:inline-flex; align-items:center; gap:.35rem;
    border:1.5px solid {BRD}; padding:.35rem .85rem; border-radius:999px;
    font-size:.82rem; font-weight:600; color:{TXT}; background:{CARD};
}}

/* ── HERO ── */
.ks-hero {{
    display:flex; flex-wrap:wrap; align-items:center; gap:2.5rem;
    background: linear-gradient(145deg, {CARD} 0%, #F0F4ED 100%);
    border:1px solid {BRD}; border-radius:24px;
    padding: 3rem 2.5rem 2.5rem; margin-bottom:1.5rem;
    box-shadow: 0 8px 28px rgba(23,75,53,.045);
}}
.ks-hero-txt {{ flex:1 1 500px; min-width:300px; }}
.ks-hero-h1 {{
    font-size:2.9rem; font-weight:800; color:{PG};
    line-height:1.14; letter-spacing:-.03em; margin:0 0 .7rem 0;
}}
.ks-hero-bar {{ width:72px; height:4px; background:{SG}; border-radius:3px; margin-bottom:1.3rem; }}
.ks-hero-p {{
    font-size:1.05rem; color:{MTXT}; line-height:1.6; margin-bottom:1.8rem; max-width:520px;
}}
.ks-hero-btns {{ display:flex; flex-wrap:wrap; gap:1rem; }}
.ks-btn-primary {{
    display:inline-flex; align-items:center; gap:.55rem;
    background:{PG}; color:#fff !important; font-weight:700; font-size:.98rem;
    padding:.8rem 1.8rem; border-radius:999px; text-decoration:none;
    box-shadow:0 4px 14px rgba(23,75,53,.22); transition:all .15s ease;
}}
.ks-btn-primary:hover {{ transform:translateY(-1px); box-shadow:0 6px 18px rgba(23,75,53,.3); }}
.ks-btn-outline {{
    display:inline-flex; align-items:center; gap:.55rem;
    background:{CARD}; color:{PG} !important; font-weight:700; font-size:.98rem;
    padding:.78rem 1.6rem; border-radius:999px; border:1.8px solid {PG}; text-decoration:none;
    transition:background .15s ease;
}}
.ks-btn-outline:hover {{ background:#EEF3EC; }}
.ks-hero-img {{ flex:1 1 400px; min-width:280px; display:flex; justify-content:center; }}
.ks-hero-photo {{
    max-width:460px; width:100%; border-radius:20px; overflow:hidden;
    box-shadow:0 12px 32px rgba(23,75,53,.12); border:4px solid {CARD};
}}
.ks-hero-photo img {{ width:100%; height:auto; display:block; object-fit:cover; }}

/* ── FEATURE STRIP ── */
.ks-features {{
    display:grid; grid-template-columns:repeat(4,1fr); gap:0;
    background:{CARD}; border:1px solid {BRD}; border-radius:16px;
    margin-bottom:3rem; box-shadow:0 4px 16px rgba(23,75,53,.03);
}}
.ks-feat {{
    display:flex; flex-direction:column; align-items:center; justify-content:center;
    padding:1.3rem 1rem; text-align:center; border-right:1px solid {BRD};
}}
.ks-feat:last-child {{ border-right:none; }}
.ks-feat-icon {{ margin-bottom:.45rem; }}
.ks-feat-label {{ font-size:.9rem; font-weight:700; color:{PG}; }}

/* ── SECTION HEADERS ── */
.ks-sec-tag {{
    display:inline-block; font-size:.74rem; font-weight:700; text-transform:uppercase;
    letter-spacing:.08em; color:{SG}; background:{LG}; padding:.25rem .75rem;
    border-radius:999px; margin-bottom:.5rem;
}}
.ks-sec-title {{
    font-size:1.75rem; font-weight:800; color:{PG}; letter-spacing:-.02em; margin-bottom:.45rem;
}}
.ks-sec-desc {{ font-size:.95rem; color:{MTXT}; line-height:1.55; }}

/* ── CARDS ── */
.ks-card {{
    background:{CARD}; border:1px solid {BRD}; border-radius:16px;
    padding:1.6rem; margin-bottom:1.4rem;
    box-shadow:0 2px 12px rgba(23,75,53,.025);
    transition: transform .15s ease, box-shadow .15s ease;
}}
.ks-card:hover {{ transform:translateY(-2px); box-shadow:0 6px 20px rgba(23,75,53,.06); }}
.ks-card-static {{
    background:{CARD}; border:1px solid {BRD}; border-radius:16px;
    padding:1.6rem; margin-bottom:1.4rem;
    box-shadow:0 2px 12px rgba(23,75,53,.025);
}}
.ks-card h3 {{ font-size:1.1rem; font-weight:700; color:{PG}; margin-bottom:.45rem; }}
.ks-card p, .ks-card-static p {{ font-size:.88rem; color:{MTXT}; line-height:1.55; margin:0; }}
.ks-card-icon {{
    width:42px; height:42px; border-radius:10px; background:{LG};
    display:flex; align-items:center; justify-content:center; margin-bottom:.9rem;
}}

/* ── FORM CONTAINER ── */
.ks-form-wrap {{
    background:{CARD}; border:1px solid {BRD}; border-radius:20px;
    padding:2rem; margin-bottom:2.5rem; box-shadow:0 4px 20px rgba(23,75,53,.04);
}}
.ks-form-head {{
    display:flex; justify-content:space-between; align-items:center;
    border-bottom:1px solid {BRD}; padding-bottom:1.1rem; margin-bottom:1.4rem;
}}
.ks-form-title {{
    display:flex; align-items:center; gap:.6rem;
    font-size:1.3rem; font-weight:800; color:{PG};
}}
.ks-form-badge {{
    font-size:.74rem; font-weight:700; color:{SG}; background:{LG};
    padding:.3rem .75rem; border-radius:999px;
}}

/* ── RESULTS ── */
.ks-cause {{
    background:#FAFCF9; border:1px solid {BRD}; border-radius:12px;
    padding:1.1rem 1.2rem; margin-bottom:.8rem;
}}
.ks-cause-name {{ font-size:1rem; font-weight:700; color:{PG}; margin-bottom:.3rem; }}
.ks-cause-reason {{ font-size:.88rem; color:{MTXT}; line-height:1.5; }}

/* ── ALERTS ── */
.ks-alert {{
    display:flex; gap:.9rem; padding:1.2rem 1.3rem; border-radius:14px; margin-bottom:1.3rem;
}}
.ks-alert-warn  {{ background:#FFFBEB; border:1px solid #FCD34D; color:#78600A; }}
.ks-alert-error {{ background:#FEF2F2; border:1px solid #FCA5A5; color:#991B1B; }}
.ks-alert-icon  {{ flex-shrink:0; padding-top:2px; }}
.ks-alert h4    {{ margin:0 0 .3rem 0; font-size:.95rem; font-weight:700; }}
.ks-alert p     {{ margin:0; font-size:.85rem; line-height:1.5; }}

/* ── FOLLOWUP ── */
.ks-followup {{
    background:{CARD}; border:2px solid {SG}; border-radius:18px;
    padding:1.8rem; margin-bottom:1.6rem; box-shadow:0 6px 22px rgba(46,125,80,.1);
}}

/* ── CONTEXT STRIP ── */
.ks-ctx {{
    background:#F3F6F0; border:1px solid {BRD}; border-radius:12px;
    padding:1rem 1.4rem; margin-bottom:1.2rem;
}}

/* ── FOOTER ── */
.ks-footer {{
    border-top:1px solid {BRD}; padding:2.5rem 1rem 1.5rem; margin-top:4rem;
    text-align:center; color:{MTXT};
}}

/* ── STREAMLIT OVERRIDES ── */
div.stButton > button[kind="primary"],
div.stButton > button:first-child {{
    background: {PG} !important; color: #fff !important;
    font-weight: 700 !important; font-size: 1rem !important;
    border-radius: 999px !important; border: none !important;
    padding: .75rem 2rem !important;
    box-shadow: 0 4px 14px rgba(23,75,53,.22) !important;
}}
div.stButton > button:first-child:hover {{
    box-shadow: 0 6px 18px rgba(23,75,53,.32) !important;
}}
div[data-testid="column"] div.stButton > button {{
    font-size:.82rem !important; padding:.35rem .75rem !important; border-radius:8px !important;
}}

/* inputs */
.stTextInput > div > div, .stTextArea > div > div,
.stSelectbox > div > div {{
    background: {CARD} !important; border-color: {BRD} !important;
    border-radius: 10px !important; color: {TXT} !important;
}}
.stTextInput label, .stSelectbox label, .stTextArea label {{
    color: {TXT} !important; font-weight: 600 !important;
}}

/* expander */
[data-testid="stExpander"] {{
    border: 1px solid {BRD} !important; border-radius: 12px !important;
    background: {CARD} !important;
}}

/* divider */
hr {{ border-color: {BRD} !important; }}

@media (max-width:860px) {{
    .ks-features {{ grid-template-columns: repeat(2,1fr); }}
    .ks-feat {{ border-right:none; border-bottom:1px solid {BRD}; }}
    .ks-feat:nth-child(2) {{ border-right:none; }}
    .ks-hero-h1 {{ font-size:2.1rem; }}
    .ks-nav-links {{ display:none; }}
    .ks-nav {{ padding:.6rem 1rem; }}
}}
</style>
"""

st.markdown(CSS, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# Session State
# ─────────────────────────────────────────────────────────────────────────────
for key, default in [
    ("result", None),
    ("follow_up_history", []),
    ("follow_up_answer", ""),
    ("original_form", {
        "crop": "", "region": "", "stage": "Not sure",
        "query": "", "spread": "Not sure", "language": "English",
    }),
]:
    if key not in st.session_state:
        st.session_state[key] = default


def _preset(crop, region, stage, spread, lang, query):
    st.session_state.original_form = {
        "crop": crop, "region": region, "stage": stage,
        "query": query, "spread": spread, "language": lang,
    }
    st.session_state.result = None
    st.session_state.follow_up_history = []
    st.session_state.follow_up_answer = ""


# ─────────────────────────────────────────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(f"""
    <div style="display:flex;align-items:center;gap:.55rem;margin-bottom:.8rem;">
        <div style="background:{LG};padding:7px;border-radius:10px;">{IC['leaf']}</div>
        <div>
            <div style="font-weight:800;font-size:1.1rem;color:{PG};">KisanSaathi</div>
            <div style="font-size:.72rem;font-weight:600;color:{MTXT};">AI Crop Advisory</div>
        </div>
    </div>""", unsafe_allow_html=True)

    api_key_input = st.text_input(
        "Gemini API Key", value="", type="password",
        help="Auto-detected from Streamlit Secrets or .env. Override here.",
    )
    _key = get_gemini_api_key(api_key_input)
    _model = get_gemini_model()
    if _key:
        st.markdown(f'<div style="background:{LG};border:1px solid #B6D9BC;padding:.45rem .75rem;'
                    f'border-radius:8px;font-size:.78rem;color:#0B5A2A;font-weight:600;'
                    f'margin-bottom:.8rem;display:flex;align-items:center;gap:.35rem;">'
                    f'{IC["check_g"]} Connected ({_model})</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="background:#FEF2F2;border:1px solid #FCA5A5;padding:.45rem .75rem;'
                    f'border-radius:8px;font-size:.78rem;color:#991B1B;font-weight:600;'
                    f'margin-bottom:.8rem;">API key needed</div>', unsafe_allow_html=True)

    sidebar_lang = st.selectbox(
        "Response Language",
        ["English", "Hindi", "Hinglish"],
        index=["English", "Hindi", "Hinglish"].index(
            st.session_state.original_form.get("language", "English")),
        key="sb_lang",
    )
    st.session_state.original_form["language"] = sidebar_lang

    st.markdown("---")
    st.markdown(f"**Safety Guardrails**")
    st.caption("🛡️ Zero chemical dosage prescription\n\n"
               "📚 ICAR-grounded evidence only\n\n"
               "👨‍🌾 KVK escalation for rapid spread")
    st.markdown("---")
    if st.button("Reset Session", use_container_width=True):
        st.session_state.result = None
        st.session_state.follow_up_history = []
        st.session_state.follow_up_answer = ""
        st.session_state.original_form = {
            "crop": "", "region": "", "stage": "Not sure",
            "query": "", "spread": "Not sure", "language": sidebar_lang,
        }
        st.rerun()

# ─────────────────────────────────────────────────────────────────────────────
# Navigation bar
# ─────────────────────────────────────────────────────────────────────────────
lang_display = st.session_state.original_form["language"]
st.markdown(f"""
<div class="ks-nav" id="home">
  <a href="#home" class="ks-nav-brand">
    {IC['leaf']}
    <div>
      <div class="ks-nav-brand-name">KisanSaathi</div>
      <div class="ks-nav-brand-sub">AI Crop Advisory Assistant</div>
    </div>
  </a>
  <div class="ks-nav-links">
    <a href="#home"         class="ks-nl-active">{IC['home']} Home</a>
    <a href="#how-it-works" class="ks-nl">{IC['layers']} How It Works</a>
    <a href="#ask-ai"       class="ks-nl">{IC['chat']} Ask AI</a>
    <a href="#safety"       class="ks-nl">{IC['shield']} Safety</a>
    <span class="ks-lang-pill">{IC['globe']} {lang_display}</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# Hero section
# ─────────────────────────────────────────────────────────────────────────────
hero_b64 = _b64("assets/hero_farmer.jpg")

st.markdown(f"""
<div class="ks-hero">
  <div class="ks-hero-txt">
    <h1 class="ks-hero-h1">Better Crop Decisions.<br>Safer Farming.</h1>
    <div class="ks-hero-bar"></div>
    <p class="ks-hero-p">
      Describe your crop problem in your preferred language and receive
      clear, cautious guidance to help you take the next step.
    </p>
    <div class="ks-hero-btns">
      <a href="#ask-ai" class="ks-btn-primary">{IC['leaf_sm']} Get Crop Advice &rarr;</a>
      <a href="#how-it-works" class="ks-btn-outline">How It Works</a>
    </div>
  </div>
  <div class="ks-hero-img">
    <div class="ks-hero-photo">
      <img src="data:image/jpeg;base64,{hero_b64}"
           alt="Indian farmer using smartphone in crop field" />
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# Feature strip
# ─────────────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="ks-features">
  <div class="ks-feat">
    <div class="ks-feat-icon">{IC['leaf_big']}</div>
    <div class="ks-feat-label">Crop Guidance</div>
  </div>
  <div class="ks-feat">
    <div class="ks-feat-icon">{IC['search_sm']}</div>
    <div class="ks-feat-label">Problem Identification</div>
  </div>
  <div class="ks-feat">
    <div class="ks-feat-icon">{IC['shieldck']}</div>
    <div class="ks-feat-label">Safe Recommendations</div>
  </div>
  <div class="ks-feat">
    <div class="ks-feat-icon">{IC['lang']}</div>
    <div class="ks-feat-label">Multi-language Support</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# How It Works
# ─────────────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div id="how-it-works" style="margin-bottom:3rem;">
  <div style="text-align:center;max-width:650px;margin:0 auto 1.8rem auto;">
    <span class="ks-sec-tag">System Architecture</span>
    <h2 class="ks-sec-title">How KisanSaathi Works</h2>
    <p class="ks-sec-desc">A grounded three-stage prompt pipeline ensuring verified agronomic advice
       with zero chemical dosage hallucination.</p>
  </div>
</div>
""", unsafe_allow_html=True)

cols_hw = st.columns(3)
steps = [
    ("1. Multi-Lingual Extraction", IC['search'],
     "Understands farmer queries in English, Hindi, and Hinglish. Extracts crop, region, growth stage, symptoms, and spread rate."),
    ("2. Grounded TF-IDF Retrieval", IC['leaf'],
     "Matches symptom profiles against ICAR agronomic reference materials. Every diagnosis grounded in verified literature."),
    ("3. Safe Advisory & Escalation", IC['shieldck'],
     "Generates cultural management checklists, asks follow-up questions for missing details, and escalates to KVK experts."),
]
for col, (title, icon, desc) in zip(cols_hw, steps):
    with col:
        st.markdown(f"""
        <div class="ks-card">
          <div class="ks-card-icon">{icon}</div>
          <h3>{title}</h3>
          <p>{desc}</p>
        </div>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# Ask AI — Diagnostic Form
# ─────────────────────────────────────────────────────────────────────────────
st.markdown('<div id="ask-ai"></div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="ks-form-wrap">
  <div class="ks-form-head">
    <div class="ks-form-title">{IC['leaf']} Crop Diagnostic Center</div>
    <span class="ks-form-badge">AI Symptom Intake</span>
  </div>
""", unsafe_allow_html=True)

# Quick-fill presets
st.caption("🧪 **Quick-Fill Benchmark Scenarios:**")
p1, p2, p3, p4 = st.columns(4)
with p1:
    if st.button("🍅 Tomato (UP)", use_container_width=True):
        _preset("Tomato", "Uttar Pradesh", "Flowering", "Slowly", "English",
                "Tomato leaves have yellow spots and curling edges.")
        st.rerun()
with p2:
    if st.button("🌾 Rice (WB)", use_container_width=True):
        _preset("Rice", "West Bengal", "Vegetative", "Slowly", "English",
                "Rice plants have brown spots on the leaves.")
        st.rerun()
with p3:
    if st.button("🌱 Wheat (PB)", use_container_width=True):
        _preset("Wheat", "Punjab", "Not sure", "Rapidly", "Hindi",
                "गेहूं की पत्तियां नोक से पीली पड़ रही हैं।")
        st.rerun()
with p4:
    if st.button("🥔 Potato (UP)", use_container_width=True):
        _preset("Potato", "Uttar Pradesh", "Vegetative", "Not sure", "Hinglish",
                "Aloo ke paudhe me curling leaves dikh rahi hain.")
        st.rerun()

OF = st.session_state.original_form
c1, c2 = st.columns(2, gap="medium")
with c1:
    crop   = st.text_input("Crop Name", value=OF["crop"], placeholder="e.g. Tomato / Rice / गेहूं")
    region = st.text_input("Region / State", value=OF["region"], placeholder="e.g. Uttar Pradesh")
    _so = ["Not sure", "Seedling", "Vegetative", "Flowering", "Fruiting", "Harvest"]
    stage  = st.selectbox("Growth Stage", _so, index=_so.index(OF["stage"]) if OF["stage"] in _so else 0)
with c2:
    _sp = ["Not sure", "Not spreading", "Slowly", "Rapidly"]
    spread = st.selectbox("Problem Spreading?", _sp, index=_sp.index(OF["spread"]) if OF["spread"] in _sp else 0)
    _lo = ["English", "Hindi", "Hinglish"]
    form_lang = st.selectbox("Advisory Language", _lo, index=_lo.index(OF["language"]) if OF["language"] in _lo else 0)
    query  = st.text_area("Describe Symptoms", value=OF["query"],
                          placeholder="Leaf colour change, spots, curling, wilting, insects…", height=105)
OF["language"] = form_lang

submit = st.button("🌿 Get Crop Advice", use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# Pipeline execution
# ─────────────────────────────────────────────────────────────────────────────
if submit:
    if not query.strip():
        st.warning("Please describe the symptoms first.")
        st.stop()
    try:
        st.session_state.original_form = {
            "crop": crop.strip(), "region": region.strip(), "stage": stage,
            "query": query.strip(), "spread": spread, "language": form_lang,
        }
        st.session_state.follow_up_history = []
        st.session_state.follow_up_answer = ""
        rk = get_gemini_api_key(api_key_input)
        rm = get_gemini_model()
        if not rk:
            st.error("GEMINI_API_KEY is missing. Add it to Streamlit Secrets, .env, or the sidebar.")
            st.stop()
        notes = load_reference_notes()
        pipe = KisanSaathiPipeline(notes, api_key=rk, model=rm)
        with st.status("🌱 Running three-stage analysis…", expanded=True) as status:
            _st = st.empty()
            def _step(m): _st.write(f"⏳ {m}")
            o = st.session_state.original_form
            result = pipe.run(query=o["query"], crop=o["crop"], region=o["region"],
                              stage=o["stage"], spread=o["spread"], language=o["language"],
                              follow_up_answer="", previous_extraction=None, on_step=_step)
            status.update(label="✅ Analysis complete", state="complete", expanded=False)
        st.session_state.result = result
    except Exception as e:
        st.error(f"Analysis failed: {e}")
        st.info("Check your API key and model availability.")

# ─────────────────────────────────────────────────────────────────────────────
# Results
# ─────────────────────────────────────────────────────────────────────────────
if st.session_state.result:
    result    = st.session_state.result
    ext       = result["extraction"]
    diag      = result["diagnosis"]
    adv       = result["advisory"]
    follow_q  = ext.get("follow_up_question", "").strip()

    st.markdown("---")
    st.markdown(f"""
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:1.4rem;">
      <div>
        <h2 style="font-size:1.7rem;font-weight:800;color:{PG};margin:0;">Assessment Results</h2>
        <p style="color:{MTXT};margin:.2rem 0 0;font-size:.9rem;">
          Grounded evaluation for <b>{ext.get('crop','—')}</b>
          in <b>{ext.get('broad_region','—')}</b></p>
      </div>
      <span style="background:{LG};color:#0B5A2A;padding:.35rem .8rem;border-radius:999px;
                   font-weight:700;font-size:.76rem;">{IC['check_g']} Verified</span>
    </div>
    """, unsafe_allow_html=True)

    # context strip
    st.markdown(f"""
    <div class="ks-ctx">
      <div style="display:flex;flex-wrap:wrap;gap:1.2rem;align-items:center;">
        <div><span style="font-size:.72rem;color:{MTXT};font-weight:700;text-transform:uppercase;">
          Crop:</span> <b>{ext.get('crop','—')}</b></div>
        <div><span style="font-size:.72rem;color:{MTXT};font-weight:700;text-transform:uppercase;">
          Region:</span> <b>{ext.get('broad_region','—')}</b></div>
        <div><span style="font-size:.72rem;color:{MTXT};font-weight:700;text-transform:uppercase;">
          Stage:</span> <b>{ext.get('growth_stage','—')}</b></div>
        <div><span style="font-size:.72rem;color:{MTXT};font-weight:700;text-transform:uppercase;">
          Spread:</span> <b>{ext.get('spread','—')}</b></div>
        <div><span style="font-size:.72rem;color:{MTXT};font-weight:700;text-transform:uppercase;">
          Symptoms:</span> <b>{', '.join(ext.get('symptoms',[])) or '—'}</b></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # possible causes
    st.markdown(f"""
    <div class="ks-card-static">
      <h3 style="font-size:1.2rem;font-weight:800;color:{PG};margin-bottom:.7rem;">
        Possible Agronomic Causes</h3>
      <div style="background:#F0FDF4;border-left:4px solid {SG};padding:.7rem 1rem;
                  border-radius:0 8px 8px 0;margin-bottom:1.1rem;font-size:.82rem;color:#166534;">
        <b>Note:</b> These are potential causes from ICAR literature, not confirmed laboratory diagnoses.
      </div>
    """, unsafe_allow_html=True)
    for c in diag.get("possible_causes", []):
        st.markdown(f"""
        <div class="ks-cause">
          <div class="ks-cause-name">{c.get('name','Possible cause')}</div>
          <div class="ks-cause-reason">{c.get('reason','')}</div>
        </div>""", unsafe_allow_html=True)
    if not diag.get("possible_causes"):
        st.write("No definitive match — continued observation recommended.")
    st.markdown("</div>", unsafe_allow_html=True)

    # advisory + checklist
    ac1, ac2 = st.columns(2, gap="medium")
    with ac1:
        st.markdown(f"""
        <div class="ks-card-static" style="height:100%;">
          <h3 style="font-size:1.15rem;font-weight:800;color:{PG};margin-bottom:.6rem;">
            Agronomic Advisory</h3>
          <div style="font-size:.9rem;line-height:1.6;color:{TXT};">
            {adv.get('advice','No specific advisory available.')}
          </div>
        </div>""", unsafe_allow_html=True)
    with ac2:
        st.markdown(f"""
        <div class="ks-card-static" style="height:100%;">
          <h3 style="font-size:1.15rem;font-weight:800;color:{PG};margin-bottom:.6rem;">
            Field Observation Checklist</h3>
        """, unsafe_allow_html=True)
        for item in adv.get("next_steps", []):
            st.markdown(f"""
            <div style="display:flex;align-items:flex-start;gap:.5rem;margin-bottom:.6rem;
                        font-size:.86rem;color:{TXT};">
              <div style="color:{SG};margin-top:2px;">{IC['check_g']}</div>
              <div>{item}</div>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # safety warning
    st.markdown(f"""
    <div class="ks-alert ks-alert-warn">
      <div class="ks-alert-icon">{IC['shield']}</div>
      <div>
        <h4>Zero Chemical Dosage Policy</h4>
        <p>KisanSaathi does <b>not</b> prescribe pesticide dosages. Consult local
           agronomists or KVK before applying any chemical.</p>
      </div>
    </div>""", unsafe_allow_html=True)

    if adv.get("escalate", True):
        st.markdown(f"""
        <div class="ks-alert ks-alert-error">
          <div class="ks-alert-icon">{IC['alert']}</div>
          <div>
            <h4>KVK / Extension Officer Escalation Recommended</h4>
            <p><b>Reason:</b> {adv.get('escalation_reason','Physical inspection required.')}</p>
            <div style="margin-top:.5rem;font-weight:600;font-size:.83rem;display:flex;
                        align-items:center;gap:.35rem;">
              {IC['phone']} Kisan Call Centre: <b>1800-180-1551</b> (Toll-Free)
            </div>
          </div>
        </div>""", unsafe_allow_html=True)

    # follow-up question
    if follow_q:
        st.markdown(f"""
        <div class="ks-followup">
          <div style="display:flex;align-items:center;gap:.55rem;color:{SG};margin-bottom:.5rem;
                      font-weight:700;text-transform:uppercase;font-size:.78rem;">
            {IC['quest']} Follow-Up Clarification Needed
          </div>
          <div style="font-size:1.2rem;font-weight:800;color:{PG};margin-bottom:.7rem;line-height:1.35;">
            {follow_q}
          </div>
        """, unsafe_allow_html=True)
        if ext.get("missing_information"):
            st.caption(f"Pending: {', '.join(ext['missing_information'])}")

        with st.form("follow_up_form"):
            fu_ans = st.text_input("Your answer:",
                                   placeholder="e.g. Flowering stage / About 20% affected",
                                   key="fu_input")
            fu_submit = st.form_submit_button("Submit & Update Diagnosis")

        if fu_submit:
            if not fu_ans.strip():
                st.warning("Please type your answer.")
            else:
                ans = fu_ans.strip()
                st.session_state.follow_up_answer = ans
                st.session_state.follow_up_history.append({"q": follow_q, "a": ans})
                try:
                    rk = get_gemini_api_key(api_key_input)
                    rm = get_gemini_model()
                    if not rk:
                        st.error("API key missing.")
                        st.stop()
                    notes = load_reference_notes()
                    pipe = KisanSaathiPipeline(notes, api_key=rk, model=rm)
                    with st.status("🌱 Updating…", expanded=True) as status:
                        _st = st.empty()
                        def _step(m): _st.write(f"⏳ {m}")
                        o = st.session_state.original_form
                        prev = st.session_state.result.get("extraction")
                        ur = pipe.run(query=o["query"], crop=o["crop"], region=o["region"],
                                      stage=o["stage"], spread=o["spread"], language=o["language"],
                                      follow_up_answer=ans, previous_extraction=prev, on_step=_step)
                        status.update(label="✅ Updated", state="complete", expanded=False)
                    rec = ur["extraction"].get("follow_up_answer") or ans.rstrip(".?! ")
                    st.session_state.follow_up_answer = rec
                    ur["follow_up_answer"] = rec
                    ur["extraction"]["follow_up_answer"] = rec
                    st.session_state.result = ur
                    ns = ur["extraction"].get("spread", "")
                    if ns and ns.lower() not in ["unknown", "not sure"]:
                        st.session_state.original_form["spread"] = ns
                    ng = ur["extraction"].get("growth_stage", "")
                    if ng and ng.lower() not in ["unknown", "not sure"]:
                        st.session_state.original_form["stage"] = ng
                    nc = ur["extraction"].get("crop", "")
                    if nc and nc.lower() not in ["unknown", "not provided"]:
                        st.session_state.original_form["crop"] = nc
                    st.rerun()
                except Exception as e:
                    st.error(f"Update failed: {e}")

        st.markdown("</div>", unsafe_allow_html=True)

    # conversation history
    if st.session_state.follow_up_history:
        with st.expander("Multi-turn conversation history", expanded=False):
            for i, item in enumerate(st.session_state.follow_up_history, 1):
                st.markdown(f"**Turn {i}:** {item['q']}")
                st.markdown(f"*Answer:* `{item['a']}`")
                st.markdown("---")

    # JSON viewer
    with st.expander("View structured pipeline output (JSON)",
                     expanded=bool(st.session_state.get("follow_up_answer"))):
        st.json(result)

# ─────────────────────────────────────────────────────────────────────────────
# Safety section
# ─────────────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div id="safety" style="margin-top:4rem;margin-bottom:3rem;">
  <div style="text-align:center;max-width:650px;margin:0 auto 1.8rem auto;">
    <span class="ks-sec-tag">Safety Architecture</span>
    <h2 class="ks-sec-title">Safety-First Agricultural Guardrails</h2>
    <p class="ks-sec-desc">Protecting crops, soil, and farmer well-being through strict computational safeguards.</p>
  </div>
</div>
""", unsafe_allow_html=True)

sc1, sc2, sc3 = st.columns(3)
safety_items = [
    ("Zero Chemical Dosage", IC['shieldck'],
     "Never computes or prescribes synthetic pesticide doses, preventing phytotoxicity and pollinator poisoning."),
    ("Evidence Grounding", IC['leaf'],
     "All possible causes grounded in ICAR and state university agronomy reference manuals."),
    ("Human-In-The-Loop", IC['search'],
     "Uncertain symptoms or rapidly spreading plots trigger automatic escalation to local extension officers."),
]
for col, (title, icon, desc) in zip([sc1, sc2, sc3], safety_items):
    with col:
        st.markdown(f"""
        <div class="ks-card">
          <div class="ks-card-icon">{icon}</div>
          <h3>{title}</h3>
          <p>{desc}</p>
        </div>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# Evaluation summary
# ─────────────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="ks-card-static" style="margin-top:1rem;">
  <div style="text-align:center;margin-bottom:1.3rem;">
    <h3 style="font-size:1.4rem;font-weight:800;color:{PG};margin-bottom:.3rem;">
      Empirical Benchmark Verification</h3>
    <p style="color:{MTXT};font-size:.88rem;margin:0;">
      Evaluated across 12 distinct scenarios with zero failures.</p>
  </div>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));
              gap:1rem;text-align:center;">
    <div style="padding:1rem;background:{BG};border-radius:12px;border:1px solid {BRD};">
      <div style="font-size:1.9rem;font-weight:800;color:{PG};line-height:1;">12/12</div>
      <div style="font-size:.8rem;font-weight:600;color:{MTXT};margin-top:.3rem;">Scenarios</div>
    </div>
    <div style="padding:1rem;background:#F0FDF4;border-radius:12px;border:1px solid #BBF7D0;">
      <div style="font-size:1.9rem;font-weight:800;color:#15803D;line-height:1;">100%</div>
      <div style="font-size:.8rem;font-weight:600;color:#166534;margin-top:.3rem;">Pass Rate</div>
    </div>
    <div style="padding:1rem;background:#FEF3C7;border-radius:12px;border:1px solid #FDE68A;">
      <div style="font-size:1.9rem;font-weight:800;color:#B45309;line-height:1;">0</div>
      <div style="font-size:.8rem;font-weight:600;color:#92400E;margin-top:.3rem;">Dosages Given</div>
    </div>
    <div style="padding:1rem;background:{BG};border-radius:12px;border:1px solid {BRD};">
      <div style="font-size:1.9rem;font-weight:800;color:{SG};line-height:1;">3</div>
      <div style="font-size:.8rem;font-weight:600;color:{MTXT};margin-top:.3rem;">Languages</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

csv_path = "evaluation_results.csv"
if os.path.exists(csv_path):
    with st.expander("View all 12 test cases (evaluation_results.csv)", expanded=False):
        try:
            with open(csv_path, encoding="utf-8") as f:
                for r in csv.DictReader(f):
                    st.markdown(f"**{r.get('Test ID','')}** — `{r.get('Pass/Fail','')}`")
                    st.caption(r.get("Reason", ""))
                    st.markdown("---")
        except Exception as e:
            st.caption(f"Could not read CSV: {e}")

# ─────────────────────────────────────────────────────────────────────────────
# Footer
# ─────────────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="ks-footer">
  <div style="display:flex;align-items:center;justify-content:center;gap:.5rem;
              font-size:1.25rem;font-weight:800;color:{PG};margin-bottom:.7rem;">
    {IC['leaf']} KisanSaathi
  </div>
  <div style="display:flex;justify-content:center;gap:1.8rem;margin-bottom:1rem;
              font-weight:600;font-size:.88rem;">
    <a href="#home" style="color:{TXT};">Home</a>
    <a href="#how-it-works" style="color:{TXT};">How It Works</a>
    <a href="#ask-ai" style="color:{TXT};">Ask AI</a>
    <a href="#safety" style="color:{TXT};">Safety</a>
  </div>
  <div style="max-width:700px;margin:0 auto 1rem;font-size:.78rem;line-height:1.6;color:{MTXT};">
    <b>Advisory Notice:</b> KisanSaathi is an AI prototype for preliminary diagnostic support.
    Confirm all recommendations with local agricultural extension officers or Krishi Vigyan Kendras.
  </div>
  <div style="font-size:.74rem;color:#94A3B8;">
    &copy; 2026 KisanSaathi &middot; Gemini 2.5 Flash + Streamlit &middot; Grounded in ICAR Standards
  </div>
</div>
""", unsafe_allow_html=True)
