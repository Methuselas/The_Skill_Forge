---
object_id: PAT_construct_only_the_hidden_path_visible_forms_require
object_type: pattern
name: Construct Only the Hidden Path Visible Forms Require
library_path:
- art
- foundations
- form-construction
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- hidden_forms
- draw_through
- form_construction
- spatial_reasoning
cross_links:
- rel: related_to
  target_object_id: PAT_create_depth_sequence_with_overlap
reference:
  source_title: Keys to Drawing
  author: Bert Dodson
confidence: high
references: []
variants:
- variant_id: VAR_hogarth_scale_hidden_figure_chain_to_visible_dependencies
  variant_name: Scale the Hidden Figure Chain to Visible Dependencies
  variant_basis: method_sequence
  difference_from_foundation: 'Hogarth and guided review specialize the draw-through decision for blocked limbs and digits:
    reconstruct the full hidden bend only when visible endpoints, attachments, balance, or later overlaps depend on it, and
    otherwise stop at the minimum useful concealed chain.'
  when_to_use: Use when a figure contains blocked limbs, digits, or overlapping anatomical members whose visible fragments
    cannot be placed reliably without a concealed route.
  when_not_to_use: Do not invent a complete hidden limb merely because anatomy says one must exist somewhere behind the visible
    body when no visible decision depends on its exact path.
  absorbed_from_object_id: none
- variant_id: VAR_dodson_think_through_after_transparent_construction_is_internalized
  variant_name: Think Through After Transparent Construction Is Internalized
  variant_basis: method_sequence
  difference_from_foundation: Adds Dodson's progression from literally drawing transparent boxes, cylinders, and hidden sides
    to holding the same solid mentally once the spatial relationship is familiar, returning to explicit construction only
    when uncertainty appears.
  when_to_use: Use in practiced freehand work when the hidden solid is understood well enough to guide visible edges without
    cluttering the drawing.
  when_not_to_use: Do not skip explicit draw-through when symmetry, attachment, contact, or continuation is still uncertain;
    mental construction is earned by understanding, not by avoiding the check.
  absorbed_from_object_id: none
- variant_id: VAR_eissen_retain_selected_construction_guides_for_shape_communication
  variant_name: Retain Selected Construction Guides for Shape Communication
  variant_basis: context
  difference_from_foundation: Keeps a small amount of transparent construction visible after the form is solved when those
    guides help a reader understand exact placement, a hidden side, a lid or part relationship, or the underlying volume that
    generated the visible contour.
  when_to_use: Use in exploratory or explanatory product sketches where showing how the form is built communicates information
    that the clean contour alone would hide.
  when_not_to_use: Do not preserve every hidden edge or guideline in a presentation image when the extra construction no longer
    explains a specific shape relationship.
  absorbed_from_object_id: none
---

# Construct Only the Hidden Path Visible Forms Require

## Pattern Rule
**IF** unseen structure controls the placement, symmetry, contact, attachment, or continuation of visible forms
**THEN** construct through the minimum hidden volume or path needed to make those visible decisions reliable
**ELSE** stop when the exposed form already supplies enough spatial information to continue confidently

## Do
- Draw through a cup, chair, box, limb, cylinder, or other form when unseen sides determine the visible rim, attachment, contact, or continuation.
- Use simple transparent solids when they make the hidden relationship easier to reason about than contour guessing.
- Scale the amount of hidden construction to the number of visible decisions that depend on it.
- Keep explicit hidden guides light and disposable; their job is to stabilize the visible result, not to survive into the finish.
- As the spatial model becomes internalized, hold obvious hidden continuations mentally and redraw them explicitly only when a check is needed.

## Don't
- Draw every hidden edge of every object by habit; excessive draw-through can bury the useful structure in line clutter.
- Skip a concealed route when two visible fragments would otherwise imply incompatible versions of the same form.
- Treat mental construction as permission to guess.
- Leave hidden guides prominent after their explanatory job is complete.

## Checklist
- Visible fragments agree with one coherent hidden whole.
- The hidden construction is no more extensive than the visible dependencies require.
- Symmetry, attachment, or contact does not force an impossible unseen continuation.
- Removing the guide leaves a visible result that still implies the solid or connected form convincingly.

## Notes
Practice transparent draw-through with cups, chairs, figures, and architecture, then progress toward “thinking through” once the solid can be held mentally. The earlier figure card is promoted into this subject-general foundation, with its minimum-sufficient hidden-limb rule retained as a figure-specific variant.
`VAR_eissen_retain_selected_construction_guides_for_shape_communication` adds a communication exception to the usual cleanup endpoint: in an exploratory product sketch, selected transparent blocks, hidden sides, and construction guides may remain visible when they tell the reader where a part sits or how the shape was derived. The variant preserves that explanatory use while rejecting indiscriminate hidden-line clutter.

Variants retained in this canonical object: `VAR_hogarth_scale_hidden_figure_chain_to_visible_dependencies`, `VAR_dodson_think_through_after_transparent_construction_is_internalized`, `VAR_eissen_retain_selected_construction_guides_for_shape_communication`.
