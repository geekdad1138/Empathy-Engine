# Testing & Evaluation

## Objectives
Verify accuracy, safety, and alignment. Track drift and regressions.

## Test Categories
1. **Unit tests** — functions: embedding → vector, intent classifier, memory store.  
2. **Integration tests** — pipeline: user input → affective vector → response selection → persona filter.  
3. **Behavioral tests** — scenario-driven conversations with expected outcomes.  
4. **Red-team tests** — adversarial prompts to probe failure modes.  
5. **Human-in-the-loop validation** — expert reviewers rate real interactions.

## Metrics
- **Affect accuracy** — MAE on valence/arousal/dominance vs. annotated gold.  
- **Response appropriateness** — human-rated scale (1–5).  
- **Escalation precision/recall** — proportion of true high-risk flagged.  
- **Conversational coherence** — perplexity & human coherency score.  
- **User wellbeing delta** — A/B test pre/post short-term distress score.

## Benchmarks
- Create canonical test set with controlled paraphrases and emotional variance.  
- Run monthly automated regression tests.

## Continuous Evaluation
- Live monitoring for drift (mean valence vs. baseline).  
- Alert when major distributional shifts occur.  
- Periodic re-annotation cycles for data refresh.

## Safety validation
- Approve every change that affects escalation policy via manual sign-off.  
- Maintain a rollback plan with immediate reverting ability.

## Reporting
- Weekly dashboard with key metrics, monthly human review summaries, and quarterly public transparency snapshot.
