---
object_id: DRILL_choose_copying_behavior_for_an_raii_class
object_type: drill
name: Choose and Implement an RAII Class's Copying Behavior
target_skill: Selecting and implementing copy semantics for a resource-managing class
library_path:
- software-engineering
- languages
- cpp
- resource-management
stage_binding: 3 rough
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- raii
- copy_control
- resource_management
cross_links:
- rel: related_to
  target_object_id: PAT_choose_raii_copying_behavior_deliberately
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u03, pp. 66-69
  evidence_type: text
confidence: high
references: []
variants: []
---

# Choose and Implement an RAII Class's Copying Behavior

## Practice Task
Given a `Lock` class that locks a mutex in its constructor and unlocks it in its destructor, decide what copying should mean and implement it.

## Target Skill
Picking among prohibit, reference-count, deep-copy, and transfer, then implementing the choice correctly.

## Setup
No special setup required.

## Instructions
- List the four copying options and argue which fits a mutex lock.
- Implement the chosen behavior: prohibit copying via Uncopyable, or reference-count via a shared pointer holding the mutex with an unlock function as its deleter.
- Show what the compiler-generated copy would have done and why it is wrong here.

## Success Check
- Copying the class behaves as chosen, not as the compiler default.
- The mutex is unlocked exactly once, no matter how many copies existed.

## Common Failures
- Leaving the compiler-generated copy in place, so the mutex is released more than once.
- Reference-counting with a deleter that deletes the mutex instead of unlocking it.

## Notes
This drills Item 14: the resource's own sharing semantics decide the class's copy semantics, and the reference-count route needs a custom deleter so release, not deletion, happens at count zero.
