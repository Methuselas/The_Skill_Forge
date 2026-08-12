# Patch Proposal — Cast Shadows From the Light/Shape Separation, Then Grade Them in Depth

**Targets:** `AP_construct_cast_shadows_in_perspective` and White's multi-plane receiver patch.

## Gill contribution
Printed pp. 76-78 (physical pp. 79-81) identify the line of separation between directly lit and shaded form and note that the cast-shadow outline is tied to that separation. Printed pp. 83-86 (physical pp. 86-89) then apply atmospheric contrast loss to the cast shadow as it recedes across the receiver.

## Proposed merge
- After the light direction is chosen, explicitly identify the form's light/shade separation before finalizing the cast-shadow boundary.
- Treat a curved form's separation as a soft turning region unless the form has a hard plane break.
- After the shadow is geometrically solved across its receivers, apply the same depth grading that affects the receiving plane: near shadow edges/values may read stronger than distant portions.
- Keep White's receiver-turn logic for shadows that cross vertical, inclined, or curved surfaces.

## Why patch instead of new Perspective card
The geometric construction already exists. Gill adds a bridge from that geometry to rendering and depth hierarchy.
