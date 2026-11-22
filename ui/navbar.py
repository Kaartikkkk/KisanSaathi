"""Navbar component for KisanSaathi.
Renders edge-to-edge top navigation bar with brand logo from the asset pack,
centered slot for native Streamlit tabs, and language selector.
Matches the target reference image with 100% native responsiveness and zero iframes.
"""

import streamlit as st
from ui.assets import LOGOS, ICONS, clean_html

def render_pinned_navbar(language: str = "English"):
    """Render the pinned full-width top navbar."""
    nav_html = f"""
    <div class="ks-navbar">
        <div class="ks-nav-left">
            <div class="ks-nav-brand" title="KisanSaathi Home">
                <div style="height:38px; display:flex; align-items:center;">
                    {LOGOS['horizontal']}
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
    """
    st.markdown(clean_html(nav_html), unsafe_allow_html=True)
