---
object_id: PAT_construct_centered_bilateral_product_from_one_solved_half
object_type: pattern
name: Construct Centered Bilateral Product From One Solved Half
library_path:
- art
- drawing
- sketching
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- sketching
- symmetry
- construction
- product_design
- centerline
cross_links:
- rel: related_to
  target_object_id: PAT_refresh_visual_judgment_with_mirror_and_inversion
reference:
  source_title: Design Sketching
  author: Erik Olofsson and Klara Sjolen
confidence: high
references: []
variants:
- variant_id: VAR_olofsson_alternate_sides_around_centerline_during_freehand_symmetry
  variant_name: Alternate Sides Around the Centerline During Freehand Symmetry
  variant_basis: method_sequence
  difference_from_foundation: Instead of completing one half and mirroring it, places one feature on one side and immediately
    locates its counterpart on the other, alternating across the centerline so width and proportion are corrected continuously
    while the form is still being searched.
  when_to_use: Use for centered freehand product sketches where strict duplication would make exploration too rigid but bilateral
    proportion still needs active control.
  when_not_to_use: Do not use paired alternation in an oblique view where the two sides project differently, or on intentionally
    asymmetric geometry.
  absorbed_from_object_id: none
---

# Construct Centered Bilateral Product From One Solved Half

## Pattern Rule
**IF** a bilaterally symmetric product is viewed with the camera centered on its symmetry plane
**THEN** establish the projected center plane, solve one structural half accurately, mirror that geometry to establish the other half, then reconcile central and intentionally asymmetric features
**ELSE** construct both sides perspectively when the view is oblique enough that a direct image-space mirror would be false

## Do
- Establish the centerline or center plane before detailed surface work so the mirrored half has a stable reference.
- Solve major width, height, wheel, opening, and contour relationships on one side before duplicating them.
- Reconcile features that cross the center plane instead of letting two mirrored halves create a doubled seam.
- Add lighting, reflections, decals, damage, or other asymmetric surface information only after the symmetric geometry is secure.
- During freehand exploration, use the alternate-side variant when repeated direct mirroring would make the search too rigid.

## Don't
- Do not screen-flip one half of an oblique three-quarter view; the two visible sides have different perspective projections.
- Do not mirror lighting and reflection effects automatically when the illumination or environment is asymmetric.
- Do not use symmetry to preserve a construction mistake equally on both sides.

## Checklist
- The camera is centered closely enough on the symmetry plane for direct mirroring to be geometrically justified.
- Paired structural features match around the projected center.
- Center-spanning features are reconciled into one coherent form.
- Surface asymmetry is added deliberately after the underlying bilateral structure is solved.

## Notes
Bilateral products create a cheap construction opportunity only in a centered view. When the projected symmetry plane aligns with the camera, one solved half can establish the other with high consistency. The shortcut disappears as the camera moves off that plane because the two sides then occupy different depths and project differently.

`VAR_olofsson_alternate_sides_around_centerline_during_freehand_symmetry` keeps symmetry live during construction instead of solving a whole half first. Place a feature, immediately answer it across the centerline, and let each pair correct width and proportion before the next level of detail. It is looser than direct mirroring but still depends on a centered bilateral view.
