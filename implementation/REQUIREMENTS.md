# Invariants and requirement traceability

[Implementation guide](README.md) · [Detailed contracts](CONTRACTS.md) · [Acceptance catalogue](../evaluation/ACCEPTANCE.md)

This is the protected design foundation and coverage index for handbook edition 2.0. The 21 invariant identifiers and 45 requirement identifiers are retained from the preceding proposal. Wording is made independent of code and implementation branches. The detailed chapters and contracts supply the full meaning; this table is not permission to omit their failure paths.

Every listed test is specified, not reported as passed. A requirement applies when its corresponding feature or effect is enabled. Proposed extensions E1–E6 retain their declared status in the [design index](../design/README.md).

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

The evidence gates refer to [M, B, and X scenarios](../evaluation/ACCEPTANCE.md). Gates may support several requirements and are not an exhaustive security or domain assurance claim.

| ID | Required behavior | Detailed design | Primary evidence gates |
|---|---|---|---|
| PER-01 | Preserve continuing identity independently of model and work. | [Identity](../design/01-personas-and-identity.md) | B10; restoration evidence |
| PER-02 | Distinguish character, preference, competence, authority, and responsibility. | [Identity](../design/01-personas-and-identity.md) | B01–B04; capability evidence |
| PER-03 | Carry relevant individual context into decisions without invented biography. | [Identity](../design/01-personas-and-identity.md) | B01–B04 |
| PER-04 | Make lifecycle changes and open-obligation dispositions explicit. | [Identity](../design/01-personas-and-identity.md) | M06; X02 |
| PER-05 | Require truthful creation provenance and bounded initialization. | [Identity](../design/01-personas-and-identity.md) | M05; M18 |
| MEM-01 | Separate work facts, authored memory, and observed evidence. | [Memory](../design/02-memory-and-learning.md) | M08–M10; B09 |
| MEM-02 | Preserve fragment sources, scope, counterevidence, revisions, and visibility. | [Memory](../design/02-memory-and-learning.md) | M08; M11; B09 |
| MEM-03 | Scope selected context to the persona and current work. | [Memory](../design/02-memory-and-learning.md) | M08; M11 |
| MEM-04 | Preserve mandatory current constraints under context pressure. | [Memory](../design/02-memory-and-learning.md) | M08; M21 |
| MEM-05 | Measure learning transfer rather than memory volume. | [Memory](../design/02-memory-and-learning.md) | B09 |
| NED-01 | Preserve original intent and authorized mandate changes. | [Work](../design/03-work-and-cooperation.md) | M20; B11–B12 |
| NED-02 | Obtain continuation acceptance and expose ownership gaps. | [Work](../design/03-work-and-cooperation.md) | M19 |
| NED-03 | Distinguish conditional assumptions from confirmed facts. | [Work](../design/03-work-and-cooperation.md) | M20 |
| NED-04 | Check scope coverage against the original need. | [Work](../design/03-work-and-cooperation.md) | B11–B12; omitted-outcome fixture |
| COL-01 | Preserve individual agendas, an unranked shared board, and accepted commitments. | [Work](../design/03-work-and-cooperation.md) | B01–B04 |
| COL-02 | Separate offers, membership, responsibility, and actual contribution. | [Work](../design/03-work-and-cooperation.md) | M06; M18–M19 |
| COL-03 | Preserve exact agreement endorsements and dissent. | [Work](../design/03-work-and-cooperation.md) | B02–B03; X01 |
| COL-04 | Resolve consequential feedback through explicit dispositions. | [Work](../design/03-work-and-cooperation.md) | M21; B05 |
| COL-05 | Support provisional interfaces and bounded iteration. | [Work](../design/03-work-and-cooperation.md) | M22 |
| COL-06 | Permit useful birth and no-birth restraint under conserved resources. | [Identity](../design/01-personas-and-identity.md) | M05–M07; B08 |
| ACT-01 | Use or acquire capabilities through actual evidence-backed operations. | [Action](../design/04-capabilities-and-action.md) | M10; B11–B12 |
| ACT-02 | Enforce execution boundaries rather than merely label them. | [Action](../design/04-capabilities-and-action.md) | M12 |
| ACT-03 | Require actual results before dependent decisions and publication. | [Action](../design/04-capabilities-and-action.md) | M17; M26 |
| ACT-04 | Preserve unknown external effects and reconcile before repetition. | [Action](../design/04-capabilities-and-action.md) | M13 |
| GOV-01 | Keep grants scoped, revocable, and no broader than their parents. | [Authority](../design/05-authority-and-resources.md) | M05–M07; M11–M13 |
| GOV-02 | Conserve resources across descendants, retries, compaction, and review. | [Authority](../design/05-authority-and-resources.md) | M07; M23 |
| GOV-03 | Protect agreed closeout capacity. | [Authority](../design/05-authority-and-resources.md) | M23 |
| GOV-04 | Bound idle cognition, reminders, and no-progress loops. | [Authority](../design/05-authority-and-resources.md) | M25 |
| EVD-01 | Preserve exact artifacts, input mappings, and actual execution evidence. | [Evidence](../design/06-evidence-and-completion.md) | M09–M10 |
| EVD-02 | Review exact scope under an explicit independence policy. | [Evidence](../design/06-evidence-and-completion.md) | B05; B11 |
| EVD-03 | Separate historical verdict from current applicability. | [Evidence](../design/06-evidence-and-completion.md) | M09; M24 |
| EVD-04 | Seal one coherent reviewed state with no unresolved applicable blockers. | [Evidence](../design/06-evidence-and-completion.md) | M21; M24 |
| EVD-05 | Expose activity, coverage, evidence, acceptance, and outside validation separately. | [Evidence](../design/06-evidence-and-completion.md) | M14; B11–B12 |
| SYS-01 | Make accepted operations retry-safe and attributable. | [Contracts](CONTRACTS.md) | M01–M04; M13 |
| SYS-02 | Restore pending events, reservations, and effects without new authority. | [Contracts](CONTRACTS.md) | M04; M16; M26 |
| SYS-03 | Prevent stale decision or write holders from adopting changes. | [Contracts](CONTRACTS.md) | M02–M03 |
| SYS-04 | Configure inference without silently changing identity, cost, or authority. | [Action](../design/04-capabilities-and-action.md) | M15; B10 |
| SOC-01 | Establish a charter and actual human or institutional accountability. | [Society, E2](../design/07-experience-and-society.md) | X01–X03 |
| SOC-02 | Distinguish real stakeholder input from simulated perspectives. | [Society, E2–E3](../design/07-experience-and-society.md) | X01 |
| SOC-03 | Preserve contextual evidence rather than a universal trust or popularity score. | [Society](../design/07-experience-and-society.md) | B02–B04; X01 |
| UX-01 | Present clear evidence-linked status and meaningful controls. | [Experience](../design/07-experience-and-society.md) | M14 |
| UX-02 | Respect access and retention across every view and derivative. | [Memory](../design/02-memory-and-learning.md) and [contracts](CONTRACTS.md) | M11; M16 |
| SRV-01 | Bound ongoing triggers, renewal, escalation, and stopping. | [Services, E4](../design/07-experience-and-society.md) | B12; X04 |
| PHY-01 | Gate physical effects on their own observation, override, and assurance contract. | [Physical extension, E4](../design/07-experience-and-society.md) | X05 |
| OSS-01 | Version design, evaluators, and public claims without rewriting failures. | [Contribution guide, E6](../CONTRIBUTING.md) | M16; X06 |

## Using this index

For each applicable row, an implementation records the responsible component, implementation state, supporting evidence, untested cases, and blocking deployment decision. “Implemented,” “mechanically tested,” “behaviorally demonstrated,” and “approved for a particular deployment” are separate statuses.

The catalogue contains 45 requirement rows. The original identifiers remain stable so a design change can be traced without confusing renamed requirements with new behavior.

## Consolidation and evaluation links

The active catalogue remains the 45 rows above, with I01–I21 unchanged. The [organization clarification](../design/03-work-and-cooperation.md#how-organization-emerges) and [core handoff contract](CONTRACTS.md#persona-owned-organization-and-capability-choice) elaborate I03 and the existing NED, COL, ACT, GOV, EVD, and SYS boundaries; they do not add a task-specific workflow.

The former DLV-01–DLV-10 layer is retired as redundant; the [historical mapping](DELIVERY-CONTRACTS.md#retired-identifier-mapping) preserves each identifier and its existing coverage. [D01–D16](../evaluation/DELIVERY-ACCEPTANCE.md) are supplemental evaluation refinements, not extra active requirements. [Emergence evaluation](../evaluation/README.md#evaluating-emergent-organization) adds comparisons under the existing behavioral gates. Record the exact design and evaluator revisions; earlier outcomes do not silently inherit revised criteria.

## Fragment-persona refinement

[The persona as an evolving fragment system](../design/FRAGMENT-PERSONA.md) refines PER-01–PER-05, MEM-01–MEM-05, COL-01–COL-04, SOC-03, and the applicable GOV, EVD, SYS, ACT, UX, and OSS boundaries without replacing their identifiers or weakening I01–I21. It makes self-understanding, procedural learning, metacognition, relationships, and context intent parts of one authored fragment system. Every ordinary primary persona decision combines useful work with a fragment disposition and next-context intent; no additional reflection, memory-authoring, or retrieval-planning LLM call is required.

The design explicitly permits bounded persona-authored conditional selection plans, resolved against actual events before a later call. This is delegated selection, not an inference of consent from a search match. Its precedence table resolves earlier immediate-selection-only wording while preserving source restrictions, current authority, and mandatory context.

[FP-M01–FP-M16 and FP-B01–FP-B07](../evaluation/FRAGMENT-PERSONA.md) provide the detailed requirement mapping and supplemental acceptance scenarios. They distinguish same-call authorship, exact provider-bound context, event recall, social interpretation, voice, and measured work improvement. These are specified tests, not execution evidence or additional active requirement rows.
