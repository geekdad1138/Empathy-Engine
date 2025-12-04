# Dataset Standards

## High-level rules
- **Consent-first:** all real user data used for training must have explicit opt-in.  
- **Anonymize:** remove direct identifiers; use differential privacy techniques where possible.  
- **Balanced representation:** ensure emotional examples cover range of cultures, age groups, communication styles.

## Dataset Structure
- `text`, `timestamp`, `source_type`, `affect_vector` (label), `intent_label`, `meta_tags`

## Annotation Guidelines
- Label emotion using multi-annotator scheme with majority vote + confidence score.  
- Annotate intent separately from affect.  
- Provide context snippets for annotators.

## Prohibited Data
- Private medical records without explicit consent and HIPAA-guarded contracts.  
- Unconsented crisis transcripts.  
- Content from minors unless explicit guardian consent exists and extra controls apply.

## Synthetic Data
- Use synthetic paraphrasing to expand rare emotion classes.  
- Keep synthetic clearly tagged and limit ratio in training to prevent drift.

## Quality Checks
- Inter-annotator agreement thresholds (Cohen’s Kappa > 0.6).  
- Random audit samples.  
- Bias checks across demographics.

## Versioning
- Maintain dataset manifest, source provenance, and release notes.  
- Each model training run references dataset commit hash.
