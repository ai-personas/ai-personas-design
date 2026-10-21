# Decisions required for a deployment

[Implementation guide](README.md) · [Contracts](CONTRACTS.md) · [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) · [Status](STATUS.md)

A deployment must turn the adopted persona design into a bounded, accountable operation and provide evidence that its chosen boundaries work. This register identifies the decisions needed to do that. It does not claim production readiness or report that the separate runtime already implements these choices.

The target is a continuing persona with one accepted, versioned character account. That account includes semantic OCEAN traits—openness, conscientiousness, extraversion, agreeableness, and neuroticism—and a VAD modeled affect profile covering valence, arousal, and dominance. These meanings are required; numeric representations are optional.

The primary LLM authors persona-defining prompt fragments that carry the persona's character. It uses bounded lexical and supported regex searches, chooses the next context, and explicitly addresses maintenance in every persona invocation. Current character and selected fragments inform all discretionary task and social choices. Actual experience may lead to revisions of compact retained context, scoped relationships, and permitted character. Tools, skills, domain knowledge, generic procedures, code, data, and histories remain supporting assets, regardless of who authored them.

A deployment must retain this design's semantic traits, modeled affect, every-invocation maintenance, and finite bounds on persona context and managed storage. For every decision below, record:

- The accountable owner and chosen policy or value.
- The rationale and exact effective version.
- Supporting evidence and remaining limitations.
- The conditions that would require reconsideration.

Until a required boundary is resolved and demonstrated, restrict the affected capability or keep it in a clearly described test environment.

## Core deployment choices

The design fixes the responsibilities below. Each deployment must specify how it meets them, what limits apply, and what evidence supports those limits.

![Identity, authority, source policy, capacity, scheduling and acceptance define a supported deployment envelope. Optional extensions retain their conditional safeguards without becoming universal requirements.](../assets/deployment-envelope.svg)

**Figure: Make deployment choices visible.** This is a conceptual explanation of the design. [Read the exact rules](DEPLOYMENT-DECISIONS.md#core-deployment-choices); the explanation below retains their qualifications. [Open the illustration](../assets/deployment-envelope.svg).

<details>
<summary>Text equivalent of the illustration</summary>

Make deployment choices visible

AN ILLUSTRATED DESIGN STORY

Which setting can we actually support?

People · limits Permissions Evidence

Decide the supported setting explicitly

Identity, permissions and audiences

Who owns the persona, who can authorize a change, which sources may be used and which recipients may receive them?

A viable operating envelope

Declare context, storage, resources, scheduling, repair and closeout capacity. Protected mandatory state must be supportable.

Acceptance and evidence

Choose criteria, review rights, assurance and relevant behavioral comparisons. Preserve exact evaluator and implementation scope.

Only the extensions actually enabled

Society, ongoing services, embodiment or between-task exploration are optional. When enabled, their applicable safeguards still apply.

An architectural design does not authorize a deployment. This is a map of decisions, not a universal product setup or research checklist.

Characters personify design choices; they do not assert feelings or consciousness. Scenes are hypothetical.

</details>

**Use, identity, and character.** Establish who the persona serves, how its accepted identity begins, and which later changes are permitted.

- **Intended use.** A domain-neutral design does not make every task feasible. Specify the users, supported tasks and results, exclusions, and any outside review needed for a particular claim.
- **Continuing identity.** Normally, attributed trait seeds become bounded initial LLM-authored candidate fragments and then one coherently accepted semantic OCEAN/VAD account shared by profile and prompt. Specify creation authority; provenance for the seed, candidates, and acceptance; initial and continuing model configurations; handling of sparse or conflicting seeds; identity across retries; truthful alternate origins; self-authorship and locked-character controls; the distinction between baseline and current state; handover; and lifecycle recovery.
- **Character representation.** Natural language is sufficient. Every persona-authored fragment must carry the owner's character and use its own voice. If the deployment adds facets or contextual operational tendencies, state their purpose. For any numeric anchors, declare provenance, display behavior, and validation. A profile must not become an independent character author, and traits must not become a deterministic action policy.
- **Experience-shaped development.** Actual consequences of tasks and human or peer interactions may inform later fragments, methods, navigation, relationships, and permitted current character. Specify user controls over self-authorship, and distinguish local methods and transient state from effective-character changes. Provide proposal-first handling, enforcement of fresh decisions, honest attribution of experience, and evidence about outcomes over time. Elapsed time or activity counts must not drive automatic aging, and the design excludes automatic weight training.
- **Modeled affect.** Keep baseline affect, transient state, outward expression, and authority distinct. Specify event and source attribution, update and recovery rules, state lifetime, uncertainty, expression limits, and consistent views tied to the same version. Any numeric dynamics are engineering choices that need testing; they are not established psychological laws.

**Primary work and maintenance.** The ordinary primary LLM owns judgment about work, maintenance, and the next context. A deployment must make those responsibilities reliable across short calls, continuing work, and repair.

- **Primary inference.** The primary LLM chooses work, fragment and asset maintenance, and the next relevant fragments and supporting resources. Declare the exact provider and model configuration, supported inputs and outputs, request bounds, refusal and failure behavior, cancellation, metering, and evidence of continuity.
- **Every-invocation maintenance.** Every persona call combines work, characteristic-fragment maintenance, supporting-resource maintenance, and next-context choice. A concise, explicit joint disposition may cover both maintenance scopes. Audit all call paths, including initialization and an empty store. Maintenance proposals must identify permitted files or paths and useful discovery cues. Provide exact receipts distinguishing accepted changes from stored changes, grounded historical records, handling for no change and deferral, permission-filtered repair, validation of the whole response, and bounds for non-persona utilities. Neither mutation nor a follow-up call is mandatory merely to satisfy maintenance.
- **Ordinary continuing work.** A local effort limit must not silently end an accepted continuing mandate. The primary retains ownership of semantic next-step choices. Specify effective continuation terms, durable eligibility and restart behavior, and scheduler fairness, capacity, and priority assumptions. Within the supported scope, persistently eligible obligations must eventually receive consideration. Include reconsideration of unanswered nonblocking questions and a policy for stopping or lack of progress. State supported capacity and how genuine blockers or missing continuation opportunities reach an accountable decision without polling, cap renewal or guaranteed success.
- **Maintenance bounds.** Mutation is selective, and a known unresolved candidate must not silently become “no change.” Specify repair-attempt limits, storage and context ceilings, the owner of a deferral or an explicit ownership gap, prerequisites, triggers, resource and lifecycle bounds, and terminal handling. Preserve independent host stopping and accounting behavior.

**Files, discovery, and exposure.** Keep the interface understandable while recording exactly what the primary could find, what it selected, and what the provider and model actually received.

- **File-facing state.** The normal interface uses named readable files, persona-chosen organization, scoped search, exact reads, and attributable edits. Specify current-state ownership, revision binding, path and rename behavior, conflict handling, atomic saves for dependent changes, recovery, retention, and export semantics.
- **Storage.** There is one accepted current state. Exports and unsaved edits do not create another authority. Choose a backend that demonstrates the contract. If canonical state uses physical files, those files need the same concurrency, revision, access, and crash guarantees as a transactional store.
- **Search.** Literal/grep search and explicitly supported regex operate over declared eligible fragment and resource corpora at the primary persona's request. Specify matching fields; pattern, scan, and output bounds; pagination; exact identities and revisions; descriptor limits; errors and incomplete coverage; cue and index maintenance; and protection of private titles and counts. Cues must not execute shell content. Discovery must not add automatic expansion or a hidden semantic retrieval engine.
- **Discovery bootstrap.** Before the primary chooses context, supply a small usable discovery and exact-read interface plus necessary current state, including mandatory work, self, and policy information. Do not preload all tools or skills. Declare permitted scope names, bounded metadata, matching and page semantics, failure meanings, actual bootstrap size, and relevant known-reference provenance. A full catalogue of names and descriptions remains prohibited even when labelled metadata.
- **Provider exposure.** Keep the bulk inventory in host storage, outside both provider-facing transport and model-visible context. Document the actual payload and callable-schema boundary, explicit loading path, provider expansion and continuation behavior, reset behavior, and retained session context. Measure request bytes, model-visible tokens, and billed tokens separately. Identify unsupported or unmeasurable modes honestly. Provider-side deferral alone does not satisfy these boundaries.
- **Navigation allowance.** The primary follows optional associations selectively. Exact evidence references and mandatory qualifications have different purposes and must retain them. Set cumulative limits for queries, candidate reads, returned text, context, relevant time and cost, and maintenance. Specify handling for broad fanout, cycles, and exhausted allowances. Exhaustion must be reported honestly; it must not truncate required qualifications or create compulsory outgoing links.

**Context and retained resources.** Bound both what defines the persona and what supports its work. Keeping an asset in the same storage account does not turn it into a characteristic fragment.

- **Persona-context corpus and prompt.** Set separate finite bounds for the authored characteristic corpus and the assembled input to each decision. The persona includes its context, LLM reasoning, actual interactions and actions, and evolving authored prompts. Specify corpus and prompt ceilings, useful coverage of characteristic distinctions, evidence of actual supply, consolidation and no-change behavior, and handling of capacity conflicts. Facts and experience may inform fragments without making the architecture episodic memory or retrieval-augmented generation (RAG).
- **Managed persona-state footprint.** Supporting resources and retained revisions count alongside the authored corpus. Declare the accounting boundary and ceilings for active and archived bodies; histories and tool records; copied skills, scripts, and code; dependency caches and data snapshots; derived indexes and revisions; provenance, qualifications, and warnings; effect and context receipts; exports and backups; externally retained context; and peak duplication during rewrites. Reserve protected closeout capacity and verify actual reclamation of space.
- **Next context.** Every persona call must explicitly state next-context intent for both fragments and resources. Handle the dispositions valid for that mode faithfully: preserve, replace, clear/no optional need, bounded discovery or read, or blocked. Missing or malformed intent rejects the combined response. Recovery may preserve prior state, but must not invent consideration or renewal by the persona. Specify exact selections and the versions, ranges, and schemas actually exposed; preserve/replace/clear behavior; protection of current self; complete qualifications; fit and stale-selection handling; current permissions; and direct paths for known references and known-current guidance.
- **Supporting-resource lifecycle.** Storage and organization must preserve actual origin, restrictions, freshness, and disposition. They do not establish persona authorship or execution. Specify acquisition, revision, retirement, and erasure rules for histories, definitions, skills, code, and data. Distinguish exact snapshots from live identifiers. Define cache scope and invalidation, stale or unknown outcomes, and—where watches are used—their actual requested, acknowledged, live, and ended coverage.
- **Qualification and provenance.** Necessary corrections must accompany usable full text, and source restrictions must follow derivatives. Specify bounded checks of exact required accompaniments and ancestry, version revalidation, whether the material fits at admission, withdrawal, erasure, and treatment of historical sources.

**Authority, execution, and resources.** Finding or loading a capability does not establish permission or readiness to use it. Each proposed operation needs current authority and a supported execution path.

- **Processing destinations.** Permission to read data does not permit sending it to every model or service. Declare approved primary-model and ordinary task-tool destinations, data-handling terms, retention limits, disclosure controls, and credential mediation. These choices do not authorize another persona-context writer, semantic retrieval engine, or selector.
- **Autonomous effects.** Every effect needs current scoped authority independent of authored files. Specify delegation, allowed effects and destinations, required approvals, durable intent, reconciliation when an effect's outcome is unknown, revocation, and actual enforcement.
- **Execution.** A stored script, selected skill, loaded schema, sandbox label, or past run does not prove current executable availability or authority. For controlled local execution, bind the exact artifact, dependencies, and environment. For remote execution, identify the observable interface, connection, client, and runner; explicitly record unknown server versions and the resulting limits on each assurance claim. Declare preparation and installation policy; current permissions for actor, target, input, output, and effects; actual result receipts; the selected host or isolated profile; the enforced trust model; separation of private evaluator material; and external destinations.
- **Resources.** Every call and the complete episode, including discovery and exposure, must stay within one controlling allowance. Set ceilings and metering for bootstrap; scans, pages, and previews; reads; schemas and guidance; dynamic loading; context and output reserves; maintenance; retries and failures; execution; and closeout. Include latency, monetary cost, conservative treatment of unknown usage, reservations, population bounds, and fairness.

**Acceptance, delivery, and continued operation.** Record what has actually been achieved, who has accepted it, and which obligations survive interruption or retirement.

- **Acceptance.** Authored judgment, independent assessment, human acceptance, and external assurance are distinct. Specify adopted criteria, qualification and separation policy, the exact subject and citation evidence, review gaps, and current release checks.
- **Delivery.** Local creation, retained publication, submission, delivery, and acceptance are separate events. Specify actual recipient surfaces, supported artifacts, explicit audiences, current readability, durable receipts, and useful failure diagnostics.
- **Retention and recovery.** Restart, renaming, retirement, consolidation, and deletion must not invent authority, resolution, or success. Declare exact-history promises and periods; derivative-use and erasure policy; conditions for lessons to survive and for reporting source unavailability honestly; backup and export boundaries; durable notifications; effect reconciliation; dispositions of protected warnings; capacity conflicts; and limits on recalling outside copies.
- **Outside stores and delivered artifacts.** Externally retained context must not become an uncounted archive. Notebook limits confer no rights over user-owned deliverables. Include the relevant external footprint or explicitly qualify the total bound as incomplete. State limits on control of provider and recipient copies, and distinguish artifact ownership from retention authority. Account for deliberate reuse of delivered artifacts as retained context without deleting, altering, or revoking them to meet a quota.
- **Optional exploration.** Between-task activity starts disabled and requires finite, explicit permission. Declare its environment, allowance, episode and recurrence bounds, precise expiry, same-persona and same-root foreground priority, scheduler assumptions, pause, and cancellation. State the supported latency for admitting foreground work—or disclose that no bound exists—including delays caused by already admitted optional inference and action batches. Account for late results and effects and preserve protected closeout.
- **Evaluation.** Target wording does not demonstrate implementation or behavior. Specify frozen fixtures, repeat counts, held-out tasks, rubrics, comparison controls, total costs, stopping rules, and bounded publication claims.
- **Distribution and contributions.** Editing the design does not select licensing or contribution terms. Obtain owner-approved terms and specify rights to material, attribution requirements, and evidence-governance responsibilities.

**Backend and interface boundaries.** Backend choice stays within the file-facing contract. A simple interface must not hide a requirement for graph bookkeeping, a separate automatic author, or another model that owns selection. Familiar files still need trusted records for permissions, exact observations, commitments, accounting, and recovery.

**From discovery to results.** Discovery, reading, selection, actual exposure, invocation, and observed results have distinct contract meanings. They need not take separate calls. An exact resource already known to the primary can retain its direct-use path, as can already supplied operative guidance that remains current.

Execution dependencies, provenance dependencies, data derivations, and required prompt qualifications require different checks. The model does not need every dependency's documentation or every data row. It does need complete required operative conditions. A missing restriction or execution prerequisite can block use. If a provider interface cannot expose a needed capability within the declared boundaries, record that deployment limitation. Do not report the tool as loaded or silently send the full catalogue.

### Effective character-authoring policy

A deployment must make clear whether the persona may revise its stable character. Initialization alone grants no continuing self-authorship permission.

**Enabled self-authorship.** A deployment claiming autonomous stable-character maturation must explicitly support a user-authorized enabled mode, record its effective scope and version, and expose that policy to ordinary primary invocations. Within that permission, the primary may propose and adopt genuine stable-trait or baseline-affect revisions under the existing coherent-acceptance and fresh-decision contract. The fresh-decision fence after effective-character changes also applies to reads and waits. Transient affect annotations do not automatically constitute stable-character revisions.

Enabled mode does not itself require new user approval for every revision. It also does not override an applicable approval requirement or withdrawal of permission.

**Locked character.** A user-selected locked mode remains valid. It still permits qualified development of methods, relationships, and transient state, but must not be advertised as autonomous stable-character self-revision.

Declare and test the effective enabled or locked policy, enforcement of transitions, and bounded progress and closeout behavior. A profile setting alone does not demonstrate those properties. This policy adds no universal numeric default, forced mutation, weaker fresh-decision fence, or new controller.

<a id="memory-bounds-and-retained-evidence"></a>
## Persona-context bounds and supporting evidence

A deployment needs explicit limits on what it retains, what it sends to each decision, and how much work it spends finding context. The [core navigation](../design/PERSONA-CORE.md#bounded-navigation-and-revisable-cues) and [compact-retention rules](../design/PERSONA-CORE.md#compact-retention-and-honest-forgetting) govern these choices.

**Set separate, complete bounds.** Bound the authored persona-context corpus, each actual prompt, cumulative navigation work, and the full managed storage footprint. A per-query limit does not bound total navigation. Measuring only a small active directory leaves lifetime storage unbounded.

Choose explicit ceilings and retention periods without claiming a universal optimum. Include retained history, supporting metadata, safe duplication during rewrites, and externally retained context deliberately used by the deployment. If that external context cannot be measured, qualify the total-bound claim rather than counting it as zero. Disclose the limits of control over arbitrary provider or recipient copies. Supporting records retain their provenance, access, expiry, and recovery obligations; counting them in storage does not redefine fragments as a memory system.

**State what history can prove.** Decide which historical questions the deployment promises to answer exactly and for how long. A lesson may survive expiry of its raw source only when the actual retention and derivative-use policy permits that interpretation to survive. Preserve the evidentiary limits:

- Report the expired source as unavailable. A digest does not reconstruct the evidence.
- Expiry does not declassify content. Any required derivative erasure also applies to the lesson.
- A present use that requires exact evidence cannot inherit a past approval.

**Check restricted meaning before adopting it into current self.** Declare the continuing persona's permitted audiences and processing destinations, including whether experience-derived meaning is eligible for the mandatory current-self account. Before adopting source-scoped meaning into that account, surface any known loss of eligibility for those audiences or destinations. Do not assume future permission or a future character transition. An authorized narrowing of audiences or destinations remains permitted.

A new client does not automatically authorize exposure of that meaning. If required character context is ineligible, the permitted paths are:

1. Obtain the applicable source permission.
2. Use an authorized, coherent character transition in a source-eligible context, under the existing acceptance and fresh-decision rules.
3. Otherwise, block the affected work.

Resetting context alone cannot make restricted derived meaning eligible. Do not silently replace accepted identity or treat removal of project names as declassification. Depending on policy, the correct disposition may be narrower claims, retired or ineligible guidance, or blocked work; permanent source retention is not the default solution.

**Protect closeout and unresolved obligations.** Reserve capacity within the total allowance for protected closeout, accepted warnings, and reconciliation. A protected unresolved effect, outstanding obligation, or accepted warning cannot be dropped as optional prompt material when space runs out. Protection also grants no exception to an erasure restriction. Resolve a conflict through its actual authorized retention or admission disposition.

Rejecting optional retention may still leave ordinary work possible. Do not promise unlimited exact history under finite storage, silently renew archive capacity, or delete user-owned delivered artifacts to meet notebook limits.

**Declare what admitted work can require.** The supported deployment must have a declared and evidenced admission and repair envelope: the range of operations whose required inputs, observations, state, and recovery can fit. Specify:

- Supported sizes for mandatory inputs and observations.
- The supported count of unresolved operations and sizes of retained state.
- Bounded consequences of admitted operations, including the context and durable records they may require.

Admission must leave a usable, permitted route to observation, reconciliation, and closeout. If that route cannot be bounded, restrict the operation or disclose the unsupported scope. An unforeseen excess still requires an honest blocked disposition; it must not lead to truncation or invented resolution.

**Make room for rewriting and repair.** Protected closeout capacity and space for peak rewrite occupancy serve different purposes. Reserve enough capacity for rewrites and primary-authored consolidation, or trigger authorized consolidation early enough for the required operation to fit. Space awaiting eventual deletion has not yet been reclaimed.

Define authorized pause and escalation when mandatory state, lawful retention, or repair cannot fit. The progress and stopping policy must bound repeated activity that makes no progress, including repeated character revisions. It must not impose mandatory phases or a universal edit quota, introduce a hidden controller, or exempt maintenance.

These choices establish a finite supported operating range. They do not promise indefinite service or authorize automatic quota increases, a hidden semantic validator, forced probes, or weaker privacy.

<a id="host-and-isolated-execution-profiles"></a>

## Default full host access

The user's current requirement is full access by default: personas can install and use any tools they choose, without application restrictions or per-tool safety approval. This default applies to both new and existing personas. A separate installation grant, command allowlist, sandbox, selected skill guide, or operator confirmation is not a prerequisite for host execution.

The host command interface runs with the host account's filesystem, network, environment, credentials, and subprocess access. Personas choose their tools, installation commands, working directories, and procedures. Actual operating-system permissions and package availability determine what a command can do; the application adds no per-tool restriction. Skill guides can be read as ordinary host files and remain attributable procedural resources.

The runtime supplies the current host command definition in ordinary persona inputs, without loading a catalogue of every installed program. Personas can discover installed programs and install additional ones through that command interface. The separate bounded WebAssembly and HTTPS profiles may remain available with their own historical contracts; their grants do not gate full host command access.

**Actual execution and continuity.** Adopt the command as part of the complete persona decision, record its identity before dispatch, and retain the observed exit status and output. Tool installation is an actual host change. Saved guidance, a proposed command, or a claimed installation is not an execution result. An interrupted command must not be automatically repeated merely because its terminal observation is missing.

Commands have no default timeout. A persona may request a timeout for a particular command. Bounded excerpts keep model context usable while full output remains available as host files. A command's live files and background processes remain distinct from an immutable recorded observation of its parent process.

**Host state and records.** This profile provides the host account's access, including access to files shared by personas using that account. Native record projections are not a filesystem isolation boundary. Native API operations continue to retain their actual adoption and execution records; direct host writes are ordinary host effects and must be described truthfully. Installation or execution does not itself establish skill application, a correct result, or completed work.

Model-call allocations and actual resource accounting remain distinct from tool permission. A host command needs no additional model attempt or per-tool attempt grant. Changing the tool-access default does not rewrite historical results, refund spending, or imply a command was executed in an older run.

This current full-access requirement supersedes the earlier requirement in this section to condition host-tool use on additional application approval or isolation controls. It does not turn earlier bounded-profile runs into full-host executions. Implementation status must be established by actual installation, filesystem and process operations through the persona's native path.

## Optional features and their conditional safeguards

These safeguards apply when the corresponding feature is enabled. Before use, declare the feature's scope, authority, and operating boundaries as specified below.

| Feature | Required declaration before use |
|---|---|
| E1: functional embodiment or enriched profiles | State which relationships the display explains. Profile richness must not imply human consciousness, feelings, competence, or physical embodiment. |
| E2: community or institution | Name the accountable sponsor and charter. Define real representation, membership, delegated powers, resource allocation, information policy, conflict and appeal routes, renewal, and the disposition of obligations at exit or dissolution. |
| E3: sensitive human-facing use | Provide transparent AI identity and meaningful choices about context, retention, and exit. Declare domain-specific policy and evidence. Do not invent credentials, diagnoses, relationships, or human endorsements. |
| E4: ongoing service | Identify the accepted owner and actual triggers. Define freshness, missed-event and disconnection handling, per-episode and overall bounds, renewal, retention, and stopping. Identify escalation recipients who actually accept that responsibility, and the fallback when they are unavailable. |
| E4: physical interface | Identify the device and environment, permitted effects, required observations, and operating conditions. Define override, responses to lost observation or conflicting controllers, safe stop, and delayed effects. Provide independent commissioning or qualified assurance. |
| E5: conformance aids | State which claims and optional features the profile covers, the exact requirement and evaluator versions, and explicit omissions. Keep worksheet use proportional; worksheets must not become mandatory task ceremony. |
| E6: public contribution and evidence | State adoption authority, exact historical results and criteria, source rights, transparent limits, and owner-approved distribution terms. |
| Cross-host activation | Explicitly disable activation or provide a separate tested contract covering transfer, exclusivity, revocation, privacy, authority, and failure. Read-only exchange does not authorize activation. |
| Separate memory-architecture research comparator | Semantic/vector retrieval and graph-driven memory are outside the current lexical/regex target. Any authorized comparison must declare that distinction, source and destination permissions, exact references, total cost, and failures. Adoption requires an explicit design change; it cannot be introduced as an optional runtime helper. |
| Numeric trait or affect representation | Declare optional engineering anchors, their actual provenance, and a consistent view of the same accepted character account. Semantic OCEAN/VAD meaning remains required without numbers. Do not fabricate or silently erase existing values. Scores confer no task router, effort quota, authority, or validated psychology claim. |

**Keep permissions specific.** Enabling personal exploration does not enable perpetual service or physical control. Simulated stakeholders in a service do not supply human consent. Adding personas does not multiply votes or funding, and completing an episode does not renew it. If an essential human escalation recipient is absent, narrow operation or pause safely under the adopted policy.

**Apply maintenance by the decision being made.** Optional features do not exempt persona LLM calls from maintenance. A narrowly scoped OCR, image, or mechanical transformation service need not author fragments when it is genuinely a non-persona utility. Its output remains attributable input for the next governed persona decision. Classify a call by what it decides, not by its name. Provider-internal routing or token computation does not provide an observable inventory of persona calls.

## What the design deliberately does not select

This edition selects the persona-facing mechanism and its behavioral responsibilities. Deployments still choose vendors, prices, cloud services, storage engines, numerical budgets, professional tolerances, retention periods, and benchmark success thresholds. The repository license also remains unselected.

An optional helper or extension must justify its actual burden and supporting evidence within the same authority and resource boundaries. Publishing these decisions does not make the separate runtime compliant.

Use the [decision worksheet](../templates/README.md#design-decision-and-evaluation-record) to record the chosen scope, accountable owner, evidence, and restriction on any unresolved feature. Keep unresolved implementation questions here or in a scoped implementation gap, rather than creating a competing active persona architecture.
