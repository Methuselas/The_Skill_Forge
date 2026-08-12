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
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u08, pp. 226-228
  evidence_type: text
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

## Don't
- Don't hard-code one class's structure into another; if `Book` assumes a chapter has only a prelude and sections, adding a chapter summary silently breaks the book's word count.
- Don't spread a single concept across classes so a requirement change forces edits in several places and risks one being forgotten.

## Checklist
- Does any method operate mainly on another class's fields or parts?
- Would a change to one concept require edits in more than one class?
- Are you reaching through an object into its members rather than asking the object directly?

## Notes
The `Book`/`Chapter` example makes the coupling concrete: putting `getChapterWordCount` on `Book` means a chapter-summary requirement changes `Book`, and forgetting to update it corrupts the count. Moving the logic onto `Chapter` confines chapter changes to `Chapter`. The Law of Demeter names the guiding heuristic — interact only with immediate collaborators, not their internals — and the chained call is exactly the transgression to look for, serving the chapter's aim that a requirement change touch only the code that owns that requirement.
