---
object_id: PAT_treat_an_unreproducible_failure_as_a_defect
object_type: pattern
name: Treat a Failure You Cannot Reproduce as a Defect
library_path:
- software-engineering
- core
- concurrency
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- concurrency
- testing
- defects
- threading
- diagnosis
cross_links:
- rel: related_to
  target_object_id: PAT_run_threaded_code_under_conditions_built_to_break_it
- rel: related_to
  target_object_id: PAT_tests_fail_only_when_code_broken
- rel: related_to
  target_object_id: PAT_check_concurrent_code_for_safety_and_liveness
reference:
  source_title: 'Clean Code: A Handbook of Agile Software Craftsmanship'
  author: Robert C. Martin, with Brett L. Schuchert
confidence: high
references: []
variants: []
---

# Treat a Failure You Cannot Reproduce as a Defect

## Pattern Rule
**IF** something failed once in code that runs more than one thread, and it passed when you ran it again
**THEN** record it and hunt it as a real fault, because in threaded code the rerun passing is the expected behaviour of a genuine bug rather than evidence against one
**ELSE** where you can demonstrate a specific external cause — a machine that was rebooted, a network that was down, a disk that filled — attribute it to that and say which, rather than to chance.

## Do
- Start from the assumption that one-off failures do not exist. The label is applied to explain away an observation, and in this domain it is almost always wrong.
- Understand why the rerun passes, because that is what makes the instinct so misleading. Only a small number of the possible orderings through a vulnerable section actually produce the wrong answer, so the chance of hitting one on any given run can be tiny — and a passing rerun samples one more ordering out of thousands.
- Capture what you can while it is fresh: which configuration, which machine, what load, and what the failure actually was. A second sighting is worth far more when you can compare it against the first, and months can separate them.
- Count the cost of waiting. Every week the failure stays unattributed is a week of further work built on top of whatever is wrong, which is what converts a contained fault into an expensive one.
- Watch for the fix that suppresses rather than resolves. Adding logging or a delay and finding that the symptom disappears is not a diagnosis — the addition changed the timing, which is evidence you have a timing-dependent fault, not evidence it is gone.
- Treat an intermittent test as reporting on the code, not on itself, until you have shown otherwise. The reflex is to distrust the test; here the test is more often right than the person rerunning it.

## Don't
- Don't attribute a failure to hardware, cosmic rays, or bad luck without evidence for that specific cause. Those explanations are available for everything and therefore distinguish nothing.
- Don't let a green rerun close the question. It is the single weakest piece of evidence available in threaded code, and it is the one most commonly treated as decisive.
- Don't mute or retry the test to make the noise stop. That converts a fault that was announcing itself into one that no longer does, which is strictly worse than either fixing it or leaving it alone.
- Don't wait for a reliable reproduction before believing it. Reliable reproduction is the hard part and may take deliberate effort to construct; belief should not be waiting on it.

## Checklist
- Was the failure recorded anywhere, or only observed?
- What is the specific alternative explanation, and what evidence supports it?
- Do you know which orderings could produce this, or only that some could?
- Has this been seen before, and would you be able to tell?
- Did anything you added to investigate change the timing?
- Is the test being distrusted because it is wrong, or because it is inconvenient?

## Notes
The statistics are what make the instinct fail, and they are worth holding as numbers rather than as a caution. A single unremarkable-looking line of code can carry thousands of distinct execution orderings once two threads run through it, and adding a wider value or another thread pushes that into the millions. The overwhelming majority of those orderings produce the right answer. A fault therefore appears as a rare event by construction — not because it is marginal, but because the failing paths are a small share of an enormous space. Rerunning draws one more sample from that space, and drawing a passing one is the likeliest outcome even when the code is definitely broken.

That is why the ordinary debugging reflex inverts here. In single-threaded code, an intermittent failure genuinely does suggest something environmental, because the code takes the same path every time. Under threads the path is chosen by a scheduler you do not control and that behaves differently under load, on other hardware, and on other operating systems. Intermittency stops being a signal about the environment and becomes the ordinary signature of a concurrency fault, which reverses what the same observation should lead you to conclude.

The compounding cost is the practical argument for acting immediately rather than waiting for a second sighting. An unattributed failure does not sit still; work continues on top of the component that produced it, and each addition assumes the foundation is sound. By the time the fault appears often enough to be undeniable — typically under production load, which is when the orderings get exercised hardest — the amount of code resting on it has grown, and so has the cost of whatever the correct fix turns out to be.
