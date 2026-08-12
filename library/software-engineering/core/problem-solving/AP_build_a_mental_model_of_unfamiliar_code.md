---
object_id: AP_build_a_mental_model_of_unfamiliar_code
object_type: ap
name: Build a Working Mental Model of Unfamiliar Code
library_path:
- software-engineering
- core
- problem-solving
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- problem_solving
- mental_model
- code_comprehension
- working_memory
cross_links:
- rel: related_to
  target_object_id: PAT_make_a_reasoning_model_determinate
- rel: related_to
  target_object_id: PAT_externalize_intermediate_state_when_tracing
- rel: related_to
  target_object_id: DRILL_annotate_a_dependency_graph_over_code
reference:
  source_id: programmers_brain
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
  publish_date: 2021
  media_type: PDF
  locator: u06, pp. 96, 99-100
  evidence_type: text
confidence: high
references: []
variants: []
---

# Build a Working Mental Model of Unfamiliar Code

## Objective
Turn a codebase you cannot hold in your head into an abstraction you can reason from directly, so that questions about the system are answered against the model rather than by repeatedly returning to the source.

## Steps / Flow
1. **Start from local models you already know how to draw.** Build the state tables and dependency graphs covered by the tracing and annotation work. They only cover a small part of the codebase, and that is fine — they serve twice over, first by lowering cognitive load so you have capacity left for a larger picture, and second by supplying its building blocks. A dependency graph that exposes a few strongly connected lines has already told you where the larger model's center is.
2. **List the elements, then map the relationships.** Write out the objects, classes, or pages in the codebase on a whiteboard or in a digital tool, then draw what connects them. Capture the constraints, not just the links: in an invoicing system, that a person can have several invoices but an invoice belongs to exactly one person is the kind of statement the model exists to hold.
3. **Interrogate the model and repair it against the code.** Answer questions using the model you just built, then verify each answer in the source. The generic set that usually works: what are the most important elements, and are they in the model? What are the relationships between them? What are the program's main goals? How do those goals relate to the core elements and their relationships? What is a typical use case, and does the model cover it?
4. **Tighten anything that admits more than one reading.** Where a question had several defensible answers under the current model, that is indeterminacy rather than ambiguity in the code — add the detail that rules out the rival reading before moving on.
5. **Stop when the model answers the question you came for.** The effort scales with how complex and unfamiliar the code is, and it is worth paying because the resulting model is an asset for every later question. It is not a mandate to model the whole system.

## Notes
Hermans presents steps 1 to 3 as the procedure for forming a mental model of complex code in working memory, following Johnson-Laird's position that models are constructed for reasoning rather than retrieved whole. The payoff she names is specific: an abstract model "allows you to reason about the model itself rather than relying on referring back to the code, which would be less efficient."

Step 4 exists because the same chapter supplies the reason — the determinate/indeterminate gap of 88% against 58% — and the repair is cheap at this point in the process.

The failure mode this plan is aimed at is documented a few pages earlier, in the characteristics of mental models: people are frugal with them, because the brain is expensive to run, and "when debugging, many programmers prefer to make small changes to their code (tweaks) and run it again to see if the bug is fixed rather than spending the energy to create a good mental model of the problem." Tweak-and-rerun is the default this plan is asking you to override, and recognizing the pull toward it is most of the discipline.
