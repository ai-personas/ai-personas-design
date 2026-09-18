# Implementing the design without prescribing code

[Home](../README.md) · [Design chapters](../design/README.md) · [Glossary](../GLOSSARY.md)

This section is a behavioral implementation brief. It specifies responsibilities, required information, handoffs, state transitions, failure behavior, and evidence. It deliberately does not prescribe a programming language, database layout, wire format, provider, or deployment stack.

An implementer should be able to decide what to build and what must be demonstrated using this repository alone. Choosing and verifying a concrete technology or a domain method remains implementation work, not a missing conversation to recover.

## Reading and build sequence

| Step | Read | Produce before advancing |
|---|---|---|
| Understand the product | [Start here](../START-HERE.md) and [design chapters](../design/README.md) | A shared account of purpose, limits, and supported user needs. |
| Establish the boundaries | [Invariants and requirements](REQUIREMENTS.md) | A requirement-to-component responsibility map with no unowned enforcement boundary. |
| Define the handoffs | [Contracts](CONTRACTS.md) | Record meanings, state transitions, concurrency rules, and recovery behavior in the chosen implementation. |
| Choose the deployment | [Deployment decisions](DEPLOYMENT-DECISIONS.md) | Explicit authority, resource, inference, retention, review, and unsupported-feature decisions. |
| Prove reliability | [Mechanical acceptance scenarios](../evaluation/ACCEPTANCE.md#mechanical-checks) | Evidence for applicable boundaries before autonomous effects are enabled. |
| Demonstrate useful behavior | [Behavioral acceptance scenarios](../evaluation/ACCEPTANCE.md#behavioral-checks) | Real outcomes and matched comparisons, preserving failures and limitations. |
| Make a scoped release | [Evidence reporting](../evaluation/README.md#reporting-a-result) | Exact configuration, demonstrated scope, pending checks, and a truthful public claim. |

## Start small, but keep the safeguards

The first useful system can be one continuing persona that accepts a bounded request, receives relevant context, produces an authorized result, preserves evidence, reaches an honest disposition, and continues to a second task. It does not need a city of personas, a role engine, or a population optimizer.

Next demonstrate a genuine peer-finding-to-edit-to-check chain. Then test changed-input adaptation, retained learning, recruitment, and optional birth. Only after those boundaries and behaviors have evidence should a deployment expand to complex community or physical features.

| Milestone | Exit evidence |
|---|---|
| Reliable foundation | Applicable tests of authority, reservations, delivery, versions, recovery, and execution isolation. |
| One continuing collaborator | A real small outcome, honest status, identity continuity, and no unnecessary idle activity. |
| Cooperative group | Accepted responsibilities, distinct relevant contexts, and actual evidence-led correction. |
| Adaptation and learning | Comparable retained-versus-withheld evidence, changed-input response, and useful expansion or restraint. |
| Complex and unrelated work | Coordinated outputs plus different small and substantial needs using the same contracts. |
| Publicly claimed capability | A reproducible evidence package with limitations tied to exact versions. |

These are evidence gates, not a delivery calendar. A failed gate should identify a missing affordance, capability, or unclear requirement rather than automatically adding more personas.

## Conformance profiles

A **persistent collaborator** supports bounded work, identity, memory, and applicable safeguards. A **cooperative group** adds accepted shared work and demonstrated correction. An **adaptive community** adds bounded recruitment or birth, governance, and accountable ongoing work. A **physical-enabled deployment** adds a specifically assessed device and environment contract.

Profiles inherit applicable lower-level requirements. A disabled feature is explicitly unavailable; an empty control or untested record does not count as implementation. No profile implies universal expertise, human-like psychology, guaranteed learning, or global cross-host identity exclusivity.

## Translating the design into a concrete system

Assign one authoritative boundary for each consequential state change. Records can share infrastructure; there need not be one service per noun. Keep persona judgment separate from authentication, execution scheduling, and evidence integrity.

For every operation, document who may request it, what information is required, which state changes together, what happens under a duplicate or stale request, how cancellation works, what survives restart, and what the user sees. The [contracts](CONTRACTS.md) provide these semantic obligations without code examples.

Record implementation-specific decisions outside this design handbook or in a clearly separate implementation repository. Do not reintroduce patch instructions, command transcripts, or unverified provider claims as the design's source of truth.
