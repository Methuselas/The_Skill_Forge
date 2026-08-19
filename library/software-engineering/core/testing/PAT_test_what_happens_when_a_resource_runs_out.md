---
object_id: PAT_test_what_happens_when_a_resource_runs_out
object_type: pattern
name: Test What Happens When Each Resource Runs Out
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
- resources
- failure_modes
- robustness
cross_links:
- rel: prerequisite_for
  target_object_id: AP_choose_test_cases_systematically
- rel: related_to
  target_object_id: PAT_work_the_input_classes_from_a_fixed_list
- rel: related_to
  target_object_id: PAT_set_the_robustness_level_deliberately
- rel: related_to
  target_object_id: PAT_match_failure_to_scope_of_recoverability
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Test What Happens When Each Resource Runs Out

## Pattern Rule
**IF** you are choosing test cases for something that will run inside finite resources
**THEN** test what it does when each one is exhausted, working past the two everybody remembers to the ones nobody does
**ELSE** where exhaustion cannot be recovered from at all, the case to test is whether the failure is graceful — state saved, work preserved, a comprehensible message — rather than whether it is avoided.

## Do
- Start with the two that get checked, then keep going. Memory and disk space are the ones everyone thinks of; the ones that go untested are processor time, disk and network bandwidth, wall-clock time, screen resolution, and colour depth.
- Ask what the environment can deny you that is not an input. This whole class is invisible to any technique that works from the parameter list, because none of it arrives through the parameters.
- Test the time dimension explicitly, not just the space one. Whether a batch job finishes before the window it must finish in is a resource question, and it fails in production long before it fails in development where the data is small.
- Test both ends of the presentation resources where they apply. An interface has to survive the smallest display it will meet and the largest, and both are boundaries nobody writes down.
- Separate what can be adapted to from what cannot. Some exhaustion is detectable and recoverable, some can be degraded around, and some ends the operation — and the right test is different for each.
- For the unrecoverable cases, make the observable behaviour the assertion. Whether work in progress survives, whether the failure is explicable, and whether the user is left able to act are the things worth checking, since preventing the exhaustion is not on offer.

## Don't
- Don't assume the ample development machine represents the deployment. Development environments are generously resourced and lightly loaded, which is precisely the configuration that hides this entire class.
- Don't test only for the resource running out completely. Running low often produces different and worse behaviour than running out, because the degraded path is the one nobody wrote carefully.
- Don't leave time out of the inventory because it does not feel like a resource. It is the one most likely to be exceeded first and the one least likely to appear in any checklist.
- Don't accept a crash as an acceptable answer without deciding that deliberately. Crashing may be right, and it should be a chosen robustness position rather than what happens by default.

## Checklist
- Which resources does this consume, beyond memory and disk?
- What happens at exhaustion for each, and has that been run rather than reasoned about?
- Does the work complete inside the time window it has to complete in?
- Does the interface survive both the smallest and largest presentation it will meet?
- For anything unrecoverable — is the failure graceful, and is that asserted anywhere?

## Notes
This class of case is missed systematically rather than occasionally, and the reason is structural. Every other selection technique works from what the code is given — the parameters, their ranges, their combinations — and resources are not given to the code, they are the conditions it runs inside. Nothing about examining a signature suggests asking what happens when the disk fills, so the question is only reached by someone deliberately looking for it, which is why a fixed inventory is worth carrying.

The development environment actively conceals the whole category. Machines used for building software have generous memory, fast local disks, ample bandwidth, and one user; deployment frequently has none of those. The result is that the code behaves impeccably everywhere it is observed during construction and encounters the constrained case for the first time in front of a user, under load, when the failure is most expensive and least understood.

Time deserves being pulled out of the list because it is both the likeliest to be exceeded and the least likely to be tested. Space limits announce themselves with clear errors; a job that takes longer than its window produces no error at all, just a result that arrives after something else needed it. That failure is invisible to any test that checks correctness alone, and it is discovered by asking what has to be true about *when* the work finishes, which nothing in the code will prompt you to ask.
