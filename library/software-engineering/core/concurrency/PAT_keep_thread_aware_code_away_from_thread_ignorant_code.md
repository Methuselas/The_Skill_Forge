---
object_id: PAT_keep_thread_aware_code_away_from_thread_ignorant_code
object_type: pattern
name: Keep Thread-Aware Code Away From Thread-Ignorant Code
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
- separation_of_concerns
- threading
- design
- maintainability
cross_links:
- rel: related_to
  target_object_id: PAT_get_the_single_threaded_version_working_first
- rel: related_to
  target_object_id: PAT_avoid_sharing_before_you_reach_for_protecting_it
- rel: related_to
  target_object_id: PAT_split_code_to_make_it_testable
- rel: related_to
  target_object_id: PAT_ask_what_should_be_hidden
reference:
  source_title: 'Clean Code: A Handbook of Agile Software Craftsmanship'
  author: Robert C. Martin, with Brett L. Schuchert
confidence: high
references: []
variants: []
---

# Keep Thread-Aware Code Away From Thread-Ignorant Code

## Pattern Rule
**IF** you are deciding where locking, thread creation, and coordination will live in a design
**THEN** gather them into their own components and leave the computation in components that know nothing about them, so each part can be read, changed, and checked for one kind of correctness at a time
**ELSE** where a component genuinely cannot be expressed without coordination — a queue, a pool, a scheduler — that component is the aware part, and the requirement becomes that it stays small and holds no application logic.

## Do
- Draw the boundary so the computation lands on the ignorant side. Something that takes its inputs, produces its outputs, and never learns whether it ran alone can be reasoned about by anyone, and it does not change when the coordination strategy does.
- Keep the coordinating components small and about coordination only. They are the hardest code in the system to get right and to check, and every line of unrelated logic inside them is carried at that difficulty.
- Treat coordination as having its own rhythm of change. A thread count adjusted for throughput has nothing to do with a business rule changing, and mixing them makes each change touch code it has no business in.
- Let the boundary serve twice. The separation that makes coordination reviewable is the same one that lets the computation be exercised alone, so the design decision and the checking strategy are a single decision.
- Name which side each component sits on, and expect very few on the aware side. A large count means the coordination has leaked, and it always leaks one convenient call at a time.
- Put shared state on the aware side beside the code that guards it. Separating the two is how a guard comes to be forgotten.

## Don't
- Don't sprinkle locking through the components that do the work. It places the hardest correctness question in the codebase inside files that are otherwise ordinary, where readers do not expect it and reviewers do not check for it.
- Don't let a component be partly aware. Something that mostly ignores threading and takes a lock in one method carries all the difficulty of the aware side and none of the containment.
- Don't argue the coordination is too small to be worth separating. It grows, and it grows into whatever it is already touching.
- Don't place application logic inside the coordinating components for convenience. Everyone who later reads that logic must then understand it in terms of ordering.

## Checklist
- Which components know threads exist, and how many are there?
- Could the computation be run and checked with no threads at all?
- Is any lock taken outside the components you designated as coordinating?
- Does shared state sit with the code that protects it?
- If the threading strategy changed tomorrow, which files would have to change?

## Notes
The argument is that coordination is a separate concern with its own reasons to change, and the usual penalty for mixing concerns is heavier here than elsewhere. Ordinary tangling costs readability. Coordination tangled through a codebase means every reader of every affected file must hold ordering in mind while reading logic, and reviewers must watch for a class of fault that is invisible on the page and that they were not looking for. The result is not a confusing file; it is a missing guard nobody noticed.

How this erodes is worth recognising, because it is never a decision anyone makes. Nobody sets out to distribute locking across a system. A lock goes in one place because that was convenient, then another because the first made it look normal, and eventually the boundary is gone without a single wrong step. Counting the components that know about threads is a cheap repeatable check against that drift, and a count rising across releases is the signal.

The relationship to checking the code is not a side benefit but the same property viewed differently. Logic on the ignorant side can be exercised without threads precisely because it does not depend on them, and that independence is what the separation creates. A design that makes coordination reviewable and a design that makes computation checkable are therefore not competing goals to be balanced — they are one boundary, drawn once, and either both benefits follow or neither does.
