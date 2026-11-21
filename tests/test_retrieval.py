from kisansaathi.retrieval import retrieve_notes

def test_retrieval_returns_relevant_notes():
    notes = [
        "Yellowing and leaf spots can have many causes.",
        "Check soil moisture and standing water.",
        "Consult an agriculture officer for rapidly spreading symptoms."
    ]
    result = retrieve_notes("yellow spots on leaves", notes)
    assert result
    assert "Yellowing" in result[0]["text"]

def test_empty_query_returns_no_notes():
    assert retrieve_notes("", ["some note"]) == []

def test_retrieval_with_follow_up_answer():
    notes = [
        "Tomato leaf curl virus is transmitted by whiteflies.",
        "Wheat rust causes brownish or reddish spots.",
        "Rice blast affects leaves, nodes, and panicles."
    ]
    # Simulates query + follow-up answer adding whitefly information
    combined_query = "Tomato leaf curl whiteflies observed under leaves"
    result = retrieve_notes(combined_query, notes)
    assert result
    assert "Tomato leaf curl" in result[0]["text"]

def test_merge_extractions_preserves_values_and_updates_stage():
    from kisansaathi.pipeline import merge_extractions

    # Initial extraction with missing growth stage
    previous = {
        "crop": "Tomato",
        "broad_region": "Uttar Pradesh",
        "growth_stage": "unknown",
        "spread": "Slowly",
        "symptoms": ["yellow spots", "curling leaves"],
        "missing_information": ["growth stage"],
        "follow_up_question": "What is the growth stage of your tomato crop?"
    }

    # Model in second turn extracted only the follow-up answer, returning unknown for crop and region
    new_raw = {
        "crop": "unknown",
        "broad_region": "unknown",
        "growth_stage": "Flowering stage",
        "spread": "unknown",
        "symptoms": [],
        "missing_information": ["crop", "region"],
        "follow_up_question": "Which crop is this?"
    }

    merged = merge_extractions(
        previous_extraction=previous,
        new_extraction=new_raw,
        follow_up_answer="Flowering stage",
        form_crop="Tomato",
        form_region="Uttar Pradesh"
    )

    # Must retain Tomato and Uttar Pradesh
    assert merged["crop"] == "Tomato"
    assert merged["broad_region"] == "Uttar Pradesh"
    # Must update growth stage to Flowering / Flowering stage
    assert "Flowering" in merged["growth_stage"]
    # Must preserve symptoms
    assert "yellow spots" in merged["symptoms"]
    assert "curling leaves" in merged["symptoms"]
    # Missing info must be cleared
    assert "crop" not in [m.lower() for m in merged["missing_information"]]
    assert "region" not in [m.lower() for m in merged["missing_information"]]
    assert "stage" not in [m.lower() for m in merged["missing_information"]]
    # Follow-up question must be empty because missing info is resolved
    assert merged["follow_up_question"] == ""

def test_merge_extractions_updates_spread_and_records_answer():
    from kisansaathi.pipeline import merge_extractions

    previous = {
        "crop": "Tomato",
        "broad_region": "Uttar Pradesh",
        "growth_stage": "Vegetative",
        "spread": "Not sure",
        "symptoms": ["yellow spots", "curling leaves"],
        "missing_information": ["how much of the crop is affected"],
        "follow_up_question": "How much of the crop is affected?"
    }

    # Model in second turn extracted follow-up answer about affected area
    new_raw = {
        "crop": "unknown",
        "broad_region": "unknown",
        "growth_stage": "unknown",
        "spread": "Around 20% of the crop",
        "symptoms": [],
        "missing_information": [],
        "follow_up_question": "",
        "follow_up_answer": "Around 20% of the crop."
    }

    merged = merge_extractions(
        previous_extraction=previous,
        new_extraction=new_raw,
        follow_up_answer="Around 20% of the crop.",
        form_crop="Tomato",
        form_region="Uttar Pradesh"
    )

    # Expected: crop and region remain unchanged
    assert merged["crop"] == "Tomato"
    assert merged["broad_region"] == "Uttar Pradesh"
    # Spread is updated
    assert "20%" in merged["spread"]
    # follow_up_answer contains the submitted answer
    assert "20%" in merged["follow_up_answer"]
    # Missing information is cleared
    assert not any("crop" in m.lower() for m in merged["missing_information"])
    assert not any("spread" in m.lower() or "affect" in m.lower() for m in merged["missing_information"])
    # No repeated question
    assert merged["follow_up_question"] == ""

def test_sequential_two_step_follow_up():
    from kisansaathi.pipeline import merge_extractions

    # Turn 1: Initial state - Tomato, Uttar Pradesh, yellow spots, curling leaves, stage unknown, spread unknown
    raw_turn1 = {
        "crop": "Tomato",
        "broad_region": "Uttar Pradesh",
        "growth_stage": "unknown",
        "spread": "unknown",
        "symptoms": ["yellow spots", "curling leaves"],
        "missing_information": ["growth_stage", "spread"],
        "follow_up_question": ""
    }
    turn1_merged = merge_extractions(
        previous_extraction=None,
        new_extraction=raw_turn1,
        form_crop="Tomato",
        form_region="Uttar Pradesh",
        form_stage="Not sure",
        form_spread="Not sure",
        language="English"
    )

    # First question asks about growth stage
    assert "growth_stage" in turn1_merged["missing_information"]
    assert "spread" in turn1_merged["missing_information"]
    assert "stage" in turn1_merged["follow_up_question"].lower() or "growth" in turn1_merged["follow_up_question"].lower()

    # Turn 2: User answers "Flowering stage"
    raw_turn2 = {
        "crop": "unknown",
        "broad_region": "unknown",
        "growth_stage": "Flowering stage",
        "spread": "unknown",
        "symptoms": [],
        "missing_information": ["spread"],
        "follow_up_question": ""
    }
    turn2_merged = merge_extractions(
        previous_extraction=turn1_merged,
        new_extraction=raw_turn2,
        follow_up_answer="Flowering stage",
        form_crop="Tomato",
        form_region="Uttar Pradesh",
        language="English"
    )

    # Stage is updated, crop & region preserved
    assert turn2_merged["crop"] == "Tomato"
    assert turn2_merged["broad_region"] == "Uttar Pradesh"
    assert "flowering" in turn2_merged["growth_stage"].lower()
    assert "growth_stage" not in turn2_merged["missing_information"]
    assert "spread" in turn2_merged["missing_information"]
    # Next question asks about spread
    assert any(w in turn2_merged["follow_up_question"].lower() for w in ["spread", "affect", "much", "area"])

    # Turn 3: User answers "Around 20% of plants are affected."
    raw_turn3 = {
        "crop": "unknown",
        "broad_region": "unknown",
        "growth_stage": "unknown",
        "spread": "Around 20% of plants are affected.",
        "symptoms": [],
        "missing_information": [],
        "follow_up_question": ""
    }
    turn3_merged = merge_extractions(
        previous_extraction=turn2_merged,
        new_extraction=raw_turn3,
        follow_up_answer="Around 20% of plants are affected.",
        form_crop="Tomato",
        form_region="Uttar Pradesh",
        language="English"
    )

    # Final verification: All preserved, missing info empty, no more questions
    assert turn3_merged["crop"] == "Tomato"
    assert turn3_merged["broad_region"] == "Uttar Pradesh"
    assert "flowering" in turn3_merged["growth_stage"].lower()
    assert "20%" in turn3_merged["spread"]
    assert turn3_merged["missing_information"] == []
    assert turn3_merged["follow_up_question"] == ""
    assert "20%" in turn3_merged["follow_up_answer"]

def test_independent_follow_up_extraction():
    from kisansaathi.pipeline import merge_extractions

    previous = {
        "crop": "Tomato",
        "broad_region": "Uttar Pradesh",
        "growth_stage": "unknown",
        "spread": "unknown",
        "symptoms": ["yellow spots", "curling leaves"],
        "missing_information": ["growth_stage", "spread"],
        "follow_up_question": "What is the current growth stage of your crop?"
    }

    # Model in second turn returned flowering stage but accidentally put the full answer in spread
    new_raw = {
        "crop": "unknown",
        "broad_region": "unknown",
        "growth_stage": "Flowering",
        "spread": "Flowering stage, around 20% of plants are affected.",
        "symptoms": [],
        "missing_information": [],
        "follow_up_question": "",
        "follow_up_answer": "Flowering stage, around 20% of plants are affected."
    }

    follow_up_input = "Flowering stage, around 20% of plants are affected."

    merged = merge_extractions(
        previous_extraction=previous,
        new_extraction=new_raw,
        follow_up_answer=follow_up_input,
        form_crop="Tomato",
        form_region="Uttar Pradesh"
    )

    # 1. Extract multiple pieces of info independently
    # 2. Update growth_stage only with growth-stage value
    assert merged["growth_stage"] == "Flowering"
    # 3. Update spread only with spread-related value
    assert merged["spread"] == "Around 20% of plants are affected"
    # 4. Never copy complete answer into every missing field
    assert merged["growth_stage"] != follow_up_input
    assert merged["spread"] != follow_up_input
    # 5. Preserve previously known values
    assert merged["crop"] == "Tomato"
    assert merged["broad_region"] == "Uttar Pradesh"
    assert "yellow spots" in merged["symptoms"]
    assert "curling leaves" in merged["symptoms"]
    # 6. Keep original follow-up answer in follow_up_answer
    assert merged["follow_up_answer"] == "Flowering stage, around 20% of plants are affected"
    # 7. Validation check passed: missing info resolved, no more questions
    assert merged["missing_information"] == []
    assert merged["follow_up_question"] == ""

def test_compound_uppercase_answer_isolation():
    from kisansaathi.pipeline import merge_extractions

    # Reproduces the exact reported bug:
    # User answers: "FLOWERING STAGE, AROUND 20% ARE AFFECTED"
    # Model extracted growth_stage = "Flowering", but put the full answer in spread
    previous = {
        "crop": "Tomato",
        "broad_region": "Uttar Pradesh",
        "growth_stage": "unknown",
        "spread": "unknown",
        "symptoms": ["yellow spots", "curling leaves"],
        "missing_information": ["growth_stage", "spread"],
        "follow_up_question": "What is the current growth stage?"
    }

    new_raw = {
        "crop": "unknown",
        "broad_region": "unknown",
        "growth_stage": "Flowering",
        "spread": "FLOWERING STAGE, AROUND 20% ARE AFFECTED",
        "symptoms": [],
        "missing_information": [],
        "follow_up_question": ""
    }

    follow_up_input = "FLOWERING STAGE, AROUND 20% ARE AFFECTED"

    merged = merge_extractions(
        previous_extraction=previous,
        new_extraction=new_raw,
        follow_up_answer=follow_up_input,
        form_crop="Tomato",
        form_region="Uttar Pradesh"
    )

    assert merged["growth_stage"] == "Flowering"
    assert merged["spread"] == "Around 20% are affected"
    assert merged["follow_up_answer"] == "FLOWERING STAGE, AROUND 20% ARE AFFECTED"
    assert merged["crop"] == "Tomato"
    assert merged["broad_region"] == "Uttar Pradesh"
    assert merged["missing_information"] == []

