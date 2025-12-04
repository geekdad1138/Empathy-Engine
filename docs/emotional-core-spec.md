# Emotional Core — Specification

## Overview
The Emotional Core converts raw inputs (text ± voice) into a compact affective state representation used throughout the system.

## Data Model — Affective Vector
- `valence` (float: -1..1) — overall pleasantness  
- `arousal` (float: 0..1) — activation/energy  
- `dominance` (float: 0..1) — control vs. overwhelmed  
- `confidence` (float: 0..1) — model certainty  
- `tags` (list[str]) — extracted keywords (e.g., "loss", "anger", "exhaustion")
- `intent` (enum) — {inform, vent, ask_help, meta, unknown}

Example JSON:
```json
{
  "valence": -0.6,
  "arousal": 0.8,
  "dominance": 0.2,
  "confidence": 0.86,
  "tags": ["work", "overwhelm"],
  "intent": "vent"
}
````

## Input Processing Pipeline

1. **Normalization:** lowercase, punctuation retention options, emoji mapping.
2. **Tokenization:** sentence/utterance split.
3. **Embedding:** sentence-transformer or local embedding model.
4. **Emotion Mapping:** classifier/regressor that maps embeddings + prosody → affective vector.
5. **Intent Extraction:** small intent classifier (fine-grained intents).
6. **Confidence Estimation:** ensemble or softmax calibration.

## Models & Techniques

* **Embeddings:** `all-MiniLM-L6-v2` or local equivalent.
* **Emotion classifier/regressor:** lightweight MLP on top of embeddings; calibrated with Platt scaling.
* **Prosody (optional):** voice amplitude, pitch variance -> arousal/dominance estimation.
* **Fallback rules:** keyword lists for immediate detection (suicidal ideation, harm, emergency).

## Safety / Redlines

* High-risk keywords immediately elevate to `risk_level: high` regardless of confidence.
* If `valence < -0.8` & `intent == ask_help` or `tags include 'harm'` → route to human review.

## Outputs

* Affective Vector (primary)
* Short diagnostic text (for UI): one-line explanation of what was detected and why.
* Suggested actions (score-ordered): e.g., "5 breath box", "call friend", "see therapist".

## Tests

* Unit tests for mapping from canonical sentences → expected vector range.
* Synthetic stress tests with paraphrases and negations.
