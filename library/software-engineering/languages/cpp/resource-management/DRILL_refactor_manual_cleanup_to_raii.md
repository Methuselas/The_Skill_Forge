---
object_id: DRILL_refactor_manual_cleanup_to_raii
object_type: drill
name: Refactor Manual Resource Cleanup into an RAII Object
target_skill: Replacing manual delete/release with RAII ownership
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
- resource_management
- refactoring
cross_links:
- rel: related_to
  target_object_id: PAT_manage_resources_with_raii_objects
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Refactor Manual Resource Cleanup into an RAII Object

## Practice Task
Take a function that calls a factory such as `createInvestment`, uses the returned raw pointer, and deletes it at the end, and make it leak-proof with RAII.

## Target Skill
Handing an acquired resource to a manager whose destructor releases it, on every exit path.

## Setup
No special setup required.

## Instructions
- Mark each path — early return, loop break, thrown exception — where the manual delete would be skipped.
- Wrap the returned pointer in a smart pointer at the point of acquisition.
- Delete the manual delete statement and confirm the destructor releases on every path.
- Note why an array allocation would need a different manager than a single-object smart pointer.

## Success Check
- Every exit is enumerated before the change — each early return, each break, each call that can throw — and the count is stated. Those are the paths the manual release had to be right on, and the count is reliably larger than the function appears to have.
- Acquisition and handover occur in one statement, checked by confirming there is no statement between them where a throw would strand the resource. A pointer assigned on one line and wrapped on the next is the original defect with a smart pointer added to it.
- The manual release is gone, established by searching rather than by recollection.
- Release on the throwing path is demonstrated rather than inferred. That is the path the original got wrong and the one no ordinary test exercises.
- The array case is named with the reason a single-object manager is wrong for it, and the run says what it would use instead rather than noting only that a difference exists.

## Common Failures
- Storing the raw pointer in a variable and forgetting to wrap it before the risky code.
- Using a single-object smart pointer for an array allocation, so the wrong delete form runs.

## Notes
This drills Item 13: the leak is not a coding slip but a structural weakness of manual cleanup, which RAII removes by tying release to destruction.
