---
object_id: PAT_decide_what_a_container_holds
object_type: pattern
name: Decide What a Container Holds
library_path:
- software-engineering
- languages
- cpp
- containers
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- containers
- copy_control
- slicing
- resource_management
cross_links:
- rel: related_to
  target_object_id: PAT_use_unique_ptr_for_exclusive_ownership
- rel: related_to
  target_object_id: PAT_choose_a_container_on_more_than_algorithmic_complexity
- rel: related_to
  target_object_id: PAT_manage_resources_with_raii_objects
- rel: related_to
  target_object_id: AP_settle_a_containers_contract_before_filling_it
reference:
  source_title: 'Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Decide What a Container Holds

## Pattern Rule
**IF** you are choosing the element type for a container
**THEN** choose it knowing the container will copy and move its elements at moments you neither write nor see, so the element's copying must be cheap, correct, and conventional — and where it is not, store an owning handle rather than the object
**ELSE** where the elements are built-in types or small aggregates of them, copying is a few bits and none of this constrains the choice.

## Do
- Fix the model first, because everything else follows from it: what goes into a container is a copy of what you supplied, what you get back is a copy of what was held, and insertion, erasure, sorting, permuting, removing, rotating, and reversing all move the elements around further.
- Treat expensive copying as a property of the container rather than of the element. An element type costly to copy makes the act of filling the container a bottleneck, and every later rearrangement pays again.
- Watch for slicing, which arrives silently. A container of base-class objects given a derived object stores the base part and discards the rest, so the stored element is a base object — its added state gone and its virtual calls resolving to the base versions.
- Where the objects are polymorphic or costly, store handles. Copying a handle is cheap, always means what you expect, and slices nothing.
- Make the handle owning rather than raw. A container destroys its elements when it is destroyed, and destroying a raw pointer does nothing at all, so a container of raw pointers to allocated objects leaks every one of them unless something else releases them.

## Don't
- Don't rely on a cleanup loop at the end of the scope to release raw pointers. It works only if control reaches it, and an exception thrown between filling the container and running the loop leaks everything in it — which is the case an owning element type handles and a loop cannot.
- Don't derive publicly from a standard container to make such cleanup tidier or better typed. They have non-virtual destructors, so destroying through a pointer to the container type is undefined, and this is a trap that has caught people trying to be careful rather than people being careless.
- Don't assume an operation that reads elements does not copy them. Sorting copies a pivot element into a local temporary, and if the element's copy has side effects on the source, sorting a container silently changes its contents rather than merely reordering them.

## Checklist
- What does copying one element cost, and how many times will the container copy it?
- Could a derived object ever be handed to this container, and what would be stored if it were?
- If the container held allocated objects, what releases them, and does it run when an exception is thrown?
- Does the element type's copy or move do anything besides copy or move?

## Notes
The requirement that copying be *conventional* is the one that catches people, because it is not about cost. The historical case is the ownership-transferring smart pointer that the standard library used to provide, whose copy operation modified the object being copied — sorting a container of them set elements to null and destroyed the objects they had pointed at, so an operation that should have reordered a container instead emptied parts of it. The committee eventually made such containers illegal, and the type has since been removed from the language.

The lesson generalizes past that one type and is why it is worth keeping after the type is gone. Any element whose copy or move has observable side effects will have those side effects triggered by container operations that appear to be doing something else, at points the standard is free to choose and implementations differ about.

The modern position on move-only element types is more permissive than it was and does not conflict with this. Containers today require only that elements be movable for many operations, so element types that cannot be copied are supported. What has not changed is the requirement that whatever moving or copying the container does have its ordinary meaning.
