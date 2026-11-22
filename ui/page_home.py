"""Home Page view module for KisanSaathi.
Precision recreation of visual reference media_1795344704327_f7649893.jpg:
- Two-column hero section with 'AGRI-TECH ADVISORY PLATFORM' badge
- Bold typography: 'Better Crop Decisions. Safer Farming.'
- 'Get Crop Advice ->' primary pill button & '▷ How It Works' secondary button
- Framed smiling farmer photograph with sprout badge on corner
- Subtle countryside agricultural landscape horizon banner
- Four feature cards grid: Crop Guidance, Problem Identification, Safe Recommendations, Multi-language Support
"""

import streamlit as st
from ui.assets import ICONS, DECORATIVE, get_image_base64, clean_html

def render_page_home():
    """Render the exact visual reference homepage."""
    farmer_img_b64 = get_image_base64("farmer-using-phone.jpg")
    landscape_b64 = get_image_base64("countryside-horizon.png")

    home_html = f"""
    <div class="ks-home-page" style="position:relative;">
        <!-- Floating Foliage Background SVGs from Asset Pack -->
        <div style="position:absolute; top:5px; left:-10px; width:130px; height:90px; pointer-events:none; z-index:1; opacity:0.4;">
            {DECORATIVE['leaf_branch']}
        </div>
        <div style="position:absolute; top:5px; right:-10px; width:130px; height:90px; pointer-events:none; z-index:1; opacity:0.4; transform:scaleX(-1);">
            {DECORATIVE['leaf_branch']}
        </div>

        <!-- 1. Hero Section (Two Columns) -->
        <div class="ks-hero-container" style="padding-top:0.8rem;">
            <div class="ks-hero-left">
                <div class="ks-hero-badge">
                    {ICONS['leaf_primary']}
                    <span>AGRI-TECH ADVISORY PLATFORM</span>
                </div>

                <div class="ks-hero-title">
                    <span class="ks-hero-title-line1">Better Crop Decisions.</span>
                    <span class="ks-hero-title-line2">Safer Farming.</span>
                </div>

                <p class="ks-hero-desc">
                    Describe your crop problem in your preferred language and receive clear, cautious guidance grounded in verified agricultural practices.
                </p>

                <div class="ks-hero-actions">
                    <button type="button" class="ks-btn-primary" onclick="(function(){{
                        var tabs = document.querySelectorAll('[data-baseweb=\\'tab-list\\'] button, div[data-testid=\\'stTabs\\'] button[role=\\'tab\\']');
                        if (tabs && tabs[1]) tabs[1].click();
                        window.scrollTo({{top: 0, behavior: 'smooth'}});
                    }})()">
                        {ICONS['leaf_white']}
                        <span>Get Crop Advice &rarr;</span>
                    </button>

                    <button type="button" class="ks-btn-secondary" onclick="(function(){{
                        var tabs = document.querySelectorAll('[data-baseweb=\\'tab-list\\'] button, div[data-testid=\\'stTabs\\'] button[role=\\'tab\\']');
                        if (tabs && tabs[2]) tabs[2].click();
                        window.scrollTo({{top: 0, behavior: 'smooth'}});
                    }})()">
                        {ICONS['play']}
                        <span>How It Works</span>
                    </button>
                </div>
            </div>

            <div class="ks-hero-right">
                <div class="ks-hero-farmer-frame">
                    <img src="{farmer_img_b64}" alt="Indian farmer using smartphone in lush green crop field" />
                    <div class="ks-farmer-sprout-badge">
                        {ICONS['sprout']}
                    </div>
                </div>
            </div>
        </div>

        <!-- 2. Countryside Landscape Horizon Decoration -->
        <div class="ks-landscape-horizon">
            <img src="{landscape_b64}" alt="Scenic Indian agricultural countryside horizon" />
        </div>

        <!-- 3. Four Feature Cards Grid Directly Below Hero -->
        <div class="ks-feature-cards-grid">
            <!-- Card 1: Crop Guidance -->
            <div class="ks-feature-card">
                <div>
                    <div class="ks-feature-icon-box">
                        {ICONS['sprout']}
                    </div>
                    <h3 class="ks-feature-title">Crop Guidance</h3>
                    <p class="ks-feature-desc">
                        ICAR-informed agricultural guidance and best practices.
                    </p>
                </div>
                <div class="ks-feature-accent-line"></div>
            </div>

            <!-- Card 2: Problem Identification -->
            <div class="ks-feature-card">
                <div>
                    <div class="ks-feature-icon-box">
                        {ICONS['search']}
                    </div>
                    <h3 class="ks-feature-title">Problem Identification</h3>
                    <p class="ks-feature-desc">
                        Multilingual symptom understanding for accurate issue detection.
                    </p>
                </div>
                <div class="ks-feature-accent-line"></div>
            </div>

            <!-- Card 3: Safe Recommendations -->
            <div class="ks-feature-card">
                <div>
                    <div class="ks-feature-icon-box">
                        {ICONS['shield_check']}
                    </div>
                    <h3 class="ks-feature-title">Safe Recommendations</h3>
                    <p class="ks-feature-desc">
                        Farmer-safe guidance without unsupported chemical dosage.
                    </p>
                </div>
                <div class="ks-feature-accent-line"></div>
            </div>

            <!-- Card 4: Multi-language Support -->
            <div class="ks-feature-card">
                <div>
                    <div class="ks-feature-icon-box">
                        {ICONS['language']}
                    </div>
                    <h3 class="ks-feature-title">Multi-language Support</h3>
                    <p class="ks-feature-desc">
                        Get advice in English, Hindi and Hinglish.
                    </p>
                </div>
                <div class="ks-feature-accent-line"></div>
            </div>
        </div>
    </div>
    """
    st.markdown(clean_html(home_html), unsafe_allow_html=True)
