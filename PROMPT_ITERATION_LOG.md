# KisanSaathi Prompt Iteration Log (V0 – V3)

This document records the exact progression, design decisions, and reasons for each iteration of the KisanSaathi prompt architecture across its three stages: **Extraction (`EXTRACTION_PROMPT`)**, **Evidence Analysis / Diagnosis (`DIAGNOSIS_PROMPT`)**, and **Safe Advisory (`ADVISORY_PROMPT`)**.

---

## Version Overview & History

| Version | Commit / Stage | Primary Motivation / Problem Addressed | Key Architectural Changes |
| :--- | :--- | :--- | :--- |
| **V0** | Baseline Commit `0e0889d` | Initial three-stage pipeline implementation. | Basic extraction without multi-turn answer integration; unescaped brace syntax error in diagnosis. |
| **V1** | Fix Commit `cd5a94a` | Python JSON formatting crash (`KeyError: '"name"'`) & missing answer recording. | Escaped curly braces in `DIAGNOSIS_PROMPT` (`[{{...}}]`); added `follow_up_answer` to extraction schema. |
| **V2** | Feature Enhancement (Reconstructed) | Lost crop details across Streamlit reruns; empty or skipped follow-up questions; language drift. | Added strict state management rules (Rules 1–5): sequential 1-at-a-time follow-up, value preservation, Devanagari Hindi/Hinglish enforcement. |
| **V3** | Anti-Contamination (Current Active) | Compound follow-up answers (e.g. `"Flowering stage, around 20% are affected"`) dumped full raw string into `spread`. | Added independent multi-field extraction rules; field-level validation isolating growth stage and spread clauses without contamination. |

---

## Detailed Version Breakdown

### Version 0 (V0) — Baseline Initial Implementation
- **Source**: Initial repository commit `0e0889d826db81e380f53ba7b00e1c73409d99cb`.
- **Architecture**:
  - `EXTRACTION_PROMPT`: Instructed model to extract only explicitly stated information from `{query}` and form details. Output schema contained `crop`, `symptoms`, `growth_stage`, `broad_region`, `spread`, `missing_information`, and `follow_up_question`.
  - `DIAGNOSIS_PROMPT`: Grounded diagnosis prompt instructing the model to rely solely on reference notes.
  - `ADVISORY_PROMPT`: Basic safety-first advisory prompt forbidding pesticide dosages and mandating escalation when uncertainty is high.
- **Identified Issues & Failure Modes**:
  1. **Syntax Error**: In `DIAGNOSIS_PROMPT`, the JSON template defined `"possible_causes": [{"name":"...", ...}]`. In Python, `DIAGNOSIS_PROMPT.format(...)` interpreted single curly brackets as string interpolation placeholders, triggering a runtime `KeyError: '"name"'`.
  2. **Follow-Up Limitation**: Extraction prompt only prompted for a follow-up question if `crop` or `symptoms` were missing, completely ignoring missing `growth_stage` or `spread`.
  3. **No Follow-Up Storage**: The schema had no `follow_up_answer` field, meaning submitted user answers could not be saved or verified in output JSON.

---

### Version 1 (V1) — Syntax Fix & Answer Schema Field
- **Source**: Commit `cd5a94a2e263211c89e8763023ad86bbcd0ec868`.
- **Changes Applied**:
  1. **Python Format String Escaping**: Escaped braces in `DIAGNOSIS_PROMPT` to `"possible_causes": [{{"name":"...", ...}}]`.
  2. **Answer Field Integration**: Added `"follow_up_answer": "the farmer's submitted answer or empty string"` to the JSON contract of `EXTRACTION_PROMPT`.
- **Identified Issues & Failure Modes**:
  1. **State Loss on Rerun**: When a farmer answered a follow-up question in the Streamlit UI, previous values for `crop`, `broad_region`, or `symptoms` were overwritten by `"unknown"` or lost entirely upon Streamlit rerun.
  2. **Skipped Follow-Up Questions**: If Gemini returned an empty string for `follow_up_question` while fields like `growth_stage` were still missing, the app silently finalized without asking the user for the missing detail.

---

### Version 2 (V2) — Strict State Management & Sequential Follow-Up
- **Source**: Reconstructed and implemented to solve state preservation and multi-turn follow-ups.
- **Changes Applied in `EXTRACTION_PROMPT`**:
  ```text
  STRICT STATE MANAGEMENT & SEQUENTIAL FOLLOW-UP RULES:
  1. IDENTIFY ALL MISSING FIELDS:
     - Check if crop, symptoms, broad_region, growth_stage, or spread are unknown or not provided.
     - List any unknown fields in missing_information (e.g. ["growth_stage", "spread"]).
  2. ASK ONE QUESTION AT A TIME:
     - If missing_information is NOT empty, you MUST generate exactly ONE concise, relevant follow-up question for the FIRST missing field.
     - NEVER return an empty follow_up_question when missing_information is not empty!
     - If missing_information is completely empty, set follow_up_question to "".
  3. PRESERVE KNOWN DATA:
     - Never revert a known value to "unknown", "Not sure", or empty string.
     - Retain previously extracted crop, region, growth stage, symptoms, and spread.
  4. MERGE FOLLOW-UP ANSWERS:
     - If a follow_up_answer is provided by the farmer, update ONLY the relevant field that was answered.
     - Remove the answered field from missing_information.
     - Record the submitted answer in follow_up_answer.
  5. LANGUAGE REQUIREMENT: If asking a follow-up question, write it in {language}:
     - Hindi: natural Hindi script (Devanagari).
     - Hinglish: natural conversational Romanized Hindi/English mix.
     - English: clear plain English.
  ```
- **Changes Applied in `ADVISORY_PROMPT`**:
  - Explicit scripts enforced: Hindi in Devanagari script, Hinglish in Romanized Hindi/English, and English in plain English.
- **Identified Issues & Failure Modes**:
  1. **Compound Multi-Part Answer Contamination**: When a farmer provided a combined answer answering both missing stage and spread (e.g. `"FLOWERING STAGE, AROUND 20% ARE AFFECTED"`), `growth_stage` was extracted as `"Flowering"`, but `spread` was assigned the entire compound string (`"FLOWERING STAGE, AROUND 20% ARE AFFECTED"`).

---

### Version 3 (V3) — Independent Multi-Field Extraction & Anti-Contamination (Current Active)
- **Source**: Current active production version in [kisansaathi/prompts.py](file:///Users/Kartikkk/Downloads/KisanSaathi/kisansaathi/prompts.py).
- **Changes Applied in `EXTRACTION_PROMPT`**:
  ```text
  4. INDEPENDENT MULTI-FIELD EXTRACTION FROM FOLLOW-UP ANSWERS:
     - When a farmer provides a compound or multi-part answer (e.g. "Flowering stage, around 20% of plants are affected"):
       * Extract each piece of information INDEPENDENTLY into its specific field.
       * Update "growth_stage" ONLY with the growth-stage value (e.g. "Flowering").
       * Update "spread" ONLY with the spread/affected rate (e.g. "Around 20% of plants are affected").
       * NEVER copy the entire compound answer into "spread", "growth_stage", or every missing field.
       * Keep the full original response in "follow_up_answer".
       * Remove all resolved fields from missing_information.
     - If only one field is answered, update ONLY that specific field.
  ```
- **Pipeline Complement (`kisansaathi/pipeline.py`)**:
  - Added programmatic clause splitting and regex isolation (`extract_growth_stage` and `extract_spread_phrase`).
  - Added deterministic pre-flight and post-flight validation (`validate_field_values`) ensuring neither field is contaminated by the other's keywords or the full raw response.
- **Outcome**:
  - For input: `"Flowering stage, around 20% of plants are affected."`
  - Extraction: `growth_stage = "Flowering"`, `spread = "Around 20% of plants are affected"`, `follow_up_answer = "Flowering stage, around 20% of plants are affected"`.
  - Zero cross-contamination, all previous fields (`crop`, `region`, `symptoms`) strictly preserved.
