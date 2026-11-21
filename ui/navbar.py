"""Navbar component for KisanSaathi.
Renders edge-to-edge top navigation bar with brand logo from the asset pack,
5 centered pill navigation buttons, and language selector.
"""

import streamlit as st
from ui.assets import LOGOS, ICONS, clean_html

NAV_SCRIPT = """
<script>
(function() {
    window.ksSwitchTab = function(idx) {
        try {
            var tabs = document.querySelectorAll('[data-baseweb="tab-list"] button, div[data-testid="stTabs"] button[role="tab"]');
            if (tabs && tabs[idx]) {
                tabs[idx].click();
            }
            var btns = document.querySelectorAll('.ks-nav-btn');
            btns.forEach(function(b, i) {
                if (i === idx) {
                    b.classList.add('active');
                } else {
                    b.classList.remove('active');
                }
            });
            window.scrollTo({ top: 0, behavior: 'smooth' });
        } catch(e) {
            console.error('ksSwitchTab error:', e);
        }
    };

    function syncActive() {
        var tabs = document.querySelectorAll('[data-baseweb="tab-list"] button, div[data-testid="stTabs"] button[role="tab"]');
        var btns = document.querySelectorAll('.ks-nav-btn');
        if (!tabs.length || !btns.length) return;
        tabs.forEach(function(t, i) {
            if (t.getAttribute('aria-selected') === 'true') {
                btns.forEach(function(b, bi) {
                    if (bi === i) b.classList.add('active');
                    else b.classList.remove('active');
                });
            }
        });
    }
    setTimeout(syncActive, 100);
    setTimeout(syncActive, 400);
    setTimeout(syncActive, 1000);
})();
</script>
"""

def render_pinned_navbar(language: str = "English"):
    """Render the pinned full-width top navbar with integrated tabs."""
    nav_html = f"""
    <div class="ks-navbar">
        <div class="ks-nav-brand" onclick="if(window.ksSwitchTab) window.ksSwitchTab(0);" title="KisanSaathi Home">
            <div style="height:42px; width:170px; min-width:170px; display:flex; align-items:center; cursor:pointer;">
                {LOGOS['horizontal']}
            </div>
        </div>

        <div class="ks-nav-links" id="ksNavLinks">
            <button type="button" class="ks-nav-btn active" onclick="if(window.ksSwitchTab) window.ksSwitchTab(0);">
                {ICONS['home']}
                <span>Home</span>
            </button>
            <button type="button" class="ks-nav-btn" onclick="if(window.ksSwitchTab) window.ksSwitchTab(1);">
                {ICONS['layers']}
                <span>How It Works</span>
            </button>
            <button type="button" class="ks-nav-btn" onclick="if(window.ksSwitchTab) window.ksSwitchTab(2);">
                {ICONS['sprout']}
                <span>Ask AI</span>
            </button>
            <button type="button" class="ks-nav-btn" onclick="if(window.ksSwitchTab) window.ksSwitchTab(3);">
                {ICONS['shield_check']}
                <span>Safety</span>
            </button>
            <button type="button" class="ks-nav-btn" onclick="if(window.ksSwitchTab) window.ksSwitchTab(4);">
                {ICONS['chart']}
                <span>Evaluation</span>
            </button>
        </div>

        <div class="ks-nav-lang">
            <span class="ks-lang-pill">{ICONS['globe']} {language} &#9662;</span>
        </div>
    </div>
    """
    st.markdown(clean_html(nav_html) + "\n" + NAV_SCRIPT, unsafe_allow_html=True)


