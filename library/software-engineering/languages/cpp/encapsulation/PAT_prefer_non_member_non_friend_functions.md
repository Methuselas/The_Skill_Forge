---
object_id: PAT_prefer_non_member_non_friend_functions
object_type: pattern
name: Prefer Non-member Non-friend Functions to Member Functions
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
- namespaces
- class_design
cross_links:
- rel: related_to
  target_object_id: PAT_expose_clean_api_hide_implementation
- rel: related_to
  target_object_id: PAT_declare_data_members_private
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u04, pp. 98-102
  evidence_type: text
confidence: high
references: []
variants: []
---

# Prefer Non-member Non-friend Functions to Member Functions

## Pattern Rule
**IF** a function can be written using only a class's public interface
**THEN** make it a non-member non-friend function rather than a member, because that increases encapsulation, packaging flexibility, and extensibility.

## Do
- Place such convenience functions in the same namespace as the class, spread across headers by topic, so clients depend only on the parts they use and can add their own.
- Count access: a non-member non-friend cannot touch private members, so it does not enlarge the set of functions that can — which is exactly what keeps the data encapsulated.

## Don't
- Don't reach for friend when a function should not be a member; a friend has the same private access as a member and the same encapsulation cost — the alternative to a member is a non-member, not a friend.

## Checklist
- Can this function do its job through the public interface alone, and if so is it a non-member?
- Is it in the class's namespace, grouped by topic across headers?
- Am I about to make it a friend when a plain non-member would do?

## Notes
Encapsulation is measured by how few functions can reach the private data; a member (or friend) adds to that count, a non-member non-friend does not — so `clearBrowser` encapsulates the `WebBrowser` better than a `clearEverything` member. Namespaces, unlike classes, span multiple headers, so convenience functions can be partitioned by topic (mirroring how the standard library splits its headers), letting clients depend only on what they use and extend the set freely.
