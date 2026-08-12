# Patch Proposal — Physical Light/Material Branch for Hogarth Tone Consolidation

**Target:** canonical `PAT_consolidate_resolved_form_with_tone`.

## Gill contribution
Gill's rendering system separates three questions that Hogarth's sculptural tone sometimes combines: (1) which surfaces are directly lit versus shaded, (2) where cast shadows land, and (3) how the material and surroundings alter the returned/reflected light. His cylinder, glass, water, and reflected-light examples repeatedly show material response modifying—but not replacing—the underlying form.

## Proposed merge
Preserve Hogarth's existing use of tone to unify resolved form, but make the production branch explicit:
- structural/sculptural tone may be used during form study;
- final scene rendering should first respect the chosen light and shadow geometry;
- material response, reflected light, transparency, and texture modify those values afterward;
- if a beautiful tonal grouping contradicts the scene light, either change the light intentionally or treat the grouping as a study rather than physical illumination.

This is a clarification patch, not a replacement of Hogarth's form-unity Pattern.
