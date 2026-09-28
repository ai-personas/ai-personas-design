# Current-decision operation working set

[Implementation contracts](CONTRACTS.md) · [Useful-work evaluation](../evaluation/DECISION-REFERENCE-USABILITY.md)

## Purpose

This refines the existing context, resource and operation-usability obligations.
It introduces no new requirement identifiers, fixed workflow, task classifier or
compulsory persona phase. These are design obligations and proposed checks, not
claims of compiled implementation or measured product benefit.

Durable records and the vocabulary supplied to one decision have different
lifetimes. Retaining an observation is necessary for audit and future access;
it does not mean every operation associated with that observation belongs in
every future response contract. Conversely, a supplied successful observation
must not be treated as undiscovered merely because it arrived in a receipt
rather than a separately selected record.

## Keep follow-ups available while they are current

A launched operation may end its decision batch because the result must first
be observed. Make the relevant observation, cancellation and artifact contracts
available for that following decision without a contract-discovery-only turn.
The latest model batch must not age out merely because an operator polls the
system. A failed launch can still need inspection or correction.

A running or uncertain job remains a current concern across history compaction
and restart. Its observation and cancellation vocabulary must not disappear
because its launch receipt is outside a recent receipt page. Only authoritative
settlement can resolve its outstanding state; schema projection cannot do so.

For an older terminal job that is absent from current context and followed by a
newer model decision, archival existence alone must not permanently pin its
follow-up contracts. An explicitly supplied receipt can make it current again.
Persona-directed recent discovery or successful use may retain a bounded
working set independently. All other currently available commands remain
explicitly discoverable. Removing a response variant from a default working set
must not delete its archive, revoke authority or make the operation unknowable.

## Treat successful receipts as observations

When the current context already supplies a direct successful artifact record
from a read, publication or capture, offer the corresponding inspection
vocabulary. Do not require the persona to select the same record, re-read its
identity or spend another decision discovering how to inspect it. Existing
selected records and received attachment references remain valid inputs to
working-set construction.

Use typed result envelopes, not recursive searches through arbitrary authored
text or examples. Failed proposals, invalid identities, missing versions and
archived results not supplied in the current request are not equivalent to a
successful current observation. Metadata availability does not establish that
file bytes were inspected or that an artifact is correct.

## Preserve authority and evidence boundaries

The working set is a generation affordance, not an authorization decision.
Intersect loaded contracts with the currently offered operations, and preserve
invitation and recovery restrictions. Another actor or participation must not
pin job-control vocabulary as though it were the current persona's own job.

No operation is dispatched merely because its contract becomes available.
Current permissions, scope, exact versions, source restrictions, funding and
execution barriers continue to govern every action. Do not summarize away
unresolved outcomes, automatically replay effects, deliver private activity or
weaken dependent-delivery checks to claim lower resource use.

## Evaluation

Exercise the actual request compiler and provider-bound encoder. Compare a
fresh participation with one containing an old terminal launch but otherwise
identical current context. Separate the cost of contracts and their help from
observation content. Include a current visible failure, a latest launch followed
by heavy operator polling, an unresolved job after compaction and restart, a
settled former job, and another actor or participation. Verify that records and
accounting are unchanged and all currently available commands remain discoverable.

For successful artifact-bearing receipts, verify that inspection is expressible
in the next decision without selecting or discovering the same identity again.
Include failed and malformed receipts, nested artifact-shaped examples, removed
observations and narrowed operation availability. These checks must not perform
provider calls or create work merely to construct a catalog.

Report source checks, native tests, transport checks and live useful outcomes
separately. Fewer contracts or a smaller configured reservation bound do not
establish billed token savings or task success. A prospective matched evaluation
must include all primary and auxiliary decisions, discovery, retries, failures,
unknown exposure and latency, and must verify a useful delivered result. Do not
reopen or replenish a closed evaluation to demonstrate the new behavior.
