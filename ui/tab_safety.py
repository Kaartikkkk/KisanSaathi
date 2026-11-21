"""Safety Architecture view module for KisanSaathi.
Matches mockup media_1795286961776_09314f39.jpg.
"""

import streamlit as st
from ui.assets import BOTTOM_ORGANIC_WAVE_SVG

SAFETY_HTML = """<div class="ks-how-it-works-page">
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
                SAFETY ARCHITECTURE
            </span>
        </div>
        <h1 style="font-size:2.8rem; font-weight:800; color:#174B35; margin:0 0 0.85rem 0; letter-spacing:-0.03em;">
            Safety-First Agricultural Guardrails
        </h1>
        <p style="color:#68756C; font-size:1.08rem; line-height:1.6; margin:0;">
            Protecting crop health, soil vitality, and farmer safety through strict computational guardrails.
        </p>
    </div>

    <!-- 3 Large Safety Cards -->
    <div class="ks-arch-container">
        <!-- Card 1: Zero Chemical Dosage -->
        <div class="ks-arch-card">
            <div>
                <div class="ks-arch-icon-box">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#174B35" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                        <polyline points="9 12 11 14 15 10"></polyline>
                    </svg>
                </div>
                <h3 class="ks-arch-card-title">Zero Chemical Dosage</h3>
                <p class="ks-arch-card-desc">
                    Never computes or prescribes synthetic pesticide spraying doses, preventing crop phytotoxicity and pollinator poisoning.
                </p>
            </div>
            <!-- Illustration 1: Sprayer tank with Red Prohibition badge & Sprout -->
            <div class="ks-arch-illus">
                <svg width="230" height="135" viewBox="0 0 230 135" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <ellipse cx="120" cy="118" rx="85" ry="12" fill="#E2E9E1" opacity="0.7"/>
                    <!-- Sprouting leaves on left -->
                    <path d="M62 108 C 50 95, 52 75, 68 70 C 72 82, 68 98, 62 108 Z" fill="#3B925E"/>
                    <path d="M62 108 C 45 106, 38 92, 42 82 C 54 80, 60 92, 62 108 Z" fill="#2E7D50"/>
                    <!-- Sprayer Tank Body -->
                    <rect x="94" y="44" width="62" height="68" rx="14" fill="#FFFFFF" stroke="#174B35" stroke-width="2.5"/>
                    <!-- Sprayer Top Neck & Pump Handle -->
                    <rect x="116" y="36" width="18" height="8" rx="2" fill="#2E7D50" stroke="#174B35" stroke-width="1.5"/>
                    <path d="M110 26 H140 V31 C140 33, 138 36, 135 36 H115 C112 36, 110 33, 110 31 Z" fill="#3B925E" stroke="#174B35" stroke-width="2"/>
                    <rect x="122" y="16" width="6" height="10" rx="2" fill="#174B35"/>
                    <rect x="112" y="12" width="26" height="5" rx="2.5" fill="#174B35"/>
                    <!-- Hose running from top right down around tank -->
                    <path d="M140 34 C 158 36, 168 55, 164 78 C 160 98, 154 108, 150 110" stroke="#174B35" stroke-width="2.5" stroke-linecap="round"/>
                    <!-- Red Prohibition Badge in Center of Tank -->
                    <circle cx="125" cy="78" r="21" fill="#FFFFFF" stroke="#DC2626" stroke-width="2.5"/>
                    <!-- Chemical Flask inside circle -->
                    <path d="M122 68 L122 72 L116 82 A 2 2 0 0 0 118 85 L132 85 A 2 2 0 0 0 134 82 L128 72 L128 68 Z" fill="#DEF7EC" stroke="#174B35" stroke-width="1.2"/>
                    <!-- Red Prohibition Slash -->
                    <line x1="110" y1="63" x2="140" y2="93" stroke="#DC2626" stroke-width="2.5" stroke-linecap="round"/>
                </svg>
            </div>
        </div>

        <!-- Card 2: Evidence Grounding -->
        <div class="ks-arch-card">
            <div>
                <div class="ks-arch-icon-box">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#174B35" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                        <polygon points="12 2 2 7 12 12 22 7 12 2"></polygon>
                        <polyline points="2 17 12 22 22 17"></polyline>
                        <polyline points="2 12 12 17 22 12"></polyline>
                    </svg>
                </div>
                <h3 class="ks-arch-card-title">Evidence Grounding</h3>
                <p class="ks-arch-card-desc">
                    All possible causes are grounded in ICAR and state university agronomy reference manuals, eliminating ungrounded speculation.
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

        <!-- Card 3: Human-In-The-Loop -->
        <div class="ks-arch-card">
            <div>
                <div class="ks-arch-icon-box">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#174B35" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                        <circle cx="9" cy="7" r="4"></circle>
                        <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                        <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                    </svg>
                </div>
                <h3 class="ks-arch-card-title">Human-In-The-Loop</h3>
                <p class="ks-arch-card-desc">
                    Uncertain symptoms or rapidly spreading plots automatically trigger escalation recommendations to local extension officers (KVK).
                </p>
            </div>
            <!-- Illustration 3: Extension Officer & Checklist Clipboard -->
            <div class="ks-arch-illus">
                <svg width="230" height="135" viewBox="0 0 230 135" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <ellipse cx="120" cy="118" rx="85" ry="12" fill="#E2E9E1" opacity="0.7"/>
                    <!-- Clipboard on the left -->
                    <rect x="52" y="32" width="56" height="78" rx="8" fill="#FFFFFF" stroke="#174B35" stroke-width="2.4"/>
                    <rect x="68" y="26" width="24" height="10" rx="3" fill="#174B35"/>
                    <!-- Checkmarks & lines -->
                    <path d="M62 48 L65 51 L71 45" stroke="#2E7D50" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    <line x1="76" y1="48" x2="98" y2="48" stroke="#174B35" stroke-width="2" stroke-linecap="round"/>
                    <path d="M62 64 L65 67 L71 61" stroke="#2E7D50" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    <line x1="76" y1="64" x2="98" y2="64" stroke="#174B35" stroke-width="2" stroke-linecap="round"/>
                    <path d="M62 80 L65 83 L71 77" stroke="#2E7D50" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    <line x1="76" y1="80" x2="98" y2="80" stroke="#174B35" stroke-width="2" stroke-linecap="round"/>
                    <line x1="64" y1="94" x2="90" y2="94" stroke="#7BA887" stroke-width="2" stroke-linecap="round"/>
                    <!-- Extension Officer on the right -->
                    <path d="M120 118 C 120 102, 132 94, 146 92 L 152 92 C 166 94, 178 102, 178 118 Z" fill="#FFFFFF" stroke="#174B35" stroke-width="2.4"/>
                    <path d="M142 92 L149 104 L146 118" stroke="#174B35" stroke-width="2" stroke-linecap="round"/>
                    <path d="M156 92 L149 104" stroke="#174B35" stroke-width="2" stroke-linecap="round"/>
                    <rect x="144" y="80" width="10" height="14" fill="#FFFFFF" stroke="#174B35" stroke-width="2"/>
                    <path d="M136 56 C 136 46, 162 46, 162 56 C 162 68, 156 78, 149 78 C 142 78, 136 68, 136 56 Z" fill="#FFFFFF" stroke="#174B35" stroke-width="2.2"/>
                    <path d="M136 58 C 133 58, 133 64, 136 64" stroke="#174B35" stroke-width="2"/>
                    <!-- Cap -->
                    <path d="M133 50 C 133 36, 165 36, 165 50 Z" fill="#2E7D50" stroke="#174B35" stroke-width="2.2"/>
                    <path d="M130 50 C 140 48, 160 48, 172 53" stroke="#174B35" stroke-width="2.5" stroke-linecap="round"/>
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
</div>"""

def render_tab_safety():
    """Render the 3 safety guardrail pillars."""
    st.markdown(SAFETY_HTML, unsafe_allow_html=True)
    st.markdown(BOTTOM_ORGANIC_WAVE_SVG, unsafe_allow_html=True)
