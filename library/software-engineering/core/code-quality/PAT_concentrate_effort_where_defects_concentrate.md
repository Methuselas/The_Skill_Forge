---
object_id: PAT_concentrate_effort_where_defects_concentrate
object_type: pattern
name: Concentrate Effort Where Defects Concentrate
library_path:
- software-engineering
- core
- code-quality
stage_binding: 4 final
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- defects
- maintenance
- rework
- quality
cross_links:
- rel: related_to
  target_object_id: PAT_count_a_routines_decision_points
- rel: related_to
  target_object_id: PAT_treat_bad_names_as_a_defect_search_heuristic
- rel: related_to
  target_object_id: PAT_combine_detection_techniques_rather_than_perfecting_one
- rel: related_to
  target_object_id: PAT_look_for_the_evidence_outside_the_code
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants:
- variant_id: change_frequency_signal
  variant_name: Rank by How Often a File Changes
  variant_basis: method_sequence
  difference_from_foundation: Ranks candidates by commit frequency drawn from version history rather than by defect reports or complexity scores, and optimises for the reading cost paid by the people who keep returning to a file rather than for the defect count that file produces.
  when_to_use: Where version history is long enough to be representative and defect records are absent, unreliable, or not attributable to particular files — which is the common situation on an inherited codebase.
  when_not_to_use: Where the codebase is young enough that the history is short, or where commit granularity varies so widely between contributors that the counts measure habits rather than churn.
  absorbed_from_object_id: none
---

# Concentrate Effort Where Defects Concentrate

## Pattern Rule
**IF** you are deciding where to spend quality effort — review, testing, or maintenance time — across a body of code
**THEN** find the small number of routines that hold most of the defects and treat those, rather than spreading the effort evenly on the assumption that defects are evenly distributed.
**ELSE** where you have no defect history yet, use complexity and comprehension signals as the stand-in, since they identify the same population before the defect reports arrive.

## Do
- Start from the actual distribution rather than the intuitive one. Roughly eighty percent of errors are found in about twenty percent of a project's classes or routines, and about half of the errors sit in five percent of them. A class with a hundred lines does not carry a hundred lines' worth of the defect budget.
- Rewrite the worst offenders instead of repairing them. Error-prone routines have been measured carrying as many as fifty defects per thousand lines, and fixing them has cost more than developing the entire system they belonged to once support and field maintenance were counted. At that ratio, patching is the expensive option.
- Point maintenance at identification rather than at the incoming queue. The productive maintenance activity is finding the error-prone routines and redesigning them from the ground up, which is different from working whatever defect arrived most recently.
- Use complexity as the proxy before you have defect data. A routine's decision-point count and the ordinary comprehension signals — names that mislead, structure nobody can hold — identify likely members of the expensive twenty percent without waiting for the field reports.
- Count the distinct contributors to a file as a third signal. Code carrying many authors who each touched it only lightly runs a higher defect risk than code with a settled owner, which is what you would expect from coordination cost meeting unfamiliarity.
- Expect the payoff to show up in schedule as well as defects. Since roughly twenty percent of routines also contribute about eighty percent of development cost, removing the worst of them shortens the work rather than adding to it.

## Don't
- Don't assume the defect density you measured across a codebase applies to any particular part of it. The average is real and almost nowhere is average, which is what makes evenly-spread effort the wrong allocation.
- Don't spend the effort proving the exact proportion. Whether it is eighty-twenty or seventy-thirty changes nothing about the action, and the studies disagree in the second digit while agreeing completely on the shape.
- Don't keep repairing a routine that keeps producing defects. Its history is the evidence, and a routine that has been buggy repeatedly will go on being buggy — that is the finding, not an impression.
- Don't confuse this with blaming the code you happen to dislike. The population is identified by defect history or by measurable complexity, not by which module is unfashionable.

## Checklist
- Which routines have produced the most defect reports in this codebase?
- Do you have that information at all, and if not, what would it cost to start collecting it?
- For the worst few — is the plan to repair them again, or to replace them?
- Where there is no history yet, which routines score worst on complexity?
- Is quality effort currently allocated by where the code is, or by where the defects are?

## Notes
The intuition this corrects is specific and nearly universal. Given a defect rate per thousand lines, people extrapolate linearly and expect a two-hundred-line class to carry twice the defects of a hundred-line one. The measured distribution is nothing like that — it is heavily concentrated, repeatedly, across studies spanning decades and organizations. Once that is believed, evenly-distributed review and testing effort stops looking fair and starts looking like spending most of the budget where the defects are not.

The economic argument for replacing rather than repairing is stronger than it first appears, because the costs being compared are not the ones usually counted. A routine that has cost more than the whole system to maintain did not do that in development time; it did it in customer support, field maintenance, and repeated repair over years. Measured only by the effort of the next fix, patching always wins. Measured across the routine's life, the rewrite is generally cheaper, and the decision looks different depending on which figure the person deciding can see.

The absorbed variant `change_frequency_signal` finds the same population from a third direction, and it is the one to reach for on a codebase you inherited. Instead of asking which files break or which score badly, it asks which files people keep opening — extracted by counting commits per file across the whole history. The distribution turns out to be as lopsided as the defect one, with a small set of files absorbing most of the changes, and the argument for treating those first is different from the argument this card is built on: they need to be cheap to read because they are read constantly, whether or not they are the ones producing faults. It generalises the same way, too — pairing change counts with a size measure over time exposes where complexity is actively growing, which is the population worth reaching before it qualifies under any of the other signals. Use it where the history is long and the defect record is thin, and distrust it where contributors commit at wildly different granularities, since then the counts describe working habits rather than churn.

The complexity proxy matters because defect history is a lagging indicator and most teams do not have it. A decision-point count is available on the first day, correlates with the population you are trying to find, and can be run over a whole codebase in minutes. It is not as good as knowing which routines have actually broken, but it is available before any of them have, which is when the choice about where to spend review effort is actually being made.
