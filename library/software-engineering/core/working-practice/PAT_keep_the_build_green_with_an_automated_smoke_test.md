---
object_id: PAT_keep_the_build_green_with_an_automated_smoke_test
object_type: pattern
name: Keep a Known-Good Build Behind an Automated Smoke Test
library_path:
- software-engineering
- core
- working-practice
stage_binding: 1 skeleton
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- integration
- build
- testing
- discipline
cross_links:
- rel: related_to
  target_object_id: PAT_choose_the_integration_order_by_risk
- rel: related_to
  target_object_id: AP_grow_a_system_from_a_running_skeleton
- rel: related_to
  target_object_id: PAT_make_breakage_fail_compile_or_test
- rel: related_to
  target_object_id: PAT_keep_unit_tests_fast_to_run
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Keep a Known-Good Build Behind an Automated Smoke Test

## Pattern Rule
**IF** a system is being built by more than one person, or over more than a few days
**THEN** build the whole thing and run an automated end-to-end smoke test on a fixed rhythm — daily at the outside — and treat a broken build as the highest-priority work until it is green again
**ELSE** where a build genuinely takes longer than the rhythm allows, shorten the build rather than lengthening the interval, because the interval is what the guarantee rests on.

## Do
- Bring the system to a known good state and then keep it there, rather than letting it drift and recovering later. That is the whole mechanism: the daily rhythm is what stops quality problems from accumulating to the point where fixing them becomes a project of its own.
- Make the smoke test the part that carries the value. It must exercise the system end to end; it does not have to be exhaustive, but it has to be capable of exposing major problems. Without it a daily build proves only that the code still compiles, which is a time-consuming way to learn very little.
- Grow the smoke test as the system grows. It may start by checking that the thing prints "Hello, World" and end up taking an hour. A smoke test that stops growing turns the whole practice into self-deception, in which a shrinking fraction of the system generates confidence about all of it.
- Define what "broken" means, strictly enough to keep showstoppers out and loosely enough that trivia cannot paralyse progress. The floor is that everything compiles, everything links, and nothing prevents the program from being launched or makes it hazardous to run.
- Automate the build and the smoke test. Doing either by hand does not survive contact with a busy week, and the practice only pays while it is happening without anyone deciding to do it.
- Integrate your own work every day or two, and smoke test it privately before it lands. Going longer puts your work at risk specifically: everyone else keeps getting the benefit of incremental integration and you stop.
- Keep building and smoke testing under schedule pressure, and understand that this is when it pays most. Discipline erodes under stress, review and self-testing get shorter, and the code tends toward entropy faster — the build is what brings that tendency to heel daily.

## Don't
- Don't conclude that frequent integration is slowing the team down. It surfaces work that would otherwise accumulate invisibly into an end-of-project tar pit; what feels like a slowdown is the first accurate picture of the pace the team was always working at.
- Don't let a broken build become ordinary. If it breaks often, the commitment not to break it stops meaning anything, and the known-good state that everything else depends on no longer exists.
- Don't read "continuous" literally. Continuous integration in practice means at least daily, and on medium and large systems there is real value in letting code get out of sync for short periods — people diverge to make larger changes and resynchronise afterwards. Frequent rendezvous points are the requirement; permanent synchrony is not.
- Don't drop the build because the system got big. The largest projects gain the most from it, and a build measured in many hours across several machines is still worth running every day.

## Checklist
- Is there a build today, and did a smoke test run against it?
- Has the smoke test grown since the last time you looked at it?
- What exactly counts as breaking the build here, and does everyone agree?
- When did you last integrate your own work?
- Is the build still running now that the schedule is tight?

## Notes
The daily build and the smoke test are frequently discussed as one practice, and separating them is what makes the practice legible. The build establishes that the parts still combine. The smoke test establishes that the combination still does something. Only the second one guards against the failure mode this exists to prevent, which is a system that assembles cleanly and does not work — so a project that automates the build and neglects the test has bought the expensive half and skipped the half that pays.

The diagnostic property is worth stating plainly because it is the day-to-day return. If the product worked on day 17 and is broken on day 18, whatever broke it happened between those two builds. That is a search through one day of changes rather than through the whole history, and it is available only because there was a known good state to compare against.

There is a genuine tension between integrating often and finishing a coherent piece of work, and it resolves in favour of integrating. Frequent integration sometimes forces a single feature to be built in several episodes, each one small enough to land safely, which is more overhead than building it in one go. That overhead is the price of reduced integration risk, better status visibility, and testability — and it is worth paying, because the alternative concentrates all the unknown work at the end where there is no room for it.

A note on what does not transfer from the era this was written in. The specific machinery — a build group of several people, a manual holding area, a check-in area on a file server, lollipops or beepers for whoever broke the build — was a response to tooling that no longer looks like this. What survives is the shape: a rhythm nobody has to remember, an automated end-to-end check that grows with the system, a shared definition of broken, and a norm that fixing it outranks whatever else you were doing.
