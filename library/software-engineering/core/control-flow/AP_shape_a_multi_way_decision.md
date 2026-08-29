---
object_id: AP_shape_a_multi_way_decision
object_type: ap
name: Shape a Multi-Way Decision
library_path:
- software-engineering
- core
- control-flow
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- control_flow
- branching
- table_driven
- readability
- complexity
cross_links:
- rel: supports
  target_object_id: PAT_put_the_variation_in_data_rather_than_logic
- rel: supports
  target_object_id: PAT_choose_the_tables_access_scheme_by_the_key
- rel: supports
  target_object_id: PAT_choose_the_control_construct_that_fits_the_data
- rel: supports
  target_object_id: PAT_order_branches_so_the_common_case_is_found_first
- rel: supports
  target_object_id: PAT_decide_the_else_instead_of_omitting_it
- rel: supports
  target_object_id: PAT_write_boolean_expressions_to_be_read_not_decoded
- rel: supports
  target_object_id: PAT_count_a_routines_decision_points
- rel: related_to
  target_object_id: PAT_handle_enums_exhaustively
- rel: related_to
  target_object_id: AP_build_a_routine_from_intent_level_pseudocode
reference:
  source_title: PASS software-engineering canonical synthesis
  author: Multiple accepted sources
confidence: medium
references: []
variants: []
---

# Shape a Multi-Way Decision

## Objective
Given a decision with more than two outcomes, arrive at the construct that should carry it — a table, a multi-way branch, or a chain of tests — and at the order, the fallback and the conditions that go with it. Success is that the construct was chosen from the shape of the decision rather than from habit, that a reader can find any one branch without scanning all of them, and that what happens when nothing matches was decided rather than defaulted. Not a rule about avoiding long conditionals; a sequence for working out what the decision actually is before spelling it.

## Steps / Flow

**Entry state.** You are about to write, or are reading, a decision with several outcomes. The default move is a chain of tests, and it is the right answer often enough that reaching for it feels safe — which is why the shape of the decision goes unexamined.

1. **Say what varies across the branches, in one sentence, before writing any of them.** Two answers are possible and they lead to different places: the branches do *the same work with different values*, or they do *genuinely different work*. Everything below turns on which, and the sentence is cheap to write and hard to write dishonestly.

2. *Branch.* **If only values vary, the decision belongs in data rather than in control flow.** `PAT_put_the_variation_in_data_rather_than_logic` owns this, along with the point at which it earns its keep — a short chain of genuinely different work is clearer left alone, and a long chain selecting among variants of one operation is a table waiting to be written. This is the step most often skipped, because a chain can be extended one branch at a time and never presents a moment where the shape is reconsidered.

3. **Where a table is the answer, pick how an entry is found from the shape of the key.** `PAT_choose_the_tables_access_scheme_by_the_key` owns the three schemes and the rule that matters when none of them fits: transform the awkward key inside a routine of its own rather than reshaping the table around it. A table with a contorted key is worse than the chain it replaced.

4. **Where genuinely different work is being selected, choose the construct from the data, not from preference.** `PAT_choose_the_control_construct_that_fits_the_data` owns it: a multi-way branch wants a value that is honestly one of a small set of categories; anything else — ranges, relationships between variables, tests on more than one thing — wants a chain that says what it is testing. Forcing a categorical construct onto non-categorical data produces branches that lie about what they are.

5. *Gate.* **Where the value is an enumeration, decide now what happens when someone adds a case.** A multi-way branch over an enumeration either fails loudly on an unhandled value or silently does nothing, and that is settled here rather than discovered when the enumeration grows. `PAT_handle_enums_exhaustively` owns it.

6. **Order the branches so the one a reader wants is near the top.** `PAT_order_branches_so_the_common_case_is_found_first` owns the ordering, including what to do when the alternatives are genuinely equal — order them by something a reader can predict, so any particular branch can be found by position rather than by reading all of them. Do this only where order does not affect correctness; where it does, correctness has already fixed the order and there is nothing to choose.

7. *Gate.* **Decide what happens when nothing matches, and record that you decided.** `PAT_decide_the_else_instead_of_omitting_it` owns this. An absent final alternative reads identically whether it was reasoned about or forgotten, and the reader cannot tell which — so where the answer is genuinely that nothing should happen, that has to be said rather than left as a silence.

8. **Read each condition back as a sentence.** `PAT_write_boolean_expressions_to_be_read_not_decoded` owns the shaping. A condition a reader must decode — by applying precedence rules, removing negations, or working out which end of a range is which — costs every future reader the same effort, and the remedy is to name its parts rather than to keep rearranging it.

9. **Count what you have built, and treat the number as a question.** `PAT_count_a_routines_decision_points` owns the counting and, more importantly, owns the fact that a high count is a flag rather than a verdict. A long multi-way branch that is genuinely one flat decision is fine and scores badly; the count is asking you to state the reason, not to restructure on sight.

10. **Completion check.** What varies is written down in a sentence. A decision that only selects values lives in data, or there is a stated reason it does not. The construct matches the shape of the data being tested. Any enumeration has a decided answer for an unhandled value. Branch order is either fixed by correctness or chosen for a reader. The no-match case was decided and is visible as a decision. Every condition reads without decoding. And the decision-point count is either unremarkable or accompanied by the reason it is not.

## Notes
The reason this is a protocol rather than a preference is that the chain of tests is reachable by accretion. Nobody decides to write a forty-line conditional; they write three branches, and then someone adds a fourth, and at no point does the shape come up for review. Every step here except the first is available at any time, but only the first is naturally prompted by the work — which is why it is the step that gets skipped and the one the rest depends on.

Steps 2 and 4 are the fork and they answer different questions that look like one question. "Should this be a table" is about whether the branches differ only in values; "should this be a multi-way branch or a chain" is about whether the thing being tested is categorical. A decision can be a table whose entries are selected categorically, or a chain of genuinely different work over ranges, and conflating the two questions produces a table of function pointers where three plain branches would have read better.

The two gates are gates because both admit an answer that compiles, runs, and is silently wrong later. An unhandled enumeration value does nothing rather than failing, and does so for the first time when somebody unrelated extends the enumeration. A missing final alternative is indistinguishable from a considered one, so the cost is paid by the next reader rather than the author, and it is paid every time.
