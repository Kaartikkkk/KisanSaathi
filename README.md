# KisanSaathi

A multilingual, safety-first crop advisory prototype built around a three-stage prompt chain.

## Current implementation
1. Information extraction (structured JSON)
2. Reference-note retrieval and cautious possible-cause analysis
3. Multilingual advisory generation with escalation rules

The local retrieval component currently uses TF-IDF over a small, illustrative reference-note file. This is a lightweight retrieval prototype, not a production agricultural knowledge base. Replace or expand the notes using verified public agricultural material and record the sources before evaluation.

## Setup (macOS / Windows)

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\Activate.ps1

pip install -r requirements.txt
cp .env.example .env
```

Add your own Gemini API key to `.env`. Never commit `.env` or share your API key.

Run:

```bash
streamlit run app.py
```

## Tests

```bash
pytest -q
```

These are software tests for the retrieval helper. They are not evidence that agricultural advice is correct.

## Important limitations
- The current reference notes are starter examples, not a complete or officially validated crop-disease database.
- TF-IDF retrieval is lexical and may miss relevant notes.
- Model-generated possible causes are not diagnoses.
- The app must not be used to decide pesticide doses or chemical treatment.
- Verify agricultural content with ICAR, state agriculture departments, KVKs or other authoritative sources before public deployment.
- Use synthetic test cases; do not enter farmer names, phone numbers or exact addresses.

## Prompt versioning for the project report
Save each actual prompt draft in `prompt_versions/` (create this folder), record the date, change and reason in the iteration log, and retain outputs from identical test cases. Do not claim a version was tested until you have run it.

## Suggested next steps
1. Verify the Gemini model name available to your API key.
2. Replace starter notes with cited, crop-specific reference material.
3. Add a test-case table with expected output, actual output and Pass/Fail.
4. Record prompt versions and evaluate Hindi, English and Hinglish cases.
5. Add a human review step before considering any real-world pilot.
