# Changelog

All notable changes to **KisanSaathi – AI Crop Advisory Assistant** are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased] - Milestone 3 Planning
### Planned
- Integration of Vision-Language models for multi-modal foliar disease image classification.
- Audio speech-to-text input pipeline for rural voice queries (Hindi and regional dialects).
- Automated SMS / WhatsApp push notifications for localized pest alerts.

---

## [0.3.0] - 2026-11-22 (Milestone 2 Final Submission)
### Added
- **Directory Structure Conformance**: Added standardized `prompts/v1/`, `prompts/v2/`, `prompts/v3/`, `prompts/final/`, `final/`, `test-data/`, `docs/`, and `CHANGELOG.md`.
- **Anti-Contamination Rule 4 (`prompts/v3`)**: Independent multi-field extraction for compound follow-up answers (e.g. separating `"Flowering stage"` from `"20% affected"`).
- **Algorithmic Clause Splitters**: Programmatic regex extraction (`extract_growth_stage` and `extract_spread_phrase`) in `kisansaathi/pipeline.py`.
- **Benchmark Evaluation Suite**: `evaluation.py` with 12 end-to-end automated test cases and CSV exporter (`evaluation_results.csv`).
- **Deterministic Python Safety Backstops**: Auto-escalation (`escalate = True`) triggered upon high diagnostic uncertainty or rapid symptom expansion.
- **Low-Latency Engine**: Standardized on `gemini-flash-lite-latest` with strict 10s deadline (`HttpOptions(timeout=10000)`), `temperature=0.2`, and fast 2-try failover.
- **Visual Redesign**: Production-grade frontend with persistent BaseWeb tabs, high-contrast typography, ICAR evidence diagrams, and full SVG icon pack.

### Changed
- Refactored `EXTRACTION_PROMPT` to prevent compound text string copying across unrelated fields.
- Reduced retrieval context bloat by focusing top-$k$ TF-IDF chunks to top 2 relevant sections.
- Upgraded Google GenAI client integration to the official `google-genai` Python SDK.

### Fixed
- Eliminated infinite loading loops during transient API spikes via strict client deadlines and fast failover.
- Eliminated state loss across Streamlit session reruns by anchoring dialogue variables in `st.session_state`.
- Fixed Python `KeyError: '"name"'` formatting crash by escaping curly braces in `DIAGNOSIS_PROMPT`.

---

## [0.2.0] - 2026-11-21 (Milestone 2 Development - V2)
### Added
- **Sequential Follow-Up Protocol (`prompts/v2`)**: Prompt rules mandating exactly one follow-up question targeting the first missing information field.
- **Devanagari Script & Hinglish Enforcement**: Explicit language instructions ensuring Hindi responses use Devanagari script and Hinglish uses natural romanized colloquial mix.
- **TF-IDF Evidence Retrieval**: Local vector similarity search matching symptom descriptions against ICAR agronomic literature chunks.

### Fixed
- Fixed silent dialogue drop where the model returned empty follow-up questions while fields like `growth_stage` or `spread` remained unknown.

---

## [0.1.1] - 2026-11-20 (Milestone 2 Baseline - V1)
### Added
- `"follow_up_answer"` schema field in `EXTRACTION_PROMPT` to record user responses.

### Fixed
- Escaped curly braces in `DIAGNOSIS_PROMPT` JSON schema (`[{{...}}]`) resolving string formatting crash.

---

## [0.1.0] - 2026-11-19 (Milestone 1 Baseline - V0)
### Added
- Initial three-stage prototype: Extraction, Diagnosis, and Advisory prompt templates.
- Baseline Streamlit proof-of-concept user interface.
- Initial knowledge base `data/agriculture_notes.txt`.
