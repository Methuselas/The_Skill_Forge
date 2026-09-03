---
object_id: DRILL_redesign_interface_to_prevent_misuse
object_type: drill
name: Redesign an Error-Prone Interface So Misuse Won't Compile
target_skill: Using types, value constraints, and ownership to make an interface hard to misuse
library_path:
- software-engineering
- languages
- cpp
- interface-design
stage_binding: 2 block
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- interface_design
- type_safety
- hard_to_misuse
cross_links:
- rel: related_to
  target_object_id: PAT_make_interfaces_hard_to_misuse
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Redesign an Error-Prone Interface So Misuse Won't Compile

## Practice Task
Given a `Date(int month, int day, int year)` constructor, redesign it so wrong-order and out-of-range arguments cannot compile.

## Target Skill
Preventing client mistakes with distinct types, constrained values, and removed bookkeeping.

## Setup
No special setup required.

## Instructions
- List the client mistakes the current signature allows — swapped month/day, and out-of-range values — writing each as a call that compiles today.
- Introduce distinct Day, Month, and Year types so the compiler rejects wrong-kind or wrong-order arguments.
- Constrain Month to its valid values, using predefined Month objects rather than a raw int or an
  enumeration of either kind. Try the scoped-enumeration version first and record the point where it stops:
  it fixes the ordering and refuses implicit conversion to int, and an explicit cast to Month
  still yields a Month value nobody declared.
- Exercise the final design both ways — the wrong call failing to compile with the rejection recorded, the right call succeeding.
- Attempt to construct an invalid month and show it impossible rather than merely inconvenient, saying whether what you built rejects at compile time or validates at run time.
- Consider whether an associated factory should return a smart pointer to remove a release obligation.
- State the cost: more types to declare, longer call sites, and conversions at every boundary where these values arrive as plain integers anyway.

## Success Check
- The mistakes the original signature permits are listed before the redesign, each written as a call that compiles today.
- The scoped-enumeration attempt is made first and the point where it stops is recorded: it fixes the ordering and refuses implicit conversion, and an explicit cast still yields a value nobody declared. Skipping to the answer removes the reason the answer is what it is.
- The final design is exercised both ways — the wrong call fails to compile, the right call succeeds — with the compiler's rejection recorded rather than predicted.
- Constructing an invalid month is attempted and shown impossible rather than merely made inconvenient. A constructor validating at run time is a different technique, and the run says which of the two was built.
- The cost is stated: more types to declare, longer call sites, and conversions at every boundary where these values arrive as plain integers anyway.

## Common Failures
- Using an unscoped enum for the month, whose enumerators leak into the surrounding scope and
  convert implicitly to int, instead of a constrained type.
- Stopping at a scoped enumeration and reporting the interface closed. It is a real improvement and
  the implicit-conversion objection does not apply to it — see
  `PAT_prefer_the_form_that_refuses_what_you_did_not_mean`, which asks for exactly this form
  elsewhere. What it does not do is make an invalid value unconstructible, because a cast still
  reaches one. Only a type whose constructor is private and whose valid values are the only ones
  handed out closes that.
- Leaving the argument order unenforced so a swap still compiles.

## Notes
This drills Item 18: the type system is the tool that turns runtime mistakes into compile errors, and consistency plus removed bookkeeping do the rest.
