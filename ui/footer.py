"""Unified application footer for KisanSaathi.
Renders brand mark, ICAR agronomic compliance notice, and copyright across all tabs.
"""

import streamlit as st
from ui.assets import LOGOS, clean_html

def render_footer():
    """Render the single unified application footer."""
    footer_html = f"""
    <div class="ks-footer">
        <div style="display:flex; align-items:center; justify-content:center; gap:0.5rem; height:42px; margin-bottom:0.75rem;">
            {LOGOS.get('horizontal', '')}
        </div>
        <div style="max-width:720px; margin:0 auto 0.85rem auto; font-size:0.82rem; line-height:1.6; color:#5A6860;">
            <b>Agricultural Advisory Notice:</b> KisanSaathi is an agronomic artificial intelligence prototype developed for preliminary educational and advisory support. All assessments and recommendations must be physically verified by certified agricultural extension officers or Krishi Vigyan Kendras (KVK).
        </div>
        <div style="font-size:0.75rem; color:#788A80;">
            &copy; 2026 KisanSaathi &middot; Built with Gemini 2.5 Flash &middot; Grounded in ICAR Agronomic Practice Standards
        </div>
    </div>
    """
    st.markdown(clean_html(footer_html), unsafe_allow_html=True)
