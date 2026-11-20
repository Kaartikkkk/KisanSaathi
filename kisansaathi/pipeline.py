import json
import os
from google import genai
from kisansaathi.prompts import EXTRACTION_PROMPT, DIAGNOSIS_PROMPT, ADVISORY_PROMPT
from kisansaathi.retrieval import retrieve_notes

class KisanSaathiPipeline:
    def __init__(self, reference_notes, model=None, api_key=None):
        api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY is missing. Add it to your .env file or enter it in the sidebar.")
        self.client = genai.Client(api_key=api_key)
        self.model = model or os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")
        self.reference_notes = reference_notes

    def _ask_json(self, prompt, max_retries=4):
        import time
        for attempt in range(max_retries):
            try:
                response = self.client.models.generate_content(
                    model=self.model,
                    contents=prompt,
                    config={"response_mime_type": "application/json"}
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
                if ("503" in str(e) or "429" in str(e) or "UNAVAILABLE" in str(e)) and attempt < max_retries - 1:
                    time.sleep(3 * (attempt + 1))
                    continue
                raise

    def run(self, query, crop="", region="", stage="Not sure", spread="Not sure", language="Hindi", on_step=None):
        if on_step:
            on_step("Stage 1/3: Extracting symptoms and details...")
        extraction = self._ask_json(EXTRACTION_PROMPT.format(
            query=query, crop=crop or "not provided", region=region or "not provided",
            stage=stage, spread=spread, language=language
        ))
        if on_step:
            on_step("Stage 2/3: Matching reference notes & analyzing evidence...")
        context_query = " ".join([
            query, crop, region, stage,
            " ".join(extraction.get("symptoms", []))
        ])
        retrieved = retrieve_notes(context_query, self.reference_notes)
        notes = "\n\n".join(x["text"] for x in retrieved) or "No relevant reference note was retrieved."
        diagnosis = self._ask_json(DIAGNOSIS_PROMPT.format(
            extraction=json.dumps(extraction, ensure_ascii=False), notes=notes
        ))
        if on_step:
            on_step(f"Stage 3/3: Generating safe advisory in {language}...")
        advisory = self._ask_json(ADVISORY_PROMPT.format(
            extraction=json.dumps(extraction, ensure_ascii=False),
            diagnosis=json.dumps(diagnosis, ensure_ascii=False),
            notes=notes, language=language
        ))
        # Deterministic safety backstop: high uncertainty / no retrieved evidence => escalate.
        if diagnosis.get("uncertainty") == "high" or not retrieved:
            advisory["escalate"] = True
            if not advisory.get("escalation_reason"):
                advisory["escalation_reason"] = "The reference material was insufficient or uncertainty was high."
        return {
            "extraction": extraction,
            "retrieved_notes": retrieved,
            "diagnosis": diagnosis,
            "advisory": advisory
        }
