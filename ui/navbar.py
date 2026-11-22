"""Navbar component for KisanSaathi.
Renders edge-to-edge top navigation bar with brand logo from the asset pack,
5 centered pill navigation buttons, and language selector.
Matches the target reference image with pixel-perfect fidelity.
"""

import streamlit as st
import streamlit.components.v1 as components
from ui.assets import LOGOS, ICONS, clean_html

NAV_CONTROLLER_JS = """
<script>
(function() {
    var p = window.parent;
    if (!p || !p.document) return;

    p.ksSwitchTab = function(idx) {
        try {
            var tabs = p.document.querySelectorAll('[data-baseweb="tab-list"] button, div[data-testid="stTabs"] button[role="tab"]');
            if (tabs && tabs[idx]) {
                tabs[idx].click();
            }
            var btns = p.document.querySelectorAll('.ks-nav-btn');
            btns.forEach(function(b, i) {
                if (i === idx) b.classList.add('active');
                else b.classList.remove('active');
            });
            p.scrollTo({ top: 0, behavior: 'smooth' });
        } catch(e) {
            console.error('ksSwitchTab error:', e);
        }
    };

    // Attach click listener on parent document for reliable tab switching
    if (!p.ksClickAttached) {
        p.document.addEventListener('click', function(e) {
            var navBtn = e.target.closest('.ks-nav-btn');
            if (navBtn) {
                var allNavBtns = Array.from(p.document.querySelectorAll('.ks-nav-btn'));
                var idx = allNavBtns.indexOf(navBtn);
                if (idx !== -1) {
                    p.ksSwitchTab(idx);
                }
                return;
            }

            if (e.target.closest('.ks-nav-brand')) {
                p.ksSwitchTab(0);
                return;
            }

            if (e.target.closest('.ks-btn-primary')) {
                p.ksSwitchTab(1);
                return;
            }

            if (e.target.closest('.ks-btn-secondary')) {
                p.ksSwitchTab(2);
                return;
            }

            var footerLink = e.target.closest('.ks-footer a');
            if (footerLink) {
                var text = footerLink.innerText.trim();
                if (text === 'Home') p.ksSwitchTab(0);
                else if (text === 'Ask AI') p.ksSwitchTab(1);
                else if (text === 'How It Works') p.ksSwitchTab(2);
                else if (text.indexOf('Safety') !== -1) p.ksSwitchTab(3);
                else if (text === 'Evaluation') p.ksSwitchTab(4);
                return;
            }
        }, true);
        p.ksClickAttached = true;
    }

    function syncActive() {
        try {
            var tabs = p.document.querySelectorAll('[data-baseweb="tab-list"] button, div[data-testid="stTabs"] button[role="tab"]');
            var btns = p.document.querySelectorAll('.ks-nav-btn');
            if (!tabs.length || !btns.length) return;
            tabs.forEach(function(t, i) {
                if (t.getAttribute('aria-selected') === 'true') {
                    btns.forEach(function(b, bi) {
                        if (bi === i) b.classList.add('active');
                        else b.classList.remove('active');
                    });
                }
            });
        } catch(e) {}
    }

    syncActive();
    if (!p.ksSyncInterval) {
        p.ksSyncInterval = setInterval(syncActive, 150);
    }
})();
</script>
"""

def render_pinned_navbar(language: str = "English"):
    """Render the pinned full-width top navbar with integrated tabs matching reference."""
    nav_html = f"""
    <div class="ks-navbar">
        <div class="ks-nav-left">
            <div class="ks-nav-brand" title="KisanSaathi Home">
                <div style="height:38px; display:flex; align-items:center; cursor:pointer;">
                    {LOGOS['horizontal']}
                </div>
            </div>
            <div class="ks-nav-divider"></div>
        </div>

        <div class="ks-nav-links" id="ksNavLinks">
            <button type="button" class="ks-nav-btn active">
                {ICONS['home']}
                <span>Home</span>
            </button>
            <button type="button" class="ks-nav-btn">
                {ICONS['message']}
                <span>Ask AI</span>
            </button>
            <button type="button" class="ks-nav-btn">
                {ICONS['layers']}
                <span>How It Works</span>
            </button>
            <button type="button" class="ks-nav-btn">
                {ICONS['shield_check']}
                <span>Safety Guardrails</span>
            </button>
            <button type="button" class="ks-nav-btn">
                {ICONS['chart']}
                <span>Evaluation</span>
            </button>
        </div>

        <div class="ks-nav-lang">
            <span class="ks-lang-pill">{ICONS['globe']} {language} &#9662;</span>
        </div>
    </div>
    """
    st.markdown(clean_html(nav_html), unsafe_allow_html=True)
    components.html(NAV_CONTROLLER_JS, height=1)
