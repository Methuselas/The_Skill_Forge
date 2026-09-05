---
object_id: PAT_avoid_returning_magic_values
object_type: pattern
name: Avoid Returning Magic Values
library_path:
- software-engineering
- core
- avoiding-surprises
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- magic_values
- avoid_surprises
- null_safety
- api_design
cross_links:
- rel: related_to
  target_object_id: PAT_match_caller_mental_model
- rel: related_to
  target_object_id: PAT_dont_hide_errors
- rel: related_to
  target_object_id: PAT_prefer_null_safety_or_optionals
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Avoid Returning Magic Values

## Pattern Rule
**IF** a function may be unable to produce a real value — the input is empty, a field is absent, the result is uncalculable
**THEN** signal that explicitly with a nullable or optional return, or an error, rather than returning a magic value that fits the normal return type but carries a special meaning.

## Do
- Make absence part of the unmistakable contract: change a `getAge()` that returns `-1` for a missing age into one that returns `Int?`, so callers get a compiler error until they handle the null.
- Watch for magic values that arise accidentally, not just deliberately: a `minValue()` that seeds with `Int.MAX_VALUE` silently returns it for an empty list, which crowns an unplayed game level "easiest" in a maximin.
- Accept the small caller burden of a null check as far cheaper than the bug it prevents, and use an error-signaling technique instead when the caller needs to know why the value is absent.

## Don't
- Don't hide absence inside a non-nullable return type; a caller summing `getAge()` values produces a plausible-but-wrong mean because `-1`s slip into the total.
- Don't assume a magic value like `Int.MAX_VALUE` is a safe default — it is language-specific, corrupts databases and cross-language clients, and breaks any comparison that treats it as a real result.

## Checklist
- Can this function fail to produce a real value, and does the return type say so?
- Could any returned sentinel be mistaken for a legitimate normal result?
- Does an empty or edge-case input silently yield an in-band special value?

## Notes
This is the avoid-surprises home for magic values, deferred here from the error-handling material. The `getMeanAge` bug is the anchor: a `-1`-for-absent age documented only in small print produces a wrong statistic that unit tests miss, because the caller never knew to test the absent case. A nullable return forces the caller to confront absence at compile time, at the cost of a handled null — a trade that is almost always worth it, escalating to an error type when the reason for absence matters.
