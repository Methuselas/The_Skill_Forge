---
object_id: DRILL_refactor_small_print_class_to_impossible_to_misuse
object_type: drill
name: Refactor a Small-Print Class to Be Impossible to Misuse
library_path:
- software-engineering
- core
- contracts
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- hard_to_misuse
- factory_function
- immutability
- refactoring
cross_links:
- rel: teaches
  target_object_id: PAT_make_misuse_impossible_by_removing_invalid_states
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
target_skill: removing invalid states from a class so misuse cannot compile
references: []
variants: []
---

# Refactor a Small-Print Class to Be Impossible to Misuse

## Practice Task
Take a class that requires a setup sequence and redesign it so an invalid instance cannot be created, then confirm the small print is gone.

## Target Skill
Applying the static-factory, private-constructor, no-exposed-state technique to eliminate invalid states.

## Setup
No special setup required.

## Instructions
1. Start from a class that requires callers to construct it, then call setup functions in a specific order before use, with a comment warning them to do so.
2. Add a static factory function that performs the setup internally and returns only a fully valid instance, signaling setup failure through its return.
3. Make the constructor private so callers must go through the factory.
4. Make every state-changing setup function private so external code cannot reach a half-built state.
5. Remove any overloaded return meanings that only existed to signal an invalid state, and re-read the contract to confirm the small print is gone.

## Success Check
- No external code path can produce an instance that is not fully initialized.
- The constructor and all setup/mutator functions are private.
- No return value carries a second meaning that only existed because of a possible invalid state.

## Common Failures
- Adding the factory but leaving the constructor public, so the invalid path still exists.
- Leaving a setup function public "for flexibility," which reopens the invalid state.

## Notes
This is the `UserSettings` transformation as practice: from a class demanding `loadSettings()` then `init()` in order, to one where a private constructor and a `create()` factory make an invalid instance impossible. The point generalizes — whenever a contract leans on a setup sequence, look for a way to make the unset-up state unrepresentable rather than documented.
