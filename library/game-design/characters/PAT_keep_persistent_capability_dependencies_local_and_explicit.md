---
object_id: PAT_keep_persistent_capability_dependencies_local_and_explicit
object_type: pattern
name: Keep Persistent Capability Dependencies Local and Explicit
library_path:
- game-design
- characters
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- advancement
- bookkeeping
- characters
- dependencies
cross_links:
- rel: related_to
  target_object_id: PAT_derive_character_capabilities_from_expected_play
- rel: related_to
  target_object_id: PAT_evaluate_mechanics_by_the_decisions_and_agency_they_create
- rel: related_to
  target_object_id: PAT_account_for_the_intended_play_environment_before_freezing_the_design
reference:
  source_title: GURPS Basic Set, Fourth Edition
  author: Steve Jackson, David L. Pulver, and Sean M. Punch
confidence: high
references: []
variants: []
---

# Keep Persistent Capability Dependencies Local and Explicit

## Pattern Rule
**IF** changing or advancing one recorded capability can alter the persistent value or purchase efficiency of another
**THEN** prefer local recorded state, and when a dependency is necessary, record its parent, transformation, and purchased contribution explicitly enough that every affected value can be propagated or recomputed without reconstructing advancement history
**ELSE** keep one-time situational borrowing or default use as a runtime modifier rather than turning it into persistent accounting.

## Do
- Distinguish temporary transfer of competence from persistent advancement. A character may use a related skill at a penalty without requiring that relationship to reprice previously purchased training.
- If advancement genuinely depends on another capability, expose the dependency on the sheet or in the implementation instead of expecting players to remember which value used to be derived from which.
- Store purchased contribution separately from any current derived baseline when later changes can move that baseline.
- Test dependency reversal: raise the formerly weaker capability above its parent and verify whether every dependent value still follows an unambiguous rule.
- Count the audit radius of an advancement change. Raising one capability should not require an open-ended search through unrelated sheet entries.
- In software, propagate derived changes automatically while preserving a readable breakdown of current parent values and purchased contributions.

## Don't
- Require players to reinterpret already-spent advancement points against a new baseline after another capability becomes stronger unless the relationship is explicit and automatically auditable.
- Hide bidirectional or reversible dependencies inside prose when either side can become the other's effective parent later.
- Treat mathematical conservation as sufficient usability when a missed recalculation can leave the character sheet wrong.
- Build chains of defaults or derived values that require users to reconstruct intermediate states that are not themselves recorded.

## Checklist
- Raising any recorded capability has a bounded, identifiable set of persistent entries that must change or be audited.
- Every derived persistent value can be reconstructed from current explicit state rather than remembered purchase order or historical baselines.
- A test in which two related capabilities exchange which one is higher produces an unambiguous result without manual reinterpretation of prior spending.
- Temporary use of related competence remains possible without automatically creating a persistent advancement dependency.
- When automation is used, the interface can explain which parent value and purchased contribution produced the displayed result.

## Notes
Related-skill defaults can be excellent runtime tools: they let existing expertise answer a nearby problem without requiring every competence to be purchased separately. The maintenance problem begins when that temporary relationship becomes a mutable accounting baseline for persistent advancement. If improving either side can change which skill should subsidize the other, the character sheet becomes a dependency graph whose correct state depends on recalculation rather than merely recorded purchases. Keeping runtime transfer separate from persistent state preserves the useful fiction of cross-training while reducing historical bookkeeping. When persistent dependency is worth keeping, it should behave like an explicit data model: current parents, transformations, and purchased deltas must be recoverable directly from the present record.
