"""Crop Diagnostic Center view module for KisanSaathi.
Features clean input alignment, professional vector icons, robust multi-turn follow-ups,
and strict adherence to ICAR agronomic grounding without synthetic dosages.
"""

import streamlit as st
from kisansaathi.pipeline import KisanSaathiPipeline
from kisansaathi.retrieval import load_reference_notes
from ui.assets import ICONS, CORNER_LEAF_BRANCH_SVG, clean_html

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
    """Set the form fields to a benchmark scenario."""
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

def render_tab_ask(resolved_api_key: str, resolved_model_name: str):
    """Render the Crop Diagnostic Center, form inputs, and grounded results."""
    OF = st.session_state.original_form

    # 1. Main White Card Container
    header_html = f"""
    <div class="ks-ask-card">
        <div class="ks-ask-corner-foliage">
            {CORNER_LEAF_BRANCH_SVG}
        </div>
        <div class="ks-ask-header">
            <div>
                <h2 class="ks-ask-title">
                    <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#174B35" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/>
                        <path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>
                    </svg>
                    Crop Diagnostic Center
                </h2>
                <p class="ks-ask-subtitle">
                    Describe the crop problem details below to get clear and safe guidance.
                </p>
            </div>
            <div>
                <span class="ks-ask-badge">&#10022; AI Symptom Intake</span>
            </div>
        </div>
    """
    st.markdown(clean_html(header_html), unsafe_allow_html=True)

    # 2. Quick-Fill Benchmark Scenarios Section (Clean text, no random emojis)
    preset_title_html = """
    <div class="ks-preset-section-title">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#174B35" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <polygon points="12 2 2 7 12 12 22 7 12 2"/>
            <polyline points="2 17 12 22 22 17"/>
            <polyline points="2 12 12 17 22 12"/>
        </svg>
        Quick-Fill Benchmark Scenarios:
    </div>
    """
    st.markdown(clean_html(preset_title_html), unsafe_allow_html=True)

    p1, p2, p3, p4, p5 = st.columns([1.1, 1.1, 1.1, 1.1, 0.9], gap="small")
    with p1:
        if st.button("Tomato Leaf Curl (UP)", key="qf_tomato", use_container_width=True):
            set_preset_scenario(
                "Tomato",
                "Uttar Pradesh",
                "Flowering",
                "Slowly",
                "English",
                "Tomato leaves have yellow spots and curling edges with stunted apex."
            )
            st.rerun()

    with p2:
        if st.button("Rice Brown Spot (WB)", key="qf_rice", use_container_width=True):
            set_preset_scenario(
                "Rice",
                "West Bengal",
                "Vegetative",
                "Slowly",
                "English",
                "Small circular to oval dark brown spots on leaves with yellow halo."
            )
            st.rerun()

    with p3:
        if st.button("Wheat Yellowing (PB)", key="qf_wheat", use_container_width=True):
            set_preset_scenario(
                "Wheat",
                "Punjab",
                "Vegetative",
                "Slowly",
                "English",
                "Yellow stripes parallel to leaf veins, yellow powder rubs off on fingers."
            )
            st.rerun()

    with p4:
        if st.button("Potato Stunting (UP)", key="qf_potato", use_container_width=True):
            set_preset_scenario(
                "Potato",
                "Uttar Pradesh",
                "Vegetative",
                "Rapidly",
                "Hindi",
                "आलू के पौधे बौने रह गए हैं, पत्तियां ऊपर की ओर मुड़ रही हैं और शिराएं पीली पड़ रही हैं।"
            )
            st.rerun()

    with p5:
        if st.button("Reset Inputs", key="qf_reset", use_container_width=True):
            reset_all_inputs()
            st.rerun()

    st.markdown("<div style='height: 1.25rem;'></div>", unsafe_allow_html=True)

    # 3. Form Inputs in 2 Balanced Columns
    col_left, col_right = st.columns(2, gap="large")

    with col_left:
        crop_val = st.text_input(
            "Crop Name",
            value=OF.get("crop", ""),
            placeholder="e.g. Tomato / Rice / गेहूं",
            help="Enter common English or local name of the crop."
        )

        reg_val_current = OF.get("region", "Select your state")
        reg_idx = INDIAN_STATES.index(reg_val_current) if reg_val_current in INDIAN_STATES else 0
        reg_val = st.selectbox(
            "Region / State",
            INDIAN_STATES,
            index=reg_idx,
            help="Select the geographic state for localized agronomic calibration."
        )

        stage_val_current = OF.get("stage", "Select growth stage")
        stg_idx = GROWTH_STAGES.index(stage_val_current) if stage_val_current in GROWTH_STAGES else 0
        stage_val = st.selectbox(
            "Crop Growth Stage",
            GROWTH_STAGES,
            index=stg_idx,
            help="Current phenological development phase of the crop."
        )

    with col_right:
        spread_val_current = OF.get("spread", "Not sure")
        spd_idx = SPREAD_OPTIONS.index(spread_val_current) if spread_val_current in SPREAD_OPTIONS else 0
        spread_val = st.selectbox(
            "Problem Spreading?",
            SPREAD_OPTIONS,
            index=spd_idx,
            help="Rate at which observed symptoms are expanding across adjacent plots."
        )

        lang_val_current = OF.get("language", "Select language")
        lng_idx = LANGUAGE_OPTIONS.index(lang_val_current) if lang_val_current in LANGUAGE_OPTIONS else 1
        lang_val = st.selectbox(
            "Preferred Advisory Language",
            LANGUAGE_OPTIONS,
            index=lng_idx,
            help="Select preferred language for diagnostic summary and cultural management checklists."
        )

        query_val = st.text_area(
            "Describe the Symptoms Observed",
            value=OF.get("query", ""),
            placeholder="e.g. leaves have yellow spots and curling edges",
            height=85,
            help="Detail visible symptoms: leaf discoloration, necrotic lesions, wilting, insect presence, etc."
        )

    # Update session state with current form values
    OF["crop"] = crop_val
    OF["region"] = reg_val if reg_val != "Select your state" else ""
    OF["stage"] = stage_val if stage_val != "Select growth stage" else "Not sure"
    OF["spread"] = spread_val
    OF["language"] = lang_val if lang_val != "Select language" else "English"
    OF["query"] = query_val

    # 4. Full-Width Analyze Button
    st.markdown('<div class="ks-analyze-btn">', unsafe_allow_html=True)
    analyze_clicked = st.button("Analyze Crop Problem →", key="btn_analyze_crop", type="primary", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Close the outer white card
    st.markdown('</div>', unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # 5. Pipeline Execution
    # -------------------------------------------------------------------------
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

    # -------------------------------------------------------------------------
    # 6. Diagnostic Assessment Results Display
    # -------------------------------------------------------------------------
    if st.session_state.result:
        result = st.session_state.result
        extraction = result.get("extraction", {})
        diagnosis = result.get("diagnosis", {})
        advisory = result.get("advisory", {})
        follow_up_q = extraction.get("follow_up_question", "").strip()

        st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)
        results_header = f"""
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:1.25rem;">
            <div>
                <h2 style="font-size:1.85rem; font-weight:800; color:#174B35; margin:0;">
                    KisanSaathi Assessment Results
                </h2>
                <p style="color:#5A6860; margin:0.25rem 0 0 0; font-size:0.95rem;">
                    Grounded diagnostic evaluation for <b>{extraction.get('crop', 'Crop')}</b> in <b>{extraction.get('broad_region', 'Region')}</b>
                </p>
            </div>
            <span style="background:#E7F2E8; color:#0B5A2A; padding:0.45rem 1rem; border-radius:999px; font-weight:700; font-size:0.85rem; border:1px solid #CDE5D2; display:inline-flex; align-items:center; gap:6px;">
                {ICONS['check_green']} Verified Advisory
            </span>
        </div>
        """
        st.markdown(clean_html(results_header), unsafe_allow_html=True)

        # Context summary strip
        summary_strip = f"""
        <div class="ks-card" style="padding:1.15rem 1.6rem; background:#FFFFFF; margin-bottom:1.5rem;">
            <div style="display:flex; flex-wrap:wrap; gap:1.75rem; align-items:center;">
                <div><span style="font-size:0.75rem; color:#5A6860; font-weight:700; text-transform:uppercase;">Crop:</span> <b style="color:#174B35;">{extraction.get('crop', 'Unknown')}</b></div>
                <div><span style="font-size:0.75rem; color:#5A6860; font-weight:700; text-transform:uppercase;">Region:</span> <b style="color:#174B35;">{extraction.get('broad_region', 'Unknown')}</b></div>
                <div><span style="font-size:0.75rem; color:#5A6860; font-weight:700; text-transform:uppercase;">Stage:</span> <b style="color:#174B35;">{extraction.get('growth_stage', 'Unknown')}</b></div>
                <div><span style="font-size:0.75rem; color:#5A6860; font-weight:700; text-transform:uppercase;">Spread:</span> <b style="color:#174B35;">{extraction.get('spread', 'Unknown')}</b></div>
                <div><span style="font-size:0.75rem; color:#5A6860; font-weight:700; text-transform:uppercase;">Symptoms:</span> <b style="color:#174B35;">{', '.join(extraction.get('symptoms', [])) or 'Observed'}</b></div>
            </div>
        </div>
        """
        st.markdown(clean_html(summary_strip), unsafe_allow_html=True)

        # Possible agronomic causes card
        causes = diagnosis.get("possible_causes", [])
        if causes:
            causes_html = "".join([f"""
            <div style="background:#F7F8F2; border-radius:12px; padding:1.15rem 1.35rem; margin-bottom:0.85rem; border:1px solid #E2E9E1;">
                <div style="font-size:1.05rem; font-weight:700; color:#174B35; margin-bottom:0.35rem;">{c.get('name', 'Possible cause')}</div>
                <div style="font-size:0.92rem; color:#5A6860; line-height:1.55;">{c.get('reason', '')}</div>
            </div>
            """ for c in causes])
        else:
            causes_html = "<p style='color:#5A6860; font-size:0.9rem;'>No definitive single match in reference notes. Continued observation recommended.</p>"

        causes_card = f"""
        <div class="ks-card" style="margin-bottom:1.5rem;">
            <h3 style="font-size:1.25rem; font-weight:800; color:#174B35; margin-bottom:0.75rem;">
                Possible Agronomic Causes
            </h3>
            <div style="background:#F0FDF4; border-left:4px solid #2E7D50; padding:0.75rem 1rem; border-radius:0 8px 8px 0; margin-bottom:1.25rem; font-size:0.85rem; color:#166534;">
                <b>Grounded Literature Disclaimer:</b> Potential causes derived from symptom matching with ICAR reference materials. These represent preliminary assessments rather than confirmed laboratory diagnoses.
            </div>
            {causes_html}
        </div>
        """
        st.markdown(clean_html(causes_card), unsafe_allow_html=True)

        # Advisory & Field Checklist in 2 equal columns
        res_col1, res_col2 = st.columns(2, gap="medium")
        with res_col1:
            checklist_card = f"""
            <div class="ks-card" style="height:100%;">
                <h3 style="font-size:1.2rem; font-weight:800; color:#174B35; margin-bottom:0.75rem;">
                    Immediate Practical Checklist
                </h3>
                <p style="font-size:0.85rem; color:#5A6860; margin-bottom:1rem;">
                    Non-chemical cultural and biological practices verified safe for immediate field application:
                </p>
                <div style="font-size:0.92rem; color:#25352D; line-height:1.65;">
                    {advisory.get('checklist_md', advisory.get('response_text', 'No checklist available.'))}
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
                    <h3 style="font-size:1.2rem; font-weight:800; color:#92400E; margin:0;">
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
        if advisory.get("escalate_to_expert", False) or extraction.get("spread") == "Rapidly":
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
                        This problem is flagged as rapidly expanding or requires laboratory confirmation. Contact your nearest Krishi Vigyan Kendra (KVK) or Call the Kisan Call Centre at <b>1800-180-1551</b> (toll-free).
                    </div>
                </div>
            </div>
            """
            st.markdown(clean_html(escalation_html), unsafe_allow_html=True)

        # Multi-turn Follow-up Section
        st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)
        fu_header = """
        <div class="ks-card">
            <h3 style="font-size:1.25rem; font-weight:800; color:#174B35; margin-bottom:0.5rem;">
                Follow-Up Clarifications & Questions
            </h3>
            <p style="font-size:0.92rem; color:#5A6860; margin-bottom:1.25rem;">
                Ask about specific symptoms, organic alternatives, or clarifying details about this diagnosis.
            </p>
        """
        st.markdown(clean_html(fu_header), unsafe_allow_html=True)

        if follow_up_q:
            st.info(f"Suggested Clarification: {follow_up_q}")

        # Display conversational follow-up history
        for item in st.session_state.follow_up_history:
            fu_item = f"""
            <div style="background:#F0FDF4; border:1px solid #BBF7D0; border-radius:12px; padding:0.85rem 1.15rem; margin-bottom:0.75rem;">
                <div style="font-weight:700; color:#166534; font-size:0.85rem; margin-bottom:0.25rem; display:flex; align-items:center; gap:6px;">
                    {ICONS['user']} Farmer Query:
                </div>
                <div style="color:#25352D; font-size:0.92rem;">{item['q']}</div>
            </div>
            <div style="background:#FFFFFF; border:1px solid #E2E9E1; border-radius:12px; padding:1rem 1.25rem; margin-bottom:1rem;">
                <div style="font-weight:700; color:#174B35; font-size:0.85rem; margin-bottom:0.25rem; display:flex; align-items:center; gap:6px;">
                    {ICONS['bot']} KisanSaathi Agronomist:
                </div>
                <div style="color:#25352D; font-size:0.92rem; line-height:1.6;">{item['a']}</div>
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
                    with st.spinner("Analyzing follow-up question..."):
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
                        answer_text = fu_res["advisory"].get(
                            "checklist_md",
                            fu_res["advisory"].get("response_text", "Could not generate response.")
                        )
                        st.session_state.follow_up_history.append({"q": fu_input.strip(), "a": answer_text})
                        st.rerun()
                except Exception as exc:
                    st.error(f"Error handling follow-up: {exc}")

        st.markdown('</div>', unsafe_allow_html=True)
