"""Central Visual Asset Library for KisanSaathi.
Integrates the complete KisanSaathi Visual Asset Pack:
- Logos (mark, horizontal, wordmark)
- 25+ Outline SVG icons (FEATHER / LUCIDE standard line styling)
- 3 Vector Illustrations (no-chemical, evidence-book, human-escalation)
- 3 Decorative agricultural SVGs (leaf-branch, crop-rows, field-hills)
- Status badge SVGs (pass, fail, caution, info)
- 4 High-Resolution genuine agricultural photographs (farmer-using-phone, farm-landscape, crop-variety, farmer-in-field)
"""

import os
import base64
from functools import lru_cache

# Path to the assets folder relative to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

def clean_html(html_str: str) -> str:
    """Clean HTML string by stripping leading whitespace from all lines.
    
    Prevents Markdown parsers (like markdown-it-py) from ever interpreting 
    indented HTML or comments as <pre><code> code blocks.
    """
    if not html_str:
        return ""
    return "\n".join(line.strip() for line in html_str.splitlines() if line.strip())

@lru_cache(maxsize=128)
def load_raw_svg(rel_path: str) -> str:
    """Read an SVG file from disk and return its clean text content."""
    full_path = os.path.join(ASSETS_DIR, rel_path)
    if not os.path.exists(full_path):
        # Fallback to direct relative path if called from different cwd
        full_path = os.path.join("assets", rel_path)
    if os.path.exists(full_path):
        with open(full_path, "r", encoding="utf-8") as f:
            return f.read().strip()
    return ""

def get_svg_icon(icon_name: str, size: int = 18, color: str = "currentColor", stroke_width: float = 1.8, extra_style: str = "") -> str:
    """Return inline SVG icon markup with specified size, stroke color, and stroke-width."""
    svg_raw = load_raw_svg(f"icons/{icon_name}.svg")
    if not svg_raw:
        # Check in root assets if not in icons/
        svg_raw = load_raw_svg(f"{icon_name}.svg")
    if not svg_raw:
        return ""
    
    # Replace standard attributes if needed or inject inline styles
    style_attr = f'style="width:{size}px; height:{size}px; stroke:{color}; stroke-width:{stroke_width}; vertical-align:middle; display:inline-block; flex-shrink:0; {extra_style}"'
    if "<svg " in svg_raw:
        svg_styled = svg_raw.replace("<svg ", f'<svg {style_attr} class="ks-svg-icon" ')
        return svg_styled
    return svg_raw

@lru_cache(maxsize=16)
def get_image_base64(filename: str) -> str:
    """Read a local JPG/PNG from assets/images/ (or assets/) and return as base64 data URI."""
    paths_to_try = [
        os.path.join(ASSETS_DIR, "images", filename),
        os.path.join(ASSETS_DIR, filename),
        os.path.join("assets", "images", filename),
        os.path.join("assets", filename),
    ]
    for p in paths_to_try:
        if os.path.exists(p):
            with open(p, "rb") as f:
                data = base64.b64encode(f.read()).decode("utf-8")
                mime = "image/png" if filename.lower().endswith(".png") else "image/jpeg"
                return f"data:{mime};base64,{data}"
    return ""

class SafeDict(dict):
    """Dictionary that returns empty string or tries to load missing icons without ever raising KeyError."""
    def __init__(self, *args, fallback_loader=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fallback_loader = fallback_loader

    def __missing__(self, key):
        if self.fallback_loader:
            try:
                res = self.fallback_loader(key)
                if res:
                    self[key] = res
                    return res
            except Exception:
                pass
        return ""

# -----------------------------------------------------------------------------
# Pre-rendered Logos
# -----------------------------------------------------------------------------
LOGOS = SafeDict({
    "horizontal": load_raw_svg("logos/kisansaathi-horizontal.svg"),
    "mark": load_raw_svg("logos/kisansaathi-mark.svg"),
    "wordmark": load_raw_svg("logos/kisansaathi-wordmark.svg"),
})

# -----------------------------------------------------------------------------
# Pre-rendered Illustrations
# -----------------------------------------------------------------------------
ILLUSTRATIONS = SafeDict({
    "no_chemical": load_raw_svg("illustrations/no-chemical.svg"),
    "evidence_book": load_raw_svg("illustrations/evidence-book.svg"),
    "human_escalation": load_raw_svg("illustrations/human-escalation.svg"),
})

# -----------------------------------------------------------------------------
# Pre-rendered Decorative Agricultural SVGs
# -----------------------------------------------------------------------------
DECORATIVE = SafeDict({
    "leaf_branch": load_raw_svg("decorative/leaf-branch.svg"),
    "crop_rows": load_raw_svg("decorative/crop-rows.svg"),
    "field_hills": load_raw_svg("decorative/field-hills.svg"),
})

# -----------------------------------------------------------------------------
# Pre-rendered Status Badges
# -----------------------------------------------------------------------------
BADGES = SafeDict({
    "pass": load_raw_svg("pass.svg"),
    "fail": load_raw_svg("fail.svg"),
    "caution": load_raw_svg("caution.svg"),
    "info": load_raw_svg("info.svg"),
})

# -----------------------------------------------------------------------------
# Central Icon Dictionary (FEATHER / LUCIDE 24x24 standard line styling)
# -----------------------------------------------------------------------------
ICONS = SafeDict({
    # Brand / Navigation
    "leaf_brand": get_svg_icon("leaf", size=24, color="#174B35", stroke_width=2.0),
    "home": get_svg_icon("home", size=16, color="#174B35", stroke_width=1.8),
    "layers": get_svg_icon("layers", size=16, color="#174B35", stroke_width=1.8),
    "leaf_primary": get_svg_icon("leaf", size=18, color="#174B35", stroke_width=1.8),
    "leaf_white": get_svg_icon("leaf", size=16, color="#FFFFFF", stroke_width=2.0),
    "shield_check": get_svg_icon("shield-check", size=18, color="#174B35", stroke_width=1.8),
    "chart": get_svg_icon("chart", size=16, color="#174B35", stroke_width=1.8),
    "globe": get_svg_icon("globe", size=15, color="#174B35", stroke_width=1.8),

    # Form Fields & Diagnostics
    "sprout": get_svg_icon("sprout", size=18, color="#174B35", stroke_width=1.8),
    "map_pin": get_svg_icon("map-pin", size=18, color="#174B35", stroke_width=1.8),
    "alert_triangle": get_svg_icon("alert-triangle", size=18, color="#B45309", stroke_width=1.8),
    "alert_amber": get_svg_icon("alert-triangle", size=18, color="#B45309", stroke_width=1.8),
    "language": get_svg_icon("language", size=18, color="#174B35", stroke_width=1.8),
    "message": get_svg_icon("message", size=18, color="#174B35", stroke_width=1.8),
    "clipboard_check": get_svg_icon("clipboard-check", size=18, color="#174B35", stroke_width=1.8),
    "refresh": get_svg_icon("refresh", size=15, color="#174B35", stroke_width=1.8),
    "play_circle": get_svg_icon("play-circle", size=18, color="#FFFFFF", stroke_width=2.0),
    "user": get_svg_icon("users", size=16, color="#174B35", stroke_width=1.8),
    "bot": get_svg_icon("sprout", size=16, color="#174B35", stroke_width=1.8),

    # Safety & Advisory
    "flask_ban": get_svg_icon("flask-ban", size=20, color="#174B35", stroke_width=1.8),
    "flask": get_svg_icon("flask", size=18, color="#174B35", stroke_width=1.8),
    "book": get_svg_icon("book", size=18, color="#174B35", stroke_width=1.8),
    "users": get_svg_icon("users", size=18, color="#174B35", stroke_width=1.8),
    "phone": get_svg_icon("phone", size=18, color="#0B5A2A", stroke_width=1.8),
    "check_circle": get_svg_icon("check-circle", size=16, color="#0B5A2A", stroke_width=2.0),
    "check_green": get_svg_icon("check-circle", size=16, color="#0B5A2A", stroke_width=2.0),
    "x_circle": get_svg_icon("x-circle", size=16, color="#C62828", stroke_width=2.0),
    "award": get_svg_icon("award", size=20, color="#174B35", stroke_width=1.8),
    "search": get_svg_icon("search", size=18, color="#174B35", stroke_width=1.8),
    "download": get_svg_icon("download", size=16, color="#174B35", stroke_width=1.8),
    "info": get_svg_icon("info", size=16, color="#174B35", stroke_width=1.8),
    "arrow_right": '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
}, fallback_loader=lambda k: get_svg_icon(k.replace('_', '-')) or get_svg_icon('info') or '')

# Corner Foliage Accent SVG using the supplied decorative leaf branch
CORNER_LEAF_BRANCH_SVG = f"""
<div class="ks-corner-foliage-svg" style="position:absolute; top:0; right:0; width:150px !important; height:90px !important; pointer-events:none; z-index:1; opacity:0.65; overflow:hidden;">
    {DECORATIVE['leaf_branch']}
</div>
"""

# Bottom Organic Wave SVG
BOTTOM_ORGANIC_WAVE_SVG = """
<div class="ks-bottom-wave-wrap" style="width:100%; overflow:hidden; line-height:0; margin-top:2.5rem; margin-bottom:-2rem;">
    <svg viewBox="0 0 1440 80" fill="none" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto;" preserveAspectRatio="none">
        <path d="M0 35 C 360 75, 720 10, 1080 55 C 1260 75, 1380 50, 1440 40 L 1440 80 L 0 80 Z" fill="#E8F2E9" opacity="0.65"/>
        <path d="M0 55 C 400 85, 800 25, 1200 65 L 1440 50 L 1440 80 L 0 80 Z" fill="#DCEDDE" opacity="0.8"/>
    </svg>
</div>
"""
