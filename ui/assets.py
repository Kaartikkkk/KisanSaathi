"""Vector assets and SVG icon library for KisanSaathi UI.
All SVGs are rendered inline for maximum sharpness, zero network latency, and high DPI.
Features consistent 24x24 viewBox and 2.0px stroke-width line styling.
"""

def svg_icon(inner_svg: str, size: int = 18, color: str = "#174B35", sw: float = 2.0) -> str:
    """Render an inline SVG icon wrapper."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" '
        f'viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" '
        f'stroke-linecap="round" stroke-linejoin="round" class="ks-svg-icon">{inner_svg}</svg>'
    )

# Clean, professional vector path definitions (24x24 viewBox)
P_LEAF = '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>'
P_SHIELD = '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>'
P_SHIELD_CHECK = '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/>'
P_SEARCH = '<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>'
P_CHECK = '<polyline points="20 6 9 17 4 12"/>'
P_ALERT = '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>'
P_PHONE = '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>'
P_GLOBE = '<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>'
P_HOME = '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>'
P_LAYERS = '<polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>'
P_CHAT = '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>'
P_BOOK = '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>'
P_CLIPBOARD = '<path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/><path d="M9 14l2 2 4-4"/>'
P_PIN = '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>'
P_SPROUT = '<path d="M7 20h10"/><path d="M10 20c5.5-2.5.8-6.4 3-10"/><path d="M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5.4-4.8-.3-1.2-.6-2.3-1.9-3-4.2 2.8-.5 4.4.1 5.5.8z"/><path d="M14.1 6a7 7 0 0 0-1.1 4c1.9-.1 3.3-.6 4.3-1.4 1-1 1.6-2.3 1.7-4.6-2.7.1-4.1 1-4.9 2z"/>'
P_ACTIVITY = '<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>'
P_USER = '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>'
P_BOT = '<rect x="3" y="11" width="18" height="10" rx="2"/><circle cx="12" cy="5" r="2"/><path d="M12 7v4"/><line x1="8" y1="16" x2="8" y2="16"/><line x1="16" y1="16" x2="16" y2="16"/>'
P_RESET = '<path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><polyline points="3 3 3 8 8 8"/>'
P_ARROW_RIGHT = '<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>'
P_LANG = '<path d="m5 8 6 6"/><path d="m4 14 6-6 2-3"/><path d="M2 5h12"/><path d="M7 2h1"/><path d="m22 22-5-10-5 10"/><path d="M14 18h6"/>'
P_CHART = '<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/>'

ICONS = {
    "leaf_brand": svg_icon(P_LEAF, 26, "#174B35", 2.2),
    "leaf_primary": svg_icon(P_LEAF, 18, "#174B35", 2.0),
    "leaf_white": svg_icon(P_LEAF, 16, "#FFFFFF", 2.0),
    "shield_green": svg_icon(P_SHIELD, 20, "#174B35", 2.0),
    "shield_check": svg_icon(P_SHIELD_CHECK, 20, "#174B35", 2.0),
    "search": svg_icon(P_SEARCH, 20, "#174B35", 2.0),
    "check_green": svg_icon(P_CHECK, 16, "#0B5A2A", 2.4),
    "check_pill": svg_icon(P_CHECK, 14, "#0B5A2A", 2.2),
    "alert_amber": svg_icon(P_ALERT, 20, "#B45309", 2.0),
    "phone": svg_icon(P_PHONE, 18, "#0B5A2A", 2.0),
    "globe": svg_icon(P_GLOBE, 15, "#174B35", 2.0),
    "home": svg_icon(P_HOME, 16, "#174B35", 2.0),
    "layers": svg_icon(P_LAYERS, 16, "#174B35", 2.0),
    "chat": svg_icon(P_CHAT, 16, "#174B35", 2.0),
    "book": svg_icon(P_BOOK, 18, "#174B35", 2.0),
    "clipboard": svg_icon(P_CLIPBOARD, 18, "#174B35", 2.0),
    "pin": svg_icon(P_PIN, 18, "#174B35", 2.0),
    "sprout": svg_icon(P_SPROUT, 18, "#174B35", 2.0),
    "activity": svg_icon(P_ACTIVITY, 18, "#174B35", 2.0),
    "user": svg_icon(P_USER, 16, "#166534", 2.0),
    "bot": svg_icon(P_BOT, 16, "#174B35", 2.0),
    "reset": svg_icon(P_RESET, 15, "#174B35", 2.0),
    "arrow_right": svg_icon(P_ARROW_RIGHT, 16, "#FFFFFF", 2.2),
    "language": svg_icon(P_LANG, 18, "#174B35", 2.0),
    "chart": svg_icon(P_CHART, 18, "#174B35", 2.0),
}

# Corner foliage leaf branch overlay
CORNER_LEAF_BRANCH_SVG = """
<svg class="ks-corner-foliage-svg" viewBox="0 0 180 140" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M190 -10 C 140 20, 90 50, 40 100" stroke="#7BA887" stroke-width="2.5" stroke-linecap="round" opacity="0.6"/>
    <path d="M140 15 C 160 5, 165 -15, 148 -10 C 132 -6, 128 10, 140 15 Z" fill="#7BA887" opacity="0.55"/>
    <path d="M105 35 C 120 22, 115 5, 98 12 C 86 18, 92 34, 105 35 Z" fill="#6B9978" opacity="0.6"/>
    <path d="M75 60 C 88 45, 78 30, 62 38 C 50 45, 58 60, 75 60 Z" fill="#7BA887" opacity="0.55"/>
    <path d="M125 45 C 140 55, 148 42, 138 30 C 125 22, 115 35, 125 45 Z" fill="#6B9978" opacity="0.5"/>
    <path d="M90 75 C 102 88, 115 78, 108 65 C 98 55, 82 65, 90 75 Z" fill="#7BA887" opacity="0.55"/>
    <path d="M50 85 C 60 98, 72 88, 66 75 C 58 65, 42 75, 50 85 Z" fill="#6B9978" opacity="0.6"/>
</svg>
"""

# Bottom Organic Wave SVG (Single unified landscape wave)
BOTTOM_ORGANIC_WAVE_SVG = """
<div class="ks-bottom-wave-wrap" style="width:100%; overflow:hidden; line-height:0; margin-top:3rem; margin-bottom:-2.5rem;">
    <svg viewBox="0 0 1440 90" fill="none" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto;" preserveAspectRatio="none">
        <path d="M0 45 C 360 85, 720 15, 1080 65 C 1260 85, 1380 60, 1440 50 L 1440 90 L 0 90 Z" fill="#E8F2E9" opacity="0.7"/>
        <path d="M0 65 C 400 95, 800 35, 1200 75 L 1440 60 L 1440 90 L 0 90 Z" fill="#DCEDDE" opacity="0.85"/>
    </svg>
</div>
"""
