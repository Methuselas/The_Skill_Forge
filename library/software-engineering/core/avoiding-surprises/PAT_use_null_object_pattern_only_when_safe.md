---
object_id: PAT_use_null_object_pattern_only_when_safe
object_type: pattern
name: Use the Null Object Pattern Only When the Empty Value Can't Surprise
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
- null_object_pattern
- avoid_surprises
- api_design
- null_safety
cross_links:
- rel: related_to
  target_object_id: PAT_match_caller_mental_model
- rel: related_to
  target_object_id: PAT_dont_hide_errors
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u06, pp. 144-150
  evidence_type: text
confidence: high
references: []
variants: []
---

# Use the Null Object Pattern Only When the Empty Value Can't Surprise

## Pattern Rule
**IF** a value can be absent and you are considering returning an innocuous stand-in — an empty collection, empty string, or null-object instance — instead of null
**THEN** do it only when the absent case is genuinely indistinguishable from and as harmless as a real value to every caller; otherwise return null or an optional so absence stays explicit.

## Do
- Use it where the distinction does not matter: returning an empty set from `getClassNames()` lets `isElementHighlighted` skip a null check, and no caller cares whether the class attribute was unset or empty.
- Return an empty string only when the string is a bare collection of characters — free-form user comments are fine; a string that is an ID (`cardTransactionId`) must return null so callers see it can be absent.
- Prefer returning null for a missing object; it is the common, low-surprise paradigm callers already recognize.

## Don't
- Don't hand callers an "empty box": a `getRandomMug()` that returns a zero-size mug or a `NullCoffeeMug` for an empty inventory looks like a valid mug and silently poisons a report on mug sizes.
- Don't reach for a null-object implementation to spare callers a null check when its do-nothing methods and default values create the very surprise you are trying to avoid.

## Checklist
- Would any caller behave differently if they knew the value was absent rather than empty?
- Does the stand-in look like a valid value while secretly meaning "nothing was here"?
- Is null-safety already available, making an explicit nullable return the simpler, clearer option?

## Notes
Long frames the null object pattern as a double-edged tool: excellent for an empty collection where absence is immaterial, dangerous for a value whose absence carries meaning. The empty-phone-box analogy captures the failure — selling a sealed box with nothing inside is worse than saying "sold out." Because null safety and optionals now make absence easy to signal explicitly, the old reasons for null objects (avoiding null-pointer exceptions, sparing caller checks) have weakened, so reserve the pattern for the genuinely indistinguishable-and-harmless case. This is distinct from the chapter-4 rule against using it to hide an error.
