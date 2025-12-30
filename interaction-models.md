# Interaction Models — Specification

## Conversation Patterns
- **Open Vent:** user expresses emotion without specific ask → model validates, mirrors, offers micro-actions.  
- **Ask for Help:** user requests specific assistance → model clarifies intent, offers immediate small steps, suggests escalation.  
- **Check-in Loop:** periodic friendly check exploring recent patterns (opt-in).  
- **Crisis Pathway:** immediate escalation, human handover, emergency resource surfacing.

## Turn-taking Rules
- Max reply length based on persona and context.  
- If user is high-arousal, prefer short replies and grounding steps.  
- Avoid asking multiple questions when user shows low dominance.

## Grounding & Micro-actions
Micro-actions are short, guided activities:
- Breathing (30–60s guided)
- 5-4-3-2-1 grounding
- Simple physical movement suggestions
- If user consents, scheduled gentle nudge to social contact

## Error Recovery
- When model confidence < threshold, admit uncertainty and ask clarifying, single-step question.  
- If user becomes frustrated, switch to "de-escalate" persona variant and offer "pause" or "human" options.

## Rate & Frequency
- Respect user fatigue: adaptive throttle based on recent engagement.  
- Avoid message flooding. Implement exponential backoff for proactive suggestions.

## Logging & Transparency
- Provide a succinct "why I said that" panel when requested: shows the short reasoning chain and which memories influenced the reply.
