---
object_id: DRILL_fix_deep_mutability_in_a_class
object_type: drill
name: Close the Deep-Mutability Holes in a Class
library_path:
- software-engineering
- core
- hard-to-misuse
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- immutability
- defensive_copying
- references
- refactoring
cross_links:
- rel: teaches
  target_object_id: PAT_make_immutability_deep
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u07, pp. 181-186
  evidence_type: text
confidence: high
target_skill: finding and closing shared-reference mutation paths in a supposedly immutable class
references: []
variants: []
---

# Close the Deep-Mutability Holes in a Class

## Practice Task
Take a class that looks immutable but holds a mutable member, demonstrate both ways its state leaks, then close the holes.

## Target Skill
Finding shared-reference mutation paths and sealing them with defensive copies or immutable structures.

## Setup
No special setup required.

## Instructions
1. Start from a class with a final member of a mutable type — a font-family list marked final, with a plain constructor and getter.
2. Reproduce scenario A: construct the object from a list, then mutate that original list afterward, and observe the object's state change.
3. Reproduce scenario B: call the getter, mutate the returned list, and observe the object's state change again.
4. Fix it two ways and compare: first by defensively copying the list in the constructor and in the getter, then by switching the member to an immutable list.
5. Confirm both scenarios are now blocked, and note that only the immutable-structure version also stops code inside the class from mutating the member.

## Success Check
- Both the after-construction and via-getter mutations no longer affect the object.
- The defensive-copy version copies at both the constructor and the getter.
- The immutable-structure version needs no copies and blocks in-class mutation too.

## Common Failures
- Copying in the constructor but not the getter (or vice versa), leaving one hole open.
- Believing a final member is enough, when final stops reassignment but not mutation of the referenced object.

## Notes
This drills the `TextOptions` font-family example, whose whole point is that a final reference is not deep immutability. Doing both fixes side by side makes the tradeoff concrete: defensive copying works but costs copies and misses in-class mutation, while an immutable data structure is the more robust and often cheaper choice.
