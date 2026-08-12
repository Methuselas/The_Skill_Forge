# MEMCAP — Burne Hogarth, *Dynamic Figure Drawing*, Chapter 5
## Targeted PASS Memory

**Chapter:** 5 — “Figure Invention: Controlling Length in Foreshortened Forms”  
**Printed pages:** 135–149  
**Scan images:** Page_136–Page_150  
**Disposition:** Targeted PASS / reinforcement-heavy  
**Commit state:** candidate only; reconcile after Chapter 6

## Source spine

```text
projected length is variable in depth
→ use circle/ellipse radius as a constant physical reach
→ treat joint as pivot and member as radius
→ track possible endpoints through arcs
→ simplify when technical ellipse work becomes cumbersome
→ use leg triangle and body-to-body functional checks in compressed poses
```

## Teacher correction / practical interpretation

The teacher's key diagnosis is that this chapter is substantially about **range of motion and reach** in practice. That makes it useful for correcting wonky anatomy, but also makes much of it redundant with the existing articulated-limb and foreshortening foundation.

Do not convert every Hogarth measuring device into a separate mandatory Skill Card.

## What Chapter 5 genuinely adds

The useful delta is a diagnostic:

> When projected limb length becomes unreliable, preserve the designed segment length, treat the carrying joint as a pivot, and test whether the next endpoint is reachable before building anatomy over it.

This complements Chapter 4:

```text
Chapter 4: width/taper preserves member identity.
Chapter 5: pivot/reach constrains believable projected length.
```

## Geometry boundary

Hogarth explicitly warns that too much reliance on ellipse construction can become cumbersome and inhibit expression. The triangle is introduced as a shortcut, and the later full-body examples increasingly use direct body-part relationships.

Therefore:
- ellipse/arc = optional diagnostic;
- isosceles triangle = source-specific shortcut, not a universal drawing law;
- body-contact checks = pose-specific sanity checks;
- believable articulated reach = the durable capability.

## Extracted candidates

1. `PAT_validate_foreshortened_limb_reach_from_joint_pivots`
2. `DRILL_correct_wonky_foreshortened_limb_with_pivot_arcs`
3. candidate note patch to `PAT_hold_member_identity_with_constant_width`

No Chapter 5 AP is created.
No new Accent is created.
No visual reference is generated.

## Why the Drill is correction-mode

The teacher specifically identified the chapter's value for **wonky anatomy**. The Drill therefore requires a real failure signal and operates on the smallest affected limb chain. Its practice artifact never becomes authority over the parent drawing.

## Hold for Chapter 6

Revisit after Chapter 6 to decide whether:
- this new Pattern remains standalone;
- it folds into a broader whole-figure projection Pattern;
- `AP_control_foreshortened_form_size_in_stage_two` should be broadened or superseded;
- the correction Drill remains useful once projection knowledge is active.

Do not finalize Stage bindings before the Stage walkthrough is committed.
