---
object_id: PAT_make_classes_care_about_themselves
object_type: pattern
name: Make Each Class Care About Itself
library_path:
- software-engineering
- core
- modularity
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- law_of_demeter
- modularity
- encapsulation
- coupling
cross_links:
- rel: related_to
  target_object_id: PAT_design_modular_interfaces
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Make Each Class Care About Itself

## Pattern Rule
**IF** logic in one class operates only on the internals of another class
**THEN** move that logic into the class it concerns, as a member function, so a change to that concept touches only one class.

## Do
- Relocate the reaching-in logic: a word-count that sums a chapter's prelude and sections belongs on `Chapter` as `wordCount()`, not on `Book` as a helper that knows a chapter's parts.
- Let the owning class expose the high-level operation and have the caller use it: `Book` sums `chapter.wordCount()` and stays ignorant of what a chapter contains.
- Watch for chained access through an object into its parts — `chapter.getPrelude().wordCount()` — as the smell that a class is caring about another's structure (the Law of Demeter).
- Price the delegation before applying it everywhere. Following the rule means writing wrapper methods whose only job is to forward a request to whatever actually holds the answer, and those wrappers cost a call and a little space each. Where that overhead is genuinely prohibitive, coupling the two directly is a legitimate design choice.

## Don't
- Don't hard-code one class's structure into another; if `Book` assumes a chapter has only a prelude and sections, adding a chapter summary silently breaks the book's word count.
- Don't spread a single concept across classes so a requirement change forces edits in several places and risks one being forgotten.
- Don't reverse the rule quietly. What makes a deliberate coupling acceptable is that the people maintaining both sides know about it and have agreed to it — the same shortcut taken without saying so is exactly the invisible dependency the rule exists to prevent.

## Checklist
- Does any method operate mainly on another class's fields or parts?
- Would a change to one concept require edits in more than one class?
- Are you reaching through an object into its members rather than asking the object directly?
- If you are choosing to couple instead, is that choice recorded somewhere the next maintainer of either side will see it?

## Notes
This is a rule with a real price, and knowing the price is what keeps it from being applied as dogma. Delegating rather than reaching through means the intermediate object takes on the job of managing everything behind it on its callers' behalf, and in practice that shows up as a large number of small forwarding methods. They cost runtime and space, and in a hot path or a memory-constrained system the cost can be the deciding factor. The comparison worth holding is denormalising a database schema: breaking a rule of normalisation for speed is not a failure of discipline, it is a trade made with open eyes. Coupling two modules tightly on purpose sits in the same category. The condition that makes it sound is not that it is fast — it is that the coupling is known and accepted by everyone who maintains either side, which is exactly what an accidental version of the same shortcut lacks.

The `Book`/`Chapter` example makes the coupling concrete: putting `getChapterWordCount` on `Book` means a chapter-summary requirement changes `Book`, and forgetting to update it corrupts the count. Moving the logic onto `Chapter` confines chapter changes to `Chapter`. The Law of Demeter names the guiding heuristic — interact only with immediate collaborators, not their internals — and the chained call is exactly the transgression to look for, serving the chapter's aim that a requirement change touch only the code that owns that requirement.
