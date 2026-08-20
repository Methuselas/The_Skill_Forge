---
object_id: PAT_consider_emplacement_where_it_can_actually_help
object_type: pattern
name: Consider Emplacement Where It Can Actually Help
library_path:
- software-engineering
- languages
- cpp
- parameter-passing
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- containers
- performance
- exception_safety
- avoiding_surprises
cross_links:
- rel: related_to
  target_object_id: PAT_pass_by_value_only_when_all_four_conditions_hold
- rel: related_to
  target_object_id: PAT_prefer_make_functions_to_direct_new
- rel: related_to
  target_object_id: PAT_price_shared_ownership_before_choosing_it
- rel: related_to
  target_object_id: PAT_let_measurement_decide_what_to_tune
reference:
  source_title: 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Consider Emplacement Where It Can Actually Help

## Pattern Rule
**IF** you are adding an object to a container and considering the emplacement function rather than the insertion one
**THEN** check that the three conditions under which it actually helps are present, and that neither of its two hazards applies
**ELSE** where you already hold an object of the container's element type and are simply putting it in, the two are equivalent and the choice is style.

## Do
- Understand where the saving comes from, because it tells you when there is none. Insertion takes an object of the element type, so arguments of any other type must first be converted into a temporary, which is then copied or moved into the container and destroyed. Emplacement takes constructor arguments and builds the element in place, so no temporary exists.
- Require the first condition: the value is being *constructed* into the container rather than assigned over an existing element. Where an element is being assigned to, the storage already exists, and building in place has nothing to save.
- Require the second: the argument types differ from the type the container holds. Passing an object of the element type to an emplacement function gives it nothing to construct — there is no temporary either way.
- Require the third: the container will not reject the value. An associative container that discovers the new value is a duplicate has already constructed it, whereas an insertion function would have compared the temporary and destroyed it — so for a container that mostly rejects duplicates, emplacement can be the slower of the two.
- Watch for the resource-management hazard, which is a correctness matter rather than a performance one. Building a smart pointer with insertion creates a temporary smart pointer first, so a failure inside the container's allocation destroys it and releases the resource. Emplacement forwards the raw pointer and constructs the smart pointer inside the container; if the allocation fails before that construction, nothing owns the resource and it leaks.
- Watch for the initialization hazard. Emplacement direct-initializes, insertion copy-initializes — so emplacement will invoke constructors marked explicit that insertion rejects. That converts a compile error into a compiling construction, which is welcome when the conversion is intended and is how an object gets built from an argument that should never have been accepted.

## Don't
- Don't convert insertion calls to emplacement across a codebase on the strength of the principle. In principle emplacement should never be slower and sometimes faster; in practice the three conditions decide it, and where they do not hold there is nothing to gain.
- Don't emplace a resource-owning object built from a raw handle. The exception-safety difference is real, and the whole point of the smart pointer was that the resource is owned from the moment it exists.
- Don't take a successful compile as evidence the argument was appropriate. Direct initialization accepts conversions the author of the type marked explicit precisely to prevent, and the result can be a well-formed object built from something meaningless.
- Don't expect the difference to show up without measurement. The saving is one temporary construction and destruction per call, which matters where the element type is expensive and the call is hot, and is invisible otherwise.

## Checklist
- Is the element being constructed into the container, or assigned over an existing one?
- Do the argument types differ from the container's element type?
- Could the container reject this value as a duplicate?
- Is the object being added a resource owner built from a raw handle?
- Would any argument here be rejected by an insertion function, and should it be?

## Notes
The general principle and the practical advice point in slightly different directions, and it is worth holding both. Emplacement should never be less efficient than insertion, because it can do everything insertion does and avoid a temporary besides. What the three conditions describe is when there is a temporary to avoid — and in a great deal of ordinary code there is not, because the caller already holds an object of the right type.

The two hazards are worth separating from the performance question entirely, since they are the reason this is a judgment rather than an upgrade. Both come from the same source: emplacement forwards arguments to a constructor that runs later and elsewhere. That is what removes the temporary, and it is also what removes the temporary's destructor from the exception path and what changes copy initialization into direct initialization.

The exception-safety case generalizes past containers. Anywhere a resource is acquired and its owner is constructed at a later point, the interval between the two is exposed — the same shape as an allocation appearing in an argument list. Emplacing a raw handle widens that interval to include a container's allocation, which is exactly the kind of thing that fails under memory pressure and never in testing.
