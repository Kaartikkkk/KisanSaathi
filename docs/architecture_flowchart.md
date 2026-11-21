# KisanSaathi Architecture & Workflow Flowcharts

This document provides visual architectural diagrams representing the KisanSaathi end-to-end system architecture, the three-stage prompt workflow, multi-turn state preservation, and the safety escalation mechanism.

---

## 1. End-to-End System Architecture

```mermaid
flowchart TD
    subgraph ClientLayer ["Farmer Interaction Layer (Streamlit UI)"]
        UI["Streamlit Web Interface (app.py)"]
        Inputs["Form Inputs: Crop, Region, Growth Stage, Spread, Query, Language"]
        StateStore[("Streamlit Session State<br/>• original_form<br/>• follow_up_history<br/>• result (JSON)")]
        UI --> Inputs
        Inputs --> StateStore
    end

    subgraph OrchestrationLayer ["Pipeline Orchestration (kisansaathi/pipeline.py)"]
        Runner["KisanSaathiPipeline.run()"]
        StateStore --> Runner

        subgraph Stage1 ["Stage 1: Extraction"]
            ExtPrompt["EXTRACTION_PROMPT (prompts.py)"]
            GeminiExt["Gemini 3.5 Flash Lite<br/>(application/json)"]
            RawExt["Raw Extraction JSON"]
            ExtPrompt --> GeminiExt --> RawExt
        end

        subgraph StateManagement ["State Management & Validation"]
            MergeLogic["merge_extractions()"]
            ClauseSplitter["extract_growth_stage()<br/>extract_spread_phrase()"]
            Validator["validate_field_values()"]
            CleanExt[("Merged & Validated Extraction")]

            RawExt --> MergeLogic
            StateStore -. Previous State .-> MergeLogic
            ClauseSplitter --> MergeLogic
            MergeLogic --> Validator --> CleanExt
        end

        subgraph RetrievalEngine ["Evidence Grounding (retrieval.py)"]
            QueryBuilder["Context Query Synthesizer"]
            TFIDF["TF-IDF Vectorizer + Cosine Similarity"]
            RefNotes[("Curated Knowledge Base<br/>data/agriculture_notes.txt")]
            RetrievedNotes["Top-k Grounding Evidence Chunks"]

            CleanExt --> QueryBuilder
            QueryBuilder --> TFIDF
            RefNotes --> TFIDF --> RetrievedNotes
        end

        subgraph Stage2 ["Stage 2: Grounded Diagnosis"]
            DiagPrompt["DIAGNOSIS_PROMPT (prompts.py)"]
            GeminiDiag["Gemini 3.5 Flash Lite<br/>(application/json)"]
            DiagOut["Diagnosis JSON<br/>(possible_causes, evidence_gaps, uncertainty, needs_expert)"]

            CleanExt & RetrievedNotes --> DiagPrompt --> GeminiDiag --> DiagOut
        end

        subgraph Stage3 ["Stage 3: Safe Advisory & Escalation"]
            AdvPrompt["ADVISORY_PROMPT (prompts.py)"]
            GeminiAdv["Gemini 3.5 Flash Lite<br/>(application/json)"]
            SafetyBackstop{"Safety Check:<br/>Uncertainty High OR<br/>No Retrieved Evidence?"}
            AdvOut["Final Advisory JSON<br/>(advice, next_steps, warning, escalate, escalation_reason)"]

            CleanExt & DiagOut & RetrievedNotes --> AdvPrompt --> GeminiAdv --> SafetyBackstop
            SafetyBackstop -- Yes --> ForceEscalate["Set escalate = True<br/>Inject KVK/Officer Escalation"] --> AdvOut
            SafetyBackstop -- No --> AdvOut
        end

        Runner --> Stage1 --> StateManagement --> RetrievalEngine --> Stage2 --> Stage3
    end

    subgraph OutputLayer ["Farmer Advisory & Follow-Up UI"]
        UI_Assessment["Display Possible Causes & Grounded Advice"]
        UI_Safety["Safety Warning & KVK Escalation Banner"]
        UI_FollowUp["Interactive Follow-Up Question Form<br/>(Submit Answer & Update)"]
        UI_JSON["Expandable Structured JSON Output"]

        AdvOut --> UI_Assessment
        AdvOut --> UI_Safety
        CleanExt -- "If missing_information is not empty" --> UI_FollowUp
        AdvOut & DiagOut & CleanExt --> UI_JSON
        UI_FollowUp -. "User submits follow-up answer" .-> StateStore
    end
```

---

## 2. Multi-Turn Follow-Up & Compound Answer Resolution

```mermaid
flowchart TD
    Start["Farmer Submits Follow-Up Answer<br/>(e.g., 'Flowering stage, around 20% of plants are affected.')"] --> InputClean["Normalize & Strip Trailing Punctuation"]
    
    subgraph MultiFieldParsing ["Independent Multi-Field Parsing"]
        InputClean --> StageCheck{"Contains Growth Stage Words?<br/>(e.g. flowering, vegetative, seedling)"}
        StageCheck -- Yes --> ExtractStage["extract_growth_stage()<br/>-> 'Flowering'"]
        StageCheck -- No --> KeepOldStage["Retain previous stage or 'unknown'"]

        InputClean --> SpreadCheck{"Contains Spread Indicators?<br/>(e.g. %, affected, spread, around)"}
        SpreadCheck -- Yes --> ExtractSpread["extract_spread_phrase()<br/>Isolates Spread Clause<br/>-> 'Around 20% of plants are affected'"]
        SpreadCheck -- No --> KeepOldSpread["Retain previous spread or 'unknown'"]
    end

    subgraph ValidationSanitization ["Cross-Field Validation (validate_field_values)"]
        ExtractStage --> ValStage{"Does growth_stage have % or spread text?"}
        ValStage -- Yes --> StripSpreadFromStage["Clean growth_stage"]
        ValStage -- No --> StageOK["growth_stage = 'Flowering'"]

        ExtractSpread --> ValSpread{"Does spread have growth stage names?"}
        ValSpread -- Yes --> StripStageFromSpread["Clean spread"]
        ValSpread -- No --> SpreadOK["spread = 'Around 20% of plants are affected'"]

        InputClean --> RawAnswer["follow_up_answer = 'Flowering stage, around 20% of plants are affected'"]
    end

    subgraph StateUpdate ["Session State & Missing Information Update"]
        StageOK & SpreadOK & RawAnswer --> UpdateMerged["Update Merged Record"]
        PreserveKnown["Preserve Known crop ('Tomato') & region ('Uttar Pradesh')"] --> UpdateMerged
        UpdateMerged --> RecomputeMissing["Recompute missing_information<br/>(Removes 'growth_stage' and 'spread')"]
        RecomputeMissing --> CheckEmpty{"Is missing_information empty?"}
        CheckEmpty -- Yes --> ClearQ["follow_up_question = ''"]
        CheckEmpty -- No --> NextQ["Generate question for next missing field"]
    end

    ClearQ & NextQ --> ReRun["Re-run Grounded Diagnosis & Safe Advisory"]
```

---

## 3. Sequence Diagram: Three-Stage Processing with Safety Guardrails

```mermaid
sequenceDiagram
    autonumber
    actor Farmer as Farmer / User
    participant UI as Streamlit UI (app.py)
    participant Pipe as Pipeline Orchestrator
    participant Gemini as Google Gemini 3.5 Flash Lite
    participant KB as TF-IDF Knowledge Base

    Farmer->>UI: Enter crop query & metadata (Hindi/Hinglish/English)
    UI->>Pipe: run(query, crop, region, stage, spread, language)

    Note over Pipe,Gemini: Stage 1: Extraction & Follow-Up Analysis
    Pipe->>Gemini: EXTRACTION_PROMPT (Query + Known Metadata)
    Gemini-->>Pipe: Extraction JSON (crop, symptoms, missing_info, follow_up_q)
    Pipe->>Pipe: merge_extractions() & validate_field_values()

    Note over Pipe,KB: Evidence Grounding
    Pipe->>KB: retrieve_notes(context_query, top_k=3)
    KB-->>Pipe: Grounded Reference Notes (Cautions, Irrigation, Escalation)

    Note over Pipe,Gemini: Stage 2: Grounded Diagnosis
    Pipe->>Gemini: DIAGNOSIS_PROMPT (Extraction + Reference Notes)
    Gemini-->>Pipe: Diagnosis JSON (possible_causes, evidence_gaps, uncertainty, needs_expert)

    Note over Pipe,Gemini: Stage 3: Safe Advisory Generation
    Pipe->>Gemini: ADVISORY_PROMPT (Extraction + Diagnosis + Notes + Language)
    Gemini-->>Pipe: Advisory JSON (advice, next_steps, warning, escalate)

    alt Uncertainty High OR Pest Dosage Requested OR Rapid Spread
        Pipe->>Pipe: Deterministic Safety Backstop (escalate = True)
    end

    Pipe-->>UI: Full Result Package (Extraction, Diagnosis, Advisory, Follow-up)
    UI-->>Farmer: Render Assessment, Advisory, Safety Banner, & Follow-Up Input
