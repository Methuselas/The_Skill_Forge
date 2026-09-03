---
object_id: DRILL_fix_templatized_base_class_name_access
object_type: drill
name: Fix Access to a Name in a Templatized Base Class
target_skill: Enabling name lookup into a templatized base with this->, using, or qualification
library_path:
- software-engineering
- languages
- cpp
- templates
stage_binding: 3 rough
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- templates
- inheritance
- name_lookup
cross_links:
- rel: related_to
  target_object_id: PAT_access_templatized_base_members_explicitly
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Fix Access to a Name in a Templatized Base Class

## Practice Task
Given a derived class template (a LoggingMsgSender) that calls an inherited function (sendClear) from its base class template (MsgSender) and won't compile, make it compile three different ways.

## Target Skill
Turning on the compiler's search of a templatized base class for an inherited name.

## Setup
No special setup required.

## Instructions
- Reproduce the failure: an unqualified call to the inherited function does not compile, because the compiler won't search the templatized base. Record the compiler's message.
- Fix it with a this-> prefix on the call, and compile it.
- Fix it again with a using declaration bringing the base name into the derived scope, and compile it.
- Fix it a third time with explicit base-class qualification, compile it, and state why that is worst when the function is virtual, since it turns off the dispatch.
- Compile a base specialization that omits the name, and show the error arriving at instantiation rather than at definition.
- Rank the three fixes with the condition that selects each.

## Success Check
- The failure is reproduced first and the compiler's message recorded, because that message is what a reader actually meets and it does not plainly describe the cause.
- All three fixes are compiled rather than one compiled and two described.
- A base specialization omitting the name is compiled too, and the error is shown arriving at instantiation rather than at definition. That timing is the substance of the exercise.
- The run states why explicit qualification is the worst of the three for a virtual function, since it turns off the dispatch, rather than listing it as a third option of equal standing.
- The three are ranked with the condition that selects each, so the run ends in a choice rather than an inventory.

## Common Failures
- Leaving the call unqualified and expecting inheritance to just work across the template boundary.
- Using explicit qualification on a virtual function and silently disabling virtual dispatch.

## Notes
This drills Item 43: all three fixes promise the name is inherited; C++ diagnoses an unfounded promise later, when the template is instantiated with a base specialization that lacks it.
