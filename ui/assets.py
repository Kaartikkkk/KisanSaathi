"""Vector assets and SVG icon library for KisanSaathi UI.
All SVGs are rendered inline for maximum sharpness, zero network latency, and high DPI.
"""

# Path strings for common icon shapes
P_LEAF = '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>'
P_SHIELD = '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>'
P_SHIELD_CHECK = '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/>'
P_SEARCH = '<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>'
P_CHECK = '<polyline points="20 6 9 17 4 12"/>'
P_ALERT = '<circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/>'
P_PHONE = '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>'
P_GLOBE = '<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>'
P_HOME = '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>'
P_LAYERS = '<polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>'
P_CHAT = '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>'

def svg_icon(inner_svg: str, size: int = 18, color: str = "#174B35", sw: float = 2.0) -> str:
    """Render an inline SVG icon wrapper."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" '
        f'viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" '
        f'stroke-linecap="round" stroke-linejoin="round">{inner_svg}</svg>'
    )

ICONS = {
    "leaf_brand": svg_icon(P_LEAF, 26, "#174B35", 2.2),
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

# Bottom Organic Wave SVG
BOTTOM_ORGANIC_WAVE_SVG = """
<div class="ks-bottom-wave-wrap">
    <svg viewBox="0 0 1440 80" fill="none" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
        <path d="M0,45 C320,80 640,15 960,50 C1200,75 1360,35 1440,45 L1440,80 L0,80 Z" fill="#EBF3EB" opacity="0.85"/>
        <path d="M0,60 C400,30 800,75 1200,45 C1320,35 1380,55 1440,50 L1440,80 L0,80 Z" fill="#E2EEE3" opacity="0.95"/>
    </svg>
</div>
"""
