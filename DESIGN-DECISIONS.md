# Design decisions

[Home](README.md) · [Normative reference](design/README.md) · [Source provenance](sources/SOURCE-MANIFEST.md)

This register explains the current target adopted in this branch. It replaces the earlier practice of adding successive normative clarifications beside conflicting manuals. Adoption changes the design reference; it does not establish runtime implementation, useful learning, or deployment approval.

The [normative documents](design/README.md) contain the actual obligations. This register records why those obligations have their present form.

## 8 October 2026: semantic character and every-invocation maintenance

This refinement deliberately reverses two norms in the 7 October edition: that OCEAN/VAD descriptors could be omitted, and that an ordinary persona response could omit any authored maintenance disposition. Those norms remain part of the design's history; they are not options in the current target. This is not a return to compulsory numeric personality initialization, typed mental-function taxonomies, or forced lessons.

The current target requires semantic coverage of OCEAN's five relatively stable trait domains and a VAD modeled affect profile in one accepted, versioned character account. Stable tendencies, affective baseline, transient situation-linked affect, and outward expression remain distinguishable. Scores are optional engineering representations with declared meanings; the design does not claim psychometric measurement of an AI or a scientific conversion from traits to actions. A profile and the decision prompt resolve the same accepted account, without independent writers.

Every application-visible LLM invocation acting as the persona receives maintenance input and returns an explicit disposition alongside its other work. A proposed patch, no change with a concise reason, an explicit block, or a bounded deferral can satisfy the response obligation. Mutation is selective. Provider failure or missing output cannot satisfy it by having the host invent a no-change judgment. Exact coverage, acceptance, and recovery live in the [core](design/PERSONA-CORE.md) and [contracts](implementation/CONTRACTS.md), not in this register.

The rationale is inspectable continuity: make the intended character explicit and make maintenance omissions detectable while leaving ordinary work, interpretation, file organization, and next-context choice with the persona. This adds prompt and response overhead and possible repair cost. Whether it improves useful behavior requires comparison, including truthful no-change, delayed correction, harmful transfer, and total cost. It is a design choice informed by the [research synthesis](sources/PERSONA-FILES-RESEARCH.md), not a result established by that research or a guarantee of successful output on every attempt.

## The adopted persona model

| Decision | Reason and consequence |
|---|---|
| A persona is a continuing character whose choices can develop through experience | Recognizable interests, approaches, relationships, and continuity should influence actual work. A name, biography, role, or style alone does not demonstrate individuality |
| One accepted character account includes semantic OCEAN and VAD | All five stable trait domains and all three modeled affect dimensions have meaning. Optional facets or operational tendencies may clarify tool/action, collaboration, coordination, and reflective preferences; no extra taxonomy or scores are compulsory |
| Every authored fragment is character-conditioned and own-voice | The persona expresses how it understands itself, a situation, a method, or a relationship. Exact facts and quotations retain their form and attribution; supplied initialization remains distinguishable from subsequent self-authorship |
| Ordinary files are the canonical authoring surface | The persona may organize, search, grep, revise, combine, split, and retire its fragments using simple tools. No canonical cognitive graph, fixed mental-function tree, or prescribed folder taxonomy is required |
| The primary LLM chooses relevant next-context fragments while doing work | Finding or reading material is distinct from choosing it for later context. Explicit next-context intent persists within its scope, can be replaced or cleared, and remains subordinate to current access and obligations |
| Work and explicit maintenance share every persona invocation | Every admitted persona call has maintenance input; every accepted response includes a patch, reasoned no change, blocked, or bounded deferred disposition. There is no mandatory extra reflection call, separate memory author, or compulsory mutation |
| Character can evolve without becoming arbitrary | Stable traits change through authorized, attributable self-authorship. Transient affect and ordinary learning do not automatically rewrite those traits. Effective-current-character changes retain the fresh-decision fence for all subsequent operations, including reads and waits; locked character cannot be replaced through another fragment |
| The host protects operational truth rather than supplying a hidden mind | It enforces ownership, current permissions, evidence, resource limits, qualification, and reliable effects. It does not turn a retrieved sentence into authority or choose a hidden profession, task workflow, or personality quota |
| Learning requires demonstrated transfer | Retention, reading, selection, prompt inclusion, behavioral influence, and beneficial effect are separate claims. Useful learning must survive appropriate later tasks, comparisons, and cost accounting |

“Human-like” refers to observable character, relations, choices, learning, and continuity. It does not depend on proving consciousness, claiming a human biography, or asserting human equivalence.

## Conflicting cognitive obligations that are superseded

These are deliberate design changes, not accidental losses caused by moving files.

| Earlier obligation or interpretation | Current disposition |
|---|---|
| A canonical ungrouped fragment graph with graph navigation as the defining representation | Superseded by persona-owned files. Links and indexes may help navigation but do not become the canonical cognitive substrate or an obligatory mental ontology |
| Stored conditional-recall plans or graph neighborhoods automatically choosing optional context after an event | Replaced by actual events reaching the primary persona, which can reconsider and choose next fragments. Trusted delivery of current obligations remains mandatory; a saved interest is not a wake trigger |
| A Jev-style or other auxiliary semantic selector as a normal recall component | Removed from the active target. The primary LLM owns next-context choice. Earlier selector mechanisms and results remain historical evidence under their original criteria |
| A universal typed cognitive package or fixed categories for all persona state | Superseded by flexible first-person fragments. Precise host bookkeeping is retained for safety and accountable work, without prescribing how a persona must think |
| Mandatory numeric starting traits or personality-to-affect formulas | Numeric scores remain optional; declared anchors do not make them validated psychological measurements or action rules |
| The 7 October treatment of OCEAN and VAD as entirely optional descriptors | Superseded on 8 October. Semantic OCEAN stable traits and a VAD modeled affect profile are required within the one accepted character account |
| The 7 October permission to omit an authored maintenance disposition | Superseded on 8 October. Every accepted persona response includes explicit maintenance alongside its work; a concise reasoned no change is valid, silence is not |
| A compulsory mutation or fresh next-context declaration on every response | Still rejected. Explicit maintenance need not change files or selection. Existing selection retains the core's preserve, replacement, clearing, scope, and expiry meanings |
| The previous files proposal's target of no persistent next-context selection | Superseded. The persona can explicitly choose fragments to inform a later relevant decision. A simple read still does not silently establish that choice |
| Mandatory current repetition of every durable record in every prompt | Rejected. Relevant current constraints remain protected, while optional history and instructions are selected within a bounded context |
| Retrieved or rewritten memory as self-validating evidence | Rejected. Authored interpretation remains distinguishable from raw observations, sources, and permissions; necessary qualifications accompany its use |

The 8 October requirements sit within the files architecture adopted in the earlier consolidation. They preserve the useful causal idea behind fragments: the persona can carry forward its own relevant understanding and use it to work differently. They remove mechanisms that made the representation more elaborate than that goal requires.

A future alternative may be evaluated as an explicitly separate experiment. It must not be inserted as another active authority while this target remains unchanged.

## Safeguards carried into the consolidated design

Simplifying persona memory does not remove the following obligations. The [requirement catalogue](implementation/REQUIREMENTS.md) keeps the protected I01–I21 invariants and traces the continuing requirement families; the [system contracts](implementation/CONTRACTS.md) provide the corresponding handoffs.

| Protected meaning | Current home |
|---|---|
| Original need, accepted changes, conditional assumptions, outcome coverage, and accepted continuation responsibility | [Work and boundaries](design/WORK-AND-BOUNDARIES.md), NED and COL requirements |
| Distinct identity, truthful creation, bounded orientation, voluntary membership, exact acceptance, withdrawal, retirement, and accountable handoff | [Persona core](design/PERSONA-CORE.md), [work and boundaries](design/WORK-AND-BOUNDARIES.md), PER and COL requirements |
| Source scope, interpretation versus observation, ownership, revision, correction, necessary qualifications, and private-memory limits | [Persona core](design/PERSONA-CORE.md), [system contracts](implementation/CONTRACTS.md), MEM and UX requirements |
| Current authority, descendant grants, revocation, information restrictions, and actual execution boundaries | [Work and boundaries](design/WORK-AND-BOUNDARIES.md), [system contracts](implementation/CONTRACTS.md), GOV and ACT requirements |
| Root-budget conservation, reservations, uncertain exposure, shared exploration allowances, protected review and closeout, and fair bounded continuation | [Work and boundaries](design/WORK-AND-BOUNDARIES.md), [system contracts](implementation/CONTRACTS.md), GOV requirements |
| One current decision authority, stale-writer exclusion, attributable admission, retry-safe local transitions, unknown external effects, and restart recovery | [System contracts](implementation/CONTRACTS.md), SYS and ACT requirements |
| Actual observation before dependent action, usable capabilities and references, exact artifacts, review applicability, and coherent release | [Work and boundaries](design/WORK-AND-BOUNDARIES.md), [system contracts](implementation/CONTRACTS.md), ACT and EVD requirements |
| Human control, faithful status and stopping reasons, privacy across derivatives, real stakeholder participation, and feature-specific safeguards | [Work and boundaries](design/WORK-AND-BOUNDARIES.md), [deployment decisions](implementation/DEPLOYMENT-DECISIONS.md), SOC, UX, SRV, and PHY requirements |
| Versioned criteria, negative results, comparison scope, and separation of mechanism, behavior, benefit, and deployment evidence | [Evaluation guide](evaluation/README.md), [historical results](evaluation/HISTORICAL-RESULTS.md), OSS requirements |

These homes carry the rules forward. A link to an old document alone would not do so. Retired manuals supply historical provenance, not extra active obligations or exceptions.

## Implementation choices no longer fixed by the handbook

Several earlier refinements prescribed a particular launch or recovery mechanism. Their useful guarantees are retained, but the mechanism is now an explicit implementation or deployment choice:

| Earlier concrete choice | Required outcome and current disposition |
|---|---|
| Resetting host-tool availability on ordinary CLI launch | The deployment declares its actual execution boundary and enabled capabilities. A restart cannot silently expand access or misrepresent disabled operations as usable |
| Coupling automatic avatar generation to particular model availability | Creation remains attributable, bounded, and honest about actual image generation. Optional presentation does not block a useful persona or prove its character |
| An exact two-call maintenance allowance | Maintenance is bounded, accountable, and able to return control or a truthful blocker. The concrete allowance is chosen and evaluated for the implementation; it is not a universal cognitive law |
| Fixed selector packets, candidate counts, or cache constants | They belong to the historical selector architecture. Current file discovery and assembly expose their real bounds, freshness, omissions, and costs without inheriting those constants |

A documented initial deployment default is distinct from a later explicit operator choice. The current target does not permit ordinary restart to silently override that later choice. This documentation revision does not change or verify the existing launcher; the [implementation gap](implementation/STATUS.md) remains explicit.

Choosing a different mechanism does not retire source restrictions, necessary qualifications, exact acceptance, conserved resources, or reliable effects. A deployment must document and demonstrate the outcome under its selected mechanism. See [deployment decisions](implementation/DEPLOYMENT-DECISIONS.md) and [system contracts](implementation/CONTRACTS.md).

## Why the contract considers every call but does not force a write

A separate post-task reflector can miss initialization, retrieval-only choices, communications, and repair calls. A compulsory write on each call instead encourages filler, repeated interpretations, and unjustified character drift. The adopted contract makes consideration explicit in the same persona's response, with no-change as a legitimate result. This neither requires an extra call nor grants new permission to make one.

A known unresolved correction requires a bounded deferral or block with an accepted continuation or an explicit ownership gap; expiry is not an invented decision that nothing changed. Ending the repair effort also cannot clear a separately authorized, durably accepted applicability warning on exact affected guidance; the warning remains qualified or ineligible across later work until its own justified resolution. A failed patch creates no warning by itself, and restricted modes gain no new semantic authority. Refusal, timeout, truncation, and malformed output retain their actual attempt outcomes. A malformed combined response releases no substantive task, tool, or communication proposals. Deterministic cancellation, receipt preservation, and resource accounting remain possible without model success. The contracts separately distinguish a well-formed response containing a rejected patch from an invalid response, so genuinely independent work is not blocked by an invented blanket rule.

An actual request to adopt a changed effective character is resolved before any other fresh operation from that response. Otherwise, merely processing an independent read or action first could evade the intended fresh-decision boundary. Acceptance activates the fence; a definite no-commit rejection or deferral leaves only the existing independently valid work path; an unknown commit holds new work for reconciliation. The necessary character-resolution transaction and independent host duties remain possible. Thinking about a possible future change is not itself an adoption request, and ordinary method or scoped affect updates do not automatically invoke this character-specific barrier.

Application-visible call coverage includes initialization, planning, search and selection, tool-result interpretation, communication, coordination, and model-based maintenance or recovery. Restricted repair remains restricted: it does not gain authority to change locked character, disclose inaccessible material, or do substantive work. A narrowly scoped non-persona utility may return attributed observations, but a helper that judges or chooses as the persona is still covered. Provider-internal computation cannot be counted as an inspectable application invocation; an opaque provider-managed agent loop needs equivalent exposed controls before claiming coverage.

## Organization and methods remain persona-owned

Personas may plan, learn methods, find capabilities, ask peers for assessment, challenge one another, and accept specialized contributions. Those choices arise within the continuing persona and its work. The host does not prescribe a profession roster, permanent supervisor, fixed team size, compulsory reviewer, or universal priority formula.

A review already required by the accepted mandate remains required. A peer's optional suggestion does not automatically become a blocker. A native editable artifact, an analysis, a rendered view, and an outside approval are distinct results and need distinct evidence where requested. The earlier delivery addendum's separate DLV requirement family remains retired as redundant; its useful coverage and historical identifiers remain mapped in [historical results](evaluation/HISTORICAL-RESULTS.md).

The same distinction applies to execution. A deployment may deliberately expose ordinary host tools within its declared trust boundary. That does not create a universal entitlement to host access, erase isolation requirements for a different profile, or authorize a persona fragment to enable a disabled capability.

## Conditional scope and the historical extension labels

The earlier E1–E6 labels remain useful for locating past criteria. They are not six additional compulsory engines.

| Label | Current interpretation |
|---|---|
| E1 | Functional embodiment and an inspectable profile are explanatory ways to describe continuing observation, choice, and effects. Required semantic character remains part of the core; no numeric psychology, rich profile UI, or physical body follows |
| E2 | Communities, institutions, and appeals are conditional features. Actual human or institutional accountability and real stakeholder input remain necessary when enabled |
| E3 | Transparent AI presentation and safeguards for sensitive human-facing use apply to the intended deployment. Character does not establish suitability for those uses |
| E4 | Ongoing services and physical interfaces remain separately bounded features, with their own triggers, renewal, escalation, stopping, observation, and assurance requirements |
| E5 | Worksheets, identifiers, and conformance descriptions organize evidence. They do not require a small task to complete a large administrative process |
| E6 | Contributions, versioning, and public evidence claims preserve provenance and prior failures. Licensing and contribution terms require the owner's actual decision |

An implementation can omit a feature and state that limitation. Enabling it requires its applicable safeguards and evidence. The unresolved choices live in [deployment decisions](implementation/DEPLOYMENT-DECISIONS.md), not in an implied default approval.

## Editorial consolidation and historical evidence

Earlier OCEAN/VAD implementation features and ordinary-call continuity mechanisms are not erased by these design changes; the [status ledger](implementation/STATUS.md) separates source-inspected partial mechanisms from unassessed universal coverage. Old results retain their exact evaluator and cannot acquire a new pass through changed wording.

The active structure now consists of one core, one work-and-boundaries account, one system contract, and supporting traceability and evaluation documents. The previous proposal, seven chapters, overlapping refinements, graph-recall atlas, and old source briefs are removed from active navigation and files. Their exact earlier revisions remain linked in [source provenance](sources/SOURCE-MANIFEST.md).

Historical reports keep their original evaluator definitions, configuration, and limitations. In particular, an old graph-recall mechanism result cannot be relabeled as a pass for the persona-owned files target, and a documentation check cannot be relabeled as a behavioral test.

## Changing this design

Follow [Contributing](CONTRIBUTING.md). Name the actual problem, the rule being changed, its affected identifiers, alternatives, consequences, and evidence needed. Reconcile all affected active views together. Preserve old criteria and results, and state the implementation gap separately from the design decision.
