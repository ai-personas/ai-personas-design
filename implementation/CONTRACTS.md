# Observable system contracts

[Implementation guide](README.md) · [Persona core](../design/PERSONA-CORE.md) · [Work and boundaries](../design/WORK-AND-BOUNDARIES.md) · [Requirements](REQUIREMENTS.md) · [Acceptance](../evaluation/ACCEPTANCE.md)

These contracts describe behavior that people and connected components must be able to observe. They are design requirements, not implementation code, a database layout, a programming interface, a required file tree, or a prescribed sequence for solving tasks.

The [human-user requirements](../USER-REQUIREMENTS.md) govern these contracts and the I01–I21 foundation. UR-050 assigns approaches and cooperation to persona judgment; UR-052 removes application limits and safety gates. The persona core explains what the persona means; the work-and-boundaries chapter explains work and its actual outcomes; these contracts explain what must cross a reliable handoff. Resolve contradictions under the [document authority order](../design/README.md#authority-within-the-repository). Earlier restrictive contracts remain at their [historical revision](https://github.com/ai-personas/ai-personas-design/blob/662537d664c809e88376d07bbdd11ae40269f913/implementation/CONTRACTS.md), with their original criteria and outcomes; no prior pass establishes these current contracts. The requirement index traces the rules rather than replacing their detailed meaning.

The persona includes its characteristic context, LLM invocation and reasoning, actual behavior, and coherently adopted self-revision. The LLM provides the capacity to reason. Persona-defining fragments provide authored prompt parts that express character; they are not a memory product attached to an otherwise complete agent.

Supporting assets have a different purpose. Plain domain knowledge, generic technical procedures, tools, skills, code, data, evidence, and operational records remain assets even when the persona authors them or writes them in the first person. They may provide operative instructions for work, but do not thereby become characteristic fragments, a current human request, or another participant’s acceptance. A fragment can refer to an exact asset. Quoting an asset or evidence does not change its role or justify copying technical bodies into persona prose.

A passage or record can serve more than one purpose if those meanings remain distinguishable. No compulsory categories or folders follow. Ordinary files and authored search cues form the compact, evolving network of prompt parts; the physical storage backend is a separate choice.

## Recoverable meanings

The system must preserve enough information to establish who chose or did something, which exact material they used, what was accepted, and what remains unresolved. The table describes meanings that must remain recoverable, not a compulsory record format.

| Information | Meaning that must remain recoverable |
|---|---|
| Persona continuity | Stable identity and actual creation provenance across characteristic context, invocation, action, and self-revision; one accepted characteristic-profile and own-voice account; separately scoped modeled affect state; actual authorship; relevant lifecycle; and inference configuration. No single record constitutes the operating persona. |
| Persona-defining fragment or file | Its own-voice prompt meaning and owner; exact accepted text and revision; attributable authorship or adoption; optional associative cues kept distinct from exact evidence references and required qualifications; source provenance; explicitly adopted applicability warnings; and correction and retention disposition. |
| Supporting resource | Actual source and author, purpose, exact retained revision or snapshot, relevant live identity and freshness, qualifications, and lifecycle. This applies to domain knowledge, generic technical procedures, histories, tool-use records, tool definitions, reusable skills, scripts, code, data, and attributable derivatives. Storage does not establish authorship, current authority, or executable availability. |
| Next-context choice | The primary persona's exact selected fragment and supporting-resource revisions or ranges; persona-chosen discovery or exact-material requests; work scope; any lifetime; required accompaniment; and later preservation, replacement, clearing, or invalidation. |
| Actual decision context | Current character, relevant modeled affect state, selected persona-defining full text, mandatory maintenance input, current work state, actual observations and supporting resources, necessary bootstrap and requested candidate metadata, operative tool guidance and exposed callable definitions, previews, omissions, and relevant versions. Also recover provider expansion, retained context, and what reached each provider-facing attempt. |
| Invocation maintenance | The persona's explicit disposition for both fragments and supporting resources: a proposed change with its intended storage target and useful discovery cues, reasoned no_change, or an identified blocked/deferred outcome. Also recover response validity, actual persistence, and dependent work held or admitted. One concise outcome may cover both scopes. Failed calls preserve host status without invented persona outcomes. |
| Need and responsibility | Original request, accepted scope and changes, criteria, assumptions, actual offers and acceptances, owners, dependencies, findings, and remaining gaps. |
| Capability and effect | Available operation and actual host/provider constraints; current observable interface or connection identity; actor and decision identity; admitted intent; reservation; relevant exact client/runner and input bindings; actual status and output; genuinely recorded executable/environment versions or explicit unknowns; and uncertain effects. |
| Evidence and release | Exact artifacts and assemblies, accepted criteria, actual reviewer, observed checks, judgments, limitations, current applicability, delivered scope, and any required human acceptance. |
| Resources and recovery | Actual calls, navigation, supplied context, managed storage including temporary copies, retention decisions, known and unknown usage, pending events and effects, cancellation, and authored stopping or continuation. Historical allocations remain records, with no application quota or reserved-capacity prerequisite. |

**What records establish.** Attribution and integrity are mechanical meanings: they establish origins and exact recorded content. The runtime does not invent what a fragment contributes to the persona, which experience informed it, why a peer is useful, or whether a result is good. An exact receipt proves the observation it records, not every interpretation written about it. Persistent records support accountability; persistence does not make them persona-defining fragments or demonstrate characteristic behavior.

**Retention and availability.** There is no application archive or history quota. Preserve exact original requests, accepted changes, authoritative receipts and unresolved effects with their actual identities. Personas may organize, retire or explicitly delete material. Deleting a body cannot establish that an obligation was fulfilled, a warning resolved or an uncertain effect never occurred. Useful compactness concerns organization and selected context, not a compulsory reduction of retained history.

Record actual deletion, unavailable evidence and storage failures honestly. Preserve remaining attribution without claiming that a digest restores missing bytes or that an unobserved save succeeded. Physical storage is not unlimited; a real failure remains an observed outcome rather than a reason to add an application quota. Never rewrite an original or replay an old request because its receipt is missing.

## Every persona invocation

Every LLM call that exercises the persona's judgment must account for its work, maintenance, and next context. A short answer can meet this duty concisely. The duty does not require an edit, a search, or another call.

A persona invocation is any LLM call that exercises the persona's judgment, own-voice authorship, selection, communication, coordination, or reflection through its actual characteristic context. Its name, adapter, brevity, or tool-shaped interface does not exempt it. Every attempted call has attributable maintenance and next-context decision input, plus an honest pending or terminal status. Only a complete valid response may be adopted. It must contain the actual work disposition, explicit maintenance outcome, and explicit next-context disposition for both fragments and supporting resources.

This is a behavioral contract, not a required serialized envelope or metadata format for fragment files. Context alone does not prove consistent persona expression. Outcomes also depend on the model's learned capabilities and priors, inference configuration and sampling, the task, tools, and observations.

**Observable boundary.** Coverage concerns the application’s persona invocation and its provider-facing attempts. It does not extend to hidden provider decoding, internal routing or other steps the host cannot inspect. Direct model-provider interfaces perform persona inference under UR-051. If a provider-managed loop makes persona choices, the actual work, maintenance, next-context and observation boundaries of those choices must be inspectable before claiming that it meets this contract. Hidden operations remain unverified, not silently exempt.

**Purpose and current work.** Fresh persona decisions use ordinary work, maintenance and next-context responsibilities, including discovery, preparation and recovery. A task purpose does not create a restricted mode or a character-authoring permission gate. Preserve the current request and accepted commitments while allowing the persona to choose useful tools, communication, maintenance and continuation.

Initialization starts from the attributed seed and accepts coherent initial character before later work uses it. That ordering identifies which character informed a decision; it imposes no initialization allowance or separate repair workflow. Historical mode declarations retain their actual meaning without restricting a new ordinary decision.

Provider structure can assist decoding of the closed initial-character contract.
It must preserve persona authorship, complete native validation, exact references
and the fresh-decision handover. Requiring explicit nulls or empty defaulted
collections changes transport spelling, not accepted character or task behavior.
A completed character unit waiting for a quiescent handover must not prevent
independent eligible calls from progressing while the original pending calls
remain. Once those calls settle, drain successors and perform the handover;
continuous refilling must not starve it.

Ordinary decisions may use non-strict provider structure derived from the same
applicable native contract. Preserve optional fields, tagged alternatives,
constraints and arbitrary capability-input values. Presentation annotations may
be omitted from the transport copy when the complete supplied contract retains
them. This assistance does not authorize actions, repair malformed responses or
replace complete native validation. Account for the actual selected output
schema in every request, including initialization; encoded byte counts do not
establish billed token usage or task quality.

A compact presentation may express a constraint once when its syntax already
entails it: an exact string literal or a union of string literals needs no
additional string-type annotation. Preserve descriptions, defaults and every
independent constraint at their original scope. Unknown constructs must retain
the full schema rather than silently weakening the supplied contract.

One current primary decision identifies the persona across adapters and nested calls. Concurrent stale decisions cannot both become its accepted current state. Proposals and adoption retain exact identity, version and persistence checks. This establishes coherent authorship and ordering, not an access or self-authorship lock.

**Input.** Each request supplies the information needed for the current decision:

- Current work and need; actual current character, relevant modeled state, and selected trait-conditioned fragments. Initial generation uses the honestly attributed seed instead of an existing character account.
- Needed supporting assets and actual observations; relevant exact revisions; unresolved consequential corrections or adopted deferrals; actual missing information and observed failures.
- Responsibility to consider useful fragment creation, updating, organization and deletion, and supporting-resource creation, storage, refinement, organization and deletion.
- Responsibility to author an appropriate next-context disposition for both fragments and supporting resources, using persona-chosen discovery, exact reading or selection when useful.
- Usable authoring, host-command and discovery interfaces, together with actual usage and known provider or host conditions.

Initialization does not require existing fragments. No call requires an entire archive or catalogue. Account for the complete supplied request, including maintenance instructions and output settings, without an application context or response ceiling.

**Character in actual decisions.** All discretionary persona judgment uses this characteristic context, including work, human-facing communication, peer collaboration, and navigation. Received exchanges and task consequences can inform later primary-authored fragment and relationship changes, or an effective-character proposal. They do not trigger automatic personality updates.

Keep actual observation, interpretation, accepted revision, later supplied context, and observed consequence distinguishable as evidence. A calendar tick, dormant interval, praise, or fragment count supplies no missing experience and proves no improvement.

**Accepted response.** A response must explicitly cover all three responsibilities:

| Responsibility | Required disposition |
|---|---|
| Work | The substantive result, action or context proposal, refusal, question, or stopping disposition appropriate to the call. |
| Maintenance of fragments and supporting resources | Attributable proposed change; no_change with a concise reason; or identified blocked or deferred work. |
| Next context for fragments and supporting resources | An appropriate preserve, clear/no optional need, discovery/read with explicit retained or cleared state, or an honest blocked/stop outcome under the selection contract. |

A maintenance proposal may cover creation, storage, refinement, editing, splitting, consolidation, movement, retirement, or explicit deletion. One short shared outcome can cover both maintenance scopes when unambiguous. Mixed outcomes must not present a remaining correction as complete. No_change must be persona-authored, not a host-inserted placeholder; it proves neither hidden reasoning nor future benefit.

Maintenance no_change does not by itself choose next context. Shared prose may cover maintenance and selection only when both meanings are explicit. Neither consideration mandates a write, an extra call, or future continuation.

**Authoring and organization proposals.** A proposal identifies its intended file/path or supported storage reference, affected exact resource and base revision where applicable, proposed content or exact content reference, and useful literal/regex discovery cues when warranted. Cues remain attributable data; their presence does not run a command or follow a link. No fixed folder taxonomy or forced outgoing links follow. Large code, data, or retained observations need not be repeated inline when an exact reference suffices.

Naming a target is a proposal, not an accepted write, installation or observed effect. Before native adoption, check the actual target and base revision, coherent dependencies and persistence outcome. Default host access and tool installation require no separate grant; a host filesystem write retains its observed effect rather than becoming a native asset-adoption receipt.

**Factual host recording.** Deterministic capture of actual received messages, history, tool outputs and receipts remains host work. The model may propose attributed extraction, summary or organization of records. It cannot fabricate an event, alter an authoritative original or turn old instructions into a current request. A discretionary resource-maintenance no_change does not suppress factual recording. Imported tools and skills retain their actual author; storing their bytes is separate from installing or executing them.

**Blocked or deferred maintenance.** Preserve the reason, affected fragment, supporting resource or concern, missing prerequisite and consequences for dependent work. Identify an accepted owner or ownership gap and any actual event or continuation opportunity. The persona chooses how to revisit it; no finite episode allowance, invented deadline or compulsory form follows.

If no continuation has been accepted, expose that gap. Missing observations or a persistence outage must not become a promise of automatic retry. A deferral remains attributable until addressed, dismissed, transferred with acceptance or ended with an honest unresolved disposition. A persona-chosen expiry does not establish evaluation or repair. Host bookkeeping invents no persona judgment or future wake. Historical allowance exhaustion is not a current application gate.

**Continuing applicability.** Ending a correction effort does not resolve a separately adopted warning. Preserve its exact affected revisions or identified uses, actual author, basis and qualifications until an attributable resolution. A warning informs persona judgment without becoming an application access or repair gate; no universal truth engine decides which interpretation the persona must adopt.

A proposed or failed patch does not create an accepted warning automatically. Record the actual persistence outcome of each independent change. If saving a warning fails or is unknown, preserve that uncertainty; do not claim that the warning exists in accepted state or that the guidance was shown to be correct.

Unavailable warning text or evidence remains unavailable. Do not invent its bytes, imply it was supplied or turn an unassessed peer contradiction into an accepted persona judgment. Required qualifications preserve the meaning of material actually supplied; historical source restrictions and character-authoring limits are not current access gates.

**Invalid or absent response.** Missing or malformed maintenance or next-context intent, an incomplete stream, structurally uninterpretable maintenance operations, or any other invalid response prevents new adoption and dispatch of all proposed substantive actions from that response. This includes communications, reads, and selection changes. Do not salvage a plausible tool call or reply from an invalid prefix.

**Response identity.** Make the current admission's exact invocation identity and
response epoch explicit in its supplied control context, with their wire types
in the response schema. Keep them distinct from work and mandate revisions.
Apply the exact binding to initialization and later decisions, including a fresh
ordinary decision after rejection and any historical repair rendering. Preserve
the original received bytes and independently check parsing, response identity
and current state before adoption; supplied identity guides authorship without
proving validity or repairing a mismatch. Count its complete representation in
actual input size, without treating changing admission identifiers as
fixed-contract growth. A generic public wire schema has no particular admission
to bind.

**Profile wire shape.** Describe the named OCEAN and VAD dimensions required by
the active parser in the supplied response schema, including each required field,
its value type and whether additional keys are accepted. An internal map must not
make the offered schema appear open when validation requires exact names. Keep
baseline and current-affect VAD shapes consistent. This describes the existing
wire contract; it neither fixes the authored descriptions nor limits characteristic
nuance or text length.

**Work evidence wire shape.** Each work disposition's evidence array describes
the parser's unique, nonempty identifier rule in its supplied schema. An empty
array is valid. Do not introduce item-count or text-size ceilings, reorder the
authored list, or silently deduplicate rejected output. Structural validity does
not establish evidence availability, relevance or support for the work judgment.

Provider refusal, transport failure, timeout, and cancellation retain their actual status and exposure. They are not persona-authored no_change outcomes. A valid persona-authored refusal still includes maintenance and next-context dispositions for ordinary work; the host fabricates neither for a provider refusal.

After rejection, prior accepted selection remains stored only under its existing validity and recovery rules. This is not an authored preserve or successful consideration. Already admitted effects remain real. Missing intent creates no automatic paid repair, retry, or new allowance. Host status reporting may disclose the actual failure without presenting rejected output as an accepted persona response.

The ordinary launcher should explain a retained provider rejection using its
actual status and available credential-redacted provider explanation. Bind that
display to the exact failed attempt and distinguish it from accepted persona
output. Equivalent explanations may be grouped without hiding which calls they
describe. Viewing a failure changes neither configuration nor retry permission;
raw response bodies and private continuation material remain separate.

Explain structural rejection using the current schema and the actual affected
section. Identify missing required members and definite nested type or enum
mismatches when known, including when a tagged decoder reports only its enclosing
operation. Known field paths and array positions can locate the problem without
repeating arbitrary authored text or dynamic map keys. Leave opaque payloads
opaque and unknown variants unresolved. Diagnostic hints describe the rejected
shape; they do not infer intent, fill omitted fields, alter the original bytes,
relax validation or supply a replacement persona decision.

For duplicate JSON members, retain both byte locations and identify the affected
known field and array position through declared schema paths. A duplicate can
precede its object's tag or closing delimiter; explaining its location must not
depend on choosing the first or last duplicate value as authoritative. Stop at
the enclosing known path for unknown members or opaque payloads, and keep dynamic
map keys out of the explanation. The persona authors any correction through an
eligible fresh decision; no partial response is adopted.

For a repeated operation identifier, identify the first and conflicting
operation positions and their `id` fields. Keep authored identifier values and
operation payloads out of the diagnostic. Reject the complete response without
renaming operations or rewriting dependent references on the persona's behalf.

If an absent tag leaves the variant unresolved, identify missing schema-owned
members required by every alternative. Do not guess a variant or present its
particular fields as universally required. Preserve whole-response rejection.
For an unrecognized tag, list the schema-declared values at its known field
when every applicable alternative has an explicit tag. Do not claim an
exhaustive list when an alternative is broad or opaque, echo the rejected value,
or choose a replacement on the persona's behalf.

When a proposed creation conflicts with an existing immutable work record,
identify the record type and the supplied identity that caused the conflict.
Preserve the existing record and whole-response rejection. The diagnostic does
not choose a new identity, replace the record or make a historical judgment
current under a later arrangement.

Retain complete failure provenance with the rejection and its receipt in one
transaction. Reference the exact admitted request and terminal; retain newly
consulted sources and policies without duplicate components or a byte quota.
Unavailable lineage remains explicitly unknown because evidence is missing,
never because an old allowance was exceeded. Serialize and account for the
complete retained record when persisting it; avoid redundant size probes.
Persistence failure rolls back rejection and its receipt together. Historical
unknown provenance is not reconstructed or reclassified by this change.

Validate request-only tool inputs against the exact admitted definition before
consulting mutable work or asset state. An input-shape error or invalid local save
dependency should retain the admitted request's lineage when that is all the
check used. Apply this distinction to host commands, HTTP retrieval, computation
and native work commands. Current implementation bindings, host environment and
asset materialization remain separate checks with their actual provenance.
Do not imply that preflight resolves the availability or every semantic property
of a retained asset reference; those checks may require staging.
Establish the character-adoption fence before checking unrelated inputs that
the fence excludes. Early validation accepts no action and performs no tool
execution.

When a host command consumes an exact supporting-asset reference as standard
input, resolve its actual representation and range. Use the ordinary qualified
file resolver for complete UTF-8 text, once-decoded JSON strings and measured
UTF-8 byte ranges. Supporting assets may also retain arbitrary original bytes.
Their explicit byte-metadata representation supplies exact length and SHA-256
without decoding or exposing the body. When used as command stdin, that reference
materializes the complete original bytes rather than the metadata descriptor.
A retained command-field reference must not require copying
the script through a new model response or substituting the whole result
document. Bind the source revision, representation, range and qualification
closure, and retain the byte count and digest of the actual stdin bytes. Recheck
those bytes and bindings before dispatch. This materialization neither supplies
model context nor proves that the process consumed the input or succeeded.

When recovery explains a rejection under an earlier application quota, identify
the recorded limit and measurements as historical. They do not require a smaller
current context, a replenished allowance or renewed access permission. New
diagnostics distinguish exact source-lineage checks from access-policy gates,
which are disabled under unrestricted execution. Preserve earlier observation
bodies and actual provider or host failures without rewriting their outcomes.
Diagnostic supply does not resume a stopped persona or establish work completion.

An earlier accepted continuation can remain usable under the same live mandate. Within the continuing session, the host may retire a definitively rejected, complete local invocation and supply its actual failure to a fresh primary decision. This preserves the existing continuation rather than deriving permission from invalid output. Keep the rejected response and its charges; do not replay its proposed actions, repair its bytes, erase recorded usage, revive an authored stop, reuse a consumed timed opportunity, or treat cancellation or an uncertain transport as a completed rejection. Recheck current work, actor, context, scheduling and actual execution state before the fresh admission; no resource allowance is replenished or required.

Report a session's final stop separately from driver failures recorded during it.
A failed attempt followed by continued work remains a real historical failure;
its presence does not replace the final scheduling outcome or establish a current
participant hold. Preserve both facts in live and saved-session displays. Current
participant state and the quality of the task result remain separate questions.

**Ordinary work controls.** The end-user launcher exposes pause and cancellation
during active work, and a separate work-wide resume after execution settles.
Record a stop atomically against the current work without waiting for the active
execution owner to finish. Preserve actual terminal observations, earlier output
and usage; a stop request is neither completed work nor proof of remote termination.
Persist each user control's exact identity and contents before submission. A
repeated identity returns its historical result without stopping or resuming a
later state again. Retain an unapplied stop when the current phase no longer
allows it, so a delayed retry cannot stop later resumed work. Work resumption
binds the inspected state and commits its
receipt with the phase change; it starts no inference, recovers no unknown effect
and preserves each participant's continuation choice. Pending feedback or question
input must not prevent the requester from stopping active work.
An invitee whose initial opportunity ended before an ordinary response must
remain explicitly resumable. Such resumption permits consideration of the
invitation and does not record acceptance on the invitee's behalf.

An explicit operator resume can separately permit a fresh decision after a
definite rejection. The ordinary participant controls should expose a complete
response rejected before adoption and a recorded rejection before provider
launch, while keeping unknown remote outcomes unresolved. Bind the choice to
the inspected work state, failed invocation and exact terminal evidence. Commit
the resumption, retained failure for the next decision and keyed receipt
together; preserve prior usage and keep unsettled usage unknown. Repeating that
request returns its historical receipt without resuming again, even if a later
call has failed or the persona has since stopped. The resume itself starts no
inference, adopts no rejected action or continuation, and lifts no separate
work-wide or identity pause.

**Communication and diagnostic inspection.** Ordinary chat and work delivery withhold the call's persona-authored preview, commentary, and reply until the complete work, maintenance, and next-context response has been validated. While the call is pending, those channels may show truthful mechanical host status.

Label any operator-visible authored draft text, including commentary, as unvalidated. A draft is not delivered persona communication, an accepted decision, completion or proof of its claims. Its exposure retains its actual audience and provenance. Concise reasoning summaries and source/result evidence suffice; this contract does not require publishing raw private reasoning or adding a live-preview feature.

Whole-response validation does not establish successful persistence. A claim that a save succeeded still depends on actual acceptance, and delivery retains its other authority and dependency checks.

After adoption, the ordinary launcher should show the persona's latest accepted
work account even when it chose not to send a reply. Preserve its authored reason,
persona and producing invocation, and identify an earlier or unavailable task
version. Present this as the persona's account based on its supplied information;
execution receipts, current task state and recorded delivery remain separately
identifiable. Displaying the account creates no message, endorsement or completion
record and requires no additional model call.

When a rejected response has a known structural mismatch, diagnostic hints
should identify the affected schema-owned path, including nested objects and
array positions. A closed nested object with unknown members should identify
its own allowed fields, rather than implying that only the enclosing response
section is malformed. Keep authored unknown names, dynamic map keys and opaque
payloads out of these hints. Diagnostics explain the rejection; they do not
repair, adopt or execute any part of the response.

For responsibility bindings, distinguish an explicit supplied-terms revision
mismatch from an offer addressed to a different persona. Identify the affected
field and its existing binding options without echoing authored values or
repairing the response. The same current-offer and exact-terms checks still apply.

**Readable response contracts.** A compact presentation of the generated schema
should place a variant's fixed `kind` tag before its payload fields and distinguish
an outer operation tag from nested command tags. Preserve all fields, requiredness,
descriptions and constraints. Display order adds no JSON member-order requirement
and does not permit the host to infer or insert a missing operation tag.

**Independent host duties.** Recording observed receipts, enforcing cancellation, fencing stale authority, accounting, and shutdown need neither another persona call nor a valid maintenance outcome. Already admitted effects remain real and must be reconciled. These duties cannot introduce a new substantive persona action, infer a new lesson, or make missing output valid.

**Visible evidence.** Identify the logical invocation and provider attempts, actual maintenance and next-context input, complete response or failure status, any persona-authored outcome, validation disposition and later save or conflict receipts. A provider invocation, a host command that inspects source and execution of the inspected feature are distinct facts. Successful source inspection is real execution but does not establish product behavior. Process exit zero does not prove that every subcommand succeeded, so preserve stderr, partial results and uncertainty. No raw private-reasoning archive or fixed reporting form is required.

Bind displayed calls and recovery holds to their actual persona and work.
Participation status belongs to the work being inspected: a stopped contribution
does not acquire pending calls because the same persona starts another task.
Show a persona-wide execution dependency on other work separately, preserving
its effect on availability without implying resumption or failure in this work.

### Coverage and call boundaries

The same contract follows persona judgment wherever it occurs. Renaming a call as a helper, repair, or tool does not remove its duties. Deterministic host work and genuinely isolated non-persona computation have different roles, as shown below.

| Call or operation | Required treatment |
|---|---|
| Character initialization and orientation | The initial LLM call receives the attributed trait seed and authoring responsibility without an application allowance. Its complete response proposes initial own-voice fragments and a coherent account, with maintenance and next-context dispositions. Record seed, candidate, inference configuration and acceptance or failure separately. Later primary decisions receive the accepted starting revision. Imported/operator-supplied material keeps its alternative origin and cannot stand in for initial LLM authorship. |
| Discovery, query formation, retrieval-only selection, and request preparation | Any persona judgment call follows the ordinary contract, even when its result is a search or context choice. A search result is not an accepted fragment or asset revision. Host-only exact assembly is not model judgment. |
| Task work, tool-result interpretation, communication, collaboration, and coordination | Each persona’s call includes its own maintenance and next-context duties. A coordinator, peer or wrapper cannot supply the owner’s missing outcome. Actual actions retain their separate identity, dependencies and observations. |
| Reflection, conflict repair, output repair, and reorganization | Each is an ordinary persona invocation when it uses persona judgment. Its outcome does not require another reflection call or a fixed repair allowance. |
| Historical restricted selection repair | Retain original inputs, mode, charges and outcomes as history. A fresh decision uses ordinary work and maintenance; no restricted repair phase is prescribed. |
| Capability or supplementary model subcall | Persona judgment, fragment authorship, next-context selection or action choice remains a persona invocation regardless of label. Isolated non-persona computation may return attributed candidate information without persona maintenance. Its result does not adopt character or choose the primary’s actions. Dependent work receives the actual result in a fresh decision. |
| Provider transport retry | Retain original logical invocation identity and distinct attempt evidence. Adopt at most one complete response for that invocation; do not merge a conflicting later response. Re-prompting to interpret failure is a new ordinary persona decision, without an application attempt quota or fabricated output. |
| Host cancellation, accounting or exact receipt ingestion | Deterministic host work is not a persona LLM call. If handling it invokes persona judgment, that call follows the ordinary contract. |

Deployed entry points and provider attempts must be inspectable enough to establish the actual coverage claimed. A hidden summary writer, persona-capable tool wrapper, or unrecorded retry is not an exception. Auxiliary models cannot silently become the persona's author or final selector.

### Complete response, persistence, and dependent work

A valid proposal is not yet an accepted operation, and an accepted intent is not an observed external result. The system must keep these stages distinct so that a failed save or uncertain action cannot be reported as completed work.

**Two acceptance checks.** First establish that the complete work-and-maintenance response is valid before adopting its proposals. Then bind each coherent operation to current identity, exact read and base revisions, accepted work, dependencies, cancellation and actual persistence or execution state. These consistency checks impose no application quota, source policy or approval gate. A structurally valid edit can still fail to persist; do not relabel it as a malformed response or completed update.

**Dependent work.** Related fragment or supporting-asset changes, qualification updates, context references, and admitted action intents need one coherent accepted disposition. A failed prerequisite holds its dependent work.

External effects are not atomic with local edits. Durable accepted intent must precede external dispatch, and each actual result needs its own receipt. A fragment may express an intention based on available evidence; it cannot claim an unobserved result. Restart preserves accepted intents and unknown effects. A later maintenance failure does not authorize replay of an already dispatched action.

**Independent work after a failed change.** A later stale revision, persistence failure, or definite no-commit disposition of a character proposal does not automatically invalidate independent work from an otherwise valid response. Independence must be explicit and supported by all of the following:

- The work needs neither the failed edit nor an unavailable result.
- Its relevant supplied information and exact source bindings remain current.
- Its current identity, accepted work, cancellation and actual execution state remain consistent.
- No unresolved-character-adoption, pending-action, accepted-character-change, or other fresh-decision barrier applies.

Missing dependency evidence is not evidence of independence. Hold uncertain cases for a fresh decision based on actual observations. Keep the actual disposition visible, and never deliver an account saying that an uncommitted save succeeded.

**Respect the actual atomic unit.** Independence does not authorize partial commit of a failed coherent adoption. An implementation that adopts the whole response as one unit commits none of its proposed operations when that adoption fails; subsequent persona work requires a fresh decision. An implementation supporting separate independent acceptance must establish each unit's complete validity, exact dependencies and coherent disposition. Previously accepted work and dispatched effects retain their own outcomes when a later operation fails. Neither path may silently turn a rejected proposal into accepted work.

**Character changes are resolved first.** If a response requests adoption of an effective-character change, resolve that request before adopting or dispatching any other fresh persona operation from the same response. Action-list order and claimed independence cannot bypass this rule.

The necessary character-proposal validation and disposition or commit may proceed as one coherent atomic unit. That unit may include the primary's exact necessary current-character account bindings and expressly proposed reductions or clearing of already accepted optional selections needed for the transition. Before acceptance, validate the proposed state's remaining mandatory and selected context, full qualification closure and exact source availability without a context-fitting quota.

A definite no-commit outcome preserves prior accepted state. It does not change current work, explicit cancellation or actual source availability. Persona-proposed optional selection changes preserve whole required qualification bundles; neither the host nor a truncated context may invent a narrower meaning or silently remove mandatory character or work text.

The character acceptance unit cannot include new optional selection or exposure, unrelated semantic asset edits, communication, reads, waits, or external effects. If unrelated mandatory-context repair is needed, reject or defer with definite no commit, or reconcile an unknown outcome. Do not widen the exception to install an inadmissible state. Do not adopt unrelated action intents alongside the character change to evade the barrier.

**After the character disposition.** An accepted change fences every other fresh operation from that response outside the atomic unit, including reads and waits. Those operations must wait for a fresh primary decision that receives the accepted state. Known rejection or explicit deferral with definite no commit permits only work that meets the independence and current-guard rules above. An unknown or unresolved commit disposition holds that work. Verified exact unchanged reselection remains idempotent under the freshness rules below.

If an explicit participant resume admitted an ordinary decision that accepts a changed character, retain that admission's actual resume permission for the required fresh decision. Character-only adoption must not strand already resumed work by consuming its permission before a decision under the new character can address it. Bind this carryover to the accepted invocation and current work; a historical resume event alone grants nothing. It creates no new operator instruction and does not adopt the fenced response's proposed continuation. Existing ordinary continuations and initial character handover keep their own conditions. Do not rearm an elapsed reconsideration timer or override current cancellation, pause, ownership or failure state.

The same fresh-decision requirement applies when a legitimate ordinary admission consumed an elapsed reconsideration opportunity. A successfully accepted ordinary character transition supplies one admission under the new character, subject to current work controls. Consume that handoff permission when preparing the fresh request; preserve the timer as consumed and keep the prior authored continuation distinct. This completes the actual character transition rather than firing the timer again. A further effective character change needs its own fresh decision. Unresumed Stop or Pause supplies no initial admission, and initialization keeps its separate handover.

An idea about possible character change, without an adoption request, does not trigger this scheduling barrier. Ordinary reads may investigate it. A proposal lacking necessary evidence may be explicitly rejected or deferred with no commit. Its candidate remains unadopted; any later character change needs a fresh attributable proposal. It must not commit automatically after independent work resumes.

By contrast, uncertainty about whether a commit changed actual character requires reconciliation before further admission relies on that character. Considering a possible change is not, by itself, an indefinite hold on future work.

**Duties that continue.** Independent deterministic host cancellation, accounting, receipt ingestion, and recovery continue. Preserve previously admitted effects and their receipts; never erase or replay them to enforce the barrier.

Ordinary method edits and scoped transient-affect updates do not automatically trigger character-specific ordering. Effective character substitution does. Accepted revisions affect future context and cannot alter the current call’s provenance. A selected newly authored fragment becomes available after its save is accepted, and any dependent claim of retention requires that receipt. There is no separate character-authoring approval or restricted recovery mode.

**Ordinary recovery.** Supply actual errors, current observations and exact relevant revisions. The persona chooses useful repair, context changes, tools, maintenance and continuation through ordinary decisions without a fixed repair allowance or protected finishing reserve. Do not ask the model to invent no_change merely to pass validation. A provider refusal remains its actual outcome.

If a real provider, host or persistence failure prevents another decision or recovery remains unsuccessful, preserve the failure and remaining work. A new identifier or restart does not erase usage, make an unknown effect safe to replay or turn earlier failure into success.

## Persona authorship and files

The primary persona maintains its own characteristic account and prompt parts. It may also propose maintenance of supporting assets, whose purposes and provenance remain distinct. In both cases, proposed text becomes accepted state only through the actual identity, version and persistence checks.

**Input.** One current primary persona decision, its actual supplied context, existing exact file revisions and attributable authorship.

**Accepted result.** While doing useful work, the persona can write or revise its first-person account and contextual prompt parts expressing its approaches to work, relationships, skills, or tools. Actual experience may inform these parts, but recording experience is not their defining purpose. Every persona-authored fragment expresses its characteristic perspective without requiring trait labels or a standard form.

The persona may name, move, split, consolidate, correct, or retire files, and create, revise, or prune useful search cues. No fragment needs an outgoing link. Consolidation must preserve decision-relevant distinctions, characteristic meaning, required caveats, unresolved contradictions, and accepted warnings.

The characteristic profile and own-voice current account have one coherent accepted designation and revision. Inconsistent proposed changes require attributable revision or rejection. A display or derived index must not become a competing writer. Transient modeled affect has its own accepted contextual basis and applicability. Expiry may make that state unavailable, but the host cannot invent a new feeling or silently change the baseline.

**Supporting assets.** In the same response, the primary may propose useful supporting assets or their storage, refinement and organization, with intended targets and useful search cues as described above. This includes tools, skills, history or message resources, data, scripts, and code, while preserving their source roles.

Deletion and retirement keep their actual author, scope and observed outcome. They do not satisfy an obligation, resolve a warning or establish that an uncertain effect never happened. Missing originals remain unavailable; exact imported bytes and authoritative receipts cannot be rewritten as persona-authored prose. Deterministic factual capture remains separate from discretionary maintenance.

**Failure behavior.** Stale edits conflict; they do not overwrite accepted changes. Dependent multi-file edits, qualification changes, and next-context references must commit coherently or leave the previous valid state intact, including any separately accepted applicability warning.

An exact repetition returns the original disposition while its authoritative history remains retained and accessible. Otherwise, return an honest unavailable or unresolved disposition under the retention rules. Do not reconstruct missing history or replay the operation. A failed save cannot support a delivered claim that a prompt part was accepted, or remove a warning from unchanged bytes.

Preserve current character, maintenance input, required qualifications and actual source ancestry when adopting a change. Record the resulting state and actual persistence outcome without an application footprint ceiling. Repeated small revisions can still increase cost or impair usefulness; the persona can choose consolidation through ordinary maintenance, and real storage or provider failures remain visible.

Independent work is eligible only under the complete-response and dependency rules above. Uncommitted prose supplies neither authority nor received evidence.

**Visible evidence.** Preserve the actual author, adopted source where relevant, prior and accepted revisions, committed changes, conflict or failure, and origin of any outside edit. A peer's suggested wording is not already the owner's account. An operator edit retains its actual origin rather than becoming persona authorship.

**Initialization and later harmonization.** Initial generation uses the same coherent acceptance boundary, with an attributed seed instead of a nonexistent prior character. Retries preserve creation identity and the actual accepted outcome without an application attempt quota. Sparse generated detail is candidate authorship, not an invented user preference or lived history.

Later self-harmonization is ordinary primary-authored maintenance. It preserves compatible conditional tensions, exposes unresolved contradictions, and retains exact authorship and coherent effective-character adoption. It creates no second writer, mandatory corpus-wide rewrite, or automatic trait drift.

No extra reflection writer, relationship writer, semantic merger, or generic prose generator maintains the persona behind its back. Work and the explicit maintenance outcome belong to the same invocation. Useful mutation is discretionary; explicit maintenance is not. A retained maintenance deferral follows the attributable lifecycle above and does not itself schedule inference.

**Honest authorship and experience.** First-person wording does not turn supplied advice into firsthand experience. A tentative intention may be retained before an operation completes; a later observed result cannot be backdated. Evidence that an operation failed supports an interpretation of that failure. An uncertain effect establishes uncertainty.

Effective current identity includes redesignation or an always-loaded substitute. Record its actual author and coherent adopted revision without a self-authorship permission or approval gate. A contextual fragment, scoped method or relationship interpretation can shape later behavior without changing stable character. When an effective-character change is adopted, the fresh-decision rule still preserves which character informed subsequent operations. Neither a stored trait nor a mechanical check proves useful maturation.

## Search and exact reading

Search helps the primary persona find candidate fragments and supporting resources. The persona chooses the query, scope, requested page or exact read and decides what is relevant. The host does not choose context on its behalf or impose a cumulative navigation allowance.

**Input.** A persona-chosen listing, literal or grep-like query, supported regular expression or exact reference identifies the material sought. Supporting resources include history, tool records, definitions, skills, scripts, code and data, with their roles kept distinct. An authored cue is data; searching it does not execute it as a shell command or automatically follow its connections.

**Result.** Describe the searched corpus, matching mode, exact source-qualified revisions and how to obtain their text or operative definitions. A descriptor or excerpt is not the full body. Declare filename, body and metadata matching, case semantics, regex dialect, ordering, pagination and treatment of hidden or ignored files. Return the requested material without application pattern, scan, text or count ceilings.

Literal and regex search, authored indexes and cues, listing and exact reading form one navigation interface. The primary chooses further navigation and context. Physical indexes may support the interface without adding a hidden semantic selector, universal relevance score or fixed taxonomy. A changed corpus can change current candidates; it cannot change a prior exact observation.

**Pagination and completion.** State whether pages refer to a snapshot, exact revision or live view, and whether completion describes a page, scan or whole identified corpus. A requested page size controls that result, not the number of later requests or total work. Return the actual continuation cursor when more material remains. A live cursor alone cannot prove exhaustive coverage of an earlier corpus.

When messages, authored decisions, tool observations and files have distinct
query interfaces, identify the requested record kind and matching surface in
each result, including unsuccessful queries. A complete message search cannot
establish that a correction is absent from decisions or tool results. Keep that
scope next to completeness and no-match claims; provide the appropriate
discovery or exact-read route without silently searching another corpus.

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

**Decode once.** Decode JSON string escaping exactly once at the serialization boundary. The resulting prompt string is the text supplied when selected. Parse a resulting regex string using the declared regex dialect/version and flags, without another JSON or generic escape-decoding pass. Regex interpretation is separate from JSON decoding and does not evaluate commands.

Faithfully preserve literal backslashes and escaped Unicode/newline distinctions. Keep an unsupported or invalid pattern distinct from invalid JSON, no match and an actual parsing or search failure.

**Locations and exact identity.** A supported decoded lexical view is a deterministic projection of the exact source revision. Record its parser/profile version, field location, and decoded match range. Raw results instead identify serialized-source locations under declared offset units. A decoded location is not a raw byte offset.

Exact source reads remain exact bytes. Labeled decoded field reads and actual prompt supply retain their source/version binding and qualifications. Re-serialization or formatting changes create a different exact revision even when decoded text remains equal. Derived views and indexes preserve exact source provenance and actual retention state. They cannot add semantic ranking, automatic cue traversal, selection, or a hidden fallback.

**Actual resource use and failure.** Record source bytes, parsing and decoded size, pattern compilation, scanning, projections, index maintenance and returned output as observed. A small result does not prove a cheap scan. Do not impose application pattern, depth, scan, output, history or cumulative navigation quotas.

An actual parser, host or storage failure must report the affected incomplete operation. It cannot establish exhaustive no-match or justify silently removing required qualifications. Search treats cue text as data and never executes it automatically; personas may separately choose host commands through the ordinary interface.

## Primary-persona next-context selection

The primary persona decides which characteristic fragments and supporting resources its next decision needs. The host supplies that exact accepted choice, together with mandatory state and complete qualifications. Finding material, choosing it, and actually supplying it are different facts.

**Input.** The current primary persona’s exact fragment and supporting-resource choices or chosen requests for later decisions, current character, actual work observations, current obligations and complete qualifications. A known exact reference may bypass discovery. Unknown material is obtained through requested metadata or exact reads, not an all-catalogue choosing prompt.

**Accepted result.** The primary LLM, acting within the current persona, chooses the prompt parts that should shape its next characteristic context and the supporting material that decision needs. An explicit choice may retain exact optional fragments or supporting resources for that work until replacement, clearing, expiry where a lifetime was specified, or invalidation.

The primary may select a currently readable exact candidate from a preview without claiming to have read its full text. It may also select newly authored accepted text without a search ritual. Evidence, histories, skill instructions, code or data ranges, tool guidance, and actual callable definitions retain their supporting roles and real authorship.

The resulting decision receives the selected exact full text or declared range and complete applicable qualifications. Operative tool exposure includes the usable definition, not merely a stored reference to it. A metadata request supplies only the requested preview. This assembled context contributes to the operating persona; it does not establish consistent or useful behavior.

Captured images can be selected as supporting context alongside text. Bind each
choice to its exact immutable capture, original observation, detail and work
lifetime; a known exact reference or an admission-bound handle can identify it.
Preservation, replacement, clearing and expiry apply to the whole chosen asset
set, including images. Receiving pixels once does not select them for later
inputs, and preservation does not renew an expiring choice. Later supply reuses
the captured bytes with their attribution and current required qualifications,
without reopening the host path or manufacturing another read. A pending and
selected copy of the same capture needs only one provider image part. No image
catalogue, automatic selection or quota is required. Selected historical pixels
do not establish current host-file contents or the correctness of a visual
judgment. Image choices follow the same character-transition and unavailable
optional-bundle rules as other supporting context.

A failed host-image capture records an unavailable observation without pixels;
it does not mean that its enclosing decision or other operations were rejected.
An optional expected SHA-256 must be a complete lowercase hexadecimal digest.
Distinguish malformed expected digests from valid digests that do not match the
captured bytes, without repairing a pin or silently supplying a different image.

**Failure and recovery.** An unavailable or changed selected revision gets an explicit disposition. It cannot silently follow a path to different bytes. The following distinctions apply:

| Situation | Required treatment |
|---|---|
| Explicit preserve, replacement, or clear | Preserve retains an appropriate accepted choice; replacement replaces it; clear removes the optional choice. Preserve renews no chosen lifetime and cannot restore an unavailable source. |
| Omitted or malformed next-context intent | Invalidate the whole response. Rejected output adopts no new choice and dispatches no fresh proposed work. Preserving stored state after rejection is recovery, not an accepted persona judgment. |
| Optional selected source or required part becomes stale, withdrawn, or inaccessible | Withhold the entire affected optional bundle and record its ineligible disposition without silently clearing the stored choice. An otherwise valid fresh decision may receive that factual disposition and repair the choice; it must not claim that withheld text was supplied. |
| Mandatory self or work source is missing | Block affected admission. |
| Failed edit on which a new selection depends | Leave the new selection unaccepted. |

Withholding an ineligible optional bundle does not permit discarding valid selected text merely to fit an ordinary task decision. Actual provider or host failure follows the recovery rules below without an application fitting or repair quota. New work begins with its own mandatory brief and observations. Another work's private focus or persistent optional selections do not transfer automatically.

**Explicit disposition in every accepted response.** Every accepted persona response authors its next-context disposition for both characteristic fragments and supporting resources. A concise, unambiguous preserve of a still-appropriate accepted choice is sufficient. Other valid dispositions are replacement, clear, no further optional need, chosen discovery/read intent with explicit retained or cleared optional state, or an honest blocked/stop outcome.

No new search, mutation, repeated list, full-body dump, extra model call, or fixed field schema is required. “No further optional need” explicitly chooses an empty future optional set: it clears an existing set or keeps an already empty one empty. This affects neither mandatory context nor already exposed observations or retained history.

An explicit replacement may select an empty set. Its emptiness is an authored
choice to clear the replaced optional material, not an omitted disposition or a
request to preserve earlier selections. When a replacement combines text, images
and provider continuation, each supplied part keeps its declared meaning; an
empty text list alone does not erase another explicitly selected part. Required
character context remains independent of these optional choices.

Before any accepted optional-context choice, including during initialization, the current optional set is empty. An explicit preserve records that empty set as the persona's first reasoned choice; clear also chooses an empty set. Neither invents an earlier selection, loads observed bodies, removes mandatory character context, nor bypasses the character-transition rules. Final, short, social, refusal, and tool-follow-up responses are covered without requiring continuation. A blocked/deferred choice may retain stored ineligible selections as ineligible; it never makes them usable exposure.

Explicit selection can still be poor judgment. For example, preserving irrelevant but eligible material is a selection-quality failure to evaluate, not evidence that the response contract prevents all semantic mistakes.

**Visible evidence.** Preserve who chose; the exact requested and selected versions or ranges; scope and lifetime; preservation or change of the choice; and actual provider-bound text and callable schemas with qualifications. Include message/channel roles, boundaries, and order as actually rendered, rendered expansion and retained context where applicable, requested previews, actual omissions, and any mismatch that blocked admission.

Host registry storage, provider transmission, model-context inclusion, and billed input need separate evidence. Inspection preserves actual exposure and retention facts. Retain sufficient exact identity without requiring an unnecessary raw prompt or private reasoning archive.

**Mandatory state and the host’s role.** The runtime adds current identity and work, cancellations, obligations, actual blockers, critical observations, coherent current character, relevant modeled state and maintenance responsibility. It preserves the exact scope of past judgments and current feedback. These records do not make the host an independent semantic selector of characteristic context or create a safety workflow.

The declared file-search interface and primary-navigated authored cues or indexes expose candidates without choosing optional prompt parts or authoring their meaning. Auxiliary semantic, vector, or graph-retrieval engines are different research comparators, not production options or fallbacks. Ordinary external task tools remain available through full host access. Their results still need primary judgment and cannot silently replace fragment navigation or authorship.

**New observations.** An unexpected reply or failure enters relevant current observations even when the prior choice did not anticipate it. In an ordinary decision, the persona can then search, read, and choose prompt parts for an appropriate next approach. A search hit does not automatically add a fragment to context, and an old selection must not suppress a new adverse fact. A same-call authored change applies to subsequent context; it cannot rewrite what the current decision received.

**Complete request and actual supply.** Record the whole request for each provider attempt: bootstrap and instructions; current character, work and modeled state; maintenance and next-context input; observations, requested metadata and operative definitions; selected fragments and assets with their qualifications; protocol history and media. Preserve exact references, current decision identity and complete response validation without application byte, item, output or attempt ceilings.

Do not silently shorten selected prose to a title, omit a required exception or choose a semantic substitute. An actual provider or host failure retains the attempted request and observed outcome. The persona can choose useful context or method changes where another decision can be supplied; the host does not impose a mandatory restricted repair workflow or invent a choice from failed output.

**Actual exposure and retained context.** The [chosen capability working set](../design/WORK-AND-BOUNDARIES.md#inference-and-bounded-working-context) concerns actual provider transmission and model context, not merely the host’s intended list. Assemble exact chosen context instead of retaining every past tool, skill and result in each input. Preserve active-operation controls, critical results, current work, character and other mandatory state. Retained history remains discoverable without an application corpus or input quota.

Cached prefixes, previous-response links and hidden provider history neither prove absence nor eliminate exposure. Describe known schema expansion and retained context honestly; unknown expansion stays unverified. Choose supported provider context or reset mechanisms when useful, without claiming a hard bound the adapter cannot establish. Sending the bulk catalogue for the model to filter fails selective discovery even if provider-native deferral is used. Remembering an old tool name does not establish its current definition or an accepted invocation.

<a id="restricted-selection-repair-after-later-context-growth"></a>

### Ordinary recovery after actual provider or host failure

The former application overflow mode and finite repair allowance are historical under UR-052. The current design follows [faithful assembly and actual failure handling](../design/PERSONA-CORE.md#selection-overflow-repair): no configured context ceiling, repair quota or separate safety approval prevents an ordinary decision.

Preserve exact selected material, mandatory persona and work context, and required qualifications. Report real provider, model-context or host failures without silent truncation, fabricated maintenance, invented next-context choices or replay of rejected actions. A preview or inventory does not establish that its underlying text reached the model.

After an exact provider `context_length_exceeded` rejection, complete pending
host results and supporting-file reads present in that failed input may be
delivered as explicitly labeled exact references or byte metadata. Preserve the
original request, read/result, source identity and current qualifications. This
is delivery recovery for an unconsumed observation, not a change to authored
optional selections or mandatory character. The fresh input states that the
requested body was not supplied successfully. Use the actual provider rejection,
not a guessed size threshold; a second rejection of metadata supplies no new
projection through this route. The ordinary primary chooses subsequent reads,
tool use, context and continuation, and acceptance consumes the pending override.

Where another decision can actually be supplied, the persona chooses useful context changes, maintenance, methods and continuation. Every such decision retains the ordinary work, fragment maintenance, asset maintenance and next-context responsibilities. The application does not prescribe a separate repair workflow or infer that a smaller selection makes the work complete.

Historical restricted-repair attempts retain their original inputs, mode, charges and outcomes. They are not retroactively reclassified as ordinary work or successful repairs.

## Decision authority and freshness

A decision may use valid information when it is made and still be too stale to act on later. The host must therefore recheck consequential current state when adopting the response, not only when assembling its request.

Deterministic host validation may reuse a successful decode when a fresh transaction establishes that the complete current logical record bytes and lookup identity are unchanged. Logical record bytes are the complete result of physical storage decoding, before interpretation as an object. Recheck physical encoding, current record metadata and the expected configuration as well; a remembered revision or earlier success alone is insufficient. Any changed logical bytes require fresh validation, including changes outside configuration or changes to JSON encoding. A different physical representation can reuse validation only when its newly validated decoded logical bytes are identical. Failed validation must not become a reusable success. Account for the actual work and retain the declared logical read charges separately from physical I/O or provider usage. This host optimization neither selects persona context nor changes decision ownership, adoption or freshness requirements.

An implementation may retain the current decoded state for ordinary loads as well
as configuration checks. Keep the stored head immutable and each caller's mutable
working state separate. Recompare expected configuration on every check, discard
failed reads or decodes, and preserve normal mutation transactions and their
current-version checks. Each Runtime owns its cache; no prior process or runtime
supplies a cached authority. Account for the extra retained memory and distinguish
measured repeated-read savings from end-to-end task latency. A decoded tree can
greatly exceed the serialized record size; release it at session waits for
providers, host commands and authored return times, then decode afresh when work
resumes. A Closeout read keeps its separate accounting and validation path.

One persona has one current primary decision authority at a time. Independent personas and isolated jobs may proceed concurrently. An admitted decision binds actual identity, work, relevant versions, observations, inference configuration and actual resource exposure. A model change does not change identity or accepted commitments.

Distinguish shared result records from the authority needed for independent
navigation and tool work. A new peer candidate, evaluation, release or delivery
record alone should not discard such a response when its separately recorded
identity, task, responsibilities, arrangements, pending dependencies and supplied
source lineage remain unchanged. Apply the response to current state, retaining
the peer's records and the original information on which the persona reasoned.
Shared work commands and responses combining them with other operations retain
their complete current-record checks. Accepted tool intents retain the dependency
scope established by their own adoption; a later record does not imply that it
was seen or used. An older admission gains no narrower scope retrospectively.

**Character and current guards.** Apply the character-proposal ordering rule before any other fresh operation from the response. A request to adopt a stable-profile or baseline-affect revision must be resolved first.

| Current-state event | Consequence |
|---|---|
| Effective-current-character change is accepted | Fence fresh operations outside the narrow atomic acceptance unit, including reads and waits, until a fresh decision receives the new state. |
| Scoped transient modeled-affect update | Treat it as ordinary contextual state unless it substitutes a new effective character. It does not automatically trigger the character barrier. |
| Cancellation, changed scope, or stale decision ownership | Fence actions that no longer match the actual current decision or accepted work. Historical source-policy revocation is not a current access gate. |
| Exact unchanged and still-current character designation | Once verified, treat it as idempotent; it does not fence otherwise valid work. |
| Definite no-commit disposition | Leave previous accepted state in place, subject to valid-response, independence, and current-guard requirements. |
| Unknown commit status | Do not treat uncertainty as evidence of rejection or unchanged state. |

Late results remain evidence and accounting; they do not restore authority.

**Evidence of receipt.** Included, received by a provider, acknowledged, understood, agreed, and used are different claims. Notification acknowledgment must bind the exact inputs actually supplied to that recipient and decision. A historical cursor cannot prove observation of an older message that has only now become readable.

Recheck actual notification identities and supplied content at mutation. Missing inclusion cannot be repaired with a fabricated receipt. A fresh observation requires an actual current invocation and supplied result, without a separate funding or access grant.

## Work and accepted responsibility

The system must keep the original need visible and show who has actually accepted responsibility for meeting it. Interpretation, an offer to help, delivery, and acceptance are not interchangeable.

**Need intake.** Preserve the exact original request, source, constraints, permitted assumptions, accepted changes, criteria, and closure terms. The persona may author an interpretation, but cannot silently reduce the need. Required outcomes must have accepted responsibility or a visible gap.

An unanswered ordinary question follows the [clarification boundary](../design/WORK-AND-BOUNDARIES.md#questions-assumptions-and-shared-context). Record provisional interpretation separately from confirmation, preserve real blockers, and reconsider affected assumptions when an answer arrives.

**Commitments and handoffs.** Keep membership, a contribution offer, commitment acceptance, and actual contribution distinct. Only real endorsements bind the named participant and terms. A handoff transfers responsibility only after the receiver accepts, or an authorized disposition explicitly replaces it.

Compute an arrangement's required assent from its actual changed commitments,
artifact transfers and old and new decision holders. Recheck the exact
delegation, current arrangement, affected acceptances and preserved duties at
adoption. Unchanged contributors do not form a compulsory approval quorum.
Adoption supplies no endorsement of the result beyond the actual attributed
judgments, and it never resumes a stopped participant. Earlier records retain
the policy and build meaning that produced them.

Decline and nonresponse create no substitute acceptance, replacement persona, punitive reputation, or dependency on someone who never agreed.

**Organization.** Persona-owned organization uses discovery, proposals, communication, accepted commitments, and evidence-led revision. No task keyword, fixed profession roster, compulsory coordinator, birth rule, or hidden domain pipeline chooses the solution. A human-imposed constraint or explicitly adopted reusable method may legitimately guide work. Evaluation needs evidence of the actual orchestration policy; a convincing unscripted transcript is insufficient.

**Birth.** Each actual creation preserves its requested identity, seed provenance, initial model authorship and invitation. No application population or initialization quota applies. Creating a persona does not establish experience, expertise, membership or accepted responsibility. Duplicate requests preserve the actual creation outcome without inventing another identity; actual usage remains recorded even if participation is declined. Existing personas and simple work need no creation ritual.

Ordinary asset maintenance must preserve a proposal's usable authorship. An
accepted native edit can supply starting material just as an accepted full
write can, either from an earlier invocation or as an exact dependency in the
creation response. Check the saved bytes against the accepted authoring
operation. For an edit, also retain and resolve its immutable base and exact
replacements; unchanged bytes retain their earlier provenance. Importing bytes
alone establishes no primary authorship, and a rejected or fenced operation
establishes no accepted proposal. Neither maintenance form creates an identity
without an actual creation request.

## Capabilities and actions

The default runtime gives personas [full host access and tool installation](DEPLOYMENT-DECISIONS.md#default-full-host-access). Ordinary inputs supply that command interface directly. No per-tool approval, installation grant, command allowlist, sandbox, or prior skill-guide selection is required. Personas choose tools and commands using the host account and environment. The distinctions below describe actual preparation, execution and observed results; they do not introduce an additional permission gate for this default host interface.

Working directories and retained-state locations may coincide or contain one another. Setup and continuing execution must not reject their placement or relationship as an application access rule. Resolve supplied paths to their actual directories, retain the identities needed for continuity, and report unavailable paths or host filesystem errors as observed outcomes. A changed saved path binding is distinct from an application directory-separation requirement.

Stored guidance helps a persona prepare for an operation. It does not establish that the operation is installed, callable or ready to run. A skill file is reusable procedural guidance with an actual author. A persona-authored characteristic interpretation is persona-defining prose; the underlying procedure retains its supporting purpose. A tool note describes an operation and its observed limits. Neither stored guidance nor scripts, code, or data install a tool, prove competence, grant credentials, or execute a helper. Preparation and current callable exposure remain separate.

### Dynamically created and shared skills

Under [UR-053](../USER-REQUIREMENTS.md#dynamically-created-and-shared-skills),
ordinary asset maintenance supports persona-authored skills of any kind,
including instructions, code, tool wrappers and supporting resources. A
publication identifies an actual common storage location, useful discovery
cues, its author and version, and relevant usage and dependency information.
The shared collection can be organized and revised by personas. Publication
requires no separate application approval or fixed skill registry.

Recipients choose discovery, exact reading, selection, use and adaptation
through the ordinary interfaces. An adaptation keeps its own identity and
attribution and identifies the source version it derives from. Existing
selections retain their exact versions until the persona changes them.
Characteristic fragments may reference the skill and express the persona's
habits for finding and applying it; the procedure and executable content keep
their asset role. General host execution and context mechanisms support new
skills without a new hardcoded workflow for each one. Actual installation,
dependency availability, callable exposure, execution and results retain the
distinctions below. Finding or saving a skill alone establishes no successful
use, and the shared catalogue stays outside model context until selectively
requested.

### Execution and observations

**Bind execution to what will actually run.** The required binding depends on the operation:

| Operation | Required binding |
|---|---|
| Default full-access host command | The exact command and inputs, host working directory and account, native runner and shell, and actual observed status/output. Transitive program versions are recorded only when actually observed. |
| Controlled local helper execution | The exact artifact, relevant resolved dependencies, environment, and inputs. |
| Remote operation | The observable service, interface, and connection identity, together with relevant exact client or runner versions and input versions. Unavailable server-build identity stays explicitly unknown. |
| Local helper that calls a service | Both the local and remote boundaries. |

An executable-version claim requires the claimed version to be genuinely bound to the observed operation. A filename, schema version, subsequently edited helper, or past success is insufficient. Missing server identity blocks a use only when the required assurance depends on that identity; otherwise, it narrows the claims that can be supported. The actual identity, dependency and outcome distinctions in the [execution boundary](../design/WORK-AND-BOUNDARIES.md#capabilities-and-the-execution-boundary) still apply.

Exact code and bulk data may remain outside model context when the selected runner consumes their references. The persona still receives relevant usage guidance and actual results under its chosen context; no application result quota is imposed.

**Keep each stage's meaning clear.** Finding an operation, supplying it to the model, and carrying it out establish different facts:

| Meaning | Required distinction |
|---|---|
| Discover | A match or descriptor requested by the primary identifies candidates, exact versions, and honest search coverage. It is not endorsement, a full read, exposure of the full operative body, or authority. |
| Read | Exact content, or a declared range or result, becomes an observation with provenance and qualifications. Reading documentation neither registers a callable native tool nor runs code. |
| Select | The primary requests exact fragments, supporting material or requested metadata for later context, with scope and disposition. Selection does not prove actual supply. |
| Load or expose | The host supplies the selected text and, where applicable, the actual operative callable definition. It records provider-facing and model-context exposure, qualifications, and omissions. Exposure does not establish execution or acceptance. |
| Invoke | A complete, valid current decision requests an available operation using its actual interface, identity and inputs. Record accepted intent and dispatch separately; storage or exposure alone establishes neither. No separate safety approval, quota or tool grant applies. |
| Observe results | The actual pending, failed, partial, completed, or effect-unknown outcome reaches a fresh decision before dependent work proceeds. Output that looks successful does not prove correctness or delivery. |

These are observable meanings, not six required calls or a compulsory sequence. A known exact reference can be requested without discovery. A still-current, fully supplied interface permits immediate invocation. Independent requests may share a decision, but actions that depend on new content or results still require a fresh observation of that information. Provider-specific loading does not replace these distinctions.

**Saving a supporting asset and using it.** An ordinary supporting-asset change does not itself require another persona call when all of the following hold:

- The primary proposed the exact bytes and the dependent action.
- The proposal uses an already supplied, still-current interface.
- Coherent local acceptance binds the dependent action to the exact saved revision before dispatch.

This case uses the existing [complete-response and persistence boundary](#complete-response-persistence-and-dependent-work). It does not allow continuation through unobserved tool-produced content or results, or through a pending or unknown write. Storage creates no installed capability, grant, or callable exposure. Actual identity, dependency, effective-character and fresh-decision semantics still apply. A failed prerequisite or an applicable fence holds dependent work; a later receipt cannot revive suppressed actions. This clarification creates no automatic workflow facility.

**Native adoption and host writes have different interfaces.** Changes submitted through the native persona API follow the complete-response, version, character and persistence contract. A native helper must record an admitted change and its actual outcome rather than inventing a maintenance or execution receipt.

The default full-access host interface also permits ordinary filesystem writes and persona-authored scripts under the host account. Those commands are not confined to the native asset interface. This profile trusts the host account's access to backing files and does not claim that record-level controls isolate or make those files tamper-proof. Report host writes and their observed outcomes as host effects; do not label a direct file edit as a native API adoption.

**Record an action before dispatch.** An admitted action identifies:

- The actor, the work that caused the action, and a stable request identity.
- The exact relevant inputs, intended effect, capability and current decision identity.
- The resources and the terms for observation or cancellation.

Durable intent precedes dispatch. Repeating the same accepted request must not duplicate its effect. Changed content under the same identity is a conflict.

**Use observed outcomes for dependent work.** A running operation does not satisfy a dependent action. Suppress the unobserved remainder of its decision; dependent work requires a fresh decision bound to the actual result. Preserve the distinctions between proposed, admitted, running, failed, completed, stopping, canceled to the observed extent, and effect-unknown states. Reconcile uncertain outside effects before repeating them. Completed execution establishes neither correctness nor delivery.

**Keep operations usable and controllable.** Available operations must be usable from their actual loaded guidance, with clear identity, version, replacement, and effect meanings. When an invocation supplies one interface for a capability ID, use that ID to select its retained exact binding rather than requiring the model to copy a revision digest. Reject absent or ambiguous admission bindings and verify the retained implementation and input schema before staging; keep that same binding in the accepted job. Current successful receipts should expose appropriate inspection options without requiring a decision devoted only to discovering syntax. Compaction must not hide control of unresolved jobs. Old terminal history, however, need not keep every operation permanently loaded. Projection is not permission, deletion, or evidence that an artifact was inspected.

**Treat changing resources according to what was observed.** Distinguish exact historical snapshots, current live references, cached observations, and derived outputs tied to their actual inputs. An unversioned path or a notification is not a fresh observation of the payload. Resolving a reference identifies the version actually obtained. Reuse preserves exact source, work scope and freshness without claiming a new read. Paginated results need not form a coherent snapshot.

When a persona selects a field or range from a retained command result, identify
the originating invocation, observation and recorded outcome time alongside its
source attribution. Describe only the representation actually supplied: selected
stdout does not also supply the command or exit status. A recording timestamp
marks outcome publication, not the production time of every output byte or a new
inspection of mutable host files. Keep missing recording metadata explicit.
New observations and retained selected output may appear together; neither
selection nor a later timestamp alone establishes current file contents or
supersedes another result. Personas decide their relevance without an automatic
refresh requirement or a prescribed repair workflow.
Likewise, a new admission, elapsed time or activity on unrelated files does not
by itself invalidate captured evidence. Rechecking relevant preconditions and
performing a proposed host change may share one command; the interface must not
imply a compulsory inspection-only call before every action or judgment.

A requested watch, acknowledged supported coverage, an active stream, and an ended or unsupported watch are different states. Lost notifications cannot establish that data is unchanged. Notifications may invalidate retained bindings, but cannot automatically select new content, enable a removed capability, or authorize an effect.

## Authority, resources, and stopping

The application follows [unrestricted execution](../design/WORK-AND-BOUNDARIES.md#unrestricted-execution-requirement). Do not require a quota increase, resource grant, safety permission or approval to continue work, run tools, navigate history or retain results. The former protected-allocation contract is superseded by UR-052.

**Keep fresh setup about current choices.** Collect the actual provider binding,
working location, destination, initial identities and attributed starting
profiles. Do not require obsolete quota or permission declarations because old
records contain them. The initial cohort is a creation choice, not a population
ceiling, reservation of future slots or assignment of work and review roles.
Any neutral internal bookkeeping defaults are not user-declared ceilings or
separate permission decisions. Retain earlier declarations and actual usage
without rewriting history or treating them as present execution gates.

**Keep provider configuration free of quota declarations.** Current provider
input identifies the selected route, model, effort, credential source and actual
account binding. Do not require historical transport estimates, fabricate them
during onboarding or expose an extension command to change an unenforced quota.
Retained declarations and receipts remain attributable to their original state.
A continuing runtime may project the fields needed for current inference without
rewriting those records; new preparation identifies the exact current
configuration. Complete JSON parsing and streamed-response assembly need no
application quota arguments. They still distinguish valid complete data from
duplicate keys, invalid encoding, partial responses and inconsistent identities.

**Measure actual use without making it an admission gate.** Record model calls, tool executions, unsuccessful attempts, navigation, selected context, maintenance and result retention. Distinguish transport bytes, reported tokens, billed usage, latency, storage and monetary exposure. Unknown usage remains unknown, and smaller context does not establish lower total cost or useful completion.

A recovery observation carries the terminal receipt's actual usage fields. A
local response rejection does not make reported token counters unknown, and
available counters do not establish unreported charges. Avoid a blanket usage
label that contradicts the attached receipt; preserve missing fields as unknown.

Retain fragments, supporting assets, histories, tool definitions, code, provenance and unresolved effects with their actual identities. Context selection and requested pagination decide what is supplied to a model input, not how much historical state may exist or how many calls a task may use. Do not erase evidence to satisfy an obsolete quota. Report real I/O, provider and representation failures with their observed outcomes.

**Separate a local stop from the goal's status.** Record the reason for a local stop separately from the accepted goal's disposition under [continuing pursuit](../design/WORK-AND-BOUNDARIES.md#continuing-a-goal-across-local-boundaries). For unfinished continuing work, bind the record to:

- The current mandate and owner.
- The exact candidate and the outcomes still unmet.
- Actual observed usage and unresolved resource failures.
- The actual continuation opportunity, or the blocker and route for reconsideration.

If these cannot be established, expose the continuation gap. Transfer or ending needs its applicable authority. Existing work records suffice; no universal new file schema is required.

**Keep a previous judgment tied to its original scope.** When supplying an earlier persona work judgment to a fresh decision, retain the invocation, admitted work version and mandate it judged. Distinguish that mandate from the current one. Do not relabel the earlier judgment after an amendment or infer missing attribution from current state. A judgment under the same mandate still does not establish that later feedback or results were considered. The persona decides its present contribution from the current request and observations; supplying a past judgment does not resolve feedback, accept new responsibility or establish current completion.

**Bind feedback to its receipt context.** Record the exact mandate in effect when requester feedback enters the durable inbox. Retain that binding through deferred delivery, replay, task amendments and history reads, and distinguish it from the current mandate in persona and operator views. Verify the binding against the retained mandate rather than recapturing it at delivery. Where an earlier receipt lacks this fact, expose the missing origin without inference. This is factual arrival provenance, not an automatic applicability decision, replacement, new obligation or resumption. Explicit replacement preserves the original body and actual persona accounts; a handled account alone does not replace a direction.

**Give eligible accepted work a real opportunity to continue.** An accepted ordinary-work continuation preserves its actual eligibility across yield, result delivery, and restart. Under the declared supported fairness and capacity assumptions, persistently eligible accepted work must receive another decision opportunity. Merely keeping it visible in a queue is insufficient. Queue churn and pagination cannot evade this obligation. Expose unmet scheduling assumptions or failed consideration as limitations, not task completion.

If a selected opportunity must wait for active calls to settle, advancing the
scheduler cursor must not spend that opportunity without admission. Retain the
candidate's identity and reconsider it first after required maintenance, checking
current eligibility and authority. If it is no longer eligible, continue ordinary
selection in the retained order for other opportunities; the failed preference
must not promote its whole work or consume another cursor position. This
preference adds no persona responsibility, fixed role or call.

Before a fresh primary decision, recheck explicit pause or cancellation, current work, decision identity and actual observations. A fresh decision does not replay a suppressed action batch. A valid dependency wait need not become polling; a wished-for reply is not an event. A partial result or explicit stop can handle a boundary correctly while leaving the full task unfinished.

**Release an ended local call after an observed stop.** When a recorded runtime stop cancels a response-only model call, retain its exact local terminal outcome and release the matching local invocation once no adoption or action intent can remain. This includes a complete response canceled before adoption. Preserve current work and persona controls and authored continuation choices; local cleanup grants neither resumption nor replay. A later explicit resumption remains a separate fact. Do not infer remote termination, reconcile unknown charges, or treat missing terminal evidence or an unavailable control monitor as a completed cancellation.

This also covers a stop between admission and provider dispatch. Retain the
admission's control-history boundary and the exact no-launch rejection. A
recorded intervening stop or a currently effective stop can justify retiring that
failed local call without lifting the stop. A subsequent explicit resumption
does not revive the old call. An unrelated configuration failure does not acquire
an automatic retry through this cleanup rule.

## Review and release

A review must support the claim being made about the work. An ordinary self-check or peer comment can be an attributable assessment without becoming a formal review commitment. When the adopted acceptance policy requires a review, an informal assessment does not silently satisfy that requirement.

**Bind a required review to its actual basis.** It must identify the exact scope, criteria, inputs, and assumptions; a reviewer who has actually accepted the review; any independence criterion actually required for the claim; observations; explained judgment; findings; and limitations.

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

These contracts state required behavior; they do not report that a runtime implements it. The [evidence criteria](../evaluation/ACCEPTANCE.md) distinguish mechanisms, observed behavior and useful outcomes, and the [evaluation method](../evaluation/README.md) governs claims from actual work. No fixed test campaign, generated scenario or minimum count is prescribed. Historical graph and selector results retain their [original criteria](../evaluation/HISTORICAL-RESULTS.md). The [status ledger](STATUS.md) identifies current implementation and evidence gaps. Documentation review and compilation do not establish product acceptance, complete useful delivery or characteristic maturation.
