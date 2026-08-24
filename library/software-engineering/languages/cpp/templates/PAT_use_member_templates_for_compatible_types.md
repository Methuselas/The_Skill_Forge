---
object_id: PAT_use_member_templates_for_compatible_types
object_type: pattern
name: Use Member Templates to Accept All Compatible Types
library_path:
- software-engineering
- languages
- cpp
- templates
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- templates
- member_templates
- smart_pointers
cross_links:
- rel: related_to
  target_object_id: PAT_know_compiler_generated_special_members
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Use Member Templates to Accept All Compatible Types

## Pattern Rule
**IF** you want a class template such as a smart pointer to be constructible or assignable from every compatible instantiation of itself
**THEN** provide a member function template — a generalized copy constructor or assignment — whose body compiles only for compatible types, while still declaring the ordinary copy constructor and copy assignment operator.

## Do
- Add a constructor template parameterized on a second type that initializes the held pointer from the other object's held pointer, so it compiles only when that underlying pointer conversion is legal.
- Leave the generalized copy constructor non-explicit to mimic built-in pointer conversions, while keeping constructors from unrelated pointer or smart-pointer types explicit.
- Where the class carries configuration parameters as well as a value type, build the conversion one parameter at a time: initialize each part of the target from the corresponding part of the source, and let each parameter decide for itself whether it accepts the other. A parameter admits a conversion by offering a constructor taking the other, or the source parameter offers an operator converting to it; if neither exists the conversion simply does not compile, which is the right outcome.

## Don't
- Don't assume the member template replaces the normal copy constructor and copy assignment; the compiler still generates its own, so declare the normal versions too when you need to control copying.
- Don't let a conversion that changes the ownership rule happen implicitly. Reference counting works only because every owner of an object is known to one shared count, so converting such a pointer into one with a different ownership rule breaks the invariant silently rather than failing. Where the change must be possible at all, make it an explicit call that succeeds only when the source is the sole owner.
- Don't open the conversion in both directions by default. Going from a permissive configuration to a stricter one mirrors what the language already does for added constness and is safe; the reverse hands out the unchecked form, so require it to be asked for explicitly and keep its use small.

## Checklist
- Does the class need to convert from all compatible instantiations, and is that a member template?
- Does the member template's body compile only for genuinely compatible types (via the underlying pointer conversion)?
- Have I also declared the normal copy constructor and copy assignment operator?
- Does every configuration parameter get initialized from its counterpart rather than default-constructed and overwritten?
- Can any permitted conversion change which ownership rule governs the object, and if so is it explicit and guarded?

## Notes
Different instantiations of one template are unrelated types, so conversions between smart-pointer instantiations must be written explicitly. A member template — a generalized copy constructor over a second type parameter — generates the unlimited family of constructors needed, and initializing the held pointer from the source's held pointer restricts it to conversions the raw pointers allow. Crucially, a member template does not suppress the compiler-generated copy constructor and copy assignment (Item 5), so declare those explicitly when it matters, as tr1::shared_ptr does.

When the class is assembled from several configuration parameters rather than one value type, converting part by part scales where a hand-written list of permitted conversions does not: each parameter states its own compatibility once, and the set of legal conversions between whole instantiations follows from those statements instead of being enumerated. It also puts the decision where the knowledge is, since only the parameter concerned can say whether accepting the other preserves what it guarantees.

Ownership is the case that must not be left to that mechanism alone. Other configuration axes trade safety against speed and convert in the direction of more safety without harm, but an ownership rule is a claim about every owner in the program, and a conversion that changes it invalidates the claim for owners that never took part in the conversion.
