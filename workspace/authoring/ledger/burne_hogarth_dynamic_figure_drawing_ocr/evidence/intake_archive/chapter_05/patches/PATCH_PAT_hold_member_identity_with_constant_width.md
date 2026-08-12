# Candidate Patch — `PAT_hold_member_identity_with_constant_width`

status: candidate patch only
commit: held until Chapter 6 reconciliation

## Proposed changes

1. Add relation:
   - `related_to -> PAT_validate_foreshortened_limb_reach_from_joint_pivots`
2. Add one note-level synthesis:
   - Chapter 4 width control and Chapter 5 reach control solve complementary dimensions of the same foreshortening problem: width/taper preserves member identity while pivot/radius checks constrain the believable projected endpoint and length.
3. Do **not** add ellipse, arc, or triangle construction as a required step.

## Why

Printed p.135 explicitly contrasts constant width with variable projected length. Chapter 5 then supplies pivot/radius controls, while printed p.144 warns that excessive technical construction can inhibit expression.
