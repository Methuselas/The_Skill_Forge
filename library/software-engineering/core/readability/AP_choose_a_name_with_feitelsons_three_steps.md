---
object_id: AP_choose_a_name_with_feitelsons_three_steps
object_type: ap
name: Choose a Name in Three Steps — Concepts, Words, Mold
library_path:
- software-engineering
- core
- readability
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- naming
- readability
- conventions
- code_review
cross_links:
- rel: supports
  target_object_id: PAT_use_descriptive_names
- rel: supports
  target_object_id: PAT_agree_on_a_small_set_of_name_molds
- rel: supports
  target_object_id: PAT_design_a_name_for_both_stm_and_ltm
- rel: supports
  target_object_id: PAT_name_the_problem_not_the_computation
- rel: supports
  target_object_id: PAT_favor_readability_over_brevity
- rel: supports
  target_object_id: PAT_let_name_length_signal_scope
- rel: supports
  target_object_id: PAT_name_a_two_argument_predicate_by_role
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Choose a Name in Three Steps — Concepts, Words, Mold

## Objective
Produce an identifier name by making three separable decisions in sequence rather than one intuitive leap, so that each decision can be examined and discussed on its own.

## Steps / Flow
1. **Select the concepts to include.** This is domain-specific and Feitelson considers it the most important decision in naming. The governing question is the name's intent — what information the object holds and what it is used for. Two practical prompts: if you feel the need to write a comment explaining the name, the wording of that comment probably belongs *in* the name; and if a comment already sits next to a name in code you are reading, the same applies. `PAT_name_the_problem_not_the_computation` owns which concepts qualify, and `PAT_design_a_name_for_both_stm_and_ltm` owns who the name has to serve.
2. **Decide which qualifying information the reader cannot infer.** Include the dimension where it matters (a length being horizontal or vertical), the unit where it matters (a weight in kilos), and the safety status where it matters (a buffer holding user input, and therefore unsafe). Where data changes status, consider a new name rather than reusing the old one — once input is validated, storing it in a variable whose name says it is safe carries the transition. `PAT_let_name_length_signal_scope` owns how much qualification the scope earns. Where the thing being named takes two arguments of the same kind and answers differently when they are swapped, their roles are qualifying information the reader cannot infer either — `PAT_name_a_two_argument_predicate_by_role` owns that case.
3. **Choose the words for each concept.** Often one word is obviously right because the domain or the codebase already uses it. Where several contend, the risk is that readers cannot tell whether two synonyms mean the same thing or mark a nuanced difference. A project lexicon recording the important definitions, with synonyms registered against their chosen term, is what makes this decision repeatable across a team. `PAT_use_descriptive_names` and `PAT_favor_readability_over_brevity` own the word choice.
4. **Construct the name by picking a mold.** Align with the molds your codebase already uses, so readers can locate the important element and relate the name to its neighbours. The mold set is `PAT_agree_on_a_small_set_of_name_molds`.
5. **Check the mold reads naturally in the language the code is written in.** English says "the maximum number of points," not "the point maximum," which is why `max_points` beats `points_max`. A preposition often helps — `indexOf`, `elementAt`.
6. **Revisit the concepts if you started from the words.** The steps do not have to run in order, and Feitelson says so explicitly; you may think of words before concepts. What matters is that the concepts get considered at all, not that they get considered first.

## Notes
This is the one naming procedure with direct evidence that it works. After defining the model, Feitelson ran a second experiment with 100 new participants who were taught the model and then given the same naming tasks as his original subjects. Two external judges, blind to which name came from which study, compared pairs; names produced with the model were judged superior by a ratio of two to one.

The reason the decomposition helps is that it makes disagreement locatable. Two developers who dislike each other's names are usually differing at exactly one of the three steps — which concepts to include, which word to use for a concept, or how to assemble them — and saying which step turns an aesthetic argument into a specific one.

Step 1 is where this plan overlaps most with the existing descriptive-naming foundation, and the overlap is corroboration rather than duplication: Long's rule that a name should do the work a comment would otherwise do arrives here from a different direction, as Feitelson's prompt for deciding what a name must carry.
