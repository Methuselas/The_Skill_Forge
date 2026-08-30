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
- Constructing an invalid instance from outside the class is attempted and fails to compile, with the rejection recorded. Privacy read off the declaration is not the same as having tried it.
- The factory signals setup failure through its return, and the run states what a caller ignoring that signal receives. If ignoring it still yields a usable-looking object, the small print has moved rather than gone.
- Every state-changing setup function is private, established by listing the public surface after the change and checking each member against whether it can produce a half-built state.
- Return values overloaded only to express an invalid state are removed, each named along with what now carries that information instead.
- The contract is re-read and whatever small print remains is stated. Something usually does, and a run reporting none has stopped looking rather than finished.

## Common Failures
- Adding the factory but leaving the constructor public, so the invalid path still exists.
- Leaving a setup function public "for flexibility," which reopens the invalid state.

## Notes
This is the `UserSettings` transformation as practice: from a class demanding `loadSettings()` then `init()` in order, to one where a private constructor and a `create()` factory make an invalid instance impossible. The point generalizes — whenever a contract leans on a setup sequence, look for a way to make the unset-up state unrepresentable rather than documented.
