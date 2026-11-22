"""Unified application footer for KisanSaathi.
Renders official brand mark, agricultural advisory notice, and ICAR compliance notice.
"""

import streamlit as st
from ui.assets import LOGOS, clean_html

def render_footer():
    """Render the single unified application footer."""
    footer_html = f"""
    <div class="ks-footer">
        <div style="height:68px; max-width:170px; margin:0 auto 0.85rem auto; display:flex; align-items:center; justify-content:center;">
            {LOGOS['full']}
        </div>
        <div style="max-width:740px; margin:0 auto 0.85rem auto; font-size:0.83rem; line-height:1.6; color:#64756C;">
            <b>Agricultural Advisory Notice:</b> KisanSaathi is an agronomic AI advisory prototype developed for preliminary educational guidance. All recommendations are non-chemical cultural practices. Always consult your nearest Krishi Vigyan Kendra (KVK) or Block Agriculture Officer for physical crop inspection.
        </div>
        <div style="font-size:0.76rem; color:#7A8D83;">
            &copy; 2026 KisanSaathi &middot; Grounded in ICAR Certified Agronomic Practice Standards
        </div>
    </div>
    """
    st.markdown(clean_html(footer_html), unsafe_allow_html=True)
