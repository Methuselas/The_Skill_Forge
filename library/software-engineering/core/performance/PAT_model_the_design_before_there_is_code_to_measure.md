---
object_id: PAT_model_the_design_before_there_is_code_to_measure
object_type: pattern
name: Model the Design Before There Is Code to Measure
library_path:
- software-engineering
- core
- performance
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- performance
- design
- measurement
- benchmarking
- estimation
cross_links:
- rel: related_to
  target_object_id: PAT_prototype_to_answer_one_specific_design_question
- rel: related_to
  target_object_id: PAT_estimate_a_concurrent_designs_ceiling_before_building_it
- rel: related_to
  target_object_id: PAT_reproduce_the_real_context_before_believing_a_microbenchmark
- rel: related_to
  target_object_id: PAT_choose_among_good_designs_by_what_they_foreclose
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Model the Design Before There Is Code to Measure

## Pattern Rule
**IF** a design decision turns on performance and the system does not exist yet
**THEN** build the smallest artefact that exhibits the property in question — a benchmark of the data shapes, or an existing program adapted to carry the new workload — and decide from that rather than from argument
**ELSE** where you have already built something similar, its measurements are the model, and they usually transfer better than anything you could construct.

## Do
- Model the property, not the program. If the question is how to organize a large body of data that will be traversed repeatedly, the model is that volume of data held two ways and traversed; nothing else about the future system has to exist for the answer to be useful.
- Adapt an existing program as a harness when one is available. A system that already moves data of roughly the right kind can be made to move the volumes you expect, with generated payloads if it has none — and then you can add the candidate technique to it and measure the difference on realistic machinery.
- Build performance prototypes differently from feature prototypes. A feature prototype demonstrates behaviour and may be sloppy anywhere; a performance prototype must be efficient in the parts being measured and may skip everything else — corner cases, error handling, most features, sometimes all of them, with a hard-coded condition standing in for what a real feature would trigger.
- Read a small difference as a tie, and treat that as a result. Two designs within about ten percent of each other in a model are indistinguishable given how approximate the model is — which is genuinely useful, because it frees the decision to be made on clarity, testability, or whatever else matters.
- Trust a large difference to survive. A several-fold gap in a model will not vanish once the code runs in context; what will not survive is the last few percent, and chasing that from anything but the finished program on real data is wasted.
- Expect the prototype's fast paths to become real code. The efficient low-level pieces written to make a performance prototype meaningful are often the foundation of the eventual libraries, which is part of what makes the exercise worth its cost.

## Don't
- Don't take a model's number as a prediction. Every model is approximate, and so is a complete implementation measured outside its final environment — code benchmarked for ideal memory access can end up sharing a saturated memory bus with threads that did not exist in the model.
- Don't dismiss models because they are approximate. The conclusion "these measurements are unreliable, so let us reason instead" replaces a noisy estimate with an unmeasured one, which is worse in every case.
- Don't model with unrepresentative data. Volume, shape, and the fraction of cases taking each path are usually what decide the answer, and a model that gets those wrong is precise about the wrong question.
- Don't let "we cannot measure a design" end the discussion. It is the reason this exists: you cannot run a design, and you can almost always run something that shares the property you are arguing about.

## Checklist
- What single property does this decision actually turn on?
- Is there an existing program or component whose measurements already answer it?
- Does the model use realistic data volumes and shapes?
- Is the gap large enough to act on, or inside the noise the model can resolve?
- Which parts of the prototype must be efficient for its numbers to mean anything?

## Notes
The objection this answers is a real one — there is no program to profile, so the first rule of performance work appears to have nothing to say at the design stage. The resolution is that the rule forbids guessing rather than requiring the finished system: what is needed is a measurement of the property under dispute, and properties can usually be exhibited by something far smaller than the program.

Accuracy scales with how much of the real thing the model contains, and it is worth being explicit about that ordering rather than treating all measurements as equal. Prior measurements of a component you actually built are best. An existing program adapted to the new workload comes next. A purpose-built micro-benchmark is the least faithful and the cheapest — which is why the complaint that micro-benchmarks lie is fair as a caution and useless as a conclusion.

There is a second payoff beyond the decision itself, and it is easy to overlook while arguing about which design wins. Building the model forces the properties that matter to be named — how much data, in what shape, accessed how often, by how many threads. Designs frequently founder because nobody stated those, and a team that has built the model has them written down whichever way the comparison goes.
