"""Evaluation benchmark verification view module for KisanSaathi.
Integrates the complete KisanSaathi Visual Asset Pack:
- Evaluation telemetry icons from assets/icons/ (clipboard-check, award, flask-ban, language)
- Official status badges from assets/ (pass.svg, fail.svg)
- Decorative elements from assets/decorative/ (leaf-branch, crop-rows)
"""

import os
import csv
import streamlit as st
from ui.assets import ICONS, LOGOS, DECORATIVE, BADGES, get_image_base64, clean_html

def get_evaluation_metrics(csv_path: str = "evaluation_results.csv") -> dict:
    """Dynamically parse evaluation_results.csv and compute benchmark telemetry."""
    if not os.path.exists(csv_path):
        return {
            "total": 0,
            "passed": 0,
            "pass_rate": 0,
            "dosages_prescribed": 0,
            "languages": 3,
            "rows": []
        }
    rows = []
    with open(csv_path, encoding="utf-8") as f:
        reader = list(csv.DictReader(f))
        for r in reader:
            rows.append(r)
    total = len(rows)
    passed = sum(1 for r in rows if r.get("Pass/Fail", "").strip().upper() == "PASS")
    pass_rate = round((passed / total * 100)) if total > 0 else 0

    # Verify zero synthetic dosage hallucination across all evaluation outputs
    dosages = 0
    for r in rows:
        text = (r.get("Actual Output", "") + " " + r.get("Reason", "")).lower()
        if any(unit in text for unit in ["ml/l", "ml/acre", "kg/ha", "g/l", "gm/l"]):
            dosages += 1

    return {
        "total": total,
        "passed": passed,
        "pass_rate": pass_rate,
        "dosages_prescribed": dosages,
        "languages": 3,
        "rows": rows
    }

def render_tab_eval():
    """Render the empirical benchmark verification dashboard."""
    metrics = get_evaluation_metrics()
    total = metrics["total"]
    passed = metrics["passed"]
    pass_rate = metrics["pass_rate"]
    dosages = metrics["dosages_prescribed"]
    langs = metrics["languages"]
    rows = metrics["rows"]

    # 1. Header & Dynamic 4-Metric Grid
    eval_header_html = f"""
    <div class="ks-eval-page" style="position:relative; padding-bottom:1.5rem;">
        <!-- Left Leafy Branch SVG from Asset Pack -->
        <div style="position:absolute; top:0; left:0; width:130px; height:90px; pointer-events:none; z-index:1; opacity:0.4;">
            {DECORATIVE['leaf_branch']}
        </div>

        <!-- Right Terraced Farm Field Rows SVG from Asset Pack -->
        <div style="position:absolute; top:10px; right:0px; width:220px; height:90px; pointer-events:none; z-index:1; opacity:0.45;">
            {DECORATIVE['crop_rows']}
        </div>

        <!-- Section Header -->
        <div style="text-align:center; max-width:760px; margin:0 auto 1.4rem auto; position:relative; z-index:2;">
            <div style="display:inline-block; margin-bottom:0.6rem;">
                <span class="ks-pill-badge">EMPIRICAL BENCHMARKS</span>
            </div>
            <h1 style="font-size:2.35rem; font-weight:800; color:#174B35; margin:0 0 0.5rem 0; letter-spacing:-0.03em; line-height:1.15;">
                Empirical Benchmark Verification
            </h1>
            <p style="color:#5A6860; font-size:1rem; line-height:1.5; margin:0;">
                Evaluated dynamically across verified synthetic field test cases against ICAR standards.
            </p>
        </div>

        <!-- 4 Dynamically Aligned Metric Cards -->
        <div class="ks-eval-metrics-grid" style="display:grid; grid-template-columns:repeat(4, 1fr); gap:1.25rem; margin-bottom:2.5rem; position:relative; z-index:2;">
            <!-- Metric 1: Total Scenarios -->
            <div style="display:flex; align-items:center; background:#FFFFFF; border:1.5px solid #DFE8DF; border-radius:18px; padding:1.25rem 1.4rem; gap:1.2rem; box-shadow:0 2px 10px rgba(23,75,53,0.03);">
                <div style="width:48px; height:48px; border-radius:12px; background:#E7F2E8; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                    {ICONS['clipboard_check']}
                </div>
                <div style="width:1px; height:42px; background:#DFE8DF;"></div>
                <div>
                    <div style="font-size:1.95rem; font-weight:800; color:#174B35; line-height:1.1;">{passed} / {total}</div>
                    <div style="font-size:0.82rem; font-weight:600; color:#5A6860; margin-top:3px;">Scenarios Evaluated</div>
                </div>
            </div>

            <!-- Metric 2: Pass Rate -->
            <div style="display:flex; align-items:center; background:#F0FDF4; border:1.5px solid #BBF7D0; border-radius:18px; padding:1.25rem 1.4rem; gap:1.2rem; box-shadow:0 2px 10px rgba(23,75,53,0.03);">
                <div style="width:48px; height:48px; border-radius:12px; background:#DEF7EC; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                    {ICONS['award']}
                </div>
                <div style="width:1px; height:42px; background:#C6EAD3;"></div>
                <div>
                    <div style="font-size:1.95rem; font-weight:800; color:#15803D; line-height:1.1;">{pass_rate}%</div>
                    <div style="font-size:0.82rem; font-weight:600; color:#166534; margin-top:3px;">Pass Rate</div>
                </div>
            </div>

            <!-- Metric 3: Dosages Prescribed -->
            <div style="display:flex; align-items:center; background:#FFFDF7; border:1.5px solid #FDE68A; border-radius:18px; padding:1.25rem 1.4rem; gap:1.2rem; box-shadow:0 2px 10px rgba(23,75,53,0.03);">
                <div style="width:48px; height:48px; border-radius:12px; background:#FEF3C7; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                    {ICONS['flask_ban']}
                </div>
                <div style="width:1px; height:42px; background:#FCE59F;"></div>
                <div>
                    <div style="font-size:1.95rem; font-weight:800; color:#B45309; line-height:1.1;">{dosages}</div>
                    <div style="font-size:0.82rem; font-weight:600; color:#92400E; margin-top:3px;">Dosages Prescribed</div>
                </div>
            </div>

            <!-- Metric 4: Languages Supported -->
            <div style="display:flex; align-items:center; background:#FFFFFF; border:1.5px solid #DFE8DF; border-radius:18px; padding:1.25rem 1.4rem; gap:1.2rem; box-shadow:0 2px 10px rgba(23,75,53,0.03);">
                <div style="width:48px; height:48px; border-radius:12px; background:#E7F2E8; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                    {ICONS['language']}
                </div>
                <div style="width:1px; height:42px; background:#DFE8DF;"></div>
                <div>
                    <div style="font-size:1.95rem; font-weight:800; color:#174B35; line-height:1.1;">{langs}</div>
                    <div style="font-size:0.82rem; font-weight:600; color:#5A6860; margin-top:3px;">Languages Supported</div>
                </div>
            </div>
        </div>
    </div>
    """
    st.markdown(clean_html(eval_header_html), unsafe_allow_html=True)

    # 2. Benchmark Test Cases Expander with Dynamic Rows & Clear PASS/FAIL States
    if rows:
        with st.expander(f"View All {len(rows)} Benchmark Test Cases (evaluation_results.csv)", expanded=True):
            rows_html = []
            for idx, r in enumerate(rows):
                tid = r.get("Test ID", f"TC-{idx+1:02d}")
                inp = r.get("Input", "")
                reas = r.get("Reason", "")
                status = r.get("Pass/Fail", "PASS").strip().upper()

                # Parse metadata fields
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

                # Badge markup using SVG status badges from Asset Pack
                if status == "PASS":
                    badge_markup = f'<span class="ks-badge-pass" style="display:inline-flex; align-items:center; gap:5px; background:#E8F5E9; color:#174B35; padding:5px 14px; border-radius:999px; font-weight:700; font-size:0.85rem; border:1px solid #C8E6C9;"><span style="width:16px; height:16px; display:inline-flex; align-items:center;">{BADGES["pass"]}</span> PASS</span>'
                else:
                    badge_markup = f'<span class="ks-badge-fail" style="display:inline-flex; align-items:center; gap:5px; background:#FFEBEE; color:#C62828; padding:5px 14px; border-radius:999px; font-weight:700; font-size:0.85rem; border:1px solid #FFCDD2;"><span style="width:16px; height:16px; display:inline-flex; align-items:center;">{BADGES["fail"]}</span> FAIL</span>'

                divider = "" if idx == len(rows) - 1 else "<hr style='border:none; border-top:1px solid #DFE8DF; margin:1rem 0;'>"

                rows_html.append(f"""
                <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:1.25rem; padding:0.5rem 0;">
                    <div style="background:#E8F5E9; color:#174B35; font-weight:800; font-size:0.95rem; border-radius:8px; padding:6px 14px; flex-shrink:0;">
                        {tid}
                    </div>
                    <div style="flex:1;">
                        <div style="display:flex; flex-wrap:wrap; align-items:center; gap:0.65rem; font-size:0.9rem; color:#25352D; line-height:1.4;">
                            <span style="display:inline-flex; align-items:center; gap:4px;">{ICONS['leaf_primary']} <b>Crop:</b> {crop_v}</span>
                            <span style="color:#C0D2C4;">|</span>
                            <span style="display:inline-flex; align-items:center; gap:4px;">{ICONS['map_pin']} <b>Region:</b> {region_v}</span>
                            <span style="color:#C0D2C4;">|</span>
                            <span style="display:inline-flex; align-items:center; gap:4px;">{ICONS['sprout']} <b>Stage:</b> {stage_v}</span>
                            <span style="color:#C0D2C4;">|</span>
                            <span style="display:inline-flex; align-items:center; gap:4px;">{ICONS['alert_triangle']} <b>Spread:</b> {spread_v}</span>
                            <span style="color:#C0D2C4;">|</span>
                            <span style="display:inline-flex; align-items:center; gap:4px;">{ICONS['language']} <b>Lang:</b> {lang_v}</span>
                        </div>
                        <div style="color:#4B6354; font-size:0.85rem; margin-top:0.45rem; line-height:1.5;">
                            <b>Assessment Verification:</b> {reas}
                        </div>
                    </div>
                    <div style="flex-shrink:0;">
                        {badge_markup}
                    </div>
                </div>
                {divider}
                """)

            cases_card_html = f"""
            <div style="background:#FFFFFF; border:1.5px solid #DFE8DF; border-radius:18px; padding:1.5rem 1.8rem; box-shadow:0 2px 12px rgba(23,75,53,0.03);">
                {''.join(rows_html)}
            </div>
            """
            st.markdown(clean_html(cases_card_html), unsafe_allow_html=True)
    else:
        st.info("No benchmark results found. Run evaluation.py to generate evaluation_results.csv.")

    # Countryside Horizon Transition
    landscape_horizon_b64 = get_image_base64("countryside-horizon.png")
    horizon_html = f"""
    <div class="ks-landscape-horizon" style="margin-top:1.5rem; margin-bottom:0;">
        <img src="{landscape_horizon_b64}" alt="Scenic Indian agricultural countryside horizon" />
    </div>
    """
    st.markdown(clean_html(horizon_html), unsafe_allow_html=True)
