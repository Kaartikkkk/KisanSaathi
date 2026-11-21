"""Home View module for KisanSaathi.
Renders hero section matching mockup media_1795285920306_a3ee7658.jpg and 4-pillar strip.
"""

import base64
import os
import streamlit as st
from ui.assets import ICONS

def get_base64_image(image_path: str) -> str:
    """Read a local image file and encode it as base64."""
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

def render_tab_home():
    """Render Home Tab hero banner and core capability strip."""
    farmer_b64 = (
        get_base64_image("assets/farmer_portrait_hd.jpg")
        or get_base64_image("assets/farmer_clean_hd.jpg")
    )

    st.markdown(f"""
    <div class="ks-hero-card" style="background:#FFFFFF; border:1.5px solid #E2E9E1; border-radius:24px; padding:2.8rem 3rem; position:relative; overflow:hidden; box-shadow:0 4px 22px rgba(23,75,53,0.04); margin-bottom:2rem;">
        <svg viewBox="0 0 160 120" fill="none" xmlns="http://www.w3.org/2000/svg" style="position:absolute; top:0; left:0; width:130px; height:100px; pointer-events:none; opacity:0.45;">
            <path d="M-10 -10 C 20 20, 60 40, 120 45" stroke="#2E7D50" stroke-width="2.5" stroke-linecap="round"/>
            <path d="M25 24 C 15 15, 20 0, 35 5 C 45 10, 40 25, 25 24 Z" fill="#2E7D50" opacity="0.8"/>
            <path d="M55 35 C 50 20, 65 10, 78 18 C 85 28, 70 40, 55 35 Z" fill="#3B925E" opacity="0.85"/>
            <path d="M85 41 C 85 25, 102 22, 110 32 C 115 42, 98 50, 85 41 Z" fill="#2E7D50" opacity="0.75"/>
            <path d="M40 32 C 30 45, 15 45, 18 32 C 22 22, 35 25, 40 32 Z" fill="#256C42" opacity="0.7"/>
            <path d="M72 40 C 65 55, 50 56, 52 42 C 55 32, 68 32, 72 40 Z" fill="#2E7D50" opacity="0.8"/>
            <path d="M105 45 C 102 60, 88 62, 88 48 C 90 38, 102 38, 105 45 Z" fill="#3B925E" opacity="0.75"/>
        </svg>

        <div style="display:flex; align-items:center; justify-content:space-between; gap:2.5rem; flex-wrap:wrap; position:relative; z-index:2;">
            <div style="flex:1 1 480px; max-width:560px;">
                <h1 style="font-size:2.85rem; font-weight:800; color:#174B35; line-height:1.15; letter-spacing:-0.03em; margin:0 0 1rem 0;">
                    Better Crop Decisions.<br>
                    <span style="color:#174B35;">Safer Farming.</span>
                </h1>
                <div style="width:48px; height:4px; background:#2E7D50; border-radius:2px; margin-bottom:1.5rem;"></div>
                <p style="font-size:1.05rem; color:#68756C; line-height:1.6; margin:0 0 2rem 0;">
                    Describe your crop problem in your preferred language and receive clear, cautious guidance to help you take the next step.
                </p>
                <div style="display:flex; align-items:center; gap:1rem; flex-wrap:wrap;">
                    <button onclick="parent.document.querySelectorAll('[data-baseweb=\\'tab\\']')[2].click()" style="background:#174B35; color:#FFFFFF; border:none; border-radius:999px; padding:0.85rem 1.85rem; font-size:1rem; font-weight:700; cursor:pointer; display:inline-flex; align-items:center; gap:0.5rem; box-shadow:0 4px 14px rgba(23,75,53,0.25);">
                        {ICONS['leaf_white']} Get Crop Advice &rarr;
                    </button>
                    <button onclick="parent.document.querySelectorAll('[data-baseweb=\\'tab\\']')[1].click()" style="background:#FFFFFF; color:#174B35; border:1.5px solid #174B35; border-radius:999px; padding:0.82rem 1.8rem; font-size:1rem; font-weight:700; cursor:pointer; display:inline-flex; align-items:center; gap:0.5rem;">
                        &#9675; How It Works
                    </button>
                </div>
            </div>

            <div style="flex:1 1 400px; max-width:480px; display:flex; justify-content:center;">
                <div style="width:100%; max-width:440px; aspect-ratio:4/3; border-radius:20px; overflow:hidden; box-shadow:0 12px 32px rgba(23,75,53,0.08); border:3px solid #FFFFFF;">
                    <img src="data:image/jpeg;base64,{farmer_b64}" alt="Indian farmer using smartphone in lush green crop field" style="width:100%; height:100%; object-fit:cover; display:block;" />
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 4-Pillar Feature Strip
    st.markdown("""
    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:1.25rem; margin-bottom:2rem;">
        <div style="background:#FFFFFF; border:1.5px solid #E2E9E1; border-radius:16px; padding:1.25rem 1.4rem; display:flex; align-items:center; gap:0.85rem;">
            <div style="background:#E7F2E8; width:44px; height:44px; border-radius:12px; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                <span style="font-size:1.3rem;">🍃</span>
            </div>
            <div>
                <div style="font-size:0.95rem; font-weight:700; color:#174B35;">Crop Guidance</div>
                <div style="font-size:0.78rem; color:#68756C;">ICAR validated steps</div>
            </div>
        </div>

        <div style="background:#FFFFFF; border:1.5px solid #E2E9E1; border-radius:16px; padding:1.25rem 1.4rem; display:flex; align-items:center; gap:0.85rem;">
            <div style="background:#E7F2E8; width:44px; height:44px; border-radius:12px; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                <span style="font-size:1.3rem;">🔍</span>
            </div>
            <div>
                <div style="font-size:0.95rem; font-weight:700; color:#174B35;">Problem Identification</div>
                <div style="font-size:0.78rem; color:#68756C;">Multilingual symptom parsing</div>
            </div>
        </div>

        <div style="background:#FFFFFF; border:1.5px solid #E2E9E1; border-radius:16px; padding:1.25rem 1.4rem; display:flex; align-items:center; gap:0.85rem;">
            <div style="background:#E7F2E8; width:44px; height:44px; border-radius:12px; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                <span style="font-size:1.3rem;">🛡️</span>
            </div>
            <div>
                <div style="font-size:0.95rem; font-weight:700; color:#174B35;">Safe Recommendations</div>
                <div style="font-size:0.78rem; color:#68756C;">Zero synthetic dosage</div>
            </div>
        </div>

        <div style="background:#FFFFFF; border:1.5px solid #E2E9E1; border-radius:16px; padding:1.25rem 1.4rem; display:flex; align-items:center; gap:0.85rem;">
            <div style="background:#E7F2E8; width:44px; height:44px; border-radius:12px; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                <span style="font-size:1.3rem;">🗣️</span>
            </div>
            <div>
                <div style="font-size:0.95rem; font-weight:700; color:#174B35;">Multi-language Support</div>
                <div style="font-size:0.78rem; color:#68756C;">English, Hindi & Hinglish</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
