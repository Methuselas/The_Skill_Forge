---
object_id: DRILL_stress_test_mechanical_constraints_under_composition
object_type: drill
name: Stress-Test Mechanical Constraints Under Composition
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
- exploits
- constraints
- playtesting
cross_links:
- rel: supports
  target_object_id: PAT_evaluate_mechanics_by_the_decisions_and_agency_they_create
- rel: supports
  target_object_id: PAT_build_complete_resolution_procedures_incrementally
- rel: related_to
  target_object_id: DRILL_stress_test_the_core_resolution_grammar
- rel: related_to
  target_object_id: DRILL_trace_a_character_option_into_play
confidence: high
target_skill: Determine whether legal combinations bypass an intended mechanical constraint and distinguish a genuine exploit from acceptable system mastery.
references: []
variants: []
---

# Stress-Test Mechanical Constraints Under Composition

## Practice Task
Take one stable, powerful mechanic or option, name the limiter that is supposed to keep it safe, trace the legal rules that can interact with it, and execute an adversarial composition test designed to escape that limiter. Classify any advantage by its impact and practical availability before deciding whether it is acceptable system mastery, a local exploit, or evidence that the underlying mechanic needs redesign.

## Target Skill
Determine whether legal combinations bypass an intended mechanical constraint and distinguish a genuine exploit from acceptable system mastery.

## Setup
Choose a mechanic or option whose ordinary procedure already works reliably enough that hostile testing will not merely rediscover baseline defects. Name the cost, cap, scarcity, action tax, risk, prerequisite, duration, or other constraint that is supposed to regulate its power. Prepare the rules that can modify its inputs, derived values, timing, action cost, resource cost, duration, stacking, stored state, or downstream outputs.

## Instructions
1. State the intended limiter in testable terms: what behavior or output it is meant to prevent, cap, price, delay, or expose to risk.
2. Execute the ordinary baseline once. If the mechanic fails before adversarial composition begins, stop and repair the baseline rather than calling the ordinary defect an exploit.
3. Trace every legal rule that can amplify, reduce, store, duplicate, convert, bypass, reorder, extend, or otherwise change the limiter or the mechanic it regulates.
4. Construct and actually execute or concretely simulate at least one extreme but legal combination that presses hardest on the named limiter.
5. Record the complete interaction chain and whether the limiter still performs its intended job under that composition.
6. If the combination produces an unusual advantage, classify its **severity**, **accessibility**, **frequency**, and **investment**, and state which intended constraint it defeats, if any.
7. Distinguish exploitation from system mastery. A clever, rare, expensive, risky, or highly situational optimization may be acceptable when the intended limiter still matters; a cheap or repeatable interaction that defeats a major constraint is a stronger defect signal.
8. Diagnose the smallest correct owner of the failure. If one dependency cleanly bypasses an otherwise sound constraint, repair that dependency. If legal play repeatedly escapes the mechanic's basic regulating assumption, redesign or remove the underlying mechanic instead of building compensating patches around it.
9. Rerun the hostile combination after any repair and test nearby dependencies that could inherit the change.

## Success Check
- The ordinary baseline was actually executed successfully before hostile testing; merely asserting that it is stable does not pass.
- The limiter is named in terms that make a bypass observable rather than as a vague claim that the mechanic should be “balanced.”
- At least one extreme but legal combination was actually executed or concretely simulated against the limiter.
- The record shows the interaction chain that produces the tested result rather than only the final optimized build or number.
- Any unusual advantage is classified by severity, accessibility, frequency, and investment, and the record states whether a major intended constraint was actually defeated.
- The record names at least one plausible near-miss: an optimized interaction that is strong or clever but does **not** defeat the limiter, and explains why treating that case as an exploit would confuse system mastery with a defect.
- If a repair is proposed, the record explains why the failure is local or structural, and the changed behavior is rerun rather than accepted from reasoning alone.

## Common Failures
- Sending adversarial testers to crack an unstable baseline and mistaking ordinary broken behavior for meaningful exploit evidence.
- Testing a powerful mechanic only in its expected use case instead of tracing the legal rules that can amplify, store, duplicate, bypass, or otherwise escape its intended limiter.
- Calling every optimized combination an exploit without considering how difficult, rare, expensive, risky, or consequential it is to assemble.
- Looking only for high output while ignoring action economy, duration, resource conversion, stored effects, stacking, and cross-procedure handoffs.
- Patching several downstream systems when a smaller change can cleanly sever the offending dependency.
- Preserving a structurally broken mechanic by adding exception after exception because the first mechanic was treated as untouchable.

## Notes
Adversarial constraint testing asks a different question from ordinary procedure testing: not merely whether the rule executes, but whether legal composition can escape the assumptions that keep its strongest effects safe. Identify the intended limiter first, then search the legal interaction surface for ways around it. Rare, expensive, difficult, risky, or highly situational optimizations may be acceptable system mastery; high-impact interactions that cheaply or repeatedly defeat a major constraint are stronger exploit signals. When a local dependency is the problem, prefer the smallest repair that restores the intended constraint. When the regulating assumption itself collapses under ordinary legal composition, redesigning or removing the mechanic is cleaner than accumulating patches.
