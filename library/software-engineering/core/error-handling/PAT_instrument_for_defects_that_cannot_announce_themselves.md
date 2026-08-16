---
object_id: PAT_instrument_for_defects_that_cannot_announce_themselves
object_type: pattern
name: Instrument for Defects That Cannot Announce Themselves
library_path:
- software-engineering
- core
- error-handling
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- corruption
- detection
- debugging
- defensive_programming
cross_links:
- rel: related_to
  target_object_id: PAT_fail_fast_near_error_source
- rel: related_to
  target_object_id: PAT_make_the_development_build_fail_louder_than_production
- rel: related_to
  target_object_id: PAT_enforce_contracts_at_runtime_with_checks
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Instrument for Defects That Cannot Announce Themselves

## Pattern Rule
**IF** a defect class corrupts state silently, so that its symptoms appear somewhere unrelated to its cause and at an unpredictable time
**THEN** build a detector where none exists — plant values whose change proves corruption, and check them on a schedule you choose — so the failure becomes reproducible and local instead of erratic and distant.
**ELSE** where the platform already supplies such a detector, turn it on and spend your effort elsewhere rather than hand-rolling a second one.

## Do
- Plant a known value beside the data and verify it. A field written at allocation and checked at every use, and again at release, converts silent corruption into a specific failing check. Placing one before the block catches repeated release; placing one after it catches writes that ran past the end; using both catches both.
- Deliberately spoil the marker on release, so that a second release of the same thing finds a value that cannot be valid rather than a plausible one left over.
- Overwrite released storage with a recognizable pattern instead of leaving it intact. This is what turns an intermittent bug into a consistent one — released memory that still holds sensible-looking contents keeps working by accident for an unpredictable while, and the whole difficulty of the defect is that unpredictability.
- Validate against a record rather than against a guess. Keeping a list of what is currently live lets a release check membership, which is exact, where checking that an address falls in a plausible range is an approximation that passes bad values.
- Duplicate a field and compare the copies when a marker is not enough. Disagreement between two writes of the same value is proof that something in between wrote where it should not have.
- Check more often than the minimum. Testing the marker only at release tells you corruption happened at some point in the object's life; testing at every use narrows the window to the last few operations, which is the difference between a search and a diagnosis.

## Don't
- Don't run two of these strategies at once without deciding they compose. Several of them are alternatives rather than layers — a maintained list of live allocations already answers the question a planted marker was added to answer — and overlapping schemes cost overhead while producing conflicting accounts of the same failure.
- Don't scatter the instrumentation through the code that uses the data. It belongs in a small number of cover routines that wrap allocation and release, both because that is the only way to keep the strategy consistent and because it is the only place you can later change or remove it.
- Don't reason from the symptom. In this defect class the symptom's location carries no information about the cause — the same corruption may crash the process, quietly alter an unrelated calculation, cause routines to be skipped, or do nothing observable at all — so time spent working backward from where it surfaced is usually wasted.
- Don't treat "no symptoms yet" as evidence of correctness. The version that does nothing today is the one that surfaces at the least convenient moment, and it is the most common of the four outcomes rather than the rarest.

## Checklist
- If this state were corrupted right now, what would go wrong, and how far from here would it appear?
- Is there anything in the system that would notice, or would the corruption simply propagate?
- What value could be planted here whose change would prove interference?
- On release, is the thing left in a state where a second release is detectable?
- Are these checks in one place where they can be turned up during development and down in production?

## Notes
The reason this class of defect needs its own treatment is that the usual relationship between finding and fixing is inverted. For most defects, locating the fault is the easy half and repairing it is the work. Here the repair is often a single line and the locating consumes days, because nothing about where the program failed points at where it went wrong. Every technique here buys the same thing — a check that fires close to the cause — and pays for it in code that exists only to catch a defect that has not happened yet.

The instrumentation described here is period-specific and the principle is not. Hand-rolled markers, manual allocation registries, and macro wrappers around allocation were the tools available when this was written; today an address sanitizer, a bounds-checked container, or an ownership-tracking type supplies the same detection with far less hand-written apparatus, and reaching for those first is correct. The move that survives is the diagnostic one — when a failure mode produces no signal, the answer is to create a signal rather than to become better at reading noise, and that generalizes well past memory to cache staleness, event ordering, and any state a second writer can quietly change.

The centralization point is worth taking seriously on its own. The checks accumulate — validate the pointer is not null, confirm it is in the live list, spoil the contents, remove it from the list, release it, clear the reference — and written inline at each site they are both verbose and certain to diverge. Behind a pair of cover routines they are one implementation with one policy, and that is also where the development-versus-production asymmetry lives, since the same wrapper can halt the program during development and log and continue in production.
