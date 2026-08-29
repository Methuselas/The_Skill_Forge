---
object_id: PAT_dont_implement_one_copying_function_via_the_other
object_type: pattern
name: Don't Implement One Copying Function in Terms of the Other
library_path:
- software-engineering
- languages
- cpp
- copy-control
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- copy_control
- code_duplication
- class_design
cross_links:
- rel: related_to
  target_object_id: PAT_copy_all_members_and_base_parts
- rel: related_to
  target_object_id: AP_write_copy_control_for_a_resource_owning_class
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Don't Implement One Copying Function in Terms of the Other

## Pattern Rule
**IF** your copy constructor and copy assignment operator share similar code
**THEN** factor the common work into a private helper both call — never have the copy constructor call the assignment operator or the reverse.

## Do
- Put the shared copying logic in a private member function (often named `init`) and call it from both copying functions.

## Don't
- Don't have copy assignment call the copy constructor: that tries to construct an object that already exists, which has no valid syntax.
- Don't have the copy constructor call copy assignment: assignment only makes sense on an already-initialized object, and the copy constructor's object is not yet initialized.

## Checklist
- Is shared copy logic in a common helper rather than one copying function calling the other?
- Have I avoided constructing an already-existing object, and assigning to a not-yet-initialized one?

## Notes
The urge to remove duplication between the two copying functions is right, but routing one through the other is the wrong cure: constructing an object that exists is nonsensical, and assigning to an object still under construction operates on uninitialized state. The safe, proven approach is a third private function — typically `init` — that both the copy constructor and copy assignment operator call.
