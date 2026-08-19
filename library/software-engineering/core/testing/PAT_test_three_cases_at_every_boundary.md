---
object_id: PAT_test_three_cases_at_every_boundary
object_type: pattern
name: Test Just Below, Exactly On, and Just Above Every Boundary
library_path:
- software-engineering
- core
- testing
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- testing
- test_design
- boundary_analysis
- defects
- off_by_one
cross_links:
- rel: prerequisite_for
  target_object_id: AP_choose_test_cases_systematically
- rel: related_to
  target_object_id: PAT_work_the_input_classes_from_a_fixed_list
- rel: related_to
  target_object_id: PAT_bound_an_arithmetic_expression_before_trusting_it
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Test Just Below, Exactly On, and Just Above Every Boundary

## Pattern Rule
**IF** you are choosing inputs for something that has a limit, a threshold, a capacity, or a range
**THEN** write three cases at each one — the value immediately below, the value exactly on it, and the value immediately above — and then add the cases where two limits are reached together
**ELSE** where the quantity has no boundary at all, the interesting inputs come from the classes of good and bad data instead, and there is nothing here to place them against.

## Do
- Identify the boundary before choosing values. It is wherever behaviour is specified to change: a maximum length, a minimum count, a threshold that switches a decision, the first and last position in a collection.
- Take all three values every time. The one immediately on the boundary is the one other techniques never generate for you, because it sits on the line that path-based reasoning treats as already covered.
- Look for boundaries the specification does not mention. Empty and full, first and last, zero and one, and the largest value a type can hold are all boundaries whether or not anyone wrote them down.
- Add the cases where limits interact, which no single-variable analysis produces. Two large values multiplied together, two large negatives, everything simultaneously at zero, every string at its maximum length at once, or a large collection whose members are themselves large.
- Reach for these specifically after path-based cases. Those establish that each branch runs; they say nothing about which values were used to run it, and the boundary is exactly the value they stepped over.

## Don't
- Don't settle for the value near the boundary. A test at ninety-nine and a test at a hundred and one leave the case at a hundred untested, which is the one the off-by-one lives in.
- Don't assume the compound cases are covered because each variable was tested alone. Interactions between limits belong to no single variable, so nothing that walks the variables one at a time will produce them.
- Don't treat a boundary as tested because a branch there executed. Reaching the branch and reaching it with the critical value are different results.
- Don't skip the boundaries that seem absurd. Empty collections, zero-length strings, and single-element ranges are where a surprising share of real defects sit.

## Checklist
- What are the boundaries here, including the ones not written down?
- Does each have a case below, on, and above?
- Which pairs of values could reach their limits at the same time, and is that tested?
- Are empty, full, first, last, zero, and one all represented?
- Were these added after the path-based cases, or instead of them?

## Notes
The reason this earns its own place among test-selection techniques is that it produces cases nothing else does. Reasoning about paths generates inputs that reach each branch, and any value on the correct side of a comparison will do that — so the input chosen is whatever came to mind, which is almost never the value at the edge. The edge is precisely where a comparison written with the wrong operator behaves identically to the right one for every input except that one.

The exactly-on case is the load-bearing member of the three and the one most often dropped, usually because two tests either side feel like they bracket the problem. They do not. A condition using less-than where it should use less-than-or-equal passes every test below and every test above, and fails only at the value itself, which means bracketing a boundary tests everything except the defect the boundary was suspected of holding.

Compound cases deserve separate attention because they belong to no variable and therefore appear in no per-variable checklist. Each input can be individually within its limits while their combination overflows, exhausts memory, or takes long enough to time out. Nobody writes these down when enumerating the parameters one at a time, which is what makes the deliberate pass over interactions worth doing after the single-variable boundaries are covered.
