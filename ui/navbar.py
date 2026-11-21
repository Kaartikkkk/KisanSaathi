"""Navbar component for KisanSaathi.
Renders edge-to-edge top navigation bar with brand logo from the asset pack,
centered slot for native Streamlit tabs, and language selector.
"""

import streamlit as st
from ui.assets import LOGOS, ICONS, clean_html

def render_pinned_navbar(language: str = "English"):
    """Render the pinned full-width top navbar."""
    nav_html = f"""
    <div class="ks-navbar">
        <div class="ks-nav-brand" onclick="var t=document.querySelectorAll('[data-baseweb=tab-list] button, button[role=tab]'); if(t&&t[0]) t[0].click();">
            <div style="height:44px; width:170px; min-width:170px; display:flex; align-items:center;">
                {LOGOS['horizontal']}
            </div>
        </div>

        <div class="ks-nav-tabs-slot" style="flex:1; max-width:650px; height:42px; pointer-events:none;">
            <!-- Native Streamlit st.tabs are positioned centered here via CSS -->
        </div>

        <div class="ks-nav-lang">
            <span class="ks-lang-pill">{ICONS['globe']} {language} &#9662;</span>
        </div>
    </div>
    """
    st.markdown(clean_html(nav_html), unsafe_allow_html=True)
