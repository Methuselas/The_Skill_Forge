---
object_id: PAT_optimize_a_codebase_for_its_likely_activities
object_type: pattern
name: Tune a Codebase for the Activities It Will Actually See
library_path:
- software-engineering
- core
- code-quality
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- code_quality
- api_design
- working_practice
- tradeoffs
cross_links:
- rel: related_to
  target_object_id: PAT_support_the_memory_system_the_activity_taxes
- rel: related_to
  target_object_id: PAT_expect_a_design_maneuver_to_cost_another_dimension
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Tune a Codebase for the Activities It Will Actually See

## Pattern Rule
**IF** you are deciding which cognitive dimension of a codebase to invest in
**THEN** work out which of the five programming activities people mostly do in it, because a dimension that helps one activity can actively harm another and there is no configuration that is good for all five.

## Do
- Identify the dominant activity first. Old, stable libraries are mostly searched; new applications are mostly incremented and transcribed. That difference alone reorders what is worth improving.
- For codebases that are **searched**, invest in secondary notation, which helps by letting comments and names signal where things are, and reduce hidden dependencies, which harm searching because you cannot tell what calls what.
- For codebases that are **comprehended**, invest in role expressiveness, visibility and abstraction, all of which help.
- For codebases that are **incremented**, invest in closeness of mapping, which lets people think in the code's goal rather than in programming concepts, and attack viscosity, which makes adding code harder.
- For codebases that are **explored**, invest in provisionality and progressive evaluation, and be wary of hard mental operations and heavy abstraction, which consume the load exploration needs.
- Re-evaluate over the codebase's life. The likely activities change as a project matures, so maneuvers that were right at the start stop being right.

## Don't
- Don't assume a universally good dimension. Consistency helps searching and comprehension and *harms* transcription, because new code has to be made to fit — worth it in the long run, and still a real cost paid by whoever is writing.
- Don't optimise for the activity you enjoy rather than the one your users perform. A library author explores; the library's users mostly search and comprehend.
- Don't skip the abstraction case. Abstraction helps comprehension and harms exploration, which is the one entry in the table that cuts both ways and is easy to read as unambiguously good.

## Checklist
- What do people mostly do in this codebase — search, comprehend, transcribe, increment, or explore?
- Has that changed in the last year?
- Is the dimension I am about to improve one that helps that activity, or one that helps a different one?

## Notes
The five activities and the dimensions come from the same framework, which is why they compose: Blackwell, Petre and Green described the activities precisely because they interact with the dimensions. The mapping is worth holding as a table rather than as prose, since several dimensions appear in both columns.

**One caution about that mapping.** Its Diffuseness row places *Searching* in the **Helps** column, while the surrounding prose says diffuseness "causes code to be longer, which also harms search simply because there is more code to search through." The table and the text contradict each other on this one row. The prose reading is the coherent one — more code to search through is more searching — and this card follows the prose. Every other row in the table agrees with the surrounding text.

The framing that makes this actionable is that a codebase's dimensions are not a quality score but a fit question. There is no dimension profile that is right in general; there is only one that matches what people do here.
