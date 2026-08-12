---
object_id: PAT_match_caller_mental_model
object_type: pattern
name: Match the Caller's Mental Model
library_path:
- software-engineering
- core
- avoiding-surprises
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- avoid_surprises
- api_design
- mental_model
- least_astonishment
cross_links:
- rel: prerequisite_for
  target_object_id: PAT_avoid_returning_magic_values
- rel: prerequisite_for
  target_object_id: PAT_use_null_object_pattern_only_when_safe
- rel: prerequisite_for
  target_object_id: PAT_avoid_unexpected_side_effects
- rel: prerequisite_for
  target_object_id: PAT_dont_mutate_input_parameters
- rel: prerequisite_for
  target_object_id: PAT_make_critical_inputs_required
- rel: prerequisite_for
  target_object_id: PAT_handle_enums_exhaustively
- rel: prerequisite_for
  target_object_id: PAT_design_against_surprises_not_rely_on_tests
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u01, pp. 13-15
  evidence_type: text
confidence: high
references: []
variants: []
---

# Match the Caller's Mental Model

## Pattern Rule
**IF** you are tempted to make your code do something helpful or clever beyond what its names, types, and conventions advertise
**THEN** keep the behavior inside the mental model a caller builds from those cues, or make the extra behavior explicit and impossible to miss at the call site.

## Do
- Remember callers infer expected inputs, actions, and outputs from names, data types, and common conventions — behavior outside that model is a prime source of bugs.
- When a genuinely useful convenience falls outside the model (a dialer that redials the next restaurant when the line is busy), surface it explicitly — an audio prompt asking to be reconnected — instead of doing it silently.

## Don't
- Don't add hidden behavior that looks fine at the moment of the call but leaves the program in an invalid state or returns a weird value that surfaces far away, much later.
- Don't let good intentions excuse a surprise: the "clever" redial still delivered a margarita cocktail instead of a margherita pizza, and the mistake was discovered only when it was too late to fix.

## Checklist
- Would an engineer reading only the name and type signature correctly predict everything this code does?
- Is any behavior outside that expectation made explicit rather than silent?
- Could a surprising effect here manifest as a failure somewhere distant in the system?

## Notes
The dialer analogy is the anchor: we trust a mental model that says "if a voice answers, we reached the number we dialed," and the app quietly breaks it. In code, the caller builds an equivalent model from names, types, and conventions; violating it lets the program limp on until weird behavior manifests far from its cause. This is the "avoid surprises" pillar's foundation — chapter 6's techniques (magic values, side effects, mutating inputs) are specializations of keeping behavior inside the caller's model.
