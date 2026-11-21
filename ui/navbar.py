"""Navbar component for KisanSaathi.
Renders edge-to-edge top navigation bar with brand logo, tabs slot, and language selector.
"""

import streamlit as st
from ui.assets import ICONS, clean_html

def render_pinned_navbar(language: str = "English"):
    """Render the pinned full-width top navbar."""
    nav_html = f"""
    <div class="ks-navbar">
        <div class="ks-nav-brand">
            <div>{ICONS['leaf_brand']}</div>
            <div>
                <div class="ks-nav-brand-title">KisanSaathi</div>
                <div class="ks-nav-brand-sub">AI Crop Advisory Assistant</div>
            </div>
        </div>
        <div style="display:flex; align-items:center; gap:0.75rem;">
            <span class="ks-lang-pill">{ICONS['globe']} {language} &#9662;</span>
        </div>
    </div>
    """
    st.markdown(clean_html(nav_html), unsafe_allow_html=True)
