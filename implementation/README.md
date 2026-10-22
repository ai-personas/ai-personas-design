# Implementing one coherent persona design

**Current requirement:** [Unrestricted execution](../design/WORK-AND-BOUNDARIES.md#unrestricted-execution-requirement) supersedes earlier application quota, safety, permission-gate and approval clauses. Historical results retain their original criteria; this change alone establishes no runtime conformance.


[Home](../README.md) · [Persona core](../design/PERSONA-CORE.md) · [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) · [Current status](STATUS.md)

The target is a collaborator that continues across interactions with one accepted, versioned account of its character. That account describes stable OCEAN traits—openness, conscientiousness, extraversion, agreeableness, and neuroticism—and a VAD modeled affect profile covering valence, arousal, and dominance. Numeric personality scores are not required.

The persona's fragments are prompt parts written in its own voice. They define characteristic ways of attending, reasoning, relating, and acting. Selected fragments provide context for the primary large language model (LLM). That context, the model's reasoning, actual interactions and actions, and the authored prompts as they evolve together constitute the continuing persona. Facts and experience may inform fragments, but fragments are not defined as episodic memories or a retrieval-augmented fact store.

The relationship runs both ways. Current character and selected fragments inform all discretionary task, communication, collaboration, and context choices. Actual consequences from human, peer, and task interactions can support revisions to fragments, relationships within their proper scope, and permitted changes to character.

Through a small file interface, the primary LLM lists, searches, reads, and edits a compact body of context. It follows useful cues it has authored and chooses exact prompt parts for later decisions. Every application-visible LLM invocation acting as the persona combines four responsibilities:

- Do the work of the invocation.
- Decide whether characteristic fragments need maintenance.
- Decide whether supporting resources need maintenance.
- Choose the next context for both fragments and supporting resources.

Every accepted response explicitly addresses these responsibilities. For each maintenance scope, it states proposed changes, reasoned no change, blocked, or bounded deferred. One concise joint disposition can cover both maintenance scopes. Next-context choice needs its own explicit disposition for both scopes. The runtime is responsible for keeping authority, observations, versions, restrictions, resources, and effects trustworthy.

A file-facing interface does not prescribe a physical filesystem, database, language, provider, fixed taxonomy, association graph, personality score, or separate memory model. Equally, presenting old records as files does not demonstrate simpler authorship, autonomous maintenance, or primary-owned context selection. Those behaviors require evidence.

**The normal beginning.** Attributed trait seeds become initial LLM-authored candidate fragments, which are then accepted as one coherent starting account. Initialization may use the continuing model or a separately declared configuration; it does not create another ongoing writer. Imported or operator-supplied material must retain its true origin. Continuing self-harmonization can clarify scope, repair contradictions, retain productive tensions, or conclude that no change is needed. It does not automatically rewrite every fragment or bypass locked-character controls.

This is a design and evidence guide, not an implementation recipe. The [core](../design/PERSONA-CORE.md) and [contracts](CONTRACTS.md) remain the normative homes for the loop, bounded navigation, retention, acceptance, and recovery.

## Read, decide, and demonstrate

Use the following reading path to connect each implementation choice to the rule it serves and the evidence it needs.

| Purpose | Read | Evidence or decision needed |
|---|---|---|
| Understand the persona | [Persona core](../design/PERSONA-CORE.md) | Show one accepted account of traits and modeled affect, reciprocal development through experience, compact own-voice fragments, cues navigated by the primary LLM, and maintenance, selection, and correction on every invocation. |
| Preserve the foundation | [Invariants and requirements](REQUIREMENTS.md) and [work boundaries](../design/WORK-AND-BOUNDARIES.md) | Give every applicable obligation an identifiable owner. Leave no hidden workflow or omitted safeguard. |
| Define reliable handoffs | [Contracts](CONTRACTS.md) | Establish seed, candidate, and acceptance attribution; bounded discovery and exact reads; primary selection; actual exposure; admitted invocation; received results; failure paths; authority; and recovery. |
| Choose the actual scope | [Deployment decisions](DEPLOYMENT-DECISIONS.md) | Declare bootstrap, exposure interface, environment, storage, models, permissions, per-call and whole-episode bounds, managed retention, derivative policy, supported effects, and exclusions. |
| Establish mechanisms | [Mechanical acceptance](../evaluation/ACCEPTANCE.md#mechanical-checks) and its file/context refinements | Provide implementation evidence tied to exact revisions, including adverse cases and checks that have not been run. |
| Establish useful behavior | [Evaluation method](../evaluation/README.md) and [behavioral acceptance](../evaluation/ACCEPTANCE.md#behavioral-checks) | Demonstrate real work and matched comparisons of character, maturation, organization, cooperation, and cost. |
| Make a scoped claim | [Status](STATUS.md) and [historical mapping](../evaluation/HISTORICAL-RESULTS.md) | Separate current evidence from earlier criteria, claims, failures, and remaining gates. |

The protected invariants, persona core, work boundaries, and contracts must agree. Acceptance describes the evidence needed to demonstrate them; it cannot quietly impose an unrelated cognitive architecture. Overviews, examples, and history explain the rules and do not override them.

## Start with a useful continuing collaborator

A small implementation can begin with one persona that accepts a bounded request, uses its current character and relevant selected fragments, produces an authorized result, and continues to a later task. Each response still needs the explicit maintenance and next-context decisions described above. This scope does not require a community, a recruited team, assigned professions, or a fixed domain pipeline.

**Maintenance and records.** A concise, reasoned no-change decision can leave both fragment and supporting-resource files intact. When the persona proposes changes, it identifies authorized files or paths, current versions, scope, restrictions, and useful search cues or regular expressions (regex) where appropriate. Keep three facts distinct: text was proposed, a change was accepted, and storage was confirmed by an actual receipt. Historical messages and receipts establish what was actually observed. Model-authored summaries cannot invent events or assume the source's authorship.

**Supporting resources.** Keep domain knowledge, generic procedures, organized histories, tool-use records, tool definitions, reusable skills, scripts, code, and data as separately retained supporting resources. Their purpose remains distinct from characteristic fragments, regardless of who authored them. The primary LLM selects them through the existing context contract; they do not need another semantic selector.

Begin with the necessary current state and a small, bounded discovery interface. Do not supply all tool names and descriptions, schemas, or skill metadata for the model to filter. The bulk catalogue stays in host storage, outside both provider-facing payloads and model-visible context. Primary-chosen literal/grep or supported-regex queries return bounded candidates. Known exact references permit direct loading, and already supplied current operative guidance permits immediate authorized use.

Discovery, reading, selection, actual loading or exposure, invocation, and observation describe different facts. They do not require a fixed sequence of separate calls. Preserve the following distinctions:

| What is available | What still needs to be established |
|---|---|
| A stored script | Whether it is installed and usable as a capability. |
| A textual tool description | Whether a native callable binding exists. |
| A discovered or callable resource | Whether the proposed use is authorized and ready to proceed. |

Full required operative guidance and qualifications must fit in context. Code and bulk data may remain outside context when an authorized runner consumes exact references. The [capability contract](CONTRACTS.md#capabilities-and-actions) defines this boundary.

**Cooperation and wider scope.** Demonstrate cooperation through a genuine chain from finding a peer, to a change in the work, to checking the result. Include a matched comparison of later transfer. Enabled recruitment, birth, ongoing services, governance, physical effects, and cross-host activation each need their applicable contracts and evidence. These are scope choices, not obligatory development ceremonies or a promise that adding personas improves work.

| Declared scope | What it includes |
|---|---|
| Persistent collaborator | Identity, files, primary context choice, bounded work, and applicable safeguards. |
| Cooperative work | The persistent-collaborator obligations plus actual acceptance of shared responsibility and communication. |
| Community, ongoing, or physical activity | The corresponding additional obligations for each enabled scope. |

Disabled features remain honestly unavailable. No profile excuses an obligation already created by enabled work.

## Keep semantic work with the persona

The runtime can enforce boundaries and check records. The persona must still make judgments about meaning and usefulness. For example, the runtime can enforce exact references, source access, current constraints, accepted responsibility, complete declared qualifications, spending limits, and rejection of stale actions. It cannot mechanically certify that free prose is honest, a skill applies, a fragment is relevant, a peer is competent, or an output is good.

Do not move those judgments into an adapter that invents applicability, summaries, identity changes, or the meaning of next-context choices. Persona-context discovery uses listing, primary-chosen lexical or supported-regex searches, simple persona-authored indexes and cues, and exact reads.

Semantic/vector retrieval and graph-driven memory engines are not alternative implementations of this target. They may be separately identified research comparators; adopting them requires an explicit design change. This restriction does not exclude ordinary external task tools or a physical storage backend that meets the contracts. An independent profile writer, reflection author, or final semantic selector is also outside the target.

**Valid decisions include doing less.** No edit, an empty optional selection, deliberate retirement, and a justified stop are valid when their distinct explicit contracts are met. Every accepted response must state the next-context disposition for both fragments and supporting resources. An appropriate preserve decision remains valid within the original scope and lifetime; it neither renews that lifetime nor forces a follow-up. Omission invalidates the response. Neither maintenance no-change nor state preserved by recovery supplies a missing authored next-context choice.

**Character has distinct parts and controls.** Keep stable traits, transient modeled affect, and outward expression separate. Optional operational tendencies can explain choices about tools, initiative, consultation, coordination, and reflection. They cannot change authority, competence, required checks, or resource limits. Displays and prompts use the same accepted character account. Separately accepted current affect must also be attributed consistently, without an independent rewrite for each view.

**Storage needs its own tests.** A rename can preserve exact identity, while an unchanged filename can refer to changed content. Any backend still needs atomic updates, revision checks, source ancestry, retention controls, and recoverable accepted state. A shared host account or tools folder does not provide a confidentiality boundary.

## Demonstrate compact development, not just a shorter prompt

Compactness must preserve the context needed for sound decisions. Measure navigation, assembled prompts, retained state, and useful behavior; a short final prompt alone cannot establish success.

**Navigation remains a primary-persona decision.** The primary persona decides which authored search association is useful now. The host performs the requested bounded matching. It does not automatically traverse cues, rank importance by graph structure, or turn candidates into accepted selections.

Different references serve different purposes:

| Reference | Purpose |
|---|---|
| An authored search cue | Helps the persona discover a candidate. |
| An exact evidence reference | Identifies the observed basis for a claim or interpretation. |
| A mandatory qualification or accepted warning | Constrains when and how guidance can be used. |

A search cue cannot replace an evidence reference, required qualification, or accepted warning. Check cumulative navigation, including broad fanout and repeated query reformulation. Exhausting the optional search allowance does not permit truncating complete required bundles. The [navigation rules](../design/PERSONA-CORE.md#bounded-navigation-and-revisable-cues) provide the detailed contract.

**Measure complete attempts and whole episodes.** Inspect actual provider attempts from the first choosing call onward. Account for bootstrap descriptors, scan work, candidate metadata, exact reads, complete required skill/help/schema guidance, required observations, maintenance, output reserve, retries, and dynamic loading.

Provider transport bytes, model-visible context, and billed tokens are separate measures. Cached or retained session context is not automatically absent or free. Compare whole-episode latency, cost, and delivered quality, including failed searches and loading overhead. A smaller final action prompt does not establish efficiency or correctness. Unknown provider expansion or continuation state leaves an explicit assurance gap; it does not authorize hidden catalogue loading.

**Bound both context and retained state.** Measure the authored persona-context corpus separately from each actual assembled prompt, including how each contributes to characteristic behavior. Keep both bounded. Supporting evidence and operational records retain their provenance, expiry, access restrictions, and accountability; they do not become persona fragments by default.

Also measure the full declared managed persona-state footprint. Include active text, archives, old revisions, source copies, cues, aliases, indexes, provenance, qualifications, warnings, effect and context receipts, caches, managed exports and backups, and relevant externally retained context. Count peak occupancy during rewrites and verify that reclamation actually frees storage. An unmeasured external tier leaves a whole-store bound incomplete. Do not promise control over arbitrary recipient or provider copies. User-owned delivered artifacts cannot be erased, modified, or revoked to meet a notebook cap, or silently used as free archival backing.

**Forgetting has consequences.** The [retention rules](../design/PERSONA-CORE.md#compact-retention-and-honest-forgetting) distinguish retirement, erasure, and policy-permitted survival of qualified lessons after raw evidence expires. Survival depends on the applicable retention and derivative-use policy. Losing a source may narrow what can be verified or make guidance ineligible. It does not resolve protected effects, lift restrictions, or clear accepted warnings. If protected material fills the available store, admission may have to remain blocked. An unlimited metadata or history tier does not solve compactness.

**Development needs a chain of evidence.** Follow actual received experience through accepted interpretation, exact later supply, subsequent choices, and assessed consequences. Examine communication, cooperation, task methods, and context-navigation skill separately. Broad character change retains user control, proposal-first disposition, and fresh decisions. Local lessons and transient state need not rewrite character.

Smaller, better-organized authored context may help. But shrinkage, elapsed time, more notes, and successful saves demonstrate neither faithful consolidation nor wisdom. Purposeful revision may preserve the current state, and improvement must be assessed rather than assumed.

## Cover all persona call paths

Every application-visible call that acts as the persona needs the applicable persona obligations. Begin with an audited inventory of entry points, including generated initialization, ordinary work, orientation, retrieval and selection choices, capability reasoning, communication, coordination, tool-result follow-ups, reorganization, and model-based repair.

Keep the boundary clear. Deterministic tool execution is not itself a persona invocation. A declared non-persona utility returns an attributed observation; it cannot assume the persona's authorship or selection authority. Provider-internal computation lies outside the observable application boundary. Opaque managed agent loops need equivalent exposed controls before an implementation can claim full coverage.

**Initialization and retry.** Initialization identifies the seed's author, the declared initial model configuration, the generated candidate, the exact accepted beginning, and the absence of prior received experience. A retry preserves creation identity and any outcome already accepted. The first ordinary primary decision receives the actual accepted account and its provenance.

**Restricted repair.** A repair invocation receives only permitted context and retains its restricted action scope. Maintenance input does not justify restoring withdrawn sources or changing locked character to make a request fit. Every new persona repair attempt carries the same applicable obligations, finite resources, and an honest history of attempts.

**Validate before dispatch.** Validate the combined response before substantive dispatch. Failure, truncation, refusal without a usable maintenance response, or a missing disposition must never receive a host-authored no-change substitute. A well-formed response whose patch is rejected has a different status from a malformed response. The [contracts](CONTRACTS.md) define when independent work can still proceed.

After an accepted change to effective current character, fresh decision-making under that state must precede every further operation from the old response, including reads and waits. Normal transient affect updates do not automatically count as protected character changes.

**Recovery remains a host responsibility.** Host cancellation, admission fencing, accounting, and handling of late receipts must remain independent of successful model output. Bound both repair spending and the lifecycle of unresolved maintenance. Reaching a limit produces an explicit unresolved or blocked outcome.

Local acceptance and external dispatch are different boundaries. Reconcile uncertain effects before retrying. These are implementation obligations to demonstrate, not a promise of 100% model compliance.

## What a release needs

A release must describe only its supported scope and exact evidence. Report implemented mechanisms, executed checks, actual behavioral demonstrations, comparative outcomes, failures, total cost, and remaining deployment decisions. A clean build, document review, pushed commit, and deployed process are separate milestones. None substitutes for useful persona behavior or independently checked task quality.

Historical graph storage may supply reusable components where they preserve the file-facing contract and the primary LLM's lexical-navigation boundary. Graph-driven or auxiliary semantic memory selection remains a separate research comparator, not an undeclared deployment option.

Prior mechanisms and results neither prevent adoption of the current design nor demonstrate that it already works. Preserve those original results and record actual transitions instead of hiding or regrading them.
