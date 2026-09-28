# Recall cache identity and useful-work continuity

[Recall design](../design/FRAGMENT-RECALL.md) · [Recall handoff](FRAGMENT-RECALL-CONTRACT.md) · [Acceptance](../evaluation/FRAGMENT-RECALL.md)

This clarifies the existing recall design's situation-digest cache rule. It adds
no model role, work phase, permission, budget, or requirement identifier. These
are implementation and evaluation expectations, not reported product results.

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

These checks do not establish persona usefulness. A separately authorized matched
work trial must still measure correct delivery, primary and auxiliary tokens,
failed and uncertain attempts, latency, and total resources per useful outcome.
Smaller packets, more cache hits, or fewer selector calls are intermediate
measurements, not substitutes for an answer the user can use.
