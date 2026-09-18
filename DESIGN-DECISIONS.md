# Design decisions and their consequences

[Home](README.md) · [Source rationale](sources/README.md) · [Detailed design](design/README.md)

This register states the choices behind handbook edition 2.0. “Retained” means a conceptual rule inherited from the consolidated proposal, not a claim that a runtime implements it. “Editorial” changes the presentation or repository scope. “Proposed extension” remains explicitly subject to adoption for the affected feature.

| Decision | Status and rationale | Consequence and alternative rejected |
|---|---|---|
| People authorize purpose; personas choose methods; the system enforces boundaries. | Retained. Judgment, permission, and evidence answer different questions. | No hidden central domain planner; no self-authorizing persona. See [S3](sources/S3-specification-v1.1.md). |
| Identity continues independently of roles and models. | Retained. Continuity requires inspectable state, not a label. | Model changes preserve obligations but may require renewed performance evidence; fixed professions and fabricated biographies are rejected. |
| Keep six public concepts with supporting records. | Retained. Readers need a small understandable vocabulary. | Agreements, grants, and findings need precise meaning, not necessarily separate engines. See [S1](sources/S1-prior-research-report.md). |
| Individual agendas coexist with shared visibility and accepted commitments. | Retained v1.2 resolution. Shared awareness need not erase independent judgment. | No universal priority score or attributed “team mind.” Dependencies may order some work without ranking all attention. |
| Responsibility requires acceptance, including continuation of the whole need. | Retained. Naming a participant does not ensure follow-through. | Unowned outcomes remain visible; continuation does not create a compulsory leader. |
| Birth, membership, and commitment are distinct. | Retained. A new participant needs bounded orientation and room to negotiate. | No automatic expertise, copied budget, broadened grant, or endless replacement loop after a decline. |
| Retained memory is authored interpretation. | Retained. Experience, hearsay, inference, and current authority differ. | No automatic conversion of documents into learning; no shared global private memory. Benefit requires later evidence. |
| Real actions need enforceable boundaries and actual observations. | Retained. A running operation is not a completed result. | Pending decisions do not publish imaginary outputs; unclear external effects are reconciled before repetition. |
| Protect finishing within the same resource envelope. | Retained. Optional exploration can otherwise leave required review unfunded. | No universal reserve percentage; authorized reallocations conserve the root and retain unknown exposure. |
| Reviews bind exact versions; final release binds one coherent state. | Retained. A result can change after a legitimate review. | Historical acceptance never transfers to newer work without appropriate current evidence. |
| Keep the design independent of a language or runtime branch. | Editorial scope decision authorized for this design repository. Behavioral contracts remain substantive. | Historical implementation instructions stay in Git history, not the reader's prerequisite path. This does not modify or certify the separate runtime. |
| Use a layered handbook rather than one mandatory long document. | Editorial. Beginners, designers, implementers, and evaluators need different entry points. | The overview explains the whole; chapters and contracts hold details; indexes preserve traceability. |
| Keep current Markdown free of implementation and diagram-code examples. | Editorial. The user requested a design-only reading experience. | No commands, schemas, snippets, or required build setup. Editable SVG artwork remains, with prose explanations. |
| Preserve old paths and history without pretending rewritten sources are original bytes. | Editorial. Existing readers need continuity and provenance. | Source filenames remain, but each brief states its new role. The manifest pins exact historical originals. |

## Proposed extensions remain proposed

| Extension | Scope | Boundary |
|---|---|---|
| E1 | Functional embodiment layers and an inspectable persona profile. | A useful explanatory organization, not a scientific claim of consciousness or feelings. |
| E2 | Community charter, actual stakeholder representation, institutions, and appeal. | Real human or institutional accountability cannot be replaced with simulated consent. |
| E3 | Transparent AI presentation and additional sensitive-use safeguards. | Does not establish suitability for every educational, personal-support, or public setting. |
| E4 | Ongoing-service and optional physical-interface contracts. | Does not provide certified physical control or guarantee an available human escalation service. |
| E5 | Worksheets, requirement identifiers, conformance profiles, and deployment decisions. | Authoring aids and evidence organization, not mandatory ceremony in every task. |
| E6 | Contribution, versioning, and public evidence governance. | Does not choose repository licensing terms or erase earlier failures. |

A basic collaborator can omit optional features and state that limit. Enabling a feature requires its applicable safeguards and evidence. Neither an attractive example nor a completed worksheet adopts a deployment policy.

## Editorial clarifications

This handbook makes the precedence of its documents explicit, supplies code-free handoff contracts, and exposes previously scattered deployment choices. Lifecycle administration remains accountable: retirement does not silently reactivate a persona or restore expired grants. Any separately authorized reactivation must preserve history and recheck obligations and permissions.

These clarifications are not reports of new measured behavior. The original invariants, requirement identifiers, and acceptance identifiers are retained; future semantic changes must name the affected identifiers and describe compatibility and evaluation consequences.

## Delivery consolidation and emergent organization

**Adopted design clarification, 18 September 2026.** Review of the pre-addendum handbook found that concrete outputs, capability acquisition, native editability, analysis mappings, repair, integration, and exact-state completion already existed. The delivery addendum overstated these as missing architecture. The [review map](design/DELIVERABLE-PRODUCTION.md) and [DLV compatibility record](implementation/DELIVERY-CONTRACTS.md) retire the redundant requirement layer without weakening existing evidence obligations or erasing history.

**Resolution:** keep the original 21 invariants and 45 requirement identifiers. Put the clarification of [persona-owned organization](design/03-work-and-cooperation.md#how-organization-emerges) in the work chapter and [core contracts](implementation/CONTRACTS.md#persona-owned-organization-and-capability-choice). Plans, output lists, method notes, and delivery inventories remain uses of existing records, not compulsory new objects or a fixed pipeline. The runtime supplies social and action affordances and enforces safeguards; personas choose approaches, negotiate, and revise actual work.

**Alternatives rejected:** hard-coding professions or task-specific workflows; hiding those choices in orchestration prompts or wrappers; forcing birth or a permanent supervisor; removing safety and evidence enforcement in the name of emergence; and requiring every task to invent a new method. Domain-specific capabilities and attributable reuse of learned methods remain valid. Continuing societies and institutions still follow the applicable declared extension contracts.

**Compatibility and evaluation:** DLV identifiers remain historical mappings, while D01–D16 remain versioned stress scenarios mapped to existing rules. Their task examples are illustrative rather than runtime policy. The [emergence comparisons](evaluation/README.md#evaluating-emergent-organization) test varied tasks, policy provenance, declined commitments, unavailable capabilities, meaningful repair, and reuse under existing behavioral gates. No live behavior, circuit output, or universal competence is established by this documentation change.

## Changing a decision

Use the [contribution guide](CONTRIBUTING.md) and [decision worksheet](templates/README.md#design-decision-and-evaluation-record). Identify the need, current rule, evidence or counterexample, proposed change, alternatives, consequences, and affected tests. Do not silently change the definition of success to make an old result appear compliant.
