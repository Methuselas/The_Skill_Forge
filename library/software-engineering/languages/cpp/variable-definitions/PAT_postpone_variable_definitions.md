---
object_id: PAT_postpone_variable_definitions
object_type: pattern
name: Postpone Variable Definitions Until You Can Initialize Them
library_path:
- software-engineering
- languages
- cpp
- variable-definitions
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- variable_definitions
- efficiency
- initialization
cross_links:
- rel: related_to
  target_object_id: PAT_initialize_members_with_init_list
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Postpone Variable Definitions Until You Can Initialize Them

## Pattern Rule
**IF** you are about to define a local variable of a type with a constructor and destructor
**THEN** postpone its definition until you actually need it and have its initialization arguments, so you skip constructing objects you never use and avoid a wasteful default-construct-then-assign.

## Do
- Define the variable only after any early-exit checks, such as a length test that throws, so an exception before that point costs no construction or destruction.
- Initialize it with its real value in the definition (copy-construct from that value) instead of default-constructing and assigning afterward.
- For a variable used only inside a loop, define it inside the loop unless assignment is cheaper than a constructor-destructor pair and the loop is performance-critical.

## Don't
- Don't define a variable at the top of a function out of habit; if a later throw skips its use, you paid for its construction and destruction for nothing.

## Checklist
- Is this variable defined right before its first use, after any code that might exit early?
- Am I initializing it with its real value rather than default-constructing then assigning?
- For a loop variable, have I weighed inside-loop (n constructions and destructions) against outside-loop (one pair plus n assignments)?

## Notes
The `encryptPassword` example defines the result string before a length check that can throw, paying for an object it may never use; moving the definition below the check fixes that, and initializing it from the password (rather than default-constructing then assigning) removes a pointless default construction — the same init-versus-assign lesson as the member initializer list. For loops, the default is to define inside; only switch to outside when assignment is measurably cheaper than a constructor-destructor pair in hot code.
