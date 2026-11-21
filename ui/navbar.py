"""Navbar component for KisanSaathi.
Renders edge-to-edge top navigation bar with brand logo, interactive navigation tabs, and language selector.
"""

import streamlit as st
from ui.assets import ICONS, clean_html

def render_pinned_navbar(language: str = "English"):
    """Render the pinned full-width top navbar with built-in navigation tabs."""
    nav_html = f"""
    <div class="ks-navbar">
        <div class="ks-nav-brand" onclick="ksSwitchTab(0)">
            <div>{ICONS['leaf_brand']}</div>
            <div>
                <div class="ks-nav-brand-title">KisanSaathi</div>
                <div class="ks-nav-brand-sub">AI Crop Advisory Assistant</div>
            </div>
        </div>

        <div class="ks-nav-links">
            <button class="ks-nav-btn active" id="ks-btn-0" onclick="ksSwitchTab(0)">
                {ICONS['home']} Home
            </button>
            <button class="ks-nav-btn" id="ks-btn-1" onclick="ksSwitchTab(1)">
                {ICONS['layers']} How It Works
            </button>
            <button class="ks-nav-btn" id="ks-btn-2" onclick="ksSwitchTab(2)">
                {ICONS['leaf_primary']} Ask AI
            </button>
            <button class="ks-nav-btn" id="ks-btn-3" onclick="ksSwitchTab(3)">
                {ICONS['shield_check']} Safety
            </button>
            <button class="ks-nav-btn" id="ks-btn-4" onclick="ksSwitchTab(4)">
                {ICONS['chart']} Evaluation
            </button>
        </div>

        <div style="display:flex; align-items:center; gap:0.75rem;">
            <span class="ks-lang-pill">{ICONS['globe']} {language} &#9662;</span>
        </div>
    </div>

    <script>
    function ksSwitchTab(idx) {{
        try {{
            var d = (window.parent && window.parent.document) || document;
            var tabs = d.querySelectorAll('[data-baseweb="tab"]');
            if (tabs && tabs[idx]) {{
                tabs[idx].click();
            }}
            var btns = d.querySelectorAll('.ks-nav-btn');
            if (btns && btns.length) {{
                for (var i = 0; i < btns.length; i++) {{
                    if (i === idx) {{
                        btns[i].classList.add('active');
                    }} else {{
                        btns[i].classList.remove('active');
                    }}
                }}
            }}
        }} catch(e) {{
            console.error(e);
        }}
    }}

    (function() {{
        function ksSync() {{
            try {{
                var d = (window.parent && window.parent.document) || document;
                var tabs = d.querySelectorAll('[data-baseweb="tab"]');
                var btns = d.querySelectorAll('.ks-nav-btn');
                if (tabs && btns && tabs.length >= btns.length) {{
                    for (var i = 0; i < tabs.length; i++) {{
                        if (tabs[i].getAttribute('aria-selected') === 'true') {{
                            for (var j = 0; j < btns.length; j++) {{
                                if (j === i) {{
                                    btns[j].classList.add('active');
                                }} else {{
                                    btns[j].classList.remove('active');
                                }}
                            }}
                            break;
                        }}
                    }}
                }}
            }} catch(e) {{}}
        }}
        setTimeout(ksSync, 50);
        setTimeout(ksSync, 200);
        setTimeout(ksSync, 500);
        setTimeout(ksSync, 1000);
    }})();
    </script>
    """
    st.markdown(clean_html(nav_html), unsafe_allow_html=True)
