---
object_id: PAT_funnel_family_consistent_creation_through_one_interface
object_type: pattern
name: Funnel Family-Consistent Creation Through One Interface
library_path:
- software-engineering
- core
- design
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- design
- factories
- consistency
- coupling
- interface_segregation
cross_links:
- rel: related_to
  target_object_id: PAT_let_each_type_register_itself_with_the_factory
- rel: related_to
  target_object_id: PAT_keep_function_parameters_focused
- rel: related_to
  target_object_id: PAT_make_misuse_impossible_by_removing_invalid_states
reference:
  source_title: 'Modern C++ Design: Generic Programming and Design Patterns Applied'
  author: Andrei Alexandrescu
confidence: high
references: []
variants: []
---

# Funnel Family-Consistent Creation Through One Interface

## Pattern Rule
**IF** several kinds of object must all come from the same variant of a system — one difficulty level, one theme, one storage backend, one set of test doubles — and mixing variants would be wrong
**THEN** gather the creation of all of them behind one interface with an implementation per variant, so the variant is chosen once and cannot be mixed afterwards.
**ELSE** where the kinds are genuinely independent and any combination is legitimate, leave their creation separate; funnelling them asserts a constraint that does not exist.

## Do
- Name the constraint before building anything. "Everything on screen comes from the active theme" is a rule the design can enforce; a vague sense that these classes go together is not, and will produce an interface with no invariant to protect.
- Give each variant one implementation, so the knowledge of what pairs with what lives in one place per variant rather than being restated at each creation site.
- Select the variant once, at a boundary you can point at, and let everything downstream work through the chosen interface without knowing which one it got.
- Split the interface for consumers even though the implementation stays whole. A module that only ever creates one of the kinds should be handed a reference to that slice, so it does not depend on the rest — the consistency guarantee comes from there being one implementation, not from every consumer seeing the whole interface.

## Don't
- Don't enforce the rule by checking at each site that the pieces match. That is the same rule written many times, it grows a new instance with every creation site added, and the one that is forgotten is the one that ships.
- Don't reach for this when the combinations are actually legitimate. Funnelling independent things into a single interface makes callers ask for a variant they do not have an opinion about, and the design then has to invent one.
- Don't let a caller construct one of these kinds directly alongside the interface. A single direct construction reintroduces exactly the mismatch the arrangement exists to prevent, and it is invisible from inside the interface.
- Don't grow the interface past the family. Each kind added is one every variant must now implement, so an interface that accumulates loosely related things becomes a tax paid by every variant for the benefit of one.

## Checklist
- Can I state, in one sentence, the rule that says which things must come from the same variant?
- Is there exactly one place where a variant is chosen, and can I point at it?
- Does any consumer depend on kinds it never creates?
- Could a caller construct one of these directly, bypassing the interface, and would anything notice?

## Notes
The value here is arithmetic rather than aesthetic. Enforcing a pairing rule at the point of creation means writing it once per variant; enforcing it at the point of use means writing it once per site, and the site count grows while the variant count does not. Being careful once beats being careful a hundred times, and it is the second version that eventually misses one.

The cost is that the interface must name every kind in the family, which couples it to all of them and makes it the file that changes whenever the family grows. Splitting the interface into per-kind slices addresses the consumer half of that without weakening anything, because the guarantee never came from the interface's shape — it came from there being one implementation behind it, choosing consistently. Consumers can therefore see as little as they use while the constraint stays intact.

Where this stops being the right tool is when the family is open rather than fixed. An interface naming every kind is workable while the set is known at design time and becomes the bottleneck it was meant to avoid once new kinds arrive from outside; at that point the question changes from enforcing consistency across a closed family to resolving types that arrive at runtime, which is a different problem with a different answer.
