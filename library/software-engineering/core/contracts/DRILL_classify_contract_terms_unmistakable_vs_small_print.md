---
object_id: DRILL_classify_contract_terms_unmistakable_vs_small_print
object_type: drill
name: Classify a Contract's Terms as Unmistakable or Small Print
library_path:
- software-engineering
- core
- contracts
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- code_contracts
- api_design
- preconditions
- error_prevention
cross_links:
- rel: teaches
  target_object_id: PAT_define_your_code_contract_explicitly
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
target_skill: analyzing a piece of code's contract and spotting terms that rely on unreliable small print
references: []
variants: []
---

# Classify a Contract's Terms as Unmistakable or Small Print

## Practice Task
Take a class or function, write out its full contract, and label every term as unmistakable or small print — then flag the small print that hides a real obligation.

## Target Skill
Seeing the contract in existing code and judging which channel each term travels in.

## Setup
No special setup required.

## Instructions
1. Pick a class with some setup requirements — for example a settings loader that must be constructed, then loaded, then initialized before use.
2. Build the list of contract terms by using the class rather than by reading its declaration: the preconditions (setup order, valid inputs), the postconditions (return values, resulting state), and any invariants.
3. Label each term unmistakable (carried by a name, parameter type, return type, or checked exception) or small print (carried by a comment, external doc, or unchecked exception), naming specifically which parameter, which return type, or which comment carries it.
4. For each small-print term, write the consequence for a caller who never reads it, and mark which of those consequences are silent rather than crashes.
5. Flag separately any term whose channel carries two meanings at once — a return value overloaded to mean two things — from one that is merely undocumented, since the remedies differ.
6. For each term that could be promoted to an unmistakable channel, name the channel it would move to and what that move costs. For anything not promotable, say why.

## Success Check
- Every term is listed — preconditions, postconditions, invariants — and the list is built by using the class rather than by reading its declaration, since the declaration is where the unmistakable terms already live and the others are what is being hunted.
- Each term names its channel specifically: which parameter, which return type, which comment. A label that does not say where the term is carried cannot be checked.
- Each small-print term has a consequence written for a caller who never reads it, and at least one of those consequences is silent rather than a crash. The silent ones are what this exercise exists to surface.
- A term whose channel carries two meanings at once is flagged separately from one that is merely undocumented, because the remedies are different.
- Each promotable term names the channel it would move to and what that move costs, and anything not promotable says why. A list of candidates with no costs attached is a wish rather than a plan.

## Common Failures
- Listing only the obvious terms (names, types) and missing the buried ones (setup order, overloaded null).
- Labeling a term "unmistakable" when it is really only stated in a comment.

## Notes
This drills the analysis Long performs on the `UserSettings` class, where the comments hide a strict call order and an overloaded null return. The transferable habit is to make the whole contract visible and channel-labeled before deciding how to enforce it, which is the setup step for hardening the contract.
