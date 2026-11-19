import streamlit as st
from dotenv import load_dotenv
from kisansaathi.pipeline import KisanSaathiPipeline
from kisansaathi.retrieval import load_reference_notes

load_dotenv()
st.set_page_config(page_title="KisanSaathi", page_icon="🌱", layout="wide")

st.title("🌱 KisanSaathi")
st.caption("A multilingual, safety-first crop advisory assistant")
st.info("This prototype provides general information, not a confirmed diagnosis. For serious or spreading crop damage, contact a local agriculture officer or KVK.")

with st.sidebar:
    st.header("About")
    st.write("KisanSaathi uses a three-stage prompt workflow: extraction, grounded diagnosis and safe advisory generation.")
    language = st.selectbox("Preferred response language", ["Hindi", "English", "Hinglish"])
    st.caption("Do not enter names, phone numbers, exact addresses or other personal information.")

st.subheader("Describe your crop problem")
crop = st.text_input("Crop (if known)", placeholder="e.g. Tomato / गेहूं")
region = st.text_input("Region or state (broad location only)", placeholder="e.g. Uttar Pradesh")
stage = st.selectbox("Crop growth stage", ["Not sure", "Seedling", "Vegetative", "Flowering", "Fruiting", "Harvest"])
query = st.text_area("Describe the symptoms", placeholder="Example: Mere tamatar ke patton par peele dhabbe hain aur kinare mud rahe hain.", height=130)
spread = st.selectbox("How quickly is the problem spreading?", ["Not sure", "Not spreading", "Slowly", "Rapidly"])
submit = st.button("Analyze crop problem", type="primary", use_container_width=True)

if submit:
    if not query.strip():
        st.warning("Please describe the crop symptoms first.")
        st.stop()
    try:
        notes = load_reference_notes()
        pipeline = KisanSaathiPipeline(notes)
        with st.spinner("Understanding the symptoms..."):
            result = pipeline.run(
                query=query, crop=crop, region=region, stage=stage,
                spread=spread, language=language
            )
        st.divider()
        st.subheader("KisanSaathi assessment")
        extraction = result["extraction"]
        if extraction.get("follow_up_question"):
            st.warning("More information is needed")
            st.write(extraction["follow_up_question"])
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
        with st.expander("View structured prompt workflow output"):
            st.json(result)
    except Exception as exc:
        st.error(f"Could not complete the analysis: {exc}")
        st.info("Check that GEMINI_API_KEY is configured and that the selected Gemini model is available.")
