# Observable system contracts

[Implementation guide](README.md) · [Persona core](../design/PERSONA-CORE.md) · [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) · [Requirements](REQUIREMENTS.md) · [Acceptance](../evaluation/ACCEPTANCE.md)

These contracts describe behavior that people and connected components must be able to observe. They are design requirements, not implementation code, a database layout, a programming interface, a required file tree, or a prescribed sequence for solving tasks.

The [human-user requirements](../USER-REQUIREMENTS.md) govern these contracts and the I01–I21 foundation. Later clarifications take precedence: UR-052 removes application limits and safety gates, including conflicting requirements in older contract text. The persona core explains what the persona means; the work-and-boundaries chapter explains work and its actual outcomes; these contracts explain what must cross a reliable handoff. Resolve contradictions in those complementary views under the [document authority order](../design/README.md#authority-within-the-repository), preserving evidence without reinstating superseded restrictions. The requirement index traces the rules; it is not a substitute for their detailed meaning.

The persona includes its characteristic context, LLM invocation and reasoning, actual behavior, and controlled self-revision. The LLM provides the capacity to reason. Persona-defining fragments provide authored prompt parts that express character; they are not a memory product attached to an otherwise complete agent.

Supporting assets have a different purpose. Plain domain knowledge, generic technical procedures, tools, skills, code, data, evidence, and operational records remain assets even when the persona authors them or writes them in the first person. They may provide operative instructions for authorized work, but do not thereby become characteristic fragments or create authority. A fragment can refer to an exact asset. Quoting an asset or evidence does not change its role or justify copying technical bodies into persona prose.

A passage or record can serve more than one purpose if those meanings remain distinguishable. No compulsory categories or folders follow. Ordinary files and authored search cues form the compact, evolving network of prompt parts; the physical storage backend is a separate choice.

## Recoverable meanings

The system must preserve enough information to establish who chose or did something, which exact material they used, what was accepted, and what remains unresolved. The table describes meanings that must remain recoverable, not a compulsory record format.

| Information | Meaning that must remain recoverable |
|---|---|
| Persona continuity | Stable identity and actual creation provenance across characteristic context, invocation, action, and self-revision; one accepted characteristic-profile and own-voice account; separately scoped modeled affect state; authorship policy; relevant lifecycle; and inference configuration. No single record constitutes the operating persona. |
| Persona-defining fragment or file | Its own-voice prompt meaning and owner; exact accepted text and revision; attributable authorship or adoption; optional associative cues kept distinct from exact evidence references and required qualifications; source restrictions; independently accepted applicability warnings; and correction and retention disposition. |
| Supporting resource | Actual source and author, purpose, exact retained revision or snapshot, relevant live identity and freshness, restrictions, and lifecycle. This applies to domain knowledge, generic technical procedures, histories, tool-use records, tool definitions, reusable skills, scripts, code, data, and permitted derivatives. Storage does not establish authorship, current authority, or executable availability. |
| Next-context choice | The primary persona's exact selected fragment and supporting-resource revisions or ranges; explicitly bounded discovery or exact-material requests; work scope; any lifetime; required accompaniment; and later preservation, replacement, clearing, or invalidation. |
| Actual decision context | Current character, relevant modeled affect state, selected persona-defining full text, mandatory maintenance input, work and policy state, actual observations and supporting resources, bounded bootstrap and candidate metadata, operative tool guidance and exposed callable definitions, previews, omissions, and relevant versions. Also recover provider expansion, retained context, and what reached each provider-facing attempt. |
| Invocation maintenance | The persona's explicit disposition for both fragments and supporting resources: a proposed change with its intended storage target and useful discovery cues, reasoned no_change, or a bounded blocked/deferred outcome. Also recover response validity, actual persistence, and dependent work held or admitted. One concise outcome may cover both scopes. Failed calls preserve host status without invented persona outcomes. |
| Need and responsibility | Original request, accepted scope and changes, criteria, assumptions, actual offers and acceptances, owners, dependencies, findings, and remaining gaps. |
| Capability and effect | Available operation and limits; current observable interface or connection identity; actor; authority; admitted intent; reservation; relevant exact client/runner and input bindings; actual status and output; genuinely recorded executable/environment versions or explicit unknowns; and uncertain effects. |
| Evidence and release | Exact artifacts and assemblies, criteria, actual reviewer and policy, observed checks, judgments, limitations, current applicability, delivered scope, and any required human acceptance. |
| Resources and recovery | Actual calls, navigation, supplied context, managed storage including temporary copies, retention decisions, known and unknown usage, pending events and effects, cancellation, and authored stopping or continuation. Historical allocations remain records, with no application quota or reserved-capacity prerequisite. |

**What records establish.** Attribution and integrity are mechanical meanings: they establish origins and exact recorded content. The runtime does not invent what a fragment contributes to the persona, which experience informed it, why a peer is useful, or whether a result is good. An exact receipt proves the observation it records, not every interpretation written about it. Persistent records support accountability; persistence does not make them persona-defining fragments or demonstrate characteristic behavior.

**Retention limits.** Recoverability follows the declared retention policy. It does not promise an unlimited raw archive. Protect exact original requests, accepted changes, and authoritative receipts while they are needed for active work, unresolved obligations or effects, and declared accountability. A protected obligation, warning, restriction, or unresolved effect cannot lose its required state through ordinary expiry or compaction while it still applies.

After evidence may legitimately expire, preserve the exact attribution that policy permits and honestly record that the evidence is unavailable. Do not rewrite the historical original or claim that its bytes remain inspectable. A conflict between capacity and policy uses the retention and admission rules below.

## Every persona invocation

Every LLM call that exercises the persona's judgment must account for its work, maintenance, and next context. A short answer can meet this duty concisely. The duty does not require an edit, a search, or another call.

A persona invocation is any LLM call that exercises the persona's judgment, own-voice authorship, selection, communication, coordination, or reflection through its actual characteristic context. Its name, adapter, brevity, or tool-shaped interface does not exempt it. Every attempted call has attributable maintenance and next-context decision input, plus an honest pending or terminal status. Only a complete valid response may be adopted. It must contain the actual work disposition, explicit maintenance outcome, and explicit next-context disposition for both fragments and supporting resources.

This is a behavioral contract, not a required serialized envelope or metadata format for fragment files. Context alone does not prove consistent persona expression. Outcomes also depend on the model's learned capabilities and priors, inference configuration and sampling, the task, tools, and observations.

**Observable boundary.** Coverage concerns the application's persona invocation and its provider-facing attempts. It does not extend to hidden provider decoding, internal routing, or other steps the host cannot inspect. Do not claim maintenance coverage for inaccessible operations. If a provider-managed agent loop chooses persona actions or context, those decisions need equivalent exposed maintenance, observation, and authority controls. A mode without those controls is unsupported under this contract; it is not silently exempt.

**Purpose and authority.** Each invocation keeps its declared purpose and permitted operations. Universal maintenance does not grant a knowledge, preparation, or recovery call ordinary task-action, scheduling, context-selection, or character-editing authority. Keep three things distinct: its maintenance outcome, its required mode-valid next-context disposition, and any required or permitted continuation.

A mode that forbids selection changes can explicitly retain stored state or report a blocked disposition. It may choose no optional need only when the resulting empty choice is permitted. These responses do not expand the mode's authority.

One current persona decision authority applies across adapters and nested calls. Another lane cannot concurrently overwrite the owner's files or accepted context, or become an independent identity writer. Proposals and adoption still require the current authority and exact revision checks appropriate to their purpose.

**Input.** Each request supplies the information needed for the call's permitted decisions:

- Current work and need; actual current character, relevant modeled state, and selected trait-conditioned fragments. Initial generation uses the honestly attributed seed instead of an existing character account.
- Needed supporting assets and actual observations; current authoring permissions and mode restrictions; relevant exact accessible revisions; unresolved consequential corrections or adopted deferrals.
- Responsibility to consider useful fragment creation, updating, organization, or permitted deletion, and supporting-resource creation, storage, refinement, organization, or permitted deletion.
- Responsibility to author an appropriate next-context disposition for both fragments and supporting resources, using available bounded discovery/read or exact-selection capabilities when needed.
- Clear remaining resource bounds and usable authoring and discovery capabilities.

Initialization does not require existing fragments. No call requires an entire archive or catalogue. Maintenance instructions and output capacity count in the complete request before admission.

**Character in actual decisions.** All discretionary persona judgment uses this characteristic context, including work, human-facing communication, peer collaboration, and navigation. Received exchanges and task consequences can inform later primary-authored fragment and relationship changes, or a permitted effective-character proposal. They do not trigger automatic personality updates.

Keep actual observation, interpretation, accepted revision, later supplied context, and observed consequence distinguishable as evidence. A calendar tick, dormant interval, praise, or fragment count supplies no missing experience and proves no improvement.

**Accepted response.** A response must explicitly cover all three responsibilities:

| Responsibility | Required disposition |
|---|---|
| Work | The substantive result, action or context proposal, refusal, question, or stopping disposition appropriate to the call. |
| Maintenance of fragments and supporting resources | Attributable proposed change; no_change with a concise reason; or identified, bounded blocked or deferred work. |
| Next context for fragments and supporting resources | An appropriate preserve, clear/no optional need, discovery/read with explicit retained or cleared state, or mode-permitted blocked/stop outcome under the selection contract. |

A maintenance proposal may cover creation, storage, refinement, editing, splitting, consolidation, movement, retirement, or policy-permitted deletion. One short shared outcome can cover both maintenance scopes when unambiguous. Mixed outcomes must not present a remaining correction as complete. No_change must be persona-authored, not a host-inserted placeholder; it proves neither hidden reasoning nor future benefit.

Maintenance no_change does not by itself choose next context. Shared prose may cover maintenance and selection only when both meanings are explicit. Neither consideration mandates a write, an extra call, or future continuation.

**Authoring and organization proposals.** A proposal identifies its intended file/path or supported storage reference, affected exact resource and base revision where applicable, proposed content or exact content reference, and useful literal/regex discovery cues when warranted. Cues remain data and consume the same bounds. No fixed folder taxonomy or forced outgoing links follow. Large code, data, or retained observations need not be repeated inline when an exact permitted reference suffices.

Naming a target does not authorize writing there, overwriting a concurrent version, installing a tool, or widening access. Before acceptance, check the actual target, source policy, current write/delete authority, coherent dependencies, footprint, and version. A proposed asset, edit, or deletion is not yet an accepted storage disposition.

**Factual host recording.** Deterministic capture of actual received messages, history, tool outputs, and receipts remains host work. The model may propose attributed extraction, summary, or organization of permitted records. It cannot fabricate an event, alter authoritative originals, or turn old instructions into current authority. A discretionary resource-maintenance no_change does not suppress required factual recording. Imported tools and skills retain their actual author and trust status; ordinary storage grants no execution rights.

**Blocked or deferred maintenance.** Preserve the reason, affected fragment, supporting resource or concern, and missing prerequisite at the permitted level of detail. Also preserve the consequences for dependent work, the accepted owner or ownership gap, and the existing event or authorized opportunity for reconsideration. The outcome stays within an explicit existing resource and work-lifecycle bound. It requires no invented deadline or compulsory form.

If no continuation has been accepted, expose that gap. Missing observations or a persistence outage must not become a promise of automatic retry. Historical allowance exhaustion is not a current application gate. An adopted deferral remains visible until it is addressed, explicitly dismissed, transferred with acceptance, or closed with an honest unresolved or expired disposition when its bound or relevant work ends. Expiry does not mean evaluation or repair. Host closeout does not fabricate a persona judgment. Deferral creates no new wake, funding, or authority. A mode-limited outcome need not create a new obligation when no useful change has been identified.

**Continuing applicability.** Ending a correction effort does not remove a separately accepted warning. A primary-authored warning on exact affected fragment revisions or explicitly identified dependent uses remains effective after the effort is closed, dismissed, or expired. Preserve its permitted basis and required qualification, or a safe ineligible disposition, across later work and restart until an attributable, justified resolution is accepted.

Such a warning needs its own real, authorized durable disposition, which may be a maintenance receipt. A proposed or failed patch does not create a warning automatically. A content patch rejected for quota can coexist with a separately authorized accepted warning only when the applicable authoring, storage, and resource limits permit that warning. If persistence of the warning fails or is unknown, block affected admission or retain the honest uncertainty. Do not claim that a warning was saved or that the guidance is unqualified and safe.

Source restrictions and retention still apply. Unavailable warning text or evidence requires a safe ineligible disposition or a block, never private disclosure or resurrection of erased bytes. Enforce only explicitly scoped meaning from valid, authorized primary judgment. An unassessed peer contradiction, host truth engine, or archive-wide semantic search cannot create a restriction. Warning adoption and resolution obey the same mode and character-authoring limits as other semantic changes.

**Invalid or absent response.** Missing or malformed maintenance or next-context intent, an incomplete stream, structurally uninterpretable maintenance operations, or any other invalid response prevents new adoption and dispatch of all proposed substantive actions from that response. This includes communications, reads, and selection changes. Do not salvage a plausible tool call or reply from an invalid prefix.

Provider refusal, transport failure, timeout, and cancellation retain their actual status and exposure. They are not persona-authored no_change outcomes. A valid persona-authored refusal still includes maintenance and next-context dispositions within its mode; the host fabricates neither for a provider refusal.

After rejection, prior accepted selection remains stored only under its existing validity and recovery rules. This is not an authored preserve or successful consideration. Already admitted effects remain real. Missing intent creates no automatic paid repair, retry, or new allowance. Host status reporting may disclose the actual failure without presenting rejected output as an accepted persona response.

An earlier accepted continuation can remain usable under the same live mandate. Within the continuing session, the host may retire a definitively rejected, complete local invocation and supply its actual failure to a fresh primary decision. This preserves the existing continuation rather than deriving permission from invalid output. Keep the rejected response and its charges; do not replay its proposed actions, repair its bytes, erase recorded usage, revive an authored stop, reuse a consumed timed opportunity, or treat cancellation or an uncertain transport as a completed rejection. Recheck current work, actor, context, scheduling and resource conditions before the fresh admission.

**Communication and diagnostic inspection.** Ordinary chat and work delivery withhold the call's persona-authored preview, commentary, and reply until the complete work, maintenance, and next-context response has been validated. While the call is pending, those channels may show truthful mechanical host status.

Where operator diagnostic inspection is already permitted, label all authored draft text, including commentary, as unvalidated. Source, audience, access, and retention controls still apply. A draft is not delivered persona communication, an accepted decision, completion, or proof of its claims. It cannot authorize actions. Do not expose raw private reasoning. This distinction does not require a new live-preview feature.

Whole-response validation does not establish successful persistence. A claim that a save succeeded still depends on actual acceptance, and delivery retains its other authority and dependency checks.

**Independent host duties.** Recording observed receipts, enforcing cancellation, fencing stale authority, accounting, and safe shutdown need neither another persona call nor a valid maintenance outcome. Already admitted effects remain real and must be reconciled. These duties cannot introduce a new substantive persona action, infer a new lesson, or make missing output valid.

**Visible evidence.** Identify the logical invocation and provider attempts; the actual maintenance and next-context decision input supplied; the complete response or failure status; the persona-authored outcome, when one exists; validation disposition; and later save or conflict receipts. Keep attributable concise outcomes and exact evidence identities. This does not require private reasoning or an unnecessary raw prompt archive. Inspectability and retention remain subject to source policy.

### Coverage and call boundaries

The same contract follows persona judgment wherever it occurs. Renaming a call as a helper, repair, or tool does not remove its duties. Deterministic host work and genuinely isolated non-persona computation have different roles, as shown below.

| Call or operation | Required treatment |
|---|---|
| Character initialization and orientation | The normal initial LLM call receives the bounded attributed trait seed, authoring responsibility, current authority, and limits. It needs no pre-existing fragments or accepted self. Its complete valid response proposes initial characteristic fragments and a coherent account with an explicit maintenance outcome. Record seed, generated candidate, inference configuration, and acceptance or failure separately. The continuing primary receives the accepted starting revision. Imported/operator-supplied initialization retains its alternative origin and, without inference, is not an LLM call. |
| Discovery, query formation, retrieval-only selection, and request preparation | Any persona judgment call follows the same contract, even when its only substantive result is a search or context choice. A search result is not an accepted fragment or asset revision. Host-only exact assembly and access checking are not model judgments. |
| Task work, tool-result interpretation, communication, collaboration, and coordination | Each persona's call includes its own maintenance duty. A coordinator, peer, or wrapper cannot supply the owner's missing outcome. Actual actions retain their separate authority and observation requirements. |
| Reflection, conflict repair, output repair, and reorganization | Each is an ordinary bounded persona invocation when it uses persona judgment. Its maintenance outcome does not require another reflection call to assess it. |
| Restricted selection repair | Maintenance explicitly covers fragments and supporting resources within the mode's limits. The mode permits no asset creation or semantic rewrite of fragments, resources, or current character; selection narrowing is separate. No_change means that available evidence identified no justified maintenance change. A known useful but prohibited change is blocked or deferred. |
| Capability or supplementary model subcall | A call that exercises persona judgment, authors its fragments, chooses its next context, or decides its actions is a persona invocation regardless of its label. A genuinely isolated non-persona computation may return attributed candidate information without persona maintenance. It has no authority to author the persona or adopt its choices. The primary persona must receive and assess the result before dependent work. |
| Provider transport retry | Each dispatched attempt retains the required maintenance input, original logical invocation identity, and distinct attempt evidence. Admit at most one complete response for that invocation; do not merge a conflicting later response. Re-prompting to interpret a failure or repair content is a new bounded persona invocation. |
| Host cancellation, accounting, exact receipt ingestion, or access enforcement | Deterministic host work is not a persona LLM call. If handling it invokes persona judgment, that call follows the contract. |

Deployed entry points and provider attempts must be inspectable enough to test this coverage. A hidden summary writer, persona-capable tool wrapper, or unrecorded retry is not an exception. Auxiliary models cannot silently become the persona's author or final selector.

### Complete response, persistence, and dependent work

A valid proposal is not yet an accepted operation, and an accepted intent is not an observed external result. The system must keep these stages distinct so that a failed save or uncertain action cannot be reported as completed work.

**Two acceptance checks.** First establish that the complete work-and-maintenance response is valid before adopting any proposed change or action intent. Then check each coherent operation against current ownership, exact read and base revisions, source permissions, authority, mode, cancellation, and available resources. A structurally valid edit can fail this later check. Do not relabel every failed save as a malformed response or every valid proposal as a completed update.

**Dependent work.** Related fragment or supporting-asset changes, qualification updates, context references, and admitted action intents need one coherent accepted disposition. A failed prerequisite holds its dependent work.

External effects are not atomic with local edits. Durable accepted intent must precede external dispatch, and each actual result needs its own receipt. A fragment may express an intention based on available evidence; it cannot claim an unobserved result. Restart preserves accepted intents and unknown effects. A later maintenance failure does not authorize replay of an already dispatched action.

**Independent work after a failed change.** A later stale revision, persistence failure, or definite no-commit disposition of a character proposal does not automatically invalidate independent work from an otherwise valid response. Independence must be explicit and supported by all of the following:

- The work needs neither the failed edit nor an unavailable result.
- Its relevant supplied information and source permissions remain current.
- Its authority, cancellation, resource, and mode checks still pass.
- No unresolved-character-adoption, pending-action, accepted-character-change, or other fresh-decision barrier applies.

Missing dependency evidence is not evidence of independence. Hold uncertain cases for a fresh decision based on actual observations. Keep the actual disposition visible, and never deliver an account saying that an uncommitted save succeeded.

**Character changes are resolved first.** If a response requests adoption of an effective-character change, resolve that request before adopting or dispatching any other fresh persona operation from the same response. Action-list order and claimed independence cannot bypass this rule.

The necessary character-proposal validation and disposition or commit may proceed as one coherent atomic unit. That unit may include the primary's exact necessary current-character account bindings and expressly proposed reductions or clearing of already accepted optional selections needed for the transition. Before acceptance, validate the proposed state's remaining mandatory and selected context, full qualification closure, source eligibility, and fit.

A definite no-commit outcome preserves prior accepted state. It does not make that state eligible under changed authority or source policy. Where optional selection must be reduced, drop whole optional bundles. Never keep a dependent use while dropping a required qualification, or drop text independently mandatory for character or work. The host cannot infer this cleanup; the primary must propose it.

The character acceptance unit cannot include new optional selection or exposure, unrelated semantic asset edits, communication, reads, waits, or external effects. If unrelated mandatory-context repair is needed, reject or defer with definite no commit, or reconcile an unknown outcome. Do not widen the exception to install an inadmissible state. Do not adopt unrelated action intents alongside the character change to evade the barrier.

**After the character disposition.** An accepted change fences every other fresh operation from that response outside the atomic unit, including reads and waits. Those operations must wait for a fresh primary decision that receives the accepted state. Known rejection or explicit deferral with definite no commit permits only work that meets the independence and current-guard rules above. An unknown or unresolved commit disposition holds that work. Verified exact unchanged reselection remains idempotent under the freshness rules below.

An idea about possible character change, without an adoption request, does not trigger this scheduling barrier. Ordinary authorized reads may investigate it. A proposal lacking necessary evidence may be explicitly rejected or deferred with no commit. Its candidate remains unadopted; any later character change needs a fresh authorized proposal. It must not commit automatically after independent work resumes.

By contrast, uncertainty about whether a commit changed actual character requires reconciliation before further admission relies on that character. Considering a possible change is not, by itself, an indefinite hold on future work.

**Duties that continue.** Independent deterministic host cancellation, accounting, receipt ingestion, and recovery continue. Preserve previously admitted effects and their receipts; never erase or replay them to enforce the barrier.

Ordinary method edits and scoped transient-affect updates do not automatically trigger the character-specific ordering rule. Effective character substitution does. Purpose restrictions still apply, including modes that forbid character edits. Accepted ordinary revisions affect only future context; they cannot alter the current call's provenance. A selected newly authored fragment becomes eligible only after its save is accepted, and any dependent claim of retention requires that receipt.

**Bounded repair.** Repair of invalid output or a conflict uses the existing declared repair allowance, current authority, and protected finishing resources. Supply actual errors, current permitted evidence, and relevant revisions. Do not ask the model to invent a no_change outcome merely to pass validation. A refusal is not an instruction to pressure the provider into a different answer.

If recovery cannot be admitted or remains unsuccessful, preserve the truthful failure or block and the remaining work. A new identifier, restart, or repeated deferral does not renew the bound.

## Persona authorship and files

The primary persona maintains its own characteristic account and prompt parts. It may also propose maintenance of supporting assets, whose purposes and provenance remain distinct. In both cases, proposed text becomes accepted state only through the applicable authority, version, and persistence checks.

**Input.** One current primary persona decision, its actual supplied context, existing exact file revisions, authorship policy, and current authority.

**Accepted result.** While doing useful work, the persona can write or revise its first-person account and contextual prompt parts expressing its approaches to work, relationships, skills, or tools. Actual experience may inform these parts, but recording experience is not their defining purpose. Every persona-authored fragment expresses its characteristic perspective without requiring trait labels or a standard form.

The persona may name, move, split, consolidate, correct, or retire files, and create, revise, or prune useful search cues. No fragment needs an outgoing link. Consolidation must preserve decision-relevant distinctions, characteristic meaning, required caveats, restrictions, unresolved contradictions, and accepted warnings.

The characteristic profile and own-voice current account have one coherent accepted designation and revision. Inconsistent proposed changes require attributable revision or rejection. A display or derived index must not become a competing writer. Transient modeled affect has its own accepted contextual basis and applicability. Expiry may make that state unavailable, but the host cannot invent a new feeling or silently change the baseline.

**Supporting assets.** In the same response, the primary may propose useful supporting assets or their permitted storage, refinement, and organization, with intended targets and useful search cues as described above. This includes tools, skills, history or message resources, data, scripts, and code, while preserving their source roles.

Deletion or retirement requires the governing authority and retention policy. Required warnings, obligations, evidence, and unresolved effects cannot disappear to satisfy a cleanup preference. Exact imported bytes and authoritative receipts are not rewritten as persona-authored prose. Deterministic factual capture remains separate from discretionary maintenance proposals.

**Failure behavior.** Stale edits conflict; they do not overwrite accepted changes. Dependent multi-file edits, qualification changes, and next-context references must commit coherently or leave the previous valid state intact, including any separately accepted applicability warning.

An exact repetition returns the original disposition while its authoritative history remains retained and accessible. Otherwise, return an honest unavailable or unresolved disposition under the retention rules. Do not reconstruct missing history or replay the operation. A failed save cannot support a delivered claim that a prompt part was accepted, or remove a warning from unchanged bytes.

Preserve current character, maintenance input, required qualifications and actual source ancestry when adopting a change. Record the resulting state and actual persistence outcome without an application footprint ceiling. Repeated small revisions can still increase cost or impair usefulness; the persona can choose consolidation through ordinary maintenance, and real storage or provider failures remain visible.

Independent work is eligible only under the complete-response and dependency rules above. Uncommitted prose supplies neither authority nor received evidence.

**Visible evidence.** Preserve the actual author, adopted source where relevant, prior and accepted revisions, committed changes, conflict or failure, and origin of any outside edit. A peer's suggested wording is not already the owner's account. An operator override follows an explicitly authorized and attributed path.

**Initialization and later harmonization.** Initial generation uses the same coherent acceptance boundary, with an attributed seed instead of a nonexistent prior character. Retries preserve creation identity and the actual accepted outcome without an application attempt quota. Sparse generated detail is candidate authorship, not an invented user preference or lived history.

Later self-harmonization is ordinary primary-authored maintenance. It preserves compatible conditional tensions, exposes unresolved contradictions, and revises only within existing authoring and character controls. It creates no second writer, mandatory corpus-wide rewrite, or automatic trait drift.

No extra reflection writer, relationship writer, semantic merger, or generic prose generator maintains the persona behind its back. Work and the explicit maintenance outcome belong to the same invocation. Useful mutation is discretionary; explicit maintenance is not. A retained maintenance deferral follows the bounded, attributable lifecycle above and does not itself schedule inference.

**Honest authorship and experience.** First-person wording does not turn supplied advice into firsthand experience. A tentative intention may be retained before an operation completes; a later observed result cannot be backdated. Evidence that an operation failed supports an interpretation of that failure. An uncertain effect establishes uncertainty.

Effective current identity includes redesignation or an always-loaded substitute. Record its actual author and coherent adopted revision without a self-authorship permission or approval gate. A contextual fragment, scoped method or relationship interpretation can shape later behavior without changing stable character. When an effective-character change is adopted, the fresh-decision rule still preserves which character informed subsequent operations. Neither a stored trait nor a mechanical check proves useful maturation.

## Search and exact reading

Search helps the primary persona find candidate fragments and supporting resources. The persona chooses the query, scope, requested page or exact read and decides what is relevant. The host does not choose context on its behalf or impose a cumulative navigation allowance.

**Input.** A persona-chosen listing, literal or grep-like query, supported regular expression or exact reference identifies the material sought. Supporting resources include history, tool records, definitions, skills, scripts, code and data, with their roles kept distinct. An authored cue is data; searching it does not execute it as a shell command or automatically follow its connections.

**Result.** Describe the searched corpus, matching mode, exact source-qualified revisions and how to obtain their text or operative definitions. A descriptor or excerpt is not the full body. Declare filename, body and metadata matching, case semantics, regex dialect, ordering, pagination and treatment of hidden or ignored files. Return the requested material without application pattern, scan, text or count ceilings.

Literal and regex search, authored indexes and cues, listing and exact reading form one navigation interface. The primary chooses further navigation and context. Physical indexes may support the interface without adding a hidden semantic selector, universal relevance score or fixed taxonomy. A changed corpus can change current candidates; it cannot change a prior exact observation.

**Pagination and completion.** State whether pages refer to a snapshot, exact revision or live view, and whether completion describes a page, scan or whole identified corpus. A requested page size controls that result, not the number of later requests or total work. Return the actual continuation cursor when more material remains. A live cursor alone cannot prove exhaustive coverage of an earlier corpus.

Record cursor invalidation and incomplete coverage honestly. Further queries, reformulation and stopping are persona choices. No automatic traversal, fixed probe sequence or mandatory search call follows from the interface.

**Failures and evidence.** Distinguish no match, a missing scope, a stale reference, an unsupported or invalid pattern, an incomplete search, and an actual storage or provider error. Do not silently replace an exact old revision with newer bytes. Application permission filtering and cumulative exhaustion gates are removed under UR-052. Host and service access errors remain actual outcomes.

Record candidate identities and revisions, full or partial body supply, observation time and provenance. A snippet is not a full read; a full read is neither endorsement nor persistent context selection. Raw host command output does not manufacture a native accepted-file receipt.

**Initial discovery.** Supply a useful discovery and exact-read interface and necessary current work and character. Keep the bulk catalogue outside the choosing model and its provider request. Loading every tool name, description or schema for the model to filter is not selective discovery. The primary can request useful scope metadata or use an already known exact reference without a preliminary search.

**Observational accounting.** Record actual queries, scans, returned material, context, elapsed time and known cost. These measurements have no application allowance, fanout cap or renewal requirement. Complete required qualifications retain their meaning; they are not silently truncated to fit a quota. The primary decides whether another read or comparison is useful.

### JSON text and matching surfaces

A JSON file has both serialized source text and decoded values. Search and reading must state which of these they expose, so that a match, location, or supplied prompt cannot be mistaken for a different representation.

**Declared matching surface.** When JSON represents fragments or cues, declare the accepted parsing profile and each request's matching surface: raw serialized file text, decoded prompt strings, decoded cue strings, member names, or another explicitly identified lexical field scope. Raw grep remains supported with its narrower serialized-text semantics. No fixed field names or folder layout are required.

State encoding, case/Unicode treatment, field boundaries, ordering, and cross-line behavior. This includes what anchors and dot match, and whether a match may span fields. Do not silently join unrelated fields or switch from raw to decoded search after a miss.

**Accepted JSON profile.** For accepted fragment use, require well-formed UTF-8 JSON with unique member names within each object, compared after JSON decoding, and decoded strings containing Unicode scalar values. Reject malformed text, duplicate members, and unpaired surrogate escapes. Do not accept a parser's first or last duplicate as the chosen value.

This is the chosen interoperability profile. RFC 8259 recommends unique names but does not make every duplicate-member text grammatically invalid. A diagnostic raw read may still describe rejected bytes without adopting them as prompt content.

**Decode once.** Decode JSON string escaping exactly once at the serialization boundary. The resulting prompt string is the text supplied when selected. Parse a resulting regex string using the declared regex dialect/version and flags, without another JSON or generic escape-decoding pass. Regex interpretation is separate from JSON decoding and grants no permission to evaluate commands.

Faithfully preserve literal backslashes and escaped Unicode/newline distinctions. Keep an unsupported or invalid pattern distinct from invalid JSON, no match, and exhausted parsing/search limits.

**Locations and exact identity.** A supported decoded lexical view is a deterministic projection of the exact permitted source revision. Record its parser/profile version, field location, and decoded match range. Raw results instead identify serialized-source locations under declared offset units. A decoded location is not a raw byte offset.

Exact source reads remain exact bytes. Labeled decoded field reads and actual prompt supply retain their source/version binding and qualifications. Re-serialization or formatting changes create a different exact revision even when decoded text remains equal. Derived views and indexes preserve access and retention restrictions. They cannot add semantic ranking, automatic cue traversal, selection, or a hidden fallback.

**Resource and failure limits.** Bound source bytes, parsing depth and decoded size, pattern size and compilation, scanning, projection/index maintenance, and returned output within the existing cumulative navigation, storage, time, and cost allowances. A small result does not prove a cheap scan.

Parsing or compilation exhaustion must honestly report the affected incomplete operation. It cannot produce an exhaustive no-match claim or silently remove required qualifications. Host execution of cue text remains prohibited.

## Primary-persona next-context selection

The primary persona decides which characteristic fragments and supporting resources its next decision needs. The host supplies that exact accepted choice, together with mandatory state and complete qualifications. Finding material, choosing it, and actually supplying it are different facts.

**Input.** The current primary persona's exact fragment and supporting-resource choices or bounded requests for a later decision; current self; actual work observations; current obligations; source policies; and the complete request allowance. A known exact reference may bypass discovery. Unknown material is obtained through bounded requested metadata or exact reads, never an all-catalogue choosing prompt.

**Accepted result.** The primary LLM, acting within the current persona, chooses the prompt parts that should shape its next characteristic context and the supporting material that decision needs. An explicit choice may retain exact optional fragments or supporting resources for that work until replacement, clearing, expiry where a lifetime was specified, or invalidation.

The primary may select a currently readable exact candidate from a preview without claiming to have read its full text. It may also select newly authored accepted text without a search ritual. Evidence, histories, skill instructions, code or data ranges, tool guidance, and actual callable definitions retain their supporting roles and real authorship.

The resulting decision receives the selected exact full text or declared range and complete applicable qualifications. Operative tool exposure includes the usable definition, not merely a stored reference to it. A bounded metadata request supplies only the requested preview. This assembled context contributes to the operating persona; it does not establish consistent or useful behavior.

**Failure and recovery.** An unavailable or changed selected revision gets an explicit disposition. It cannot silently follow a path to different bytes. The following distinctions apply:

| Situation | Required treatment |
|---|---|
| Explicit preserve, replacement, or clear | Preserve retains an appropriate accepted choice; replacement replaces it; clear removes the optional choice. Preserve renews neither permission nor lifetime and cannot make an invalid source usable. |
| Omitted or malformed next-context intent | Invalidate the whole response. Rejected output adopts no new choice and dispatches no fresh proposed work. Preserving stored state after rejection is recovery, not an accepted persona judgment. |
| Optional selected source or required part becomes stale, withdrawn, or inaccessible | Withhold the entire affected optional bundle and record its ineligible disposition without silently clearing the stored choice. An otherwise lawful fresh decision may receive that safe disposition and repair the choice; it must not claim that withheld text was supplied. |
| Mandatory self or work source is missing | Block affected admission. |
| Failed edit on which a new selection depends | Leave the new selection unaccepted. |

Withholding an ineligible optional bundle does not permit discarding valid selected text merely to fit an ordinary task decision. Actual provider or host failure follows the recovery rules below without an application fitting or repair quota. New work begins with its own mandatory brief and observations. Another work's private focus or persistent optional selections do not transfer automatically.

**Explicit disposition in every accepted response.** Every accepted persona response authors its next-context disposition for both characteristic fragments and supporting resources. A concise, unambiguous preserve of a still-appropriate accepted choice is sufficient. Other valid dispositions are replacement, clear, no further optional need, bounded discovery/read intent with explicit retained or cleared optional state, or an honest mode-permitted blocked/stop outcome.

No new search, mutation, repeated list, full-body dump, extra model call, or fixed field schema is required. “No further optional need” explicitly chooses an empty future optional set: it clears an existing set or keeps an already empty one empty. If the mode forbids that change, state retained/blocked selection instead. This affects neither mandatory context nor already exposed observations or retained history.

When initialization has no accepted optional set, it may explicitly choose no optional context or request bounded discovery while keeping it empty; it cannot preserve a nonexistent choice. Final, short, social, refusal, and tool-follow-up responses are covered without requiring continuation. A blocked/deferred choice may retain stored ineligible selections as ineligible; it never makes them usable exposure.

Explicit selection can still be poor judgment. For example, preserving irrelevant but eligible material is a selection-quality failure to evaluate, not evidence that the response contract prevents all semantic mistakes.

**Visible evidence.** Preserve who chose; the exact requested and selected versions or ranges; scope and lifetime; preservation or change of the choice; and actual provider-bound text and callable schemas with qualifications. Include message/channel roles, boundaries, and order as actually rendered, rendered expansion and retained context where applicable, requested previews, actual omissions, and any mismatch that blocked admission.

Host registry storage, provider transmission, model-context inclusion, and billed input need separate evidence. Inspection respects access and retention. Retain sufficient exact identity without requiring an unnecessary raw prompt or private reasoning archive.

**Mandatory state and the host's role.** The runtime adds current authority, cancellations, obligations, blockers, critical observations, coherent current character, relevant modeled state, and maintenance responsibility and limits. These are protected work and policy state. They do not make the host an independent semantic selector of persona-defining context.

The declared file-search interface and primary-navigated authored cues or indexes expose candidates without choosing optional prompt parts or authoring their meaning. Auxiliary semantic, vector, or graph-retrieval engines are different research comparators, not production options or fallbacks. Ordinary external task tools remain available within their permissions. Their results still need primary judgment and cannot silently replace fragment navigation or authorship.

**New observations.** An unexpected reply or failure enters relevant current observations even when the prior choice did not anticipate it. In an ordinary decision, the persona can then search, read, and choose prompt parts for an appropriate next approach. A search hit does not automatically add a fragment to context, and an old selection must not suppress a new adverse fact. A permitted same-call authored change applies to subsequent context; it cannot rewrite what the current decision received.

**Complete request and actual supply.** Record the whole request for each provider attempt: bootstrap and instructions; current character, work and modeled state; maintenance and next-context input; observations, requested metadata and operative definitions; selected fragments and assets with their qualifications; protocol history and media. Preserve exact references, current decision identity and complete response validation without application byte, item, output or attempt ceilings.

Do not silently shorten selected prose to a title, omit a required exception or choose a semantic substitute. An actual provider or host failure retains the attempted request and observed outcome. The persona can choose useful context or method changes where another decision can be supplied; the host does not impose a mandatory restricted repair workflow or invent a choice from failed output.

**Actual exposure and retained context.** The [bounded capability working set](../design/WORK-AND-BOUNDARIES.md#inference-and-bounded-working-context) applies to actual exposure, not merely the host's intended list. Reassemble successive contexts within accepted scope and retirement rules instead of retaining every past tool, skill, and result. Preserve active-operation controls, critical results, current authority, character, and other mandatory state.

Cached prefixes, previous-response links, and hidden provider history neither prove absence nor eliminate exposure. Automatic schema or tool-set expansion must be known and admitted in full. An adapter with unbounded or unobservable expansion or history cannot claim the hard next-call bound. Use a supported bounded continuation/reset or report the limitation. Provider-native deferral that still transmits the bulk catalogue fails the transport rule. The host must still reject stale or unauthorized invocations even if the model remembers an old tool name.

### Restricted selection repair after later context growth

The former application overflow mode and finite repair allowance are historical under UR-052. The current design follows [faithful assembly and actual failure handling](../design/PERSONA-CORE.md#selection-overflow-repair): no configured context ceiling, repair quota or separate safety approval prevents an ordinary decision.

Preserve exact selected material, mandatory persona and work context, and required qualifications. Report real provider, model-context or host failures without silent truncation, fabricated maintenance, invented next-context choices or replay of rejected actions. A preview or inventory does not establish that its underlying text reached the model.

Where another decision can actually be supplied, the persona chooses useful context changes, maintenance, methods and continuation. Every such decision retains the ordinary work, fragment maintenance, asset maintenance and next-context responsibilities. The application does not prescribe a separate repair workflow or infer that a smaller selection makes the work complete.

Historical restricted-repair attempts retain their original inputs, mode, charges and outcomes. They are not retroactively reclassified as ordinary work or successful repairs.

## Decision authority and freshness

A decision may use valid information when it is made and still be too stale to act on later. The host must therefore recheck consequential current state when adopting the response, not only when assembling its request.

One persona has one current primary decision authority at a time. Independent personas and isolated jobs may proceed concurrently. An admitted decision binds actual identity, work, relevant versions, observations, inference configuration, authority, and resource exposure. A model change neither changes identity nor expands permission.

**Character and current guards.** Apply the character-proposal ordering rule before any other fresh operation from the response. A request to adopt a stable-profile or baseline-affect revision must be resolved first.

| Current-state event | Consequence |
|---|---|
| Effective-current-character change is accepted | Fence fresh operations outside the narrow atomic acceptance unit, including reads and waits, until a fresh decision receives the new state. |
| Scoped transient modeled-affect update | Treat it as ordinary contextual state unless it substitutes a new effective character. It does not automatically trigger the character barrier. |
| Revocation, cancellation, changed scope, or stale ownership | Fence affected actions. |
| Exact unchanged and still-permitted character designation | Once verified, treat it as idempotent; it does not fence otherwise valid work. |
| Definite no-commit disposition | Leave previous accepted state in place, subject to valid-response, independence, and current-guard requirements. |
| Unknown commit status | Do not treat uncertainty as evidence of rejection or unchanged state. |

Late results remain evidence and accounting; they do not restore authority.

**Evidence of receipt.** Included, received by a provider, acknowledged, understood, agreed, and used are different claims. Notification acknowledgment must bind the exact inputs actually supplied to that recipient and decision. A historical cursor cannot prove observation of an older message that has only now become readable.

Recheck actual notification identities and permission at mutation. Missing inclusion cannot be repaired with a fabricated receipt. Fresh observation requires its own current authority and funding.

## Work and accepted responsibility

The system must keep the original need visible and show who has actually accepted responsibility for meeting it. Interpretation, an offer to help, delivery, and acceptance are not interchangeable.

**Need intake.** Preserve the exact original request, source, constraints, permitted assumptions, accepted changes, criteria, and closure terms. The persona may author an interpretation, but cannot silently reduce the need. Required outcomes must have accepted responsibility or a visible gap.

An unanswered ordinary question follows the [clarification boundary](../design/WORK-AND-BOUNDARIES.md#questions-assumptions-and-shared-context). Record provisional interpretation separately from confirmation, preserve real blockers, and reconsider affected assumptions when an answer arrives.

**Commitments and handoffs.** Keep membership, a contribution offer, commitment acceptance, and actual contribution distinct. Only real endorsements bind the named participant and terms. A handoff transfers responsibility only after the receiver accepts, or an authorized disposition explicitly replaces it.

Decline and nonresponse create no substitute acceptance, replacement persona, punitive reputation, or dependency on someone who never agreed.

**Organization.** Persona-owned organization uses discovery, proposals, communication, accepted commitments, and evidence-led revision. No task keyword, fixed profession roster, compulsory coordinator, birth rule, or hidden domain pipeline chooses the solution. A human-imposed constraint or explicitly adopted reusable method may legitimately guide work. Authorized evaluators need evidence of the actual orchestration policy; a convincing unscripted transcript is insufficient.

**Birth.** Each actual creation preserves its requested identity, seed provenance, initial model authorship and invitation. No application population or initialization quota applies. Creating a persona does not establish experience, expertise, membership or accepted responsibility. Duplicate requests preserve the actual creation outcome without inventing another identity; actual usage remains recorded even if participation is declined. Existing personas and simple work need no creation ritual.

## Capabilities and actions

The default runtime gives personas [full host access and tool installation](DEPLOYMENT-DECISIONS.md#default-full-host-access). Ordinary inputs supply that command interface directly. No per-tool approval, installation grant, command allowlist, sandbox, or prior skill-guide selection is required. Personas choose tools and commands using the host account and environment. The distinctions below describe actual preparation, execution and observed results; they do not introduce an additional permission gate for this default host interface.

Stored guidance helps a persona prepare for an operation. It does not establish that the operation is available, permitted, or ready to run. A skill file is reusable procedural guidance with an actual author. A persona-authored characteristic interpretation is persona-defining prose; the underlying procedure retains its supporting purpose. A tool note describes an operation and its observed limits. Neither stored guidance nor scripts, code, or data install a tool, prove competence, grant credentials, or execute a helper. Preparation and current callable exposure remain separate.

**Bind execution to what will actually run.** The required binding depends on the operation:

| Operation | Required binding |
|---|---|
| Default full-access host command | The exact command and inputs, host working directory and account, native runner and shell, and actual observed status/output. Transitive program versions are recorded only when actually observed. |
| Controlled local helper execution | The exact artifact, relevant resolved dependencies, environment, and inputs. |
| Remote operation | The observable service, interface, and connection identity, together with relevant exact client or runner versions and input versions. Unavailable server-build identity stays explicitly unknown. |
| Local helper that calls a service | Both the local and remote boundaries. |

An executable-version claim requires the claimed version to be genuinely bound to the observed operation. A filename, schema version, subsequently edited helper, or past success is insufficient. Missing server identity blocks a use only when the required assurance depends on that identity; otherwise, it narrows the claims that can be supported. All other admission and evidence safeguards in the [execution boundary](../design/WORK-AND-BOUNDARIES.md#capabilities-and-the-execution-boundary) still apply.

Exact code and bulk data may remain outside model context when an authorized runner consumes their references. The persona still receives relevant usage guidance and actual results under its chosen context; no application result quota is imposed.

**Keep each stage's meaning clear.** Finding an operation, supplying it to the model, and carrying it out establish different facts:

| Meaning | Required distinction |
|---|---|
| Discover | A bounded match or descriptor requested by the primary identifies candidates, exact versions, and honest search coverage. It is not endorsement, a full read, exposure of the full operative body, or authority. |
| Read | Exact permitted content, or a declared range or result, becomes an observation with provenance and qualifications. Reading documentation neither registers a callable native tool nor runs code. |
| Select | The primary requests exact fragments, supporting material, or bounded metadata for later context, with scope and disposition. Selection does not prove actual supply. |
| Load or expose | The host supplies the selected text and, where applicable, the actual operative callable definition. It records provider-facing and model-context exposure, qualifications, and omissions. Exposure grants no execution authority. |
| Invoke | A complete, valid, authorized decision requests an operation that is actually available, using the current interface, binding, inputs, and admitted resources. Storage, exposure, or a self-described permission is insufficient. |
| Observe results | The actual pending, failed, partial, completed, or effect-unknown outcome reaches an authorized fresh decision before dependent work proceeds. Output that looks successful does not prove correctness or delivery. |

These are observable meanings, not six required calls or a compulsory sequence. A known exact reference can be requested without discovery. A still-current, fully supplied interface permits immediate authorized invocation. Independent bounded requests may share a decision, but actions that depend on new content or results still require a fresh observation of that information. Provider-specific loading does not replace these distinctions.

**Saving a supporting asset and using it.** An ordinary supporting-asset change does not itself require another persona call when all of the following hold:

- The primary proposed the exact bytes and the dependent action.
- The proposal uses an already supplied, still-current interface.
- Coherent local acceptance binds the dependent action to the exact saved revision before dispatch.

This case uses the existing [complete-response and persistence boundary](#complete-response-persistence-and-dependent-work). It does not allow continuation through unobserved tool-produced content or results, or through a pending or unknown write. Storage creates no installed capability, grant, or callable exposure. All authority, dependency, effective-character, mode, and fresh-decision requirements still apply. A failed prerequisite or an applicable fence holds dependent work; a later receipt cannot revive suppressed actions. This clarification creates no automatic workflow facility.

**Native adoption and host writes have different interfaces.** Changes submitted through the native persona API follow the complete-response, version, character and persistence contract. A native helper must record an admitted change and its actual outcome rather than inventing a maintenance or execution receipt.

The default full-access host interface also permits ordinary filesystem writes and persona-authored scripts under the host account. Those commands are not confined to the native asset interface. This profile trusts the host account's access to backing files and does not claim that record-level controls isolate or make those files tamper-proof. Report host writes and their observed outcomes as host effects; do not label a direct file edit as a native API adoption.

**Record an action before dispatch.** An admitted action identifies:

- The actor, the work that caused the action, and a stable request identity.
- The exact relevant inputs, intended effect, capability, and current authority.
- The resources and the terms for observation or cancellation.

Durable intent precedes dispatch. Repeating the same accepted request must not duplicate its effect. Changed content under the same identity is a conflict.

**Use observed outcomes for dependent work.** A running operation does not satisfy a dependent action. Suppress the unobserved remainder of its decision; dependent work requires a fresh decision bound to the actual result. Preserve the distinctions between proposed, admitted, running, failed, completed, stopping, canceled to the observed extent, and effect-unknown states. Reconcile uncertain outside effects before repeating them. Completed execution establishes neither correctness nor delivery.

**Keep operations usable and controllable.** Available operations must be usable from their actual loaded guidance, with clear identity, version, replacement, and effect meanings. Current successful receipts should expose appropriate inspection options without requiring a decision devoted only to discovering syntax. Compaction must not hide control of unresolved jobs. Old terminal history, however, need not keep every operation permanently loaded. Projection is not permission, deletion, or evidence that an artifact was inspected.

**Treat changing resources according to what was observed.** Distinguish exact historical snapshots, current live references, cached observations, and derived outputs tied to their actual inputs. An unversioned path or a notification is not a fresh observation of the payload. Resolving a reference identifies the version actually obtained. Reuse checks source and work scope, permission, and freshness without claiming a new read. Paginated results need not form a coherent snapshot.

A requested watch, acknowledged supported coverage, an active stream, and an ended or unsupported watch are different states. Lost notifications cannot establish that data is unchanged. Notifications may invalidate retained bindings, but cannot automatically select new content, enable a removed capability, or authorize an effect.

## Authority, resources, and stopping

The application follows [unrestricted execution](../design/WORK-AND-BOUNDARIES.md#unrestricted-execution-requirement). Do not require a quota increase, resource grant, safety permission or approval to continue work, run tools, navigate history or retain results. The former protected-allocation contract is superseded by UR-052.

**Measure actual use without making it an admission gate.** Record model calls, tool executions, unsuccessful attempts, navigation, selected context, maintenance and result retention. Distinguish transport bytes, reported tokens, billed usage, latency, storage and monetary exposure. Unknown usage remains unknown, and smaller context does not establish lower total cost or useful completion.

Retain fragments, supporting assets, histories, tool definitions, code, provenance and unresolved effects with their actual identities. Context selection and requested pagination decide what is supplied to a model input, not how much historical state may exist or how many calls a task may use. Do not erase evidence to satisfy an obsolete quota. Report real I/O, provider and representation failures with their observed outcomes.

**Separate a local stop from the goal's status.** Record the reason for a local stop separately from the accepted goal's disposition under [continuing pursuit](../design/WORK-AND-BOUNDARIES.md#continuing-a-goal-across-local-boundaries). For unfinished continuing work, bind the record to:

- The current mandate and owner.
- The exact candidate and the outcomes still unmet.
- Actual observed usage and unresolved resource failures.
- The actual continuation opportunity, or the blocker and route for reconsideration.

If these cannot be established, expose the continuation gap. Transfer or ending needs its applicable authority. Existing work records suffice; no universal new file schema is required.

**Give eligible accepted work a real opportunity to continue.** An accepted ordinary-work continuation preserves its actual eligibility across yield, result delivery, and restart. Under the declared supported fairness and capacity assumptions, persistently eligible accepted work must receive another decision opportunity. Merely keeping it visible in a queue is insufficient. Queue churn and pagination cannot evade this obligation. Expose unmet scheduling assumptions or failed consideration as limitations, not task completion.

Before a fresh primary decision, recheck explicit pause or cancellation, current work, decision identity and actual observations. A fresh decision does not replay a suppressed action batch. A valid dependency wait need not become polling; a wished-for reply is not an event. A partial result or safe stop can handle a boundary correctly while leaving the full task unfinished.

## Review and release

A review must support the claim being made about the work. An ordinary self-check or peer comment can be an attributable assessment without becoming a formal review commitment. When the adopted acceptance policy requires a review, an informal assessment does not silently satisfy that requirement.

**Bind a required review to its actual basis.** It must identify the exact scope, criteria, inputs, and assumptions; a reviewer who has actually accepted the review; applicable funding and independence policy; observations; explained judgment; findings; and limitations.

Command counts and successful exits do not determine a verdict. Text may receive a reasoned review without an invented command. Technical claims need observations appropriate to those claims. A different persona is not automatically qualified or independent.

**Preserve both agreement and dissent.** A [shared sufficiency disposition](../design/WORK-AND-BOUNDARIES.md#individual-and-shared-sufficiency-judgments) records whether the group considers the work sufficient while preserving the exact candidate and scope, attributed judgments and dissent, the actual adopted decision basis, required gaps, and remaining commitments.

The host checks applicable authority and record consistency. It does not infer a semantic completion verdict from everyone stopping, a majority, an editor's identity, or a resource limit. Delivered version, accepted-goal completion, required stakeholder acceptance, and later improvement retain separate states and evidence.

**Keep review evidence tied to when it was captured.** A citation snapshot records the exact stage and content genuinely captured. Identity established at recording time does not prove earlier inclusion, attention, or understanding. A changed receipt, artifact, assumption, criterion, or relevant dependency changes the verdict's current applicability without rewriting the original verdict. Missing snapshot evidence stays missing. Never retrofit an old assessment with a newly observed result.

**Release the state that was actually reviewed.** Release binds one coherent reviewed state, legitimate blocker dispositions, exact delivered scope, and current authority. The order of an update and release matters:

| Order | Consequence |
|---|---|
| Update before release | Stale acceptance cannot support release. |
| Release before update | Acceptance remains valid only for that historical state. |

An empty optional citation list creates neither automatic review nor release. An unresolved mandatory finding, missing required output, or unavailable recipient access prevents the affected full-delivery claim. Partial results retain their gaps. Digital delivery does not authorize construction, publication, spending, or another outside effect.

## Recovery, privacy, and retention

Recovery preserves accepted state and unfinished work without inventing success or replaying accepted effects. UR-052 removes application access, source-sharing and retention quotas; actual provenance, exact identities, explicit stops and truthful outcomes remain necessary.

**Recover related state together.** Preserve current character and fragments, modeled state, selected context, adopted maintenance dispositions, unresolved corrections and warnings, accepted responsibilities, pending effects, unknown usage, cancellations and undelivered events. Notifications retain their actual identities and repeated delivery is recognizable. Restart, import and rollback do not manufacture a new persona origin, acceptance, provider result or observed effect.

**Preserve actual information use.** Record source relationships, supplied content and destinations. A summary or new filename does not change which source informed an earlier decision. Clearing later selections does not undo earlier exposure. Application metadata is not a claim of isolation from the host account or control over provider and recipient copies.

**Retire stale guidance honestly.** Persona-authored retirement and explicit deletion decisions retain their actual scope. Filename reuse, old links and indexes must not silently turn retired material into current guidance. If a record or body is unavailable, report that fact; do not reconstruct its bytes, rewrite the original or claim a read that never occurred.

**Missing receipts do not make old requests new.** An old action or invocation identity cannot become fresh unsent work merely because its receipt is missing. Keep an unavailable or uncertain outcome explicit and preserve any evidence needed to avoid duplicating an accepted transition. A new identifier does not establish that a previous effect never occurred. Fresh work uses current decisions and actual dependencies; an unknown bill alone is not a quota gate.

**Retention and meaning are different.** A fragment can retain a fallible interpretation after its original supporting evidence becomes unavailable, but it cannot provide the missing observation or establish a historical claim that requires it. A digest does not restore source text. Losing a body does not resolve a warning, commitment or uncertain effect.

Semantic consolidation and retirement remain primary-authored. Mechanical cleanup follows a real accepted retention or deletion choice. Do not erase records or modify user-owned delivered artifacts to satisfy an obsolete application ceiling. Record actual storage failures and incomplete saves. A small active corpus does not establish a small managed footprint, indefinite storage or control of arbitrary outside copies.

**State the actual environment.** A shared host account and native record metadata do not provide filesystem isolation. Claims of confidentiality, evaluator independence or immutable execution must identify what actually establishes them. This requirement concerns truthful claims; it does not add an application sandbox, safety approval or source-access gate.

## Evidence boundary

These contracts state required behavior; they do not report that a runtime implements it. [Acceptance](../evaluation/ACCEPTANCE.md) tests mechanics and behavior separately, and the [evaluation method](../evaluation/README.md) governs useful-work comparisons. Historical graph and selector results retain their [original criteria](../evaluation/HISTORICAL-RESULTS.md). The [status ledger](STATUS.md) identifies current implementation and evaluation gaps. Documentation checks do not establish product acceptance.
