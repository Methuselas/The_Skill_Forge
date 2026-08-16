---
object_id: PAT_access_templatized_base_members_explicitly
object_type: pattern
name: Access Templatized Base Class Members Explicitly
library_path:
- software-engineering
- languages
- cpp
- templates
stage_binding: 3 rough
lane_fit: both
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
  target_object_id: PAT_unhide_inherited_names_with_using
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Access Templatized Base Class Members Explicitly

## Pattern Rule
**IF** a class template derives from a base class template and calls a name it inherits
**THEN** tell the compiler to look in the base — with a this-> prefix, a using declaration, or explicit base-class qualification — because it will not search a templatized base by default.

## Do
- Prefix the inherited call with this-> (this->sendClear(info)) to promise the name is inherited.
- Or add a using declaration bringing the base name into the derived scope, or qualify the call with the base class name.

## Don't
- Don't call the inherited name unqualified; the compiler refuses to search the templatized base, because a specialization of that base (like one for CompanyZ) might not offer the name at all.
- Don't use explicit base-class qualification when the function is virtual — qualifying turns off virtual dispatch; prefer this-> or a using declaration.

## Checklist
- Does a derived class template call a base-class-template name unqualified?
- Have I enabled the lookup with this->, a using declaration, or base qualification?
- If the inherited function is virtual, did I avoid explicit qualification that would disable dispatch?

## Notes
When the base is a template (MsgSender parameterized on Company), the compiler will not assume it offers sendClear, because a specialization such as the one for CompanyZ may omit it — so it refuses to look there, and inheritance seems to stop working across the Object-Oriented-to-Template C++ boundary. All three fixes promise that the name is inherited; C++ prefers this early diagnosis, catching an unfounded promise later when the template is instantiated. Explicit qualification is the weakest fix because it suppresses virtual dispatch.
