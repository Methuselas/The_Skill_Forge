---
object_id: PAT_give_each_variable_exactly_one_purpose
object_type: pattern
name: Give Each Variable Exactly One Purpose
library_path:
- software-engineering
- core
- variables
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- variables
- naming
- hybrid_coupling
- magic_values
cross_links:
- rel: related_to
  target_object_id: PAT_avoid_returning_magic_values
- rel: related_to
  target_object_id: PAT_use_descriptive_names
- rel: related_to
  target_object_id: PAT_minimize_variable_span_and_live_time
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Give Each Variable Exactly One Purpose

## Pattern Rule
**IF** a variable would take on a second job — reused further down for an unrelated computation, or carrying a special meaning in some part of its value range
**THEN** give the second job a variable of its own, and name both for what they actually hold.
**ELSE** when the two uses really are the same concept at two moments, keep one variable and fix the name so it says which concept, rather than leaving a placeholder that invites a third use.

## Do
- Split reused temporaries. A `temp` holding the square root in a quadratic solution and then, a few lines later, holding a value mid-swap reads as though the two are connected; `discriminant` and `oldRoot` say plainly that they are not.
- Read an out-of-band value as a type error rather than a style problem. When `pageCount` is a count of pages except at −1, where it reports an error, the integer is moonlighting as a boolean — it is simply the wrong type for the second job.
- Inspect the value range for smuggled fields, not only for sentinels. A `customerId` above 500,000 that means "subtract 500,000 to get a delinquent account number" has packed two independent data items into one integer, and neither the name nor the type admits it.
- Delete a declared variable nothing references. That is the zero-purpose case, and unreferenced variables have been found to correlate with higher fault rates — so it reads as a defect signal rather than as tidiness.

## Don't
- Don't keep a double meaning because it is obvious to you. Whether a second reader can recover it from the declaration, the type, and the name is a property of the code, and in these cases the answer is no.
- Don't economize on storage this way. The clarity bought by a second variable is worth far more than the bytes, and nobody has ever begrudged anyone the extra one.
- Don't let a placeholder name license the reuse. `temp` and `x` attract a second job precisely because they promise nothing, so the vague name is usually the first move in this failure rather than a side effect of it.

## Checklist
- Does this variable hold the same kind of thing everywhere it appears?
- Is there a value it can take that means something other than what its name says?
- Could a reader learn the second meaning from the code alone, or only by asking you?
- Does the declared type fit every job the variable is doing?
- Is every declared variable actually referenced somewhere?

## Notes
The two failures here look different and are the same fault. One splits a variable across *time* — the same storage serving unrelated computations at different points in a routine. The other splits it across its *value range* — most values meaning one thing and a reserved band meaning another. Both take one name and one type and make them cover two jobs, and the name and type can only describe one. The established term for the second is hybrid coupling.

The diagnostic that makes this quick to apply is the type check. Ask what type each job would need if it had its own variable. When the answers differ — a count and a success flag, an identifier and an account category — the variable is carrying two jobs no matter how the code reads. That test is faster than arguing about whether the dual use is confusing, and it does not depend on how familiar you already are with the code.

`PAT_avoid_returning_magic_values` covers the neighbouring ground from the caller's side, deciding how a *function* should report that it has no real value to return. This card is wider on two axes and narrower on none. It reaches any variable rather than only return values, it covers second meanings that have nothing to do with absence — the delinquent-account band is a whole extra field, not a missing one — and it includes reuse over time, which has no equivalent in a return type at all. Where they overlap, on the in-band sentinel, they agree.
