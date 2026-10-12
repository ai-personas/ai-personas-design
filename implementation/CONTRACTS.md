# Observable system contracts

[Implementation guide](README.md) · [Persona core](../design/PERSONA-CORE.md) · [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) · [Requirements](REQUIREMENTS.md) · [Acceptance](../evaluation/ACCEPTANCE.md)

These contracts describe behavior that people and connected components must be able to observe. They are design requirements, not implementation code, a database layout, a programming interface, a required file tree, or a prescribed sequence for solving tasks.

The protected foundation is I01–I21. The persona core explains what the persona means; the work-and-boundaries chapter explains its constraints; these contracts explain what must cross a reliable handoff. These are complementary normative views. None silently overrides another. A conflict requires an explicit recorded resolution. Until then, preserve the conservative authority and evidence boundary. The requirement index traces these rules; it is not a shorter substitute for them.

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
| Resources and recovery | Root allowance, cumulative navigation limits, declared persona-context corpus, assembled-prompt and managed persona-state bounds, retention scope, reservations including peak rewrite copies, consumed and uncertain exposure, protected finishing capacity, pending events, cancellation, and stopping or continuation disposition. |

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

If no continuation has been accepted, expose that gap. Missing observations, an authoring prohibition, a persistence outage, or exhausted allowance must not become a promise of automatic retry. An adopted deferral remains visible until it is addressed, explicitly dismissed, transferred with acceptance, or closed with an honest unresolved or expired disposition when its bound or relevant work ends. Expiry does not mean evaluation or repair. Host closeout does not fabricate a persona judgment. Deferral creates no new wake, funding, or authority. A mode-limited outcome need not create a new obligation when no useful change has been identified.

**Continuing applicability.** Ending a correction effort does not remove a separately accepted warning. A primary-authored warning on exact affected fragment revisions or explicitly identified dependent uses remains effective after the effort is closed, dismissed, or expired. Preserve its permitted basis and required qualification, or a safe ineligible disposition, across later work and restart until an attributable, justified resolution is accepted.

Such a warning needs its own real, authorized durable disposition, which may be a maintenance receipt. A proposed or failed patch does not create a warning automatically. A content patch rejected for quota can coexist with a separately authorized accepted warning only when the applicable authoring, storage, and resource limits permit that warning. If persistence of the warning fails or is unknown, block affected admission or retain the honest uncertainty. Do not claim that a warning was saved or that the guidance is unqualified and safe.

Source restrictions and retention still apply. Unavailable warning text or evidence requires a safe ineligible disposition or a block, never private disclosure or resurrection of erased bytes. Enforce only explicitly scoped meaning from valid, authorized primary judgment. An unassessed peer contradiction, host truth engine, or archive-wide semantic search cannot create a restriction. Warning adoption and resolution obey the same mode and character-authoring limits as other semantic changes.

**Invalid or absent response.** Missing or malformed maintenance or next-context intent, an incomplete stream, structurally uninterpretable maintenance operations, or any other invalid response prevents new adoption and dispatch of all proposed substantive actions from that response. This includes communications, reads, and selection changes. Do not salvage a plausible tool call or reply from an invalid prefix.

Provider refusal, transport failure, timeout, and cancellation retain their actual status and exposure. They are not persona-authored no_change outcomes. A valid persona-authored refusal still includes maintenance and next-context dispositions within its mode; the host fabricates neither for a provider refusal.

After rejection, prior accepted selection remains stored only under its existing validity and recovery rules. This is not an authored preserve or successful consideration. Already admitted effects remain real. Missing intent creates no automatic paid repair, retry, or new allowance. Host status reporting may disclose the actual failure without presenting rejected output as an accepted persona response.

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

Before accepting a change, check that the resulting mandatory state remains admissible. This includes current character, maintenance input, exact required qualifications, source ancestry, and other protected context. Both the peak rewrite footprint and the resulting retained footprint must fit. Repeated small revisions must not create an unusable state merely because the visible prose is short.

Independent work is eligible only under the complete-response and dependency rules above. Uncommitted prose supplies neither authority nor received evidence.

**Visible evidence.** Preserve the actual author, adopted source where relevant, prior and accepted revisions, committed changes, conflict or failure, and origin of any outside edit. A peer's suggested wording is not already the owner's account. An operator override follows an explicitly authorized and attributed path.

**Initialization and later harmonization.** Initial generation uses the same coherent acceptance boundary, with an attributed seed instead of a nonexistent prior character. Bounded retries preserve creation identity and the actual accepted outcome. Sparse generated detail is candidate authorship, not an invented user preference or lived history.

Later self-harmonization is ordinary primary-authored maintenance. It preserves compatible conditional tensions, exposes unresolved contradictions, and revises only within existing authoring and character controls. It creates no second writer, mandatory corpus-wide rewrite, or automatic trait drift.

No extra reflection writer, relationship writer, semantic merger, or generic prose generator maintains the persona behind its back. Work and the explicit maintenance outcome belong to the same invocation. Useful mutation is discretionary; explicit maintenance is not. A retained maintenance deferral follows the bounded, attributable lifecycle above and does not itself schedule inference.

**Honest authorship and experience.** First-person wording does not turn supplied advice into firsthand experience. A tentative intention may be retained before an operation completes; a later observed result cannot be backdated. Evidence that an operation failed supports an interpretation of that failure. An uncertain effect establishes uncertainty.

Authorship controls apply to effective current identity, including redesignation or an always-loaded substitute. They do not forbid ordinary qualified methods and relationship refinement. Mechanical controls cannot promise complete detection of semantic bypass in free prose; that limitation also needs behavioral evaluation.

A persona-defining contextual fragment need not revise relatively stable character. A scoped method or relationship interpretation can shape the next invocation while accepted character remains locked. An effective substitution of that character still requires its existing authority, proposal ordering, and fresh-decision fence. Calling the substitution context assembly does not bypass those controls.

## Search and exact reading

Search helps the primary persona find candidate fragments and supporting resources. It does not decide what is relevant, select context, or grant permission to use what it finds. The primary chooses bounded searches and exact reads within the authorized scope.

**Input.** A primary-persona-chosen bounded listing, literal or grep-like query, supported regular expression, or exact reference, within the authorized fragment or supporting-resource scope and remaining cumulative navigation allowance. Supporting resources include history, tool records, definitions, skills, scripts, code, and data without merging their roles. An authored associative cue may motivate a request, but it is data—not executable shell content, an access grant, or a trigger.

**Accepted result.** Bounded results identify the searched corpus, matching mode, exact source-qualified candidate revisions, and how to request permitted text or operative definitions. Where available, a concise descriptor or matched excerpt provides purpose and compatibility information for the next choice. It must not pretend to supply the body.

Declare the search's relevant filename/body/metadata scope, case and text semantics, pattern dialect, ordering, pagination, and treatment of hidden or ignored files. Bound result size as well as result count.

Bounded listing, literal or regex search, simple owner-authored indexes and cues, and exact reading form one navigation interface. The primary uses it to choose characteristic context and separately needed supporting material. The primary also chooses query expansion and further navigation. There is no fixed taxonomy, graph or vector retrieval engine, auxiliary semantic retriever, or universal relevance scorer. Physical storage and indexes may support the interface only while preserving its declared matching and boundary guarantees. Corpus changes may change current candidates; they do not alter a prior exact observation or selection.

**Pagination and completion.** Declare whether pagination is snapshot-bound, revision-bound, live, or otherwise consistent, and whether a completion indication covers a page, scan, or identified corpus view. Exhausting a live page or cursor does not prove that the traversal exposed every item that matched earlier.

Preserve exact observations and disclose known cursor invalidation or coverage uncertainty. Claim coherent or exhaustive traversal only with supporting evidence. Continuation or restart is primary-chosen within the same cumulative allowance. These rules do not require a snapshot service, universal scan, automatic restart, or semantic ranker.

**Failure behavior.** Keep no match, unavailable scope, stale reference, unsupported or invalid pattern, incomplete search, exhausted bound, and storage failure distinct. A stale result must not silently open newer bytes as though they were the earlier observation. Search must not leak inaccessible titles, snippets, relations, or counts. Index lag needs either a bounded discovery path to the current store or a visible limitation, never an invented exhaustive result.

**Visible evidence.** Record search scope and completion, returned candidate identities and revisions, actual full or partial reads, observation time, and provenance. Model-visible descriptors, excerpts, and reads may influence the receiving decision even without persistent selection. A snippet is not a full read. A full read is neither endorsement nor persistent selection. Raw host command output is that command's observation; it does not manufacture a trusted accepted-file receipt.

**Small initial bootstrap.** Initial discovery supplies only bounded usable discovery, exact-read, and exposure affordances; permitted scope information and limits; the mandatory persona/work core; and any legitimately known bounded references. It must not require loading all resource names, descriptions, namespaces, or manifests before choosing among them. Discover scope metadata in bounded portions when needed.

Keep the bulk registry outside every choosing LLM and outside its provider request. Preloading a catalogue and asking an LLM to filter it is not selective discovery. An external service's paginated listing is not itself lexical search. An adapter that fetches or indexes pages must enforce the declared host-work budget and return only the primary-requested bounded subset. Permission-filter all metadata before exposure, including titles, counts, and source associations.

**Host and primary responsibilities.** The host evaluates only requested searches, under declared pattern-language, processing, and returned-text limits. It does not execute cue or query text as commands, follow associations recursively, expand neighborhoods on its own, enumerate all pages for model filtering, or select matches automatically. Only the primary persona judges relevance. Authored associations, exact historical references, and mandatory qualifications keep the [distinct meanings in the core](../design/PERSONA-CORE.md#ordinary-files-and-self-organization).

**Cumulative navigation limits.** Bound fanout, branch expansion, cumulative calls and reformulations, inspected revisions and revisits, returned text, context, time, and cost within the current purpose. A bounded current-work account exposes prior queries, exact visited revisions, and mechanically reused results; it is not an unlimited lifetime traversal log.

Cycles and new query wording do not reset the allowance. A useful revisit after changed evidence is permitted within it. Deduplication never claims that a new read occurred. During authorized maintenance, the primary may revise stale or overbroad cues. The host invents no semantic redirect or replacement link. Alias and successor retention is bounded, and an expired exact reference cannot resolve to different bytes.

**Complete guidance and its qualifications.** The runtime faithfully preserves accepted text. It does not substitute a hidden summary or infer required caveats from semantic similarity. Essential qualifications should normally sit beside the method. If they are authored separately, an explicit required-accompaniment binding preserves the exact complete bundle, including transitive prerequisites and corrections.

Deduplicate exact identities, including cycles, without dropping distinct conditions. An optional navigation cutoff cannot truncate the bundle and leave the method presented as usable. Ordinary hyperlinks and associative cues support navigation; they do not automatically create authority or mandatory accompaniment.

If a required part is missing, revoked, stale, or too large, the affected method cannot be represented as a complete usable bundle. The primary may repair it under current authority. The runtime may not silently drop the qualification to fit.

**Different kinds of dependency.** Operative guidance closure means the complete guidance and required caveats needed by the affected decision. It is distinct from executable dependencies, provenance/restriction closure, and data-derivation lineage. Required caveats must reach the decision; every code dependency, ancestor document, or data row need not.

Where supported, resolve and enforce non-prompt dependencies outside model context while retaining enough evidence for the actual claim. Missing required dependency, integrity, or source-policy evidence blocks affected use. An exact requested range or data slice is a partial read. It cannot stand in for a complete operative contract or a dataset-wide observation.

**Previously accepted warnings.** A version-bound applicability warning remains effective when an unchanged index, preview, or exact read rediscovers the same guidance in new work. Do not falsify retained bytes or historical attribution. Retain or erase payloads under the declared policy while preserving the permitted accepted warning or a safe ineligible disposition. This is not a promise to retain payloads forever.

Do not present a warned revision or explicitly covered dependent use as unqualified current instruction. Supply its permitted accepted qualification or a safe ineligible disposition. An inaccessible mandatory warning blocks affected admission. Ending a repair attempt does not remove this accepted binding.

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

Withholding an ineligible optional bundle does not permit discarding valid selected text merely to fit an ordinary task decision. Later size pressure on a previously valid selection uses only the restricted repair decision below. New work begins with its own mandatory brief and observations. Another work's private focus or persistent optional selections do not transfer automatically.

**Explicit disposition in every accepted response.** Every accepted persona response authors its next-context disposition for both characteristic fragments and supporting resources. A concise, unambiguous preserve of a still-appropriate accepted choice is sufficient. Other valid dispositions are replacement, clear, no further optional need, bounded discovery/read intent with explicit retained or cleared optional state, or an honest mode-permitted blocked/stop outcome.

No new search, mutation, repeated list, full-body dump, extra model call, or fixed field schema is required. “No further optional need” explicitly chooses an empty future optional set: it clears an existing set or keeps an already empty one empty. If the mode forbids that change, state retained/blocked selection instead. This affects neither mandatory context nor already exposed observations or retained history.

When initialization has no accepted optional set, it may explicitly choose no optional context or request bounded discovery while keeping it empty; it cannot preserve a nonexistent choice. Final, short, social, refusal, and tool-follow-up responses are covered without requiring continuation. A blocked/deferred choice may retain stored ineligible selections as ineligible; it never makes them usable exposure.

Explicit selection can still be poor judgment. For example, preserving irrelevant but eligible material is a selection-quality failure to evaluate, not evidence that the response contract prevents all semantic mistakes.

**Visible evidence.** Preserve who chose; the exact requested and selected versions or ranges; scope and lifetime; preservation or change of the choice; and actual provider-bound text and callable schemas with qualifications. Include message/channel roles, boundaries, and order as actually rendered, rendered expansion and retained context where applicable, requested previews, actual omissions, and any mismatch that blocked admission.

Host registry storage, provider transmission, model-context inclusion, and billed input need separate evidence. Inspection respects access and retention. Retain sufficient exact identity without requiring an unnecessary raw prompt or private reasoning archive.

**Mandatory state and the host's role.** The runtime adds current authority, cancellations, obligations, blockers, critical observations, coherent current character, relevant modeled state, and maintenance responsibility and limits. These are protected work and policy state. They do not make the host an independent semantic selector of persona-defining context.

The declared file-search interface and primary-navigated authored cues or indexes expose candidates without choosing optional prompt parts or authoring their meaning. Auxiliary semantic, vector, or graph-retrieval engines are different research comparators, not production options or fallbacks. Ordinary external task tools remain available within their permissions. Their results still need primary judgment and cannot silently replace fragment navigation or authorship.

**New observations.** An unexpected reply or failure enters relevant current observations even when the prior choice did not anticipate it. In an ordinary decision, the persona can then search, read, and choose prompt parts for an appropriate next approach. A search hit does not automatically add a fragment to context, and an old selection must not suppress a new adverse fact. A permitted same-call authored change applies to subsequent context; it cannot rewrite what the current decision received.

**Complete request admission.** Validate the whole request for every provider attempt. The total includes:

- Bounded bootstrap and instructions; current character and modeled state; maintenance/next-context input and outcome allowance.
- Observations and results; requested metadata; complete operative schemas and provider expansions.
- Selected fragments and supporting material with their qualifications; continuing history and protocol bindings; media where applicable; and output reserve.

Per-item limits, count limits, or a small latest message do not bound the aggregate. Do not silently shorten selected prose to a title, remove an exception, or choose a different semantic substitute.

Reject a proposed selection that is already inadmissible when committed, preserving prior accepted state. A different case arises when new mandatory observations make a previously valid accepted selection too large for an ordinary decision. Ordinary admission then remains blocked; the restricted selection-repair decision below may be available. Optional discovery previews may be omitted with an honest scope limit, but that omission does not prove that no relevant resource exists.

**Actual exposure and retained context.** The [bounded capability working set](../design/WORK-AND-BOUNDARIES.md#inference-and-bounded-working-context) applies to actual exposure, not merely the host's intended list. Reassemble successive contexts within accepted scope and retirement rules instead of retaining every past tool, skill, and result. Preserve active-operation controls, critical results, current authority, character, and other mandatory state.

Cached prefixes, previous-response links, and hidden provider history neither prove absence nor eliminate exposure. Automatic schema or tool-set expansion must be known and admitted in full. An adapter with unbounded or unobservable expansion or history cannot claim the hard next-call bound. Use a supported bounded continuation/reset or report the limitation. Provider-native deferral that still transmits the bulk catalogue fails the transport rule. The host must still reject stale or unauthorized invocations even if the model remembers an old tool name.

### Restricted selection repair after later context growth

A previously valid optional selection can stop fitting when mandatory context grows. Restricted repair lets the primary narrow or clear that optional selection without pretending that an ordinary task decision still fits. It is a limited persona decision, not an auxiliary selector or permission to resume the task.

**Admission and required input.** Label the repair explicitly. It uses the same current identity, assigned inference configuration, authority, and controlling resources. Declare its finite attempt allowance before admission; repair creates no extra funding.

The repair context must contain current character, relevant modeled state, mandatory work and policy state, accepted obligations, cancellations, blockers, consequential observations and evidence, resource facts, maintenance and next-context responsibilities, and restricted repair instructions. It may also contain a bounded, access-filtered inventory of the exact stored selection and mechanical fit diagnostics.

**Transparent withholding.** Selected optional bodies and their qualification bundles may be withheld from the repair request. Text or qualifications independently required by the mandatory core must still be supplied, even if optional selection also references them. The receipt records actual supply; it must not call those supplied bodies withheld.

The supplied-context receipt records the eligible exact bodies withheld, the inventory or previews supplied instead, why ordinary admission failed, and a safe disposition for any incomplete inventory or unavailable entry. It must not reveal inaccessible identities or content, or present a preview as a supplied body or complete method.

Withholding changes no stored choice, source restriction, observation history, or accepted responsibility. Only an accepted primary repair changes selection.

**Permitted activity.** Repair may only narrow or clear optional selection, request the necessary bounded repair reads described here, or honestly stop. It cannot rewrite current self, edit the meaning of fragments or supporting records, change mandatory state or required qualifications, switch models, publish a deliverable, or perform any substantive task action. This prohibition also covers task actions based on mandatory observations rather than previews. Inventory and previews do not establish the underlying task evidence.

A read for repair must be permitted, exact, fully qualified, and able to fit the repair context. If it would overflow or omit a required part, it is unavailable; it must not be silently shortened. A later authorized repair decision must observe the actual read result before making a dependent choice, within the same remaining allowance and ordinary observation boundary. Narrowing or clearing must remain possible without reading every withheld body.

If the mandatory repair core cannot fit, or current authority, funding, or remaining repair allowance cannot support it, block without dispatch.

**Required response.** Repair includes an explicit mode-limited maintenance outcome and a next-context disposition covering fragments and supporting resources. For an allowed repair read or honest stop, the response may explicitly retain stored selection while awaiting evidence or leaving ordinary admission blocked. It cannot claim that preserving an oversized set repaired its fit. Missing intent invalidates the response without clearing stored state.

No_change is valid when available evidence identifies no justified maintenance change. It does not claim inspection of withheld files. If a useful candidate change is known but prohibited in this mode, report it as bounded blocked or deferred. Unchanged files alone do not prove that no useful change exists.

The mode permits no asset creation, semantic edits of fragments or supporting resources, hidden broad rewrite, or additional mandatory reflection call. Missing or malformed maintenance invalidates repair just as it invalidates an ordinary response.

**Warnings remain subject to mode.** When the mode forbids semantic changes, repair cannot adopt a new applicability warning or required qualification through its maintenance receipt. It may report the candidate as blocked or deferred, preserve received mandatory observations, and narrow or clear optional selection. Existing accepted warnings retain their force. A new warning requires a later ordinary decision with the necessary authority. Neither warning adoption nor resolution may bypass locked-character controls.

**Adoption and return to ordinary work.** At adoption, recheck source versions, qualifications, permissions, current self, mandatory state, and authority. A change during repair does not justify following newer bytes, reviving an unavailable source, or overlooking a new blocker.

After accepted repair, require fresh normal admission. That request supplies the remaining exact selected full text and complete qualifications alongside the then-current mandatory state. The repair response cannot itself perform resumed task actions. A successful selection change does not guarantee that normal admission will fit or be authorized.

**Failure and remaining allowance.** An admitted failed, uncertain, or no-op repair retains its resource and attempt charges. Restart, repeated diagnostics, a new event, or an unchanged choice does not reset the allowance. A later restricted repair may observe its predecessor's actual receipt only within the remaining bound.

If repair cannot produce an admissible normal context, preserve the exact disposition and stop or block. Do not invent progress, supplied text, or additional authority.

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

**Birth, where enabled.** Each creation preserves truthful provenance, a restricted seed and invitation preview, population and initialization limits, and bounded orientation. Creation grants no money, permissions, experience, membership, expertise, or commitment. Duplicate and concurrent requests must conserve the controlling limits. Declined participation does not erase spent resources. Existing personas and simple work need no creation ritual.

## Capabilities and actions

Stored guidance helps a persona prepare for an operation. It does not establish that the operation is available, permitted, or ready to run. A skill file is reusable procedural guidance with an actual author. A persona-authored characteristic interpretation is persona-defining prose; the underlying procedure retains its supporting purpose. A tool note describes an operation and its observed limits. Neither stored guidance nor scripts, code, or data install a tool, prove competence, grant credentials, or execute a helper. Preparation and current callable exposure remain separate.

**Bind execution to what will actually run.** The required binding depends on the operation:

| Operation | Required binding |
|---|---|
| Controlled local helper execution | The exact artifact, relevant resolved dependencies, environment, and inputs. |
| Remote operation | The observable service, interface, and connection identity, together with relevant exact client or runner versions and input versions. Unavailable server-build identity stays explicitly unknown. |
| Local helper that calls a service | Both the local and remote boundaries. |

An executable-version claim requires the claimed version to be genuinely bound to the observed operation. A filename, schema version, subsequently edited helper, or past success is insufficient. Missing server identity blocks a use only when the required assurance depends on that identity; otherwise, it narrows the claims that can be supported. All other admission and evidence safeguards in the [execution boundary](../design/WORK-AND-BOUNDARIES.md#capabilities-and-the-execution-boundary) still apply.

Exact code and bulk data may remain outside model context when an authorized runner consumes their references. The persona must still receive complete relevant usage guidance and bounded actual results.

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

**Helpers and writes must follow accepted-state controls.** Runners, primary-authored code, and workspace write access do not bypass those controls. A helper may implement an already-admitted exact change only through the same whole-response, version, authority, character, source-policy, resource, and retention checks. It cannot independently adopt persona or supporting-resource meaning, forge action or maintenance receipts, or alter its own bindings, grants, or admission checks.

A direct write to protected backing state outside that acceptance path does not automatically become accepted context or recovery state. Where appropriate, treat permissible content as an unaccepted candidate; otherwise expose an integrity failure. A purported or corrupted receipt needs trustworthy evidence and reconciliation. Its claims cannot simply be adopted as true.

Ordinary admitted data and artifact outputs remain possible. Refuse a write or block affected use when these guarantees cannot be preserved. No particular folder layout or new service is required.

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

Permission and resources both have limits. Every grant is scoped, revocable, and no broader than its parent. Reserve resources before spending or dispatch. Initialization, tools, descendants, inference, unsuccessful attempts, maintenance, auxiliary discovery, review, and finishing all count toward the same controlling allowance. Expose unknown usage; never assume it is free. A genuinely closed local failed decision and its conservative metering are separate facts. Uncertainty cannot fund a retry.

**Measure the whole cost of obtaining and using context.** Context efficiency applies both to each admitted call and to the complete work episode. Count bootstrap and returned metadata, host scans and index work, exact reads, operative-schema loading and reloads, continuing provider context, output, maintenance, failed branches, and retries.

Report transport bytes, model-visible tokens, billed tokens, latency, storage, and monetary exposure according to what is actually measured or conservatively bounded. These measures are distinct. Fewer tokens in a final action call do not establish lower total cost or useful completion. Compare discovery overhead and avoided irrelevant context alongside task quality and harmful omissions, using matched resources.

**Protect capacity for finishing.** Agreed review, repair, and closeout capacity is protected from ordinary exploration unless explicitly reallocated. Optional between-task exploration needs an actual authorized trigger, finite bounds on both the episode and its recurrence, expiry, and stopping terms.

A new input, restart, changed cursor, repeated narrative, or fresh filename does not reset a recovery or exploration allowance. Local preparation rejected before admission is distinct from an admitted call that fails or remains uncertain. A fragment, deferral, search miss, or empty selection does not create an idle reflection loop.

**Bound all managed state, not just the current prompt.** Declare and enforce separate bounds for:

- The persona-context corpus of prompt parts.
- The assembled prompt supplied to an invocation.
- The total managed persona-state footprint.

The total footprint includes both the corpus and its supporting resources. Account for all of the following wherever they are managed:

| State or storage | Included material |
|---|---|
| Fragments and navigation | Current and archived fragments, versions, cues, indexes, and aliases. |
| Supporting resources | Histories and tool records, retained definitions and skills, scripts and generated helpers, dependency caches, data snapshots, and derived outputs. |
| Evidence and operational records | Source evidence, provenance and qualification closures, warnings, and relevant effect and supplied-context records. |
| Additional managed copies | Caches, managed exports and backups, external backing stores, and peak temporary rewrite copies. |

Separating these materials by purpose does not exempt any managed backing from accounting. Reserve storage for required warning, reconciliation, and closeout state before accepting optional additions. Before accepting a write or closure change, check peak occupancy and resulting retained occupancy; later reclamation is credited only to the extent actually established. An unknown external footprint cannot support a verified total-state-cap claim.

Report retained and reserved occupancy, applicable limits, actual or uncertain reclamation, retention scope, and blocked writes. Fewer active files do not necessarily mean a smaller managed footprint.

When protected state cannot fit, block affected admission and expose the authorized retention or capacity decision needed. Do not erase required warnings, restrictions, caveats, obligations, or unsettled effects to meet the cap. Do not move them into an undeclared unlimited archive. Refusing an optional new fragment need not block unrelated admissible work.

**Separate a local stop from the goal's status.** Record the reason for a local stop separately from the accepted goal's disposition under [continuing pursuit](../design/WORK-AND-BOUNDARIES.md#continuing-a-goal-across-local-boundaries). For unfinished continuing work, bind the record to:

- The current mandate and owner.
- The exact candidate and the outcomes still unmet.
- The remaining resources.
- The actual continuation opportunity, or the blocker and route for reconsideration.

If these cannot be established, expose the continuation gap. Transfer or ending needs its applicable authority. Existing work records suffice; no universal new file schema is required.

**Give eligible accepted work a real opportunity to continue.** An accepted ordinary-work continuation preserves its actual eligibility across yield, result delivery, and restart. Under the declared supported fairness and capacity assumptions, persistently eligible accepted work must receive another decision opportunity. Merely keeping it visible in a queue is insufficient. Queue churn and pagination cannot evade this obligation. Expose unmet scheduling assumptions or failed consideration as limitations, not task completion.

Before a fresh primary decision, admission rechecks pause or cancellation, current authority, observations, source eligibility, and capacity. This admits neither a suppressed action batch nor a new budget. A valid dependency wait need not become polling; a wished-for reply is not an event. A partial result or safe stop can handle a boundary correctly while leaving the full task unfinished.

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

Recovery must preserve the accepted state and unfinished responsibilities needed for honest continuation. It must also respect current source restrictions and retention rules. A restart cannot create permission, evidence, or a successful outcome that did not exist before it.

**Recover state and its required notifications together.** Restart preserves:

- Accepted character and fragments, separately scoped modeled state, selections, and invocation and maintenance dispositions.
- Unresolved adopted deferrals, independently accepted applicability warnings even after their correction effort ends, obligations, and unresolved findings.
- Pending effects, reservations, unknown exposure, cancellation, and undelivered events.

Accepted state and its required notification recover together, subject to current source restrictions and retention. Repeated delivery must be recognizable. Waiting must be safe whether the awaited event arrives before or after registration. Import or rollback creates neither a new founder, new money, a successful effect, nor cross-host activation authority.

**Carry source restrictions through every use and derivative.** Restrictions apply to reads and to search, indexes, snippets, summaries, self-prose, methods, relationships, selections, caches, exports, errors, and backups. Shortening or generalizing a private interpretation does not declassify it, even when it becomes persona-defining prose.

Withdrawal prevents new affected use and disclosure. A call already exposed to content cannot erase that lineage by clearing context. Preserve actual or uncertain effects, and use a fresh permitted context or an honest block where needed. Do not promise to retrieve bytes already disclosed or undo an unobservable outside effect.

**Retire stale guidance without losing required accountability.** Correction and retirement preserve minimal historical accountability under the deployment's retention rules while making stale guidance ineligible as current instruction. Filename reuse, links, old selections, and index entries must not resurrect retired or erased material. Keep deletion limits for outside copies explicit.

**Missing receipts do not make old requests new.** An expired, reclaimed, or unknown old action or invocation identity cannot be admitted as a fresh request, treated as an unsent effect, reopened, or replayed because its receipt is unavailable. Return an honest unavailable or unresolved disposition. Require the current authority and reconciliation appropriate to the intended effect. A new identifier alone cannot bypass uncertainty about a prior effect.

The retention design must preserve this boundary without requiring a particular tombstone or epoch mechanism. If it cannot preserve the boundary, block affected admission. Do not reclaim necessary protection or promise unlimited hidden history.

**Distinguish evidence expiry from withdrawal of permission.** Permitted raw-evidence expiry is not revocation. An accepted experience-informed fragment may continue to shape the persona only when the governing retention and derivative-use policy allows it. Its interpretation remains fallible, with allowed attribution, surviving restrictions and caveats, and an honest unavailable-evidence limit. Continuing to express a method does not establish recollection or inspection of the expired event.

If exact evidence is required for present use, withhold that use or block it. A hash or retained summary cannot replace the missing observation. If policy withdraws derivative use or requires derivative erasure, generalization does not exempt the fragment.

Expiry cannot resolve a warning, commitment, or unknown effect. Conflicting retention and protected-state duties require an authorized disposition or blocked admission. They never justify prohibited payload retention disguised as accountability.

**Separate mechanical cleanup from authored decisions.** Mechanical reclamation follows already accepted policy and eligibility. Semantic selection, consolidation, cue revision, and retirement remain primary-authored.

This contract covers managed copies of prompt parts and supporting records. It does not establish control over arbitrary recipient copies or provider retention. Do not delete, modify, or revoke user-owned delivered artifacts to meet a persona-state cap. If such artifacts deliberately serve as backing for persona context or supporting records, disclose and account for that reliance and its limits. State which exact historical questions remain answerable within the retention window, rather than promising indefinite historical evidence as a condition of persona continuity.

**Enforce isolation outside editable prose where it is needed.** A file interface or shared host account is not an isolation boundary. A deployment needing cross-persona confidentiality, protected evaluator data, or executable integrity must provide and demonstrate the relevant enforcement outside persona-editable prose. Profile limitations do not waive incurred authority or evidence obligations.

## Evidence boundary

These contracts state required behavior; they do not report that a runtime implements it. [Acceptance](../evaluation/ACCEPTANCE.md) tests mechanics and behavior separately, and the [evaluation method](../evaluation/README.md) governs useful-work comparisons. Historical graph and selector results retain their [original criteria](../evaluation/HISTORICAL-RESULTS.md). The [status ledger](STATUS.md) identifies current implementation and evaluation gaps. Documentation checks do not establish product acceptance.
