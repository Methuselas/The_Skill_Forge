---
object_id: AP_alternate_search_and_control_cycles
object_type: ap
name: Alternate Search and Control Cycles
library_path:
- metaskills
- iterative-construction
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- search
- control
- exploration
- refinement
- iteration
cross_links:
- rel: supports
  target_object_id: PAT_verify_result_against_objective_after_production
- rel: supports
  target_object_id: PAT_generate_novel_options_by_combining_distant_concepts
- rel: related_to
  target_object_id: AP_plan_and_build_work_from_thumbnail_to_final
- rel: related_to
  target_object_id: AP_progress_artifact_through_ratified_steps
reference:
  source_title: Keys to Drawing
  author: Bert Dodson
confidence: high
references: []
variants: []
---

# Alternate Search and Control Cycles

## Objective
Develop complex work by alternating operations that discover possibilities with operations that constrain, verify, organize, or refine them, instead of demanding exploration and final precision from the same operation at the same time.

## Steps / Flow
1. **Search.** Generate, observe, probe, or sketch enough alternatives to expose promising directions without requiring final precision.
2. **Control the search.** Activate `PAT_verify_result_against_objective_after_production`. Compare the discovered material against the current objective, structure, constraints, or tests; identify what survives and what does not.
3. **Reopen Search when the solution space fails or the next unresolved level becomes available.** Broad rejection is a reason to search again, not merely to polish rejected options. Preserve useful critique and constraints while allowing genuinely different solutions. When the reopened search keeps returning the family that was just rejected, activate `PAT_generate_novel_options_by_combining_distant_concepts`.
4. **Control a viable result.** Consolidate, verify, clean, test, or refine material that remains directionally sound without reopening commitments that have already been ratified.
5. **Nest smaller loops when needed.** A Control phase may reopen a local Search when evidence shows the current solution is inadequate; a Search phase may pause for a small Control check before exploration drifts too far.
6. **Do not confuse Control with authority.** Evaluation, ranking, recommendation, or the assistant's artistic preference can inform a decision but cannot substitute for an approval that the surrounding workflow requires from the user or another authority.
7. **Do not confuse the mode with the artifact step.** Search and Control describe how attention operates; a staged or domain-specific workflow describes what information the work currently contains. The current step defines what Search is allowed to invent and what Control must preserve.

## Notes
Dodson distinguishes a freer, intuitive handwriting from a slower, analytical one and shows artists moving back and forth between them. The transferable behavior is the alternation, not a fixed mapping such as “this numbered stage is always Search.”

In a staged visual workflow, Stage 0 may contain a large Search loop followed by Control and user selection; after that approval, Stage 1 primarily Controls the chosen picture while searching only inside unresolved structural decisions. Other domains can map the same modes differently.
