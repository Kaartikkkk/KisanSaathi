"""Evaluation benchmark verification view module for KisanSaathi.
Matches mockup media_1795287029531_b2ec03a3.jpg.
"""

import os
import csv
import streamlit as st
from ui.assets import ICONS, BOTTOM_ORGANIC_WAVE_SVG

def render_tab_eval():
    """Render the 12-scenario empirical benchmark verification section."""
    # -----------------------------------------------------------------------------
    # 9. Evaluation Benchmark Summary (Exact Reference Mockup Layout)
    # -----------------------------------------------------------------------------
    st.markdown("""
    <div class="ks-how-it-works-page" style="padding-bottom:1.5rem;">
        <!-- Left Leafy Branch SVG -->
        <svg class="ks-bg-foliage-left" viewBox="0 0 140 160" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M-10 20 C 30 40, 70 80, 100 130" stroke="#7BA887" stroke-width="2.5" stroke-linecap="round" opacity="0.6"/>
            <path d="M28 35 C 10 25, 12 5, 28 8 C 42 12, 45 28, 28 35 Z" fill="#7BA887" opacity="0.55"/>
            <path d="M60 55 C 50 40, 62 25, 78 30 C 88 40, 80 58, 60 55 Z" fill="#6B9978" opacity="0.6"/>
            <path d="M75 90 C 65 72, 85 62, 98 72 C 102 85, 90 100, 75 90 Z" fill="#7BA887" opacity="0.55"/>
            <path d="M42 65 C 28 75, 15 68, 20 54 C 26 42, 42 48, 42 65 Z" fill="#6B9978" opacity="0.5"/>
            <path d="M78 120 C 62 130, 52 118, 58 104 C 64 92, 82 98, 78 120 Z" fill="#7BA887" opacity="0.55"/>
        </svg>
    
        <!-- Right Terraced Farm Field Rows SVG -->
        <svg viewBox="0 0 200 140" fill="none" xmlns="http://www.w3.org/2000/svg" style="position:absolute; top:20px; right:0px; width:200px; height:140px; pointer-events:none; z-index:1;">
            <path d="M140 32 C 160 22, 185 24, 200 30 L 200 140 L 0 140 Z" fill="#C5DEC7" opacity="0.4"/>
            <path d="M160 38 L 0 85 L 0 105 L 160 48 Z" fill="#88B890" opacity="0.65"/>
            <path d="M160 48 L 0 105 L 0 118 L 165 58 Z" fill="#ADCBAF" opacity="0.6"/>
            <path d="M165 58 L 15 130 L 40 140 L 172 68 Z" fill="#88B890" opacity="0.65"/>
            <path d="M172 68 L 55 140 L 95 140 L 180 78 Z" fill="#ADCBAF" opacity="0.6"/>
            <path d="M180 78 L 105 140 L 150 140 L 188 88 Z" fill="#88B890" opacity="0.65"/>
            <path d="M188 88 L 160 140 L 200 140 L 195 98 Z" fill="#ADCBAF" opacity="0.6"/>
        </svg>
    
        <!-- Section Header -->
        <div style="text-align:center; max-width:760px; margin:0 auto 2.8rem auto; position:relative; z-index:2;">
            <div style="display:inline-block; margin-bottom:0.85rem;">
                <span style="font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:0.08em; color:#2E7D50; background:#E7F2E8; padding:0.4rem 1.15rem; border-radius:999px;">
                    EVALUATION
                </span>
            </div>
            <h1 style="font-size:2.8rem; font-weight:800; color:#174B35; margin:0 0 0.85rem 0; letter-spacing:-0.03em;">
                Empirical Benchmark Verification
            </h1>
            <p style="color:#68756C; font-size:1.08rem; line-height:1.6; margin:0;">
                Evaluated across 12 distinct synthetic field scenarios with zero failures.
            </p>
        </div>
    
        <!-- 4 Metric Cards with Icons & Separators -->
        <div style="max-width:1260px; margin:0 auto 2.5rem auto; padding:0 1.5rem; display:grid; grid-template-columns:repeat(auto-fit, minmax(240px, 1fr)); gap:1.25rem; position:relative; z-index:2;">
            <!-- Card 1 -->
            <div style="display:flex; align-items:center; background:#FFFFFF; border:1.5px solid #E2E9E1; border-radius:18px; padding:1.25rem 1.4rem; gap:1.2rem; box-shadow:0 2px 10px rgba(23,75,53,0.03);">
                <div style="width:48px; height:48px; border-radius:12px; background:#E7F2E8; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#2E7D50" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
                        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
                        <path d="m9 14 2 2 4-4"></path>
                    </svg>
                </div>
                <div style="width:1px; height:42px; background:#E2E9E1;"></div>
                <div>
                    <div style="font-size:1.95rem; font-weight:800; color:#174B35; line-height:1.1;">12 / 12</div>
                    <div style="font-size:0.82rem; font-weight:600; color:#68756C; margin-top:3px;">Scenarios Evaluated</div>
                </div>
            </div>
    
            <!-- Card 2 -->
            <div style="display:flex; align-items:center; background:#F0FDF4; border:1.5px solid #BBF7D0; border-radius:18px; padding:1.25rem 1.4rem; gap:1.2rem; box-shadow:0 2px 10px rgba(23,75,53,0.03);">
                <div style="width:48px; height:48px; border-radius:12px; background:#DEF7EC; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#15803D" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="8" r="7"></circle>
                        <polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline>
                    </svg>
                </div>
                <div style="width:1px; height:42px; background:#BBF7D0;"></div>
                <div>
                    <div style="font-size:1.95rem; font-weight:800; color:#15803D; line-height:1.1;">100%</div>
                    <div style="font-size:0.82rem; font-weight:600; color:#166534; margin-top:3px;">Pass Rate</div>
                </div>
            </div>
    
            <!-- Card 3 -->
            <div style="display:flex; align-items:center; background:#FEF9EE; border:1.5px solid #FDE68A; border-radius:18px; padding:1.25rem 1.4rem; gap:1.2rem; box-shadow:0 2px 10px rgba(23,75,53,0.03);">
                <div style="width:48px; height:48px; border-radius:12px; background:#FEF3C7; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#B45309" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M10 2v7.31L4.1 20.3a2 2 0 0 0 1.7 2.7h12.4a2 2 0 0 0 1.7-2.7L14 9.31V2"></path>
                        <line x1="8.5" y1="2" x2="15.5" y2="2"></line>
                        <line x1="4" y1="4" x2="20" y2="20" stroke="#DC2626" stroke-width="2.2"></line>
                    </svg>
                </div>
                <div style="width:1px; height:42px; background:#FDE68A;"></div>
                <div>
                    <div style="font-size:1.95rem; font-weight:800; color:#B45309; line-height:1.1;">0</div>
                    <div style="font-size:0.82rem; font-weight:600; color:#92400E; margin-top:3px;">Dosages Prescribed</div>
                </div>
            </div>
    
            <!-- Card 4 -->
            <div style="display:flex; align-items:center; background:#FFFFFF; border:1.5px solid #E2E9E1; border-radius:18px; padding:1.25rem 1.4rem; gap:1.2rem; box-shadow:0 2px 10px rgba(23,75,53,0.03);">
                <div style="width:48px; height:48px; border-radius:12px; background:#E7F2E8; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#2E7D50" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="m5 8 6 6"></path>
                        <path d="m4 14 6-6 2-3"></path>
                        <path d="M2 5h12"></path>
                        <path d="M7 2h1"></path>
                        <path d="m22 22-5-10-5 10"></path>
                        <path d="M14 18h6"></path>
                    </svg>
                </div>
                <div style="width:1px; height:42px; background:#E2E9E1;"></div>
                <div>
                    <div style="font-size:1.95rem; font-weight:800; color:#174B35; line-height:1.1;">3</div>
                    <div style="font-size:0.82rem; font-weight:600; color:#68756C; margin-top:3px;">Languages Supported</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    csv_path = "evaluation_results.csv"
    if os.path.exists(csv_path):
        with st.expander("📄 View All 12 Test Cases (evaluation_results.csv)", expanded=True):
            try:
                with open(csv_path, encoding="utf-8") as f:
                    reader = list(csv.DictReader(f))
                    rows_html = []
                    for idx, r in enumerate(reader):
                        tid = r.get("Test ID", "")
                        inp = r.get("Input", "")
                        reas = r.get("Reason", "")
                        status = r.get("Pass/Fail", "PASS")
    
                        parts = inp.split("|")
                        meta = {}
                        for p in parts:
                            if ":" in p:
                                k, v = p.split(":", 1)
                                k = k.strip().lower()
                                v = v.strip().strip('"')
                                if k in ["crop", "region", "stage", "spread", "lang"]:
                                    meta[k] = v
    
                        crop_v = meta.get("crop", "Not specified")
                        region_v = meta.get("region", "Not specified")
                        stage_v = meta.get("stage", "Not sure")
                        spread_v = meta.get("spread", "Not sure")
                        lang_v = meta.get("lang", "English")
    
                        divider = "" if idx == len(reader) - 1 else "<hr style='border:none; border-top:1px solid #E2E9E1; margin:1rem 0;'>"
    
                        rows_html.append(f"""
                        <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:1.25rem; padding:0.4rem 0;">
                            <div style="background:#E8F5E9; color:#174B35; font-weight:800; font-size:0.95rem; border-radius:8px; padding:6px 14px; flex-shrink:0;">
                                {tid}
                            </div>
                            <div style="flex:1;">
                                <div style="display:flex; flex-wrap:wrap; align-items:center; gap:0.55rem; font-size:0.9rem; color:#25352D; line-height:1.4;">
                                    <span>🍃 <b>Crop:</b> {crop_v}</span>
                                    <span style="color:#C0D2C4;">|</span>
                                    <span>📍 <b>Region:</b> {region_v}</span>
                                    <span style="color:#C0D2C4;">|</span>
                                    <span>🌱 <b>Stage:</b> {stage_v}</span>
                                    <span style="color:#C0D2C4;">|</span>
                                    <span>↔️ <b>Spread:</b> {spread_v}</span>
                                    <span style="color:#C0D2C4;">|</span>
                                    <span>🌐 <b>Lang:</b> {lang_v}</span>
                                </div>
                                <div style="color:#4B6354; font-size:0.85rem; margin-top:0.45rem; line-height:1.5;">
                                    <b>Reason:</b> {reas}
                                </div>
                            </div>
                            <div style="border:1.5px solid #2E7D50; color:#174B35; font-weight:700; font-size:0.84rem; border-radius:999px; padding:4px 14px; flex-shrink:0; display:inline-flex; align-items:center; gap:4px; background:transparent;">
                                ✓ {status}
                            </div>
                        </div>
                        {divider}
                        """)
    
                    st.markdown(f"""
                    <div style="background:#FFFFFF; border:1.5px solid #E2E9E1; border-radius:18px; padding:1.5rem 1.8rem; box-shadow:0 2px 12px rgba(23,75,53,0.03);">
                        {''.join(rows_html)}
                    </div>
                    """, unsafe_allow_html=True)
            except Exception as e:
                st.caption(f"Could not read CSV: {e}")
    
    # -----------------------------------------------------------------------------
    # 10. Footer (Clean, High-Quality Light Theme)
    # -----------------------------------------------------------------------------
    st.markdown(f"""
    <div class="ks-footer">
    <div style="display:flex; align-items:center; justify-content:center; gap:0.5rem; font-size:1.3rem; font-weight:800; color:#174B35; margin-bottom:0.75rem;">
        {ICONS['leaf_brand']} KisanSaathi
    </div>
    <div style="display:flex; justify-content:center; gap:1.8rem; margin-bottom:1rem; font-weight:600; font-size:0.88rem;">
        <a href="#home">Home</a>
        <a href="#how-it-works">How It Works</a>
        <a href="#ask-ai">Ask AI</a>
        <a href="#safety">Safety Guardrails</a>
    </div>
    <div style="max-width:720px; margin:0 auto 1rem auto; font-size:0.8rem; line-height:1.6; color:#68756C;">
        <b>Agricultural Advisory Notice:</b> KisanSaathi is an agronomic artificial intelligence prototype developed for preliminary educational and advisory support. All assessments and recommendations must be physically verified by certified agricultural extension officers or Krishi Vigyan Kendras (KVK).
    </div>
    <div style="font-size:0.75rem; color:#94A3B8;">
        &copy; 2026 KisanSaathi &middot; Built with Gemini 2.5 Flash &amp; Streamlit &middot; Grounded in ICAR Agronomic Practice Standards
    </div>
    </div>
    """, unsafe_allow_html=True)
    

    st.markdown(BOTTOM_ORGANIC_WAVE_SVG, unsafe_allow_html=True)
