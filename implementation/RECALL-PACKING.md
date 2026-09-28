# Count and byte limits form one recall-packing decision

[Implementation guide](README.md) · [Recall design](../design/FRAGMENT-RECALL.md) · [Recall acceptance](../evaluation/FRAGMENT-RECALL.md)

This clarification applies the existing bounded-context, permission, qualification
and resource requirements. It adds no task workflow, required provider, memory
category or requirement identifier. It is a design obligation, not evidence that
an implementation or live-model comparison has passed.

## A proposal is not an admitted candidate

Candidate discovery and remote packet admission have different bounds. Discovery
must inspect only a finite, authorized local set. The dispatch count limits the
candidates actually sent for assessment, subject also to the complete request's
byte and resource limits. It must not be confused with a prefix length applied
before candidate costs are known.

For example, with one dispatch slot, an oversized first proposal and a fitting
second proposal, the first proposal does not consume the slot. The runtime may
consider the second proposal within the same bounded discovery set. It does not
need another language-model call, an increased allowance or an automatic retry
to make that allocation decision. This does not require searching an unbounded
archive or guaranteeing a globally optimal combination.

Fit the shared situation and each candidate's complete required questions before
counting that candidate as admitted. A conditional route keeps its independent
situation and relevance judgments together; a direct relevance route need not
invent a conditional link. Preserve the established ordering unless an explicitly
described allocation policy says otherwise. Stop adding candidates when the
actual dispatch count is full. Count- and byte-excluded candidates are unassessed,
not rejected by the selector and not awaiting a promised later result.

## Boundaries remain independent

A candidate must pass current source and destination processing permissions
before its information reaches a remote provider. A smaller candidate is not
permission to disclose it. Searching further within the local bound does not
increase authorized remote count, bytes, tokens, attempts or spending.

Shared observations and complete candidate questions must not be silently
truncated to manufacture a fit. If the protected shared situation cannot fit,
or no whole eligible candidate fits, retain the declared fallback or explicit
block. Do not turn an optional size miss into a negative relevance judgment.

Assessment and full-fragment packing are separate steps. Selected methods still
need their exact complete corrections and prerequisites. Cache reuse and final
admission must still check meaningful input identity, current permissions and
source freshness. An allocation repair grants neither truth nor action authority.

## Acceptance must exercise the actual caller

A fitting helper tested with an already complete candidate list is insufficient.
Exercise the ordinary request compiler, preflight and dispatch boundary with an
oversized early candidate and a later fitting candidate under a small count
limit. Verify that a legal complete packet is admitted without exceeding any
bound, and that the resulting qualified context can pass ordinary admission.

Also exercise mixed one- and two-question routes, an unfit shared situation,
no fitting candidates, denied sources, exhausted attempt allowances, cache reuse
and meaningful changes after preparation. Verify exact questions and source
identity rather than only smaller serialized size. Synthetic judgments may
exercise mechanisms but must not be presented as observed model judgments or
live results.

Report structural checks, compiled mechanism tests and behavioral comparisons
separately. Reclaiming an unused packet slot may make a previously blocked
assessment possible, not make every request smaller. Useful efficiency still
requires matched outcomes and total primary, auxiliary, tool, failed and uncertain
usage. A run that never answers is not a cheaper equivalent answer.
