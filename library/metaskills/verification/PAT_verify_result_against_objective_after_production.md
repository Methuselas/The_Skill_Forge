---
object_id: PAT_verify_result_against_objective_after_production
object_type: pattern
name: Verify the Result Against the Objective After Production
library_path:
- metaskills
- verification
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- verification
- post_check
- instruction_following
- quality_control
cross_links: []
reference:
  source_id: bert_dodson_keys_to_drawing
  source_title: Keys to Drawing
  author: Bert Dodson
  publish_date: 1985
  media_type: PDF
  locator: u01, physical pp. 9-40
  evidence_type: mixed
confidence: high
references: []
variants: []
---

# Verify the Result Against the Objective After Production

## Pattern Rule
**IF** a task has produced a candidate result that is about to be declared complete
**THEN** switch out of production mode and evaluate the result against the actual objective, instructions, constraints, and success criteria rather than merely checking whether the chosen process was executed
**ELSE** keep producing until there is a concrete result to evaluate

## Do
- Ask whether the output achieved the requested external result, not whether effort or procedure felt complete.
- Re-read the governing instructions during the post-check when constraint compliance matters.
- Separate evaluation enough from generation that obvious omissions, contradictions, or drift can be noticed without defending the work.
- Route a detected failure back to the earliest step that owns it instead of cosmetically patching the finish.

## Don't
- Do not treat a successful internal workflow as proof that the delivered result is correct.
- Do not collapse evaluation into vague good/bad judgment; check the stated objective and constraints.
- Do not skip the post-check because the output is fluent, polished, or passes one superficial test.

## Checklist
- Every explicit requirement has been checked against the produced result.
- The main objective is satisfied independently of process compliance.
- Any failure has a named correction path before completion is claimed.

## Notes
Dodson separates the practical, curious state used while drawing from detached self-evaluation against the exercise's stated criteria. Guided teaching generalized the same post-check to writing, coding, research, and artifact work: production and verification solve different problems and should not be conflated.
