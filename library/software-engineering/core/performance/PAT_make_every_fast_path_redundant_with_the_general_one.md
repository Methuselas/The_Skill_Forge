---
object_id: PAT_make_every_fast_path_redundant_with_the_general_one
object_type: pattern
name: Every Fast Path Must Be Deletable Without Changing the Answer
library_path:
- software-engineering
- core
- performance
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- performance
- correctness
- optimization
- fallback
- testing
cross_links:
- rel: related_to
  target_object_id: PAT_check_the_last_used_slot_before_searching
- rel: related_to
  target_object_id: PAT_choose_the_level_before_tuning_the_code
- rel: related_to
  target_object_id: PAT_treat_conditionally_compiled_code_as_untested
reference:
  source_title: PASS software-engineering canonical synthesis
  author: Multiple accepted sources
confidence: medium
references: []
variants: []
---

# Every Fast Path Must Be Deletable Without Changing the Answer

## Pattern Rule
**IF** an operation has a cheap way that works for some inputs and a general way that works for all of them
**THEN** write the general way first and make it correct, then add each cheap path guarded by a condition under which it provably produces the identical result, so that deleting every fast path would change only the speed
**ELSE** where the cheap way would produce a different answer rather than the same answer sooner, it is a different operation and wants its own name instead of a branch inside this one.

## Do
- Build the general case first and leave it as the final branch. It is the thing that has to be right, every fast path is an exception to it, and a routine whose general case was written last tends to have been shaped around the shortcuts rather than the other way round.
- Make each fast path's condition exact rather than approximately safe. The guard defines the set of inputs on which the shortcut is claimed to be equivalent, so a guard that admits one input where the answers differ has converted an optimization into a defect that appears only for that input.
- Prefer the conservative test at the edges of a guard. Where a subtype might behave differently from the type you reasoned about, an exact type check admits less and stays correct, while a subtype-tolerant check is wider and quietly takes responsibility for every subtype anybody writes later.
- Order the checks by what they cost to evaluate, not by how often you imagine they fire, until you have measured which fire. Every guard is paid for by the inputs that fail it and fall through to the next one.
- Test each fast path against the general one on its own subset rather than against expected values. The claim being made is equivalence to a specific other implementation, and that is directly checkable by running both.
- Say what each shortcut is for. A guard reading as an arbitrary special case invites a later reader to widen it, and the widening is where the equivalence quietly stops holding.

## Don't
- Don't let a fast path change the answer in a way that seems harmless. A shortcut returning a shared object where the general path returns a copy, or preserving order where the general path does not, has changed behaviour that something downstream may depend on, and the difference will surface far away.
- Don't widen a guard to catch more cases without re-establishing equivalence for the cases it newly admits. The widening is usually motivated by a profile and reasoned about as if it were the same optimization, and it is a new one.
- Don't leave the general case unexercised. Once the fast paths cover the inputs the tests happen to use, the branch that must be correct is the branch nothing runs.
- Don't stack shortcuts until the operation is mostly guards. Past a handful, the reader cannot tell which branch a given input takes, and that is the point at which the equivalence stops being checkable by reading.

## Checklist
- If every fast path were deleted, would the results be identical and only the timing different?
- Is each guard exact about the inputs it claims equivalence for, or does it approximate that set?
- Which branch does the general case get exercised by, and does anything test it?
- Does any shortcut return something with different sharing, ordering, or identity than the general path returns?
- What does each guard cost on the inputs that fail it?

## Notes
The discipline this asks for is a claim rather than a preference: each shortcut asserts that for the inputs its guard admits, it computes what the general path would have computed. Stated that way the shortcut is checkable, because the thing it is claimed equivalent to is sitting in the same routine and can be run on the same inputs. Left unstated, a fast path becomes an independent implementation of part of the operation, maintained separately from the general case and diverging from it whenever either is edited.

The failure mode worth anticipating is not a wrong fast path but a widened one. Shortcuts arrive because a profile pointed at a hot input, and they are correct when written because their author had that input in mind. The guard is then relaxed later — a type test loosened to accept subtypes, an emptiness test extended to small collections — by somebody reading the shortcut as an optimization rather than as an equivalence claim. Nothing about the relaxation looks like a behaviour change, and the equivalence it silently depended on is nowhere written down.

Leaving the general case unexercised is the quieter half of the same problem. A well-covered set of shortcuts can take every input the tests supply, so the branch that defines what the operation means is the one branch no test enters. That is worth checking directly rather than assuming, because coverage tooling reports the routine as covered while the general path inside it has never run.
