---
object_id: PAT_declare_data_members_private
object_type: pattern
name: Declare Data Members private
library_path:
- software-engineering
- languages
- cpp
- encapsulation
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- encapsulation
- access_control
- class_design
cross_links:
- rel: related_to
  target_object_id: PAT_encapsulate_related_data_together
- rel: related_to
  target_object_id: PAT_prefer_non_member_non_friend_functions
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u04, pp. 94-98
  evidence_type: text
confidence: high
references: []
variants: []
---

# Declare Data Members private

## Pattern Rule
**IF** you are choosing the access level of a class's data members
**THEN** declare them private and expose access only through member functions, because private is the only level that actually encapsulates.

## Do
- Route all data access through functions, so clients use one uniform syntax and you can grant no access, read-only, or read-write access per member.
- Keep the freedom to replace a stored member with a computed value later without breaking clients, since they only ever call a function.

## Don't
- Don't make data members public: everyone gets read-write access, invariants cannot be enforced, and any later change breaks an unknowable amount of client code.
- Don't assume protected is safer than public; removing a protected member breaks all derived classes, so it is no more encapsulated than public.

## Checklist
- Are all data members private, reached only through functions?
- Could I change a member's representation or compute it later without breaking clients?
- Am I treating protected as encapsulated when it is not?

## Notes
Functional access buys syntactic consistency (everything is a call), fine-grained control (the `AccessLevels` read-only/write-only mix), and — most importantly — encapsulation: `averageSoFar` can switch between a stored running average and an on-demand computation with clients none the wiser. Public means unencapsulated, and unencapsulated means unchangeable. Protected offers no relief, because removing a protected member breaks an unknowable amount of derived-class code; from an encapsulation standpoint there are only private and everything else.
