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
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u07, pp. 207-212
  evidence_type: text
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
- Reproduce the failure: an unqualified call to the inherited function does not compile, because the compiler won't search the templatized base.
- Fix it with a this-> prefix on the call.
- Fix it again with a using declaration bringing the base name into the derived scope.
- Fix it a third time with explicit base-class qualification, and note why that is worst when the function is virtual.

## Success Check
- Each of the three forms compiles for a base specialization that provides the name.
- A base specialization that omits the name still fails to compile, at instantiation, as expected.

## Common Failures
- Leaving the call unqualified and expecting inheritance to just work across the template boundary.
- Using explicit qualification on a virtual function and silently disabling virtual dispatch.

## Notes
This drills Item 43: all three fixes promise the name is inherited; C++ diagnoses an unfounded promise later, when the template is instantiated with a base specialization that lacks it.
