---
object_id: PAT_settle_one_error_handling_strategy_systemwide
object_type: pattern
name: Decide Error Handling Once for the System, Not Once Per Function
library_path:
- software-engineering
- core
- error-handling
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- error_handling
- architecture
- consistency
- exceptions
- validation
cross_links:
- rel: related_to
  target_object_id: AP_decide_how_to_signal_and_handle_an_error
- rel: related_to
  target_object_id: PAT_judge_an_architecture_before_building_on_it
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants:
- variant_id: VAR_settle_the_cleanup_mechanism_too
  variant_name: Settle the Cleanup Mechanism, Not Just the Handling Policy
  variant_basis: context
  difference_from_foundation: The foundation settles what the system does about errors — correct or detect, propagate or handle locally, who validates. This variant settles the mechanical question that sits underneath and gets decided per-routine by default — how a routine that acquired resources releases them once a step partway through has failed. Four mechanisms compete and each buys something different. A jump to a single exit label avoids both deep nesting and redundant tests, at the price of an unstructured jump. Nested conditionals avoid the jump but bury the nominal path several levels deep and make the routine look more logically complex than it is. A status variable tested before each subsequent step avoids both the jump and the nesting and models the problem the way people describe it — find the file, and if everything is still fine open it, and if everything is still fine overwrite it — at the price of an extra test per step. A try-finally block avoids the jump, the nesting, and the extra tests, but exists only in some languages and assumes the operations signal failure by throwing rather than by returning codes. The recommendation is try-finally where the language offers it and the codebase has not already standardized on something else, and the status variable ahead of the other two otherwise.
  when_to_use: Use when a routine acquires something it must release — a file, a connection, allocated memory, a temporary — and any step between acquisition and release can fail. That is the case where the per-routine default is duplicated cleanup code, which is the outcome all four mechanisms exist to avoid.
  when_not_to_use: Do not treat the ranking as the point. The finding that survives is that any of the four works when applied consistently across a codebase, and mixing them is what costs — so an existing project's established mechanism beats the theoretically better one. It also does not apply where nothing needs releasing, in which case the guard-clause and early-return techniques settle the shape without any of this.
  absorbed_from_object_id: none
---

# Decide Error Handling Once for the System, Not Once Per Function

## Pattern Rule
**IF** you are starting a system, or writing the first error path in one that has no stated policy
**THEN** settle the handling questions systemwide before writing per-site handling, because the consequences reach across every module and cannot be made consistent by local decisions taken later.

## Do
- Answer whether handling is corrective or merely detective. Corrective means the program attempts recovery; detective means it continues as if nothing happened, or quits — and in either case it tells the user something was detected.
- Answer whether detection is active or passive. Active anticipates trouble, for instance by checking input validity; passive responds only when it cannot avoid it, such as when a combination of inputs produces numeric overflow. Both are defensible and the choice has user-interface consequences.
- Fix how errors propagate: discard the offending data immediately, enter an error-processing state, or continue and report at the end that errors occurred somewhere.
- Fix where they are handled: at the point of detection, by a dedicated error-handling class, or by passing up the call chain.
- Fix which layer validates. Either each class validates its own inputs, or a designated group of classes validates the system's data and everything inside that boundary may assume clean data. What breaks systems is neither policy — it is having both beliefs held in different modules.
- Decide explicitly whether to use the environment's built-in exception mechanism or your own, and settle when exceptions may be thrown, where they are caught, how they are logged and documented.
- Set the conventions for error messages at the same time.

## Don't
- Don't treat this as a coding-convention issue, or leave it to whatever each author does. The implications are systemwide even though every individual decision looks local.
- Don't assume the environment's error-handling approach is the right one just because it is there. That a platform ships a mechanism does not make it the best fit for your requirements.
- Don't underestimate the surface. Estimates suggest as much as 90 percent of a program's code goes to exceptional cases and housekeeping and only 10 percent to the nominal path — so an unspecified policy is unspecified across most of the code you will write.
- Don't let inconsistency reach the user. Without one strategy the interface reads as a collage of different interfaces assembled from different parts of the program, which is a design defect visible to people who never see the code.

## Checklist
- Can you state, in one sentence each, this system's answers on correction, detection, propagation, and handling location?
- If two modules disagree about who validates input, which one is wrong?
- Is the exception policy written down — throw sites, catch sites, logging, documentation?
- Would a user encountering three different errors in three parts of the program see three consistent behaviours?

## Notes
The reason this decision escapes its apparent scope is arithmetic. Any single error path looks like a local matter, so it gets decided locally, and the decision is reasonable each time. But because error and housekeeping code dominates the codebase, "decided locally each time" means the system's dominant behaviour was never designed — it accumulated. The visible symptom arrives late and at the user interface, by which point unwinding it means touching everything.

The validation-boundary question is the one that causes the most damage in practice, because both answers are correct and the failure comes from mixing them. If a designated group validates the system's inputs, everything downstream may assume clean data, and duplicate checks are noise. If each class validates its own, then no class may assume anything. What produces the real defects is a codebase where half the modules were written under one assumption and half under the other, so the checks are simultaneously redundant in some paths and absent in others.

`VAR_settle_the_cleanup_mechanism_too` pushes the same argument down one level, to the question of how a routine releases what it acquired when a step partway through fails. Four mechanisms compete — a jump to a single exit label, nested conditionals, a status variable tested before each subsequent step, and a try-finally block — and the useful part is that each buys a genuinely different thing. The jump avoids nesting and redundant tests but is unstructured. Nesting avoids the jump and buries the nominal path. The status variable avoids both and adds a test per step, while modelling the problem the way anyone would describe it aloud. try-finally avoids all three costs and is not universally available, and assumes failures arrive as thrown exceptions rather than returned codes. The recommendation is try-finally where the language has it and nothing else is established, and the status variable ahead of the remaining two otherwise.

What makes it belong to this card rather than standing alone is the conclusion. Any of the four works when applied consistently across a project, and the damage comes from mixing them — the same shape as the validation-boundary problem above, where both policies are correct and holding two at once is what produces defects. So this is a projectwide decision wearing the clothes of a per-routine one, which is exactly what the foundation warns about.

Fault tolerance is a separate axis from this policy and worth naming when reliability matters: retrying from a known-good point, switching to auxiliary code when the primary path faults, running several implementations and comparing their results, substituting a value known to be benign, or degrading to partial operation. Which of these is expected should be stated rather than discovered.
