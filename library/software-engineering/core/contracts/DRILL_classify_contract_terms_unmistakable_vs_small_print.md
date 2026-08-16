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
2. List every term of its contract: the preconditions (setup order, valid inputs), the postconditions (return values, resulting state), and any invariants.
3. Label each term unmistakable (carried by a name, parameter type, return type, or checked exception) or small print (carried by a comment, external doc, or unchecked exception).
4. For each small-print term, ask what goes wrong if a caller never reads it — and flag any that would cause a silent bug, such as a return value overloaded to mean two things.
5. Note which small-print terms could be promoted to an unmistakable channel or removed by redesign.

## Success Check
- Every contract term is written down and labeled by channel.
- Each small-print term has a named consequence if it is ignored.
- At least one overloaded or hidden term is identified as a candidate to promote or eliminate.

## Common Failures
- Listing only the obvious terms (names, types) and missing the buried ones (setup order, overloaded null).
- Labeling a term "unmistakable" when it is really only stated in a comment.

## Notes
This drills the analysis Long performs on the `UserSettings` class, where the comments hide a strict call order and an overloaded null return. The transferable habit is to make the whole contract visible and channel-labeled before deciding how to enforce it, which is the setup step for hardening the contract.
