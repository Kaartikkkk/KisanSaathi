import os
import streamlit as st
from dotenv import load_dotenv
from kisansaathi.pipeline import KisanSaathiPipeline
from kisansaathi.retrieval import load_reference_notes

load_dotenv(override=True)
st.set_page_config(page_title="KisanSaathi", page_icon="🌱", layout="wide")

def get_gemini_api_key(sidebar_input=""):
    """
    Resolves the Gemini API key using strict priority:
    1. User-entered sidebar API key, if provided.
    2. Streamlit Community Cloud Secrets (st.secrets.get("GEMINI_API_KEY", "")).
    3. Local environment variable (os.getenv("GEMINI_API_KEY", "") from .env).
    """
    if sidebar_input and sidebar_input.strip():
        return sidebar_input.strip()
    try:
        cloud_key = st.secrets.get("GEMINI_API_KEY", "")
        if cloud_key and str(cloud_key).strip():
            return str(cloud_key).strip()
    except Exception:
        pass
    env_key = os.getenv("GEMINI_API_KEY", "")
    if env_key and env_key.strip():
        return env_key.strip()
    return ""

def get_gemini_model():
    """
    Resolves the Gemini model name using priority:
    1. Streamlit Community Cloud Secrets (st.secrets.get("GEMINI_MODEL", "")).
    2. Local environment variable (os.getenv("GEMINI_MODEL", "")).
    3. Default fallback: st.secrets.get("GEMINI_MODEL", "gemini-2.5-flash") or "gemini-3.5-flash-lite".
    """
    try:
        cloud_model = st.secrets.get("GEMINI_MODEL", "")
        if cloud_model and str(cloud_model).strip():
            return str(cloud_model).strip()
    except Exception:
        pass
    env_model = os.getenv("GEMINI_MODEL", "")
    if env_model and env_model.strip():
        return env_model.strip()
    try:
        return st.secrets.get("GEMINI_MODEL", "gemini-2.5-flash")
    except Exception:
        return "gemini-3.5-flash-lite"

st.title("🌱 KisanSaathi")
st.caption("A multilingual, safety-first crop advisory assistant")
st.info("This prototype provides general information, not a confirmed diagnosis. For serious or spreading crop damage, contact a local agriculture officer or KVK.")

# Initialize persistent session state
if "result" not in st.session_state:
    st.session_state.result = None
if "follow_up_history" not in st.session_state:
    st.session_state.follow_up_history = []
if "follow_up_answer" not in st.session_state:
    st.session_state.follow_up_answer = ""
if "original_form" not in st.session_state:
    st.session_state.original_form = {
        "crop": "",
        "region": "",
        "stage": "Not sure",
        "query": "",
        "spread": "Not sure",
        "language": "Hindi"
    }

with st.sidebar:
    st.header("About")
    st.write("KisanSaathi uses a three-stage prompt workflow: extraction, grounded diagnosis and safe advisory generation.")
    api_key_input = st.text_input(
        "Gemini API Key",
        value="",
        type="password",
        help="Enter your Gemini API key (or configure GEMINI_API_KEY in Streamlit Cloud Secrets / .env)"
    )
    language = st.selectbox(
        "Preferred response language",
        ["Hindi", "English", "Hinglish"],
        key="language_select"
    )
    st.caption("Do not enter names, phone numbers, exact addresses or other personal information.")

st.subheader("Describe your crop problem")
crop = st.text_input(
    "Crop (if known)",
    placeholder="e.g. Tomato / गेहूं",
    key="crop_input"
)
region = st.text_input(
    "Region or state (broad location only)",
    placeholder="e.g. Uttar Pradesh",
    key="region_input"
)
stage = st.selectbox(
    "Crop growth stage",
    ["Not sure", "Seedling", "Vegetative", "Flowering", "Fruiting", "Harvest"],
    key="stage_input"
)
query = st.text_area(
    "Describe the symptoms",
    placeholder="Example: Mere tamatar ke patton par peele dhabbe hain aur kinare mud rahe hain.",
    height=130,
    key="query_input"
)
spread = st.selectbox(
    "How quickly is the problem spreading?",
    ["Not sure", "Not spreading", "Slowly", "Rapidly"],
    key="spread_input"
)
submit = st.button("Analyze crop problem", type="primary", use_container_width=True)

if submit:
    if not query.strip():
        st.warning("Please describe the crop symptoms first.")
        st.stop()
    try:
        # Securely persist user inputs in session_state
        st.session_state.original_form = {
            "crop": crop.strip(),
            "region": region.strip(),
            "stage": stage,
            "query": query.strip(),
            "spread": spread,
            "language": language
        }
        st.session_state.follow_up_history = []  # Reset follow-up history for a fresh analysis
        st.session_state.follow_up_answer = ""

        resolved_key = get_gemini_api_key(api_key_input)
        resolved_model = get_gemini_model()
        if not resolved_key:
            st.error("⚠️ GEMINI_API_KEY is missing. Please configure GEMINI_API_KEY in Streamlit Community Cloud Secrets, add it to your local .env file, or enter it in the sidebar.")
            st.stop()

        notes = load_reference_notes()
        pipeline = KisanSaathiPipeline(notes, api_key=resolved_key, model=resolved_model)
        with st.status("🌱 Analyzing crop problem...", expanded=True) as status:
            step_text = st.empty()
            def handle_step(msg):
                step_text.write(f"⏳ {msg}")
            result = pipeline.run(
                query=st.session_state.original_form["query"],
                crop=st.session_state.original_form["crop"],
                region=st.session_state.original_form["region"],
                stage=st.session_state.original_form["stage"],
                spread=st.session_state.original_form["spread"],
                language=st.session_state.original_form["language"],
                follow_up_answer="",
                previous_extraction=None,
                on_step=handle_step
            )
            status.update(label="✅ Analysis complete!", state="complete", expanded=False)
        st.session_state.result = result
    except Exception as exc:
        st.error(f"Could not complete the analysis: {exc}")
        st.info("Check that GEMINI_API_KEY is configured and that the selected Gemini model is available.")

# Render analysis results and follow-up interaction
if st.session_state.result:
    result = st.session_state.result
    extraction = result["extraction"]
    follow_up_q = extraction.get("follow_up_question", "").strip()

    st.divider()
    st.subheader("KisanSaathi assessment")

    # Initial assessment components
    st.markdown("### Possible causes")
    for item in result["diagnosis"].get("possible_causes", []):
        st.write(f"**{item.get('name', 'Possible cause')}**")
        st.write(item.get("reason", ""))
    st.markdown("### Advisory")
    st.write(result["advisory"].get("advice", "No advisory could be generated."))
    st.markdown("### What to observe next")
    for item in result["advisory"].get("next_steps", []):
        st.write(f"- {item}")
    if result["advisory"].get("escalate", True):
        st.error("Please consult an agriculture officer or your nearest Krishi Vigyan Kendra (KVK).")
        st.write(result["advisory"].get("escalation_reason", "The available information is insufficient for a safe recommendation."))
    st.caption("Safety note: No pesticide dosage or chemical application instruction is provided. Verify all actions with a qualified local agricultural expert.")

    # 1. & 2. Prominently display follow-up question below assessment whenever information is missing
    if follow_up_q:
        st.divider()
        st.warning("### ❓ Additional Information Needed")
        st.markdown(f"#### **{follow_up_q}**")
        if extraction.get("missing_information"):
            st.caption(f"Fields pending information: {', '.join(extraction['missing_information'])}")

        # 3. Provide an input field for user's answer and a Submit Answer button
        with st.form("follow_up_form"):
            follow_up_answer = st.text_input(
                "Your Answer:",
                placeholder="e.g. Flowering stage / Around 20% of plants are affected",
                key="follow_up_text_input"
            )
            submit_follow_up = st.form_submit_button("Submit Answer", type="primary")

        if submit_follow_up:
            if not follow_up_answer.strip():
                st.warning("Please type your answer before submitting.")
            else:
                submitted_ans = follow_up_answer.strip()
                # 4. Save the answer in Streamlit session_state
                st.session_state["follow_up_answer"] = submitted_ans
                st.session_state.follow_up_history.append({
                    "q": follow_up_q,
                    "a": submitted_ans
                })
                try:
                    resolved_key = get_gemini_api_key(api_key_input)
                    resolved_model = get_gemini_model()
                    if not resolved_key:
                        st.error("⚠️ GEMINI_API_KEY is missing. Please configure GEMINI_API_KEY in Streamlit Community Cloud Secrets, add it to your local .env file, or enter it in the sidebar.")
                        st.stop()

                    notes = load_reference_notes()
                    pipeline = KisanSaathiPipeline(notes, api_key=resolved_key, model=resolved_model)
                    with st.status("🌱 Updating analysis with your answer...", expanded=True) as status:
                        step_text = st.empty()
                        def handle_step(msg):
                            step_text.write(f"⏳ {msg}")

                        # 5. Pass answer to Gemini along with all previously collected crop information
                        orig = st.session_state.original_form
                        prev_extraction = st.session_state.result.get("extraction")

                        # 6. & 7. Update only relevant missing field and re-run diagnosis and advisory
                        updated_result = pipeline.run(
                            query=orig["query"],
                            crop=orig["crop"],
                            region=orig["region"],
                            stage=orig["stage"],
                            spread=orig["spread"],
                            language=orig["language"],
                            follow_up_answer=submitted_ans,
                            previous_extraction=prev_extraction,
                            on_step=handle_step
                        )
                        status.update(label="✅ Analysis updated!", state="complete", expanded=False)

                    # Update session state with merged result
                    clean_submitted = submitted_ans.rstrip(".?! ")
                    ans_to_record = updated_result["extraction"].get("follow_up_answer") or clean_submitted
                    st.session_state["follow_up_answer"] = ans_to_record
                    updated_result["follow_up_answer"] = ans_to_record
                    updated_result["extraction"]["follow_up_answer"] = ans_to_record
                    st.session_state.result = updated_result

                    # Update form data if follow-up answered spread, growth stage or crop
                    new_spread = updated_result["extraction"].get("spread", "")
                    if new_spread and new_spread.lower() not in ["unknown", "not sure"]:
                        st.session_state.original_form["spread"] = new_spread

                    new_stage = updated_result["extraction"].get("growth_stage", "")
                    if new_stage and new_stage.lower() not in ["unknown", "not sure"]:
                        st.session_state.original_form["stage"] = new_stage

                    new_crop = updated_result["extraction"].get("crop", "")
                    if new_crop and new_crop.lower() not in ["unknown", "not provided"]:
                        st.session_state.original_form["crop"] = new_crop

                    st.rerun()
                except Exception as exc:
                    st.error(f"Could not update the analysis: {exc}")
                    st.info("Check that GEMINI_API_KEY is configured and that the selected Gemini model is available.")

    # Display previously answered follow-up questions if available
    if st.session_state.follow_up_history:
        with st.expander("📝 Answered follow-up questions", expanded=False):
            for idx, item in enumerate(st.session_state.follow_up_history, 1):
                st.markdown(f"**Q{idx}:** {item['q']}")
                st.markdown(f"**Your answer:** {item['a']}")

    if st.session_state.get("follow_up_answer"):
        st.info(f"**Last submitted follow-up answer:** {st.session_state['follow_up_answer']}")

    # 8. Display the updated structured JSON so the answer can be verified
    with st.expander("🔍 View structured prompt workflow output (JSON)", expanded=bool(st.session_state.get("follow_up_answer"))):
        st.json(result)
