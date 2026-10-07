# Observable system contracts

[Implementation guide](README.md) · [Persona core](../design/PERSONA-CORE.md) · [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) · [Requirements](REQUIREMENTS.md) · [Acceptance](../evaluation/ACCEPTANCE.md)

The protected foundation is I01–I21. The persona core, work-and-boundaries chapter, and these contracts are complementary normative views: what the persona means, which constraints hold, and what must cross a reliable handoff. None silently overrides another. A conflict requires an explicit recorded resolution; preserve the conservative authority and evidence boundary meanwhile. The requirement index is traceability, not a shorter substitute for these rules.

These contracts specify observable behavior, not a database layout, programming interface, required file tree, or task-solving sequence. One record can serve several purposes if their meanings remain distinguishable. Persona-owned files are the authoring and retrieval interface; choosing a physical storage backend is separate.

## Recoverable meanings

| Information | Meaning that must remain recoverable |
|---|---|
| Persona | Stable identity, actual creation provenance, accepted current self, authorship policy, relevant lifecycle, and inference configuration. |
| Authored fragment or file | Owner, exact accepted text and revision, attributable authorship or adoption, source restrictions, actual evidence references when supplied, correction and retention disposition. |
| Next-context choice | The primary persona's exact selected revisions, work scope, any explicit lifetime, required accompaniment, and later preservation, replacement, clearing, or invalidation. |
| Actual decision context | Current self, mandatory work and policy state, actual observations, selected full text, previews, omissions, relevant versions, and what reached the provider-facing request. |
| Need and responsibility | Original request, accepted scope and changes, criteria, assumptions, actual offers and acceptances, owners, dependencies, findings, and remaining gaps. |
| Capability and effect | Available operation and its limits, actor, authority, admitted intent, reservation, actual status and output, relevant executable or environment version when genuinely recorded, and uncertain effects. |
| Evidence and release | Exact artifacts and assemblies, criteria, actual reviewer and policy, observed checks, judgments, limitations, current applicability, delivered scope, and any required human acceptance. |
| Resources and recovery | Root allowance, reservations, consumed and uncertain exposure, protected finishing capacity, pending events, cancellation, and stopping or continuation disposition. |

Attribution and integrity are mechanical meanings. The runtime does not invent what a fragment means, which experience it generalizes, why a peer is useful, or whether a result is good. An exact receipt proves its recorded observation, not the truth of every interpretation written about it.

## Persona authorship and files

**Input:** one current primary persona decision, its actual supplied context, the existing exact file revisions, authorship policy, and current authority.

**Accepted result:** the persona can write or revise its own first-person account and ordinary experience, relationship, skill, or tool notes while doing useful work. It can name, move, split, consolidate, correct, or retire files without filling a fixed cognitive form. Current self has one authoritative accepted designation; a display or derived index must not become a competing writer.

**Failure behavior:** stale edits conflict rather than overwrite accepted changes. Dependent multi-file edits, qualification changes, and next-context references commit coherently or leave the previous valid state intact. Exact repetition returns the original disposition. A failed save cannot support a delivered claim that a lesson was remembered. Before accepting a change, check that the resulting mandatory state remains admissible, including current self, exact required qualifications, source ancestry and other protected context. Repeated small revisions must not accept an unusable state merely because the visible prose is short. Independently valid work retains its originally admitted context and current guards; uncommitted prose supplies no authority or received evidence.

**Visible evidence:** actual author, adopted source when relevant, prior and accepted revisions, committed changes, conflict or failure, and the origin of any outside edit. A peer's suggested wording is not already the owner's account. An operator override uses an explicitly authorized and attributed path.

No extra reflection writer, relationship writer, semantic merger, or generic prose generator maintains the persona behind its back. The primary response may learn and act together, but it owes no memory edit or compulsory no-change declaration. No edit means unchanged files, not proof of an internal learning judgment. An explicitly retained learning deferral remains attributable until it is addressed or explicitly dismissed, without scheduling inference by itself.

First-person wording does not make supplied advice firsthand experience. A tentative intention may be retained before an operation completes; a later observed result cannot be backdated. Evidence that an operation failed supports learning about that failure. An uncertain effect establishes uncertainty. Authorship controls apply to effective current identity, including redesignation or an always-loaded substitute. They do not forbid ordinary qualified methods and relationship learning. Mechanical controls cannot promise complete detection of semantic bypass in free prose; that limitation also needs behavioral evaluation.

## Search and exact reading

**Input:** a persona-chosen listing, literal query, supported regular expression, or exact file reference within an authorized notebook scope.

**Accepted result:** bounded results identify the searched corpus, matching mode, exact current revisions, and how to obtain permitted text. Simple file listing, search, grep-like matching, and exact reading suffice for the baseline. The persona may choose query expansion, useful names, and its own index; no taxonomy or universal relevance scorer is required.

**Failure behavior:** no match, unavailable scope, stale reference, unsupported or invalid pattern, incomplete search, exhausted bound, and storage failure remain distinct. A stale result does not silently open newer bytes as the earlier observation. Search does not leak inaccessible titles, snippets, relations, or counts. An index lag has a bounded current-store discovery path or a visible limitation, never an invented exhaustive result.

**Visible evidence:** search scope and completion, returned candidate identities and revisions, actual full or partial reads, and their observation time and provenance. A snippet is not a full read; a full read is not endorsement or persistent selection. Raw host command output remains that command's observation and does not manufacture a trusted notebook receipt.

The runtime faithfully preserves accepted text. It does not replace it with a hidden summary or infer required caveats from semantic similarity. Essential qualifications should normally stay beside the method. When they are separately authored, an explicit required-accompaniment binding preserves the exact complete bundle, including transitive prerequisites and corrections. Ordinary hyperlinks are navigation, not automatic authority or mandatory accompaniment. A missing, revoked, stale, or excessive required part prevents the affected method from being represented as a complete usable bundle. The primary persona may repair it under current authority; the runtime may not silently drop the qualification to fit.

## Primary-persona next-context selection

**Input:** the primary persona's choice of relevant exact fragments for a later ordinary decision, current self, actual work observations, current obligations, source policies, and the complete request allowance.

**Accepted result:** the primary LLM chooses semantic relevance and future attention. Its explicit choice may retain exact optional fragments for that work until replaced, cleared, expired where a lifetime was specified, or invalidated. A choice may name a currently readable exact candidate discovered in a preview without falsely claiming its full text was already read; newly authored accepted text may also be selected without a search ritual. Permitted source evidence and tool help can also be chosen as context, remaining attributed observations or capability guidance rather than automatically becoming persona-authored fragments. The resulting ordinary decision receives actual selected full text with required qualifications.

**Failure behavior:** an unavailable or changed selected revision receives an explicit disposition and cannot silently follow a path to different bytes. Omitted next-context changes preserve an existing valid choice; explicit replacement replaces it; explicit clear removes the optional choice. Preserving a choice neither renews permission or lifetime nor makes an invalid source usable. If an optional selected source or required part becomes stale, withdrawn, or inaccessible, withhold the entire affected optional bundle and record its ineligible disposition without silently clearing the choice. An otherwise lawful fresh decision may receive that safe disposition and repair the choice; it must not claim the withheld text was supplied. Missing mandatory self or work sources still block affected admission. This exception does not permit discarding valid selected text to make an ordinary task decision fit. Later pressure on a previously valid selection uses only the explicitly restricted repair decision below. A failed dependent edit leaves its new selection unaccepted. New work starts with its own mandatory brief and observations; another work's private focus or persistent optional selections do not transfer automatically.

**Visible evidence:** who chose, what exact versions were chosen, selection scope, how that choice was preserved or changed, the actual provider-bound full text and qualifications, previews and omissions, and any mismatch that blocked admission. Inspection must respect access and retention; retain sufficient exact identity without requiring an unnecessary raw prompt or private reasoning archive.

The runtime adds mandatory current authority, cancellations, obligations, blockers, critical observations, and current self. These are protected work and policy state, not an independent semantic memory selector. Search, indexes, optional graph navigation, and optional semantic discovery aids may offer candidates; they cannot independently choose the persona's optional prompt parts, author meaning, or outrank its current choice. Their use still needs actual permission, bounded resources, and attributable observations.

An unexpected reply or failure enters relevant current observations even when the prior choice did not predict it. The persona can then search, read, and choose applicable experience in an ordinary decision. A search hit does not automatically activate a lesson, and an old selection must not suppress a new adverse fact. A permitted same-call authored change is for subsequent context; it cannot rewrite what the current decision previously received.

Validate the whole request, including instructions, current self, observations, tools, selected text, qualifications, media where applicable, and output reserve. Do not silently shorten selected prose to a title, remove its exception, or select a different semantic substitute. Reject a proposed selection that is already inadmissible when committed, preserving the prior accepted state. Separately, new mandatory observations can make a previously valid accepted selection too large for an ordinary decision. That ordinary admission remains blocked; a restricted selection-repair decision may be available under the following contract. Optional discovery previews may be omitted with an honest scope limit; that omission is not evidence that no relevant fragment exists.

### Restricted selection repair after later context growth

The repair is an explicitly labeled primary-persona decision under the same current identity, assigned inference configuration, authority and controlling resources. Its finite attempt allowance is declared before admission; it neither creates extra funding nor appoints an auxiliary selector. The repair context must contain current self, mandatory work and policy state, accepted obligations, cancellations, blockers, consequential observations and evidence, resource facts, and the restricted repair instructions. It may add a bounded, access-filtered inventory of the exact stored selection and mechanical fit diagnostics.

Selected optional bodies and their qualification bundles may be transparently withheld from this repair request. Text or qualifications independently required by the mandatory core remain supplied, even when also referenced by an optional selection; the receipt reflects what was actually supplied rather than calling those bodies withheld. The supplied-context receipt records which eligible exact bodies were withheld, what inventory or previews were supplied instead, why ordinary admission failed, and any incomplete inventory or unavailable entry through a safe disposition. It must neither expose inaccessible identities or content nor claim that a preview is a supplied body or a complete method. Withholding changes no stored choice, source restriction, observation history or accepted responsibility; only an accepted primary repair changes the selection.

Its only permitted activity is narrowing or clearing optional selection, the necessary bounded repair reads described below, or an honest stop. It cannot rewrite current self, edit the meaning of memory, change mandatory state or required qualifications, switch models, publish a deliverable, or perform any substantive task action, including one based on mandatory observations rather than previews. Inventory and previews do not establish the underlying task evidence. Any read to inform repair must itself be permitted, exact, fully qualified and able to fit the repair context; a read that would overflow or omit a required part is unavailable rather than silently shortened. Its actual result must be observed in a later authorized repair decision before a dependent choice, within the same remaining allowance and ordinary observation boundary. Narrowing or clearing must remain possible without reading every withheld body. If the mandatory repair core itself cannot fit, or current authority, funding or the remaining repair allowance cannot support it, block without dispatch.

Recheck source versions, qualifications, permissions, current self, mandatory state and authority when adopting the repair. A change during repair cannot justify following newer bytes, reviving an unavailable source or overlooking a new blocker. After an accepted repair, require a fresh normal admission that supplies the remaining exact selected full text and complete qualifications together with the then-current mandatory state. The repair response cannot perform the resumed task actions itself, and successful selection change does not guarantee that this later admission will fit or be authorized.

An admitted failed, uncertain or no-op repair retains its resource and attempt charges. Restart, repeated diagnostics, a new event or an unchanged choice does not reset the allowance. A subsequent restricted repair may observe its predecessor's actual receipt only within the remaining bound. If repair cannot produce an admissible normal context, retain the exact disposition and stop or block without inventing progress, supplied text, or additional authority.

## Decision authority and freshness

One persona has one current primary decision authority at a time; independent personas and isolated jobs can proceed concurrently. The admitted decision binds actual identity, work, relevant versions, observations, inference configuration, authority, and resource exposure. A model change does not change identity or expand permission.

Recheck consequential current state at adoption, not only when the request was assembled. Accepted current-self change fences all fresh operations from the originating response, including reads and waits, until a fresh decision receives the new state. Revocation, cancellation, changed scope, or stale ownership fences affected actions. An exact unchanged and still-permitted self designation is idempotent and does not fence otherwise valid work. A rejected identity proposal leaves the previous accepted state, subject to all current guards. Late results remain evidence and accounting, not restored authority.

Included, received by a provider, acknowledged, understood, agreed, and used are different claims. Notification acknowledgment must bind the exact inputs actually supplied to that recipient and decision. A historical cursor cannot prove observation of an older newly readable message. Recheck actual notification identities and permission at mutation; missing inclusion is not repaired with a fabricated receipt. Fresh observation requires its own current authority and funding.

## Work and accepted responsibility

Need intake preserves the exact original request, source, constraints, permitted assumptions, accepted changes, criteria, and closure terms. Interpretation may be persona-authored, but cannot silently reduce the need. Required outcomes show accepted responsibility or a visible gap.

Membership, a contribution offer, commitment acceptance, and actual contribution remain distinct. Only real endorsements bind the named participant and terms. A handoff transfers responsibility only after the receiver accepts, or an authorized disposition explicitly replaces it. Decline and nonresponse create no substitute acceptance, replacement persona, punitive reputation, or dependency on a person who never agreed.

Persona-owned organization uses discovery, proposals, communication, accepted commitments, and evidence-led revision. No task keyword, fixed profession roster, compulsory coordinator, birth rule, or hidden domain pipeline chooses the solution. A human-imposed constraint or an explicitly adopted reusable method can legitimately guide work. Authorized evaluators need evidence of the actual orchestration policy, not just a convincing unscripted transcript.

Where birth is enabled, one creation preserves truthful provenance, restricted seed and invitation preview, population and initialization limits, and bounded orientation. Creation does not grant money, permissions, experience, membership, expertise, or commitment. Duplicate and concurrent requests conserve the controlling limits; declined participation does not erase spent resources. Existing personas and simple work need no creation ritual.

## Capabilities and actions

A skill file is a reusable authored method. A tool note describes an operation and its observed limits. Neither installs a tool, proves competence, grants credentials, or executes a helper. A known executable version supports a claim only if that version was genuinely bound to the observed operation; a filename or subsequently edited helper is insufficient.

An admitted action identifies actor, causal work, stable request, exact relevant inputs, intended effect, capability, current authority, resources, and observation or cancellation terms. Durable intent precedes dispatch. Repeat the same accepted request without duplicating its effect; changed content under the same identity conflicts.

A running operation does not satisfy a dependent action. Suppress the unobserved remainder of its decision; a fresh observation-bound decision uses the actual result. Preserve proposed, admitted, running, failed, completed, stopping, canceled to the observed extent, and effect-unknown states. Reconcile uncertain outside effects before repeating them. Completed execution establishes neither correctness nor delivery.

Available operations must be usable from their actual loaded guidance, with clear identity, version, replacement, and effect meanings. Current successful receipts should expose appropriate inspection affordances without a syntax-discovery-only decision. Compaction must not hide control of unresolved jobs, while old terminal history need not keep every operation permanently loaded. Projection is not permission, deletion, or evidence that an artifact was inspected.

## Authority, resources, and stopping

Every grant is scoped, revocable, and no broader than its parent. Reserve before spending or dispatch; initialization, tools, descendants, inference, unsuccessful attempts, maintenance, auxiliary discovery, review, and finishing all count toward the same controlling allowance. Unknown usage remains exposed, never assumed free. A genuinely closed local failed decision and its conservative metering are separate facts; uncertainty cannot fund a retry.

Protect agreed review, repair, and closeout capacity from ordinary exploration unless explicitly reallocated. Optional between-task exploration needs a real authorized trigger, finite episode and recurrence bounds, expiry, and stopping terms. A new input, restart, changed cursor, repeated narrative, or fresh filename does not reset a recovery or exploration allowance. Local preparation rejected before admission is distinct from an admitted failed or uncertain call. No idle reflection loop is created by a fragment, deferral, search miss, or empty selection.

A stop identifies completion, partial delivery, voluntary yield, a real outside dependency, an accepted peer contribution, an authorized scheduled continuation, or a resource or infrastructure block. Remaining obligations and adverse findings stay visible. A valid wait need not be turned into endless retries; a wished-for event is not a scheduled trigger. Missing information blocks only dependent claims and work. Permitted conditional progress remains possible without pretending an assumption is verified.

## Review and release

An ordinary self-check or peer comment can be an attributable assessment without a formal review commitment. A review required by the adopted acceptance policy binds exact scope, criteria, inputs and assumptions, an actual accepted reviewer, applicable funding and independence policy, observations, explained judgment, findings, and limitations. An informal assessment does not silently satisfy that formal requirement. Command counts and successful exits do not determine a verdict. Text may receive a reasoned review without an invented command; technical claims need the observations appropriate to those claims. A different persona is not automatically qualified or independent.

A citation snapshot records the exact stage and content genuinely captured. Recording-time identity does not prove earlier inclusion, attention, or understanding. A changed receipt, artifact, assumption, criterion, or relevant dependency changes current applicability without rewriting the original verdict. Missing snapshot evidence stays missing; never retrofit an old assessment with a newly observed result.

Release binds one coherent reviewed state, legitimate blocker dispositions, exact delivered scope, and current authority. Update-before-release blocks stale acceptance; release-before-update preserves acceptance only for that historical state. An empty optional citation list creates neither automatic review nor release. An unresolved mandatory finding, missing required output, or unavailable recipient access prevents the affected full-delivery claim. Partial results retain their gaps. Digital delivery does not authorize construction, publication, spending, or another outside effect.

## Recovery, privacy, and retention

Restart preserves accepted text, selections, obligations, pending effects, reservations, unknown exposure, cancellation, unresolved findings, and undelivered events. Accepted state and its required notification recover together. Repeated delivery is recognizable; waiting is safe whether the awaited event arrives before or after registration. Import or rollback creates neither a new founder, new money, successful effect, nor cross-host activation authority.

Every read and derivative follows source restrictions: search, indexes, snippets, summaries, self-prose, methods, relationships, selections, caches, exports, errors, and backups. A shortened or generalized private lesson is not declassified. Withdrawal prevents new affected use and disclosure; a call already exposed to content cannot erase its lineage by clearing context. Preserve actual or uncertain effects and use a fresh permitted context or honest block where needed. Do not promise to retrieve bytes already disclosed or undo an unobservable outside effect.

Correction and retirement preserve minimal historical accountability under the deployment's retention rules, while making stale guidance ineligible as current instruction. Filename reuse, links, old selections, or index entries must not resurrect retired or erased material. Deletion limits for outside copies stay explicit.

A file interface or shared host account is not an isolation boundary. A deployment needing cross-persona confidentiality, protected evaluator data, or executable integrity must provide and demonstrate the relevant enforcement outside persona-editable prose. Profile limitations do not waive incurred authority or evidence obligations.

## Evidence boundary

These are obligations, not a report that the runtime implements them. [Acceptance](../evaluation/ACCEPTANCE.md) tests mechanics and behavior separately; the [evaluation method](../evaluation/README.md) governs useful-work comparisons. Historical graph and selector results retain their [original criteria](../evaluation/HISTORICAL-RESULTS.md). The [status ledger](STATUS.md) identifies the current implementation and evaluation gaps without treating documentation checks as product acceptance.
