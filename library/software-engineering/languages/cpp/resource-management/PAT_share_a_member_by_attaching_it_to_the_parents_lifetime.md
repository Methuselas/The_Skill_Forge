---
object_id: PAT_share_a_member_by_attaching_it_to_the_parents_lifetime
object_type: pattern
name: Share a Member by Attaching It to the Parent's Lifetime
library_path:
- software-engineering
- languages
- cpp
- resource-management
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- ownership
- lifetime
- shared_ownership
cross_links:
- rel: related_to
  target_object_id: PAT_price_shared_ownership_before_choosing_it
- rel: related_to
  target_object_id: PAT_keep_a_non_owning_view_within_the_lifetime_of_what_it_views
- rel: related_to
  target_object_id: PAT_provide_access_to_raw_resource_in_raii_class
- rel: related_to
  target_object_id: PAT_manage_resources_with_raii_objects
reference:
  source_title: 'C++20 STL Cookbook: Leverage the latest features of the STL to solve real-world problems'
  author: Bill Weinman
confidence: high
references: []
variants: []
---

# Share a Member by Attaching It to the Parent's Lifetime

## Pattern Rule
**IF** a part of a shared-owned object must be handed out on its own, and the recipient may keep it after every obvious reference to the whole object is gone
**THEN** hand out a shared pointer that addresses the part while participating in the whole object's ownership, so holding the part keeps the parent alive
**ELSE** where the recipient provably finishes with the part before the parent's owner does, an ordinary reference or pointer to the member is simpler and costs nothing.

## Do
- Recognise the shape before reaching for the mechanism. Something owns a composite; a caller wants one field of it; the caller's use may outlast the scope that held the composite. Handing back a plain pointer to the field makes the caller responsible for a lifetime it cannot see, and handing back a copy of the field may be expensive or may not be what was wanted.
- Construct the part's pointer from the parent's, so the two share one reference count and one deleter while addressing different things. The count rises because the part is held, and the parent is destroyed only when every handle to it and to any of its parts is gone.
- Read the consequence at the call site, which is the point of the whole arrangement. A function can create a composite, return handles to two of its members, let its own handle to the composite go out of scope, and the composite survives — because the returned handles are participating in its ownership even though neither of them names it.
- Keep the part's pointer honest about what it addresses. It reports the part when dereferenced and the part's address when asked, so nothing at the point of use suggests a larger object is being kept alive; that fact belongs in a comment or a name where the handle is produced.
- Prefer this to widening the interface. The alternative that suggests itself is to hand out the whole composite and let the caller reach in, which gives the caller access to everything in order to grant access to one thing.

## Don't
- Don't reach for it where a plain reference would do. It buys shared ownership, and shared ownership has a price that should be paid deliberately rather than as the default answer to a lifetime question.
- Don't use it to keep a large object alive for the sake of a small field. The parent is retained in full, so a handle to one small member of an expensive composite pins the whole of it, and a copy of the field would have released the rest.
- Don't assume the arrangement is visible to whoever holds the handle. Nothing about the part's pointer shows that a parent exists, so a reader tracing why an expensive object has not been destroyed will not find the reason at any of the places still holding it.

## Checklist
- Does the recipient of this part outlive the scope that owns the composite?
- Would a plain reference to the member be provably safe here? If so, why is more needed?
- Is the whole parent being retained for the sake of a field small enough to copy?
- Is it written down anywhere that holding this handle keeps a larger object alive?

## Notes
This is the owning counterpart to the non-owning view, and the two answer the same question in opposite directions. A view over part of an object is cheap and imposes a rule the compiler will not enforce, namely that the view must not outlive its subject. This arrangement removes the rule by making the reference participate in ownership, and pays for it in the price of shared ownership and in retaining the parent for as long as any part is held. Which is right depends on whether the lifetime relationship is visible and short, or invisible and open-ended.

The property that makes it work is worth stating on its own, because it is not the obvious behaviour of a smart pointer. The handle separates two things a pointer normally keeps together: what is addressed, and what is kept alive. Everything else about the ownership machinery — the count, the deleter, the moment of destruction — belongs to the parent; only the address belongs to the part. That separation is the whole mechanism, and once seen it explains the otherwise surprising fact that destroying the last handle *to the composite* destroys nothing at all.
