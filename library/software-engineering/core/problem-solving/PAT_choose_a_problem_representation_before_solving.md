---
object_id: PAT_choose_a_problem_representation_before_solving
object_type: pattern
name: Choose the Problem's Representation Before Solving It
library_path:
- software-engineering
- core
- problem-solving
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- problem_solving
- models
- representation
- cognition
cross_links:
- rel: related_to
  target_object_id: PAT_externalize_intermediate_state_when_tracing
- rel: prerequisite_for
  target_object_id: PAT_make_a_reasoning_model_determinate
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Choose the Problem's Representation Before Solving It

## Pattern Rule
**IF** a problem looks like it needs a complicated solution
**THEN** treat the representation as a decision in its own right and try a second one before committing effort, because the representation you pick changes how hard the problem is rather than merely how you describe it.

## Do
- Ask what the current representation forces you to track, and whether a different one would make the same answer fall out of a shorter calculation.
- Notice when the obvious framing follows the surface story rather than the quantity actually asked for; the bird-and-trains problem is hard when you model the bird's path and easy when you notice the trains meet in thirty minutes and multiply the bird's speed by the time.
- Exploit representations your tools make cheap — halving a number is a right shift once it is in binary — and say out loud which operation you are trying to make cheap.
- Treat a language's built-in representations as a real force on your design: APL makes a matrix solution natural, while Java makes nested loops the path of least resistance because a matrix class has to be built first.

## Don't
- Don't confuse "correct" with "worth doing." Modeling the bird's trajectory yields the right answer through a set of equations most people would rather avoid, and correctness is not what makes it the wrong choice.
- Don't accept the first framing simply because it arrived first and is already partly built.
- Don't assume a representation that is efficient for the machine is the one that is efficient for your reasoning; those are separate questions and this pattern is about the second.

## Checklist
- Can I state the problem a second way that a different reader would still recognize as the same problem?
- Which representation makes the quantity I actually need most directly readable?
- Am I reaching for nested loops because the problem is loop-shaped, or because my language made the alternative expensive to express?

## Notes
Hermans opens the chapter's problem-solving material with the claim that representation is not presentation: "there are numerous problems where the representation influences the solution strategy." The two worked cases sit at different scales. Dividing by two is trivial once the number is binary because the operation collapses to a bit shift, which is a representation chosen for the machine. The bird and the two trains is the reasoning-side case: both framings are correct, but one requires modeling a path of infinitely many turns while the other needs only the observation that the trains meet in the middle after half an hour, at which point the bird has flown 37.5 miles.

The language observation is the practical one for working programmers, and it cuts both ways — a language that limits representations "can be both helpful and harmful in solving problems." The constraint is a filter that is welcome when the problem fits it and a tax when it does not.
