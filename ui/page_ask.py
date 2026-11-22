"""Crop Diagnostic Center view module for KisanSaathi.
Features:
- Header with AI Symptom Intake pill
- 5 quick-fill benchmark scenario pills
- Clean two-column input form
- Prominent 'Analyze Crop Problem ->' button with progress status
- Verified agronomic advisory results with possible causes, field checklist, guardrails card, KVK escalation
- Multi-turn conversational follow-up questions
"""

import streamlit as st
from kisansaathi.pipeline import KisanSaathiPipeline
from kisansaathi.retrieval import load_reference_notes
from ui.assets import ICONS, DECORATIVE, clean_html

INDIAN_STATES = [
    "Select your state",
    "Uttar Pradesh",
    "West Bengal",
    "Punjab",
    "Maharashtra",
    "Madhya Pradesh",
    "Rajasthan",
    "Bihar",
    "Haryana",
    "Gujarat",
    "Karnataka",
    "Andhra Pradesh",
    "Tamil Nadu",
    "Telangana",
    "Odisha",
    "Kerala",
    "Assam",
    "Jharkhand",
    "Chhattisgarh",
    "Uttarakhand",
    "Himachal Pradesh",
    "Other",
]

GROWTH_STAGES = [
    "Select growth stage",
    "Seedling",
    "Vegetative",
    "Flowering",
    "Fruiting",
    "Harvest / Maturity",
    "Not sure",
]

SPREAD_OPTIONS = [
    "Not sure",
    "Not spreading",
    "Slowly",
    "Rapidly",
]

LANGUAGE_OPTIONS = [
    "Select language",
    "English",
    "Hindi",
    "Hinglish",
]

def set_preset_scenario(crop: str, region: str, stage: str, spread: str, lang: str, query: str):
    """Set form inputs to a benchmark scenario."""
    st.session_state.original_form["crop"] = crop
    st.session_state.original_form["region"] = region
    st.session_state.original_form["stage"] = stage
    st.session_state.original_form["spread"] = spread
    st.session_state.original_form["language"] = lang
    st.session_state.original_form["query"] = query
    st.session_state.result = None
    st.session_state.follow_up_history = []
    st.session_state.follow_up_answer = ""

def reset_all_inputs():
    """Reset all form inputs to clean default state."""
    st.session_state.original_form = {
        "crop": "",
        "region": "Select your state",
        "stage": "Select growth stage",
        "spread": "Not sure",
        "language": "Select language",
        "query": "",
    }
    st.session_state.result = None
    st.session_state.follow_up_history = []
    st.session_state.follow_up_answer = ""

def render_page_ask(resolved_api_key: str, resolved_model_name: str):
    """Render the Crop Diagnostic Center and assessment results."""
    OF = st.session_state.original_form

    # 1. Main Header
    st.markdown(f"""
    <div class="ks-card" style="margin-bottom:1.5rem; position:relative; overflow:hidden;">
        <div style="position:absolute; top:-10px; right:-10px; width:110px; height:80px; pointer-events:none; opacity:0.35;">
            {DECORATIVE['leaf_branch']}
        </div>
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem;">
            <div>
                <h2 style="font-family:var(--font-heading); font-size:1.85rem; font-weight:800; color:#124C36; margin:0 0 0.35rem 0; display:flex; align-items:center; gap:0.6rem;">
                    {ICONS['sprout']} Crop Diagnostic Center
                </h2>
                <p style="color:#64756C; font-size:0.95rem; margin:0; line-height:1.5;">
                    Describe your crop problem details below to receive grounded diagnostic assessment.
                </p>
            </div>
            <div>
                <span class="ks-pill-badge">&#10022; AI Symptom Intake</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 2. Quick-Fill Benchmark Scenarios (5 buttons in a row)
    st.markdown("""
    <div style="font-size:0.85rem; font-weight:700; color:#183B2D; margin-bottom:0.65rem; display:flex; align-items:center; gap:6px;">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#124C36" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>
        </svg>
        Quick-Fill Benchmark Scenarios:
    </div>
    """, unsafe_allow_html=True)

    qcols = st.columns(5, gap="small")
    with qcols[0]:
        if st.button("Tomato Leaf Curl", key="preset_tomato", use_container_width=True):
            set_preset_scenario("Tomato", "Uttar Pradesh", "Flowering", "Slowly", "English", "Tomato leaves are curling upwards with yellow borders and stunted growth.")
            st.rerun()
    with qcols[1]:
        if st.button("Rice Brown Spot", key="preset_rice", use_container_width=True):
            set_preset_scenario("Rice", "West Bengal", "Vegetative", "Slowly", "English", "Rice leaves showing scattered brown oval spots with greyish centers.")
            st.rerun()
    with qcols[2]:
        if st.button("Wheat Rust Yellowing", key="preset_wheat", use_container_width=True):
            set_preset_scenario("Wheat", "Punjab", "Tillering", "Not sure", "English", "Wheat leaves turning yellow from leaf tips with yellowish pustules.")
            st.rerun()
    with qcols[3]:
        if st.button("Potato Blight Stunting", key="preset_potato", use_container_width=True):
            set_preset_scenario("Potato", "Uttar Pradesh", "Vegetative", "Rapidly", "English", "Potato plants showing dark water-soaked lesions on leaf margins.")
            st.rerun()
    with qcols[4]:
        if st.button("↺ Reset Form", key="btn_reset_form", use_container_width=True):
            reset_all_inputs()
            st.rerun()

    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)

    # 3. Two-Column Diagnostic Intake Form
    with st.container():
        fcol1, fcol2 = st.columns(2, gap="large")

        with fcol1:
            crop_val = st.text_input(
                "Crop Name *",
                value=OF.get("crop", ""),
                placeholder="e.g. Tomato, Rice, Wheat, Cotton, Mustard",
                help="Specify the name of your affected crop."
            )

            current_reg = OF.get("region", "Select your state")
            reg_idx = INDIAN_STATES.index(current_reg) if current_reg in INDIAN_STATES else 0
            reg_val = st.selectbox(
                "State / Region *",
                options=INDIAN_STATES,
                index=reg_idx,
                help="Helps ground agronomic recommendations to your local agro-climatic zone."
            )

            current_stage = OF.get("stage", "Select growth stage")
            stage_idx = GROWTH_STAGES.index(current_stage) if current_stage in GROWTH_STAGES else 0
            stage_val = st.selectbox(
                "Crop Growth Stage",
                options=GROWTH_STAGES,
                index=stage_idx,
                help="Select the current biological growth stage of the crop."
            )

        with fcol2:
            current_spread = OF.get("spread", "Not sure")
            spread_idx = SPREAD_OPTIONS.index(current_spread) if current_spread in SPREAD_OPTIONS else 0
            spread_val = st.selectbox(
                "Problem Spread Rate",
                options=SPREAD_OPTIONS,
                index=spread_idx,
                help="Rapidly spreading conditions trigger immediate extension expert escalation."
            )

            current_lang = OF.get("language", "English")
            lang_idx = LANGUAGE_OPTIONS.index(current_lang) if current_lang in LANGUAGE_OPTIONS else 1
            lang_val = st.selectbox(
                "Preferred Advisory Language",
                options=LANGUAGE_OPTIONS,
                index=lang_idx,
                help="Receive advisory in English, Hindi (हिन्दी), or Hinglish."
            )

            query_val = st.text_area(
                "Describe the Symptoms Observed *",
                value=OF.get("query", ""),
                placeholder="e.g. leaves have yellow spots and curling edges, small white insects under leaves",
                height=85,
                help="Describe visual signs: spots, wilting, insect damage, color changes."
            )

        # Update session state with current form values
        OF["crop"] = crop_val
        OF["region"] = reg_val if reg_val != "Select your state" else ""
        OF["stage"] = stage_val if stage_val != "Select growth stage" else "Not sure"
        OF["spread"] = spread_val
        OF["language"] = lang_val if lang_val != "Select language" else "English"
        OF["query"] = query_val

        st.markdown("<div style='height: 0.85rem;'></div>", unsafe_allow_html=True)

        # 4. Full-Width Analyze Button
        analyze_clicked = st.button("Analyze Crop Problem →", key="btn_analyze_crop", type="primary", use_container_width=True)

    # 5. Pipeline Execution
    if analyze_clicked:
        if not query_val.strip() and not crop_val.strip():
            st.warning("Please enter crop symptoms or select a quick-fill benchmark scenario above.")
            st.stop()

        if not resolved_api_key:
            st.error("GEMINI_API_KEY is missing. Please add it to Streamlit Secrets, .env, or the sidebar.")
            st.stop()

        try:
            st.session_state.follow_up_history = []
            st.session_state.follow_up_answer = ""

            notes = load_reference_notes()
            pipeline = KisanSaathiPipeline(notes, api_key=resolved_api_key, model=resolved_model_name)

            with st.status("Running Grounded Agronomic Analysis...", expanded=True) as status:
                step_slot = st.empty()
                def on_pipeline_step(msg):
                    step_slot.write(f"Analyzing: {msg}")

                result = pipeline.run(
                    query=OF["query"] or f"Observed issues on {OF['crop']}",
                    crop=OF["crop"],
                    region=OF["region"],
                    stage=OF["stage"],
                    spread=OF["spread"],
                    language=OF["language"],
                    follow_up_answer="",
                    previous_extraction=None,
                    on_step=on_pipeline_step,
                )
                status.update(label="Agronomic Analysis Complete", state="complete", expanded=False)

            st.session_state.result = result
        except Exception as exc:
            st.error(f"Analysis could not be completed: {exc}")
            st.info("Please verify your API key validity and network connectivity.")

    # 6. Diagnostic Assessment Results Display
    if st.session_state.result:
        result = st.session_state.result
        extraction = result.get("extraction", {})
        diagnosis = result.get("diagnosis", {})
        advisory = result.get("advisory", {})
        follow_up_q = extraction.get("follow_up_question", "")

        st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)

        # Results header banner
        results_header = f"""
        <div class="ks-card" style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem; border-left:5px solid #238B52; margin-bottom:1.25rem;">
            <div>
                <h3 style="font-family:var(--font-heading); font-size:1.45rem; font-weight:800; color:#124C36; margin:0;">
                    Grounded Diagnostic Assessment
                </h3>
                <p style="color:#64756C; margin:0.25rem 0 0 0; font-size:0.95rem;">
                    Evaluated for <b>{extraction.get('crop', 'Crop')}</b> in <b>{extraction.get('broad_region', 'Region')}</b>
                </p>
            </div>
            <span style="background:#E8F3E9; color:#124C36; padding:0.45rem 1rem; border-radius:999px; font-weight:700; font-size:0.85rem; border:1px solid #C8DEC9; display:inline-flex; align-items:center; gap:6px;">
                {ICONS['check_green']} Verified Advisory
            </span>
        </div>
        """
        st.markdown(clean_html(results_header), unsafe_allow_html=True)

        # Context summary strip
        summary_strip = f"""
        <div class="ks-card" style="padding:1.15rem 1.6rem; background:#FFFFFF; margin-bottom:1.5rem;">
            <div style="display:flex; flex-wrap:wrap; gap:1.75rem; align-items:center;">
                <div><span style="font-size:0.75rem; color:#64756C; font-weight:700; text-transform:uppercase;">Crop:</span> <b style="color:#124C36;">{extraction.get('crop', 'Unknown')}</b></div>
                <div><span style="font-size:0.75rem; color:#64756C; font-weight:700; text-transform:uppercase;">Region:</span> <b style="color:#124C36;">{extraction.get('broad_region', 'Unknown')}</b></div>
                <div><span style="font-size:0.75rem; color:#64756C; font-weight:700; text-transform:uppercase;">Stage:</span> <b style="color:#124C36;">{extraction.get('growth_stage', 'Unknown')}</b></div>
                <div><span style="font-size:0.75rem; color:#64756C; font-weight:700; text-transform:uppercase;">Spread:</span> <b style="color:#124C36;">{extraction.get('spread', 'Unknown')}</b></div>
                <div><span style="font-size:0.75rem; color:#64756C; font-weight:700; text-transform:uppercase;">Symptoms:</span> <b style="color:#124C36;">{', '.join(extraction.get('symptoms', [])) or 'Observed'}</b></div>
            </div>
        </div>
        """
        st.markdown(clean_html(summary_strip), unsafe_allow_html=True)

        # Possible agronomic causes card
        causes = diagnosis.get("possible_causes", [])
        if causes:
            causes_html = "".join([f"""
            <div style="background:#F7F9F4; border-radius:12px; padding:1.15rem 1.35rem; margin-bottom:0.85rem; border:1px solid #DDE8DE;">
                <div style="font-size:1.05rem; font-weight:700; color:#124C36; margin-bottom:0.35rem;">{c.get('name', 'Possible cause')}</div>
                <div style="font-size:0.92rem; color:#64756C; line-height:1.55;">{c.get('reason', '')}</div>
            </div>
            """ for c in causes])
        else:
            causes_html = "<p style='color:#64756C; font-size:0.9rem;'>No definitive single match in reference notes. Continued observation recommended.</p>"

        causes_card = f"""
        <div class="ks-card" style="margin-bottom:1.5rem;">
            <h3 style="font-family:var(--font-heading); font-size:1.25rem; font-weight:800; color:#124C36; margin-bottom:0.75rem;">
                Possible Agronomic Causes
            </h3>
            <div style="background:#E8F3E9; border-left:4px solid #238B52; padding:0.75rem 1rem; border-radius:0 8px 8px 0; margin-bottom:1.25rem; font-size:0.85rem; color:#124C36;">
                <b>Grounded Literature Disclaimer:</b> Potential causes derived from symptom matching with ICAR reference materials. These represent preliminary assessments rather than confirmed laboratory diagnoses.
            </div>
            {causes_html}
        </div>
        """
        st.markdown(clean_html(causes_card), unsafe_allow_html=True)

        # Advisory & Field Checklist in 2 equal columns
        res_col1, res_col2 = st.columns(2, gap="medium")
        with res_col1:
            checklist_items = []
            if isinstance(advisory.get("next_steps"), list):
                for step in advisory.get("next_steps", []):
                    if step and str(step).strip():
                        checklist_items.append(f"<li style='margin-bottom:0.55rem;'>{step}</li>")

            advice_text = advisory.get("advice", "")
            checklist_body = ""
            if advice_text:
                checklist_body += f"<div style='margin-bottom:0.85rem; font-weight:600; color:#124C36; line-height:1.5;'>{advice_text}</div>"
            if checklist_items:
                checklist_body += f"<ul style='padding-left:1.25rem; margin:0 0 0.85rem 0;'>{''.join(checklist_items)}</ul>"
            if advisory.get("warning"):
                checklist_body += f"<div style='margin-top:0.75rem; padding:0.65rem 0.95rem; background:#FEF3C7; border:1px solid #FDE68A; border-radius:10px; font-size:0.85rem; color:#92400E;'><b>Caution:</b> {advisory['warning']}</div>"

            if not checklist_body:
                checklist_body = advisory.get("checklist_md") or advisory.get("response_text") or "Non-chemical cultural practices verified safe for immediate field application."

            checklist_card = f"""
            <div class="ks-card" style="height:100%;">
                <h3 style="font-family:var(--font-heading); font-size:1.2rem; font-weight:800; color:#124C36; margin-bottom:0.75rem;">
                    Immediate Practical Checklist
                </h3>
                <p style="font-size:0.85rem; color:#64756C; margin-bottom:1rem;">
                    Non-chemical cultural and biological practices verified safe for immediate field application:
                </p>
                <div style="font-size:0.92rem; color:#183B2D; line-height:1.65;">
                    {checklist_body}
                </div>
            </div>
            """
            st.markdown(clean_html(checklist_card), unsafe_allow_html=True)

        with res_col2:
            guardrails_card = f"""
            <div class="ks-card" style="height:100%; border:1.5px solid #FCD34D; background:#FFFDF7;">
                <div style="display:flex; align-items:center; gap:0.6rem; margin-bottom:0.85rem;">
                    <div style="background:#FEF3C7; padding:8px; border-radius:10px;">
                        {ICONS['alert_amber']}
                    </div>
                    <h3 style="font-family:var(--font-heading); font-size:1.2rem; font-weight:800; color:#92400E; margin:0;">
                        Safety Guardrails Enforced
                    </h3>
                </div>
                <div style="font-size:0.9rem; color:#78350F; line-height:1.6; margin-bottom:1rem;">
                    <b>Strict Prohibition Notice:</b> KisanSaathi will never prescribe synthetic chemical spraying dosages (ml/L or kg/ha). Synthetic pesticides pose severe risks of phytotoxicity, pollinator harm, and chemical exposure without physical agronomist inspection.
                </div>
                <div style="background:#FFFFFF; border:1px solid #FDE68A; border-radius:12px; padding:1rem; font-size:0.85rem; color:#92400E;">
                    <b>Escalation Policy:</b> Rapidly spreading conditions or uncertain diagnostics must be evaluated by your local Krishi Vigyan Kendra (KVK) or Block Agriculture Officer.
                </div>
            </div>
            """
            st.markdown(clean_html(guardrails_card), unsafe_allow_html=True)

        # KVK Escalation Banner
        should_escalate = (
            advisory.get("escalate", False) or
            advisory.get("escalate_to_expert", False) or
            extraction.get("spread") == "Rapidly" or
            diagnosis.get("uncertainty") == "high"
        )
        if should_escalate:
            escalation_reason = advisory.get("escalation_reason") or "This problem is flagged as rapidly expanding or requires laboratory confirmation."
            escalation_html = f"""
            <div style="background:#FEF2F2; border:1.5px solid #FCA5A5; border-radius:16px; padding:1.25rem 1.5rem; margin-top:1.5rem; display:flex; align-items:center; gap:1.25rem;">
                <div style="background:#FEE2E2; width:48px; height:48px; border-radius:12px; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                    {ICONS['phone']}
                </div>
                <div>
                    <div style="font-weight:800; font-size:1.05rem; color:#991B1B; margin-bottom:0.25rem;">
                        Recommended Field Action: Consult Local Agricultural Extension (KVK)
                    </div>
                    <div style="font-size:0.88rem; color:#7F1D1D; line-height:1.5;">
                        {escalation_reason} Contact your nearest Krishi Vigyan Kendra (KVK) or Call the Kisan Call Centre at <b>1800-180-1551</b> (toll-free).
                    </div>
                </div>
            </div>
            """
            st.markdown(clean_html(escalation_html), unsafe_allow_html=True)

        # Multi-turn Follow-up Section
        st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)
        fu_header = """
        <div class="ks-card">
            <h3 style="font-family:var(--font-heading); font-size:1.25rem; font-weight:800; color:#124C36; margin-bottom:0.5rem;">
                Follow-Up Clarifications & Questions
            </h3>
            <p style="font-size:0.92rem; color:#64756C; margin-bottom:1.25rem;">
                Ask about specific symptoms, organic alternatives, or clarifying details about this diagnosis.
            </p>
        """
        st.markdown(clean_html(fu_header), unsafe_allow_html=True)

        if follow_up_q:
            st.info(f"💡 **Suggested Clarification:** {follow_up_q}")

        # Display conversational follow-up history
        for item in st.session_state.follow_up_history:
            fu_item = f"""
            <div style="background:#E8F3E9; border:1px solid #C8DEC9; border-radius:12px; padding:0.85rem 1.15rem; margin-bottom:0.75rem;">
                <div style="font-weight:700; color:#124C36; font-size:0.85rem; margin-bottom:0.25rem; display:flex; align-items:center; gap:6px;">
                    {ICONS['user']} Farmer Query:
                </div>
                <div style="color:#183B2D; font-size:0.92rem;">{item['q']}</div>
            </div>
            <div style="background:#FFFFFF; border:1px solid #DDE8DE; border-radius:12px; padding:1rem 1.25rem; margin-bottom:1rem;">
                <div style="font-weight:700; color:#124C36; font-size:0.85rem; margin-bottom:0.25rem; display:flex; align-items:center; gap:6px;">
                    {ICONS['bot']} KisanSaathi Agronomist:
                </div>
                <div style="color:#183B2D; font-size:0.92rem; line-height:1.6;">{item['a']}</div>
            </div>
            """
            st.markdown(clean_html(fu_item), unsafe_allow_html=True)

        fu_input = st.text_input(
            "Ask follow-up question:",
            key="fu_question_input",
            placeholder="e.g. Can I use neem oil spray? How often should I prune affected leaves?"
        )

        if st.button("Send Follow-Up Question", key="btn_send_followup"):
            if fu_input.strip():
                try:
                    notes = load_reference_notes()
                    pipeline = KisanSaathiPipeline(notes, api_key=resolved_api_key, model=resolved_model_name)
                    with st.spinner("Refining advisory with agronomist guidelines..."):
                        fu_res = pipeline.run(
                            query=fu_input.strip(),
                            crop=extraction.get("crop", OF["crop"]),
                            region=extraction.get("broad_region", OF["region"]),
                            stage=extraction.get("growth_stage", OF["stage"]),
                            spread=extraction.get("spread", OF["spread"]),
                            language=OF["language"],
                            follow_up_answer=fu_input.strip(),
                            previous_extraction=extraction,
                        )
                        answer_text = (
                            fu_res["advisory"].get("advice", "") + "\n" +
                            "\n".join([f"• {s}" for s in fu_res["advisory"].get("next_steps", [])])
                        )
                        if not answer_text.strip():
                            answer_text = fu_res["advisory"].get("checklist_md") or fu_res["advisory"].get("response_text") or "Follow verified non-chemical cultural sanitation."
                        st.session_state.follow_up_history.append({"q": fu_input.strip(), "a": answer_text})
                        st.rerun()
                except Exception as exc:
                    st.error(f"Error handling follow-up: {exc}")

        st.markdown('</div>', unsafe_allow_html=True)
