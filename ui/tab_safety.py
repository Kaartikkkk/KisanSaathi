"""Safety Architecture view module for KisanSaathi.
Integrates the complete KisanSaathi Visual Asset Pack:
- Safety icons from assets/icons/ (flask-ban, book, users)
- Vector illustrations from assets/illustrations/ (no-chemical, evidence-book, human-escalation)
- Decorative elements from assets/decorative/ (leaf-branch)
- Scenic Countryside Horizon Banner matching reference design
"""

import streamlit as st
from ui.assets import ICONS, ILLUSTRATIONS, DECORATIVE, get_image_base64, clean_html

def render_tab_safety():
    """Render the Safety Guardrails architecture page."""
    landscape_horizon_b64 = get_image_base64("countryside-horizon.png")

    safety_html = f"""
    <div class="ks-safety-page" style="position:relative;">
        <!-- Floating Foliage Background SVGs from Asset Pack -->
        <div style="position:absolute; top:0; left:0; width:130px; height:90px; pointer-events:none; z-index:1; opacity:0.4;">
            {DECORATIVE['leaf_branch']}
        </div>
        <div style="position:absolute; top:0; right:0; width:130px; height:90px; pointer-events:none; z-index:1; opacity:0.4; transform:scaleX(-1);">
            {DECORATIVE['leaf_branch']}
        </div>

        <!-- Section Header -->
        <div style="text-align:center; max-width:760px; margin:0 auto 1.4rem auto; position:relative; z-index:2;">
            <div style="display:inline-block; margin-bottom:0.6rem;">
                <span class="ks-pill-badge" style="display:inline-flex; align-items:center; gap:6px;">
                    {ICONS['shield_check']} SAFETY ARCHITECTURE
                </span>
            </div>
            <h1 style="font-size:2.35rem; font-weight:800; color:#174B35; margin:0 0 0.5rem 0; letter-spacing:-0.03em; line-height:1.15;">
                Safety-First Agricultural Guardrails
            </h1>
            <p style="color:#5A6860; font-size:1rem; line-height:1.5; margin:0;">
                Protecting crop health, soil vitality, and farmer safety through strict computational guardrails.
            </p>
        </div>

        <!-- 3 Large Safety Cards -->
        <div class="ks-arch-container">
            <!-- Card 1: Zero Chemical Dosage -->
            <div class="ks-arch-card">
                <div>
                    <div class="ks-arch-icon-box">
                        {ICONS['flask_ban']}
                    </div>
                    <h3 class="ks-arch-card-title">Zero Chemical Dosage</h3>
                    <p class="ks-arch-card-desc">
                        Never computes or prescribes synthetic pesticide spraying doses, preventing crop phytotoxicity, soil degradation, and pollinator poisoning.
                    </p>
                </div>
                <!-- Illustration 1 from Visual Asset Pack -->
                <div class="ks-arch-illus" style="display:flex; justify-content:center; align-items:center; min-height:120px;">
                    <div style="width:140px; height:120px; display:flex; align-items:center; justify-content:center;">
                        {ILLUSTRATIONS['no_chemical']}
                    </div>
                </div>
                <div class="ks-feature-accent-line"></div>
            </div>

            <!-- Card 2: Evidence Grounding -->
            <div class="ks-arch-card">
                <div>
                    <div class="ks-arch-icon-box">
                        {ICONS['book']}
                    </div>
                    <h3 class="ks-arch-card-title">Evidence Grounding</h3>
                    <p class="ks-arch-card-desc">
                        All possible causes and cultural interventions are grounded in ICAR and state university agronomy reference manuals, eliminating ungrounded speculation.
                    </p>
                </div>
                <!-- Illustration 2 from Visual Asset Pack -->
                <div class="ks-arch-illus" style="display:flex; justify-content:center; align-items:center; min-height:120px;">
                    <div style="width:180px; height:120px; display:flex; align-items:center; justify-content:center;">
                        {ILLUSTRATIONS['evidence_book']}
                    </div>
                </div>
                <div class="ks-feature-accent-line"></div>
            </div>

            <!-- Card 3: Human-In-The-Loop -->
            <div class="ks-arch-card">
                <div>
                    <div class="ks-arch-icon-box">
                        {ICONS['users']}
                    </div>
                    <h3 class="ks-arch-card-title">Human-In-The-Loop</h3>
                    <p class="ks-arch-card-desc">
                        Uncertain symptoms or rapidly spreading plots automatically trigger escalation recommendations to local Krishi Vigyan Kendra (KVK) extension officers.
                    </p>
                </div>
                <!-- Illustration 3 from Visual Asset Pack -->
                <div class="ks-arch-illus" style="display:flex; justify-content:center; align-items:center; min-height:120px;">
                    <div style="width:190px; height:120px; display:flex; align-items:center; justify-content:center;">
                        {ILLUSTRATIONS['human_escalation']}
                    </div>
                </div>
                <div class="ks-feature-accent-line"></div>
            </div>
        </div>

        <!-- Scenic Countryside Horizon Decoration -->
        <div class="ks-landscape-horizon" style="margin-top:1.5rem; margin-bottom:0;">
            <img src="{landscape_horizon_b64}" alt="Scenic Indian agricultural countryside horizon" />
        </div>
    </div>
    """
    st.markdown(clean_html(safety_html), unsafe_allow_html=True)
