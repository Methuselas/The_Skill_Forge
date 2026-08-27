---
object_id: PAT_keep_a_non_owning_view_within_the_lifetime_of_what_it_views
object_type: pattern
name: Keep a Non-Owning View Within the Lifetime of What It Views
library_path:
- software-engineering
- languages
- cpp
- foundations
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- views
- lifetime
- ownership
cross_links:
- rel: related_to
  target_object_id: PAT_choose_pointer_or_reference_by_nullability_and_rebinding
- rel: related_to
  target_object_id: PAT_hand_container_data_to_a_c_api_as_a_pointer_and_a_count
- rel: related_to
  target_object_id: PAT_choose_a_callables_storage_by_whether_it_must_carry_context
- rel: related_to
  target_object_id: PAT_treat_undefined_behavior_as_a_whole_program_assumption
reference:
  source_title: 'C++20 STL Cookbook: Leverage the latest features of the STL to solve real-world problems'
  author: Bill Weinman
confidence: high
references: []
variants: []
---

# Keep a Non-Owning View Within the Lifetime of What It Views

## Pattern Rule
**IF** you are holding, passing, or returning a non-owning view — over characters, over contiguous elements, over any range
**THEN** keep every use of it inside the lifetime of the thing it views, and read a copy of it as another alias rather than as another copy of the data
**ELSE** where the data must outlive the reference to it, or where nothing in the code establishes who owns it, take a value that owns its storage and pay for the copy.

## Do
- Read the type as a claim about ownership rather than as a cheaper string or a cheaper container. It holds a position and an extent and nothing else, which is where the efficiency comes from and also the entire hazard — there is no storage inside it, so everything about its validity is a fact about something else.
- Expect every copy to alias. Copying a view copies the position and the extent, so all the copies read the same underlying bytes and a change made through one is visible through all of them. This is the opposite of what the rest of the language trains you to expect from copying a value, and it is why a chain of copies that looks obviously independent is not.
- Treat passing one to a function as handing out another alias, because that is what it is. The parameter is a copy, the copy views the same data, and a function that modifies the data through it has modified the caller's object without taking a reference to anything.
- Refuse to return one that views something local. The view outlives its storage and the result is undefined, and the failure is at its most convincing here because the function reads as though it returns a string-like value by value, which is normally the safe thing to do.
- Read the missing operations as evidence rather than as an omission. There is no appending, no resizing, no adding to the end, because every one of those would need storage the view does not have. When you find yourself wanting one, the answer is not to work around it but to notice that the job needs an owner.

## Don't
- Don't cast the const off a view's data to modify the source through it. The view's pointer is const for a reason and the cast reaches through into an object the caller believes it owns, changing it from a place that has no visible connection to it.
- Don't store one as a data member without writing down what keeps its subject alive. Membership separates the moment of construction from the moment of use by an unbounded interval, which is exactly the gap the lifetime rule lives in, and nothing at the point of use suggests the question.
- Don't reach for one to avoid a copy nobody measured. It is a genuine saving in the cases that need it and a genuine hazard in all of them, so it should be bought deliberately rather than adopted as a default spelling.

## Checklist
- What owns the data this view refers to, and where does that owner's lifetime end?
- Does this view escape the scope that owns the data — by return, by storage in a member, by capture in something stored?
- Are there copies of it, and is it clear to a reader that they all refer to one buffer?
- Is anything modifying the underlying data while views of it exist?
- Is the wish for an operation the view lacks a signal that this job wants an owning value?

## Notes
What makes this dangerous rather than merely delicate is that the correct use and the broken use are spelled identically. A function taking a view and reading it is right; a function taking a view and storing it is wrong; the parameter lists are the same, and nothing at the call site distinguishes them. The same holds for the return case, where the broken version looks more like ordinary safe C++ than the fixed one does — returning a value is the habit, and this is the type where the habit is wrong.

The aliasing behaviour is worth separating out because it surprises people who already know the lifetime rule. Copying is the language's mechanism for getting an independent thing, and here it produces a second name for the same thing. That means the usual defence — make a copy and stop worrying about the original — does not work, and a piece of code holding four views constructed from one another has one buffer and four ways to observe or corrupt it.
