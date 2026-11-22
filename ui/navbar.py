"""Navbar component for KisanSaathi.
Renders edge-to-edge top navigation bar matching the target reference design:
- Left: Leaf logo + KisanSaathi brand name + AI Crop Advisory Assistant subtitle + vertical divider
- Center: Centered slot reserved for native Streamlit tabs
- Right: Language selector pill with globe icon and dropdown indicator
"""

import streamlit as st
from ui.assets import LOGOS, ICONS, clean_html

def render_top_navbar(language: str = "English"):
    """Render the pinned top navbar."""
    nav_html = f"""
    <div class="ks-navbar">
        <div class="ks-nav-left">
            <div class="ks-nav-brand" title="KisanSaathi Home">
                <div class="ks-nav-logo-box">
                    {LOGOS['mark']}
                </div>
                <div class="ks-nav-brand-text">
                    <span class="ks-brand-title">KisanSaathi</span>
                    <span class="ks-brand-subtitle">AI Crop Advisory Assistant</span>
                </div>
            </div>
            <div class="ks-nav-divider"></div>
        </div>

        <!-- Center slot reserved for the native Streamlit tab buttons -->
        <div class="ks-nav-tabs-slot" style="flex:1; max-width:680px; height:42px; margin:0 auto; pointer-events:none;"></div>

        <div class="ks-nav-lang">
            <span class="ks-lang-pill">{ICONS['globe']} {language} &#9662;</span>
        </div>
    </div>
    <!-- Client-side script to clear lingering heading anchor hashes, inject tab icons, and guarantee scroll-to-top on tab switches -->
    <img src="x" style="display:none;" onerror="
        try {{
            if (window.location.hash) {{
                history.replaceState(null, null, window.location.pathname + window.location.search);
            }}
            function resetAllScroll() {{
                window.scrollTo(0, 0);
                if (document.documentElement) document.documentElement.scrollTop = 0;
                if (document.body) document.body.scrollTop = 0;
                document.querySelectorAll('section.main, [data-testid=\\'stMain\\'], [data-testid=\\'stAppViewContainer\\'], .main, .block-container, [data-baseweb=\\'tab-panel\\']').forEach(function(el) {{
                    el.scrollTop = 0;
                }});
            }}
            resetAllScroll();

            var TAB_ICONS = [
                '<svg width=\\'15\\' height=\\'15\\' viewBox=\\'0 0 24 24\\' fill=\\'none\\' stroke=\\'currentColor\\' stroke-width=\\'2\\' stroke-linecap=\\'round\\' stroke-linejoin=\\'round\\' style=\\'margin-right:6px;flex-shrink:0;\\'><path d=\\'M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z\\'/><polyline points=\\'9 22 9 12 15 12 15 22\\'/></svg>',
                '<svg width=\\'15\\' height=\\'15\\' viewBox=\\'0 0 24 24\\' fill=\\'none\\' stroke=\\'currentColor\\' stroke-width=\\'2\\' stroke-linecap=\\'round\\' stroke-linejoin=\\'round\\' style=\\'margin-right:6px;flex-shrink:0;\\'><path d=\\'M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z\\'/></svg>',
                '<svg width=\\'15\\' height=\\'15\\' viewBox=\\'0 0 24 24\\' fill=\\'none\\' stroke=\\'currentColor\\' stroke-width=\\'2\\' stroke-linecap=\\'round\\' stroke-linejoin=\\'round\\' style=\\'margin-right:6px;flex-shrink:0;\\'><polygon points=\\'12 2 2 7 12 12 22 7 12 2\\'/><polyline points=\\'2 17 12 22 22 17\\'/><polyline points=\\'2 12 12 17 22 12\\'/></svg>',
                '<svg width=\\'15\\' height=\\'15\\' viewBox=\\'0 0 24 24\\' fill=\\'none\\' stroke=\\'currentColor\\' stroke-width=\\'2\\' stroke-linecap=\\'round\\' stroke-linejoin=\\'round\\' style=\\'margin-right:6px;flex-shrink:0;\\'><path d=\\'M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z\\'/></svg>',
                '<svg width=\\'15\\' height=\\'15\\' viewBox=\\'0 0 24 24\\' fill=\\'none\\' stroke=\\'currentColor\\' stroke-width=\\'2\\' stroke-linecap=\\'round\\' stroke-linejoin=\\'round\\' style=\\'margin-right:6px;flex-shrink:0;\\'><line x1=\\'18\\' y1=\\'20\\' x2=\\'18\\' y2=\\'10\\'/><line x1=\\'12\\' y1=\\'20\\' x2=\\'12\\' y2=\\'4\\'/><line x1=\\'6\\' y1=\\'20\\' x2=\\'6\\' y2=\\'14\\'/></svg>'
            ];

            var tabs = document.querySelectorAll('[data-baseweb=\\'tab-list\\'] button, div[data-testid=\\'stTabs\\'] button[role=\\'tab\\']');
            tabs.forEach(function(tab, idx) {{
                if (!tab.__hasKisanIcon && idx < TAB_ICONS.length) {{
                    tab.__hasKisanIcon = true;
                    tab.insertAdjacentHTML('afterbegin', TAB_ICONS[idx]);
                }}
                if (!tab.__hasKisanScroll) {{
                    tab.__hasKisanScroll = true;
                    tab.addEventListener('click', function() {{
                        resetAllScroll();
                        setTimeout(resetAllScroll, 10);
                        setTimeout(resetAllScroll, 50);
                        setTimeout(resetAllScroll, 120);
                    }});
                }}
            }});
        }} catch(e) {{}}
    " />
    """
    st.markdown(clean_html(nav_html), unsafe_allow_html=True)
