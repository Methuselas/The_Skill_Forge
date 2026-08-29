---
object_id: PAT_order_branches_so_the_common_case_is_found_first
object_type: pattern
name: Order Branches So the Common Case Is Found First
library_path:
- software-engineering
- core
- control-flow
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- control_flow
- conditionals
- case_statements
- readability
cross_links:
- rel: related_to
  target_object_id: PAT_choose_the_control_construct_that_fits_the_data
- rel: related_to
  target_object_id: PAT_minimize_nesting_with_early_returns
- rel: related_to
  target_object_id: AP_shape_a_multi_way_decision
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Order Branches So the Common Case Is Found First

## Pattern Rule
**IF** you are arranging the alternatives in a conditional chain or a case statement and the order does not affect correctness
**THEN** put the cases a reader is most likely to be looking for at the top, which for most code means the most frequent ones.
**ELSE** where the alternatives are genuinely equal in importance and frequency, order them alphabetically or numerically so that any particular one can be found by position rather than by scanning.

## Do
- Pick the ordering rule deliberately from the small set that exists, and say which one you used when it is not obvious. Frequency puts the common paths where they are read first. One-normal-case-plus-exceptions puts the normal one first with a comment marking it. Equal alternatives go in alphabetical or numerical order.
- Weigh readability first and let efficiency follow. Testing the common categories before the rare ones means a reader looking for typical behaviour finds it immediately, and as a side effect the code performs fewer tests on the paths it takes most often — but the second benefit is small and should not be the reason.
- Check that the order matches reality rather than the order you thought of the cases in. A character classifier that tests punctuation before letters was almost certainly written in the order the categories occurred to its author, and letters are far more common than punctuation in anything it will classify.
- Keep the ordering rule consistent within one construct. A chain that starts by frequency and finishes alphabetically has no rule, and a reader who works out the first half will mispredict the second.

## Don't
- Don't reorder branches whose order affects behaviour. Overlapping tests in a chain are evaluated in sequence, so moving a broad test above a narrow one silently captures the narrow case — establish that the alternatives are mutually exclusive before treating the order as free.
- Don't bury the usual path underneath exception handling. Someone reading to find out what normally happens should not have to work through the unusual cases first, and that is exactly what the reflex ordering produces.
- Don't invest in ordering a three-case construct. The decision is worth making where there are many alternatives — a statement dispatching dozens of events in an event-driven program — and is noise on a handful.

## Checklist
- Which of these cases will a reader most often be looking for?
- Which of them actually happen most often, as opposed to which came to mind first?
- Are the alternatives mutually exclusive, so that reordering is safe?
- Is one ordering rule applied consistently through the whole construct?
- Is this construct long enough for the ordering to matter at all?

## Notes
The reason this needs stating is that the natural order of writing is not the natural order of reading. Cases get written in the order the author enumerated them — often working through a specification, or from the most interesting case to the most boring — and that order encodes the author's discovery process rather than the reader's search. The character classifier is a clean illustration: control characters, punctuation, digits, and letters in that order is a perfectly sensible way to have thought of the categories, and close to the reverse of how often they occur.

The efficiency argument is real but should stay in second place, and it is worth knowing why. In a chain, the tests before a match are all evaluated, so putting frequent cases first genuinely reduces work on the hot paths. But the saving is a handful of comparisons, a compiler may reorganize a case statement into a jump table where the ordering costs nothing at all, and reaching for this as a performance technique invites the mistake of ordering by measured frequency in code where nobody will ever notice. The reliable payoff is that a person looking for the normal behaviour finds it in the first few lines.

The measurements are worse for the efficiency argument than that caution suggests, which is the reason to keep readability as the stated justification. Benchmarking exactly this reordering on a character classifier — the case above — returned about 7 percent in one language, precisely zero in a second, and 18 percent *slower* in a third. The explanation is the jump-table point arriving from the other direction: where a language requires each case value to be enumerated individually rather than as a range, the compiled form does not resemble the chain of tests the reordering was reasoning about, so the analytic argument simply does not apply. An ordering chosen for readability is still right in all three languages; one chosen for speed was wrong in two of them.
