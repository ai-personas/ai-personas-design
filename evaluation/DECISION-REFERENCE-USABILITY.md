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

## Discovery has one lifecycle across the whole request

A bounded active capability set is not a bounded request when retired contracts
continue to travel through historical discovery results. Evaluate instructions,
response contracts, ordinary history, explicitly selected receipts and recovery
indexes together. A contract leaving the active set must not implicitly impose
permanent repeated full-help overhead through another context channel.

Keep newly acquired calling instructions usable for the following decision,
including a batch larger than the ordinary recent-history window. Operator
inspection and polling are not new persona decisions. Preserve current repair
instructions and full help for active capabilities. A still-discoverable retired
contract may instead have a bounded recovery entry with its operation name and
exact archived receipt reference. Reading that receipt is not repeating an
outside effect. Historical help never restores withdrawn authority.

Only a recognized, settled discovery result may receive this treatment. An
arbitrary record resembling a schema, a changed historical contract, an extended
result carrying an adverse observation, a failed or unfinished action, unread
input or explicit evidence selection must not be silently discarded. Schema
argument names such as state, error and verdict are not themselves observations;
that distinction requires validated provenance and content, not a global
exception to failure protection. Durable receipts remain intact.

Test the complete fresh-discovery batch, later eviction, operator polling,
rediscovery, restart, permission changes, selected and unread help, malformed
results, and exact archive recovery. Compare the real provider-bound views with
all replacement indexes and instructions included. When both views fit, retain
the original if projection would increase its quoted input exposure. A smaller
serialized journal alone is not evidence of a smaller encoded request, measured
token savings or better task performance.

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

For disabled or terminally unavailable auxiliary recall, verify useful ordinary
reads or explicit qualified selection, or an actually delivered limitation when
progress is blocked. An unchanged delegation is not a pending selector call.
Successful internal updates followed by silence do not pass a delivery scenario.
A warning explaining unavailability is necessary but is not behavioral evidence
that the persona uses the available alternative. Do not manufacture a semantic
match, force a particular memory choice, silently resume an explicit wait, or
spend extra inference to make this check pass.

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
