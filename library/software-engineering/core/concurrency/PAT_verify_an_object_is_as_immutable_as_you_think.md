---
object_id: PAT_verify_an_object_is_as_immutable_as_you_think
object_type: pattern
name: Immutability Is a Guarantee You Have to Actually Check
library_path:
- software-engineering
- core
- concurrency
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- concurrency
- immutability
- threading
- state
- invariants
cross_links:
- rel: related_to
  target_object_id: PAT_check_concurrent_code_for_safety_and_liveness
- rel: related_to
  target_object_id: PAT_atomic_steps_do_not_compose_into_a_safe_whole
- rel: related_to
  target_object_id: PAT_dont_mutate_input_parameters
- rel: related_to
  target_object_id: PAT_prefer_immutable_objects
- rel: related_to
  target_object_id: PAT_avoid_global_state_inject_shared_state
reference:
  source_title: 'Implementing Effective Code Reviews: How to Build and Maintain Clean Code'
  author: Giuliana Carullo
confidence: high
references: []
variants: []
---

# Immutability Is a Guarantee You Have to Actually Check

## Pattern Rule
**IF** you are leaning on an object being unchangeable to avoid protecting it against concurrent access
**THEN** confirm the property holds all the way down — nothing can alter it after construction, no field can be reassigned, no reference to it escapes before it is complete, and the things it holds are themselves unchangeable — before treating shared access to it as free
**ELSE** where any of those fails, the object is ordinary shared mutable state and needs the same protection as anything else, whatever the type is called.

## Do
- Check that construction is the only moment state is set, and that no method anywhere assigns to a field afterwards. A single setter added later by someone who did not know what the class was for silently withdraws the guarantee from every place that relied on it.
- Check that the fields cannot be reassigned, using whatever the language provides to enforce it. Where the language offers nothing, the property rests on convention, and a comment saying not to modify something is not a guarantee.
- Check that a reference to the object cannot escape before construction finishes. An object registering itself somewhere from inside its own constructor, or handing a reference to a listener partway through, is visible to another thread in a half-built state — and this is the failure people miss, because the finished object looks correct.
- Follow the property inward to what the object holds. A container that never swaps out its contents is not unchangeable if the contents are, and handing out the internal collection directly gives every caller a way through.
- Separate the object from the reference to it. Nothing about an unchangeable object stops a variable holding it from being pointed at something else, and if two threads share that variable rather than the object, the guarantee was never relevant to the problem.
- Reach for objects with no state at all where the work allows it. Something holding nothing between calls has nothing to protect and nothing to verify, which is the cheapest version of this and worth preferring on those grounds alone.
- Know what your language gives you by default. Some types are unchangeable unless you work at it, others are the opposite, and assuming the wrong default is a class of error that survives careful review because the code looks the same either way.

## Don't
- Don't treat the label as the property. Naming a class for what it is meant to be, or placing it in a package of such things, does not enforce anything.
- Don't stop the audit at the outermost object. The guarantee is only as strong as the least protected thing reachable through it.
- Don't assume a value type is unchangeable because it is small or feels primitive. That varies by language and sometimes by version, and it is worth confirming rather than remembering.
- Don't rely on this for anything that has to change. Where state genuinely evolves, the answer is protection, and forcing the design into an unchangeable shape it does not fit produces object churn and a guarantee that gets quietly broken later.

## Checklist
- Can any method on this type alter the object after it is built?
- Are the fields themselves prevented from being reassigned, or only never reassigned in practice?
- Does a reference to this escape anywhere during construction — a registration, a callback, a listener?
- Is everything reachable through this object also unchangeable, including anything it hands back?
- Are the threads sharing the object, or sharing a variable that points at it?
- Could this hold nothing at all between calls instead?

## Notes
The appeal is real and the reasoning is sound as far as it goes: an object that cannot change cannot be seen in an inconsistent state, so concurrent readers need no coordination and an entire class of fault disappears. That conclusion is exactly correct when the premise holds. The difficulty is that the premise is a property of the whole reachable graph and of every constructor and method on the way, while it usually gets established by glancing at the class and forming an impression.

Escape during construction is the failure worth learning to spot, because the finished object is genuinely correct and the fault lives entirely in the window before it is finished. An object that publishes a reference to itself from inside its own constructor — registering with a manager, subscribing to something, passing itself to a helper — has made itself reachable while some fields are still unset. Another thread following that reference sees a state that will never exist again and that the class was designed to make impossible. Nothing in the finished object records that this happened, so review has to catch it at the constructor or not at all.

The reference-versus-object distinction is the other one that survives careful work, because it is a category confusion rather than an oversight. The guarantee attaches to the thing; a variable naming the thing is separate and ordinarily assignable. Two threads sharing a field that holds an unchangeable object can still race on that field, and the resulting bug looks bizarre precisely because everyone involved knows the object cannot change. Asking which of the two is actually shared resolves it immediately, and asking it early costs nothing.
