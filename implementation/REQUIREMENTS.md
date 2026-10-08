# Invariants and requirement traceability

[Implementation guide](README.md) · [Contracts](CONTRACTS.md) · [Acceptance](../evaluation/ACCEPTANCE.md)

The protected foundation remains I01–I21 and the 45 requirement identifiers below. The current [persona core](../design/PERSONA-CORE.md) defines the persona as the continuing whole of characteristic context, LLM reasoning and invocation, actual behavior, and controlled self-revision. One coherent OCEAN- and VAD-grounded character account and selected own-voice prompt parts form its characteristic context. Fragments are persona-defining parts, not a memory store attached to the LLM. The LLM is the reasoning substrate, with learned capabilities and priors that also affect behavior. Actual human, peer, and task experience can reshape fragments, later choices and relationships, and permitted character development. Every persona invocation receives maintenance input and returns an explicit outcome alongside actual work before its response can be adopted. [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) preserves authority, obligations, supporting evidence, resources, and recovery. The index names design obligations; it does not replace their failure paths or provide implementation code.

This revision clarifies what constitutes the persona and its prompt parts, with continuing character, invocation, navigation, and compact-retention obligations; it does not rewrite earlier results. The previous optional-OCEAN/VAD and omitted-maintenance norms are superseded: the characteristic basis and explicit maintenance outcome are required, while numeric scores, fixed cognitive forms and actual mutation on every call are not. Bounded listing, literal or regex search, simple owner-authored indexes and cues, and exact reads let the persona form its next characteristic context. The primary persona reformulates queries and selects prompt parts; auxiliary semantic, vector, and graph-retrieval engines are different research comparators, not optional production paths. Their historical criteria remain identifiable in the [transition mapping](../evaluation/HISTORICAL-RESULTS.md). Existing identifiers, including MEM-01–MEM-05, are retained for traceability rather than as a claim that fragments are recall memory. Their subjects now explicitly distinguish persona-defining context from supporting records. Earlier passes do not establish these clarified criteria, and no scenario is reported as executed merely because its description exists.

## Invariants

| ID | Rule that must remain true |
|---|---|
| I01 | Preserve the exact original request, accepted changes, constraints, and their authority. |
| I02 | Persona identity continues independently of model, project, and temporary responsibility. |
| I03 | No hidden profession registry, semantic task router, universal priority formula, fixed domain workflow, or population optimizer chooses the solution. |
| I04 | Preference, relationship interpretation, group agreement, observed fact, and permission remain distinct. |
| I05 | Responsibility exists only after acceptance or an already accepted delegation; mentioning a peer does not commit it. |
| I06 | Birth creates neither money nor broader permission, and supplied knowledge is not invented firsthand experience. |
| I07 | Every admitted action is attributable to its actor, causal work, authority, exact request, and relevant information versions. |
| I08 | One persona has one current decision authority at a time; independent personas and isolated jobs may work concurrently. |
| I09 | Relevant mandatory constraints, cancellations, current obligations, and blockers survive context selection and summarization. |
| I10 | Tool availability, execution, artifact integrity, and result correctness require different evidence. |
| I11 | Review applies to exact criteria and inputs under an explicit policy; changed inputs do not silently inherit a pass. |
| I12 | Local retries do not duplicate accepted transitions; uncertain outside effects are reconciled before repetition. |
| I13 | Retrieval, summaries, birth, exports, and interfaces cannot widen access to private information. |
| I14 | Unseen images, unrun analyses, unperformed edits, and unobserved measurements are never reported as completed. |
| I15 | Individuality, learning, cooperation, and useful birth require behavioral evidence rather than biographies or counts. |
| I16 | Idle personas consume no model calls without an authorized stimulus, self-wake, or bounded exploration allowance. |
| I17 | Running tools do not satisfy completed dependencies; deferred actions from an old decision require a fresh observation-bound decision. |
| I18 | Accepted work has accepted continuation responsibility or an explicit unowned or handoff-needed disposition; required outcomes expose gaps. |
| I19 | Evidence based on an assumption cannot silently establish an unconditional real-world claim. |
| I20 | Agreed review, repair, and safe closeout capacity is protected from ordinary exploration unless explicitly reallocated. |
| I21 | Final release binds exact reviewed state and current authority coherently; historical acceptance never silently moves to a newer result. |

## Requirement catalogue

M, B, and X refer to the [mechanical, behavioral, and extension checks](../evaluation/ACCEPTANCE.md). Applicability depends on the actual enabled effect or feature. Small work does not acquire an artificial team, formal package, or physical deployment merely because those cases exist in the catalogue.

| ID | Required behavior | Detailed design | Primary evidence gates |
|---|---|---|---|
| PER-01 | Preserve continuing identity across model and work changes while treating context, invocation, behavior, and self-revision as the operating persona; continuity does not guarantee unchanged behavior or competence on a different reasoning substrate. | [Persona core](../design/PERSONA-CORE.md) | B10; restoration evidence |
| PER-02 | Ground one coherent character account in OCEAN tendencies, VAD modeled affect, and useful additional characteristics; distinguish stable character, transient state, preference, competence, authority, and responsibility. | [Persona core](../design/PERSONA-CORE.md) | B01–B04; capability evidence |
| PER-03 | Form each invocation's characteristic context from accepted character and relevant persona-selected prompt parts; they help constitute discretionary communication, collaboration, navigation and work, with own-voice perspective and no invented biography or altered evidence. Actual behavior still needs observation. | [Persona core](../design/PERSONA-CORE.md) | B01–B04; B07; B09–B10 |
| PER-04 | Make lifecycle changes and open-obligation dispositions explicit. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M06; X02 |
| PER-05 | Require truthful creation provenance and bounded initialization. | [Persona core](../design/PERSONA-CORE.md) | M05; M18 |
| MEM-01 | Distinguish persona-defining prompt parts from supporting work facts, observations, and operational records, without a rigid taxonomy; every persona invocation explicitly considers maintenance of its authored context. | [Persona core](../design/PERSONA-CORE.md#fragments-are-reusable-prompt-parts) and [contracts](CONTRACTS.md#every-persona-invocation) | M08–M10; B09 |
| MEM-02 | Maintain a useful, consistent, compact corpus of persona-defining prompt parts and cues; preserve characteristic meaning, restrictions, scope, counterevidence, permitted provenance, qualifications, warnings, and actual edit or bounded no_change, blocked, or deferred dispositions through revision, pruning, consolidation, and policy-governed retention. | [Persona core](../design/PERSONA-CORE.md#maintenance-correction-and-continuity) and [contracts](CONTRACTS.md#every-persona-invocation) | M08; M11; M16; M21; M23; B09 |
| MEM-03 | Let the primary persona navigate bounded file-search cues and choose exact next-context fragments; dynamic matches remain candidates, associative cues differ from exact references and mandatory qualifications, and cumulative traversal, fanout, reads, context and cost remain bounded. | [Persona core](../design/PERSONA-CORE.md#bounded-navigation-and-revisable-cues) and [contracts](CONTRACTS.md#search-and-exact-reading) | M08; M11; M23; B09 |
| MEM-04 | Preserve mandatory current constraints under context pressure. | [Persona core](../design/PERSONA-CORE.md) | M08; M21 |
| MEM-05 | Measure reciprocal experience-shaped development of characteristic context and behavior, qualified transfer, correction, navigation quality, harmful drift, and total maintenance and persona-state cost; recall scores, calendar age, storage growth, accepted edits, or praise do not establish the intended persona or improvement. | [Persona core](../design/PERSONA-CORE.md) | B01–B04; B07; B09–B10 |
| NED-01 | Preserve original intent and authorized mandate changes. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M20; B11–B12 |
| NED-02 | Obtain continuation acceptance and expose ownership gaps. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M19 |
| NED-03 | Distinguish conditional assumptions from confirmed facts. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M20 |
| NED-04 | Check scope coverage against the original need. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | B11–B12; omitted-outcome fixture |
| COL-01 | Preserve individual agendas, an unranked shared board, and accepted commitments. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | B01–B04 |
| COL-02 | Separate offers, membership, responsibility, and actual contribution. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M06; M18–M19 |
| COL-03 | Preserve exact agreement endorsements and dissent. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | B02–B03; X01 |
| COL-04 | Resolve consequential feedback through explicit dispositions. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M21; B05 |
| COL-05 | Support provisional interfaces and bounded iteration. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M22 |
| COL-06 | Permit useful birth and no-birth restraint under conserved resources. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M05–M07; B08 |
| ACT-01 | Use or acquire capabilities through actual evidence-backed operations. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M10; B11–B12 |
| ACT-02 | Enforce execution boundaries rather than merely label them. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M12 |
| ACT-03 | Require a complete valid persona response before new action adoption, and actual prerequisite results before dependent decisions and publication. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) and [contracts](CONTRACTS.md#every-persona-invocation) | M17; M26 |
| ACT-04 | Preserve unknown external effects and reconcile before repetition. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M13 |
| GOV-01 | Keep grants scoped, revocable, and no broader than their parents. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M05–M07; M11–M13 |
| GOV-02 | Conserve resources across descendants, every-call maintenance, navigation, provider attempts, retries, compaction, and review; bound the persona-context corpus, assembled prompt and total managed persona-state footprint, including supporting records, archives, versions, ancestry, qualifications, warnings, caches, external backing, and peak rewrite copies. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md#resource-conservation-and-protected-closeout) and [contracts](CONTRACTS.md#authority-resources-and-stopping) | M07; M23; B09 |
| GOV-03 | Protect agreed closeout capacity. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M23 |
| GOV-04 | Bound idle cognition, reminders, maintenance deferrals, and no-progress loops; an outcome creates no automatic reflection call or self-wake. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M25 |
| EVD-01 | Preserve exact artifacts, input mappings, and actual execution evidence. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M09–M10 |
| EVD-02 | Review exact scope under an explicit independence policy. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | B05; B11 |
| EVD-03 | Separate historical verdict from current applicability. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M09; M24 |
| EVD-04 | Seal one coherent reviewed state with no unresolved applicable blockers. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M21; M24 |
| EVD-05 | Expose activity, coverage, evidence, acceptance, and outside validation separately. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M14; B11–B12 |
| SYS-01 | Make invocation, maintenance and operation dispositions retry-safe and attributable; never invent persona outcomes for failed, refused or canceled calls. | [Contracts](CONTRACTS.md) | M01–M04; M13 |
| SYS-02 | Restore pending events, maintenance dispositions, adopted deferrals, continuing accepted warnings, reservations, and effects without new authority; expired or unknown old action and invocation identities never become fresh unsent work or replay authority. | [Contracts](CONTRACTS.md#recovery-privacy-and-retention) | M04; M13; M16; M26 |
| SYS-03 | Prevent invalid responses and stale decision or write holders from adopting changes; resolve same-response character-adoption requests before other fresh operations and preserve explicit dependency, freshness and accepted-character fences. | [Contracts](CONTRACTS.md) | M02–M03 |
| SYS-04 | Configure inference without silently changing identity, cost, or authority. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M15; B10 |
| SOC-01 | Establish a charter and actual human or institutional accountability. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | X01–X03 |
| SOC-02 | Distinguish real stakeholder input from simulated perspectives. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | X01 |
| SOC-03 | Preserve contextual evidence and revisable human or peer relationship interpretations; praise is not truth, familiarity is not acceptance, and no universal trust or popularity score replaces judgment. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | B02–B04; B09; X01 |
| UX-01 | Present clear evidence-linked status and meaningful controls. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | M14 |
| UX-02 | Respect access and retention across fragments, supporting records, views and derivatives; distinguish permitted evidence expiry from revocation, expose unavailable-history limits, and protect user-owned delivered artifacts from persona-state-cap cleanup without promising control of arbitrary outside copies. | [Persona core](../design/PERSONA-CORE.md#compact-retention-and-honest-forgetting) and [contracts](CONTRACTS.md#recovery-privacy-and-retention) | M11; M16; M23 |
| SRV-01 | Bound ongoing triggers, renewal, escalation, and stopping. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | B12; X04 |
| PHY-01 | Gate physical effects on their own observation, override, and assurance contract. | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) | X05 |
| OSS-01 | Version design, evaluators, and public claims without rewriting failures. | [Contribution guide](../CONTRIBUTING.md) | M16; X06 |


## What the persona-core refinement requires

The existing rows apply to one coherent account rather than parallel identity, graph, and reflection systems. The changed criteria require fresh evidence under the current evaluator revision:

| Concern | Existing requirements | Observable meaning |
|---|---|---|
| Character and own voice | PER-01–PER-03, PER-05 | The persona is the continuing whole of characteristic context, LLM invocation and reasoning, behavior, and self-revision. OCEAN tendencies, baseline VAD, useful additional characteristics and own-voice prose resolve one accepted character revision; selected prompt parts further define its situated approach. The LLM supplies a non-neutral reasoning substrate. Context supply and observed characteristic behavior need separate evidence. Supplied ideas and dormant time do not become invented firsthand experience. |
| Every-invocation maintenance | MEM-01–MEM-02, ACT-03, SYS-01–SYS-03, GOV-02–GOV-04 | Initialization, retrieval-only judgment, ordinary work, communication, coordination, reflection, repair and persona-capable subcalls receive maintenance input. Complete valid responses include an explicit outcome. Failed provider attempts keep truthful host status. Restricted selection repair remains mode-limited; no recursive maintenance call or self-wake follows. |
| Learning from work and surroundings | MEM-01–MEM-02, MEM-05, ACT-01 | Actual task, tool, environmental, human, peer, and self-observed consequences can change how prompt parts define later approaches, relationships, and navigation habits. Supporting records establish actual experience; fragments express the persona's own approach informed by it. Trace accepted revision through exact later supply, behavior, and assessed consequence. Stable-trait revision is optional and controlled, never automatic aging, weight training, or guaranteed improvement. Useful change, reasoned no_change, and bounded blocked or deferred outcomes remain valid. |
| Self-organization and next context | MEM-02–MEM-04, SYS-01–SYS-03, UX-01–UX-02 | Ordinary files form a compact persona-context corpus through primary-authored grep/search/regex cues, exact references, and optional indexes; no fixed taxonomy or outgoing link is forced. The primary persona navigates it to form its next characteristic context within cumulative fanout, calls, reads, context and cost limits, handling cycles, useful revisits and stale cues honestly. Dynamic matches are candidates; the host never follows associations recursively, executes cues as shell programs, or silently supplies them. Supporting evidence discovery and complete mandatory qualification closure retain their distinct purposes. |
| Relationships and cooperation | COL-01–COL-04, SOC-03 | All discretionary communication, collaboration and coordination use characteristic context without host role routing. Actual exchanges can update directional interpretations; praise, factual support, consent, competence, and accepted responsibility remain distinct. A useful encounter can change later work without a universal reputation score or an unaccepted peer commitment. |
| Skills and tools | ACT-01–ACT-04, EVD-01, MEM-05 | A characteristic reusable method is authored knowledge; a tool note is not an executable capability or proof of correct results. Traits may influence discretionary choices without changing authority or necessary verification. Relevant operations, versions, and outcomes need their own evidence. |
| Correction and continuity | PER-04, MEM-02–MEM-04, EVD-03, SYS-01–SYS-04 | Retained exact history and authoring character remain attributable under declared retention, with missing evidence honestly unavailable. Conflicting old character guidance is qualified, revised, retired or not selected. Invalid response and later persistence conflict remain distinct; independent work needs explicit evidence and current guards. Resolve character-adoption requests before other same-response operations: acceptance fences, definite no commit permits only eligible independent work, and unknown commit status holds. Mere investigation is not adoption. Restart or model change does not erase obligations or revive withdrawn information. |
| Correction effort and applicability | MEM-02–MEM-04, SYS-02, GOV-04, UX-02 | Ending bounded correction work does not resolve a separately accepted primary-authored warning on exact guidance or identified uses. Failed patches do not revive that guidance unqualified. Durable warning acceptance, source policy and justified resolution remain necessary; restricted repair and locked-character authority do not expand. |
| Useful and bounded work | NED-01–NED-04, MEM-02, MEM-05, GOV-01–GOV-04, EVD-02–EVD-05, UX-02 | Judge characteristic behavior, usefulness, harmful omission, task quality, and total cost together. Distinguish the prompt-part corpus, assembled prompt, and managed persona-state footprint; the last includes supporting records, archives, versions, cues, indexes, aliases, evidence and qualification closures, warnings, caches, managed copies, external backing and peak rewrites. Permitted evidence expiry may leave an experience-informed fragment only under derivative policy, never declassification, verified recollection or a substitute receipt. Protected state that cannot fit requires honest blocked admission or an authorized retention/capacity decision, not hidden growth or erased obligations. User-owned delivered artifacts retain their own authority; arbitrary recipient/provider copies are not claimed controlled. |

These refinements add no requirement family or fixed cognitive taxonomy. They do require explicit maintenance input and an explicit outcome in every complete valid persona response. A reasoned no_change outcome is sufficient when no useful change is warranted; silent omission is invalid. Mutation, a new selection, a separate reflection call, and numeric trait scores are not compulsory. A proposal, accepted save, actual later supply, observed action, and measured benefit remain different claims. Required work and stopping dispositions remain independent, and failed or refused calls cannot be backfilled with invented persona judgments.

## Applying and reporting the requirements

For each applicable row, record the responsible enforcement boundary, supported scope, implementation state, exact evidence, unrun cases, and unresolved deployment decision. Keep these statuses separate:

- Design conformance: the documented implementation responsibilities cover the rule without contradiction
- Mechanism evidence: the actual implementation enforces the boundary under the tested cases
- Behavioral evidence: observed persona work supports a scoped claim about choices, learning, cooperation, or utility
- Deployment approval: an accountable authority accepts the demonstrated scope and remaining risks

A disabled feature is not applicable only when it is genuinely unavailable and its absence does not remove an obligation incurred by other enabled work. Missing evidence is unassessed or not run, never passed. The [status ledger](STATUS.md) states what this documentation revision does and does not establish.

Historical DLV identifiers, supplemental D/FP/FR scenario labels, and earlier evaluator revisions remain mapped in [evaluation history](../evaluation/HISTORICAL-RESULTS.md). Changed criteria require a new versioned result; an old outcome never silently inherits this edition's interpretation.
