# Chapter 5 Reconciliation Patch Proposal

**Target:** `PAT_validate_foreshortened_limb_reach_from_joint_pivots`  
**State:** proposal only; no canonical mutation.

Chapter 6 does **not** supersede the Chapter 5 Pattern.

Recommended relationship:
- Chapter 6 projection establishes whole-view / scene correspondence.
- Chapter 5 reach validation remains a local diagnostic when an individual projected limb endpoint is still uncertain.
- Add `PAT_transport_proportional_landmarks_across_views` as an optional upstream context for difficult-view corrections.
- Keep pivot arcs optional and correction-triggered.

Compact hierarchy:

`shared projection/correspondence → local limb reach → width/taper identity → anatomy finish`
