---
object_id: AP_review_code_you_did_not_write
object_type: ap
name: Review Code You Did Not Write
library_path:
- software-engineering
- core
- code-quality
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- code_quality
- review
- defects
- judgment
cross_links:
- rel: supports
  target_object_id: PAT_concentrate_effort_where_defects_concentrate
- rel: supports
  target_object_id: PAT_judge_change_risk_by_what_it_can_break
- rel: supports
  target_object_id: PAT_combine_detection_techniques_rather_than_perfecting_one
- rel: supports
  target_object_id: PAT_look_for_the_evidence_outside_the_code
- rel: related_to
  target_object_id: AP_build_a_mental_model_of_unfamiliar_code
- rel: related_to
  target_object_id: DRILL_run_a_cdcb_review_of_a_codebase
confidence: medium
references: []
variants: []
---

# Review Code You Did Not Write

## Objective
Given a body of code somebody else wrote, produce the list of what is wrong with it and a judgment on whether it is sound enough for its purpose. The result is a ranked set of findings, each naming the defect and what it can break, plus an explicit statement of what was examined and found acceptable. Not a rewrite, and not a comprehension exercise that stops once you understand the code. A second output comes out of the same reading and is easy to leave on the floor: the places where the guidance you reviewed against was absent, or present but stated more coarsely than the code shows the practice to be. Step 8 owns collecting it.

## Steps / Flow

**Entry state.** You have code, you did not write it, and you are being asked whether it is any good. You may or may not be able to change it. If you cannot yet say what the code is *for*, you are not ready to judge it — `AP_build_a_mental_model_of_unfamiliar_code` owns getting to that point, and reviewing without it produces opinions about style.

1. **Establish what the code claims before looking for what is wrong.** Write down what it owns, what it promises callers, and what it assumes of them. Ownership is the single most load-bearing fact: whether a type holds a resource decides whether an entire family of questions applies to it, and getting that wrong sends the whole review to the wrong place. Promises and assumptions matter for the same reason — a component that assumes clean input is reviewed against different rules than one that validates.

2. **Ask whether the thing should exist before reviewing how well it is built.** A hand-rolled version of something the standard library or an existing component already provides is one finding that outranks everything inside it. `AP_give_an_acquired_resource_an_owner` makes this its second step for the same reason. **Branch:** if the answer is that it should be replaced, stop reviewing the internals unless the code will be kept anyway — every defect you find inside is conditional on a decision that has already gone the other way, and reporting twenty of them buries the one that matters.

3. **Take each family the code touches and run the owning protocol's completion check backwards.** This is the move that makes the review tractable, and it is not obvious: the library's authoring protocols each end in a completion check stating what a finished piece of work must satisfy, and those checks are better review checklists than anything written as one, because they were built by someone deciding what "done" means. A class holding a resource gets `AP_write_copy_control_for_a_resource_owning_class`'s final step; a class with an interface gets `AP_make_a_class_const_correct`'s; a function that can fail gets `AP_make_a_function_exception_safe`'s. Read them as questions rather than as instructions.

4. **Separate a rule being silent from a rule not applying.** Most of the library will say nothing about any particular piece of code, and almost always that is because the situation it addresses is absent — a forty-line function does not exercise concurrency guidance. That silence is not a finding and recording it as one buries the real ones. Only where the situation is genuinely present and nothing addresses it do you have something, and you should be able to say what makes it present.

5. **Rank by what a defect can break, not by how easily you found it.** Surface faults are found first and are usually the cheapest; the finding worth leading with is the one whose failure is remote from its cause. `PAT_judge_change_risk_by_what_it_can_break` owns the scope question. A defect whose symptom appears in unrelated code, at an unrelated time, outranks a dozen naming problems however obvious those are.

6. **Surface a conflict rather than resolving it silently.** Where two rules give opposite readings of the same code, or where a rule appears to certify something you believe is wrong, that disagreement is itself a finding and belongs in the report. **Recovery:** do not quietly pick the answer you prefer. Either the code is fine and you have misread a rule, or a rule is stated in a way that endorses a defect — and both are worth more than a silent choice between them.

7. **Say what you examined and found acceptable, not only what failed.** A report listing six defects and nothing else cannot be distinguished from a review that stopped after six. Naming the families you checked and cleared is what tells a later reader which parts were looked at.

8. **Collect what the review taught about the guidance, not only about the code.** Reading code somebody else wrote is the cheapest evidence available about where the library is thin, and the reading has already happened by the time you reach this step — but it yields nothing unless it is asked for explicitly, because the review's attention is pointed at the code. Go back over what the reading showed — the techniques the code used well, and the defects you confirmed — and sort each into one of three outcomes. Each entry has to name either the object already covering it or the search that came back empty. Without that, the pass returns a list of things the reviewer happened to admire.

   *Gate.* Settle whether the code is right before classifying any of it. A defect mistaken for a practice will widen a card until it endorses the defect, which is worse than the gap the pass was opened to close. The question is answerable rather than a matter of taste: a technique held up as worth learning from should survive the same scrutiny the defect list received, and where a sibling elsewhere in the same codebase does the same job differently, that disagreement is evidence about which of the two is the mistake.

   What the gate forbids is calling a defect sound and then widening a card to accommodate it. It does not forbid a defect from producing an entry, and reading it that way closes the only route by which the library hears about the rules it does not have. A defect you have confirmed *is* a defect can still show that nothing in the library forbids it, and that is an unowned gap like any other. The difference is which way the resulting card would point: write the entry as the rule that is missing rather than as a technique worth copying, and it cannot widen anything toward the defect. A finding that appears in both lists is the pass working rather than a mistake — the code findings say this code is wrong, and the guidance findings say nothing here would have caught it.

   - *Owned.* A card already covers it. This will be most of what you collect, and it is recognition rather than discovery — expected, not a disappointment, and worth recording only as a count.
   - *Unowned.* The situation is genuinely present in the code, you can say what makes it present, and nothing in the library addresses it. This is a candidate for authoring and the reason the pass exists. The situation may be something the code did well or something it got wrong; what makes the entry admissible is that you can state what the missing rule would say, not which of the two prompted it.
   - *Owned but coarser than the practice.* A card points the right way and stops short of what the code actually does. This is the outcome that is easiest to miss, because the card reads as correct and the disagreement is one of resolution rather than direction.

   Expect the unowned share to move with how the slice was chosen. A slice aimed deliberately at regions the library covers thinly returns more of it; a slice chosen freely returns less, and the drop is information about coverage rather than about the reviewer.

**Completion check.** Every finding names the defect, the code it is in, and what it can break. The families examined are listed, including the ones that produced nothing. Anything reported as missing is something you can show is genuinely absent rather than merely unmentioned. If the code should be replaced wholesale, that finding is first and the rest are marked as conditional on keeping it. The guidance findings are reported separately from the code findings and each names either a covering object or an empty search, so a reader can tell a genuine gap from an unexamined enthusiasm. Every technique carried into those findings was checked for being correct before it was classified, so nothing there is a defect wearing the clothes of a practice — and where a defect did produce a guidance entry, that entry states the rule that is missing rather than holding the defect up as something to copy.

## Notes
The reason this needs a protocol rather than a list of things to look for is that the library's guidance is organised for the person writing code, and a reviewer arrives at it from the opposite direction. An author reaches for the rule covering the decision in front of them; a reviewer has to work out which decisions were made at all, most of them invisible because nothing in the code marks a road not taken. Step 1 exists to reconstruct that set of decisions, and steps 3 and 4 exist because the reviewer's failure mode is not missing a rule — it is checking rules that never applied and reporting their silence as approval.

The backwards use of completion checks in step 3 is worth stating plainly because nothing else points at it. Those checks already encode what a competent author would verify before calling the work finished, which is exactly the question a reviewer is asking, and they are ordered so that the dependent judgments come after the ones they rest on. Using them this way costs nothing to maintain — they improve whenever the authoring protocol does — and it avoids the alternative, which is a separately maintained review checklist that drifts from the rules it was derived from.

Step 8 is separated from the rest because it answers a different question and is lost by default. Everything before it asks what is wrong with this code; step 8 asks what this code shows about the rules being used to judge it, and the reviewer has no reason to ask that while looking for defects. Demanding a covering object or an empty search behind every entry is what keeps the pass honest, because it separates a gap that was looked for from one that was merely not noticed. The majority of what comes back will be canon already held, and that is the expected shape rather than evidence the pass is not worth running, because the minority that is not is material the library cannot obtain any other way: real code is the only place where a rule that is right in direction and too coarse in resolution becomes visible.

The gate in front of step 8 was originally written as though everything reaching the step were a technique the code used well, and that framing had a cost worth recording. A reviewer who confirms a defect, then notices that nothing in the library would have caught it, has found the most valuable thing the pass can return — a gap demonstrated by a failure rather than argued from an absence — and the gate as first written sent it to the code findings, where there is nowhere to record that no card covers it. Two runs hit this before it was fixed: one classified such a gap as unowned anyway and produced a card that is now in the library, the other stopped and reported the contradiction instead of resolving it. The distinction that resolves it is narrow and worth keeping in view: widening an existing card to accommodate a defect is the failure the gate exists to prevent, and authoring a new card that forbids the defect is close to its opposite.

Step 6 deserves its place because the failure it prevents is invisible. A reviewer who silently resolves a contradiction between two rules leaves no trace that there was one, and the next reviewer resolves it again, possibly the other way. Where the contradiction is real rather than a misreading, it is a defect in the guidance that only surfaces when someone applies it to code it was not written against — which is precisely what a review is.
