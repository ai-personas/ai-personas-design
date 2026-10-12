# Source provenance and consolidation map

[Sources](README.md) · [Current design](../design/README.md) · [Decisions](../DESIGN-DECISIONS.md) · [Historical results](../evaluation/HISTORICAL-RESULTS.md)

## Current authority and historical stages

This manifest records where the design came from, what changed, and where historical evidence remains available. The current normative design is the persona core, work and boundaries, and contracts, governed by the protected invariants. Earlier manuals, proposals, figures, and source briefs have been removed from active navigation where they duplicate or conflict with that design. Retiring them does not erase their history or permit implementation evidence to be discarded.

**Immediate predecessor.** The **7 October 2026** consolidation is pinned at **202dd753dd1816dc9a6121f267a0d4fe7d060fad**. Its [complete tree](https://github.com/ai-personas/ai-personas-design/tree/202dd753dd1816dc9a6121f267a0d4fe7d060fad) and [commit record](https://github.com/ai-personas/ai-personas-design/commit/202dd753dd1816dc9a6121f267a0d4fe7d060fad) preserve that stage. It adopted ordinary own-voice files, context choice by the primary persona, and repair of selection failures within defined limits. Its descriptions and evaluation criteria document that stage; they do not establish a pass for the changed 8 October target.

**Earlier archive.** The complete pre-consolidation repository is pinned at **f4549bd594e6a0cf5205ac031ed422ab269def8d**. The [complete pre-consolidation tree](https://github.com/ai-personas/ai-personas-design/tree/f4549bd594e6a0cf5205ac031ed422ab269def8d) preserves every path retired during the 7 October consolidation, including text and artwork, at its exact historical revision. These links are historical evidence, not alternative active specifications. Historical references use fixed revisions, never a moving branch.

**What the current target retains and changes.** Compulsory graph organization, delegated semantic selection, mandatory numeric character controls, and the on-demand-only file proposal remain superseded. The 8 October semantics additionally require meaningful descriptions of OCEAN traits—openness, conscientiousness, extraversion, agreeableness, and neuroticism—and a distinct VAD modeled affect account covering valence, arousal, and dominance. Authored reusable fragments must carry the persona's character, and every persona invocation must explicitly consider maintenance and return its outcome. Changes remain selective; numeric scales remain optional.

Exact provenance, qualifications, permissions, commitments, resource bounds, effects, and evidence remain protected. The [recorded decisions](../DESIGN-DECISIONS.md) distinguish changed obligations from editorial clarification.

## 7 October predecessor and 8 October semantic changes

The pinned files below show what the 7 October design meant. Their current counterparts use the same paths but contain changed obligations. Keeping both versions identifiable prevents an old observation from being treated as evidence for a newer rule.

| Exact 7 October source | 8 October disposition and authoritative home |
|---|---|
| [Persona core](https://github.com/ai-personas/ai-personas-design/blob/202dd753dd1816dc9a6121f267a0d4fe7d060fad/design/PERSONA-CORE.md) | The [current persona core](../design/PERSONA-CORE.md) requires semantic OCEAN/VAD grounding and its expression throughout authored reusable fragments. Coherent prose alone, without the required trait and affect coverage, no longer suffices. Compulsory numeric controls are not restored. |
| [Contracts](https://github.com/ai-personas/ai-personas-design/blob/202dd753dd1816dc9a6121f267a0d4fe7d060fad/implementation/CONTRACTS.md) and [requirements](https://github.com/ai-personas/ai-personas-design/blob/202dd753dd1816dc9a6121f267a0d4fe7d060fad/implementation/REQUIREMENTS.md) | The [current contracts](../implementation/CONTRACTS.md) and [requirements](../implementation/REQUIREMENTS.md) require a maintenance request for every persona-level invocation and an explicit outcome in every accepted response. Ordinary work may still leave fragments unchanged. Missing or failed maintenance cannot silently count as an authored decision to leave them unchanged. |
| [Work and boundaries](https://github.com/ai-personas/ai-personas-design/blob/202dd753dd1816dc9a6121f267a0d4fe7d060fad/design/WORK-AND-BOUNDARIES.md) | The [current work boundaries](../design/WORK-AND-BOUNDARIES.md) retain protections for authority, resources, observations, continuity, and release. Character and modeled affect grant no new authority. |
| [Evaluation directory](https://github.com/ai-personas/ai-personas-design/tree/202dd753dd1816dc9a6121f267a0d4fe7d060fad/evaluation) and [implementation status](https://github.com/ai-personas/ai-personas-design/blob/202dd753dd1816dc9a6121f267a0d4fe7d060fad/implementation/STATUS.md) | The current [acceptance catalogue](../evaluation/ACCEPTANCE.md), [historical results](../evaluation/HISTORICAL-RESULTS.md), and [status](../implementation/STATUS.md) separate changed criteria, planned comparisons, and actual historical evidence. This revision creates no new model trial or runtime result. |
| [File-and-context research](https://github.com/ai-personas/ai-personas-design/blob/202dd753dd1816dc9a6121f267a0d4fe7d060fad/sources/PERSONA-FILES-RESEARCH.md) and [source manifest](https://github.com/ai-personas/ai-personas-design/blob/202dd753dd1816dc9a6121f267a0d4fe7d060fad/sources/SOURCE-MANIFEST.md) | The [current research](PERSONA-FILES-RESEARCH.md) adds distinctions between human traits and affect, limitations of LLM personas, and maintenance rationale, while keeping source claims within their stated limits. This manifest adds the predecessor stage without changing the lineage of earlier supplied sources. |
| [Examples](https://github.com/ai-personas/ai-personas-design/blob/202dd753dd1816dc9a6121f267a0d4fe7d060fad/examples/WORKED-EXAMPLES.md), [visual guide](https://github.com/ai-personas/ai-personas-design/blob/202dd753dd1816dc9a6121f267a0d4fe7d060fad/VISUAL-GUIDE.md), and [loop artwork](https://github.com/ai-personas/ai-personas-design/blob/202dd753dd1816dc9a6121f267a0d4fe7d060fad/assets/persona-files-loop.svg) | The current [examples](../examples/WORKED-EXAMPLES.md) and [visual explanation](../VISUAL-GUIDE.md) illustrate the revised meaning. Both generations are hypothetical design illustrations, not records of executed persona behavior. |

The 8 October research is a new explanatory synthesis, not an edited copy of an original supplied report. The research brief gives each external source a bounded claim and a date or version. Those sources support individual constructs or mechanisms; they do not validate the complete architecture or provide a 100% guarantee. The original provenance and integrity statements below apply only to the original bytes they describe.

## Reciprocal development and compact context refinement

The later 8 October design-only refinement addresses how actual experience can shape a persona and how its stored and selected context stays bounded. It adds [reciprocal development from actual work and interaction](PERSONA-FILES-RESEARCH.md#reciprocal-development-from-actual-work-and-interaction) and [compact associative fragments and selective retention](PERSONA-FILES-RESEARCH.md#compact-associative-fragments-and-selective-retention).

The independently checked primary sources include Roberts, Caspi, and Moffitt's human longitudinal study; the original vocabulary-problem article; ReadAgent v1; A-MEM v1; LongMemEval v1; Memora v1; and ANCHOR v1. The research brief records exact publication links, inspected versions, supported claims, and limits on applying the findings to this design.

**Version distinction.** The earlier benchmark-category account still cites LongMemEval v2. The added compression analysis identifies its inspected LongMemEval v1 explicitly; it does not silently substitute one version for the other.

The synthesis keeps human analogy, component experiments, engineering judgment, and the untested combined architecture separate. It preserves the latest [direct collaboration evidence and limits](PERSONA-FILES-RESEARCH.md#trait-composition-and-collaboration-direct-evidence-and-limits), all earlier research references, and every pinned historical link below.

Query cues suggest where to look. They do not replace exact evidence references or accepted required qualifications. Accounting for the whole managed store, and respecting conditions on retaining material derived from other sources, are design obligations. They are not empirical guarantees supplied by these publications. This prose revision gives no original attachment, historical result, or artwork-validation record a new integrity claim or runtime pass.

## Persona-defining context clarification

The earlier 8 October clarification treats the whole loop—context, LLM reasoning, action, feedback, and self-revision—as the persona. Authored fragments are prompt parts that carry the persona's character; their primary purpose is not factual memory storage.

The [context-adaptation comparison](PERSONA-FILES-RESEARCH.md#context-adaptation-is-the-closer-engineering-comparison) originally added GEPA v1 and expanded the existing ACE v1 account. Both were independently checked on 8 October 2026, with these inspection limits at that stage:

| Source | Source date | Inspection recorded at that stage |
|---|---|---|
| GEPA v1 | 25 July 2025 | Abstract only |
| ACE v1 | 6 October 2025 | Full text |

Their prompt and context adaptation mechanisms offer a closer engineering comparison. They do not validate persona identity, continuity, or this design's ownership and selection rules.

**Later ACE inspection.** A separate inspection on 9 October 2026 examined [ACE v3, 29 March 2026](https://arxiv.org/html/2510.04618v3), specifically Appendices A.3–A.4 and A.6. It supports the research brief's bounded extension on robustness, reflection, and evaluation cost. The earlier v1 attribution and source locations remain intact. This inspection is neither a reproduction nor an adoption of the architecture.

**Contextual-persona sources.** The discussion adds the Persona Selection Model author essay, dated 23 February 2026, and The Assistant Axis v1 abstract, dated 15 January 2026. Both were independently inspected on 8 October 2026. They establish the scope of the cited account and reported mechanisms. They do not prove that a coherent enduring persona exists or that context is the sole source of behavior.

Existing memory and retention references remain available for adjacent questions about storage, discovery, stale guidance, and provenance. Clarifying their role neither changes their results nor removes bounded-retention protections. This clarification adds no runtime finding and transfers no original integrity claim to rewritten prose. All pinned historical links and supplied-source lineage below remain unchanged.

## Bootstrap and bounded supporting-resource refinement

The subsequent 8 October synthesis explains how a persona starts from a trait seed, keeps its prompts coherent, and finds supporting material within limits. It integrates [trait-seeded bootstrap and self-harmonization](PERSONA-FILES-RESEARCH.md#trait-seeded-bootstrap-and-self-harmonization), [need-directed supporting context](PERSONA-FILES-RESEARCH.md#need-directed-supporting-context), and [provider/lifecycle fit](PERSONA-FILES-RESEARCH.md#provider-and-standards-fit).

Persona-defining prompt authorship remains separate from supporting histories, tool interfaces, skills, scripts, and data. The source comparison motivates bounded discovery controlled by the client and exact supply of selected material. The global catalogue stays outside both the provider request and the model's context. The comparison introduces no semantic selector and does not turn provider marketing into a runtime guarantee.

**Every-call responsibilities.** The later 8 October clarification combined work, fragment maintenance, supporting-asset maintenance, and any next-context requests in each persona call. The 10 October correction then required every accepted response to include explicit next-context dispositions for both fragments and supporting resources, superseding silent omission. A concise, reasoned no-change outcome for maintenance and an explicit decision to preserve appropriate context or request no optional context remain valid under the current design. The [maintenance rationale](PERSONA-FILES-RESEARCH.md#universal-consideration-and-selective-mutation-are-engineering-choices) identifies every-call asset consideration as a requested, untested design choice. It attributes no new empirical finding or compulsory write, search, or extra call to the component literature.

**Component-source checks.** Primary claims were independently checked on 8 October 2026. The deeper GEPA v1 methods inspection supersedes only the earlier abstract-only inspection limit. It changes neither the source version nor the limits on applying its findings here.

Added component evidence comprises Self-Refine v2 (25 May 2023), the published PersonaLLM evaluation details, Lost in the Middle (TACL 2024), ComplexBench (NeurIPS 2024), OpenAI/Anthropic tool-search documentation current at inspection, Agent Skills specification/integration guidance, and Anthropic engineering reports. The research brief holds the exact links and bounded claims, avoiding a second bibliography that could detach conclusions from their limits.

**Protocol and provider versions.** Current MCP claims use the pinned **2026-07-28** tools, resources, subscriptions, and caching specifications; the current-version redirect was checked that day. **2025-11-25** remains a historical protocol version and is not the source for current subscription or caching behavior. SLSA provenance uses **v1.2**. Mutable provider and skills pages carry inspection dates. The Anthropic tool identifier's 20251119 suffix is not a page publication date.

None of these sources establishes a working adapter, bounded retention across the whole managed store, fidelity to the trait seed, behavioral self-harmonization, or lower total episode cost for AI Personas.

**Generated assets.** The [generated-asset evidence](PERSONA-FILES-RESEARCH.md#generated-reusable-assets-empirical-limits) adds four independently inspected sources. Inspection took place on 8 October 2026.

| Source | Inspected version's date |
|---|---|
| Voyager v2 | 19 October 2023 |
| LATM v2 | 11 March 2024 |
| ToolMaker v1 | 17 February 2025 |
| SkillsBench v4 | 14 June 2026 |

Their component results and confounding factors remain tied to those versions. SkillsBench's diagnostic does not inherit percentages from earlier versions or establish generated code as an isolated cause. No source validates this design's lexical discovery, single-primary-LLM ownership, and every-call maintenance loop.

**Direct discovery evidence.** The [direct discovery note](PERSONA-FILES-RESEARCH.md#direct-tool-discovery-evidence) adds ToolRet's published ACL Findings 2025 paper and T-Eval v2 (4 January 2024), independently checked on 8 October 2026. Assisted inputs and static retrieval differ from this design's unaided, adaptive discovery. These sources create no new requirement or runtime evidence.

The revision adds rationale and comparisons that have not been run. It preserves original source lineage, pinned historical evidence, and failed or limited results. The edits add no code, model trial, runtime conformance test, publication, or deployment approval.

## 9 October evidence-driven evaluation refinement

The 9 October additions explain what future evaluations should examine and keep separate. Selective additions to the [research brief](PERSONA-FILES-RESEARCH.md) support assessment isolation, chosen opportunities to gather evidence, coordination conventions with a defined scope, controls for source style, poisoning of derived assets, and attribution of durable reuse.

Each claim states the inspected primary version and the limits of its component evidence. Han's published abstract is kept distinct from earlier preprint methods. For the Nature source, the cited outcome is narrowed to generated status text.

These sources motivate comparisons that have not yet been run in the existing [method](../evaluation/README.md) and [acceptance catalogue](../evaluation/ACCEPTANCE.md). They do not establish architectural changes, independent replication of the persona loop, runtime passes, or inherited source-integrity claims.

## Original supplied-source lineage

The historical package recorded five supplied attachments before the code-free briefs were written. Their original repository copies are pinned at **0c96694303e344ef976150a4d544f3ca57f77d33**. The names below identify their origins; matching lineage does not mean that a later rewritten brief has identical bytes.

| Original recorded attachment | Exact original repository copy |
|---|---|
| deep-research-report(2).md | [S1 original research report](https://github.com/ai-personas/ai-personas-design/blob/0c96694303e344ef976150a4d544f3ca57f77d33/sources/S1-prior-research-report.md) |
| AI-PERSONAS-EMERGENT-DESIGN(1)(2).md | [S2 original emergence proposal](https://github.com/ai-personas/ai-personas-design/blob/0c96694303e344ef976150a4d544f3ca57f77d33/sources/S2-emergent-design.md) |
| AI-PERSONAS-RUST-FINAL-SPEC(1)(2).md | [S3 original v1.1 specification](https://github.com/ai-personas/ai-personas-design/blob/0c96694303e344ef976150a4d544f3ca57f77d33/sources/S3-specification-v1.1.md) |
| AI-PERSONAS-RUST-SPEC-v1.2(1)(2).md | [S4 original v1.2 specification](https://github.com/ai-personas/ai-personas-design/blob/0c96694303e344ef976150a4d544f3ca57f77d33/sources/S4-specification-v1.2.md) |
| STRESS-TEST-REPORT(1)(2).md | [S5 original stress-test report](https://github.com/ai-personas/ai-personas-design/blob/0c96694303e344ef976150a4d544f3ca57f77d33/sources/S5-stress-test-report.md) |

The [original manifest and its integrity claims](https://github.com/ai-personas/ai-personas-design/blob/0c96694303e344ef976150a4d544f3ca57f77d33/sources/SOURCE-MANIFEST.md) apply only to the bytes it describes. Those claims must not be reused as fingerprints for later briefs, new consolidated chapters, or altered artwork. The [original complete proposal](https://github.com/ai-personas/ai-personas-design/blob/0c96694303e344ef976150a4d544f3ca57f77d33/AI-PERSONAS-DESIGN-PROPOSAL.md) is also historical.

The final separate code-free source briefs remain available at the pre-consolidation revision:

- [S1 foundations](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/sources/S1-prior-research-report.md)
- [S2 emergence](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/sources/S2-emergent-design.md)
- [S3 architecture rationale](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/sources/S3-specification-v1.1.md)
- [S4 reliability](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/sources/S4-specification-v1.2.md)
- [S5 stress scenarios](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/sources/S5-stress-test-report.md)

Their useful rationale now appears in the current design and [research brief](PERSONA-FILES-RESEARCH.md). They are no longer parallel active chapters.

## Retired design paths and their current homes

Use this map to find where an older topic is covered now. Links in the first column open exact historical files. The second column identifies the current home of retained meaning; it does not imply that every old obligation remains unchanged.

| Historical source | Current disposition |
|---|---|
| [Complete proposal](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/AI-PERSONAS-DESIGN-PROPOSAL.md) | Consolidated into the [home](../README.md), persona core, and work boundaries. |
| [Personas and identity](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/design/01-personas-and-identity.md), [memory and learning](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/design/02-memory-and-learning.md) | The [persona core](../design/PERSONA-CORE.md) retains continuity while revising representation and selection. |
| [Fragment persona](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/design/FRAGMENT-PERSONA.md), [memory graph](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/design/MEMORY-GRAPH.md), [fragment recall](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/design/FRAGMENT-RECALL.md) | The [persona core](../design/PERSONA-CORE.md) and [contracts](../implementation/CONTRACTS.md) retain the protection of exact authored text and its qualifications. Mandatory graph organization and delegated selection are superseded. |
| [Persona-owned files proposal](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/design/PERSONA-OWNED-FILES.md) | The [persona core](../design/PERSONA-CORE.md) adopts the file-facing interface. The proposal's on-demand-only selection target and pending-adoption status are superseded. |
| [Persona development](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/design/PERSONA-DEVELOPMENT.md) | The persona core covers own-voice development; work boundaries cover exploration and lifecycle. Numeric controls are no longer a minimal-persona requirement. |
| [Work and cooperation](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/design/03-work-and-cooperation.md), [capabilities and action](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/design/04-capabilities-and-action.md), [authority and resources](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/design/05-authority-and-resources.md) | [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) covers adopted needs, actual consent, operations, trust boundaries, and conserved resources. |
| [Evidence and completion](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/design/06-evidence-and-completion.md), [experience and society](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/design/07-experience-and-society.md) | Work boundaries cover exact claims, assessments, release, readable controls, and the conditions for wider deployments. |
| [Coordination and lifecycle](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/design/COORDINATION-LIFECYCLE.md), [persona-owned process](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/design/PERSONA-OWNED-PROCESS.md) | Work boundaries and [deployment decisions](../implementation/DEPLOYMENT-DECISIONS.md) cover exact acceptance, an accountable lifecycle, optional process, and declared execution modes. |
| [Continuity and recovery](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/design/CONTINUITY-RECOVERY.md), [recovery and delivery](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/design/RECOVERY-AND-DELIVERY.md), [effort and stopping](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/design/EFFORT-AND-STOPPING.md) | Work boundaries cover blocking stale decisions, recovery within limits, honest diagnostics, explicit continuation, delivery, and remaining obligations. |
| [Exploration accounting](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/design/EXPLORATION-ACCOUNTING.md), [development evidence boundaries](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/design/DEVELOPMENT-EVIDENCE-BOUNDARIES.md) | Work boundaries and the persona core cover limits across the whole episode, privacy for historical sources, exact retained changes, and actual triggers. |
| [Decision efficiency](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/design/DECISION-EFFICIENCY.md), [qualified observations](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/design/QUALIFIED-OBSERVATIONS.md) | The core, work boundaries, and contracts cover usable capability instructions within bounds, total cost, and full required qualifications. They do not require selector machinery. |
| [Delivery review](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/design/DELIVERABLE-PRODUCTION.md) | Work boundaries consolidate existing production and delivery obligations without adding another requirement family. |
| [Circuit and cross-domain illustrations](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/examples/5W-INVERTER-AND-CROSS-DOMAIN.md), [example index](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/examples/README.md) | One [worked-examples](../examples/WORKED-EXAMPLES.md) page illustrates hypothetical outcomes and disturbances. These are never installed workflows. |

## Implementation and evaluation history

Historical implementation evidence may require access that the public design does not. **Source access, checked 8 October 2026:** the connected account confirmed that the runtime implementation repository ai-personas/ai-personas is private. Its pinned implementation references require repository access; listing them here does not make them publicly available. This restriction concerns implementation evidence, separate from the public design contract.

Authenticated source inspection is not execution, a test rerun, or proof of current conformance. Historical pins and reported outcomes retain their original scope.

**Implementation archive.** The [complete former implementation directory](https://github.com/ai-personas/ai-personas-design/tree/f4549bd594e6a0cf5205ac031ed422ab269def8d/implementation) preserves DELIVERY-CONTRACTS, FRAGMENT-RECALL-CONTRACT, FRAGMENT-RECALL-STATUS, OPERATION-WORKING-SET, RECALL-CACHE-IDENTITY, RECALL-PACKING, and the previous contract and requirement versions.

Their current obligations are consolidated in [contracts](../implementation/CONTRACTS.md), [requirements](../implementation/REQUIREMENTS.md), and [status](../implementation/STATUS.md). Old semantic-selection cache rules apply to historical or explicitly optional experiments, not to every persona.

**Evaluation archive.** The [complete former evaluation directory](https://github.com/ai-personas/ai-personas-design/tree/f4549bd594e6a0cf5205ac031ed422ab269def8d/evaluation) preserves DECISION-EFFICIENCY, DECISION-REFERENCE-USABILITY, DELIVERY-ACCEPTANCE, FRAGMENT-PERSONA, FRAGMENT-RECALL, METHOD-CONTINUITY, PERSONA-WORK-COMMUNICATION, RECOVERY-AND-DELIVERY, and the previous acceptance and method versions.

The [historical-results ledger](../evaluation/HISTORICAL-RESULTS.md) gives the exact mapping of identifiers and criteria. The current [acceptance catalogue](../evaluation/ACCEPTANCE.md) specifies the observations now required. No old result silently passes those current criteria.

**Earlier vendor research.** The [former vendor-source note](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/sources/FRAGMENT-RECALL-SOURCES.md) records dated TypeSafe/Jev documentation consulted for an earlier optional-selector design. It is neither a current vendor audit nor evidence that this design needs that service. Current external research supports only the claims stated in [the research brief](PERSONA-FILES-RESEARCH.md).

## Artwork retirement

**Current explanatory artwork, 12 October 2026.** The [visual guide](../VISUAL-GUIDE.md) indexes 19 repository-native SVG diagrams, including the revised loop. They are newly authored teaching illustrations of this design, with captions and complete text equivalents beside the relevant rules. They are not screenshots, observed persona traces, psychological validation, or runtime evidence. Earlier artwork render checks apply only to their exact historical versions.


The historical artwork remains available with its original notes. The old [visual guide](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/VISUAL-GUIDE.md), [fragment-recall atlas](https://github.com/ai-personas/ai-personas-design/blob/f4549bd594e6a0cf5205ac031ed422ab269def8d/design/FRAGMENT-RECALL-VISUALS.md), [asset directory](https://github.com/ai-personas/ai-personas-design/tree/f4549bd594e6a0cf5205ac031ed422ab269def8d/assets), and [editable-artwork directory](https://github.com/ai-personas/ai-personas-design/tree/f4549bd594e6a0cf5205ac031ed422ab269def8d/assets/visuals) preserve every original image and its notes: five raster posters, five SVG posters, seven general diagrams, five fragment-recall diagrams, and the former asset indexes.

The collection is retired from the active reading path. Several graph/selector sheets conflict with the adopted mechanism; other general sheets duplicate the consolidated explanation. Historical rendering and integrity records remain attached to those exact versions. No unchanged retired figure is claimed as freshly rendered or visually validated.

The current [persona-files loop](../assets/persona-files-loop.svg) and its [accessible text guide](../VISUAL-GUIDE.md) replace the active atlas. The loop illustrates the target design; it is not a product screenshot or a record of executed behavior. Artwork presentation checks establish presentation only.

## Evidence is not inherited by editing

Editing a document changes its explanation, not the evidence for the system. The original sources included implementation observations, abstract checks, and authored scenarios. The historical ledger preserves the limits stated for each.

A documentation rewrite, new link, renamed file, or simplified figure is not a rerun, runtime audit, model evaluation, or demonstration of competence. Missing evidence remains missing. A reported failure remains a failure under its original criteria.

This consolidation does not choose licensing terms, reproduce private runtime data, publish credentials, or revive old branch instructions. The current public contract and any future measured claim remain reviewable on their own evidence.
