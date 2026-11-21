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

    # -------------------------------------------------------------------------
    # 1. Main Hero Banner
    # -------------------------------------------------------------------------
    hero_html = f"""
    <div class="ks-hero-card" style="background:#FFFFFF; border:1.5px solid #E2EBE2; border-radius:24px; padding:2.8rem 3rem; position:relative; overflow:hidden; box-shadow:0 4px 24px rgba(23,75,53,0.05); margin-bottom:2rem;">
        <!-- Foliage Accent SVG from Asset Pack -->
        <div style="position:absolute; top:0; left:0; width:160px; height:120px; pointer-events:none; opacity:0.35;">
            {DECORATIVE['leaf_branch']}
        </div>

        <div style="display:flex; align-items:center; justify-content:space-between; gap:2.5rem; flex-wrap:wrap; position:relative; z-index:2;">
            <div style="flex:1 1 480px; max-width:560px;">
                <div style="display:inline-block; margin-bottom:0.75rem;">
                    <span class="ks-pill-badge">AGRI-TECH ADVISORY PLATFORM</span>
                </div>
                <h1 style="font-size:2.85rem; font-weight:800; color:#174B35; line-height:1.15; letter-spacing:-0.03em; margin:0 0 1rem 0;">
                    Better Crop Decisions.<br>
                    <span style="color:#2F8A57;">Safer Farming.</span>
                </h1>
                <div style="width:48px; height:4px; background:#2F8A57; border-radius:2px; margin-bottom:1.5rem;"></div>
                <p style="font-size:1.05rem; color:#5A6860; line-height:1.6; margin:0 0 2rem 0;">
                    Describe your crop problem in your preferred language and receive clear, cautious guidance grounded in verified ICAR agronomic practices.
                </p>
                <div style="display:flex; align-items:center; gap:1rem; flex-wrap:wrap;">
                    <button onclick="var d=(window.parent&&window.parent.document)||document; var t=d.querySelectorAll('[data-baseweb=\\'tab\\']'); if(t&&t[2]) t[2].click();" style="background:#174B35; color:#FFFFFF; border:none; border-radius:999px; padding:0.85rem 1.85rem; font-size:1rem; font-weight:700; cursor:pointer; display:inline-flex; align-items:center; gap:0.5rem; box-shadow:0 4px 14px rgba(23,75,53,0.25);">
                        {ICONS['leaf_white']} Get Crop Advice &rarr;
                    </button>
                    <button onclick="var d=(window.parent&&window.parent.document)||document; var t=d.querySelectorAll('[data-baseweb=\\'tab\\']'); if(t&&t[1]) t[1].click();" style="background:#FFFFFF; color:#174B35; border:1.5px solid #174B35; border-radius:999px; padding:0.82rem 1.8rem; font-size:1rem; font-weight:700; cursor:pointer; display:inline-flex; align-items:center; gap:0.5rem;">
                        How It Works
                    </button>
                </div>
            </div>

            <div style="flex:1 1 400px; max-width:480px; display:flex; justify-content:center;">
                <div style="width:100%; max-width:440px; aspect-ratio:4/3; border-radius:20px; overflow:hidden; box-shadow:0 12px 32px rgba(23,75,53,0.08); border:3px solid #FFFFFF;">
                    <img src="{phone_farmer_b64}" alt="Indian farmer using smartphone in lush green crop field" style="width:100%; height:100%; object-fit:cover; display:block;" />
                </div>
            </div>
        </div>
    </div>
    """
    st.markdown(clean_html(hero_html), unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # 2. 4-Pillar Capability Strip
    # -------------------------------------------------------------------------
    strip_html = f"""
    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:1.25rem; margin-bottom:2.5rem;">
        <div style="background:#FFFFFF; border:1.5px solid #E2EBE2; border-radius:16px; padding:1.25rem 1.4rem; display:flex; align-items:center; gap:0.85rem; box-shadow:0 2px 8px rgba(23,75,53,0.02);">
            <div style="background:#E7F2E8; width:44px; height:44px; border-radius:12px; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                {ICONS['leaf_primary']}
            </div>
            <div>
                <div style="font-size:0.95rem; font-weight:700; color:#174B35;">Crop Guidance</div>
                <div style="font-size:0.78rem; color:#5A6860;">ICAR validated steps</div>
            </div>
        </div>

        <div style="background:#FFFFFF; border:1.5px solid #E2EBE2; border-radius:16px; padding:1.25rem 1.4rem; display:flex; align-items:center; gap:0.85rem; box-shadow:0 2px 8px rgba(23,75,53,0.02);">
            <div style="background:#E7F2E8; width:44px; height:44px; border-radius:12px; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                {ICONS['search']}
            </div>
            <div>
                <div style="font-size:0.95rem; font-weight:700; color:#174B35;">Problem Identification</div>
                <div style="font-size:0.78rem; color:#5A6860;">Multilingual symptom parsing</div>
            </div>
        </div>

        <div style="background:#FFFFFF; border:1.5px solid #E2EBE2; border-radius:16px; padding:1.25rem 1.4rem; display:flex; align-items:center; gap:0.85rem; box-shadow:0 2px 8px rgba(23,75,53,0.02);">
            <div style="background:#E7F2E8; width:44px; height:44px; border-radius:12px; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                {ICONS['shield_check']}
            </div>
            <div>
                <div style="font-size:0.95rem; font-weight:700; color:#174B35;">Safe Recommendations</div>
                <div style="font-size:0.78rem; color:#5A6860;">Zero synthetic dosage</div>
            </div>
        </div>

        <div style="background:#FFFFFF; border:1.5px solid #E2EBE2; border-radius:16px; padding:1.25rem 1.4rem; display:flex; align-items:center; gap:0.85rem; box-shadow:0 2px 8px rgba(23,75,53,0.02);">
            <div style="background:#E7F2E8; width:44px; height:44px; border-radius:12px; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                {ICONS['language']}
            </div>
            <div>
                <div style="font-size:0.95rem; font-weight:700; color:#174B35;">Multi-language Support</div>
                <div style="font-size:0.78rem; color:#5A6860;">English, Hindi & Hinglish</div>
            </div>
        </div>
    </div>
    """
    st.markdown(clean_html(strip_html), unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # 3. Crop Variety Showcase Section (Featuring crop-variety.jpg)
    # -------------------------------------------------------------------------
    crop_section_html = f"""
    <div style="background:#FFFFFF; border:1.5px solid #E2EBE2; border-radius:24px; padding:2.5rem 3rem; margin-bottom:2rem; box-shadow:0 4px 20px rgba(23,75,53,0.03);">
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
                    <div style="background:#F7FAF4; border:1px solid #E2EBE2; border-radius:12px; padding:0.85rem 1rem;">
                        <div style="font-weight:700; color:#174B35; font-size:0.92rem; display:flex; align-items:center; gap:6px;">
                            {ICONS['sprout']} Cereals & Grains
                        </div>
                        <div style="font-size:0.8rem; color:#5A6860; margin-top:2px;">Rice (WB), Wheat (PB), Maize</div>
                    </div>
                    <div style="background:#F7FAF4; border:1px solid #E2EBE2; border-radius:12px; padding:0.85rem 1rem;">
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
    <div style="background:#FFFFFF; border:1.5px solid #E2EBE2; border-radius:24px; padding:2.5rem 3rem; margin-bottom:2rem; box-shadow:0 4px 20px rgba(23,75,53,0.03);">
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
