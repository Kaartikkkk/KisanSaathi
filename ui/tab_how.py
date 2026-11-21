"""How It Works Architecture view module for KisanSaathi.
Matches mockup media_1795286699297_c6bbf8cd.jpg.
"""

import streamlit as st
from ui.assets import BOTTOM_ORGANIC_WAVE_SVG

def render_tab_how():
    """Render the 3-stage architecture workflow."""
    # -----------------------------------------------------------------------------
    # 4. How It Works Section (Exact Reference Mockup Layout)
    # -----------------------------------------------------------------------------
    st.markdown("""
    <div class="ks-how-it-works-page">
        <!-- Floating Foliage Background SVGs -->
        <svg class="ks-bg-foliage-left" viewBox="0 0 140 160" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M-10 20 C 30 40, 70 80, 100 130" stroke="#7BA887" stroke-width="2.5" stroke-linecap="round" opacity="0.6"/>
            <path d="M28 35 C 10 25, 12 5, 28 8 C 42 12, 45 28, 28 35 Z" fill="#7BA887" opacity="0.55"/>
            <path d="M60 55 C 50 40, 62 25, 78 30 C 88 40, 80 58, 60 55 Z" fill="#6B9978" opacity="0.6"/>
            <path d="M75 90 C 65 72, 85 62, 98 72 C 102 85, 90 100, 75 90 Z" fill="#7BA887" opacity="0.55"/>
            <path d="M42 65 C 28 75, 15 68, 20 54 C 26 42, 42 48, 42 65 Z" fill="#6B9978" opacity="0.5"/>
            <path d="M78 120 C 62 130, 52 118, 58 104 C 64 92, 82 98, 78 120 Z" fill="#7BA887" opacity="0.55"/>
        </svg>
        <svg class="ks-bg-foliage-right" viewBox="0 0 140 160" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M150 20 C 110 40, 70 80, 40 130" stroke="#7BA887" stroke-width="2.5" stroke-linecap="round" opacity="0.6"/>
            <path d="M112 35 C 130 25, 128 5, 112 8 C 98 12, 95 28, 112 35 Z" fill="#7BA887" opacity="0.55"/>
            <path d="M80 55 C 90 40, 78 25, 62 30 C 52 40, 60 58, 80 55 Z" fill="#6B9978" opacity="0.6"/>
            <path d="M65 90 C 75 72, 55 62, 42 72 C 38 85, 50 100, 65 90 Z" fill="#7BA887" opacity="0.55"/>
            <path d="M98 65 C 112 75, 125 68, 120 54 C 114 42, 98 48, 98 65 Z" fill="#6B9978" opacity="0.5"/>
            <path d="M62 120 C 78 130, 88 118, 82 104 C 76 92, 58 98, 62 120 Z" fill="#7BA887" opacity="0.55"/>
        </svg>
    
        <!-- Section Header -->
        <div style="text-align:center; max-width:760px; margin:0 auto 3.2rem auto; position:relative; z-index:2;">
            <div style="display:inline-block; margin-bottom:0.85rem;">
                <span style="font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:0.08em; color:#2E7D50; background:#E7F2E8; padding:0.4rem 1.15rem; border-radius:999px;">
                    SYSTEM ARCHITECTURE
                </span>
            </div>
            <h1 style="font-size:2.8rem; font-weight:800; color:#174B35; margin:0 0 0.85rem 0; letter-spacing:-0.03em;">
                How KisanSaathi Works
            </h1>
            <p style="color:#68756C; font-size:1.08rem; line-height:1.6; margin:0;">
                A grounded three-stage prompt workflow ensuring verified agronomic advice with zero chemical dosage hallucination.
            </p>
        </div>
    
        <!-- 3 Cards with Connecting Arrows -->
        <div class="ks-arch-container">
            <!-- Card 1 -->
            <div class="ks-arch-card">
                <div>
                    <div class="ks-arch-icon-box">
                        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#174B35" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                            <circle cx="11" cy="11" r="8"></circle>
                            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                        </svg>
                    </div>
                    <h3 class="ks-arch-card-title">1. Multi-Lingual Extraction</h3>
                    <p class="ks-arch-card-desc">
                        Understands farmer queries in English, Hindi, and Hinglish. Extracts crop, region, phenological stage, symptoms, and spread rate.
                    </p>
                </div>
                <!-- Illustration 1: Document with speech bubbles -->
                <div class="ks-arch-illus">
                    <svg width="230" height="135" viewBox="0 0 230 135" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <rect x="80" y="24" width="70" height="96" rx="8" fill="#FFFFFF" stroke="#2E7D50" stroke-width="2.2"/>
                        <line x1="94" y1="44" x2="136" y2="44" stroke="#2E7D50" stroke-width="2.2" stroke-linecap="round"/>
                        <line x1="94" y1="58" x2="136" y2="58" stroke="#2E7D50" stroke-width="2.2" stroke-linecap="round"/>
                        <line x1="94" y1="72" x2="124" y2="72" stroke="#2E7D50" stroke-width="2.2" stroke-linecap="round"/>
                        <line x1="94" y1="86" x2="136" y2="86" stroke="#2E7D50" stroke-width="2.2" stroke-linecap="round"/>
                        <line x1="94" y1="100" x2="116" y2="100" stroke="#2E7D50" stroke-width="2.2" stroke-linecap="round"/>
                        <!-- Bubble: Hindi -->
                        <g>
                            <rect x="18" y="20" width="56" height="28" rx="14" fill="#E7F2E8" stroke="#2E7D50" stroke-width="1.5"/>
                            <text x="46" y="38" font-family="Inter, sans-serif" font-size="11.5" font-weight="700" fill="#174B35" text-anchor="middle">Hindi</text>
                            <path d="M52 47 L60 56 L64 47 Z" fill="#E7F2E8" stroke="#2E7D50" stroke-width="1.5"/>
                            <line x1="53" y1="47" x2="63" y2="47" stroke="#E7F2E8" stroke-width="2"/>
                        </g>
                        <!-- Bubble: English -->
                        <g>
                            <rect x="146" y="14" width="66" height="28" rx="14" fill="#E7F2E8" stroke="#2E7D50" stroke-width="1.5"/>
                            <text x="179" y="32" font-family="Inter, sans-serif" font-size="11.5" font-weight="700" fill="#174B35" text-anchor="middle">English</text>
                            <path d="M156 41 L148 50 L162 43 Z" fill="#E7F2E8" stroke="#2E7D50" stroke-width="1.5"/>
                            <line x1="154" y1="41" x2="161" y2="41" stroke="#E7F2E8" stroke-width="2"/>
                        </g>
                        <!-- Bubble: Hinglish -->
                        <g>
                            <rect x="148" y="76" width="68" height="28" rx="14" fill="#E7F2E8" stroke="#2E7D50" stroke-width="1.5"/>
                            <text x="182" y="94" font-family="Inter, sans-serif" font-size="11.5" font-weight="700" fill="#174B35" text-anchor="middle">Hinglish</text>
                            <path d="M158 77 L148 70 L160 76 Z" fill="#E7F2E8" stroke="#2E7D50" stroke-width="1.5"/>
                            <line x1="156" y1="77" x2="161" y2="77" stroke="#E7F2E8" stroke-width="2"/>
                        </g>
                    </svg>
                </div>
            </div>
    
            <!-- Arrow 1 -> 2 -->
            <div class="ks-arch-arrow">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#2E7D50" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="5" y1="12" x2="19" y2="12"></line>
                    <polyline points="12 5 19 12 12 19"></polyline>
                </svg>
            </div>
    
            <!-- Card 2 -->
            <div class="ks-arch-card">
                <div>
                    <div class="ks-arch-icon-box">
                        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#174B35" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                            <polygon points="12 2 2 7 12 12 22 7 12 2"></polygon>
                            <polyline points="2 17 12 22 22 17"></polyline>
                            <polyline points="2 12 12 17 22 12"></polyline>
                        </svg>
                    </div>
                    <h3 class="ks-arch-card-title">2. Grounded TF-IDF Retrieval</h3>
                    <p class="ks-arch-card-desc">
                        Matches symptom profiles against ICAR agronomic reference materials. Every diagnosis is grounded in verified literature citations.
                    </p>
                </div>
                <!-- Illustration 2: 3D ICAR Book -->
                <div class="ks-arch-illus">
                    <svg width="230" height="135" viewBox="0 0 230 135" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <ellipse cx="115" cy="116" rx="78" ry="12" fill="#E2E9E1"/>
                        <path d="M52 84 L114 106 L178 84 L178 72 L114 94 L52 72 Z" fill="#D6E8D8"/>
                        <path d="M52 78 L114 100 L178 78 L178 68 L114 90 L52 68 Z" fill="#F7F8F2" stroke="#D6E8D8"/>
                        <path d="M50 72 L114 94 L180 72 L116 50 Z" fill="#2E7D50"/>
                        <path d="M50 70 L114 92 L180 70 L116 48 Z" fill="#3B925E"/>
                        <g transform="rotate(18, 114, 68) skewX(-24)">
                            <text x="86" y="73" font-family="Inter, sans-serif" font-size="14.5" font-weight="800" fill="#FFFFFF" letter-spacing="2">ICAR</text>
                        </g>
                        <path d="M112 92 L112 112 L117 107 L122 112 L122 92 Z" fill="#D97706"/>
                    </svg>
                </div>
            </div>
    
            <!-- Arrow 2 -> 3 -->
            <div class="ks-arch-arrow">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#2E7D50" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="5" y1="12" x2="19" y2="12"></line>
                    <polyline points="12 5 19 12 12 19"></polyline>
                </svg>
            </div>
    
            <!-- Card 3 -->
            <div class="ks-arch-card">
                <div>
                    <div class="ks-arch-icon-box">
                        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#174B35" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                            <polyline points="9 12 11 14 15 10"></polyline>
                        </svg>
                    </div>
                    <h3 class="ks-arch-card-title">3. Safe Advisory & Escalation</h3>
                    <p class="ks-arch-card-desc">
                        Generates cultural management checklists, asks follow-up questions for missing details, and escalates to KVK experts when needed.
                    </p>
                </div>
                <!-- Illustration 3: Clipboard Checklist & Leaf -->
                <div class="ks-arch-illus">
                    <svg width="230" height="135" viewBox="0 0 230 135" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <rect x="80" y="22" width="70" height="96" rx="8" fill="#FFFFFF" stroke="#2E7D50" stroke-width="2.2"/>
                        <rect x="96" y="14" width="38" height="16" rx="4" fill="#174B35"/>
                        <rect x="104" y="18" width="22" height="6" rx="2" fill="#E7F2E8"/>
                        <!-- Checkmark 1 -->
                        <path d="M90 48 L95 53 L104 43" stroke="#2E7D50" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
                        <line x1="110" y1="48" x2="138" y2="48" stroke="#2E7D50" stroke-width="2" stroke-linecap="round"/>
                        <!-- Checkmark 2 -->
                        <path d="M90 66 L95 71 L104 61" stroke="#2E7D50" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
                        <line x1="110" y1="66" x2="138" y2="66" stroke="#2E7D50" stroke-width="2" stroke-linecap="round"/>
                        <!-- Checkmark 3 -->
                        <path d="M90 84 L95 89 L104 79" stroke="#2E7D50" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
                        <line x1="110" y1="84" x2="138" y2="84" stroke="#2E7D50" stroke-width="2" stroke-linecap="round"/>
                        <!-- Dot line 4 -->
                        <circle cx="95" cy="100" r="3.5" fill="#2E7D50"/>
                        <line x1="110" y1="100" x2="130" y2="100" stroke="#2E7D50" stroke-width="2" stroke-linecap="round"/>
                        <!-- Leaf Sprout on Right -->
                        <path d="M156 108 C 154 92, 166 84, 172 75 C 174 86, 165 98, 160 108" fill="#3B925E"/>
                        <path d="M158 95 C 168 90, 180 90, 184 97 C 178 101, 165 101, 158 95" fill="#2E7D50"/>
                        <path d="M158 102 C 148 98, 140 102, 138 108 C 144 110, 153 106, 158 102" fill="#3B925E"/>
                    </svg>
                </div>
            </div>
        </div>
    
        <!-- Bottom Landscape Wave -->
        <div style="width:100%; overflow:hidden; line-height:0; margin-top:4rem;">
            <svg viewBox="0 0 1440 90" fill="none" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto;">
                <path d="M0 45 C 360 85, 720 15, 1080 65 C 1260 85, 1380 60, 1440 50 L 1440 90 L 0 90 Z" fill="#DCEBDE" opacity="0.6"/>
                <path d="M0 65 C 400 95, 800 35, 1200 75 L 1440 60 L 1440 90 L 0 90 Z" fill="#C7DFC8" opacity="0.75"/>
            </svg>
        </div>
    </div>
    """, unsafe_allow_html=True)
    

    st.markdown(BOTTOM_ORGANIC_WAVE_SVG, unsafe_allow_html=True)
