# Agronomic Knowledge Base

This folder contains the verified agricultural reference notes used by KisanSaathi's TF-IDF retrieval engine.

## Contents

- `agriculture_notes.txt`: Domain-specific agronomic guidance compiled from Indian Council of Agricultural Research (ICAR) extension literature, State Agricultural Universities (SAUs), and Krishi Vigyan Kendra (KVK) advisories.

## Structure

Notes are organized into thematic chunks separated by `---` delimiters:
1. Crop symptom identification criteria (e.g. leaf spots, wilting, curling, rusts).
2. Non-chemical cultural management practices (sanitation, moisture regulation, rogueing).
3. Risk thresholds and expert escalation triggers.

## Usage in Pipeline

During Stage 2 of the advisory pipeline, `kisansaathi.retrieval.retrieve_notes` computes cosine similarity over TF-IDF vectors of the farmer query against these reference chunks, grounding the downstream Gemini diagnosis.
