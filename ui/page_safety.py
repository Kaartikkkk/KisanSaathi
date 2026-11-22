"""Safety Guardrails view module for KisanSaathi.
Presents the verified three-pillar safety architecture:
1. Zero Chemical Dosage
2. Evidence Grounding
3. Human-In-The-Loop
"""

import streamlit as st
from ui.assets import ICONS, ILLUSTRATIONS, DECORATIVE, get_image_base64, clean_html

def render_page_safety():
    """Render the Safety Guardrails architecture page."""
    landscape_b64 = get_image_base64("countryside-horizon.png")

    safety_html = f"""
    <div class="ks-safety-page" style="position:relative;">
        <!-- Floating Foliage Background SVGs from Asset Pack -->
        <div style="position:absolute; top:-15px; left:-10px; width:130px; height:90px; pointer-events:none; z-index:1; opacity:0.4;">
            {DECORATIVE['leaf_branch']}
        </div>
        <div style="position:absolute; top:-15px; right:-10px; width:130px; height:90px; pointer-events:none; z-index:1; opacity:0.4; transform:scaleX(-1);">
            {DECORATIVE['leaf_branch']}
        </div>

        <!-- Section Header -->
        <div style="text-align:center; max-width:760px; margin:0 auto 1.4rem auto; position:relative; z-index:2;">
            <div style="display:inline-block; margin-bottom:0.6rem;">
                <span class="ks-pill-badge" style="display:inline-flex; align-items:center; gap:6px;">
                    {ICONS['shield_check']} SAFETY ARCHITECTURE
                </span>
            </div>
            <h1 style="font-family:var(--font-heading); font-size:2.35rem; font-weight:800; color:#124C36; margin:0 0 0.5rem 0; letter-spacing:-0.03em; line-height:1.15;">
                Safety-First Agricultural Guardrails
            </h1>
            <p style="color:#64756C; font-size:1rem; line-height:1.5; margin:0;">
                Protecting crop health, soil vitality, and farmer safety through strict computational guardrails.
            </p>
        </div>

        <!-- 3 Cards with Connecting Arrows (Identical Symmetrical Geometry) -->
        <div class="ks-arch-container">
            <!-- Card 1: Zero Chemical Dosage -->
            <div class="ks-arch-card">
                <div>
                    <div class="ks-feature-icon-box">
                        {ICONS['flask_ban']}
                    </div>
                    <h3 class="ks-feature-title" style="font-size:1.15rem; color:#124C36;">1. Zero Chemical Dosage</h3>
                    <p class="ks-feature-desc">
                        Never computes or prescribes synthetic pesticide spraying doses, preventing crop phytotoxicity, soil degradation, and pollinator poisoning.
                    </p>
                </div>
                <!-- Illustration 1: No Chemical Flask -->
                <div style="display:flex; justify-content:center; align-items:center; min-height:120px; padding-top:0.75rem;">
                    <div style="width:180px; height:120px; display:flex; align-items:center; justify-content:center;">
                        {ILLUSTRATIONS['no_chemical']}
                    </div>
                </div>
                <div class="ks-feature-accent-line"></div>
            </div>

            <!-- Arrow 1 -> 2 -->
            <div class="ks-arch-arrow">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#238B52" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="5" y1="12" x2="19" y2="12"></line>
                    <polyline points="12 5 19 12 12 19"></polyline>
                </svg>
            </div>

            <!-- Card 2: Evidence Grounding -->
            <div class="ks-arch-card">
                <div>
                    <div class="ks-feature-icon-box">
                        {ICONS['book']}
                    </div>
                    <h3 class="ks-feature-title" style="font-size:1.15rem; color:#124C36;">2. Evidence Grounding</h3>
                    <p class="ks-feature-desc">
                        All possible causes and cultural interventions are grounded in ICAR and state university agronomy reference manuals, eliminating ungrounded speculation.
                    </p>
                </div>
                <!-- Illustration 2: ICAR Guidelines Stacked Book -->
                <div style="display:flex; justify-content:center; align-items:center; min-height:120px; padding-top:0.75rem;">
                    <div style="width:180px; height:120px; display:flex; align-items:center; justify-content:center;">
                        {ILLUSTRATIONS['evidence_book']}
                    </div>
                </div>
                <div class="ks-feature-accent-line"></div>
            </div>

            <!-- Arrow 2 -> 3 -->
            <div class="ks-arch-arrow">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#238B52" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="5" y1="12" x2="19" y2="12"></line>
                    <polyline points="12 5 19 12 12 19"></polyline>
                </svg>
            </div>

            <!-- Card 3: Human-In-The-Loop -->
            <div class="ks-arch-card">
                <div>
                    <div class="ks-feature-icon-box">
                        {ICONS['users']}
                    </div>
                    <h3 class="ks-feature-title" style="font-size:1.15rem; color:#124C36;">3. Human-In-The-Loop</h3>
                    <p class="ks-feature-desc">
                        Uncertain symptoms or rapidly spreading plots automatically trigger escalation recommendations to local Krishi Vigyan Kendra (KVK) extension officers.
                    </p>
                </div>
                <!-- Illustration 3: Checklist & KVK Expert -->
                <div style="display:flex; justify-content:center; align-items:center; min-height:120px; padding-top:0.75rem;">
                    <div style="width:180px; height:120px; display:flex; align-items:center; justify-content:center;">
                        {ILLUSTRATIONS['human_escalation']}
                    </div>
                </div>
                <div class="ks-feature-accent-line"></div>
            </div>
        </div>

        <!-- Scenic Countryside Horizon Banner -->
        <div class="ks-landscape-horizon" style="margin-top:1.5rem; margin-bottom:0;">
            <img src="{landscape_b64}" alt="Scenic Indian agricultural countryside horizon" />
        </div>
    </div>
    """
    st.markdown(clean_html(safety_html), unsafe_allow_html=True)
