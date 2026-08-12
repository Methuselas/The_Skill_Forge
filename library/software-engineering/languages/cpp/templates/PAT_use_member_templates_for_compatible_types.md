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
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u07, pp. 218-222
  evidence_type: text
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

## Don't
- Don't assume the member template replaces the normal copy constructor and copy assignment; the compiler still generates its own, so declare the normal versions too when you need to control copying.

## Checklist
- Does the class need to convert from all compatible instantiations, and is that a member template?
- Does the member template's body compile only for genuinely compatible types (via the underlying pointer conversion)?
- Have I also declared the normal copy constructor and copy assignment operator?

## Notes
Different instantiations of one template are unrelated types, so conversions between smart-pointer instantiations must be written explicitly. A member template — a generalized copy constructor over a second type parameter — generates the unlimited family of constructors needed, and initializing the held pointer from the source's held pointer restricts it to conversions the raw pointers allow. Crucially, a member template does not suppress the compiler-generated copy constructor and copy assignment (Item 5), so declare those explicitly when it matters, as tr1::shared_ptr does.
