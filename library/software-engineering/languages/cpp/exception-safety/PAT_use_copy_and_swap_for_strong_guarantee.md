---
object_id: PAT_use_copy_and_swap_for_strong_guarantee
object_type: pattern
name: Use Copy-and-Swap for the Strong Exception-Safety Guarantee
library_path:
- software-engineering
- languages
- cpp
- exception-safety
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- exception_safety
- copy_and_swap
- pimpl
cross_links:
- rel: related_to
  target_object_id: PAT_support_nonthrowing_swap
- rel: related_to
  target_object_id: PAT_offer_an_exception_safety_guarantee
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Use Copy-and-Swap for the Strong Exception-Safety Guarantee

## Pattern Rule
**IF** you want a function to offer the strong guarantee — an all-or-nothing state change
**THEN** use copy-and-swap: make a copy of the object's data, apply all changes to the copy, then swap it into place with a non-throwing swap, so a failure leaves the original untouched.

## Do
- Put the object's data behind an implementation pointer (pimpl), copy it, modify the copy, and swap the pointers at the end in a non-throwing operation.
- Do the swap only after every operation that could throw has already succeeded.

## Don't
- Don't expect copy-and-swap alone to make a function strongly safe when it also has side effects on non-local data — a committed database change or a moved stream position cannot be undone by a swap.
- Don't pay for copy-and-swap when the strong guarantee is impractical here; the basic guarantee is a legitimate, deliberate choice.

## Checklist
- Are all throwing operations performed on the copy before anything is swapped into place?
- Is the final swap non-throwing?
- Do side effects on non-local state defeat the strong guarantee here, making the basic guarantee the honest choice?

## Notes
Copy-and-swap gives atomic state change: build the new state in a copy, then swap it in with the non-throwing swap from the swap Item, so a throw during modification never touches the original. Its two limits are real: side effects on non-local data (databases, stream markers) survive the swap and break the guarantee, and copying costs time and space. Offer the strong guarantee when practical, but the basic guarantee is a reasonable, defensible outcome for many functions.
