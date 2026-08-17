---
object_id: PAT_script_the_procedure_instead_of_writing_down_the_steps
object_type: pattern
name: Script the Procedure Instead of Writing Down the Steps
library_path:
- software-engineering
- core
- working-practice
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- automation
- reproducibility
- build
- tooling
cross_links:
- rel: related_to
  target_object_id: PAT_keep_the_build_green_with_an_automated_smoke_test
- rel: related_to
  target_object_id: PAT_give_knowledge_one_authoritative_home
reference:
  source_title: The Pragmatic Programmer
  author: Andrew Hunt & David Thomas
confidence: high
references: []
variants: []
---

# Script the Procedure Instead of Writing Down the Steps

## Pattern Rule
**IF** a procedure will be carried out more than once — standing up a development environment, producing a release, deploying, running a recurring chore
**THEN** encode it as a script kept under source control alongside the code it serves, rather than as a document telling a person which steps to follow, because people execute steps slightly differently every time and nothing in the process reveals that it happened.

## Do
- Name the actual failure mode, which is silent divergence rather than wasted effort. Hand a team several pages of click-here, scroll-there, double-click-that instructions for installing their tooling and every machine ends up loaded slightly differently; what you observe weeks later is a defect that reproduces for one developer and not another, and a small surprise every time anyone checks which version of a component is actually installed.
- Keep the script in version control with everything else. The procedure then has a history you can read, which is the only way to answer "but it used to work" with evidence instead of recollection.
- Define the build as starting from an empty directory and a known environment: check out, build from scratch with a version or date stamp, assemble the distributable exactly as it will ship — permissions, examples, documentation and all — then run the tests. A procedure that only succeeds from the working directory you already have is not reproducible, it is familiar.
- Schedule whatever must happen without anyone remembering it. A nightly build, a backup, a periodic report, and a regular full test run should all fire on their own; the point of a scheduler is that it removes a human from the reliability path.
- Derive the published views rather than maintaining them. Build results, test results, metrics, and extracted documentation should be generated from the repository and published without intervention — a status page updated by hand goes stale the first busy week, and misleading information is worse than none at all.
- Automate the administration around a procedure even where the procedure itself stays human. Finding what is ready for review, notifying the people involved, and recording the outcome can all run off a marker in the source and a script, whether or not the review is a meeting.

## Don't
- Don't treat a carefully written procedure as equivalent to an automated one. Precision was never the missing property — repeatability is, and a script has it for the same reason a person does not.
- Don't let a release build differ from the regular one without testing it again. Different optimization settings, debug flags, or a locked repository produce a different program, and the results from the build you did test do not carry across to it.
- Don't skip automating something because doing it by hand only takes a minute. The minute is not the cost; the cost is that it is a slightly different minute each time, and the differences accumulate somewhere nobody is looking.
- Don't leave the automation to whoever has spare time. On a team, someone has to be explicitly responsible for building the tooling, or the drudgery stays manual because it is always individually cheaper to just do it again.

## Checklist
- Could someone reproduce this on a clean machine from what is in source control alone?
- Does the build work starting from an empty directory?
- When this last broke, could you see what changed in the procedure itself?
- Is anything being published or updated by hand that could be derived?
- Is anything in this process relying on somebody remembering to run it?

## Notes
The argument is usually made as a labour-saving one and that is the weakest version of it. Automating a five-minute task that runs weekly may never repay the time spent automating it. What it buys instead is that the result stops depending on who ran it, what they remembered, and whether they were interrupted halfway — and that property is worth having even when the arithmetic on effort comes out flat.

The instructive part of the manual-installation story is how the failure presents itself. Nobody experiences it as a process problem. It arrives as a bug that will not reproduce, as two developers disagreeing about whether something works, as an afternoon lost to discovering that one machine has a different version of a library than the rest. Every one of those looks like a technical problem in the moment, and the common cause is only visible if you already suspect it. That is why the rule is stated as prohibition rather than preference: by the time the evidence is available it has already been misread several times.

Starting from an empty directory is the part most often quietly dropped, and it is the part that carries the guarantee. A build that runs in a directory containing yesterday's artifacts is testing a state that no fresh environment will ever be in, and the first person to discover the difference is whoever tries to build it somewhere new — usually under pressure, usually at the worst point in a release. The empty-directory rule is what converts a build from something that works here into something that works.
