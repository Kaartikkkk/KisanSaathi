"""Home View module for KisanSaathi.
Renders:
1. Hero section with farmer-using-phone.jpg and leaf-branch decorative SVG.
2. 4-Pillar capability strip with Feather/Lucide vector line icons.
3. Crop variety showcase featuring crop-variety.jpg.
4. Farmer empowerment & KVK escalation section featuring farmer-in-field.jpg.
5. Scenic agricultural footer banner featuring farm-landscape.jpg.
"""

import streamlit as st
from ui.assets import ICONS, DECORATIVE, get_image_base64, clean_html

def render_tab_home():
    """Render Home Tab hero banner, capability pillars, and visual showcases."""
    phone_farmer_b64 = get_image_base64("farmer-using-phone.jpg")
    crop_variety_b64 = get_image_base64("crop-variety.jpg")
    field_farmer_b64 = get_image_base64("farmer-in-field.jpg")
    landscape_b64 = get_image_base64("farm-landscape.jpg")
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

    # -------------------------------------------------------------------------
    # 3. Crop Variety Showcase Section (Featuring crop-variety.jpg)
    # -------------------------------------------------------------------------
    crop_section_html = f"""
    <div style="background:#FFFFFF; border:1.5px solid #DFE8DF; border-radius:24px; padding:2.5rem 3rem; margin-bottom:2rem; box-shadow:0 4px 20px rgba(23,75,53,0.03);">
        <div style="display:flex; align-items:center; justify-content:space-between; gap:2.5rem; flex-wrap:wrap;">
            <div style="flex:1 1 400px; max-width:480px;">
                <div style="width:100%; aspect-ratio:16/9; border-radius:18px; overflow:hidden; box-shadow:0 8px 24px rgba(23,75,53,0.06); border:2px solid #FFFFFF;">
                    <img src="{crop_variety_b64}" alt="Diverse Indian agricultural crops, grains, and produce" style="width:100%; height:100%; object-fit:cover; display:block;" />
                </div>
            </div>
            <div style="flex:1 1 460px;">
                <div style="display:inline-block; margin-bottom:0.5rem;">
                    <span class="ks-pill-badge">AGRONOMIC COVERAGE</span>
                </div>
                <h2 style="font-size:2rem; font-weight:800; color:#174B35; margin:0 0 0.75rem 0; letter-spacing:-0.02em;">
                    Calibrated Across Major Indian Crops
                </h2>
                <p style="color:#5A6860; font-size:0.98rem; line-height:1.6; margin:0 0 1.25rem 0;">
                    KisanSaathi's grounded knowledge retrieval integrates standard packages of practices covering staple cereals, solanaceous vegetables, oilseeds, and pulses across distinct state agro-climatic zones.
                </p>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.75rem;">
                    <div style="background:#F7FAF4; border:1px solid #DFE8DF; border-radius:12px; padding:0.85rem 1rem;">
                        <div style="font-weight:700; color:#174B35; font-size:0.92rem; display:flex; align-items:center; gap:6px;">
                            {ICONS['sprout']} Cereals & Grains
                        </div>
                        <div style="font-size:0.8rem; color:#5A6860; margin-top:2px;">Rice (WB), Wheat (PB), Maize</div>
                    </div>
                    <div style="background:#F7FAF4; border:1px solid #DFE8DF; border-radius:12px; padding:0.85rem 1rem;">
                        <div style="font-weight:700; color:#174B35; font-size:0.92rem; display:flex; align-items:center; gap:6px;">
                            {ICONS['leaf_primary']} Solanaceous Crops
                        </div>
                        <div style="font-size:0.8rem; color:#5A6860; margin-top:2px;">Tomato (UP), Potato (UP)</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
    st.markdown(clean_html(crop_section_html), unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # 4. Farmer Empowerment & KVK Extension Section (Featuring farmer-in-field.jpg)
    # -------------------------------------------------------------------------
    farmer_section_html = f"""
    <div style="background:#FFFFFF; border:1.5px solid #DFE8DF; border-radius:24px; padding:2.5rem 3rem; margin-bottom:2rem; box-shadow:0 4px 20px rgba(23,75,53,0.03);">
        <div style="display:flex; align-items:center; justify-content:space-between; gap:2.5rem; flex-wrap:wrap;">
            <div style="flex:1 1 460px;">
                <div style="display:inline-block; margin-bottom:0.5rem;">
                    <span class="ks-pill-badge">FIELD EXTENSION ALIGNMENT</span>
                </div>
                <h2 style="font-size:2rem; font-weight:800; color:#174B35; margin:0 0 0.75rem 0; letter-spacing:-0.02em;">
                    Empowering Farmers On-Ground
                </h2>
                <p style="color:#5A6860; font-size:0.98rem; line-height:1.6; margin:0 0 1.25rem 0;">
                    Rather than speculating with hazardous chemical spraying dosages, KisanSaathi provides biological, mechanical, and cultural remedies. When issues are uncertain or rapidly spreading, it provides immediate contact pathways to Krishi Vigyan Kendra (KVK) agronomy scientists.
                </p>
                <div style="display:flex; flex-wrap:wrap; gap:0.75rem;">
                    <span style="background:#E7F2E8; color:#174B35; font-weight:700; font-size:0.82rem; padding:0.4rem 1rem; border-radius:999px; border:1px solid #D0E7D4; display:inline-flex; align-items:center; gap:5px;">
                        {ICONS['shield_check']} Zero Chemical Dosage Risk
                    </span>
                    <span style="background:#E7F2E8; color:#174B35; font-weight:700; font-size:0.82rem; padding:0.4rem 1rem; border-radius:999px; border:1px solid #D0E7D4; display:inline-flex; align-items:center; gap:5px;">
                        {ICONS['users']} Human-in-the-Loop Safeguard
                    </span>
                </div>
            </div>
            <div style="flex:1 1 400px; max-width:480px;">
                <div style="width:100%; aspect-ratio:16/9; border-radius:18px; overflow:hidden; box-shadow:0 8px 24px rgba(23,75,53,0.06); border:2px solid #FFFFFF;">
                    <img src="{field_farmer_b64}" alt="Indian farmer inspecting crop foliage in the field" style="width:100%; height:100%; object-fit:cover; display:block;" />
                </div>
            </div>
        </div>
    </div>
    """
    st.markdown(clean_html(farmer_section_html), unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # 5. Agricultural Landscape Banner (Featuring farm-landscape.jpg)
    # -------------------------------------------------------------------------
    landscape_banner_html = f"""
    <div style="position:relative; border-radius:24px; overflow:hidden; height:180px; box-shadow:0 8px 24px rgba(23,75,53,0.06); margin-bottom:1.5rem; border:2px solid #FFFFFF;">
        <img src="{landscape_b64}" alt="Lush Indian agricultural terraced farmland landscape" style="width:100%; height:100%; object-fit:cover; display:block; filter:brightness(0.85);" />
        <div style="position:absolute; inset:0; background:linear-gradient(90deg, rgba(23,75,53,0.88) 0%, rgba(23,75,53,0.4) 100%); display:flex; align-items:center; padding:0 3rem;">
            <div style="max-width:560px;">
                <h3 style="color:#FFFFFF; font-size:1.6rem; font-weight:800; margin:0 0 0.35rem 0;">
                    Sustaining Soil, Crop & Farmer Prosperity
                </h3>
                <p style="color:#E7F2E8; font-size:0.95rem; margin:0; line-height:1.5;">
                    Reliable agricultural AI grounded in certified agronomic literature for Indian farming communities.
                </p>
            </div>
        </div>
    </div>
    """
    st.markdown(clean_html(landscape_banner_html), unsafe_allow_html=True)
