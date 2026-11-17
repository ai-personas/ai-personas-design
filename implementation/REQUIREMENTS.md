# Invariants and implementation traceability

[Guide](README.md) · [Human requirements](../USER-REQUIREMENTS.md) · [Contracts](CONTRACTS.md) · [Acceptance](../evaluation/ACCEPTANCE.md)

The existing **21 invariants and 45 implementation identifiers** are retained. Their character-related meaning is reconciled with the numerical-model clarification; historical fragment criteria do not silently pass the new target. Human requirements govern this catalogue, including removal of application quotas and approval gates.

![Human intent governs the design. Contracts preserve exact operations. Observations support scoped claims. A requirement identifier or a diagram is not an executed result.](../assets/sources.svg)

*Read the arrows as possible, recorded transitions—not promises that a result will improve.*

The diagram separates authority from evidence. A requirement explains what should happen; an observation explains what actually happened. Neither a source-code feature nor a completed document alone proves useful maturation.

## Invariants

| ID | What remains true |
|---|---|
| I01 | Preserve the original need, accepted changes, constraints and actual authority. |
| I02 | Identity continues across tasks and model revisions; every active characteristic package remains owner-bound. |
| I03 | No hidden profession registry, semantic task router, fixed team workflow, universal priority formula or population optimizer supplies the solution. |
| I04 | Preference, relationship interpretation, agreement, observed fact and actual authority remain distinct. |
| I05 | Responsibility exists after actual acceptance or an already accepted delegation, not after mention in a plan. |
| I06 | Creation preserves truthful origin; imported or generated knowledge is not invented firsthand experience. |
| I07 | Every adopted action binds actor, causal work, current decision, exact inputs and relevant model/evidence versions. |
| I08 | One persona has one current decision authority; independent personas and admitted isolated jobs may operate concurrently. |
| I09 | Current controls, obligations, blockers and necessary qualifications survive selection and summarization. |
| I10 | Tool availability, execution, artifact integrity and correctness require distinct evidence. |
| I11 | Review applies to exact inputs and criteria under the actual adopted policy; changes do not inherit a pass. |
| I12 | Retry does not duplicate accepted transitions; uncertain outside effects are reconciled before repetition. |
| I13 | Retrieval, import, creation and export preserve source attribution; metadata is not an application sharing gate. |
| I14 | Unseen images, unrun analyses, unperformed edits and unobserved measurements are not reported as completed. |
| I15 | Individuality, maturation, cooperation and useful expansion require behavioral evidence, not names, descriptions or counts. |
| I16 | Continuation follows actual chosen work or activity and honors stops and pauses; no exploration quota is imposed. |
| I17 | Pending effects do not satisfy completed dependencies; deferred old actions need fresh observation-bound decisions. |
| I18 | Unfinished accepted outcomes retain accepted follow-through or a visible ownership/handoff gap. |
| I19 | Evidence under an assumption cannot silently establish an unconditional real-world claim. |
| I20 | Review, repair, delivery and honest closeout remain available without application quotas; actual failures remain visible. |
| I21 | Final release coherently binds exact reviewed state and current authority; historical acceptance does not move to new results. |

## Implementation catalogue

These are responsibilities and evidence references, not a fixed production workflow, an application admission gate or an instruction to generate automated test cases. Applicability follows the actual feature and accepted need. Small work does not require a team or physical deployment simply because those cases appear here.

| ID | Required behavior | Authoritative home | Evidence |
|---|---|---|---|
| PER-01 | Continuing identity and model ownership; separate provider changes from numerical maturation. | [Persona core](../design/PERSONA-CORE.md) | B10 |
| PER-02 | Meaningful OCEAN/VAD starting account; distinguish stable tendencies, temporary appraisal, competence and responsibility. | [Persona core](../design/PERSONA-CORE.md) | B01–B03 |
| PER-03 | Current numerical character influences substantive decisions, with exact supply records and observed behavior. | [Persona core](../design/PERSONA-CORE.md) | B01–B04 |
| PER-04 | Explicit lifecycle changes preserve obligations and actual stopping state. | [Work](../design/WORK-AND-BOUNDARIES.md) | M19; M25; X02 |
| PER-05 | Attributed seed, own numerical candidate, observed adoption and first ordinary participation; retry-safe origins. | [Persona core](../design/PERSONA-CORE.md) | M05; M18 |
| MEM-01 | Separate numerical character from resources; every ordinary interaction covers work, both maintenance scopes and next state/context. | [Contracts](CONTRACTS.md) | M08; M15 |
| MEM-02 | Coherent model proposals and asset maintenance, with exact bases, intended destinations, discovery cues and actual outcomes. | [Context](../design/CONTEXT-AND-SKILLS.md) | M02; M11; M16 |
| MEM-03 | Persona-owned lexical/regex discovery and exact context selection; no full catalogue in the choosing model. | [Context](../design/CONTEXT-AND-SKILLS.md) | M08; M11 |
| MEM-04 | Faithful assembly of required current state, character and chosen support; explicit provider recovery instead of silent truncation. | [Contracts](CONTRACTS.md) | M08; M15 |
| MEM-05 | Connect lifetime experience, warranted numerical revision, later behavior and benefit; distinguish resource improvement, drift and missed transfer. | [Development](../design/CONTINUAL-DEVELOPMENT.md) | B03; B04; B07; B09 |
| NED-01 | Preserve the original need and authorized changes, rather than narrowing it to easier outputs. | [Work](../design/WORK-AND-BOUNDARIES.md) | M20; B11; B12 |
| NED-02 | Accepted continuation responsibility or an explicit ownership gap for unfinished required outcomes. | [Collaboration](../design/COLLABORATION.md) | M19 |
| NED-03 | Keep conditional assumptions separate from established facts and actual consent. | [Work](../design/WORK-AND-BOUNDARIES.md) | M20 |
| NED-04 | Judge coverage and usefulness against the actual need, including omissions from the persona’s own plan. | [Work](../design/WORK-AND-BOUNDARIES.md) | B05; B11; B12 |
| COL-01 | Individual agendas, unranked shared needs/offers and persona-chosen arrangements. | [Collaboration](../design/COLLABORATION.md) | B02; B08 |
| COL-02 | Separate invitations, membership, accepted responsibility and actual contribution. | [Collaboration](../design/COLLABORATION.md) | M06; M18 |
| COL-03 | Versioned adopted agreements, exact endorsements and retained dissent. | [Collaboration](../design/COLLABORATION.md) | B02; B05; X01 |
| COL-04 | Attributable handling of feedback and unresolved findings; copied criticism is not an automatic veto. | [Contracts](CONTRACTS.md) | M21; B05 |
| COL-05 | Provisional interfaces and persona-directed iteration with dependencies and uncertainty visible. | [Collaboration](../design/COLLABORATION.md) | M22 |
| COL-06 | Useful new persona creation or a choice not to create; truthful origin without population or birth quotas. | [Collaboration](../design/COLLABORATION.md) | M05–M07; B08 |
| ACT-01 | Distinguish discovery, reading, selection, exposure, invocation and observations without ceremonial extra calls. | [Context](../design/CONTEXT-AND-SKILLS.md) | M08; M10; M12 |
| ACT-02 | Exact actor/input/environment/result binding for host execution and installation; actual failure stays visible. | [Contracts](CONTRACTS.md) | M12 |
| ACT-03 | Complete valid decisions precede dispatch; actual prerequisites precede dependent decisions. | [Contracts](CONTRACTS.md) | M15; M17 |
| ACT-04 | Unknown outside effects remain explicit and are reconciled before repeat. | [Contracts](CONTRACTS.md) | M13 |
| GOV-01 | Actual authorship, destination/account, decision identity and acceptance; historical policies do not recreate application gates. | [Work](../design/WORK-AND-BOUNDARIES.md) | M03; M12 |
| GOV-02 | Full usage accounting including discovery, maintenance, assessment, failures, caches, archives and temporary copies; no quotas. | [Context](../design/CONTEXT-AND-SKILLS.md) | M07; M23 |
| GOV-03 | Usable repair, delivery and honest closeout without reserved-capacity gates; failures do not discharge duties. | [Work](../design/WORK-AND-BOUNDARIES.md) | M19; M23 |
| GOV-04 | Persona-chosen task, social and developmental continuation with explicit waits/stops and no forced-edit cadence. | [Development](../design/CONTINUAL-DEVELOPMENT.md) | M25; M26 |
| EVD-01 | Exact artifacts, dependencies, supply and execution evidence; selected content differs from actual exposure. | [Contracts](CONTRACTS.md) | M08–M10 |
| EVD-02 | Reviews identify exact scope, criteria, real reviewer and adopted independence. | [Work](../design/WORK-AND-BOUNDARIES.md) | B05; B11 |
| EVD-03 | Historical verdict and current applicability stay separate. | [Contracts](CONTRACTS.md) | M09 |
| EVD-04 | Coherent delivery of an exact state with remaining applicable findings and conditions visible. | [Contracts](CONTRACTS.md) | M21; M24 |
| EVD-05 | Report activity, coverage, evidence, acceptance and outside validation separately. | [Work](../design/WORK-AND-BOUNDARIES.md) | M14; B11; B12 |
| SYS-01 | Retry-safe invocation, maintenance, context and operation outcomes; no fabricated judgment after failure. | [Contracts](CONTRACTS.md) | M01–M04; M15 |
| SYS-02 | Recovery preserves events, obligations, warnings and effects without creating fresh authority from old identities. | [Contracts](CONTRACTS.md) | M04; M13; M16 |
| SYS-03 | Reject stale or invalid adoption; resolve numerical activation before new-model operations and invalidate old outputs across tasks. | [Contracts](CONTRACTS.md) | M02; M03; M17 |
| SYS-04 | Direct provider calls with explicit configuration and actual transport/usage; no silent fallback or uncertain tool replay. | [Contracts](CONTRACTS.md) | M07; M15; B10 |
| SOC-01 | Actually adopted institutions preserve real accountability without imposing a charter on ordinary cooperation. | [Collaboration](../design/COLLABORATION.md) | X01–X03 |
| SOC-02 | Distinguish real stakeholder input from simulated perspectives. | [Collaboration](../design/COLLABORATION.md) | X01 |
| SOC-03 | Local revisable relationship interpretations, distinct from truth, consent and competence. | [Collaboration](../design/COLLABORATION.md) | B02; B09 |
| UX-01 | Readable evidence-linked state and meaningful user controls; no false maturity badges. | [Work](../design/WORK-AND-BOUNDARIES.md) | M14 |
| UX-02 | Preserve attribution across records and derivatives; distinguish deletion, retirement and loss without retention quotas. | [Context](../design/CONTEXT-AND-SKILLS.md) | M11; M16; M23 |
| SRV-01 | Explicit ongoing triggers, observations, continuation and stopping; no claim of unobserved continuous service. | [Work](../design/WORK-AND-BOUNDARIES.md) | M25; M26; X04 |
| PHY-01 | Actual device interfaces, observations, commands and uncertain outcomes; digital work is not physical validation. | [Work](../design/WORK-AND-BOUNDARIES.md) | X05 |
| OSS-01 | Version design, evaluation and claims; preserve failures and source lineage without publishing private live records. | [Sources](../sources/SOURCE-MANIFEST.md) | X06 |

## Meaning of conformance

For each applicable responsibility, identify documented design coverage, inspected or observed mechanism, actual behavioral evidence and the deployment’s remaining gaps separately. Missing evidence is unassessed, never passed. “Not applicable” must not be used to remove a required part of the user’s objective.

Model creation, numerical revision, changed function, actual supply, changed behavior, useful outcome and retained transfer are separate claims. MEM-05 and PER-03 cover the full development relationship; they are not satisfied by a reflection log or weight-update count.

The [human requirement map](../examples/REQUIREMENTS-WALKTHROUGH.md) accounts for all 46 active human IDs and the eight retired IDs. The [historical ledger](../evaluation/HISTORICAL-RESULTS.md) preserves changed criteria and earlier results.
