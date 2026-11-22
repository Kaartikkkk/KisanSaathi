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
    <!-- Client-side script to clear lingering heading anchor hashes and guarantee scroll-to-top on tab switches -->
    <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg'/>" style="display:none;" onerror="
        try {{
            if (window.location.hash) {{
                history.replaceState(null, null, window.location.pathname + window.location.search);
                window.scrollTo(0, 0);
            }}
            document.querySelectorAll('[data-baseweb=\\'tab\\'], button[role=\\'tab\\']').forEach(function(tab) {{
                if (!tab.__hasScrollHandler) {{
                    tab.__hasScrollHandler = true;
                    tab.addEventListener('click', function() {{
                        window.scrollTo({{top: 0, behavior: 'instant'}});
                        var sc = document.querySelector('section.main, [data-testid=\\'stMain\\']');
                        if (sc) sc.scrollTop = 0;
                    }});
                }}
            }});
        }} catch(e) {{}}
    " />
    """
    st.markdown(clean_html(nav_html), unsafe_allow_html=True)
