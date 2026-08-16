---
object_id: PAT_decompose_into_layers_of_abstraction
object_type: pattern
name: Decompose a Problem Into Clean Layers of Abstraction
library_path:
- software-engineering
- core
- abstraction
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- abstraction
- decomposition
- subproblems
- modularity
cross_links:
- rel: related_to
  target_object_id: PAT_design_modular_interfaces
- rel: prerequisite_for
  target_object_id: PAT_expose_clean_api_hide_implementation
- rel: prerequisite_for
  target_object_id: PAT_write_functions_as_single_sentences
- rel: prerequisite_for
  target_object_id: PAT_size_classes_by_pillars_not_lines
- rel: prerequisite_for
  target_object_id: PAT_dont_widen_api_for_reuse_or_testing
- rel: prerequisite_for
  target_object_id: PAT_use_interfaces_for_swappable_layers
- rel: prerequisite_for
  target_object_id: PAT_tune_layer_thickness_err_thin
- rel: prerequisite_for
  target_object_id: PAT_keep_clean_layers_inside_microservices
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Decompose a Problem Into Clean Layers of Abstraction

## Pattern Rule
**IF** you face a problem at any level, from "let users share photos" down to "add two numbers"
**THEN** break it recursively into subproblems and structure the code as layers, where each layer solves its subproblem using only a few concepts and treats the layer beneath it as an abstract capability it need not understand.

## Do
- Aim for the property the `HttpConnection.connect(...).send(...).close()` example shows: three lines exposing four concepts (a URL, a connection, a send, a close) while hiding TCP, HTTP, radio modulation, and error correction entirely.
- Separate subproblems you must be aware of from ones you need not be — the top layer sends a string; it does not know whether the user is on WiFi or cellular.
- Keep recursing until no individual piece of code deals with more than a few easily-comprehended concepts at a time.

## Don't
- Don't force higher-level code to know how a lower layer is implemented; that coupling is the sign the layers are not clean.
- Don't dump a whole problem and all its subproblems into one undivided unit just because the top-level statement sounds like "one thing."

## Checklist
- Does each unit deal with only a handful of concepts?
- Can you describe the top layer without referring to how any lower layer works?
- Have others' solved subproblems (libraries, platform) been treated as abstract layers rather than reimplemented?

## Notes
This is the chapter's central idea and the mechanism behind four pillars at once: clean layers make code readable (few concepts per layer), modular (swap a layer without touching others — WiFi vs cellular module), reusable and generalizable (a TCP layer also serves WebSockets), and testable (each subproblem's soundness can be checked like a surveyor checking a house's foundations). The constructs that realize layers — functions, classes, interfaces — are the subjects of the more specific patterns from this chapter.
