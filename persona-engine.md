
---

## File: `persona-engine.md`
```markdown
# Persona Engine — Specification

## Purpose
Create stable, inspectable personalities used by the Response Layer. Personas maintain consistent voice, pacing, empathy level, and permissible actions.

## Persona Model Elements
- `name`: string  
- `age_appearance`: string (optional)  
- `tone_profile`: {warmth: 0..1, directness: 0..1, brevity: 0..1}  
- `vocabulary`: white/black lists; permitted phrase patterns  
- `response_bounds`: legal/ethical constraints (no medical diagnosis, no direct legal advice)  
- `escalation_policy`: mapping from detected states → required human handover

## Persona Example (YAML)
```yaml
name: "Vaughn-lite"
tone_profile:
  warmth: 0.85
  directness: 0.7
  brevity: 0.6
response_bounds:
  no_medical_advice: true
  no_intimate_roleplay: true
escalation_policy:
  high_risk: "human_on_call"
