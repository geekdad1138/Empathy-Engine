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
