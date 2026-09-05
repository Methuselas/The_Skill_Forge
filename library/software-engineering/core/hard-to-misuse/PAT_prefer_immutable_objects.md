---
object_id: PAT_prefer_immutable_objects
object_type: pattern
name: Prefer Immutable Objects Set Only at Construction
library_path:
- software-engineering
- core
- hard-to-misuse
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- immutability
- hard_to_misuse
- class_design
- concurrency
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_hard_to_misuse
- rel: related_to
  target_object_id: PAT_dont_mutate_input_parameters
- rel: related_to
  target_object_id: PAT_make_misuse_impossible_by_removing_invalid_states
- rel: related_to
  target_object_id: PAT_verify_an_object_is_as_immutable_as_you_think
- rel: related_to
  target_object_id: AP_make_a_class_immutable
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Prefer Immutable Objects Set Only at Construction

## Pattern Rule
**IF** you are designing a class whose instances will be passed around to other code
**THEN** default to making it immutable — take all values at construction, mark the members final (const/readonly), and provide no setters — so no other code can change it after creation, making it mutable only where mutation is genuinely required.

## Do
- Remove setter functions and set every member in the constructor; marking `font` and `fontSize` final stops even code inside the class from reassigning them and signals they never change.
- Treat immutability as a tamper-proof seal: an immutable object can be passed anywhere with certainty that no caller altered it, the way a sealed juice carton guarantees its contents.
- Lean on this for thread safety only once the seal holds all the way down — every member final, nothing mutable reachable through the object, and no reference to it handed out before the constructor has finished. A mutable object read by one thread while another writes it is a classic concurrency bug; a half-built one published early is the same bug wearing the word immutable, and it is the harder of the two to see because the finished object looks correct.

## Don't
- Don't expose setters on a value class; a `renderTitle` that calls `setFontSize(18)` on a shared instance silently changes the font size seen by the next caller.
- Don't make things mutable by default "just in case"; mutable objects are harder to reason about, so reserve mutability for the parts of the code that must track changing state.

## Checklist
- Can any code change this object's state after construction?
- Are all members final and set once, with no setter functions?
- Would passing this object to another function risk it being mutated underneath you?

## Notes
This is the core hard-to-misuse technique that the unmistakable-contract and avoid-surprises material both point toward. The `TextOptions` setter bug is the anchor: a shared instance mutated by one render call corrupts the next, and removing setters plus final members makes that impossible. Immutability also answers the reason-about-it and multithreading concerns raised earlier, with one qualification worth carrying: this card is about building the guarantee, and building it is not the same as confirming it survived. The property is easy to establish on the day and easy to lose later to a setter added by someone who did not know what the class was for, or to a collection handed straight back out. Before any concurrency argument rests on it, the guarantee is worth checking rather than assumed. The one wrinkle — needing an optional value or a modified copy — is handled by the builder and copy-on-write patterns rather than by reintroducing mutability.
