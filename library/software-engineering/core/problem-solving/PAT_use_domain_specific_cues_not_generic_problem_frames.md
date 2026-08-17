---
object_id: PAT_use_domain_specific_cues_not_generic_problem_frames
object_type: pattern
name: Cue Yourself With the Domain, Not With a Generic Problem-Solving Frame
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
- retrieval
- transfer
- deliberate_practice
cross_links:
- rel: related_to
  target_object_id: PAT_choose_a_problem_representation_before_solving
- rel: related_to
  target_object_id: PAT_set_up_for_transfer_when_learning_a_new_language
- rel: related_to
  target_object_id: PAT_study_worked_examples_rather_than_only_solving
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Cue Yourself With the Domain, Not With a Generic Problem-Solving Frame

## Pattern Rule
**IF** you are stuck and reaching for a general method like "understand the problem, devise a plan, carry it out"
**THEN** replace the generic step with the most specific technical vocabulary the problem admits, because retrieval from long-term memory needs specific cues and a generic frame supplies none.

## Do
- Say the technique's name, not the step's name. "Devise a plan" gives long-term memory nothing to search on; "tail division" or "subtract multiples of the divisor" retrieves the method you already hold. The specificity of the clue is what determines whether the right memory is found.
- Name the three elements concretely instead of abstractly — the goal state you want, the start state you have, and the rules or constraints in force. In programming the rules usually arrive as constraints such as implementing in a given language or not breaking existing tests, and stating them is itself a retrieval cue.
- Say how the goal state will be checked, because "passing these tests" and "a satisfied user" are different goals that retrieve different approaches.
- Accept that the plan depends on the building blocks available. Checking a palindrome is `s == reverse(s)` where a reverse exists — Java's `StringBuilder` has one, APL has one under an operator name, BASIC has none — so "devise a plan" is not answerable independently of the language.

## Don't
- Don't expect a general problem-solving skill to exist to be trained. Research has consistently shown problem solving is neither a generic skill nor a cognitive process of its own, despite the durability of frameworks that assume it is.
- Don't expect transfer from the generic level back down. Transfer between distant domains is already unlikely; transfer from the very general domain of problem solving into a specific one is less likely still.
- Don't read this as a dismissal of Pólya. The three steps describe what solving looks like from outside; they just do not function as retrieval cues from inside.

## Checklist
- What is the most specific name I can give to what I am trying to do here?
- Have I stated the goal state, the start state, and the constraints in this problem's own terms?
- Am I searching my memory with a word that appears in the domain, or with a word that appears in a methodology?

## Notes
Pólya's *How to Solve It* (1945) proposes understanding the problem, devising a plan, and carrying out the plan. Hermans walks a palindrome check through all three across Java, APL and BASIC to show where it breaks: step 1 is fine for a programmer, step 2 depends entirely on whether the language offers a reverse, and step 3 depends on knowing how that facility is spelled — APL has one, but its keywords are operators, so knowing it exists does not tell you how to invoke it.

The retrieval argument is the deeper of the two and the one that generalises. Memories sit in a network and are reached through clues; the more specific the clue, the likelier the right memory surfaces. A generic frame is a maximally unspecific clue, which is why it can leave useful strategies you genuinely hold unretrieved.

The state-space framing sits underneath all of this — solving means traversing the space from start to goal in as few steps as possible, and for a small problem like tic-tac-toe the whole space can be drawn. For adding a button to a website the space is every JavaScript program there could be, which is precisely why the search has to be cued rather than enumerated.

This rule has since been tested against a source built on the opposite premise, and the conflict is recorded here rather than resolved by seniority. Spraul's *Think Like a Programmer* opens with eight general techniques — always have a plan, restate the problem, divide the problem, start with what you know, reduce the problem, look for analogies, experiment, don't get frustrated — presented as a portable method that applies to almost any situation. That is the framework this card says is not a retrieval cue, offered by an author who teaches it to students and reports it working.

The resolution is that the two disagree about only part of the list, and the line falls in a useful place. "Always have a plan" and "divide the problem" name what solving looks like from outside and supply nothing to search memory with, exactly as the retrieval argument predicts. But "reduce the problem" and "experiment" are not step names at all — they are operations with an input, a procedure, and a result, and running either one *produces* the specific cue this card asks for. Reducing a closest-pair problem to one dimension does not tell you to devise a plan; it hands you "find the two numbers with the smallest difference," which is a phrase long-term memory can be searched on. So the operational techniques survive the objection and the frame-shaped ones do not, and the distinguishing test is whether the technique yields a more specific problem statement than the one you started with.

What does not survive on either account is the premise that general problem-solving ability is a trainable skill in its own right. Both authors are describing something narrower and more defensible — a stock of concrete manoeuvres for converting a problem you cannot name into one you can — and that is worth having under its own name rather than under a claim the evidence does not support.
