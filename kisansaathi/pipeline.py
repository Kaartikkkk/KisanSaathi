import json
import os
from google import genai
from kisansaathi.prompts import EXTRACTION_PROMPT, DIAGNOSIS_PROMPT, ADVISORY_PROMPT
from kisansaathi.retrieval import retrieve_notes

class KisanSaathiPipeline:
    def __init__(self, reference_notes, model=None):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY is missing. Add it to your .env file.")
        self.client = genai.Client(api_key=api_key)
        self.model = model or os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
        self.reference_notes = reference_notes

    def _ask_json(self, prompt):
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config={"response_mime_type": "application/json"}
        )
        return json.loads(response.text)

    def run(self, query, crop="", region="", stage="Not sure", spread="Not sure", language="Hindi"):
        extraction = self._ask_json(EXTRACTION_PROMPT.format(
            query=query, crop=crop or "not provided", region=region or "not provided",
            stage=stage, spread=spread, language=language
        ))
        context_query = " ".join([
            query, crop, region, stage,
            " ".join(extraction.get("symptoms", []))
        ])
        retrieved = retrieve_notes(context_query, self.reference_notes)
        notes = "\n\n".join(x["text"] for x in retrieved) or "No relevant reference note was retrieved."
        diagnosis = self._ask_json(DIAGNOSIS_PROMPT.format(
            extraction=json.dumps(extraction, ensure_ascii=False), notes=notes
        ))
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
