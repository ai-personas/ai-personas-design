# Design decisions

[Home](README.md) · [Normative reference](design/README.md) · [Source provenance](sources/SOURCE-MANIFEST.md)

This register explains the current target adopted in this branch. It replaces the earlier practice of adding successive normative clarifications beside conflicting manuals. Adoption changes the design reference; it does not establish runtime implementation, useful learning, or deployment approval.

The [normative documents](design/README.md) contain the actual obligations. This register records why those obligations have their present form.

## The adopted persona model

| Decision | Reason and consequence |
|---|---|
| A persona is a continuing character whose choices can develop through experience | Recognizable interests, approaches, relationships, and continuity should influence actual work. A name, biography, role, or style alone does not demonstrate individuality |
| First-person fragments are the persona's own reusable prompt parts | The persona can express how it understands itself, a situation, a method, or a relationship in language it can use again. Supplied initialization remains distinguishable from subsequent self-authorship |
| Ordinary files are the canonical authoring surface | The persona may organize, search, grep, revise, combine, split, and retire its fragments using simple tools. No canonical cognitive graph, fixed mental-function tree, or prescribed folder taxonomy is required |
| The primary LLM chooses relevant next-context fragments while doing work | Finding or reading material is distinct from choosing it for later context. Explicit next-context intent persists within its scope, can be replaced or cleared, and remains subordinate to current access and obligations |
| Work, learning, and context choice can share one ordinary decision | There is no mandatory reflection call, separate memory author, or compulsory new fragment on every response. A useful no-change response is valid |
| Character can evolve without becoming arbitrary | The persona may revise its self-understanding in response to experience. The system preserves attribution and continuity; it does not reward unchanging mistakes as authenticity or silently rewrite the persona for a task |
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
| Mandatory numeric starting traits and current OCEAN or VAD state | Not required. A persona may use descriptive or quantitative aids where useful, but conformance and human-like character are not defined by those scales |
| A learning disposition and fresh next-context declaration on every ordinary response | Not required. Ordinary work can leave existing state unchanged. Existing context intent follows explicit preserve, replacement, clearing, scope, and expiry meanings; silence is not an invented memory or an unrestricted new selection |
| The previous files proposal's target of no persistent next-context selection | Superseded. The persona can explicitly choose fragments to inform a later relevant decision. A simple read still does not silently establish that choice |
| Mandatory current repetition of every durable record in every prompt | Rejected. Relevant current constraints remain protected, while optional history and instructions are selected within a bounded context |
| Retrieved or rewritten memory as self-validating evidence | Rejected. Authored interpretation remains distinguishable from raw observations, sources, and permissions; necessary qualifications accompany its use |

These changes preserve the useful causal idea behind fragments: the persona can carry forward its own relevant understanding and use it to work differently. They remove mechanisms that made the representation more elaborate than that goal requires.

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

## Organization and methods remain persona-owned

Personas may plan, learn methods, find capabilities, ask peers for assessment, challenge one another, and accept specialized contributions. Those choices arise within the continuing persona and its work. The host does not prescribe a profession roster, permanent supervisor, fixed team size, compulsory reviewer, or universal priority formula.

A review already required by the accepted mandate remains required. A peer's optional suggestion does not automatically become a blocker. A native editable artifact, an analysis, a rendered view, and an outside approval are distinct results and need distinct evidence where requested. The earlier delivery addendum's separate DLV requirement family remains retired as redundant; its useful coverage and historical identifiers remain mapped in [historical results](evaluation/HISTORICAL-RESULTS.md).

The same distinction applies to execution. A deployment may deliberately expose ordinary host tools within its declared trust boundary. That does not create a universal entitlement to host access, erase isolation requirements for a different profile, or authorize a persona fragment to enable a disabled capability.

## Conditional scope and the historical extension labels

The earlier E1–E6 labels remain useful for locating past criteria. They are not six additional compulsory engines.

| Label | Current interpretation |
|---|---|
| E1 | Functional embodiment and an inspectable profile are explanatory ways to describe continuing observation, choice, and effects. No required numeric psychology or physical body follows |
| E2 | Communities, institutions, and appeals are conditional features. Actual human or institutional accountability and real stakeholder input remain necessary when enabled |
| E3 | Transparent AI presentation and safeguards for sensitive human-facing use apply to the intended deployment. Character does not establish suitability for those uses |
| E4 | Ongoing services and physical interfaces remain separately bounded features, with their own triggers, renewal, escalation, stopping, observation, and assurance requirements |
| E5 | Worksheets, identifiers, and conformance descriptions organize evidence. They do not require a small task to complete a large administrative process |
| E6 | Contributions, versioning, and public evidence claims preserve provenance and prior failures. Licensing and contribution terms require the owner's actual decision |

An implementation can omit a feature and state that limitation. Enabling it requires its applicable safeguards and evidence. The unresolved choices live in [deployment decisions](implementation/DEPLOYMENT-DECISIONS.md), not in an implied default approval.

## Editorial consolidation and historical evidence

The active structure now consists of one core, one work-and-boundaries account, one system contract, and supporting traceability and evaluation documents. The previous proposal, seven chapters, overlapping refinements, graph-recall atlas, and old source briefs are removed from active navigation and files. Their exact earlier revisions remain linked in [source provenance](sources/SOURCE-MANIFEST.md).

Historical reports keep their original evaluator definitions, configuration, and limitations. In particular, an old graph-recall mechanism result cannot be relabeled as a pass for the persona-owned files target, and a documentation check cannot be relabeled as a behavioral test.

## Changing this design

Follow [Contributing](CONTRIBUTING.md). Name the actual problem, the rule being changed, its affected identifiers, alternatives, consequences, and evidence needed. Reconcile all affected active views together. Preserve old criteria and results, and state the implementation gap separately from the design decision.
