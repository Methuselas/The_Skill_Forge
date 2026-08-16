---
object_id: PAT_write_a_well_behaved_new_handler
object_type: pattern
name: Write a New-Handler That Always Makes Progress
library_path:
- software-engineering
- languages
- cpp
- memory-management
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- memory_management
- new_handler
- allocation
cross_links:
- rel: related_to
  target_object_id: PAT_offer_an_exception_safety_guarantee
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Write a New-Handler That Always Makes Progress

## Pattern Rule
**IF** you install a new-handler with set_new_handler to respond to allocation failure
**THEN** ensure it does one of five things — make more memory available, install a different new-handler, deinstall the handler, throw bad_alloc (or a derived type), or not return — because operator new calls it in a loop that only these actions can end.

## Do
- Free memory the handler reserved at startup, or install a more capable handler, so the next allocation attempt inside operator new can succeed.
- Otherwise deinstall the handler by passing null (letting operator new throw), throw bad_alloc yourself, or terminate with abort or exit when recovery is impossible.

## Don't
- Don't write a new-handler that returns without changing anything; operator new will call it again and again in an infinite loop.
- Don't rely on nothrow new for safety; it only stops operator new from throwing, while the object's constructor can still throw, so the whole new expression may still yield an exception.

## Checklist
- Does the handler perform one of the five progress-making actions on every path?
- Could it return without freeing memory, swapping handlers, or terminating — an infinite loop?
- Am I over-trusting nothrow new, forgetting the constructor may still throw?

## Notes
When operator new cannot satisfy a request it calls the installed new-handler repeatedly until it can, so a handler that neither frees memory, swaps itself out, deinstalls, throws, nor terminates spins forever. set_new_handler installs the handler and returns the previous one. Nothrow new is of limited use: it makes only the allocation non-throwing, so a constructor invoked by the same new expression can still throw and propagate.
