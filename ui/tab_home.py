"""Home View module for KisanSaathi.
Renders:
1. Main Hero section with farmer-using-phone.jpg, pill badge, title lines, and CTAs.
2. Countryside landscape horizon decoration.
3. 4-Pillar capability cards (Crop Guidance, Problem Identification, Safe Recommendations, Multi-language Support).
"""

import streamlit as st
from ui.assets import ICONS, DECORATIVE, get_image_base64, clean_html

def render_tab_home():
    """Render Home Tab hero banner, capability pillars, and visual showcases."""
    phone_farmer_b64 = get_image_base64("farmer-using-phone.jpg")
    landscape_horizon_b64 = get_image_base64("countryside-horizon.png")

    # -------------------------------------------------------------------------
    # 1. Main Hero Section (Exact Recreation of Reference Image)
    # -------------------------------------------------------------------------
    hero_html = f"""
    <div class="ks-hero-container">
        <div class="ks-hero-left">
            <div class="ks-hero-badge">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#124C35" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/>
                    <path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>
                </svg>
                <span>AGRI-TECH ADVISORY PLATFORM</span>
            </div>

            <h1 class="ks-hero-title">
                <span class="ks-hero-title-line1">Better Crop Decisions.</span>
                <span class="ks-hero-title-line2">Safer Farming.</span>
            </h1>

            <p class="ks-hero-desc">
                Describe your crop problem in your preferred language and receive clear, cautious guidance grounded in verified ICAR agronomic practices.
            </p>

            <div class="ks-hero-actions">
                <button type="button" class="ks-btn-primary" onclick="(function(){{var t=document.querySelectorAll('[data-baseweb=\'tab-list\'] button, div[data-testid=\'stTabs\'] button[role=\'tab\']');if(t&&t[1])t[1].click();var b=document.querySelectorAll('.ks-nav-btn');b.forEach(function(el,i){{if(i===1)el.classList.add('active');else el.classList.remove('active');}});window.scrollTo({{top:0,behavior:'smooth'}});}})()">
                    <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/>
                        <path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>
                    </svg>
                    <span>Get Crop Advice &rarr;</span>
                </button>
                <button type="button" class="ks-btn-secondary" onclick="(function(){{var t=document.querySelectorAll('[data-baseweb=\'tab-list\'] button, div[data-testid=\'stTabs\'] button[role=\'tab\']');if(t&&t[2])t[2].click();var b=document.querySelectorAll('.ks-nav-btn');b.forEach(function(el,i){{if(i===2)el.classList.add('active');else el.classList.remove('active');}});window.scrollTo({{top:0,behavior:'smooth'}});}})()">
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#124C35" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
                        <polygon points="6 3 20 12 6 21 6 3"/>
                    </svg>
                    <span>How It Works</span>
                </button>
            </div>
        </div>

        <div class="ks-hero-right">
            <div class="ks-hero-farmer-frame">
                <img src="{phone_farmer_b64}" alt="Indian farmer using smartphone in lush green crop field" />
            </div>
        </div>
    </div>

    <!-- Countryside Landscape Horizon Decoration -->
    <div class="ks-landscape-horizon">
        <img src="{landscape_horizon_b64}" alt="Scenic Indian agricultural countryside horizon" />
    </div>

    <!-- 4 Feature Cards Grid Directly Below Hero -->
    <div class="ks-feature-cards-grid">
        <div class="ks-feature-card">
            <div class="ks-feature-icon-box">
                {ICONS['leaf_primary']}
            </div>
            <div class="ks-feature-text">
                <div class="ks-feature-title">Crop Guidance</div>
                <div class="ks-feature-desc">ICAR-validated agronomic steps and best practices.</div>
            </div>
            <div class="ks-feature-accent-line"></div>
        </div>

        <div class="ks-feature-card">
            <div class="ks-feature-icon-box">
                {ICONS['search']}
            </div>
            <div class="ks-feature-text">
                <div class="ks-feature-title">Problem Identification</div>
                <div class="ks-feature-desc">AI-powered, multilingual symptom understanding.</div>
            </div>
            <div class="ks-feature-accent-line"></div>
        </div>

        <div class="ks-feature-card">
            <div class="ks-feature-icon-box">
                {ICONS['shield_check']}
            </div>
            <div class="ks-feature-text">
                <div class="ks-feature-title">Safe Recommendations</div>
                <div class="ks-feature-desc">No chemical dosage, with farmer-safe guidance.</div>
            </div>
            <div class="ks-feature-accent-line"></div>
        </div>

        <div class="ks-feature-card">
            <div class="ks-feature-icon-box">
                {ICONS['language']}
            </div>
            <div class="ks-feature-text">
                <div class="ks-feature-title">Multi-language Support</div>
                <div class="ks-feature-desc">Get advice in English, Hindi and Hinglish.</div>
            </div>
            <div class="ks-feature-accent-line"></div>
        </div>
    </div>
    """
    st.markdown(clean_html(hero_html), unsafe_allow_html=True)
