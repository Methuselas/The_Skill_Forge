---
object_id: PAT_have_the_doer_record_the_undo
object_type: pattern
name: Have the Operation Record Its Own Reversal
library_path:
- software-engineering
- core
- design
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- design
- undo
- reversibility
- command
- state_management
cross_links:
- rel: related_to
  target_object_id: PAT_split_a_deferred_call_into_captured_and_supplied
- rel: related_to
  target_object_id: PAT_single_source_of_truth_for_logic
- rel: related_to
  target_object_id: PAT_make_every_milestone_a_place_you_could_stop
reference:
  source_title: 'Modern C++ Design: Generic Programming and Design Patterns Applied'
  author: Andrei Alexandrescu
confidence: high
references: []
variants: []
---

# Have the Operation Record Its Own Reversal

## Pattern Rule
**IF** you are building undo, rollback, or compensation over a set of operations
**THEN** make each operation, at the moment it runs, record the action that reverses it — rather than giving the stored action a method that knows how to invert itself, because the relation between doing and undoing is not derivable in general.

## Do
- Record the reversal where the change happens, while the information needed to reverse it is still in hand. The value being overwritten, the position being removed from, and the state being replaced are all available at that instant and gone afterwards.
- Let the recorded reversal be a sequence when one change causes several. An edit that also moved the view has two things to undo, and if only the edit is recorded the view never comes back — the common and visible version of getting this wrong.
- Record the redo alongside the undo when redo is wanted, built the same way: at the moment the operation runs, from the same information.
- Group consecutive operations of the same kind into one recorded entry where the user would think of them as one act. A run of typing is one undo, not one per keystroke.

## Don't
- Don't ask the stored action to invert itself. Reversal is not a property of an action, it is a relation between an action and the state it ran against, and the same action reverses differently depending on what was there before.
- Don't reconstruct the reversal later from the current state. By then the information that would have told you what to restore is exactly what the operation destroyed.
- Don't assume one undo per operation. The mapping is one-to-many often enough that building the stack around a single entry per action is a structural decision you will have to undo later.
- Don't let an operation skip recording because it is small or unlikely to be undone. A stack with a hole in it does not fail on the missing entry, it fails on everything above it, and it fails by silently restoring the wrong state.

## Checklist
- At the moment each operation runs, is the reversal captured with the information it needs?
- Does any operation cause a change it does not record — a scroll, a selection, a cascade into another object?
- Does one user-level act produce one entry, or a run of entries the user will have to undo repeatedly?
- If undo runs on a stack with an entry missing, what does the state look like afterwards?

## Notes
Putting the burden on the operation rather than on the stored action is what makes this generic at all. An action that knows how to invert itself needs a bespoke class per operation, since the inverse is specific to what the operation did and to what it did it to; an action that is simply recorded by whoever performed it needs only one mechanism for holding calls, and the knowledge of what reverses what stays where it already lived.

The multiplicity is the part most often designed out too early. Operations cause other operations — an insert scrolls, a delete changes a selection, a change fires a recalculation — and each of those is a change the user expects undo to reverse. A stack whose entries are single actions cannot express that, so the structure has to allow an entry to be a sequence before it is needed rather than after.

The failure is quiet in the way that makes it expensive. An undo stack with a missing or incomplete entry does not report anything; it restores a state that is nearly right, and the discrepancy is discovered later as data that seems to have changed on its own, with no path back to the operation that failed to record itself.
