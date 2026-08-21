---
object_id: PAT_implement_postfix_increment_in_terms_of_prefix
object_type: pattern
name: Implement Postfix Increment in Terms of Prefix
library_path:
- software-engineering
- languages
- cpp
- operators
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- operators
- class_design
- consistency
cross_links:
- rel: related_to
  target_object_id: PAT_return_by_const_value_to_block_assignment
reference:
  source_title: 'More Effective C++: 35 New Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Implement Postfix Increment in Terms of Prefix

## Pattern Rule
**IF** you are overloading increment or decrement for a class and want both the prefix and the postfix spelling to work
**THEN** write the prefix form as the real one — modify the object, return a reference to it — and define the postfix form as: save the old value, invoke prefix, return the saved value by const value.

## Do
- Read the two names C programmers gave these as implementation specifications rather than folklore. Prefix is increment-and-fetch, so it changes the object and hands that object back; postfix is fetch-and-increment, so it keeps what was there, changes the object, and hands back what it kept.
- Leave the disambiguating parameter unnamed. Compilers pass a zero for it and the body has no use for it, so naming it only earns a warning about a parameter that is never read.
- Return the postfix result by const value so that applying the operator twice in one expression fails to compile. Built-in integers refuse that, and a class permitting it would change the object once while appearing to change it twice, since the second application acts on the returned copy.
- Tell clients to reach for the prefix spelling on class types whenever they do not need the previous value, because the postfix form has to construct and destroy an object that the prefix form never creates.

## Don't
- Don't write the two forms independently from the same specification. They are meant to differ only in what they hand back, nothing enforces that, and two people maintaining them separately will eventually make them disagree about what incrementing this type means.
- Don't give the postfix form a non-const return in the belief that returning a value is protection enough. Constness is what makes the doubled application fail, because the operator that would be applied to the returned object is not a const member function.

## Checklist
- Does the postfix body state what incrementing means, or does it delegate that entirely?
- Is the postfix return type a const value and the prefix return type a reference?
- Is the disambiguating parameter left unnamed?
- If a client applied the operator twice in succession on one object, would that be a diagnostic?

## Notes
The asymmetry in return types looks arbitrary until you see what each one is for. Prefix can return a reference because the object it owes the caller is the object it just modified, which still exists. Postfix cannot, because the value it owes the caller is the one the object no longer holds, so it must return a copy — and the copy has to be const to reproduce the behavior of the built-in types.

This is the clearest case for returning a const object, worth noting because the construct looks pointless in isolation. Its purpose is not to protect the temporary from harm; it is to make an expression that would mislead whoever reads it fail during compilation instead of at run time.

The efficiency point follows from the structure rather than from any implementation choice. Postfix necessarily creates something to hold the previous value, so on user-defined types the two spellings genuinely differ in cost — unlike on built-in integers, where the habit of writing either one was formed and where the difference does not exist.
