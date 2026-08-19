---
object_id: PAT_trace_each_variable_from_definition_to_use
object_type: pattern
name: Trace Each Variable From Definition to Use
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
- data_flow
- defects
- variables
cross_links:
- rel: prerequisite_for
  target_object_id: AP_choose_test_cases_systematically
- rel: related_to
  target_object_id: PAT_count_a_routines_decision_points
- rel: related_to
  target_object_id: PAT_declare_and_initialize_at_first_use
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Trace Each Variable From Definition to Use

## Pattern Rule
**IF** you are looking for faults in a routine, whether by reading it or by choosing cases to run against it
**THEN** follow each variable through the three things that can happen to it — being given a value, being read, and ceasing to be valid — and treat certain sequences as defects on sight
**ELSE** where a variable is assigned once and read once in the following line, the trace is trivial and the effort belongs on the ones whose life spreads across the routine.

## Do
- Learn the sequences that are wrong before any test runs. A variable given a value twice before anything reads it; given a value and then discarded unread; given a value and then left as the routine exits; discarded twice; or read after it has been discarded. Each is suspect on inspection, and finding them by reading costs less than finding their consequences by testing.
- Cover the pairs, not just the lines. Running every line proves each assignment was reached; it does not prove each assignment reached each of the places that read it, and the difference is where this technique lives.
- Hunt the combinations that path-based cases miss. Where two conditions each select a value, the cases setting both the same way tend to fall out of ordinary path coverage for free, and the crossed combinations do not — those are the ones to add deliberately.
- Follow the variable across the branches rather than down the page. What matters is which assignment is live when a particular read happens, and that depends on the route taken, not on the order the lines appear in.
- Give the longest-lived variables the most attention. A value that is set early, survives several branches, and is read late has the most opportunities to be reassigned, invalidated, or read at the wrong moment.

## Don't
- Don't treat line coverage as covering this. Every line executing is compatible with an assignment never once reaching the read that matters.
- Don't ignore a suspect sequence because the routine currently works. An assignment nobody reads is either dead or a symptom that the wrong thing is being read somewhere, and both are worth resolving before they are built upon.
- Don't limit the trace to local variables. Fields, parameters passed by reference, and anything reachable through them go through the same three states and are harder to follow, which is why they are worth following.
- Don't stop at the first read. A variable read in three places has three pairs to account for, and the later ones are where a reassignment in between does its damage.

## Checklist
- For each variable: where is it given a value, where is it read, and where does it stop being valid?
- Is anything assigned twice before a read, or assigned and never read?
- Does every assignment reach every read it is supposed to reach?
- Which crossed combinations of conditions are untested?
- Which variable here lives longest, and has it been traced across the branches?

## Notes
This technique exists because coverage of the code and coverage of the data are different things, and satisfying one says remarkably little about the other. A routine can execute every one of its lines under a set of cases where a particular assignment is never the one live at a particular read — so the pairing that actually breaks in production has been executed zero times while the coverage report shows everything green. Following the data rather than the control flow is what closes that.

The suspect sequences are worth memorising because they are found by reading, before any test is written or run, and they turn a testing activity into an inspection one. A value assigned and never read is either dead code or a sign that some other value is being read where this one was intended. A value read after being invalidated is a defect already. Neither requires execution to spot, which makes this among the cheapest checks available on a routine you are about to spend real effort testing.

The crossed-combination point is the one that determines how many cases you end up adding. Where two conditions independently select values, ordinary path-based selection tends to produce the cases that set both conditions the same way, because those are the natural routes through the code. The combinations where the conditions disagree require deliberate construction, and since disagreement is exactly the circumstance nobody had in mind while writing, that is where the interesting faults concentrate.
