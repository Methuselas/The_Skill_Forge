---
object_id: AP_construct_quadruped_walk_from_staggered_fore_and_hind_support_cycles
object_type: ap
name: Construct Quadruped Walk From Staggered Fore And Hind Support Cycles
library_path:
- art
- subjects
- animals
- gesture-locomotion
stage_binding: 1 skeleton
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: none
tags:
- animation
- quadruped
- walk
- animal_locomotion
cross_links: []
reference:
  source_title: The Animator's Survival Kit
  author: Richard Williams
confidence: high
references: []
variants: []
---

# Construct Quadruped Walk From Staggered Fore And Hind Support Cycles

## Objective
Construct a quadruped walk as coordinated forequarter and hindquarter support systems with staggered contacts, independent chest/pelvis phases, spinal response, head delay, and tail overlap.

## Steps / Flow
1. Establish the foreleg and hind-leg contact order.
2. Track support transfer between front and rear systems.
3. Offset chest and pelvis high/low phases.
4. Carry the phase difference through the spine and delay the head from the chest.
5. Drive the tail root from the hindquarters and let the rest overlap as a flexible chain.

**Completion check**
- The animal’s weight transfer is readable through both pairs of limbs.
- Chest, pelvis, head, and tail do not peak mechanically together.

## Notes

Plot contacts and support intervals before judging surface motion; a convincing torso wave cannot rescue an impossible support sequence. Species, speed, and body plan may change the phase relationship, so preserve the established limb topology and derive chest, pelvis, head, and tail response from that specific gait.
