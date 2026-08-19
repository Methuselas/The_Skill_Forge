---
object_id: AP_choose_test_cases_systematically
object_type: ap
name: Choose Test Cases Systematically
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
- test_design
- coverage
- boundary_analysis
- defect_detection
cross_links:
- rel: related_to
  target_object_id: PAT_count_a_routines_decision_points
- rel: related_to
  target_object_id: PAT_trace_each_variable_from_definition_to_use
- rel: related_to
  target_object_id: PAT_test_three_cases_at_every_boundary
- rel: related_to
  target_object_id: PAT_work_the_input_classes_from_a_fixed_list
- rel: related_to
  target_object_id: PAT_test_what_happens_when_a_resource_runs_out
- rel: related_to
  target_object_id: PAT_read_coverage_as_a_floor_not_a_score
- rel: related_to
  target_object_id: PAT_concentrate_effort_where_defects_concentrate
- rel: related_to
  target_object_id: PAT_combine_detection_techniques_rather_than_perfecting_one
- rel: related_to
  target_object_id: AP_write_a_unit_test_suite
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Choose Test Cases Systematically

## Objective

Assemble the set of cases for a routine by running the selection techniques in an order where each one is defined by what the previous ones cannot produce — rather than writing cases until you feel finished, which reliably stops at about half the code while feeling like ninety-five percent of it.

Exhaustive testing was never available. A trivial routine taking a twenty-character name, a twenty-character address, and a ten-digit phone number has around ten-to-the-sixty-six possible inputs, so the whole craft is choosing the few cases that tell you different things. Each technique below owns its own decision and is documented in its own place; what this procedure owns is the sequence, the point at which each becomes worth running, and the condition that ends it.

## Steps / Flow

1. **Write cases from the requirements and the design, before the code exists.** One per relevant requirement and per relevant design concern. Earlier detection is the obvious return; the better one is that a poor requirement is hard to write a test against at all, so the attempt exposes it while it is still cheap to change.

2. **Compute the floor from the decision points.** The same count that flags a routine as too complex sets the minimum number of cases it needs, and each of those keywords needs one case making it true and one making it false. Read the result as a lower bound and nothing more: the number says how many are needed and nothing about which, and any six arbitrary cases will not cover a routine that needs six.

   *Gate.* A routine scoring above ten is simultaneously telling you to break it up and telling you that testing it properly starts at eleven cases. Consider simplifying before continuing, because everything after this step gets cheaper if you do.

3. **Inspect the variables before running anything.** Follow each from definition through use, and treat the suspect sequences as findings. This is the only pass that costs nothing to execute, so it comes before the passes that do.

4. **Add the definition-to-use pairs the path cases missed.** Exercising every line guarantees each assignment was reached, not that each reached every use, and the crossed combinations of conditions are the ones that do not fall out for free.

5. **Add the boundary cases, then the compound ones.** Below, on, and above each limit; then the cases where two limits are reached together, which belong to no single variable and so appear in no per-variable pass.

6. **Work the input classes from the fixed list.** Both halves — the malformed classes and the well-formed ones. Much will already be covered by now, and the value is that the list does not vary with what you happen to think of at this point.

7. **Add cases from this codebase's own defect history.** Guessing where faults are is respectable when the guesses come from a record of what actually breaks here, which is the same record a review checklist is built from.

8. **Test what the environment can deny.** Resource exhaustion arrives through no parameter, so nothing in the preceding steps will have suggested it.

9. **Branch where the space is too large to enumerate.** Generate inputs instead, weighting the distribution toward realistic sizes rather than spreading evenly across everything legal, and pick values whose expected results you can compute without redoing the work under test.

10. **Measure what was reached, and stop on evidence rather than on feel.** Aim past statement coverage at branch coverage. The report's reliable output is the list of code no case reached; treat that list as the completion condition, and treat the percentage as carrying no information about how well anything was tested.

   *Completion.* The set is finished when nothing is unreached and every pass above has been run — not when the figure looks respectable. A high percentage obtained without steps 3 through 8 is a thorough pass over a routine that has not been tested.

## Notes

The order is the whole contribution, because each technique is defined by the gap the previous ones leave. Path-based selection guarantees every line runs and says nothing about the data used to run it. Following the data covers the definition-to-use routes that line coverage misses. Boundary analysis covers the specific values both of those step over. The input classes cover the shapes of input that no path reasoning suggests. Resource exhaustion covers what never arrives as input at all. Running them in this sequence makes each pass short, because most of what it would generate is already present — run in another order, the same techniques produce heavy duplication and it becomes tempting to stop early.

The most useful number in this area is about what gets tested rather than how. Immature groups write roughly five clean cases — does it work — for every dirty one that tries to break the code; mature groups run five dirty for every clean. The reversal is not achieved by writing fewer clean tests. It comes from producing something like twenty-five times as many of the other kind, which is what steps 3 through 8 exist to generate, and it is why working through them feels unnatural compared with confirming that the code does what it was written to do.

The final step is where the procedure is most often misread, because it produces the only figure in the process. Coverage answers whether a line or branch was ever reached; what you want to know is which of the program's states have been visited, and those diverge fast — a few integer parameters puts the state count into the millions while the line count stays in single figures, and the states that break are usually a specific combination rather than a specific path. That is why the measurement sits at the end rather than the middle. It is there to catch code the earlier passes never reached, not to certify the code they did.
