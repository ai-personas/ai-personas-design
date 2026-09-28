# Decision-reference usability and useful-work cost

[Evaluation guide](README.md) · [Recall acceptance](FRAGMENT-RECALL.md) · [Authoring handoff](../implementation/FRAGMENT-RECALL-CONTRACT.md)

## Status and purpose

This refines existing evidence, memory, usability and resource requirements. It
adds no requirement identifiers, mandatory workflow or generative reviewer.
These are design obligations and proposed checks, not reported runtime passes or
measured product benefits. No private implementation or trial evidence is part
of this document.

A response can be valid JSON yet mechanically impossible to commit. When the
runtime already knows the reference kind and required revision semantics, merely
describing those rules in prose leaves avoidable generation errors available.
Atomic rollback protects the records but cannot recover the model resources
already consumed. Useful-work efficiency therefore includes preventable failed
transactions, not only the size of an individual prompt.

## Generation and admission must agree

Expose complete copyable references, distinguishing ordinary versioned records,
settled action receipts and memory-navigation handles. An ordinal in a convenience
handle is not a record revision. A receipt's revision-free identity is not a
versioned record, and a navigation card is not evidence of its unread content.

Where supported by the transport, express mechanically known kind/revision and
field-domain constraints in the generated response contract. Keep dependent
choices coupled; independent lists of identifiers and revisions must not permit
invalid cross-pairings. Do not require another model call to rediscover rules
already known at compilation. Describe any transport that can only present an
inner contract as instructions rather than enforce its structure.

This does not permit a runtime to silently repair a wrong reference, substitute a
newer version, invent a receipt digest, broaden processing permission or adopt
an unobserved result. Current-call scope, exact positive revisions, ownership,
source access, receipt settlement, freshness and source restrictions are still
checked at admission. Syntactic restrictions are not evidence validation.

Keep unchanged server interfaces and persisted historical proposals distinct
from a narrower provider-facing generation view. A projection must preserve all
other constraints, apply only at recognized schema positions, remain bounded,
and disclose unsupported representations instead of guessing. Any sharing of
repeated structures must remain lossless after the deliberate refinement.

## Supplemental checks under existing recall scenarios

Extend the atomic-update, exact-context and bounded-cost scenarios with a valid
versioned observation, a valid settled receipt, the wrong reference kind, a
zero or wrong positive record revision, a missing receipt digest, a foreign or
expired handle, and a navigation-only card. Validate tentative no-source learning
and explicit no-change alongside sourced learning; successful retention is not
mandatory on every response.

Check the actual generated transport contract, not just a separately maintained
schema fixture. Verify that allowed forms still work and impossible forms are
excluded wherever the transport supports that guarantee. Verify admission
independently so a manually supplied or nonconforming response cannot bypass the
same guards. Repeat through different decision modes and after lossless sharing.
An unrelated reference type, arbitrary example, annotation or property name must
not be rewritten accidentally. A generic API or storage format must not change
as an unintended consequence of a provider-only refinement.

Retain failures, exact retries, rollback and dependent-delivery behavior. A
failed learning transaction must not produce a successful retention confirmation.
Do not reopen a closed evaluation, manufacture evidence or replenish its budget
to make a new implementation appear to have passed the original case.

## Outcome and economics gate

Report mechanical schema checks, compiled tests, real transport checks and live
useful outcomes separately, with exact revisions and limits. A regex fixture,
parser test or successful documentation build proves none of the later stages.

For prospective matched tasks, measure the delivered artifact or answer and the
retained, qualified learning that was actually needed. Count all primary and
auxiliary input/output, reported reasoning, discovery, unsuccessful attempts,
retries, unknown exposure and latency. A refinement may add schema bytes while
reducing failed work; that tradeoff needs whole-task measurements. Conversely,
shorter individual calls that require more calls or never deliver usable work
must not be reported as an efficiency improvement.

Character influence, qualified transfer and useful collaboration still need
their existing controlled comparisons. Neither more fragments nor fewer invalid
references establishes those benefits by itself.
