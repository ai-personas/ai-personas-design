# Implementing one coherent persona design

[Home](../README.md) · [Persona core](../design/PERSONA-CORE.md) · [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) · [Current status](STATUS.md)

The implementation target is a continuing persona with one accepted, versioned character account: semantic OCEAN stable traits and a VAD modeled affect profile. Its own-voice fragments are conditioned by that character and preserve truthful experience. Through a small file interface it can list, search, read, and edit those fragments, organize them for itself, and choose exact relevant prompt parts for its next ordinary decision. The primary LLM makes those semantic choices while doing useful work. Every application-visible LLM invocation acting as the persona receives maintenance input, and every accepted response returns a proposed patch, reasoned no change, blocked, or bounded deferred disposition alongside its work. The runtime keeps authority, observations, versions, restrictions, resources, and effects trustworthy.

A file-facing interface does not require a particular physical filesystem, database, language, provider, fixed taxonomy, association graph, personality score, or separate memory model. Conversely, presenting old records as files does not by itself establish simpler authorship, autonomous maintenance, or primary-owned context selection. Those behaviors need actual evidence.

## Read, decide, and demonstrate

| Purpose | Read | Evidence or decision needed |
|---|---|---|
| Understand the persona | [Persona core](../design/PERSONA-CORE.md) | A single accepted account of traits and modeled affect, own-voice fragments, every-invocation maintenance, learning, files, selection, and correction. |
| Preserve the foundation | [Invariants and requirements](REQUIREMENTS.md) and [work boundaries](../design/WORK-AND-BOUNDARIES.md) | Every applicable obligation has an identifiable owner; no hidden workflow or omitted safeguard. |
| Define reliable handoffs | [Contracts](CONTRACTS.md) | Exact meanings, accepted state changes, failure paths, current authority, recovery, and inspectable context. |
| Choose the actual scope | [Deployment decisions](DEPLOYMENT-DECISIONS.md) | Explicit environment, storage, model, permissions, resource and retention policies, supported effects, and exclusions. |
| Establish mechanisms | [Mechanical acceptance](../evaluation/ACCEPTANCE.md#mechanical-checks) and its file/context refinements | Actual implementation evidence at exact revisions, including adverse cases and unrun gaps. |
| Establish useful behavior | [Evaluation method](../evaluation/README.md) and [behavioral acceptance](../evaluation/ACCEPTANCE.md#behavioral-checks) | Real work plus matched character, learning, organization, cooperation and cost comparisons. |
| Make a scoped claim | [Status](STATUS.md) and [historical mapping](../evaluation/HISTORICAL-RESULTS.md) | Current evidence separated from prior criteria, claims, failures and remaining gates. |

The protected invariants, persona core, work boundaries, and contracts must agree. Acceptance describes what evidence would demonstrate them; it cannot quietly impose an unrelated cognitive architecture. Overview, examples and history explain these rules rather than override them.

## Start with a useful continuing collaborator

A small implementation can support one persona accepting a bounded request, using its current character and relevant selected fragments, producing an authorized result alongside an explicit maintenance decision, and continuing to a later task. A concise reasoned no change can leave all files intact. It need not create a community, recruit a team, assign professions, or install a fixed domain pipeline.

Then demonstrate a genuine peer-finding-to-work-change-to-check chain and matched later transfer. Enabled recruitment, birth, ongoing services, governance, physical effects, and cross-host activation need their own applicable contracts and evidence. These are scope choices, not obligatory development ceremonies or a promise that more personas improve work.

A persistent-collaborator scope includes identity, files, primary context choice, bounded work, and applicable safeguards. A cooperative scope adds actual accepted shared responsibility and communication. Community, ongoing and physical scopes add the corresponding obligations. Disabled features remain honestly unavailable; no profile excuses an obligation already created by enabled work.

## Keep semantic work with the persona

The runtime can enforce exact references, source access, current constraints, accepted responsibility, complete declared qualifications, spending and stale-action rejection. It cannot mechanically certify that free prose is honest, a skill applies, a selected fragment is relevant, a peer is competent, or an output is good.

Do not restore removed complexity behind an adapter that invents applicability, summaries, identity changes, or next-context meaning. A discovery aid can offer candidates; final semantic selection remains with the primary persona. An independent profile writer, reflection author, or final semantic selector is not part of this target. No edit, empty optional selection, deliberate retirement, and a justified stop are valid outcomes when their distinct explicit contracts are met. Omitted next-context changes may preserve existing selection; omitted maintenance cannot masquerade as an authored no-change decision.

Stable traits, transient modeled affect, and expression stay separate. Optional operational tendencies can help explain choices about tools, initiative, consultation, coordination, and reflection. They cannot change authority, competence, required checks, or resource limits. A display and a prompt use the same accepted account, with separately accepted current affect attributed consistently rather than independently rewritten.

Choose and test storage separately. Exact identity can survive a rename, while a stable filename can point to changed content. Atomicity, revision checks, source ancestry, retention, and recoverable accepted state remain necessary regardless of backend. A shared host account or tools folder is not a confidentiality boundary.

## Cover all persona call paths

Start from an audited inventory of application-visible persona LLM entry points. Include generated initialization, ordinary work, orientation, retrieval and selection choices, capability reasoning, communication, coordination, tool-result follow-ups, reorganization, and model-based repair. A deterministic tool execution is not itself a persona invocation. A declared non-persona utility returns an attributed observation and cannot assume the persona's authorship or selection authority. Provider-internal computation is outside the observable application boundary; opaque managed agent loops need equivalent exposed controls before claiming full coverage.

Initialization identifies the seed's author and the absence of prior learned experience. Restricted repair receives only permitted context and retains its restricted action scope. Maintenance input does not justify restoring withdrawn sources or changing locked character to make a request fit. Every new persona repair attempt carries the same obligation, finite resources, and honest attempt history.

Validate the combined response before substantive dispatch. Failure, truncation, refusal without a usable maintenance response, or missing disposition never receives a host-authored no-change substitute. A well-formed response with a rejected patch has a different status from a malformed response; the [contracts](CONTRACTS.md) define when independent work can still proceed. After an accepted effective-current-character change, fresh decision-making under that state precedes every further operation from the old response, including reads and waits. Normal transient affect updates do not automatically constitute protected character changes.

Keep host cancellation, admission fencing, accounting, and late receipt handling independent of successful model output. Bound both repair spending and unresolved maintenance lifecycles; reaching a limit yields an explicit unresolved or blocked outcome. Local acceptance and external dispatch remain different boundaries, with uncertain effects reconciled before retry. These are implementation obligations to demonstrate, not a promise of 100% model compliance.

## What a release needs

Publish only the supported scope and exact evidence: implemented mechanisms, executed checks, actual behavioral demonstrations, comparative outcomes, failures, total cost and remaining deployment decisions. A clean build, a document review, a pushed commit and a deployed process are separate milestones. None can substitute for useful persona behavior or independently checked task quality.

Historical graph and selector mechanisms may be implementation starting points or explicit research comparators. They neither obstruct adoption of the simpler current design nor establish that the new design already works. Preserve their original results and record actual transitions instead of hiding or regrading them.
