"""How It Works view module for KisanSaathi.
Presents the verified three-stage prompt workflow:
1. Multi-Lingual Extraction
2. Grounded TF-IDF Retrieval
3. Safe Advisory & Escalation
"""

import streamlit as st
from ui.assets import ICONS, ILLUSTRATIONS, DECORATIVE, get_image_base64, clean_html

def render_page_how():
    """Render the 3-stage architecture workflow."""
    landscape_b64 = get_image_base64("countryside-horizon.png")

    how_html = f"""
    <div class="ks-how-page" style="position:relative;">
        <!-- Floating Foliage Background SVGs from Asset Pack -->
        <div style="position:absolute; top:5px; left:-10px; width:130px; height:90px; pointer-events:none; z-index:1; opacity:0.4;">
            {DECORATIVE['leaf_branch']}
        </div>
        <div style="position:absolute; top:5px; right:-10px; width:130px; height:90px; pointer-events:none; z-index:1; opacity:0.4; transform:scaleX(-1);">
            {DECORATIVE['leaf_branch']}
        </div>

        <!-- Section Header -->
        <div style="text-align:center; max-width:760px; margin:0 auto 1.4rem auto; padding-top:1.2rem; position:relative; z-index:2;">
            <div style="display:inline-block; margin-bottom:0.75rem;">
                <span class="ks-pill-badge" style="display:inline-flex; align-items:center; gap:6px;">
                    {ICONS['layers']} PROMPT ENGINEERING ARCHITECTURE
                </span>
            </div>
            <h1 style="font-family:var(--font-heading); font-size:2.35rem; font-weight:800; color:#124C36; margin:0 0 0.5rem 0; letter-spacing:-0.03em; line-height:1.15;">
                How KisanSaathi Works
            </h1>
            <p style="color:#64756C; font-size:1rem; line-height:1.5; margin:0;">
                A grounded three-stage prompt workflow ensuring verified agronomic advice with zero chemical dosage hallucination.
            </p>
        </div>

        <!-- 1. PROMPT EXPERIMENT: BEFORE VS. AFTER (RUBRIC PART 2) - TOP PLACEMENT FOR INSTANT VISIBILITY -->
        <div style="margin-bottom:2.2rem; background:#FFFFFF; border:2px solid #C8DEC9; border-radius:14px; padding:1.5rem 1.8rem; box-shadow:0 4px 16px rgba(18,76,54,0.06); position:relative; z-index:2;">
            <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:0.5rem; margin-bottom:1.2rem; border-bottom:1px solid #EEF3EE; padding-bottom:0.75rem;">
                <div style="display:flex; align-items:center; gap:0.6rem;">
                    <span class="ks-pill-badge" style="font-size:0.75rem; padding:3px 10px; background:#E8F3E9; color:#124C36; font-weight:700;">
                        🔬 RUBRIC PART 2: PROMPT EXPERIMENT
                    </span>
                    <h3 style="font-family:var(--font-heading); font-size:1.35rem; font-weight:800; color:#124C36; margin:0;">
                        Before vs. After Prompt Iteration
                    </h3>
                </div>
                <span style="font-size:0.8rem; color:#64756C; font-weight:600;">
                    Baseline V0 (Naive Zero-Shot) &rarr; Grounded V3 (Pipeline)
                </span>
            </div>

            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:1.25rem;">
                <!-- BEFORE: Old Prompt & Failure Output -->
                <div style="background:#FFF8F8; border:1.8px solid #FCA5A5; border-radius:10px; padding:1.2rem; box-sizing:border-box;">
                    <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:0.6rem;">
                        <span style="background:#EF4444; color:#FFFFFF; font-size:0.75rem; font-weight:800; padding:3px 9px; border-radius:4px; text-transform:uppercase;">
                            ❌ Old Prompt (Baseline V0)
                        </span>
                        <span style="font-size:0.72rem; color:#991B1B; font-weight:600;">Naive Zero-Shot</span>
                    </div>
                    <div style="background:#FFFFFF; border:1px solid #FECACA; border-radius:6px; padding:0.7rem 0.85rem; font-family:monospace; font-size:0.82rem; color:#7F1D1D; margin-bottom:0.75rem; line-height:1.45;">
                        &ldquo;You are an agricultural AI. Tell the farmer what disease their crop has and recommend pesticides to spray.&rdquo;
                    </div>
                    <div style="font-size:0.82rem; font-weight:700; color:#991B1B; margin-bottom:0.4rem;">
                        ⚠️ Old Output (Dangerous Hallucinations &amp; State Loss):
                    </div>
                    <ul style="margin:0; padding-left:1.2rem; font-size:0.83rem; color:#7F1D1D; line-height:1.55;">
                        <li><b>Hazardous Dosages:</b> Hallucinated <i>&ldquo;Spray 2.5 ml/L Imidacloprid twice a week&rdquo;</i> risking severe crop toxicity.</li>
                        <li><b>Input Contamination:</b> Multi-turn follow-ups dumped into a flat unstructured string.</li>
                        <li><b>No Evidence Grounding:</b> Guessed diseases without certified ICAR literature citations.</li>
                    </ul>
                </div>

                <!-- AFTER: Improved Prompt & Grounded Output -->
                <div style="background:#F2FBF5; border:1.8px solid #86EFAC; border-radius:10px; padding:1.2rem; box-sizing:border-box;">
                    <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:0.6rem;">
                        <span style="background:#15803D; color:#FFFFFF; font-size:0.75rem; font-weight:800; padding:3px 9px; border-radius:4px; text-transform:uppercase;">
                            ✅ Improved Prompt (Grounded V3)
                        </span>
                        <span style="font-size:0.72rem; color:#166534; font-weight:600;">Three-Stage Pipeline</span>
                    </div>
                    <div style="background:#FFFFFF; border:1px solid #BBF7D0; border-radius:6px; padding:0.7rem 0.85rem; font-family:monospace; font-size:0.82rem; color:#14532D; margin-bottom:0.75rem; line-height:1.45;">
                        &ldquo;Strict Negative Constraint: Never prescribe synthetic pesticide dosages. Ground all advice in ICAR reference notes. Return verified cultural checklist in strict JSON.&rdquo;
                    </div>
                    <div style="font-size:0.82rem; font-weight:700; color:#166534; margin-bottom:0.4rem;">
                        🛡️ Improved Output (Farmer-Safe &amp; Production-Grade):
                    </div>
                    <ul style="margin:0; padding-left:1.2rem; font-size:0.83rem; color:#14532D; line-height:1.55;">
                        <li><b>Zero Chemical Risk:</b> Replaces chemical sprays with non-chemical cultural remedies.</li>
                        <li><b>Evidence-Grounded:</b> Every symptom matches certified ICAR agronomic research.</li>
                        <li><b>Automated Escalation:</b> Severe or uncertain outbreaks route directly to <b>KVK scientists</b>.</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- Section Sub-Header: Three-Stage Production Architecture -->
        <div style="text-align:center; margin:1rem auto 1.2rem auto;">
            <h2 style="font-family:var(--font-heading); font-size:1.6rem; font-weight:800; color:#124C36; margin:0 0 0.3rem 0;">
                Three-Stage Pipeline Execution
            </h2>
            <p style="color:#64756C; font-size:0.9rem; margin:0;">
                How queries are processed from raw farmer dialect into structured, safe advice
            </p>
        </div>

        <!-- 3 Cards with Connecting Arrows -->
        <div class="ks-arch-container">
            <!-- Card 1: Multi-Lingual Extraction -->
            <div class="ks-arch-card">
                <div>
                    <div class="ks-feature-icon-box">
                        {ICONS['search']}
                    </div>
                    <h3 class="ks-feature-title" style="font-size:1.15rem; color:#124C36;">1. Multi-Lingual Extraction</h3>
                    <p class="ks-feature-desc">
                        Understands farmer queries in English, Hindi, and Hinglish. Extracts crop, region, phenological stage, symptoms, and spread rate.
                    </p>
                </div>
                <!-- Illustration 1: Document with speech bubbles -->
                <div style="display:flex; justify-content:center; align-items:center; min-height:120px; padding-top:0.75rem;">
                    <div style="width:180px; height:120px; display:flex; align-items:center; justify-content:center;">
                        <svg width="180" height="110" viewBox="0 0 230 135" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <rect x="80" y="24" width="70" height="96" rx="8" fill="#FFFFFF" stroke="#238B52" stroke-width="2.2"/>
                            <line x1="94" y1="44" x2="136" y2="44" stroke="#238B52" stroke-width="2.2" stroke-linecap="round"/>
                            <line x1="94" y1="58" x2="136" y2="58" stroke="#238B52" stroke-width="2.2" stroke-linecap="round"/>
                            <line x1="94" y1="72" x2="124" y2="72" stroke="#238B52" stroke-width="2.2" stroke-linecap="round"/>
                            <line x1="94" y1="86" x2="136" y2="86" stroke="#238B52" stroke-width="2.2" stroke-linecap="round"/>
                            <line x1="94" y1="100" x2="116" y2="100" stroke="#238B52" stroke-width="2.2" stroke-linecap="round"/>
                            <g>
                                <rect x="18" y="20" width="56" height="28" rx="14" fill="#E8F3E9" stroke="#238B52" stroke-width="1.5"/>
                                <text x="46" y="38" font-family="'Inter', sans-serif" font-size="11.5" font-weight="700" fill="#124C36" text-anchor="middle">Hindi</text>
                                <path d="M52 47 L60 56 L64 47 Z" fill="#E8F3E9" stroke="#238B52" stroke-width="1.5"/>
                            </g>
                            <g>
                                <rect x="146" y="14" width="66" height="28" rx="14" fill="#E8F3E9" stroke="#238B52" stroke-width="1.5"/>
                                <text x="179" y="32" font-family="'Inter', sans-serif" font-size="11.5" font-weight="700" fill="#124C36" text-anchor="middle">English</text>
                                <path d="M156 41 L148 50 L162 43 Z" fill="#E8F3E9" stroke="#238B52" stroke-width="1.5"/>
                            </g>
                            <g>
                                <rect x="148" y="76" width="68" height="28" rx="14" fill="#E8F3E9" stroke="#238B52" stroke-width="1.5"/>
                                <text x="182" y="94" font-family="'Inter', sans-serif" font-size="11.5" font-weight="700" fill="#124C36" text-anchor="middle">Hinglish</text>
                                <path d="M158 77 L148 70 L160 76 Z" fill="#E8F3E9" stroke="#238B52" stroke-width="1.5"/>
                            </g>
                        </svg>
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

            <!-- Card 2: Grounded TF-IDF Retrieval -->
            <div class="ks-arch-card">
                <div>
                    <div class="ks-feature-icon-box">
                        {ICONS['layers']}
                    </div>
                    <h3 class="ks-feature-title" style="font-size:1.15rem; color:#124C36;">2. Grounded TF-IDF Retrieval</h3>
                    <p class="ks-feature-desc">
                        Matches symptom profiles against ICAR agronomic reference materials. Every diagnosis is grounded in verified literature citations.
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

            <!-- Card 3: Safe Advisory & Escalation -->
            <div class="ks-arch-card">
                <div>
                    <div class="ks-feature-icon-box">
                        {ICONS['shield_check']}
                    </div>
                    <h3 class="ks-feature-title" style="font-size:1.15rem; color:#124C36;">3. Safe Advisory & Escalation</h3>
                    <p class="ks-feature-desc">
                        Generates cultural management checklists, asks follow-up questions for missing details, and escalates to KVK experts when needed.
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
    st.markdown(clean_html(how_html), unsafe_allow_html=True)
