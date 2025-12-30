# Memory System — Specification

## Goals
Enable contextual continuity: short-term session memory + long-term personal motifs while preserving privacy and user control.

## Memory Types
- **Episodic (short-term):** last N interactions (sliding window) — ephemeral, fast retrieval.  
- **Semantic (long-term):** distilled facts and patterns (e.g., "prefers short answers", "anxiety pattern: work-related on Thursdays").  
- **Emotional Baseline:** aggregated stats over time (mean valence, typical arousal ranges).

## Schema (SQL-like)
````

USER_PROFILE(id, hashed_id, consent_flags, created_at)
EPISODES(id, user_id, timestamp, raw_text, affect_vector, tags)
SEMANTIC_FACTS(id, user_id, key, value, weight, last_updated)
EMOTIONAL_SUMMARY(user_id, mean_valence, mean_arousal, last_sampled)

```

## Retrieval & Scoring
- Query returns top-K memories weighted by:
  - recency (decay function)
  - relevance (embedding similarity)
  - importance (manually flagged or high-weighted semantic facts)

Score = `alpha*recency + beta*relevance + gamma*importance`

## Decay & Forgetting
- Episodic memory: default window 7 days, configurable per deployment.  
- Semantic facts: decays slowly; requires reinforcement to stay above threshold.  
- Forget API: user can request deletion; system executes irreversible purge and writes audit entry.

## Privacy & Controls
- Default retention short; user opt-in to extended memory.  
- All identifiable data hashed & encrypted at rest.  
- Requests to export user memory produce a downloadable, time-limited package with audit trail.

## Safety
- Sensitive tags (health, harm) are stored with heightened controls and require explicit policy for sharing.
