---
object_id: PAT_run_threaded_code_under_conditions_built_to_break_it
object_type: pattern
name: Run Threaded Code Under Conditions Built to Break It
library_path:
- software-engineering
- core
- concurrency
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- concurrency
- testing
- threading
- test_design
- defects
cross_links:
- rel: related_to
  target_object_id: PAT_treat_an_unreproducible_failure_as_a_defect
- rel: related_to
  target_object_id: PAT_get_the_single_threaded_version_working_first
- rel: related_to
  target_object_id: PAT_design_for_testability
- rel: related_to
  target_object_id: PAT_combine_detection_techniques_rather_than_perfecting_one
reference:
  source_title: 'Clean Code: A Handbook of Agile Software Craftsmanship'
  author: Robert C. Martin, with Brett L. Schuchert
confidence: high
references: []
variants: []
---

# Run Threaded Code Under Conditions Built to Break It

## Pattern Rule
**IF** you are testing code that runs more than one thread over shared state
**THEN** build the ability to vary the conditions into the code itself — thread counts, timings, doubles, iteration counts — and then run it in the arrangements most likely to expose a fault, rather than in the one arrangement you happen to develop under
**ELSE** where the component genuinely holds no shared state and coordinates nothing, test it as ordinary code, because there is no ordering for varied conditions to vary.

## Do
- Make the coordinating code configurable from the outside before you try to test it. Thread count adjustable from one upward, collaborators replaceable by doubles, those doubles able to run fast or slow or erratically, and the whole thing able to repeat for a set number of iterations. None of that can be bolted on afterwards.
- Oversubscribe deliberately. Running more threads than there are processors forces the scheduler to swap between them constantly, and each swap is another chance to land in the window where a missing guard or a bad acquisition order shows itself.
- Run on every environment you will deploy to, early. Scheduling policy differs between operating systems, and code known to be broken can fail readily on one and almost never on another — so a clean run proves something about that platform and very little about the next.
- Vary the load as well as the shape. Faults that never appear when the system is idle appear under contention, because contention is what makes threads actually meet.
- Perturb the ordering on purpose. Inserting yields, sleeps, or priority changes at points inside a guarded section shifts which interleavings occur and can make a latent fault fail immediately. If that makes it break, the perturbation did not cause the fault — it revealed one.
- Route the perturbation through a single named hook rather than scattering calls. One function that does nothing in production and randomly chooses among yielding, sleeping, or falling through in test lets you run the same code a thousand times under different orderings without shipping any of it.
- Keep every failure the arrangement produces. The whole point of these conditions is to generate rare events, and discarding one because it did not recur wastes what the effort bought.

## Don't
- Don't test the coordination in the configuration you developed in and conclude it works. That configuration is one sample from a very large space and it is the sample selected for being convenient.
- Don't scatter timing calls through production code by hand. You will not know where to put them or which to use, they slow the shipped system, and they are a scattergun against a target you cannot see.
- Don't treat a run that passes a thousand times as proof. It is a thousand samples from a space with millions of orderings in it, which is worth having and is not a guarantee.
- Don't expect the ordinary suite to find these. Tests written to check behaviour exercise the paths that behaviour takes, and the failing orderings are not among them unless something forces the issue.

## Checklist
- Can the thread count be changed without editing the code?
- Can the collaborators be replaced with doubles that run at controllable speeds?
- Have you run with more threads than the machine has processors?
- Has this run on every platform it will be deployed to?
- Is there a single place where ordering perturbation is injected, and is it inert in production?
- What happened to the last failure this arrangement produced?

## Notes
The premise is that correctness here cannot be established by proof or by ordinary testing, so what remains is raising the probability of observing a fault until it becomes likely rather than remote. Every technique here is aimed at that one number. Oversubscription increases the frequency of switching; varied platforms sample different scheduling policies; load makes threads contend rather than pass one another; and deliberate perturbation reaches orderings that would otherwise occur rarely enough never to be seen. None of them proves anything, and together they move a fault from appearing once a month in production to appearing during a test run.

Perturbation deserves defending because it looks like sabotage the first time it is proposed. Adding a yield in the middle of a guarded section and watching the code break invites the conclusion that the yield broke it. It did not — it changed which of the existing orderings was taken, and one of them was already wrong. The code was broken before, silently, and would have stayed silent until the ordering came up on its own, most likely under production load and at an inconvenient hour. Making it fail sooner and more often is the entire objective.

Building the configurability into the design rather than adding it later is what makes any of this available, and it is the step most often skipped. Code where the thread count is fixed, the collaborators are constructed internally, and the timing cannot be influenced offers exactly one arrangement to test. Since the goal is to run many arrangements, the ability to vary them is not test scaffolding — it is a property the code has to be given while it is being written, which is why this is a design decision rather than a testing one.
