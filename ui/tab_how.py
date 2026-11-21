"""How It Works Architecture view module for KisanSaathi.
Integrates the complete KisanSaathi Visual Asset Pack:
- Workflow icons from assets/icons/ (search, layers, shield-check)
- Vector illustrations from assets/illustrations/ (evidence-book, human-escalation)
- Decorative elements from assets/decorative/ (leaf-branch, field-hills)
"""

import streamlit as st
from ui.assets import ICONS, ILLUSTRATIONS, DECORATIVE, clean_html

def render_tab_how():
    """Render the 3-stage architecture workflow."""
    how_html = f"""
    <div class="ks-how-it-works-page" style="position:relative;">
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
                <span class="ks-pill-badge">SYSTEM ARCHITECTURE</span>
            </div>
            <h1 style="font-size:2.35rem; font-weight:800; color:#174B35; margin:0 0 0.5rem 0; letter-spacing:-0.03em; line-height:1.15;">
                How KisanSaathi Works
            </h1>
            <p style="color:#5A6860; font-size:1rem; line-height:1.5; margin:0;">
                A grounded three-stage prompt workflow ensuring verified agronomic advice with zero chemical dosage hallucination.
            </p>
        </div>

        <!-- 3 Cards with Connecting Arrows -->
        <div class="ks-arch-container">
            <!-- Card 1: Multi-Lingual Extraction -->
            <div class="ks-arch-card">
                <div>
                    <div class="ks-arch-icon-box">
                        {ICONS['search']}
                    </div>
                    <h3 class="ks-arch-card-title">1. Multi-Lingual Extraction</h3>
                    <p class="ks-arch-card-desc">
                        Understands farmer queries in English, Hindi, and Hinglish. Extracts crop, region, phenological stage, symptoms, and spread rate.
                    </p>
                </div>
                <!-- Illustration 1: Document with speech bubbles -->
                <div class="ks-arch-illus" style="display:flex; justify-content:center; align-items:center; min-height:120px;">
                    <svg width="200" height="110" viewBox="0 0 230 135" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <rect x="80" y="24" width="70" height="96" rx="8" fill="#FFFFFF" stroke="#2F8A57" stroke-width="2.2"/>
                        <line x1="94" y1="44" x2="136" y2="44" stroke="#2F8A57" stroke-width="2.2" stroke-linecap="round"/>
                        <line x1="94" y1="58" x2="136" y2="58" stroke="#2F8A57" stroke-width="2.2" stroke-linecap="round"/>
                        <line x1="94" y1="72" x2="124" y2="72" stroke="#2F8A57" stroke-width="2.2" stroke-linecap="round"/>
                        <line x1="94" y1="86" x2="136" y2="86" stroke="#2F8A57" stroke-width="2.2" stroke-linecap="round"/>
                        <line x1="94" y1="100" x2="116" y2="100" stroke="#2F8A57" stroke-width="2.2" stroke-linecap="round"/>
                        <g>
                            <rect x="18" y="20" width="56" height="28" rx="14" fill="#E7F2E8" stroke="#2F8A57" stroke-width="1.5"/>
                            <text x="46" y="38" font-family="Inter, sans-serif" font-size="11.5" font-weight="700" fill="#174B35" text-anchor="middle">Hindi</text>
                            <path d="M52 47 L60 56 L64 47 Z" fill="#E7F2E8" stroke="#2F8A57" stroke-width="1.5"/>
                        </g>
                        <g>
                            <rect x="146" y="14" width="66" height="28" rx="14" fill="#E7F2E8" stroke="#2F8A57" stroke-width="1.5"/>
                            <text x="179" y="32" font-family="Inter, sans-serif" font-size="11.5" font-weight="700" fill="#174B35" text-anchor="middle">English</text>
                            <path d="M156 41 L148 50 L162 43 Z" fill="#E7F2E8" stroke="#2F8A57" stroke-width="1.5"/>
                        </g>
                        <g>
                            <rect x="148" y="76" width="68" height="28" rx="14" fill="#E7F2E8" stroke="#2F8A57" stroke-width="1.5"/>
                            <text x="182" y="94" font-family="Inter, sans-serif" font-size="11.5" font-weight="700" fill="#174B35" text-anchor="middle">Hinglish</text>
                            <path d="M158 77 L148 70 L160 76 Z" fill="#E7F2E8" stroke="#2F8A57" stroke-width="1.5"/>
                        </g>
                    </svg>
                </div>
            </div>

            <!-- Arrow 1 -> 2 -->
            <div class="ks-arch-arrow">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#2F8A57" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="5" y1="12" x2="19" y2="12"></line>
                    <polyline points="12 5 19 12 12 19"></polyline>
                </svg>
            </div>

            <!-- Card 2: Grounded TF-IDF Retrieval -->
            <div class="ks-arch-card">
                <div>
                    <div class="ks-arch-icon-box">
                        {ICONS['layers']}
                    </div>
                    <h3 class="ks-arch-card-title">2. Grounded TF-IDF Retrieval</h3>
                    <p class="ks-arch-card-desc">
                        Matches symptom profiles against ICAR agronomic reference materials. Every diagnosis is grounded in verified literature citations.
                    </p>
                </div>
                <!-- Illustration 2 from Visual Asset Pack -->
                <div class="ks-arch-illus" style="display:flex; justify-content:center; align-items:center; min-height:120px;">
                    <div style="width:130px; height:120px; display:flex; align-items:center; justify-content:center;">
                        {ILLUSTRATIONS['evidence_book']}
                    </div>
                </div>
            </div>

            <!-- Arrow 2 -> 3 -->
            <div class="ks-arch-arrow">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#2F8A57" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="5" y1="12" x2="19" y2="12"></line>
                    <polyline points="12 5 19 12 12 19"></polyline>
                </svg>
            </div>

            <!-- Card 3: Safe Advisory & Escalation -->
            <div class="ks-arch-card">
                <div>
                    <div class="ks-arch-icon-box">
                        {ICONS['shield_check']}
                    </div>
                    <h3 class="ks-arch-card-title">3. Safe Advisory & Escalation</h3>
                    <p class="ks-arch-card-desc">
                        Generates cultural management checklists, asks follow-up questions for missing details, and escalates to KVK experts when needed.
                    </p>
                </div>
                <!-- Illustration 3 from Visual Asset Pack -->
                <div class="ks-arch-illus" style="display:flex; justify-content:center; align-items:center; min-height:120px;">
                    <div style="width:130px; height:120px; display:flex; align-items:center; justify-content:center;">
                        {ILLUSTRATIONS['human_escalation']}
                    </div>
                </div>
            </div>
        </div>

        <!-- Bottom Landscape Hills Decoration -->
        <div style="width:100%; overflow:hidden; line-height:0; margin-top:1.5rem; opacity:0.65;">
            {DECORATIVE['field_hills']}
        </div>
    </div>
    """
    st.markdown(clean_html(how_html), unsafe_allow_html=True)
