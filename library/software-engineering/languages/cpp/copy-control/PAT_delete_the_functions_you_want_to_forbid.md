---
object_id: PAT_delete_the_functions_you_want_to_forbid
object_type: pattern
name: Delete the Functions You Want to Forbid
library_path:
- software-engineering
- languages
- cpp
- copy-control
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- copy_control
- hard_to_misuse
- class_design
- overloading
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_hard_to_misuse
- rel: related_to
  target_object_id: PAT_know_compiler_generated_special_members
- rel: related_to
  target_object_id: PAT_understand_special_member_generation
- rel: related_to
  target_object_id: AP_write_copy_control_for_a_resource_owning_class
reference:
  source_title: 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14'
  author: Scott Meyers
confidence: high
references: []
variants:
- variant_id: VAR_private_undefined
  variant_name: Declare the Copy Operations Private and Leave Them Undefined
  variant_basis: constraint
  difference_from_foundation: Instead of marking the function deleted, the copy operations
    are declared private with no definition, or inherited privately from a small
    uncopyable base whose own copy operations are private and undefined. Parameter names
    are omitted, since the functions are never defined or called.
  when_to_use: The code must compile as C++98. This is the only mechanism available
    before deleted functions existed, and it does block copying.
  when_not_to_use: Anything C++11 or later. The private form diagnoses a copy inside a
    member or friend at link time rather than compile time, applies only to member
    functions, and produces error messages about access rather than about the function
    being forbidden.
  absorbed_from_object_id: PAT_suppress_copying_with_private_undefined_or_uncopyable
---

# Delete the Functions You Want to Forbid

## Pattern Rule
**IF** you want to make a function uncallable — a copy operation the compiler would otherwise generate, or an overload that would silently accept an argument you did not intend
**THEN** declare it `= delete`, and declare it public
**ELSE** where the function is yours to simply not write, do not write it; deletion is for functions that would otherwise exist, or overloads that would otherwise be selected.

## Do
- Delete rather than hide, and take the difference seriously: a deleted function may not be used *in any way*, so a copy attempted inside a member or a friend fails to compile. The older private-and-undefined idiom lets that same code compile and fails at link time instead, which is later and harder to read.
- Declare deleted functions public even though they can never be called. Accessibility is checked before deleted status, so a private deleted function invites a diagnostic about access rather than about the function being forbidden — and that matters most when converting legacy code, where the message is the whole point of the change.
- Delete any function, not only members. This is the capability the older idiom did not have: non-member overloads and specific template instantiations can be deleted too.
- Use deleted overloads to reject conversions you never wanted. A function taking an `int` will happily accept a `char`, a `bool`, or a `double` through implicit conversion; declaring those overloads deleted rejects the calls at compile time. Deleting the `double` overload catches `float` arguments as well, since C++ prefers converting `float` to `double` over converting it to `int`.
- Remember that deleted functions still take part in overload resolution — that is the mechanism. The call resolves to the deleted overload and is then rejected, which is why the technique works and why adding one can change which overload an existing call selects.
- Extend the treatment to types that merely cannot *afford* to be copied, not only those that must not be. Deleting the copy operations on an expensive type turns every accidental copy into a compile error, and where copies are genuinely wanted a named operation such as `clone()` supplies them — so the copies that remain are the ones somebody asked for, and they are visible.
- Give such a type move operations where moving is cheaper than copying. Cheap moves are what let an otherwise non-copyable type still be returned by value and stored in containers without the copies you were trying to prevent.

## Don't
- Don't leave copy operations undeclared and expect them to be unavailable. The compiler generates public ones on demand, and the class is silently copyable.
- Don't reach for private-and-undefined in new code. It is the pre-C++11 answer, it diagnoses late, and it cannot express any of the non-member cases.
- Don't delete only one of a pair. Suppressing the copy constructor while leaving copy assignment generated leaves half the capability in place.
- Don't assume deleting a copy operation leaves the move operations alone. Declaring *any* copy operation — deleted or not — stops the compiler generating move operations for the class.

## Checklist
- Is every operation you meant to forbid actually deleted, rather than merely private or absent?
- Are the deleted declarations public?
- Which implicit conversions can still reach this function through an overload you did not delete?
- Does the class still need move operations, and are they still being generated?
- If this code must compile as C++98, is the older idiom being used deliberately rather than by habit?

## Notes
The predecessor to this rule made copying impossible by declaring the copy operations private and never defining them, so a client's copy failed to compile on access and an insider's copy failed to link on the missing definition. That worked and is preserved here as the variant `VAR_private_undefined`, which remains correct for code that must build as C++98. Deletion supersedes it on three counts rather than as a matter of style: the diagnosis moves from link time to compile time and covers members and friends, the mechanism extends to functions that are not members at all, and the error says what is actually wrong.

The extension past copy control is the part most easily missed, because the feature arrived to solve a copy-control problem. Deleting overloads is a general way to narrow what a function will accept — turning C++'s willingness to convert almost anything numeric into an explicit list of what is allowed. That is the same move as making an interface hard to misuse, applied at the level of overload resolution.

One interaction is worth carrying, since it can surprise: the special member functions are generated according to what you declare, and a declared copy operation suppresses the move operations regardless of whether that declaration is a definition, a defaulted one, or a deleted one. Deleting copying to protect an expensive type therefore also removes its generated moves, which is usually the opposite of what was wanted.
