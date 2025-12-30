
---

## File: `memory-system-spec.md`
```markdown
# Memory System — Specification

## Goals
Enable contextual continuity: short-term session memory + long-term personal motifs while preserving privacy and user control.

## Memory Types
- **Episodic (short-term):** last N interactions (sliding window) — ephemeral, fast retrieval.  
- **Semantic (long-term):** distilled facts and patterns (e.g., "prefers short answers", "anxiety pattern: work-related on Thursdays").  
- **Emotional Baseline:** aggregated stats over time (mean valence, typical arousal ranges).

## Schema (SQL-like)
