# Help Art

`Help Art` opens this user guide. Help requests are non-productive: they do not generate an image, approve or reject an artifact, advance or roll back the staged workflow, or change the active Art mode unless you explicitly issue a mode command separately.

## Production modes

### Mode: staged
Use when you want to build one image interactively through approval-gated visual development.

Typical start:

`MODE Staged`

Then give the art brief normally. PASS keeps the staged route active until you explicitly change mode, exit the active domain thread, or complete it. A later request for a “finished,” “final,” or “one finished full-character” image describes the eventual goal and does not cancel Staged Mode or skip the approval-gated Drawing operations. The owning Art domain supplies the actual number and meaning of visible operations; not every downstream workflow uses Drawing's five-stage sequence.

For **Drawing**, the visible workflow remains:

1. composition exploration — choose the visual idea/camera/layout;
2. scene framework — establish the whole-scene structural scaffold;
3. mass construction — establish the minimum solid forms;
4. specific rough / developed pencils — resolve specific anatomy, design, clothing/gear, architecture, props, and working form/value logic without final pencil cleanup;
5. finished pencils — clean, resolve, and integrate the approved rough as a production-ready pencil drawing without redesign.

For explicit approval-gated **Color** from an authoritative Drawing, the visible workflow is:

1. **Broad Color Direction** — establish or preserve the picture-level Color strategy, large value/light organization, broad palette/gamut, dominant Color families, warm/cool structure, and major chroma hierarchy while keeping the Drawing fixed. If several real Color strategies remain open, this operation may show roughly four to six cheap whole-picture Color roughs for selection.
2. **Color Development / Completion** — develop the exact approved Color-direction artifact into coherent causal local Color, material response, atmosphere, chroma nuance, edge hierarchy, and focal integration without replacing the approved Drawing or global Color direction.

The image generator is not asked to depict these workflows. It receives only the single visual artifact currently being made.

Stage 4 closes the universal **Drawing** workflow. Color begins only when you explicitly request it. Approval-gated Color closes after Color Development / Completion; it does not automatically launch Paint, Ink, Manga/B&W, watercolor, or another medium. Other downstream media may define different operation counts of their own.

### Mode: direct
Use when you want one finished image rather than visible approval-gated development.

Typical start:

`MODE Direct`

PASS may still use its drawing knowledge internally, but only the requested final artifact is surfaced.

## Selecting and approving in staged mode

At a candidate-selection gate, a selection such as `2`, `Use 2`, or `I like 2` means:

- candidate 2 becomes the canonical visual root for that operation;
- the current Search closes;
- unselected candidates lose productive authority;
- exactly one next visual operation becomes legal when the domain thread has a successor.

This applies to Drawing composition Search and to optional Broad Color Direction auditions.

At a non-terminal approval gate, an unqualified `Continue` means:

**commit the current artifact + freeze the decisions it owns + advance exactly one visual operation.**

`Commit and Continue` is the explicit PASS form of the same action and is always valid where a successor exists.

At terminal Color completion, bare `Continue` does not invent another medium; the Color thread simply closes unless you explicitly request a downstream workflow.

Approval is never inferred from assistant preference, praise, silence, or partial positive commentary.

## Revisions and rejection

A revision does not automatically advance the workflow.

Examples:

- `Keep this, but lower the camera.` — revise the decision that owns camera placement; roll back if necessary.
- `The left arm is wrong.` — local revision where legally possible.
- `This is too rendered.` — remain at the same visual operation and lower information density.
- `I don't like any of these.` — reopen composition Search at the same point.
- `Stop giving me this wall-run family.` — retire that composition/action family from the current Search until you explicitly reopen it.

A rejected artifact never becomes a later anchor merely because it is attractive.

## Continuity in staged mode

Once a visual root is approved, later artifacts develop the **same image forward**.

The exact approved predecessor is the visual authority. For a registered-successor operation that requires edit/reference continuity, PASS must separately confirm that this **exact canonical artifact is actually accessible to the native image tool**. Canonical identity alone is not enough. Later work preserves approved camera, crop, placement, scale, perspective, overlaps, contacts, major proportions, environment geometry, and other decisions owned upstream unless you explicitly reopen them. In approval-gated Color, once Broad Color Direction is approved, Color Development must use that exact approved Color artifact rather than restarting from the original Drawing.

This continuity applies to the whole scene: figures, creatures, weapons, vehicles, props, buildings, terrain, signs, pipes, cables, and other important objects.

The verbal brief says what may be added or changed. The approved predecessor says what must remain the same.

If exact edit/reference access is unavailable, PASS should stop and ask to recover or re-upload the exact accepted artifact. Re-uploading that artifact restores access to the same canonical predecessor and lockset; it does not create a new composition or require reapproval. PASS should not reconstruct a near-match from prose, an earlier stage, or a rejected artifact.

**Loss of edit-target access does not authorize visual reinterpretation.**

## Golden-truth references

If you identify supplied references as required character/design/canon authority, PASS must inspect the relevant visual sheets and explicit rules/specs before generating dependent artwork. You do not need to use the literal phrase **golden truth**; making a supplied package/file the required design source is enough.

Golden truth controls design authority. Early low-information artifacts may omit fine details, but omission is not permission to redesign them. Details become visible only when the current visual operation needs them.

If the reference package cannot be read or resolved, PASS should stop rather than claim the design is locked.

## Useful help topics

You can ask naturally for narrower help, for example:

- `Help Art modes`
- `Help Art staged`
- `Help Art direct`
- `Help Art revisions`
- `Help Art references`
- `Help Art approval`
- `Help Art color`

These are help requests only. They do not alter the current production state.
