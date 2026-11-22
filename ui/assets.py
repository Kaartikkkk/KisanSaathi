"""Central Visual Asset Library for KisanSaathi.
Integrates the complete KisanSaathi Visual Asset Pack:
- Logos (emblem, horizontal, mark, wordmark)
- Outline SVG icons (FEATHER / LUCIDE standard line styling)
- Vector Illustrations (no-chemical, evidence-book, human-escalation)
- Decorative agricultural SVGs (leaf-branch, crop-rows, field-hills)
- Status badges (pass, fail, caution, info)
- High-Resolution genuine agricultural photographs (farmer-using-phone, countryside-horizon)
"""

import os
import base64
from functools import lru_cache

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
        full_path = os.path.join("assets", rel_path)
    if os.path.exists(full_path):
        with open(full_path, "r", encoding="utf-8") as f:
            return f.read().strip()
    return ""

def get_svg_icon(icon_name: str, size: int = 18, color: str = "currentColor", stroke_width: float = 1.8, extra_style: str = "") -> str:
    """Return inline SVG icon markup with specified size, stroke color, and stroke-width."""
    svg_raw = load_raw_svg(f"icons/{icon_name}.svg")
    if not svg_raw:
        svg_raw = load_raw_svg(f"{icon_name}.svg")
    if not svg_raw:
        return ""
    
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
        os.path.join(ASSETS_DIR, "logos", filename),
        os.path.join(ASSETS_DIR, filename),
        os.path.join("assets", "images", filename),
        os.path.join("assets", "logos", filename),
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

    def __getitem__(self, key):
        if key not in self:
            return self.__missing__(key)
        return super().__getitem__(key)

    def get(self, key, default=""):
        if key in self:
            return super().get(key, default)
        val = self.__missing__(key)
        return val if val else (default or "")

# -----------------------------------------------------------------------------
# Pre-rendered Logos
# -----------------------------------------------------------------------------
icon_b64 = get_image_base64("kisansaathi-icon.png")
full_logo_b64 = get_image_base64("kisansaathi-full-logo.png")

LOGOS = SafeDict({
    "icon": f'<img src="{icon_b64}" alt="KisanSaathi Icon" style="width:100%; height:100%; object-fit:contain; display:block;" />',
    "full": f'<img src="{full_logo_b64}" alt="KisanSaathi" style="width:100%; height:100%; object-fit:contain; display:block;" />',
    "emblem": f'<img src="{full_logo_b64}" alt="KisanSaathi" style="width:100%; height:100%; object-fit:contain; display:block;" />',
    "mark": f'<img src="{icon_b64}" alt="KisanSaathi Icon" style="width:100%; height:100%; object-fit:contain; display:block;" />',
    "horizontal": load_raw_svg("logos/kisansaathi-horizontal.svg"),
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
# Central Icon Dictionary (FEATHER / LUCIDE standard line styling)
# -----------------------------------------------------------------------------
ICONS = SafeDict({
    # Brand / Navigation
    "leaf_brand": get_svg_icon("leaf", size=24, color="#124C36", stroke_width=2.0),
    "home": get_svg_icon("home", size=16, color="#124C36", stroke_width=1.8),
    "message": get_svg_icon("message", size=16, color="#124C36", stroke_width=1.8),
    "layers": get_svg_icon("layers", size=16, color="#124C36", stroke_width=1.8),
    "leaf_primary": get_svg_icon("leaf", size=18, color="#124C36", stroke_width=1.8),
    "leaf_white": get_svg_icon("leaf", size=16, color="#FFFFFF", stroke_width=2.0),
    "shield_check": get_svg_icon("shield-check", size=18, color="#124C36", stroke_width=1.8),
    "chart": get_svg_icon("chart", size=16, color="#124C36", stroke_width=1.8),
    "globe": get_svg_icon("globe", size=15, color="#124C36", stroke_width=1.8),
    "search": get_svg_icon("search", size=18, color="#124C36", stroke_width=2.0),
    "sprout": get_svg_icon("sprout", size=18, color="#124C36", stroke_width=2.0),
    "language": get_svg_icon("language", size=18, color="#124C36", stroke_width=1.8),
    "flask_ban": get_svg_icon("flask-ban", size=18, color="#124C36", stroke_width=1.8),
    "book": get_svg_icon("book", size=18, color="#124C36", stroke_width=1.8),
    "users": get_svg_icon("users", size=18, color="#124C36", stroke_width=1.8),
    "check_circle": get_svg_icon("check-circle", size=16, color="#15803D", stroke_width=2.0),
    "check_green": get_svg_icon("check-circle", size=16, color="#15803D", stroke_width=2.0),
    "alert_triangle": get_svg_icon("alert-triangle", size=16, color="#B45309", stroke_width=1.8),
    "alert_amber": get_svg_icon("alert-triangle", size=18, color="#B45309", stroke_width=1.8),
    "phone": get_svg_icon("phone", size=20, color="#DC2626", stroke_width=1.8),
    "play": get_svg_icon("play-circle", size=16, color="#124C36", stroke_width=1.8),
    "refresh": get_svg_icon("refresh", size=14, color="#124C36", stroke_width=1.8),
    "download": get_svg_icon("download", size=15, color="#124C36", stroke_width=1.8),
    "user": get_svg_icon("users", size=15, color="#166534", stroke_width=1.8),
    "bot": get_svg_icon("sprout", size=15, color="#124C36", stroke_width=1.8),
})
