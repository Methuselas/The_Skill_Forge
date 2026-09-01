---
object_id: DRILL_stress_test_the_core_resolution_grammar
object_type: drill
name: Stress-Test the Core Resolution Grammar
library_path:
- game-design
- mechanics
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- mechanics
- resolution
- refactoring
- playtesting
cross_links:
- rel: teaches
  target_object_id: PAT_reuse_core_resolution_grammar_before_adding_new_mechanics
- rel: teaches
  target_object_id: PAT_invoke_resolution_only_for_meaningful_uncertainty
- rel: supports
  target_object_id: PAT_evaluate_mechanics_by_the_decisions_and_agency_they_create
- rel: teaches
  target_object_id: PAT_build_complete_resolution_procedures_incrementally
reference:
  source_title: Designing TTRPGs For Dummies
  author: Martin Buinicki
confidence: high
target_skill: Determine when a core resolution grammar is broad enough, whether added mechanics integrate into complete resolution procedures, when no resolution is needed, and when a specialized subsystem genuinely earns its additional complexity.
references: []
variants: []
---

# Stress-Test the Core Resolution Grammar

## Practice Task
Run a mixed set of ordinary, pressured, unusual, and subsystem-like situations through the current core mechanics, then perform one incremental integration pass on a known-working resolution procedure. Once the ordinary procedure is stable, perform an adversarial constraint pass that deliberately searches for legal combinations that bypass a mechanic's intended limiter. Record which cases need no check, which fit the established grammar, which additions integrate cleanly, which constraints fail under composition, and which genuinely require refactoring or specialized procedure.

## Target Skill
Determine when a core resolution grammar is broad enough, whether added mechanics integrate into complete resolution procedures, when no resolution is needed, and when a specialized subsystem genuinely earns its additional complexity.

## Setup
Choose a game with a defined core resolution method. Prepare six short test situations: one routine action with no meaningful failure state; the same or a similar action under pressure; one physical challenge; one social or informational challenge; one unusual edge case not explicitly covered by the written rules; and one activity that appears to deserve its own subsystem. For at least one task with a known or plausible duration, also prepare a compressed-time version in which the available window is substantially shorter than the normal work time. Identify one already-working multi-step resolution procedure and one plausible new mechanic that could be inserted into it. After the baseline game is stable enough for hostile testing, select one powerful mechanic or option and name the cost, cap, scarcity, action tax, risk, prerequisite, or other constraint that is supposed to keep it safe.

## Instructions
1. For each situation, state what success changes, what failure changes, and whether uncertainty is meaningful enough to invoke resolution.
2. Classify each case as no check, core resolution, or specialized subsystem before executing it.
3. Execute every case classified as core resolution and record arithmetic, lookups, state tracking, explanation time, and any exception logic needed.
4. For the incremental integration pass, write the known-working procedure from trigger to termination and execute that baseline once before changing it.
5. Insert the proposed mechanic at the point where its required inputs first exist, then re-execute every affected branch of the complete procedure. If anything breaks, classify the failure as a problem in the mechanic itself, its insertion/order, or its interaction with existing state before adding another rule.
6. For the unusual edge case, attempt to express it through existing primitives before writing any new rule; record exactly where the attempt succeeds or breaks down.
7. For the apparent subsystem case, first execute a compressed version through the core mechanic, then execute or concretely simulate the proposed specialized procedure.
8. Compare the two subsystem executions and identify any decisions, information, tactics, pacing, or genre experience that exist only in the specialized version.
9. Test one plausible bespoke-rule near-miss: add a case-specific rule that solves the immediate problem but does not generalize, then identify whether it creates an adapter, exception, or new lookup burden.
10. For each recurring gap, choose apply, extend, refactor, or new subsystem and record the reason for that choice.
11. Apply temporal compression to the prepared extended task: reduce the available time and test whether the existing grammar supports rushing through difficulty, modifiers, assistance, reduced scope or quality, added risk, partial completion, or an explicit impossibility boundary. Record which response the system produces and whether a bespoke time rule was actually necessary.
12. Once the relevant procedure is stable, perform an adversarial constraint pass on the selected mechanic. Trace every rule that can modify its inputs, derived values, timing, action cost, resource cost, duration, stacking, stored state, or downstream outputs. Test extreme but legal combinations and record whether any combination bypasses the constraint that was supposed to regulate the mechanic.
13. Distinguish an exploit from ordinary system mastery by recording severity, accessibility, frequency, investment, and whether the interaction defeats a major intended constraint. Prefer the smallest clean repair that restores the constraint, but redesign the underlying mechanic when the failure is structural rather than local.
14. Remove any proposed check, mechanic, or procedural stage whose execution cost does not buy a meaningful difference in play.

## Success Check
- At least one prepared situation was actually resolved without a check because failure had no meaningful consequence; merely labeling a case “routine” does not pass.
- At least one unexpected or explicitly uncovered situation was actually executed through the established grammar and produced a usable result without a bespoke rule.
- The named near-miss is a concrete case-specific patch, and the record states what adapter, exception, lookup, or maintenance cost it introduces; a generic warning about complexity does not pass.
- The subsystem candidate was executed or concretely simulated both through the core mechanic and through the specialized procedure, with at least one observed difference recorded.
- Any retained specialized subsystem names the decision or experience that justifies its extra procedure; “it is more detailed” does not pass.
- Every apply, extend, refactor, or new-subsystem choice includes the observed reason for the selection rather than only the selected label.
- The compressed-time case was actually tested, and the record states whether scarcity produced a meaningful tradeoff, exposed a missing interface, or merely changed an existing difficulty or consequence.
- The incremental integration pass includes a known-working baseline, one inserted mechanic, a full re-execution of affected branches, and any failure is classified as mechanic, insertion/order, or interaction failure before another patch is proposed.
- The adversarial constraint pass begins only after the tested procedure is stable enough to distinguish ordinary defects from deliberate exploitation, names the limiter being attacked, and tests at least one extreme legal combination against it.
- Any discovered exploit is classified by severity, accessibility, frequency, investment, and the constraint it defeats before a repair is proposed; a merely clever or rare advantage is not automatically labeled a defect.

## Common Failures
- Inventing new procedures before attempting to express the case through established mechanics.
- Treating every task as a roll simply because the core mechanic can resolve it.
- Declaring a subsystem richer without running the compressed and specialized versions against the same situation.
- Keeping a one-off patch because it fixes the current example while ignoring the additional interface it creates.
- Refusing every subsystem on principle even when the core mechanic erases the decisions the game is supposed to foreground.
- Treating a shorter deadline as an automatic new subsystem instead of first testing the game’s existing difficulty and consequence grammar.
- Testing a new mechanic only in isolation and assuming the larger resolution procedure still works.
- Adding an exception immediately after an integration failure instead of first diagnosing the mechanic, its insertion point, or its interaction with existing state.
- Sending adversarial testers to crack an unstable baseline and mistaking ordinary broken behavior for meaningful exploit evidence.
- Testing a powerful mechanic only in its expected use case instead of tracing the legal rules that can amplify, store, duplicate, bypass, or otherwise escape its intended limiter.
- Calling every optimized combination an exploit without considering how difficult, rare, expensive, or consequential it is to assemble.
- Patching several downstream systems when a smaller change can cleanly sever the offending dependency.

## Notes
A core mechanic should be broad enough to absorb ordinary variation but not so dominant that every distinct activity collapses into the same experience. This drill separates three decisions that are often conflated: whether resolution is needed, whether the existing grammar can express the situation, and whether a specialized subsystem adds enough meaningful play to justify its operating cost. Temporal compression is a useful integration stress because it can pressure several mechanics at once without introducing a new test language: an eight-hour repair attempted inside four hours may reveal whether difficulty, assistance, interruption, partial progress, scope, and consequences already connect coherently. Incremental integration adds the complementary development test: preserve a known-working baseline, add one mechanic at its dependency point, and rerun the complete affected procedure before continuing. This makes regression diagnosable and discourages patch accretion around an interaction that should instead be redesigned. Once that baseline is stable, adversarial playtesting asks a different question: not whether the procedure executes, but whether legal composition can escape the assumptions that keep its strongest mechanics safe. A useful burn identifies the intended limiter first, then searches across stacking, derived values, action economy, stored effects, duration, resource conversion, and cross-procedure handoffs for ways around it. Rare, expensive, or difficult optimizations may be acceptable system mastery; high-impact interactions that cheaply defeat a major constraint are stronger exploit signals. When a local dependency is the problem, prefer the smallest repair that restores the intended constraint rather than accumulating compensating patches elsewhere.
