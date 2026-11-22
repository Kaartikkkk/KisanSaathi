import json
import os
import re
from google import genai
from kisansaathi.prompts import EXTRACTION_PROMPT, DIAGNOSIS_PROMPT, ADVISORY_PROMPT
from kisansaathi.retrieval import retrieve_notes

def extract_growth_stage(text):
    """
    Extracts only the agricultural growth stage name from text.
    Returns normalized stage name or None if not found.
    """
    if not text:
        return None
    t = text.lower()
    stages = [
        (["seedling", "germination", "nursery", "अंकुरण", "पौध"], "Seedling"),
        (["vegetative", "wanaspati", "वानस्पतिक", "बढ़वार"], "Vegetative"),
        (["flowering", "bloom", "फूल"], "Flowering"),
        (["fruiting", "fruit", "फल"], "Fruiting"),
        (["harvest", "maturity", "कटाई", "पकाई"], "Harvesting"),
    ]
    for keywords, standard_name in stages:
        if any(k in t for k in keywords):
            return standard_name
    return None

def extract_spread_phrase(text):
    """
    Extracts only the spread/affected rate phrase from a multi-part answer.
    Strips out growth stage keywords or clauses so that spread contains only spread info.
    """
    if not text:
        return None
    clean_text = text.strip()
    if " | A: " in clean_text:
        clean_text = clean_text.split(" | A: ")[-1].strip()
    elif clean_text.startswith("A: "):
        clean_text = clean_text[3:].strip()

    # Split into clauses by commas, semicolons, pipes, newlines, or conjunctions
    clauses = re.split(r'[,;\n|]|\b(?:and|aur|tatha|evam|va)\b', clean_text, flags=re.IGNORECASE)

    spread_keywords = [
        "%", "percent", "प्रतिशत", "affect", "प्रभावित", "spread", "फैलाव",
        "crop", "plant", "पौधे", "field", "खेत", "slowly", "rapidly", "fast",
        "tezi", "dheere", "around", "about", "lagbhag", "लगभग", "area", "hissa", "हिस्सा",
        "half", "quarter", "most", "entire", "few"
    ]
    stage_keywords = [
        "seedling", "vegetative", "flowering", "fruiting", "harvest",
        "stage", "avastha", "अवस्था", "अंकुरण", "वानस्पतिक", "फूल", "फल", "कटाई"
    ]

    candidate_clauses = []
    for clause in clauses:
        c = clause.strip()
        if not c:
            continue
        c_lower = c.lower()
        has_spread = any(kw in c_lower for kw in spread_keywords)
        has_stage = any(kw in c_lower for kw in stage_keywords)

        if has_spread:
            cleaned_c = c
            if has_stage:
                for st in [
                    "flowering stage", "vegetative stage", "seedling stage", "fruiting stage",
                    "harvesting stage", "harvest stage", "flowering", "vegetative",
                    "seedling", "fruiting", "harvest", "stage",
                    "फूल आने की अवस्था", "वानस्पतिक अवस्था", "अंकुरण अवस्था", "फल लगने की अवस्था"
                ]:
                    cleaned_c = re.sub(rf'\b{re.escape(st)}\b', '', cleaned_c, flags=re.IGNORECASE).strip()
                    cleaned_c = cleaned_c.lstrip(',- ')
            cleaned_c = cleaned_c.rstrip('.?! ')
            if cleaned_c:
                candidate_clauses.append(cleaned_c)

    if candidate_clauses:
        best = candidate_clauses[0]
        for cand in candidate_clauses:
            if "%" in cand or "affect" in cand.lower() or "spread" in cand.lower():
                best = cand
                break
        best = best.strip().rstrip('.?! ')
        if best:
            if best.isupper():
                return best.capitalize()
            return best[0].upper() + best[1:] if len(best) > 1 else best.upper()

    c_lower = clean_text.lower()
    if any(kw in c_lower for kw in spread_keywords) and not any(sk in c_lower for sk in stage_keywords):
        cleaned = clean_text.rstrip('.?! ')
        if cleaned:
            if cleaned.isupper():
                return cleaned.capitalize()
            return cleaned[0].upper() + cleaned[1:] if len(cleaned) > 1 else cleaned.upper()

    return None

def validate_field_values(merged, previous_extraction=None, follow_up_answer=""):
    """
    Validates and sanitizes fields in the merged extraction:
    1. Ensures growth_stage only contains growth stage values (never spread percentages or affected text).
    2. Ensures spread only contains spread/affected values (never growth stage names or full compound answers).
    3. Never allows complete compound follow-up answers to be copied into every field.
    4. Preserves previously known values if new values are invalid.
    """
    prev = previous_extraction or {}
    invalid_values = {"unknown", "not sure", "not provided", "none", "", "n/a", "null"}

    # 1. Validate growth_stage
    stage_val = merged.get("growth_stage", "")
    if stage_val and stage_val.lower() not in invalid_values:
        s_lower = stage_val.lower()
        if any(w in s_lower for w in ["%", "percent", "affect", "spread", "plants affected", "crop affected"]):
            cleaned_stage = extract_growth_stage(stage_val) or extract_growth_stage(follow_up_answer)
            if cleaned_stage:
                merged["growth_stage"] = cleaned_stage
            elif prev.get("growth_stage") and prev["growth_stage"].lower() not in invalid_values:
                merged["growth_stage"] = prev["growth_stage"]
            else:
                merged["growth_stage"] = "unknown"
        else:
            norm_stage = extract_growth_stage(stage_val)
            if norm_stage:
                merged["growth_stage"] = norm_stage

    # 2. Validate spread
    spread_val = merged.get("spread", "")
    if spread_val and spread_val.lower() not in invalid_values:
        sp_lower = spread_val.lower()
        has_stage_word = any(st in sp_lower for st in ["flowering", "seedling", "vegetative", "fruiting", "harvest"])
        if has_stage_word or (follow_up_answer and spread_val.strip().lower() == follow_up_answer.strip().lower() and has_stage_word):
            isolated_spread = extract_spread_phrase(spread_val) or extract_spread_phrase(follow_up_answer)
            if isolated_spread:
                merged["spread"] = isolated_spread
            elif prev.get("spread") and prev["spread"].lower() not in invalid_values:
                merged["spread"] = prev["spread"]
            else:
                merged["spread"] = "unknown"
        else:
            merged["spread"] = spread_val.rstrip(".?! ")

    # 3. Check for identical non-unknown values between growth_stage and spread (copy-paste contamination)
    if (merged.get("growth_stage") and merged.get("spread") and 
        merged["growth_stage"].lower() not in invalid_values and
        merged["spread"].lower() not in invalid_values and
        merged["growth_stage"].strip().lower() == merged["spread"].strip().lower()):

        extracted_st = extract_growth_stage(merged["growth_stage"]) or extract_growth_stage(follow_up_answer)
        extracted_sp = extract_spread_phrase(merged["spread"]) or extract_spread_phrase(follow_up_answer)

        merged["growth_stage"] = extracted_st if extracted_st else "unknown"
        merged["spread"] = extracted_sp if extracted_sp else "unknown"

    # 4. Recompute missing_information based on validated fields
    missing_fields = []
    if not merged.get("crop") or merged["crop"].lower() in invalid_values:
        missing_fields.append("crop")
    if not merged.get("symptoms"):
        missing_fields.append("symptoms")
    if not merged.get("broad_region") or merged["broad_region"].lower() in invalid_values:
        missing_fields.append("broad_region")
    if not merged.get("growth_stage") or merged["growth_stage"].lower() in invalid_values:
        missing_fields.append("growth_stage")
    if not merged.get("spread") or merged["spread"].lower() in invalid_values:
        missing_fields.append("spread")
    merged["missing_information"] = missing_fields

    return merged

def get_question_for_missing_field(field_name, language="English"):
    lang = (language or "English").lower()
    fn = (field_name or "").lower()

    if "crop" in fn:
        if "hindi" in lang and "hinglish" not in lang:
            return "कृपया अपनी फसल का नाम बताएं (जैसे टमाटर, गेहूं, मिर्च)?"
        elif "hinglish" in lang:
            return "Aap kaun si crop/fasal uga rahe hain (jaise Tomato, Wheat)?"
        else:
            return "What crop are you growing (e.g. Tomato, Wheat, Rice)?"

    if "stage" in fn or "growth" in fn or "age" in fn:
        if "hindi" in lang and "hinglish" not in lang:
            return "आपकी फसल अभी किस विकास अवस्था में है (जैसे अंकुरण, वानस्पतिक, फूल आने की, या फल लगने की अवस्था)?"
        elif "hinglish" in lang:
            return "Aapki crop abhi kis growth stage mein hai (jaise seedling, vegetative, flowering, fruiting, ya harvest)?"
        else:
            return "What is the current growth stage of your crop (e.g. seedling, vegetative, flowering, fruiting, or harvest)?"

    if "spread" in fn or "affect" in fn or "area" in fn or "much" in fn:
        if "hindi" in lang and "hinglish" not in lang:
            return "फसल का कितना हिस्सा प्रभावित है और क्या यह समस्या धीरे-धीरे या तेजी से फैल रही है?"
        elif "hinglish" in lang:
            return "Crop ka lagbhag kitna hissa affected hai aur problem slowly fail rahi hai ya rapidly?"
        else:
            return "How much of the crop is affected, and is the problem spreading slowly or rapidly?"

    if "region" in fn or "state" in fn or "location" in fn:
        if "hindi" in lang and "hinglish" not in lang:
            return "आपका खेत किस राज्य या क्षेत्र में स्थित है?"
        elif "hinglish" in lang:
            return "Aapka farm kis state ya region mein situated hai?"
        else:
            return "Which state or broad region is your crop located in?"

    if "symptom" in fn:
        if "hindi" in lang and "hinglish" not in lang:
            return "क्या आप पत्तियों या पौधों पर दिखने वाले अन्य लक्षणों के बारे में बता सकते हैं?"
        elif "hinglish" in lang:
            return "Kya aap leaves ya plants par dikhne wale aur symptoms describe kar sakte hain?"
        else:
            return "Could you describe any additional symptoms visible on the leaves or plants?"

    # Generic
    if "hindi" in lang and "hinglish" not in lang:
        return f"कृपया {field_name} के बारे में अतिरिक्त जानकारी प्रदान करें।"
    elif "hinglish" in lang:
        return f"Please {field_name} ke baare mein thodi aur detail batayein."
    else:
        return f"Could you provide more details regarding the {field_name}?"

def merge_extractions(previous_extraction, new_extraction, follow_up_answer="", form_crop="", form_region="", form_stage="", form_spread="", language="English"):
    """
    Merges newly extracted data with previously known extracted data and form inputs.
    Guarantees:
    - Known values (crop, region, stage, symptoms) are never overwritten by 'unknown', 'Not sure', or empty strings.
    - Follow-up answers are integrated into the relevant fields.
    - Computes missing_information deterministically from field states.
    - If missing_information is not empty, ensures exactly ONE relevant follow-up question is asked.
    - Never displays an empty question while fields are missing.
    """
    merged = dict(previous_extraction or {})
    new_data = dict(new_extraction or {})

    invalid_values = {"unknown", "not sure", "not provided", "none", "", "n/a", "null"}

    # 1. Merge crop
    new_crop = (new_data.get("crop") or "").strip()
    if new_crop and new_crop.lower() not in invalid_values:
        merged["crop"] = new_crop
    elif merged.get("crop") and merged["crop"].lower() not in invalid_values:
        pass  # retain existing known crop
    elif form_crop and form_crop.strip().lower() not in invalid_values:
        merged["crop"] = form_crop.strip()
    else:
        merged["crop"] = "unknown"

    # 2. Merge broad_region
    new_region = (new_data.get("broad_region") or "").strip()
    if new_region and new_region.lower() not in invalid_values:
        merged["broad_region"] = new_region
    elif merged.get("broad_region") and merged["broad_region"].lower() not in invalid_values:
        pass  # retain existing known region
    elif form_region and form_region.strip().lower() not in invalid_values:
        merged["broad_region"] = form_region.strip()
    else:
        merged["broad_region"] = "unknown"

    # 3. Merge growth_stage (extract independently)
    new_stage = (new_data.get("growth_stage") or "").strip()
    stage_from_answer = extract_growth_stage(follow_up_answer) if follow_up_answer else None

    if stage_from_answer:
        merged["growth_stage"] = stage_from_answer
    elif new_stage and new_stage.lower() not in invalid_values:
        norm_stage = extract_growth_stage(new_stage)
        merged["growth_stage"] = norm_stage if norm_stage else new_stage
    elif merged.get("growth_stage") and merged["growth_stage"].lower() not in invalid_values:
        pass  # retain existing known stage
    elif form_stage and form_stage.strip().lower() not in invalid_values:
        merged["growth_stage"] = form_stage.strip()
    else:
        merged["growth_stage"] = "unknown"

    # 4. Merge spread (extract independently, never whole answer or stage)
    new_spread = (new_data.get("spread") or "").strip()
    spread_from_answer = extract_spread_phrase(follow_up_answer) if follow_up_answer else None

    # If new_spread from model contains compound stage info or full answer, isolate the spread phrase
    if new_spread and new_spread.lower() not in invalid_values:
        isolated_new_spread = extract_spread_phrase(new_spread)
        if isolated_new_spread:
            new_spread = isolated_new_spread
        elif any(st in new_spread.lower() for st in ["seedling", "vegetative", "flowering", "fruiting", "harvest"]):
            new_spread = ""

    if spread_from_answer:
        merged["spread"] = spread_from_answer
    elif new_spread and new_spread.lower() not in invalid_values:
        merged["spread"] = new_spread
    elif merged.get("spread") and merged["spread"].lower() not in invalid_values:
        pass
    elif form_spread and form_spread.strip().lower() not in invalid_values:
        merged["spread"] = form_spread.strip()
    else:
        merged["spread"] = "unknown"

    # 5. Merge symptoms (preserve all unique symptoms)
    prev_symptoms = [s.strip() for s in merged.get("symptoms", []) if s and str(s).strip()]
    new_symptoms = [s.strip() for s in new_data.get("symptoms", []) if s and str(s).strip()]
    seen = {s.lower() for s in prev_symptoms}
    for s in new_symptoms:
        if s.lower() not in seen:
            prev_symptoms.append(s)
            seen.add(s.lower())
    merged["symptoms"] = prev_symptoms

    # 6. Validate and sanitize fields to guarantee independent extraction and relevancy
    merged = validate_field_values(merged, previous_extraction, follow_up_answer)

    # 7. Follow-up question generation (one question at a time for the first missing field):
    if not merged["missing_information"]:
        merged["follow_up_question"] = ""
    else:
        first_missing = merged["missing_information"][0]
        new_q = (new_data.get("follow_up_question") or "").strip()

        # Check if the model question specifically targets the first missing field and does not ask about known fields
        model_q_valid = False
        if new_q:
            q_lower = new_q.lower()
            if first_missing == "growth_stage" and any(w in q_lower for w in ["stage", "growth", "avastha", "अवस्था", "flowering", "seedling", "vegetative"]):
                model_q_valid = True
            elif first_missing == "spread" and any(w in q_lower for w in ["spread", "much", "affect", "area", "percent", "fail", "फैलाव", "हिस्सा", "कितना"]):
                model_q_valid = True
            elif first_missing == "crop" and any(w in q_lower for w in ["crop", "fasal", "फसल", "plant"]):
                model_q_valid = True
            elif first_missing == "broad_region" and any(w in q_lower for w in ["region", "state", "rajya", "राज्य", "area", "location"]):
                model_q_valid = True
            elif first_missing == "symptoms" and any(w in q_lower for w in ["symptom", "lakshan", "लक्षण", "leaves", "damage"]):
                model_q_valid = True

        if model_q_valid:
            merged["follow_up_question"] = new_q
        else:
            merged["follow_up_question"] = get_question_for_missing_field(first_missing, language)

    # 8. Record the submitted follow-up answer in merged extraction
    clean_answer = (follow_up_answer or "").strip()
    if " | A: " in clean_answer:
        clean_answer = clean_answer.split(" | A: ")[-1].strip()
    elif clean_answer.startswith("A: "):
        clean_answer = clean_answer[3:].strip()

    if clean_answer:
        merged["follow_up_answer"] = clean_answer.rstrip(".?! ")
    elif "follow_up_answer" not in merged:
        merged["follow_up_answer"] = (new_data.get("follow_up_answer") or "").strip().rstrip(".?! ")

    return merged

class KisanSaathiPipeline:
    def __init__(self, reference_notes, model=None, api_key=None):
        if not api_key:
            # Check Streamlit Community Cloud Secrets, then local os.getenv
            try:
                import streamlit as st
                api_key = st.secrets.get("GEMINI_API_KEY", "")
            except Exception:
                api_key = ""
            if not api_key:
                api_key = os.getenv("GEMINI_API_KEY", "")

        if not api_key or not str(api_key).strip():
            raise RuntimeError("GEMINI_API_KEY is missing. Please configure GEMINI_API_KEY in Streamlit Community Cloud Secrets, add it to your .env file, or enter it in the sidebar.")
        api_key = str(api_key).strip()

        if not model:
            try:
                import streamlit as st
                model = st.secrets.get("GEMINI_MODEL", "")
            except Exception:
                model = ""
            if not model:
                model = os.getenv("GEMINI_MODEL", "")
            if not model:
                model = "gemini-flash-lite-latest"

        # Initialize with a strict 10s timeout to guarantee responsive, low-latency UI
        from google.genai import types
        self.client = genai.Client(
            api_key=api_key,
            http_options=types.HttpOptions(timeout=10000)
        )
        self.model = str(model).strip()
        self.reference_notes = reference_notes

    def _ask_json(self, prompt, max_retries=2):
        import time
        from google.genai import types

        # Only use verified ultra-low-latency models (avoid slow 30s+ reasoning models)
        candidate_models = [
            self.model,
            "gemini-flash-lite-latest",
            "gemini-3.5-flash-lite"
        ]
        # Deduplicate while preserving priority order
        models_to_try = []
        for m in candidate_models:
            if m and m not in models_to_try:
                models_to_try.append(m)

        last_error = None
        for attempt in range(max_retries):
            current_model = models_to_try[attempt % len(models_to_try)]
            try:
                response = self.client.models.generate_content(
                    model=current_model,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        response_mime_type="application/json",
                        temperature=0.2
                    )
                )
                text = (response.text or "").strip()
                if text.startswith("```json"):
                    text = text[7:]
                if text.startswith("```"):
                    text = text[3:]
                if text.endswith("```"):
                    text = text[:-3]
                return json.loads(text.strip())
            except Exception as e:
                last_error = e
                err_str = str(e)
                # Quick retry on transient 503/429 with minimal sleep
                if attempt < max_retries - 1:
                    time.sleep(0.5)
                    continue
                raise last_error

    def run(self, query, crop="", region="", stage="Not sure", spread="Not sure", language="Hindi", follow_up_answer="", previous_extraction=None, on_step=None):
        if on_step:
            on_step("Stage 1/3: Extracting symptoms and details...")

        known_data_str = json.dumps(previous_extraction, ensure_ascii=False) if previous_extraction else "None (first turn)"

        try:
            raw_extraction = self._ask_json(EXTRACTION_PROMPT.format(
                query=query, crop=crop or "not provided", region=region or "not provided",
                stage=stage, spread=spread, language=language,
                known_data=known_data_str,
                follow_up_answer=follow_up_answer.strip() if follow_up_answer else "None provided"
            ))
        except Exception:
            raw_extraction = {
                "crop": crop or "unknown",
                "broad_region": region or "unknown",
                "growth_stage": stage if stage != "Not sure" else "unknown",
                "spread": spread if spread != "Not sure" else "unknown",
                "symptoms": [query] if query else [],
                "missing_information": [],
                "follow_up_question": ""
            }

        # Merge newly extracted details with previous extraction and form inputs
        extraction = merge_extractions(
            previous_extraction=previous_extraction,
            new_extraction=raw_extraction,
            follow_up_answer=follow_up_answer,
            form_crop=crop,
            form_region=region,
            form_stage=stage,
            form_spread=spread,
            language=language
        )

        if on_step:
            on_step("Stage 2/3: Matching reference notes & analyzing evidence...")

        # Build context query for retrieval using merged known details
        context_parts = [
            query,
            follow_up_answer or "",
            extraction.get("crop") if extraction.get("crop") != "unknown" else "",
            extraction.get("broad_region") if extraction.get("broad_region") != "unknown" else "",
            extraction.get("growth_stage") if extraction.get("growth_stage") != "unknown" else "",
            " ".join(extraction.get("symptoms", []))
        ]
        context_query = " ".join([p for p in context_parts if p and p.strip() and p != "Not sure" and p != "unknown"])
        retrieved = retrieve_notes(context_query, self.reference_notes, top_k=2)
        notes = "\n\n".join(x["text"] for x in retrieved) or "No relevant reference note was retrieved."

        try:
            diagnosis = self._ask_json(DIAGNOSIS_PROMPT.format(
                extraction=json.dumps(extraction, ensure_ascii=False), notes=notes
            ))
        except Exception:
            causes = []
            for n in retrieved[:2]:
                first_line = n["text"].split("\n")[0] if "\n" in n["text"] else n["text"]
                causes.append({"name": first_line[:60], "reason": n["text"][:220]})
            diagnosis = {
                "possible_causes": causes if causes else [{"name": "Agronomic Stress / Potential Disease", "reason": "Symptom matching from ICAR references indicates observation needed."}],
                "uncertainty": "high",
                "missing_information": ["under-leaf examination"]
            }

        if on_step:
            on_step(f"Stage 3/3: Generating safe advisory in {language}...")

        try:
            advisory = self._ask_json(ADVISORY_PROMPT.format(
                extraction=json.dumps(extraction, ensure_ascii=False),
                diagnosis=json.dumps(diagnosis, ensure_ascii=False),
                notes=notes, language=language
            ))
        except Exception:
            advisory = {
                "advice": f"Maintain non-chemical cultural sanitation for {extraction.get('crop', 'crop')}. Inspect plants regularly and isolate heavily affected foliage.",
                "next_steps": [
                    "Isolate and safely remove any severely spotted or wilting plant parts to prevent spore spread.",
                    "Ensure adequate drainage and avoid water stagnation around the root zone.",
                    "Disinfect pruners and farm tools before handling healthy plants.",
                    "Maintain close observation over the next 48-72 hours for signs of rapid expansion."
                ],
                "warning": "Strict ICAR Safety Rule: Never apply unverified synthetic chemical pesticides or spraying doses without physical agronomist inspection.",
                "escalate": True,
                "escalation_reason": "High-demand failover activated. Field inspection with local KVK agronomist recommended."
            }

        # Deterministic safety backstop: high uncertainty / no retrieved evidence => escalate.
        if diagnosis.get("uncertainty") == "high" or not retrieved:
            advisory["escalate"] = True
            if not advisory.get("escalation_reason"):
                advisory["escalation_reason"] = "The reference material was insufficient or uncertainty was high."

        return {
            "extraction": extraction,
            "retrieved_notes": retrieved,
            "diagnosis": diagnosis,
            "advisory": advisory,
            "follow_up_answer": extraction.get("follow_up_answer") or (follow_up_answer.strip() if follow_up_answer else "")
        }
