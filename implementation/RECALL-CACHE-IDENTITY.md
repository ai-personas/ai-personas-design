# Recall cache identity and useful-work continuity

[Recall design](../design/FRAGMENT-RECALL.md) · [Recall handoff](FRAGMENT-RECALL-CONTRACT.md) · [Acceptance](../evaluation/FRAGMENT-RECALL.md)

This clarifies the existing recall design's situation-digest cache rule and the
preservation of authored recall choices. It adds no model role, work phase,
permission, budget, or requirement identifier. These are implementation and
evaluation expectations, not reported product results.

## Separate three questions

**What was assessed?** Cache identity describes the exact approved selector input:
the current need, permitted observations, authored focus, candidate and condition
versions, question template, pinned model, owner, scope, and processing policy.
Changing a bookkeeping counter without changing that input is not new evidence.

**Where did it come from?** The assessment receipt keeps the exact source revisions
and provenance used when the assessment was made. A cache hit must not rewrite
that receipt to claim a new observation, current authorship, or another model call.

**May it be used now?** Current access, source withdrawal, expiry, cancellation,
participation, and admission checks still apply. Matching cached input is never
an authorization to disclose or act. Recheck the cached assessment's original
source ancestry as well as the new request's current sources.

## Preservation is not renewed authorization

Keeping an existing prospective recall choice is distinct from authoring a new
one. The no-change form of a next-context plan preserves the original source
versions, selection modes, count and byte ceilings, and expiry. It must not
require rediscovery of the same source cards in every primary decision merely
because optional previews or old read receipts have left the bounded context.
Otherwise reducing context creates a recurring evidence-repair cost, and an
unrelated valid handoff or dependent delivery can fail without new work evidence.

Preservation does not silently follow an edited source to its new version, renew
an expiry, restore a withdrawn source, or extend processing permission or funding.
A changed or unavailable optional source remains ineligible at use under its old
binding. An independent valid graph edit, including an edit to a delegated source,
need not reauthorize that binding merely to commit. The retained choice may
remain inactive until the persona explicitly replaces or disables it. Record
retention and source-disposition rules still govern what may remain stored.

A replacement choice still requires the currently received exact source versions
and all existing authorship checks. An explicitly authored same-transaction
handle can bind a committed new version under the existing local-reference
contract; preservation alone cannot do so. An explicit choice to remove the
delegation disables it rather than restoring the old one. Invalid stored bounds are not repaired or
expanded by a no-change choice.

This distinction covers prospective delegation and the dormant navigation
described below, not active payload validation. Full selected content, current self-fragments, mandatory qualifications, current work
and authority, source restrictions, and inference admission retain their existing
validation. Neither an old plan nor a cached result makes absent or revoked
content newly readable, received evidence, or permission to act.

## Dormant navigation is not an active read

A retained graph focus is a navigation pointer, not a request to include its
full fragment in every primary decision. Suspending optional previews may leave
that pointer without a current card. An unavailable focus may likewise cause
navigation to recover to discovery without changing the stored choice. Neither
condition should make an otherwise valid no-change handoff depend on another
browse call just to reauthorize the unchanged pointer.

Preserve the stored focus identity when the graph selection is unchanged. Do
not synthesize a received card, revive a retired node, select a fragment, claim
knowledge of its content, or change current source permissions. Subsequent
navigation and reads must still validate the current node and its information
rights. Invalid stored pointer syntax is not a valid historical choice and must
not be repaired silently.

A newly authored replacement focus still requires a currently received owned
node or an authorized local handle. Explicitly clearing focus clears it; it must
not restore the old pointer. Active full-fragment selections, graph edits and
required qualification bundles retain their own evidence, freshness and access
checks even when the same node is also a dormant focus. A failed edit must roll
back the entire handoff and continue to block any reply that depends on it.

This adds no lookup, automatic page, selector attempt, retry, prompt role or
funding. It separates preservation of optional navigation from authorization to
read or modify memory, rather than keeping more old cards in every request.

## Bounded view identity

When a selector is supplied only an authored focus from a mutable execution
record, a versioned identity of that exact focus view may be used for cache
matching. Only irrelevant changes to the containing record may be ignored.
Retain the owner's identity, scope, policy versions, and source dependencies.
A missing focus contributes no source merely because a containing record exists.

Do not generalize this into stripping revisions from arbitrary objects. A full
record explicitly supplied as an observation retains exact identity and version.
Historical source references, candidate descriptions, corrections, prerequisites,
and other evidence remain versioned. An unknown or extended view contract must
retain conservative dependencies until its projection is explicitly defined.
Changing the cache-identity contract creates a new cache domain rather than
silently certifying historical entries under different rules.

A changed focus, new observation, altered candidate or question, revoked source,
changed relevant processing policy, or unresolved model version prevents an
unjustified cache hit. An approximate semantic similarity is not exact reuse.

## A cache hit is not progress by itself

A completed unknown assessment remains unknown after reuse. It is not a pending
result, a successful match, or a reason to wait for another selector response.
The persona may choose an ordinary permitted read, revise its approach, deliver
what is supported, or explain a material missing input. This is not a forced
workflow and does not relax qualification or evidence rules.

Reusing an authorized completed assessment needs no new remote attempt. A real
cache miss still obeys the existing attempt ceiling and declared fallback.
Neither a cache miss nor a no-answer outcome authorizes extra funding, automatic
retries, or resumption of stopped work.

## Acceptance distinctions

A mechanism check should demonstrate that identical approved input survives
irrelevant execution-record revisions, including after the remote attempt
allowance is exhausted. It should show one retained assessment, unchanged
reported usage, no additional dispatch, and unchanged exact origin receipts.

Companion negative checks should change focus, candidate or policy versions,
withdraw an assessment or source, pause participation, and supply a full record
instead of its focus-only view. Reuse must not bypass the applicable invalidation
or authority check. Historical ancestry and unknown future view fields must not
be silently removed to obtain a hit.

Preservation checks should omit prior source cards from a new bounded request,
then commit an ordinary no-change handoff without rediscovery or an extra model
call. Exercise repeated decisions and restored durable state. Edit or retire a
delegated source and verify that preserving the plan neither blocks an independent
valid edit nor binds the old choice to the new source version. Expired plans must
remain expired. Explicit replacement must still reject unreceived or stale
sources; deliberate local-handle replacement and disabling must remain available.
Invalid graph edits must still roll back atomically, and selected or mandatory
source failures must not be ignored as optional-delegation failures.

Navigation checks should combine a retained non-active focus with suspended
previews and no previous browse receipt. Repeated no-change decisions must
preserve the pointer without adding its card, fragment or evidence alias. Repeat
with unavailable optional navigation. Explicit replacement without a received
card and unobserved edits must still fail; explicit clearing and an observed
valid edit must still work. Test an active selection of the same node separately
to ensure the navigation exception cannot bypass required full-context checks.

Delivery verification must exercise the real continuity-dependent reply path,
not merely the storage mutator. Preserve the dependency: failed changes cannot
produce a success confirmation. Report avoided rediscovery or repair decisions
separately from measured total tokens per correctly delivered result.

These checks do not establish persona usefulness. A separately authorized matched
work trial must still measure correct delivery, primary and auxiliary tokens,
failed and uncertain attempts, latency, and total resources per useful outcome.
Smaller packets, more cache hits, or fewer selector calls are intermediate
measurements, not substitutes for an answer the user can use.
