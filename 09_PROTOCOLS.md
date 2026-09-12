---
title: PersonaOS — Protocols, Standards, Adapters, and Keys
status: Stable
---

# 09 — Protocols, Standards, Adapters, and Keys

This document defines PersonaOS protocol boundaries. Wire protocols transport
exact authority and effects. They do not select persona behavior, interpret a
task, impose a workflow, or manufacture completion.

This revision is a clean break from ranked capability discovery, fixed tool
phases, prompt programs, stage-only action surfaces, host-selected team
channels, reputation/fitness routing, and compatibility adapters for retired
schemas.

## 1. Protocol invariants

1. Every authority-bearing record is canonical, signed, replayable,
   and bound to exact subjects and scopes.
2. Descriptors declare mechanics and effects explicitly. The runtime never
   derives them from names, prose, arguments, prompts, task words, filenames,
   extensions, executables, professions, regular expressions, media types, or
   domain vocabulary.
3. Inventories are complete and unranked. Pages state their exact omissions
   and continuation; a presentation window does not cap durable inventory.
   Stable ordering is transport order only. Append-derived pages
   preserve absolute positions and cardinality, including equal records at
   distinct positions.
4. Personas choose actions. Protocol adapters neither recommend nor sequence
   them.
5. Open persona-authored content remains a claim. It does not become kernel
   truth, action authority, completion, or continuation by crossing a protocol.
6. Missing optional identity, work-note, gap-like knowledge, memory, or skill data
   never narrows an otherwise authorized ordinary action surface.
7. Quiescence is a nonterminal absence of pending causal delivery.
8. Mechanical admission may refuse an already-chosen effect using exact
   canonical, integrity, authority, consent, resource, safety, and declared-
   effect facts. It never turns task/content semantics into workflow,
   population, model, tool, artifact, or next-action selection.

## 2. MCP capability and resource transport

MCP carries tools, resources, the generic `author_persona_knowledge` action, and
visibility-authorized persona-owned knowledge metadata. A live tool descriptor exposes:

- exact action identity and descriptor hash;
- exact input and output schemas;
- provider and authorization bindings;
- read-only, workspace, owner, task, external-event, and other mechanical
  effect annotations when applicable;
- `personaosReplicationEffects` when the action can materialize another actor;
- terminal result and retry semantics; and
- current signature, policy, expiry, and revocation authority.

Reserved transport bindings are injected only by the trusted dispatcher and
cannot be supplied by public/model-authored arguments. An adapter that cannot
preserve a required binding fails as adapter configuration; it does not
reinterpret the request as persona intent.

The immutable dispatch descriptor retains those reserved fields and its exact
hash. The persona-facing projection removes only fields mechanically supplied
by the current authenticated principal, including their root required and
dependency declarations. The dispatcher restores the exact bound values before
validating against the immutable descriptor. Action-authorship receipts exclude
the restored values, so host identity is never misattributed as a persona
choice. This projection does not inspect action names, task text, domains,
roles, argument values, or executable names.

Downstream admission, wake, population, artifact, and presentation verifiers
therefore take principal identity from the verified action envelope and compare
only persona-authored fields against `action_arguments`; they never require a
transport-bound field to reappear in that authored map.

A causal wake can remain bound to an authenticated task after the originating
run has exported, so its raw run-scoped mission identity may legitimately be
empty. Capability admission and active-call comparison preserve that empty value
exactly. After the action crosses the authenticated boundary, task-bound handlers
use the already-bound task identity as the effective mission scope when no
separate mission identity exists. This does not select, rewrite, or infer a task;
it keeps the same task's later event-driven work capable of ordinary execution,
acquisition, communication, and successor actions.

An authenticated workspace is publication authority and the default execution
base, not an authored working-directory choice. When an action schema exposes a
working-directory argument, a persona-provided value survives transport;
relative values resolve from the authenticated workspace. With no authored
value, the handler uses that workspace itself. In either case only effects
inside the authenticated workspace can be published as task artifacts. The
dispatcher never replaces a persona-authored working directory with a host
path, and the host workspace identifier is absent from persona-authored action
bytes.

Command execution preserves terminal status, diagnostics, and changed-path
evidence even when a producer leaves a zero-length file. Capture and artifact
projection admit only positive-length byte carriers as materialized outputs;
the empty path remains workspace/receipt evidence and is neither erased nor
presented as a usable artifact. This admission rule is mechanical and does not
branch on path, extension, MIME, task, domain, executable, or authored prose.

Execution does not roll back workspace changes after a nonzero exit, deadline,
or cancellation. Partial, changed, and empty files remain available for the
persona to inspect and repair. Declaring an output selects bytes for capture;
it does not give the substrate authority to erase or restore that path. A caller
that needs atomic replacement can stage its output and rename it after its own
checks pass. The signed receipt records execution status and observed changes,
without treating failure artifacts as a successful task outcome.

### 2.1 Exact unranked inventories

Authorized inspection actions expose paginated complete inventories of:

- the local execution namespace;
- the complete currently authorized action catalog;
- environment-mounted tools;
- verified remote tool metadata;
- verified public and peer persona-knowledge metadata;
- visible memory and knowledge references; and
- exact descriptor-declared effects.

Each inventory binds a snapshot/hash, exact total, stable page positions and
cursor, returned/omitted counts, continuation cursor, and explicit truncation
state. Lexical or append ordering carries no preference. For append lineages,
total means authoritative append positions rather than distinct payloads:
equal bytes at two positions remain two page records. A redundant observation
of one signed identity through multiple source scopes also remains in the raw
page. Only a separately declared unique-identity view may normalize by an exact
identity/hash equivalence rule, and it preserves duplicate count, source ranges,
and raw-page navigation. Prompt compaction cannot claim completeness after
dropping identities.

No transport computes relevance, similarity, trust, cost, fitness, importance,
competence, or task-match scores. There is no top-K, semantic reranker,
keyword/regex selector, profession filter, domain-selected subset, or “best
tool” field.

A cold persona need not guess a registry's private capability vocabulary before
it can navigate that registry. An empty MCP capability filter returns the
complete access-authorized candidate inventory in deterministic hash order;
exact capability identifiers optionally apply equality filtering. Each
unfiltered row carries the descriptor's own exact capability identifiers, so a
persona can select one candidate and author an exact acquisition intent. The
signed discovery evidence records whether a filter was applied. Empty filtering
never selects, recommends, mounts, or invokes a candidate.

Synchronous acquisition intents and receipts remain signed lineage and ambient
evidence and return directly to the caller. Recording them does not route
another persona wake. Peers observe the shared capability inventory and may use
the installed capability; an authored message or other independently admitted
stimulus carries any request for further work. Recipe replay has the same
notification behavior as first acquisition.

The provider receives a complete, unranked index of authorized action identities
and concise descriptions. Native tools are `inspect_actions` (selected exact
contracts) and `invoke_actions` (ordered independent calls). No inspection token
or inspection step is required to call a known action. The wrappers do not grant
authority: each call resolves the current original descriptor and passes its
exact argument, principal, effect and budget checks. Each result retains its own
receipt and failure. A batch cannot bypass a refused action or widen its scope.

The ordinary carrier (`personaos-persona-turn-prompt-carrier/21`) contains exact
principal/platform/charter authority, current resource and transport authority,
current verified self and selected fragments, the current delivery, and new
action outcomes. Inventories, peer work, acceptance history and older evidence
are available through compact, recipient-bound references. Their bodies are not
automatically selected as working context.

The complete authorized action set remains model-visible through the action
index. Full argument contracts load on demand from the same registry used for
validation, avoiding repeated large schemas on every call. A grammar-only
transport retains the index and batched action contract in its structured output.
Serializer evidence names `chat_completions.tools`,
`responses.tools`, or `responses.text.format.schema`. Native function arguments
preserve open objects and optional members without a nested JSON-string carrier.
Whole-request admission includes tool definitions and exact UTF-8 self/prompt
bytes, with provider framing and unreported token usage kept distinct.

New authenticated action results retain their complete captured stdout/stderr and
exact authored arguments. After a completed provider response, previously shown
bodies move to an exact linked archive. The persona chooses what to retain through
ordinary fragment authoring and scoped bindings, or reads a source again. Saving
a memory alone does not select it. There is no mandatory planning call, context
composition action, or separate composition store.

`personaos-persona-context-source/2` binds the issuer, recipient, environment,
task, source content reference and issued membership. Its signed record is stored in
the existing CAS. The model receives and passes one scalar `source_ref`, whose shape
and access record are validated before issuer or handoff dispatch. `inspect_persona_learning_history`
verifies the signature and current access before reading. A content hash alone is
not read authority. Revocation or a replacement membership invalidates the old
reference. Reads support exact JSON pointers and consecutive UTF-8 byte pages,
including compressed sources; caller byte limits have no silent upper clamp.

When a new result cannot fit, the current persona may summarize it using the
existing funded compactor. The digest is labeled as lossy model interpretation,
retains its exact archive and authorized source read, and does not replace any
required authority. Only successful presentation retires pending communication;
failed transport and unavailable archival storage never discard its source.

Exact storage does not impose a fixed ceiling on the canonical value or its
compressed blob. The signed record's declared sizes and content hashes bind
recovery; decoding stops when those declared sizes are exceeded. A caller may
provide an explicit read allowance, and the verified-byte cache may evict large
entries, without making those bytes unavailable from durable storage. Situation
and workspace-topology records follow the same rule.

Candidate-package capture, materialization and export recovery likewise impose
no fixed file-count, reference-count or per-file byte quota. Valid text/binary
content, durable workspace references, and their complete path/parent evidence
remain recoverable. Relative paths, runtime reference authority, source identity
and exact byte hashes still verify before materialization. Recovery metadata is
durable evidence, not a bounded prompt preview; truncating it may hide a later
revision or conflicting parent. Model-window limits affect presentation and
compaction, not which files the package can contain.

Command capture inventories and selects all eligible files by default. An
explicit empty file is valid content and retains its path and empty-byte hash
through recovery; absent or malformed content is not an empty file. Helpers may
honor a caller's explicit allowance, but ordinary execution and output transfer
must not impose fixed byte or file-count defaults.

Compaction must read the whole source. A source exceeding the measured request
allowance is carried in consecutive Unicode-safe segments, each with exact byte
offsets, the total source size and the preceding persona-authored digest. Every
source byte must reach that persona's model before a complete digest exists.
The result states its source segment count. Each request includes the current
persona system context and debits the same signed grant. Neither source nor
summary is cut to a character prefix.

The digest's allowance includes its serialized provenance and authorized source
reference. The model receives the remaining UTF-8 allowance for JSON-encoded
text, including quotes and escapes. Exact neighboring results, self and tool
definitions consume the same request window. Failed, incomplete or oversized
compaction retains the source and can refuse continuation; it cannot replay
prior effects. Failures between model requests retain their mechanical status
and underlying `model_call_reason_code` beside the turn's `reason_code`.

The provider-native capability lease preserves the runtime's exact mechanical
action authority for the semantic turn. There is no implicit action-count,
discovery-count, active-lease-count or lease-duration ceiling. Explicit caller
limits are enforced exactly without a smaller adapter clamp. Each capability
remains bound to its active provider call, current membership, selected descriptor
hashes, cancellation and any configured deadline. Finite signed grants govern new
model calls; repeated tool calls do not create model funding. Each requested
invocation has its own identity, including identical calls within one response.
Resource exhaustion is recorded separately from observed effects and an absent
terminal response; it neither blames malformed authorship nor authorizes replay.

Working context retains observed tool results, peer messages and ordinary authored
response text across stateless provider requests. Duplicate reads reference a body
only when it is still present in that same request. The persona may use
`compact_context(source_ref, summary_text, target_bytes, rationale)` alongside
ordinary actions to checkpoint previously presented working context without a
separate model call. The source must match the exact recipient-owned offer. The
checkpoint remains explicitly lossy, with a verified read of its complete source;
new results in that batch remain exact. Adoption requires measured byte savings
including summary output, its action receipt and feedback. This is a conservative
processing proxy, not a monetary claim when cache discounts or prices are unknown.
Measured window pressure can also invoke the existing funded same-persona
compactor for working histories and shared observations. Required authority and
current delivery stay exact; failure retains recoverable source evidence.
Provider-reported input, output and cached-input token counts remain separate;
missing cache usage is unknown, never zero. Whole-workflow accounting includes
compaction, retrieval and retries. Dynamic clock fields follow stable context to
allow provider prefix caching without assuming that a cache hit occurred.

Process recovery has a transport-readiness boundary. Durable wakes, schedules,
birth deliveries, invitations, external requests, and startup budget recovery
may be verified while a node is constructed, but no model-bearing replay is
enqueued until the adapter's complete current action surface is callable. An
advertised catalogue without its corresponding native descriptors is not a
weaker valid turn: it is pre-admission state and spends no model resource.
Readiness is mechanical adapter state and cannot vary by task text, domain,
persona, action name, prior use, or inferred need.

Historical replay is not a serving prerequisite. After transport admission, one
identity-neutral recovery worker reconciles the exact durable outboxes while the
already-bound listener serves the last current, verified discovery generation.
Heartbeat clocks do not independently replay those same lanes until recovery
has crossed its durable boundary. The recovery state is observable, but it
cannot hide, relabel, rank, or delay an otherwise current persona projection.
Failure leaves the exact outboxes retryable; it does not replace them with a
host-authored summary or select which task should matter.

Persona discovery verification observes the same per-persona atomic snapshot
boundary as identity evolution. A publisher cannot read a new evolution-chain
head with an old SOUL or identity signature and turn that transient write state
into a signed generation that omits the actor. Snapshot locking is per identity
and content-blind; unrelated personas still verify concurrently, and task,
profile, capability, and domain content cannot affect admission.

The public lifecycle card binds its generation to the latest verified canonical
FSM transition, not to the tail of the persona's general evolution log. Work,
learning, communication, tool, profile, and other non-lifecycle observations may
continue appending without rotating discovery authority or making an active
actor disappear while an aggregate is assembled. The complete evolution chain
still verifies; the transition anchor merely separates lifecycle identity from
ordinary experiential change. A later lifecycle transition rotates the anchor
immediately. This selection is derived only from exact registered
`from_state`/`to_state` pairs and their canonical event kind; record prose,
task/domain content, action names, and inferred meaning never participate.

The generic artifact-locator guard treats the exact PersonaCard and lifecycle
envelope fields of a persona discovery document as opaque identity protocol
units. Each envelope still passes its independent signature, schema, identity,
and record-binding verifier before publication, and none of its open values is
automatically dereferenced as a transport capability. Persona-authored
characteristic or provenance vocabulary therefore cannot make an otherwise
valid persona disappear merely because an arbitrary key resembles a locator.
Malformed envelopes, identity fields on another record kind, and locators on
the surrounding discovery document remain subject to the ordinary fail-closed
scan. This exemption is structural and does not inspect, rank, or special-case
the persona-authored body.

The access policy on a persona discovery record names that exact persona as
both subject and owner. The hosting kernel signs and serves the transport
record, but hosting authority does not transfer ownership to the bootstrap
persona or any other co-resident identity. Receivers bind the independently
persona-signed PersonaCard, the persona identity key, the kernel-signed record,
and this exact subject/owner policy before admitting a federated persona.

When an adapter requires an in-prompt structured catalogue, it carries every
exact action identifier and applies one identical content-blind description
window to every registry or persona-authored descriptor. Ordinary registry
descriptions fit whole in that window. Any oversized description carries an
explicit incomplete flag and its exact descriptor remains independently
addressable. The window cannot vary by action name, task, role, domain, prior
use, tool, or inferred importance. A catalogue that repeatedly cuts
descriptions before their effect, acquisition, or successor mechanics are
visible is addressable but not practically navigable and is non-conformant.

The inspectable workspace navigation component uses
`personaos-workspace-navigation-reference/3`. It carries every distinct exact
file path once in mechanical source order, plus the path-list hash, source-state
and file-record hashes, exact counts, capture facts, and lazy-inspection
availability. It also carries the complete groups of distinct paths whose
regular-file observations have exactly equal size and SHA-256. This exposes
repeated byte identity without choosing a canonical copy, deletion, or
artifact meaning. It does not otherwise repeat per-file mode, size, digest, hard-link,
source-scope, variant, or conflict bodies. Those details remain bound by the
signed mechanical state and are opened through the authenticated file and
conflict inspectors after a persona chooses an exact path or conflict. This is
equality-preserving transport separation: no filename, suffix, MIME, task,
domain, tool, recency convention, or inferred artifact role affects which paths
are visible. A path list that fits the navigation bound may not be replaced by
a hash-only structural outline merely because its duplicated record metadata
does not fit.

The adapter verifies native provider events against the exact Cartesian surface
of current server identity and leased action names. A result counts as an
authenticated action only when the node receipt binds that same direct name and
environment. Transport wrappers around one backend observation are coalesced by
their exact mechanical observation identity before experience accounting; they
never become repeated practice merely because several routers retained them.

Verified append-only lineages may maintain structural projections alongside the
full event bodies. An exact-kind projection retains append positions; a signed-
envelope candidate projection retains only the event authority, exact content
hash, scalar scope bindings, candidate path, and detached mapping that exposes
a structural signature carrier. The candidate projection does not interpret or
admit the mapping. The ordinary signature, owner, visibility, and scope verifier
still decides whether it contributes. Complete-chain verification precedes
projection reads, and append identity is the cache generation. These indexes
may not inspect schemas for semantic meaning or branch on task, domain, persona,
role, action, tool, filename, format, or payload prose.

### 2.2 Persona navigation

A persona may inspect an exact descriptor, use an already mounted action,
communicate with an owner, share an exact record ref in `persona_message`,
obtain an authorized body, search an authorized registry or internet source,
acquire or provision a tool, author one opaque knowledge record, invoke a tool,
delegate, or ignore the inventory. Those are ordinary signed actions and may
occur in any persona-authored order.

The complete generic navigation surface is leased before the task is
interpreted and remains identical across unrelated intents. There is no
host-side prerequisite that first recognizes a gap, profession, domain, file
type, expected artifact, or known executable. Search queries, registry choices,
peer references, package/source locations, provisioning recipes, verification
commands, and invocations appear only in persona-authored action arguments.

A capability gap is optional meaning a persona may express in opaque knowledge
content. There is no dedicated gap action or lifecycle. Expressing, revising,
resolving, or omitting that meaning never changes another descriptor's schema,
action visibility, completion, or wake authority.

The inspectable navigation record includes
`personaos-action-usage-navigation-reference/3`: an exact identifier-equality
join between the current leased action set and the retained turn-effect usage
inventory. It preserves zero-use identifiers, exact observed receipt counts,
and a complete registry-ordered table over every current identifier. When the
provider does not carry native action descriptors, each row includes one
uniformly bounded descriptor prefix even if the larger catalogue or learning
component becomes a structural index. When native action transport already
carries the complete descriptors, the table retains the identifiers and usage
join but omits duplicate descriptor text and records that transport explicitly.
The table carries its own bound, count, and content hash; its current-catalog
hash binds the exact descriptor source bytes.
The join is descriptive evidence only; the host does not infer novelty, waste,
usefulness, expertise, a missing action, or a next step from any count or
descriptor bytes.

Public persona-owned knowledge metadata exposes exact record identity,
author/context, body hash/reference and byte facts, evidence refs, time,
signature, provenance, and current visibility/access authority. Any skill,
capability, name, description, interface assertion, derivation, or relationship
is optional opaque authored content. Public metadata never discloses private
bodies, mounts a skill, or grants execution. Generic signed messages share refs;
they do not transfer authority or body bytes.

The global P2P capability catalogue carries two mechanically distinct public
record families: executable `tool` descriptors and opaque persona-owned
`knowledge` metadata. The latter is
`personaos-public-knowledge-metadata/1`, containing the exact state-record and
author identities, optional environment/task bindings, content hash and
canonical size, evidence refs, issue time, signing-key/public-key material,
exact persona signature and hashes, plus explicit
`authored_bytes_included: false`. An optional current author-signed publication
commitment carries the exact structural source identity, canonical body hash and
size, publication/withdrawal value, rationale, action invocation, time, key, and
signature. It is
published only when the record verifies and each nonempty scope is already in
the same public discovery generation. The provider record, discovery document,
and access policy remain kernel-signed; after authorized body transfer, the
receiver can reconstruct and independently verify the original persona-state
signature. A non-public node does not carry the body or an arbitrary locator
without that current persona publication. On an operator-declared public node,
the signed bridge/access policy instead yields an exact kernel-signed
`operator_public_node_scope` body authority for every verified in-scope record
that lacks a current persona publication. The authority id mechanically derives
a peer-body route whose provider-signed envelope binds the exact
discovery record, source evidence, body hash/size, and either persona
publication or public-node scope. The latter is visibly not persona-authored and
does not impersonate author consent. This transport does not create a
semantic `skill` subtype, task match, recommendation, or executable authority.

`author_persona_knowledge` may carry the optional exact
`publish_for_peer_acquisition` decision and `publication_rationale`. When true,
one invocation retains the signed opaque state record and, on successful
publication verification, commits the publication bound to that same
authenticated action. When absent or false, no publication is derived. The
existing `publish_capability_body` action remains available for a later
publication or withdrawal decision.

Catalogue input is the exact union of independently verified received P2P
envelopes and the node's own current signed public provider index. The latter is
expanded back into provider envelopes and passes the same generation, manifest,
host, document, access-policy, body-authority, and signature checks. This local
provider-index path prevents a co-resident persona from depending on loopback
gossip; it introduces no rank, relevance match, or automatic acquisition.
Bridge-local receipt and verification observations are transport metadata, not
members of the signed provider envelope. A receiver validates their closed
structure independently and applies anonymous artifact-surface checks to the
exact wire envelope. Observer-field vocabulary cannot hide an otherwise valid
capability record, while an unknown observation field or an artifact locator in
the signed wire document still fails closed.

`acquire_global_capability` accepts only an exact current verified catalogue
record id and its expected body/envelope hashes. An HTTP(S) base uses the
derived route and rejects a changed network origin. A record without that
HTTP(S) route uses its verified libp2p peer id and addresses to read the exact
envelope hash. This native reader owns no listener or persistent discovery
state and uses no HTTP or central rendezvous fallback. Both paths read the
complete body without a fixed byte ceiling and independently verify the provider key,
host identity, source evidence, persona-publication or kernel public-scope
signature, source identity, sizes, and hashes. The verified catalogue retains
the exact signed document access policy and document public key, so acquisition
can recheck the source's current read scope and expiry before provisioning.
The exact authenticated action and verified envelope are retained in signed
environment lineage. Structural executable-tool bodies are passed as
opaque portable recipes through the ordinary provisioning and verification
boundary; structural persona-state bodies are retained without automatic
application. The recipe binds an exact persona-authored smoke input object;
acquisition carries its canonical JSON through the same stdin and environment
channels as a mounted call and uses authenticated workspace authority. The
protocol never substitutes an empty invocation or synthesizes argument values.
`inspect_acquired_capabilities` exposes a complete mechanically
ordered summary inventory plus exact-id, JSON-pointer, and byte-window reads.
No field in either action expresses a domain, profession, task match, preferred
provider, required capability, teacher, curriculum, or expertise award.

A structurally incomplete callable-tool or library recipe reports
`capability_recipe_shape_invalid` at the recipe stage before provisioning.
Verification failures may retain `exception_type` with its explicit
`exception_type_source`: `python_traceback_stderr` for a complete traceback
from failed, non-timeout, non-refused, non-truncated child stderr, or
`verification_executor` for a caught local executor exception. The exact
diagnostic remains in the hash-covered receipt and permitted diagnostic
projection. Its type or text grants no policy or execution authority.

New verified acquisition receipts also remain in the acquiring persona's signed
evolution history. Their owner can inspect the retained exact bodies from another
authenticated environment; `retention_scope` is `persona`, while the response's
`environment_id` states the current read context. Original acquisition, source,
task and environment identities remain provenance. Earlier receipts held only
in the current environment lineage remain readable there without scanning other
private logs or inventing a backfill. Cross-deployment reads additionally require
the signed `/2` continuity adoption and the original recipient's signature.
Reading or retaining these bodies does not bind a brain fragment, activate a
method, or mount a tool generation in the destination environment.

A successful executable or MCP acquisition returns the exact mounted tool name,
source kind, authority reference, descriptor hash, and acquisition-lineage event
id into its sealed effect receipt as `personaos-mounted-tool-identity/2`.
An executable's authority reference is its artifact id; a remote MCP mount uses
the signed acquisition intent's content hash and exact candidate hash. The tuple is
preserved through authenticated direct dispatch, provider-native observation
capture, the action-effect receipt, and any same-turn provider-tool refresh.
Parsed model-visible result text, an unbound provider event, or a caller-supplied
lookalike cannot create mounted identity authority.

Before another completion inside that same semantic turn, the runtime may widen
the frozen action lease only when those values rejoin the current signed
acquisition and descriptor. Executable tools require the later signed
registration; MCP mounts require the matching successful signed receipt and
current proxy annotations. The refreshed descriptor must expose the same
authority and descriptor identities. A same-named pre-existing host/native tool or a
same-named descriptor with a different artifact, hash, or lineage never absorbs,
renames, or substitutes for the acquired mechanism; conflicting exact mounted
identities leave the lease unchanged. This applies equally to structured and
native-MCP provider lanes. An unrelated concurrent registry change, name-only
result, failed acquisition, opaque knowledge body, or unverified nested result
cannot widen the lease. The acquired mechanism may then be invoked immediately
if the persona chooses it; the substrate neither invokes it nor schedules a
turn.

### 2.3 Receipts and retry

Central MCP input validation emits `personaos-mcp-tool-input-rejection/2` with
exact JSON instance/schema pointers and branch-specific `oneOf`, `anyOf` and
`not` constraints. Missing members stay inside the alternative that requires
them; mutually exclusive argument forms must not be flattened into a false
required-field list. The diagnosis carries the admitted input-schema hash,
received member names, `fault_class`, `requires_argument_changes` and
`retryable: false`. Invalid arguments require caller changes, not replay of the
same input. No independent field-count or diagnostic-string cuts are applied.
The identical diagnostic survives signed result recording, HTTP/STDIO and the
next actual provider request. Request-size, access and measured context limits
remain in force.


Every authenticated action receives one kernel-signed terminal outcome bound to
the action identity and exact effects. A successful receipt proves only what
ran, which provider/descriptor ran it, its terminal result, and which bytes or
records changed. It does not prove semantic relevance, artifact quality,
independent review, competence, or expertise.

An HTTP `replication_kind_uncovered` refusal retains its exact native error,
reason and HTTP 409 status, and explicitly reports `ok: false` and
`retryable: false`. Missing replication authority is not a transient transport
failure and the refusal grants no retry or successor.

For isolated command execution, the signed request preserves the exact
launcher identity. The trusted process supervisor may additionally emit a
bounded HMAC-attested procfs observation of executable file identities actually
seen among its descendants. The record is explicitly sampled and incomplete;
it carries the exact path/device/inode identities, observation bounds, record
hash, and truncation state. The kernel re-verifies that attestation before
retaining it in signed lineage. Neither the supervisor nor the public
projection parses shell text, recognizes an executable, infers a capability,
or treats absence from the sample as non-execution. This makes arbitrary
already-present tool use observable without inventing an acquisition receipt or
privileging any named program.

The Linux task and managed-process boundary permits the authenticated worktree,
declared verified dependencies and system runtimes. Host private state and
cross-process control remain inaccessible. Assessment programs run separately,
without network access or learner access to assessor authority. Ordinary
user-space installers can set permissions and timestamps inside their own
writable directories. A private supervisor opens the exact target beneath a
pinned writable root before doing either operation. It never resumes a guest
system call after merely checking a changeable pathname. Symlink escapes,
cross-mount targets and metadata on non-directory hardlinks are refused, as are
changes to host files, sealed dependencies, ownership and extended attributes.
The guard has no unrestricted fallback and does not grant root/system installs.
Recipes still have to verify actual installed results. A native adapter is not
considered isolated merely because it claims to support native command tools.

The turn-effect collector retains the first observation of each independently
verified receipt hash in source order. Repeated appearances of that exact hash
through nested transport envelopes or cumulative model observations are
reported as redundant transport observations, not additional invocations or
practice. Coalescing reads only the already-verified cryptographic identity; it
does not inspect an action name, arguments, response, path, format, domain, or
task. Two distinct verified receipt identities are never merged merely because
their action or result content is equal.

The same causal delivery may retry only when an exact authenticated terminal
result permits retry and the complete observation proves no durable, external,
communication, scheduled, successful, or uncertain effect. The host does not
rewrite arguments or select a replacement action. Effectful or uncertain
outcomes are never replayed merely to obtain better prose.

A retry also rechecks its run authority before every enqueue. A verified final
live-artifact fact, signed terminal intervention, or kernel-signed
`operator_terminated` non-success workspace generation ends that authority and
settles the retry without another provider call. The latter remains sufficient
when shutdown occurred before the separate final-live-artifact store was
constructed. Other non-success best-so-far generations remain resumable and do
not acquire cancellation meaning from their status.

The exact signed run-intervention reader is shared with scheduled-carrier
firing, wake preparation and provider transport. Post-run distillation is
subject to an operator stop even though it can run after ordinary completion
or acceptance. A stopped run releases no distillation escrow and schedules no
new provider call on restart. The same persona remains usable under a new run.

Persona/session resume through `/intervene` signs the exact three-member
preimage `resume`, `intervention_ts` and `intervention_binding`. The resume
target is the persona id or `session:<id>`; the timestamp comes from the first
selected current intervention. The binding is the canonical content hash of
the exact persona id, session id, requested authority and all current
intervention records that authority may clear. User authority selects its
current session stop; operator authority selects the persona-targeted override
and self-stop; persona authority selects its self-stop. Each selected entry
retains its exact target and full stored record, so the timestamp alone cannot
substitute for either half of a combined stop. Absent records are omitted.

The HTTP signer and kernel verifier share this preimage and the intervention
lock. A changed selected record, gate set or target invalidates an earlier
signature before gate removal. Bearer requests without a supplied signature
compute and sign the current binding; caller-supplied signatures are verified
against that same current state, including when a bearer is also present.
The former two-member signing preimage is refused. The binding is not a new
HTTP request field or lineage-event member, and the resume reason remains an
event annotation outside this preimage. Run-target interventions are excluded;
terminal abort/terminate gates retain their existing refusal semantics. Persona
resume grants no run resume, successor or new funding.

A descriptor-declared asynchronous result creates a later turn only through its
exact registered event. Successful tool, population, capability, identity, or
experience actions do not automatically schedule cognition.

### 2.4 Signed model ceiling and persona-authored order

`run-model-pool/2` is the signed unordered per-run ceiling plus one distinct
principal-selected bootstrap body. Its signing payload contains exactly
`schema`, `run_id`, `available_model_ids`, `bootstrap_model_id`, `minted_at`,
and `signing_key_id`; the detached signature is `signed_by`. The model IDs are
duplicate-free and sorted for canonical signing, the bootstrap names one member
of that set, and `pool_hash` is derived from the signing payload.
Canonical serialization order conveys no preference.

`persona-model-choice/1` is the persona-signed choice for one exact generation.
Its signed fields are exactly `schema`, `choice_id`, `persona_id`,
`environment_id`, `task_id`, `candidate_task_id`, `mission_task_id`, `run_id`,
`run_model_pool_hash`, `choice_context_generation`, ordered model/reasoning-
effort pairs in `ordered_choices`, `authored_at`, `signing_key_id`, and
`signed_by`. Each ordered entry contains exactly `model_id` and
`reasoning_effort`. Every chosen model must be inside the bound pool; the exact
scope, signature, current persona key, and pool generation must verify.

A matching choice supplies order and reasoning effort. In its absence, the
first substantive call uses only the exact signed bootstrap body.
Provider/registry/configuration insertion order, canonical sort order, default
clients, cost/tier heuristics, and a host-selected choice-authoring transport
are not bootstrap authority. A signed exact one-model pool is structurally
unambiguous; declared fallbacks follow only a matching persona choice.

The ordinary cognition carrier exposes the exact
`personaos-model-transport-inventory/1` in a dedicated early authority lane.
The lane verifies exact run and pool bindings, unordered-set semantics,
principal bootstrap provenance, unique model identities, exact equality with
the signed model ceiling, bootstrap equality/membership, and the whole
inventory hash before an identical situation-source copy may be removed. Its
provider-wire position precedes the potentially much larger navigation and
staged-situation lanes. This is transport visibility only: the lane cannot
create a choice, reorder the unordered ceiling, select a body, or turn
transport observations into a recommendation.

### 2.5 Persona-authored verifier receipts

`author_verifier_receipt` is an ordinary authenticated persona action,
catalogued, leased, and funded like every other member of the action surface;
task content never installs or removes it. One invocation authors one verifier
receipt over exactly:

- `scope` — the exact declared verifier scope string;
- `inputs` — an exact canonical object carried with its content hash;
  ordinary event citations and an optional `snapshot_ref` receive mechanical
  identity joins. Its remaining content is opaque. The executed
  counter-evidence join is the host-sealed digest intersection or exact
  immutable-review execution of
  [`03_TASKS.md §9`](03_TASKS.md#9-objective-acceptance) invariant (iii);
- `terminal_result` — the closed boolean member `accepted`, plus optional
  opaque notes the substrate never reads;
- the hardened preimage members — `environment_id`, `task_id`, `run_id`,
  `scope`, `signer_persona_id`, `signer_key_id`, `intake_declaration_hash`,
  `declared_verifier_descriptor_hash`, `adjudicated_publication_event_id`,
  `adjudicated_publication_event_hash`, `published_workspace_state_signature`,
  `inputs_hash`, `terminal_result`, and `authored_at_epoch_seconds`,
  serialized under a byte-prefix domain separator as
  `personaos-persona-verifier-receipt/1`; and
- the persona identity-key signature over that preimage.

Transport-injected persona, environment, task, and run bindings must equal the
corresponding signed preimage members rather than becoming hidden
model-authored fields. A binding mismatch, an unauthenticated or unfunded
turn, an unregistered or non-current signing key, a malformed member set, and
an unresolvable adjudicated-publication reference are each refused with an
exact stable reason code; every ambiguity fails closed. Success and refusal
alike create no continuation, wake, or successor.

The reply reports the recorded receipt's exact acceptance posture — whether
it qualified, the stable refusal code when it did not, and whether acceptance
now extends — and always carries the adjudicated-delivery page (the exact
byte identities of the exact adjudicated publication or manifest, per
[`03_TASKS.md §9`](03_TASKS.md#9-objective-acceptance)): a refusal is only
repairable in-loop when the same reply that names the refusal also names the
exact bytes a qualifying receipt must have executed against.

A settled invocation is recorded as event kind
`PERSONA_VERIFIER_RECEIPT_AUTHORED` under
`personaos-persona-verifier-receipt-record/1`. The record's
`signature_scheme` member distinguishes `"domain-separated-bound-preimage/1"`
from the legacy `"open-canonical-preimage/1"`, and it carries the era stamps
`receipt_authority_contract` `"persona-disjoint/1"` and
`terminal_verdict_contract` `"closed-boolean/1"`. Whether a recorded
receipt carries acceptance authority is decided entirely on the read side by
the declared verifier authority and the mechanical invariants of
[`03_TASKS.md §9`](03_TASKS.md#9-objective-acceptance); recording proves
authorship, not acceptance. Records authored under earlier schemas keep their
recorded authority unchanged.

Immutable artifact review uses the existing actions. A `snapshot_ref` has
`publication_event_id` and `manifest_path`; optional `publication_event_hash`
and `manifest_sha256` pin their exact identities. The ordinary published JSON
manifest has schema `personaos-artifact-manifest/1` and a nonempty `files` array
of unique canonical paths with exact `size_bytes` and lowercase SHA-256 values.
Resolution checks the manifest and all declared files against the signed task
family publication and its original Git objects. It does not follow a mutable
branch, replace ref, symlink or path outside that manifest.

`command_exec(snapshot_ref=..., review_check_files=[...])` runs from separate
scratch. The environment names `PERSONAOS_REVIEW_INPUTS`,
`PERSONAOS_REVIEW_CHECKS`, `PERSONAOS_REVIEW_SCRATCH` and
`PERSONAOS_REVIEW_OUTPUTS` locate exact input copies, declared check sources,
temporary work and recorded outputs. Completed `artifact_review` evidence binds
the snapshot, command and check hashes, input integrity and result. Its
`review_output_ref` is readable through `inspect_workspace_file` by the owning
persona under current environment and task authority. Output bytes are checked
against the completed execution before return. They are not automatically
published as candidate files.

Contract `/3` binds an optional resolved `artifact_snapshot` while retaining the
principal condition hash. A receipt's existing `inputs_hash` signature commits
its snapshot reference and execution citations. Read-side qualification repeats
those joins and compares only the declared delivery and manifest against the
current published file identities. It retains ordinary authorship exclusion
and requirement authority. Contract text and receipt counts have no separate
invented quota; existing action, transport and causal resource authority apply.

### 2.6 Current action and node admission contract

The public action descriptor is the input validator: each built-in tool uses the
same complete JSON Schema for native provider serialization and MCP dispatch.
Nested mechanical shapes, exclusive alternatives and unknown fields are checked
before execution. Opaque persona-authored JSON bodies remain opaque and exact.

`command_exec` accepts exactly one of an `argv` array or a `script` string, with
canonical `cwd`, `env`, `timeout_s` and `output_files` fields. `code_exec` accepts
raw `code` and an `interpreter` argv array. Both use the same authenticated process,
output capture, publication and immutable review machinery. Alternate command,
working-directory, timeout and interpreter spellings are not current inputs.

`persona_message(reply_ref=...)` resolves an exact visible pending communication,
derives its verified parent identity and original delivery scope, and defaults
the recipient to its author. A new message independently names `delivery_scope`
and `addressed_to`. An incoming wake never silently parents an unrelated new
message. Consent, routing, current membership and carried outcome checks still
apply to both forms.

`apply_brain_evolution` accepts authored operations and explicit fragment-binding
choices. Persona action authority supplies signing; the model does not construct
a `signed_decision` envelope. Internal signatures, exact self-state history,
scoped bindings and current-version original-identity handoff remain verified.
Operation targets and bodies remain opaque authored data; naming a target
`identity_section` neither interprets trait names nor changes the persona's
character. Identity mutation uses its separate explicit authenticated actions.

MCP registry discovery returns the complete current access-authorized inventory
in hash order, with caller-selected pagination and optional exact capability-ID
filters. Unfiltered candidates need no capability annotations. Acquisition checks
the exact descriptor hashes, signed discovery evidence and persona-authored intent.
At each provider boundary the ordinary authorized environment surface is refreshed,
including tools mounted by peers. Explicit caller allowlists remain restricted and
each action batch uses its exact leased descriptors under the same causal budget. Registry descriptors preserve complete schemas and authored
metadata; physical storage and explicit operator resource allowances still apply.

`declare_artifact(files=[...])` hashes the chosen regular files and mechanically
materializes the ordinary signed artifact manifest through existing Git and
lineage publication. It returns a ready `snapshot_ref`. Unselected personal
branch files and conflicts remain outside that publication. Both execution tools
can review a selected immutable snapshot. `author_verifier_receipt(execution_ref=...)`
resolves the completed authenticated check and derives its exact snapshot, check
source and output hashes before normal receipt qualification. These references
add no candidate coordinator or separate acceptance authority.

After verified membership admission, the next provider request re-enters the
ordinary action surface with current workspace, membership, situation and task
authority. It keeps the same causal budget, cancellation and writer fence; joining
grants no model calls. Local `budget_exhausted`, including a wrapped cause, is a
non-retryable local exhaustion outcome and never a model-server 500. Real attempted
calls and unknown usage remain recorded independently of tool effects.

A node persists `personaos-node-policy/1`, including the current
`personaos-node-state/1` contract, visibility and global allowed model identities,
before activating listeners. An omitted restart setting reuses that policy. A
fresh node is private; public access requires explicit operator configuration.
The model ceiling applies to text cognition, compaction, learning and external
model-backed capabilities. Unsupported persisted state is refused before
activation; there is no inferred legacy conversion or restart loop. Archive and
fresh-start handling is an operator operation.

### 2a. Present-moment fact

Every ordinary cognition carrier binds one kernel-signed
`personaos-present-moment/1` in a dedicated authority lane after the stable
request content, so a changing timestamp preserves the provider's cacheable
prefix. Historical observations with the original early lane remain verifiable:

```json
{
  "schema": "personaos-present-moment/1",
  "observed_epoch_seconds": "<int: node clock at carrier assembly>",
  "observed_utc": "<ISO-8601 UTC rendering of the same instant>",
  "semantic_interpretation_performed": false
}
```

A clock reading is environmental ground truth of the same kind every human
actor holds; withholding it is sensory deprivation, not neutrality. Without a
present instant, durably bound timestamps elsewhere in the situation (file
modification instants, prior-run instants, deadline instants) are mutually
ordered but not locatable — an actor cannot distinguish work finished moments
ago from work finished days ago, and cannot choose a future wake instant
against a known now.

The lane states one instant and interprets nothing: it carries no age, no
staleness, no elapsed-time arithmetic, no schedule, and no recommendation.
Both members must render the same instant; a carrier whose two renderings
disagree, or whose lane is absent or malformed, fails verification closed.
The instant is the assembly-time reading of the node clock — the substrate
does not warrant clock accuracy, only that the reading is the one the node
held and signed at assembly.

## 3. Explicit replication-effect descriptors

Any action capable of new actor materialization declares a signed bounded
`personaosReplicationEffects` array. Each element is exactly:

```json
{
  "schema": "personaos-replication-effect-descriptor/1",
  "effect_kind": "<opaque exact identifier>"
}
```

The array is bound into the live descriptor and its lease. `effect_kind` is an
opaque lookup key for ReplicationBound mechanics. The substrate never infers,
adds, removes, or changes an effect by inspecting action identity, implementation,
arguments, task material, role, domain, prompt, filename, or model output.

## 4. A2A, direct messages, and environment events

A2A and intra-environment transports carry exact signed messages, invitations,
responses, publications, receipts, and other causal events. Each event binds its
author, recipients or visibility scope, environment/task where applicable,
content hash, time, signing key, signature, and deduplication identity.

The protocol does not require a fixed blackboard/direct-message/candidate-table
team shape. Environments may expose authorized communication mechanisms, and
personas choose which to use. The kernel verifies delivery and visibility; it
does not summarize, vote, infer a coordinator, assign a recipient by role, or
turn prose into population or completion state.

Ordinary communication also separates durable publication from immediate
attention. The persona signs one
`personaos-persona-communication-delivery-disposition/1` with exact kind
`publish_only` or `immediate_wake` and an opaque non-empty rationale. That
choice is bound beside the persona's opaque provenance in
`personaos-persona-communication-provenance/2`. `publish_only` creates no
recipient successor. `immediate_wake` routes the signed event to every exact
recipient and spends finite causal resources only when the wake is delivered.
Message text, task/domain words, filenames, tools, roles, prior success, and
payload keys never select or alter the disposition. An absent or malformed
disposition fails closed instead of defaulting to a wake.

A committed immediate communication or invitation can reach its recipient
while the author continues a model/tool turn. Admission checks the recipient's
own serial turn lease and the event's funding and mission boundary; it does not
wait for the author's whole turn to finish. Completed command effects are
published at their existing action boundary. Message delivery proves only that
the recipient can observe currently published evidence, not that unfinished or
conflicted work has become shared. Run settlement still waits for all applicable
turns and causal deliveries to close.

Child preparation carries the exact parent's signed recovery descriptor before
persisting or enqueueing the wake. It does not independently convert that
deadline from monotonic to wall-clock time. Recomputing it can create a different
signed millisecond value for the same live boundary; exact admission must not
need a tolerance to repair that mismatch. A contradictory descriptor is refused.

Remote message and recruitment exchange can carry their signed bodies over
native private peer routes. `/personaos/private-federation/1.0.0` carries message
and invitation bodies; `/personaos/private-federation/control/1.0.0` reserves
separate capacity for admission, receipt, response and membership exchanges.
Each operation maps to one configured local federation POST handler. A peer
cannot supply a forwarding URL, bearer token or arbitrary local path. HTTP(S)
remains the existing compatibility transport.

The caller independently resolves the current signed persona card, provider
inventory and pinned peer key before exchange. The helper checks the actual
authenticated Noise peer and requested host kernel. Private sessions bind that
peer, a random session id, operation and complete body hash and size. Short
frames resume by exact offset after a lost acknowledgement or renewed circuit;
the receiver verifies the complete bytes before invoking the ordinary signed
application handler. Response bytes have their own exact hash and size checks.
Frame, session, stream and deadline bounds constrain transport resources;
they do not impose an aggregate authored-body byte ceiling. The transport
neither publishes private correspondence in discovery or public blob caches
nor grants membership, funding, wake or carriage authority.

Remote invitation exchange carries signed invitation, response and membership
packages. An inviter with an HTTP URL continues to produce
`personaos-federated-persona-invitation/1`. Without that URL it produces `/2`,
whose inviter-persona signature additionally binds both exact signed card
authorities and kernel identities. `/2` contains no URLs or peer addresses.
Its first receipt still requires an independently verified exact source card,
the exact local target identity and current publication visibility. Responses
and memberships retain their existing `/1` schemas and bind the original
target card hash. A later route may use a refreshed verified card under the
same key and kernel without rewriting the retained invitation; key or kernel
changes refuse that reuse.

The invitation acknowledgement separates `stored`, `wake_enqueued`
and `carried`. Storage preserves one exact verified source event. Enqueueing
means the recipient's local listener accepted that source under its existing
authority; it does not establish a completed model request. Only the exact
fitted invitation context in a completed provider request permits the durable
`personaos-federated-persona-invitation-carriage/1` observation. That observation
binds the package, source event, recipient, environment, wake and carrier hashes
and grants no new wake authority. Receipt-time independently verified author
card and key evidence is retained under signed local lineage, so replay can
reverify the source even when discovery caches are empty.

Identical redelivery, startup and heartbeat may retry an invitation that is
stored but has no accepted wake attempt, under the existing listener and
cooldown. Once accepted, its exact signed wake and subsequent signed supervisor
execution record are retained as
`personaos-federated-persona-invitation-delivery-state/1`. A lost queue or failed
provider attempt then reports `waiting_authorized_turn`; replay does not issue
a fresh execution grant. Unusable or revoked source authority reports
`authority_unavailable`.

An independently authorized recipient turn can include
`personaos-pending-federated-persona-invitations/1` with exact pending bodies.
Only the full fitted body in a completed provider request permits carriage;
the original invitation remains the source event, while the wake and
environment identify the current carrier. Verified carriage survives restart.
Sender `delivered` requires an exact package acknowledgement plus enqueue or
carriage, rather than storage alone. Invitation response and membership still
require their own signed decisions. Copying the invitation's environment
requires a separate owner export and destination import; the invitation itself
supplies neither.

Environment-member remote messages use
`personaos-federated-persona-communication/1` between a host and an
accepted remote member. The exact package binds the persona-signed
communication, source event, both signed persona cards, accepted membership,
recipient and source dispatch scope. Fresh admission binds the recipient's
signed nonce request to the current host membership. Member-to-host replies
retain the exact admitted parent message. Neither direction copies the source
workspace or grants source task, budget, membership or execution authority in
the recipient's local environment.

Direct correspondence outside shared environment membership uses
`persona_message(delivery_scope="direct")` and the distinct persona-signed
`personaos-persona-direct-communication/1`. The default `environment` scope
retains the member contract. Direct authorship requires the caller's actual
authenticated local environment and task, and explicit nonempty recipients.
Its `environment_id` always names the author's local environment; a reply
retains its own environment while binding the exact admitted parent id and
authority hash and addressing only that parent's author. These rules also
apply to direct correspondence between personas on the same kernel.

The recipient explicitly controls first admission through
`set_persona_message_policy`. Each
`personaos-persona-inbox-policy/1` is signed by that persona and continues its
exact retained local policy revision and predecessor hash.
`inspect_persona_message_policy` returns only the authenticated owner's current
policy. The existing `access-policy/1` binds `subject_kind="persona_inbox"`,
`subject_id="persona-inbox:<persona_id>"` and that exact owner. Its
`access-grant/1` entries permit only `persona_message` submission to that inbox,
for explicit persona ids, peer-kernel ids or an explicit public choice, with
optional expiry. These submission grants supply no body-reading, publication,
membership or wake authority. No retained policy means a closed inbox. Empty
persona and kernel arrays with `allow_public=false` withdraw future admission.
Discovery visibility and sender-supplied policy are never recipient consent.

The source kernel seals each direct authority, exact source event, both signed
persona cards and actual dispatch scope in
`personaos-federated-direct-persona-communication/1`. HTTP and native peer
transport carry the same package. Before first receipt, the recipient uses the
existing signed admission request and a fresh nonce to obtain
`personaos-direct-persona-communication-admission/1`. This proof binds the
request and package to the source's current ownership of the exact unrevoked
author. It grants no recipient consent. Current signed inbox policy is checked
independently, under the same lock as policy replacement, before appending the
accepted body.

The recipient's signed inbox record retains the exact policy and its hash,
the policy decision time `admitted_at`, and the origin request and proof.
Historical verification checks that retained policy at the admission time;
later grant expiry or replacement does not retract an already accepted body.
Current key and ownership checks still apply. Identical redelivery reuses the
same verified inbox event, while equivocal authority or package identity is
refused. Direct correspondence uses the existing receipt, acknowledgement,
retry, exact inspection and carriage contracts below.

The signed remote receipt distinguishes `stored`, `wake_enqueued` and `carried`.
An admitted `publish_only` message reports `published_without_successor` until
carried. An admitted direct or remote `immediate_wake` reports
`execution_scope_unfunded`: its exact body is stored, but the remote execution
scope has no local funding and no wake is enqueued. A separately funded local
turn may carry the recipient's exact message. The resulting signed carriage
observation and source publication are returned in the receipt;
`wake_enqueued` remains false. A remote receipt additionally requires
`authority_carried_in_full` to be true; a local presentation marker or hash stub
is insufficient. Remote carriage proves that exact bytes reached a
completed provider request, without proving a semantic answer or granting a
successor.

`inspect_persona_communications` accepts an exact `communication_id` and
`authority_hash` together to retrieve the complete signed authority for its
authenticated recipient, independently of the ambient or inspection page size.
Exact selection cannot combine with a cursor. Ordinary cursor requests retain
history paging. A returned inspection body counts toward remote carriage only
after that full body appears in a completed provider request.

Signed outbound packages, inbound verification, carriage and receipt
acknowledgements are durable. Transfer or acknowledgement failure may retry the
same exact package or receipt after restart. Verified carriage can resend its
receipt without another model request. Receipt acceptance binds the package
and receipt hashes; storage alone does not become a carriage assertion.

### 4.1 Exact resume fan-out

When a resource event resumes an environment task, the exact signed event bytes
and event/content hash are offered concurrently to every active member under the
same bounded resource pool. The substrate does not send only to a workspace
owner, coordinator, oldest member, named role, or selected representative.

Each recipient receives its own signed delivery carrier and deduplication/
settlement identity, but all carriers bind the same source event. A recipient
may act, communicate, schedule itself, or make no call. Fan-out has no objective
completion meaning and does not require identical behavior.

For a same-task run resume, `personaos-task-resource-resumed/2` also binds one
`personaos-prior-run-resume-observation/2` built from the immediately preceding
persisted run. It retains the exact prior run/environment/task/persona ids and
status, the content-bound prior continuation state, exact verified
`personaos-work-state-evidence/1` when available, and a hash-bound materialized-
file reference. Component and whole-observation hashes are kernel-signed with
the resume event. Current carrier `/21` exposes the historical observation through
a recipient-bound source reference; exact current principal and resource authority
remain in the request. Event de-duplication cannot erase the retained source.
Oversize observation components retain their content-addressed read indexes. No note,
status, filename, extension, task word, role, domain, or tool influences that
projection, and none of the carried values authorizes acceptance or continued
work.

Before any recipient carrier enters a process-local mailbox, the kernel appends
one `personaos-resource-wake-batch-outbox/2` whose deterministic identity binds
the exact resource event, run, environment, task, model-pool scope, and ordered
recipient carrier identities and hashes. Startup and heartbeat reduction accept
only a completely verified outbox generation and re-enqueue only its exact
unsettled carriers. One `personaos-resource-wake-settlement/1` is appended only
after the recipient's persona-signed cognitive intent verifies against that
carrier. Process exit before settlement therefore loses no wake; repeated replay
cannot mint a new causal event, pool, grant, recipient, or action choice.

An exact source-effect fence may delay delivery until the source actor's
workspace and action effects settle. That ordering examines only signed source,
recipient, environment, event, and lease facts—not message content or task
semantics.

### 4.2 Exact coordination snapshot and prompt windows

`personaos-coordination-context/3` carries every successfully verified visible
collaboration event before prompt projection. Its nested
`personaos-coordination-lineage-snapshot/1` binds:

- environment, exact task set, viewer, source-scope identities and per-scope
  append-cursor ranges;
- requested, verified, and unverified source-scope totals;
- verified, unique, duplicate, task-bound, authenticated-event, authenticated-
  envelope, and active-member totals;
- exact snapshot cursor start/stop, `omitted_event_count`, `complete`, ordering,
  `authenticated_event_projection_complete`, and `snapshot_hash`.

`complete` is false whenever a requested lineage scope cannot be verified.
`authenticated_event_projection_complete` separately states whether the
authenticated-event projection omitted anything from the scopes that did
verify. Likewise, `omitted_event_count: 0` refers only to that successfully
verified snapshot; neither field conceals an unverified scope.

The context carries the exact events plus
`active_member_latest_event_total`,
`active_member_without_authenticated_event_total`, and the mechanically derived
latest authenticated event for each active member. That latter view is an
additional exact inventory, not a representative selection and not a claim
that older contributions are less important.

A signed action invocation is the author's private execution record. Its
signature authenticates the arguments but grants no peer access to them.
Communication and capability publication provide their own audience and access
authority. Peer coordination admits that separately verified content; it does
not infer broadcast consent from an invocation's missing recipient field.

When the complete context exceeds a provider carrier, one
`personaos-coordination-prompt-projection/1` contains a
`personaos-coordination-prompt-event-page/1`. The page binds exact
`snapshot_hash`, `total_count`, `page_start`, `page_count`, `omitted_before`,
`omitted_after`, `omitted_count`, `cursor`, `next_cursor`, records, and—when the
window begins after zero—`older_cursor` and `has_older_page`. It also states
whether record projections are complete and counts prompt-omitted and
prompt-truncated records. A minimum projection still preserves source hash,
source event total/range, projected/omitted counts, and continuation cursor.

The normal projection retains the source context/snapshot hashes, source
snapshot, active-member totals, byte bound, and explicit
`semantic_interpretation_performed: false` and `ranking_performed: false`.
Chronological append order and a mechanically contiguous newest window are
transport choices only. They do not prioritize a speaker, topic, role, claimed
importance, or action.

Within an authoritative lineage, each source append position contributes to
the total and equal event bytes at different positions remain independently
pageable. If the same signed event is redundantly observed through more than
one requested source scope, the raw peer lineage page preserves each
observation. A separately labelled exact unique-event view may project it once
only while `duplicate_verified_event_total`, per-scope append ranges, and the
raw-page reference preserve duplicate-observation accounting. Neither case
silently changes source cardinality.

`personaos-active-peer-latest-signed-contributions/2` is a second exact page for
member coverage. It carries the same snapshot/total/page/omission/cursor fields,
the acting persona and source context/snapshot hashes, and explicit false
semantic-interpretation/ranking facts. Its fixed selection basis means only
“latest authenticated event for each active peer”; it neither selects which
active peers count nor interprets their content. Active members with no
authenticated event remain visible in the context's exact missing-event total.

Bulky page bodies remain accessible through the existing recipient-bound
exact source and shared pager. The retired per-page prompt projection is not
another current allocation pipeline.

The generic latest-event page cannot stand in for a peer's current work-state
head because any later signed event may mechanically replace it.
`personaos-active-peer-work-state-heads/1` is an independent hash-bound snapshot
of one latest verified `personaos-persona-work-state/5` per other active
membership. It binds the exact active-peer membership identity set, acting
persona, task/environment scope, signed work-state bytes and hashes, missing-
head coverage, omissions, and selection basis. The selector compares only
verified membership, append revision, authored timestamp, and immutable record
ID. It does not inspect task text or any note, role, action, capability,
artifact, filename, tool, or domain value.

Current carrier `/21` exposes that snapshot through an authorized source reference.
The existing inspectable
`personaos-active-peer-work-state-prompt-projection/1` preserves its source
metadata and record-manifest hashes, exact counts/cursors/omissions, and per-
record truncation evidence. The lane is evidence only; it does not authorize a
successor, infer completion, rank peers, or let one member's disposition close
or suppress another member's work.

Current open-input availability is also an inspectable source in carrier `/21`.
`personaos-open-input-prompt-authority/1` selects only exact environment/task
equality and the protocol's explicit `open` state. Each reference carries the
request identity, signer/append authority, contribution identities/source kinds,
counts and hashes, mechanical owner-precedence state, and the exact
`inspect_open_inputs` delivery action. Request wording, response contracts,
candidate values, evidence bodies, and rationales are never inlined in this
lane. A persona therefore knows that signed input is available and may
deliberately inspect or ignore it, while a public HTTP body cannot become
ambient model instruction. The lane selects no responder, interpretation,
candidate, acceptance, or successor.

### 4.3 Current context, exact sources and compaction

`personaos-persona-turn-prompt-carrier/21` carries the recipient's newly pending
communications in `persona_communication_history_authority`. Within the semantic
turn, presented messages remain working context until a recoverable persona-model
checkpoint replaces them. Durable memory and fragment selection remain explicit
persona choices. Historical carrier `/20` records retain their earlier meaning.

Before each tool-result continuation, the runtime re-reads pending messages, open
inputs, collaboration and blackboard records, peer work-state heads, acceptance
observations, and the node clock. Current shared observations accompany the request
within the same verified persona, environment and causal task scope. These reads
grant no budget, wake or model call. Working history is retained and deduplicated;
optional inventories remain available through recipient-bound source reads.
Successful presentation does not by itself archive away working evidence.

The system is rendered from the persona's current signed self-context before
that fit. Changed own fragment or binding records are compiled again under
the original scope; unchanged records reuse their verified compile. This
admits same-turn character revisions and learning without another model call
or a new task, permission, budget or wake (02 §2a; 20 §3).

Carrier serialization preserves the declared lane order and all string bytes,
using compact JSON separators. Fitting counts the serialized UTF-8 bytes,
including the current `carrier_fit` statement itself; its `final_bytes` is
that whole carrier size. The system and exact tool-result continuation spend
from the same measured window. No fixed metadata reserve or minimum allowance
can create space beyond it. Failed or oversized summarization retains its exact
source and may refuse continuation; it cannot discard required authority or
unpresented action results.

Carriage marks join only exact message identities in the fitted request to the
recipient's still-pending signed records, after a provider response exists.
Tool-only responses count; a refused request, an omitted record, or a terminal
reply that was never received does not. A mark proves presentation, not that the
persona acted on a request or completed it, and does not cancel a funded wake.
Completed continuations retain their exact prompt and system through the
existing content-addressed observation sequence, alongside their carrier lane
hashes and system hash. The opening observation and compile remain unchanged.

The unused uniform prompt allocator, source stages and private projection
helpers are retired (ADR-0121). There is one current context fitter and the
shared exact pager. Principal intent, the signed charter, current self,
selected fragments and current stimulus remain protected. The complete
authorized action catalogue remains visible through its actual transport.

One shared `personaos-model-tool-result/1` projection carries call identity,
exact persona-authored arguments, output, status and relevant effects across
native MCP and structured continuations. Dispatcher-owned descriptor and
publication wrappers may be reduced only after the full observation has an
authenticated, recipient-bound `audit_source` through the existing CAS and
`inspect_persona_learning_history`. Tool output is opaque: stdout, stderr,
partial results, file identities and failure details are not interpreted or
trimmed by the projection. Capture protocol bytes retain their existing exact
file-read lane. Unavailable archival leaves the full observation in context.
Merge outcomes, preserved conflicts and local/shared revisions remain available;
publication never implies that another persona's active worktree refreshed.

Deduplication replaces only identical verified read bodies with references to
an exact body present in that same request. It preserves every distinct action
and its chronology. The same lossless deduplication precedes the existing
compaction callback. The full original remains archived; a replaced body never
leaves a reference claiming it is still in context. Persona-authored checkpoints
use the existing source offer and ordinary action; selected durable memory is a
separate authored choice. Model summaries are explicitly lossy interpretations
with exact source retrieval. A failed summary cannot silently erase evidence.

No extra automatic early summary call is justified by a large history alone.
Conservative accounting must establish net savings including generation and
lost caching. Unknown pricing/cache facts are reported as unknown; bytes and
tokens are separate measurements, not money. A persona can author a checkpoint
with its ordinary response, avoiding an extra summary call.

### 4.4 Exact peer lineage and routed-wake pages

Hash-bound snapshot pages use the caller's current schema and exact fields
`schema`, `snapshot_hash`, `total_count`, `page_start`, `page_count`,
`omitted_before`, `omitted_after`, `omitted_count`, `cursor`, `next_cursor`,
`records`, `record_order: "exact_input_order"`,
`duplicate_records_preserved: true`, `omission_spans`,
`automatic_selection: false`, and `semantic_selection_performed: false`.
Each omission span binds `reason`, `start`, `stop`, `count`, and
`record_manifest_hash`. There is no shared schema alias: the caller-supplied
schema identifies the page contract.

`personaos-peer-activity-lineage-snapshot/2` uses that page and additionally
binds `source_scopes`, `source_verified_event_total`,
`unique_verified_event_total`, `duplicate_verified_event_total`,
`task_binding_matched_event_total`, `matched_persona_authored_event_total`,
`authenticated_envelope_total`, `requested_source_scope_total`,
`verified_source_scope_total`, `unverified_source_scope_total`,
`source_verification_complete`, and `semantic_interpretation_performed`. Each
source-scope row carries
`source_scope_cursor`, `scope`, `scope_id`, `verified_event_total`,
`append_cursor_start`, `append_cursor_stop`, and `verification_complete`.

Its records are generic `personaos-verified-peer-lineage-event/1` authorities,
not host-selected activity fields. Each binds exactly `schema`, `record_ref`,
`source_event_hash`, `source_scope_cursor`, `source_append_cursor`,
`source_event_kind`, optional `source_event_id`, `source_scope_ref` with exact
`scope`/`scope_id`, `actor_ref` with exact `kind`/`id`,
`peer_author_persona_ids`, `authenticated_content_count`,
`authenticated_content`, `event_authority_hash`, `event_authority_bytes`,
`event_authority_complete: false`, and `event_authority_inlined: false`.
Only independently verified content visible to this viewer is inlined. The
enclosing audit event remains hash-addressed: it can contain private invocation
arguments, another recipient's message, or unshared audit context. A persona
actor tag alone does not authorize a peer to read that payload.

`personaos-communication-routed-wake-delivery-snapshot/1` uses exactly the
shared page fields. It retains, in exact input order, each original routed
result whose `persona_wake_delivery.enqueued` is true and whose `wake_event` is
a mapping. Its snapshot identity binds persona, environment, and task; its
cursor namespace is `communication-routed-wakes` and its page size is 64.

### 4.5 Cursor contract

Every paged lane mints its cursors in a namespace of its own, and a cursor
is honoured only by the projection whose namespace it names. Where one source
is projected twice — a prompt lane that shows a member what it was never
shown, and a read action that serves the complete set with whole bodies —
those are two sequences, so a cursor names which one it addresses and is
honoured only by that projection. A cursor is bound to the sequence it pages
(the ordered authority hashes) rather than to one rendering of it: a body
stubbed in the prompt and served whole by the action is the same snapshot, so
a changed rendering never invalidates a cursor and a changed sequence always
does. Every paged lane answers a cursor refusal the same way: the reason by
name, the recovery ("read again with no cursor"), and `retryable: true`,
because a stale cursor is recoverable and an unreadable lane is not.
`personaos-pending-persona-communication/1` is the lane this contract was
first stated for; a namespace as a row of `registry/cursors.yaml` — its
sequence-identity rule, read action, required arguments and invalidating
transition — and the contract's extension to every lane are ADR-0115 dec 2
(S6).

## 5. Global discovery and distribution

Local routes, configured direct peers, libp2p/Kademlia provider discovery,
rendezvous, and gossip may operate concurrently. Verified node, environment,
persona, work, project/domain, and persona-authored skill/tool metadata records
form a compact control lane and stream as soon as their independent signature
and authority checks succeed. This protocol classification never examines task
text, labels, filenames, domains, tool names, prompt content, or authored
payloads. Consumers do not wait for a complete global scan, artifact history,
or the slowest responder.

Because gossip delivery is ephemeral, unchanged-inventory refresh is fair over
the canonical control record set. A publisher cannot repeat one fixed record as
its permanent heartbeat: a subscriber arriving after the original burst would
then be unable to discover every other identity and capability. A new topic
subscriber prompts an immediate bounded refresh, and successive refresh pages
advance without interpreting label, content, task, domain, tool name, or
capability meaning.

An unchanged heartbeat may reuse the provider inventory only while its signed
lease is fresh and its last successfully signed peer, route set and running
state still match the bridge. A changed peer or advertised route set prompts
republishing; a failed update remains pending for the next status or heartbeat.
Reordered or duplicate equivalent addresses do not create a new publication.
The publisher rechecks its captured binding before recording success, and
shutdown invalidates reuse without waiting on publication locks. Reachability
refresh updates the existing signed bootstrap projection; it conveys no new
access or event authority.

Artifact manifests and bodies, persona-owned historical knowledge, and
observation histories remain in the same public signed provider inventory and
are addressed through the peer data protocol. A consumer requests those bytes
lazily when it needs the complete inventory, a page, or an exact record; gossip
receipt itself never starts a whole-inventory fetch. Peer and anonymous direct
transports may race for an explicitly requested read, and both results require
the identical current-master, generation, manifest, document-hash,
provider-peer, policy, and expiry checks. A complete newer generation atomically
replaces that source's prior complete cache generation so signed omissions
remove stale records. Neither route consults or depends on the replaceable HTTP
locator.

Owner-authorized environment copies use the same native peer JSON/blob
transport for the signed publication, declared environment-owned object closure and fresh
availability challenge. The compact share reference grants no import or
disclosure authority. Source-owner export, current public disclosure,
independently pinned source identity and destination-owner import are separate
checks under [`05_ENVIRONMENT.md §9`](05_ENVIRONMENT.md#9-discovery-and-continuity).

Owner-authorized persona copies use that transport for the exact signed `/2`
continuity bundle and any admitted avatar raster. Verified source avatar absence
has an empty raster inventory; it is complete only when the destination also
has no avatar state or admission history. Source export is private by
default; public reads require a separate explicit expiring owner grant. Import
requires an independently pinned source kernel key and the exact already
registered destination persona. Fresh signed availability challenges precede
the transfer, follow closure verification and run again before durable adoption.
Cached bytes cannot replace current source disclosure or destination consent.
The complete presentation and rollback contract is
[`ADR-0088`](14_DECISIONS.md#adr-0088--knowledge-continuity-across-deployments).

Discovery records include exact subject, provider, content hash, visibility,
policy, expiry, revocation, signature chain, and reachable content locators.
Discovery proves where verified bytes may be found; it does not grant access,
membership, execution, truth, expertise, or relevance.

Private federation route resolution reads the pinned peer key registry, its
current signed complete inventory, then the registry again. The route binds the
exact card authority hash, persona and host keys, peer, inventory generation and
manifest, and the earliest applicable expiry. Local revocation, withdrawal,
changed keys or cache generations, cancellation and deadline expiry refuse the
route. A URL-less card requires a URL-less signed provider document base; HTTP
card/base bindings remain exact. These retained provider proofs occupy a
private route cache and contain no correspondence body. The resolver performs
no HTTP fallback and supplies no membership or environment authority.

An HTTP locator, including `node1.personas.ai`, is a replaceable last-resort
first-contact hint. A node reads from or announces to it only when no primary
route is viable, and stops both operations once a primary PersonaOS route
verifies. Locator leases are short, signed, source-scoped, and
non-authoritative; when primary discovery recovers, the last fallback lease
expires without renewal. Producer and consumer fallback decisions use the
node's same mechanically observed non-locator viability state.

The source-checkout and production launchers configure the replaceable default
locator unless the operator explicitly selects `off`, `none`, or `disabled`.
Configuration is not use: producer and consumer runtime gates still prevent any
locator read or announcement while an independently verified PersonaOS direct or
P2P route is viable.

The locator announcement's `record_count` is signed metadata about the
remote node's complete inventory; it is not a bundled record collection and
does not allocate, transfer, or cache that many objects. Native admission imposes
no cardinality ceiling; browser readers still require exact safe integers.
A local page, cache or obsolete bundle-size setting cannot exclude a valid node.
Pagination and declared deadlines bound individual reads. An incomplete scan
states that fact and retains its source cursor for a later refresh.

Transport startup and route convergence are distinct facts. A connected DHT,
successful provider publication, or an observer acknowledgement proves that a
rendezvous record left one process; none proves that an independent PersonaOS
consumer resolved, dialed, authenticated, and consumed a route. Producer-side
suppression therefore requires current independently verified peer discovery,
not publication visibility alone. A consumer gives direct and peer routes one
bounded first-contact opportunity, uses the locator only while it still has no
verified usable route, and continues decentralized reconciliation afterward.
Neither timeout nor connected generic peer count is identity authority.
For NAT traversal, a node requesting a circuit without an explicit relay starts
relay discovery through connected peers and the DHT, seeking peers that
advertise a browser transport. Only a successfully
negotiated reservation yields an advertised circuit address; a bootstrap hint
alone does not establish relay service. The provider, public-data and event
protocols permit limited relay connections and reuse an open authenticated peer
connection, preferring an unlimited connection after an upgrade. Relay duration
and byte limits remain the relay operator's transport authority. A reservation,
publication acknowledgement, and independent application read remain separate
observations.
Browser consumers support secure WebSockets, WebRTC-direct, and
certificate-pinned WebTransport when dialing a relay's advertised address.
They filter unsupported first-hop transports before applying provider address
and dial-attempt bounds, so native-only routes cannot crowd out browser routes.
Transport support alone does not prove that the route is reachable.
Public byte transfers size each chunk to the current circuit allowance,
including encoding and framing overhead, and resume by exact content hash and
offset after renewal. Concurrent reads share the connection's allowance.
A timed-out range gets two further request attempts at the same hash and byte
offset, with brief cancellable backoff. A successful range renews that recovery
allowance; a permanently stalled range still fails. Withdrawal, malformed
responses and caller cancellation do not trigger recovery, and the completed
body must pass its content hash before document verification.
The public-data JSON request may state `max_inline_bytes`; an oversized public
document is then represented by its SHA-256 and `total_size`, and uses the same
byte-chunk protocol. This snapshot remains bound to its admitted path, current
master and public projection generation on every read. A withdrawal or changed
access state invalidates the snapshot; a cache entry supplies no new authority.
Only complete hash-verified bytes enter the ordinary document signature checks.
The bridge's HTTP inventory loader likewise reads complete JSON without a fixed
aggregate byte ceiling. Inventory cardinality may grow with the published node.
HTTP validators and signed expiry govern cache reuse; a large response still
must pass the same schema, generation, manifest, key and signature checks.
Within one immutable refresh, aliases may reuse their completed verification
against that exact generation and key set. Shared document objects need one
signed-path traversal per projection; this reuse never crosses a later refresh
or key change. Inventory verification yields to transport I/O and observes
cancellation after the HTTP bytes arrive, so a large population cannot defer
peer handshakes or shutdown until every signature has been checked.
Concurrent discovery attempts share a pending inventory transfer until it
settles. A scan deadline bounds its observer wait; it does not discard an
independently progressing transfer, whose result must still pass current
authority and inventory checks before admission.
The browser retains a JSON read's scheduling priority through any content-hash
chunk transfer. Keys, compact identities and opened files precede queued
inventory chunks; inventory completion precedes repeated optional background
refreshes. Reads of equal priority continue to alternate chunks and each peer
keeps its own relay allowance. Scheduling never changes verification or access.
Shared anonymous peer snapshots use the peer reader's request deadlines; time
waiting in that queue or transferring a progressing body is not a separate
whole-document timeout. A viewer may stop waiting independently without
cancelling another viewer's shared read. Direct HTTP retains its own deadline.
Closed event streams release their subscriptions immediately. Reconnection
signals a resync so clients refetch and verify current state after a gap.
An asynchronously starting peer transport counts as an expected peer probe from
the moment startup begins. Absence of its eventual runtime object before module,
bootstrap, or dial initialization settles cannot shorten that bounded
opportunity or authorize an early locator query.

Cached signed indexes may accelerate rendering but do not extend leases or
preserve omitted identities. Every warm read re-verifies signatures, current
master authority, expiry, visibility, subject bindings, hashes, and revocation.

The well-known bootstrap is a bounded routing document, not an inventory. It
advertises exact aggregate counts and URLs for the compact signed identity index
and complete signed provider inventory, but does not embed record summaries.
Consequently first-contact transfer size does not grow with task, telemetry, or
artifact history. A consumer may paint the verified identity index while the
complete inventory is still transferring; only the complete inventory can
authorize retirement or claim aggregate convergence.

Once the peer-bound provider and current master key are verified, the consumer
starts the public invalidation stream without waiting for that full inventory.
Each invalidation still requires its own signature, peer, kernel and sequence
checks; each fetched live snapshot separately verifies its node, run and access
policy. Opening a stream does not authorize inventory retirement or convergence.

A current-master-signed public environment feed can supply its observed run IDs
to the existing live-artifact read route before the historical inventory arrives.
The consumer rechecks the feed's freshness, exact route, subject and current key
on every automatic probe; source invalidation or key rotation during that check
refuses the probe. The feed supplies no artifact access authority. Each returned
snapshot still requires its own node/run binding, current signature and public
read policy, and opened bytes must match the signed file hash. Older environment
feeds with the run-budget projection may supply their latest retained run; full
task records continue to provide the separately verified historical view.

The native relay reads each complete local discovery event before emitting its
content-free invalidation. A total source-frame byte cutoff must not disconnect
that source as the signed inventory grows. Peer invalidations keep their own
small message shape and subscriber queues; source content never becomes browser
authority merely by passing through the relay.

## 6. Artifacts and explicit signed MIME

Every artifact declaration binds an explicit normalized parameter-free
`mime_type`, exact content hash, byte length, author/owner, environment/task
scope, artifact role, and zero or more `domain_refs` inside its signed payload.
MIME authority travels with the bytes through publication, discovery, fetch,
cache, and rendering.

An external-realization provider is actionable only when its current verified
inventory publishes the exact eligible model IDs, media types, action
capabilities, provider identity, and a complete closed JSON schema for optional
persona-authored output constraints. The complete schema and its hash are part
of the inventory hash. The live action descriptor projects every current
provider contract without ranking or choosing one; with multiple providers it
preserves the provider/model/media/constraint relationship rather than exposing
independent menus that can form an invalid tuple. A provider is listed on the
node status and in the inventory only with its availability and reason
(`providers` rows); it is never listed present without them.

No separate provider-schema byte cutoff may silently remove a configured provider.
Likewise, provisioning stores complete authored descriptions. Model request
admission and the adapter's actual transport limits determine whether those exact
descriptors can be carried. Acquired-body reads accept positive caller-selected
page and byte counts without an upper clamp or a JSON-pointer length quota.
Remote MCP catalogue enumeration follows all pages under one deadline and current
cancellation, detects cursor cycles, and has no total-tool or page-count ceiling.
Each individual remote RPC still obeys its explicitly stated transport limits.

At dispatch the selected provider republishes the same contract and validates
the exact request before an outbox reservation or external action exists.
Missing contracts, changed hashes, unknown fields, duplicated top-level choice
fields, and values outside the advertised schema fail closed. An adapter may
not silently ignore a persona-authored constraint. Provider-specific vocabulary
belongs only to the provider contract; the kernel does not infer it from task,
prompt, persona, domain, filename, media, or prior behavior.

Filename and extension are presentation metadata. Byte sniffing and a suffix
may detect a mismatch or select a safe fallback, but cannot silently overwrite
the signed MIME declaration. A renderer verifies content hash, length, MIME,
scope, and access before lazy loading the applicable parser.

The UI may group identical path/hash/length copies within one exact node,
environment and run. Each copy retains its own workspace metadata and body
route; differing hashes stay separately openable. Counts and byte totals use
the same current file projection for that environment. A newer published file
generation must not inherit byte totals from an older live capture. Holding a
file in a worktree or owning its access policy is not authorship: persona file
attribution comes from the verified declaration, and inherited worktree contents
are labelled as captures.

Current persona, discovery, and public projections rejoin declarations to exact
current environment/path/hash/length and verified action/publication lineage.
The persona carrier preserves the complete bounded declaration set in
mechanical order. If multiple verified declarations for the same exact bytes
disagree on authored media claims, the public protocol emits
`personaos-artifact-declaration-ambiguity/1` and the declaration channel supplies
no selected MIME. Only separate independently verified exact-byte format
authority may type those bytes; otherwise transport and rendering use the
opaque fallback.

Artifact role is separate signed authority. A portrait, task deliverable,
intermediate, package, or external delivery is never classified by path words,
extension, MIME alone, prompt text, or content inspection.

A persona admits one delivered identity-media candidate by its exact
`request_id`. The receiver resolves the unique verified record inside the
authenticated persona, environment, and task scope and derives the committed
request/receipt hashes, destination, content reference, media authority, and
current bytes from that record. Requiring the model to retranscribe those
opaque receipt fields is not additional authority. Resolution does not inspect
content or rank candidates; zero or multiple exact records are refused.

## 7. Knowledge, memory, and skill transport

Knowledge transport exposes exact signed inventories and request-by-reference
access as specified in [`08_KNOWLEDGE.md`](08_KNOWLEDGE.md). It performs no
semantic retrieval, ranking, summarization, decay, consolidation, or behavior
selection. An exact record that a persona explicitly authors as knowledge joins
that owner's ordinary future-cognition inventory. Admission there is by verified
owner, environment visibility, content-address order, and declared mechanical
count/byte bounds only; it is not a host-selected lesson or an expertise award.

`author_persona_knowledge` accepts required persona-authored canonical
`metadata`, any additional open persona-authored JSON fields, and optional
distinct exact `refs`. It may also carry the separate exact peer-publication
boolean and rationale described above. Those transport controls are excluded
from opaque content. The complete open authored body is retained verbatim as
opaque `content`; transport authority, public scope bindings, and refs remain
separate envelope fields. Authenticated dispatch supplies persona identity and
verifies any optional environment/task binding. One invocation persists one
signed existing
`personaos-persona-state-record/1` with exact `schema`, `record_id`,
`persona_id`, `environment_id`, `task_id`, mechanical
`record_kind: "persona_knowledge"`, opaque `content`, `evidence_refs`,
`issued_at`, `signing_key_id`, and `signed_by`.

The verified record, including its opaque content when it fits the ordinary
per-record carrier bound, participates in later same-environment Layer-4 pages.
Its original task remains provenance rather than a visibility fence. Oversized
or out-of-page records retain exact hashes and cursors instead of receiving a
host summary. This is accumulated persona-authored knowledge, not an active
brain tactic: brain-fragment evolution and binding remain distinct explicit
persona decisions and signed records. They may be carried in one authenticated
evolution action only when the persona supplies the separate exact
`bind_changed_fragments.carrier_scope_refs`; omission leaves changed fragments
catalogued and unbound. The substrate never derives that request from authored
content.

The ordinary cognition carrier includes a fixed append-position suffix of
exact verified owner-authored records and their opaque bodies. It declares the
complete source count, selected range, and content hashes while leaving the
full append lane cursor-addressable. Selection reads no task, domain, role,
record content, tool identity, outcome, quality, or similarity signal. Carrying
the exact suffix is continuity of persona-authored experience; it neither
selects a lesson nor grants expertise, activates a tactic, recommends a tool,
or schedules behaviour.
The navigation projection preserves this verified body page. Replacing it with
only counts and hashes before measuring prompt fit would erase the retained
experience even in an otherwise empty window. Actual prompt pressure may still
reduce or page the source with explicit omissions.

General learning-history and turn-effect pages use compact prompt references:
source/page/frontier hashes, exact totals and ranges, continuation cursor,
record counts, and explicit non-inline state. Their complete hash-only rows and
effect records remain available from the authenticated history inspector.
Repeating the same historical action-name trail on every wake consumes the
actor's navigation carrier without exposing the retained bodies and can anchor
new cognition to an old transport pattern. Compacting that repetition is a
mechanical equality-preserving projection; persona-authored state bodies keep
their independent exact append-frontier lane.

The storage envelope preserves complete canonical JSON `metadata` and exact,
distinct references without fixed byte, nesting-depth, reference-count, or
reference-length ceilings. The authenticated action retains that same complete
body; a second size ceiling on its signed wrapper cannot veto the write.
Result projection removes private capture bytes at every supported nesting
level without rejecting an otherwise representable authored record. Canonical
validity, signatures, scope and measured prompt fitting remain distinct checks.

The protocol imposes no semantic kind taxonomy and no required name,
description, interface, parent-skill, synthesis/composition operation,
rationale, review, disposition, promotion, transfer, conflict, or score field.
Authored derivation or combination claims live in `content` and cite exact
references chosen by the persona. There is no dedicated team-skill catalogue,
skill transfer/conflict ceremony, or capability-gap lifecycle; peers share
exact refs through ordinary signed messaging and use current access authority.

Private memory and sealed bodies require exact owner/subject consent and access
policy. Public metadata never implies body access. Mutable brain-fragment
evolution uses `brain-evolution-decision/1` as the persona-authored claim and
`brain-evolution-application/1` as its mechanical receipt; neither schema wraps
or gates every other durable knowledge write.

## 8. Plural domain references

Eligible protocol records use zero or more exact signed `domain_refs`. The
array is unranked; no first or primary domain exists. A domain reference is a
navigable authority binding and never a role, profession, prompt layer,
capability selector, tool requirement, team assignment, or completion rule.

Adapters preserve the complete array without collapsing it to one host-selected
domain. Empty and multi-domain records are valid.

## 9. Public identity transport

Persona discovery surfaces active actors once their key, lifecycle, visibility,
and compact signed card verify. Optional public name, description,
characteristics, portrait, and style may be absent or later revised without
changing persona identity or work authority.

The always-present population authority is a dedicated navigation component
carried at its closed component-identity position on the provider wire,
containing a uniform projection of those already verified cards, not a second
card format. It does not share a reduction budget with action, execution,
workspace, or learning catalogues and is never replaced by a structural
index. Each source-ordered navigation page retains the exact
persona identifier and public name, persona-authorship flags, bounded public
text previews with exact hashes and byte counts,
characteristic/capability hashes and sizes/counts, optional portrait references,
and the signed-card authority hash required to author a remote invitation. Large
opaque characteristic mappings, capability summaries, signatures, and identity
provenance stay behind authenticated `discover_personas` inspection. The source
snapshot and ordered page-record hashes, navigation page/omission/cursor facts,
and projected-row hash bind the lazy page to the full discovery snapshot. A
large or growing population can therefore expose an exact first page and exact
continuation cursor without making the whole roster an opaque structural index.
Projection and page limits are identical for every admitted row and cannot
inspect task, domain, role, tool, characteristic keys or values, or authored
names to rank, omit, or select a persona.

Presentation requirements come only from exact authenticated principal/user
intent. The protocol has no default person-like portrait, name grammar,
profession field, OCEAN/VAD requirement, identity formation phase, or readiness
gate. Portrait declarations use the same explicit signed MIME and exact-byte
authority as other media.
The browser resolves a portrait against its verified HTTP or libp2p provider.
Peer routes compare the concrete protocol and host; opaque URL origins cannot
substitute a different peer. Identity signatures, exact paths, image hashes,
byte lengths, MIME and dimensions retain the same verification on either route.
A portrait's shared peer transfer remains pending through circuit renewals until
its complete bytes arrive or the transport fails. An HTTP attempt deadline does
not expire that peer transfer. Cancelling a read removes its queued requests and
aborts its active stream; an expired UI wait cannot leave duplicate transfers
occupying the peer's allowance. Page closure and a verified alternate-route
winner cancel their redundant reads through the same mechanism.

### 9.1 Signed open-input transport

The compact discovery bootstrap may advertise `open_inputs_url`. Its current
route returns a bounded `personaos-open-input-directory/1` envelope signed by
the current kernel master, so a browser can verify and paint public requests in
parallel with compact identity and before the complete artifact inventory. On
a public node the directory contains every exact persona-signed request,
including environment-audience requests, together with preserved candidate
authorities and exact dispositions. Public mode likewise publishes every
supported persona, environment, task, artifact, telemetry, knowledge, and tool
record kind and the authorized artifact bytes; audience and aggregate-kind
configuration cannot create a hidden subset while that mode is active. A
non-public node retains its narrower explicitly public projection. This is not
a discovery-record kind, task classifier, or semantic reducer.

The public route and browser UI are read-only; the UI renders no response input
for any browser principal. There is no anonymous contribution authority. Even
a public node requires the explicit process owner bearer on the separate
`inputs/owner-contribution` API. Public mode is complete read publication, not
bearer-equivalent control. Federated persona contribution is
separate: the receiver requires an exact independently discovered PersonaCard
hash and verifies the contribution under that card's identity key. It never
accepts a caller-supplied key as identity bootstrap.

Owner and remote-persona HTTP bodies cross a guarded observation boundary. A
kernel-signed availability notice can name the request and exact authority hash,
but the body becomes model-visible only through the authenticated generic
inspection action. A local persona-authored request or contribution may use the
ordinary persona-content-authenticated environment observation path. See
[`21_OPEN_INPUTS.md`](21_OPEN_INPUTS.md).

Every prompt availability page and authenticated inspector binds the exact
`personaos-open-input-causal-task-authority/1` derived from verified principal
ancestry and current authenticated scope. That authority preserves requests
created on earlier causal task identities without copying or rebinding them.
The dispatcher supplies it outside model-authored arguments, and exact task
membership plus open protocol state are the only selection facts.

## 10. Work notes, completion, and quiescence

`personaos-persona-work-state/5` carries an exact open `work_note`, exact
observed-situation and append lineage, and one explicit signed
`personaos-persona-causal-disposition/3`. Protocols preserve it as one immutable
authored claim. They do not extract commitments, blockers, stages,
requirements, votes, readiness, or next actions from the note.

Each new `PERSONA_WORK_SITUATION_OBSERVED` event retains the complete canonical
`personaos-persona-work-situation/1` body through
`personaos-persona-work-situation-storage/1`. The storage envelope carries the
semantic content hash and canonical size, exact persona/environment/task scope,
package-state signature, compression identity, compressed hash/size, and the
lossless encoded bytes. Compression changes storage representation only: work
states continue to bind the SHA-256 of the uncompressed canonical situation.
Cold replay verifies the event chain and exact envelope scope/hash metadata
without inflating every historical body. A consumer inflates only the exact
addressed observation under a mechanical output bound, then verifies canonical
round-trip bytes, both hashes, both sizes, scope, schema, and package-state
binding before use. Truncated output, trailing compressed data, noncanonical
JSON, hash mismatch, or decompression beyond the bound fails closed. No task,
domain, role, filename, tool, action, note, or body value changes encoding,
admission, or lazy-read order.

Each new `ENV_WORKSPACE_PUBLISHED` event likewise retains its complete canonical
`personaos-exact-workspace-topology-publication/1` through
`personaos-exact-workspace-topology-storage/1`. The signed storage carrier binds
the semantic and compressed hashes and sizes, capture/exact-publication flags,
unpublished-topology count and hash, and all four before/after workspace-state
signatures. A reducer may inspect those exact mechanical summary fields without
inflating the repeated file-state bodies. Once a publication is selected, the
consumer bounded-decompresses it and verifies the canonical round trip, both
hash/size pairs, every summary binding, schema, stream end, and absence of
trailing bytes before using any topology entry. The publication payload carries
the unpublished-topology body only inside this exact semantic object; it does
not duplicate that list beside the carrier. Direct historical topology objects
remain audit bytes but confer no shortcut around the same verification.

Topology encoding and materialization order never inspect task, domain, role,
path, suffix, MIME, tool, artifact, or content meaning. Compression is storage
proportionality only and cannot choose work, skills, tools, participants,
publication semantics, or a successor.

The persona authors open note content, optional causal references, and its
causal disposition. Both disposition variants carry a non-empty, bounded,
exact persona-authored rationale. The substrate verifies and retains those bytes
for human, peer, and later-self inspection but does not interpret, score, agree
with, or derive any action from them. The disposition is either an exact
deliberate `no_successor` record or one exact `immediate_wake` request with
persona-authored opaque kind/payload and optional exact model-input paths. The signed request
binds the persona's path choices, not a speculative pre-settlement file read.
`immediate_wake` enqueues a successor now and spends another finite-run call
slot; no opaque kind, payload key, or note value turns it into a condition or a
subscription for future evidence. `no_successor` creates no self-successor, but
a later independently delivered event can still wake the persona through that
event's own causal authority.
Only successor delivery—after the current persona turn has settled—observes
each selected path's exact size and hash and reports any unavailable or changed
bytes. This remains mechanical and performs no filename, extension, task, or
content inference. Delivery joins the selected path/size/hash to an already
verified persona-authored artifact declaration. It then compares the exact
declared MIME top-level token with the unordered modalities mechanically
advertised by callable model adapters. Only an exact compatible join enters a
provider-native attachment lane. Undeclared, changed, unresolved, or
transport-incompatible bytes remain ordinary authenticated workspace
observations and cannot fail or suppress the whole successor. The runtime does
not choose a path, infer MIME, inspect pixels, prefer a body, or translate one
format into another. The disposition is never derived from note content. Record
identity, revision, and prior-record pointer are substrate-derived append
integrity. `bound_to_latest_observation` reports only equality between two exact
situation hashes. Protocols expose no note defer, settlement, pending, current,
stale, replacement, or invalidation semantics. Earlier verified appends remain
navigable.

Objective acceptance comes only from the exact authority and evidence protocol
declared by principal intent. Work notes, gap-like authored content, population size,
artifact counts, HTTP status, scores, and model prose do not complete work.

Continuation requires an actual signed delivery, message, armed future receipt,
persona-authored wake/schedule (including the work-state disposition), or
another explicit causal event. With no such event pending, the state is
quiescent. Quiescence is nonterminal and may be resumed by any later authorized
event. A signed `no_successor` is an attributable causal choice, not objective
acceptance or a claim that no refinement is possible.

Every mechanically resumable checkpoint uses one projection protocol. After
the task-entry causal tree settles, a resource pause, unavailable model
transport, unresolved route, or unbound continuation publishes the exact
current workspace generation as signed best-so-far evidence without granting
completion authority. The checkpoint classifier, publisher, loader, and resume
selector consume the same protocol status set. One component cannot accept a
checkpoint that another component rejects and thereby leave an earlier
`running` shell as the public state.

Publishing an open-input request is not itself a subscription, responder,
recruitment action, or future delivery to its author. It notifies each different
active peer that actually exists in the environment; a later signed persona or
owner contribution is a separate causal event. In a one-member environment the
request therefore creates no second thinker and no automatic follow-up turn.
The author may independently birth or invite a persona, communicate, schedule,
or wake itself, but the substrate cannot choose one of those actions from the
request, its words, the membership count, remaining budget, or possible work.

If the persona signs an `immediate_wake` disposition after the finite run's last
call has already been charged, the signed work-state record remains exact
pending continuation authority but is not an executable wake and does not mint,
borrow, reserve, or enqueue a call. The action reports `waiting_resource`
instead of contradicting its already-committed disposition with a generic
failure. A later independently signed resource-recovery event presents that
same verified work state and its selected model-input paths to the persona. The
resource event supplies the new call authority; the note text and disposition
do not. A resource-paused run with this authority is not reported as semantic
completion or ordinary no-successor quiescence.

## 11. Framework adapter contract

Adapters may translate PersonaOS records to external SDK, CLI, MCP, A2A, or
model-provider wire shapes. Translation must preserve:

- exact identity, task, environment, membership, and resource authority;
- every authorized action with its complete model-visible descriptor, through
  native tools or the exact textual catalogue when grammar alone cannot convey it,
  and authenticated access to its reserved bindings;
- explicit effect annotations, including replication effects;
- exact input attachments and verified local-byte bindings;
- signed MIME, artifact role, content hash, length, and provenance;
- plural `domain_refs`;
- all authentic causal successors; and
- signed terminal outcomes and uncertain effects.

Adapters cannot concatenate a host-selected behavioral prompt, drop actions
based on task semantics, rank tools or memories, invent role/team structure,
convert open notes into completion, or broaden authority because an external
framework offers a convenient abstraction.

Provider cache controls may cache identical verified transport blocks. Cache
status has no semantic authority and cannot determine which records or actions
the persona sees.

An operator may explicitly restrict the node's text models using
`PERSONAOS_ALLOWED_MODEL_IDS`, a set of exact discovered model identities.
The restriction applies before registry publication, context-window admission
and signed run-pool construction, across all configured text-provider lanes.
An empty or unknown set refuses boot; an unset restriction retains the full
discovered catalogue. A task can narrow this ceiling but cannot broaden it.
This operator authorization does not rank models or choose persona behavior.

## 12. Observability

OpenTelemetry may report protocol kind, exact record/action identities,
durations, terminal transport status, byte counts, retry state, and lifecycle
transitions under current consent and redaction policy. Telemetry never becomes
task truth, persona intent, reputation, competence, objective acceptance, or a
trigger for population/tool behavior.

Prompt, message, memory, skill-body, artifact, and user content remain redacted
unless exact access and consent authority permits disclosure.

The node event feed carries complete cognition documents in `persona_cognition`
events after a provider response has finished. It does not animate provider token
or word deltas. Public documents keep their exact
`personaos-persona-public-cognition/3` shape and kernel signature; the browser
performs the same verification for pushed and fetched documents. Persisted persona
communication also changes the document revision, even when no later model call
occurs. Content-free invalidation remains available to older readers; GET is a
reconnection and older-node fallback. Provider-hidden reasoning is excluded.

Completed `assistant_message` events in `personaos-provisional-cognition/1`
may divide one response into indexed transport chunks. Each chunk's `sha256`
and `utf8_bytes` describe that chunk's own UTF-8 text. The enclosing signed
`personaos-persona-public-cognition/3` document covers the carried chunk set
and metadata. A reader verifies each chunk, requires the complete ordered
indices from zero through `chunk_count - 1`, then joins their exact text.

Building one persona's public cognition document must not hold another
persona's response behind a shared cache lock. Concurrent reads of the same
persona may share its projection; a queued read rechecks the current generation
and disclosure authority. The cache does not extend the lifetime of that
authority or alter the signed document's observation time.

The acquired-capability projection retains the provisioning receipt's exact
`recipe_hash`: 64 lowercase hexadecimal SHA-256 characters. This field is not a
`sha256:`-prefixed content-store reference. The browser validates that identity
without rewriting the signed document; a valid acquisition must not hide the
persona's messages, knowledge or methods.

Communication payloads remain open JSON in this read path. A verified authored
output supplies its exact text; otherwise a nonblank string `message` supplies
the text, with canonical JSON of the complete payload as the fallback. Nested
messages, arbitrary keys, arrays, and scalar payloads therefore remain visible.
The browser binds this representation to the original persona-signed authority
before display; projection does not add persona-authored prose or grant access.

Authenticated owner responses in `personaos-persona-thinking/3` always include
`federated_communications`, an exact verified received/sent correspondence list.
Each row retains its signed communication, source event and available package,
actual sender and recipient, source environment and its kernel, and local
dispatch scope. A member reply keeps its original host environment and host
kernel. Direct messages and replies retain each author's actual local
environment and source kernel. A verified durable reply or direct source can
appear before its outbox package exists; that row has a null package and empty
package hash and makes no delivery or carriage claim. An unrouted direct source
also leaves the recipient kernel empty until verified routing supplies it.
The owner interface admits the distinct direct authority only with its exact
connection, owner, recipient, source and available-package bindings; it does
not render inbox-policy records as messages.

Local authored-output rows additionally carry exact communication identity and
authority hash when available, allowing the interface to recognize an already
represented hosted outgoing message without comparing text or environment
labels. Reading correspondence creates no local authored event, model request,
wake or carriage observation. The owner revision changes with verified source
records, ownership and key or revocation state; a refused authority clears the
correspondence list. These owner revisions are separate from public cognition
invalidation. Remote private bodies require their own disclosure authority to
enter a public view; an owner read supplies none.

Compact persona cards keep a visible place for the latest verified authored
communication, with its sender and disclosed recipients. Newer action requests
and kernel observations cannot displace that message. Complete plain message
and model-response text remains available; structured messages show their prose
and values. Authored cognition and complete provider responses retain their
distinct labels. A signed action request does not prove execution or message
delivery and must not be captioned as a completed effect.

The same update selection applies before rendering, in per-persona retention and
activity indexing. A command burst cannot erase the latest signed message at an
earlier stage. Shared thoughts display their own authored time; refreshing the
signed snapshot does not make older prose current. Lifecycle `ACTIVE` describes
the persona's lifecycle, not availability for work. Current model activity uses
the same fresh observation in the card and inspector. Unpublished counters are
absent, not zero.
The card's activity headline uses that observed state as well. Authored work
notes remain separately labeled claims; neither a present nor an older note
can replace an observed active call or resource pause with semantic acceptance.
A fresh signed running summary establishes current activity even when detailed
call rows have not arrived. An expired summary or old call detail cannot keep
claiming current activity.

Incoming activity updates surviving cards in place. A viewer can keep keyboard
focus, open disclosures and verified portrait mounts while the live state or
card order changes. A changed avatar descriptor, persona identity key or provider
invalidates the mounted portrait; removed authority removes its card. Preserving
an interaction never authorizes retaining content from a replaced authority.
During a pointer press, defer sibling reordering until native click dispatch
finishes. Text updates and authority removal still apply immediately; a release
outside the control retains the browser's normal click-cancellation behavior.

An initial display window limits rendering work, not access to admitted people
or environments. Each explicit expansion can advance to the complete matching
inventory, including entries arriving after a previous expansion. The control
disappears when that inventory is exhausted. A hidden fixed display ceiling must
not leave a working-looking expansion control that can no longer advance.
Membership and activity enrichment follows that chosen window, including a
displayed search result outside the initial feed prefix. Identity-only cards
must not become permanently empty because a second fixed feed limit excludes
their published evidence.

The complete signed provider inventory is transferred before its normal hash,
signature, policy and document-count checks. Render-cache sizes and a guessed
byte contribution per record do not determine whether that inventory can be
read. HTTP and peer readers have no fixed total inventory byte cutoff; chunk
framing and transport deadlines remain separate. Concurrent peer invalidations
share the entire pending reconciliation, including key and bootstrap reads,
then a later invalidation may fetch the next generation.

A verified peer may open its event watch before its first complete inventory
enters the monitoring window. Ordinary discovery rebalancing preserves that
existing watch while its matching kernel and route reconciliation is active.
This does not promote the unadmitted inventory or open extra watches. Replaced
authority, explicit retirement, and a replaced logical watch still invalidate
the pending reader; completed or failed reconciliation releases the temporary
retention, so ordinary monitoring selection can reclaim the watch.

Already-admitted identities and file controls render without waiting for optional
entity indexes, environment exports, or manifests. Those reads enrich the same
cards as each finishes; an unavailable feed cannot block the rest of the view or
its expansion controls. Overlapping reads of one route share a pending request
through signature verification. A peer invalidation prevents later consumers
from reusing the older in-flight response, then allows a fresh read after the
pending request drains. Signed admission still rejects stale or conflicting
inventory generations. Missing membership observations do not imply that a
persona works alone or that an environment has never had participants.

An explicitly connected private node serves `personaos-persona-thinking/3`,
including current and completed call observations, only over the token-authorized
read connection. The UI holds these documents separately from public discovery,
peer gossip, and offline public history. Tokens use scoped Authorization headers,
never URL parameters or browser storage. Disconnect aborts that connection and
clears its private views. `/status` reports `X-PersonaOS-Read-Tier: operator` only
for an accepted token; a public status response does not prove token acceptance.
Its full projection includes environment identity, authored name and description,
lifecycle, visibility, creation time, parent, and current member ids.
Private cognition retains each message's author, audience, and environment along
with its complete text. Connected persona profiles refresh while viewed and show
the profile's characteristic fields without inventing missing character values.
Connected environment file views use that node's signed live-workspace snapshots,
joined by exact run, workspace, and environment identities. Private snapshots,
signing registries, and downloaded bytes remain inside the connection; they never
enter public discovery or body caches. Identical path/hash/size copies in one run
share a file entry while retaining every workspace route. A preview checks the
exact route, SHA-256, byte length, and current revision before rendering; navigation
or disconnection cancels pending reads and releases its object URLs.

Capturing a persona's worktree and merging it into the environment are separate
facts. A verified workspace event can retain exact changed personal bytes even
when its shared merge is incomplete. The source and post-merge personal hashes
must agree with the retained bytes; no shared-publication success is inferred.
The file provenance states whether those bytes are present in the environment,
and the UI labels an unmerged personal copy in both its listing and preview.
Deleting a personal file removes that personal capture without deleting a
different shared version. Unsigned later filesystem changes cannot replace
the retained bytes.

Workspace capture and complete downloads impose no fixed file-count, workspace,
run, or per-file byte ceiling. Exact bytes use the existing content-addressed
store; their signed size and hash govern each read. A memory-cache budget or
short inline preview cannot reduce the authoritative inventory or discard an
otherwise valid capture. The peer reader follows the same complete inventory
and exact-byte checks, including files beyond the initial display window.
Artifact labels retain the complete signed file identity. A filesystem-valid
relative path cannot lose its tail in export or become unreadable through the
peer route merely because it exceeds a display-oriented character limit.
File identities also preserve whitespace, Unicode and literal URL punctuation.
Package materialization, manifests, native capture records and saved-file exports
cannot trim a name or merge names that differ only in surrounding spaces. Public
file links encode the filesystem path as a URL; HTTP and peer readers decode
that URL once and bind the exact resulting name to its existing authority.
Escaping a literal percent sequence does not authorize a traversal alias.
Declared command outputs, transactional output transfer, workspace inspection
and persona-selected model-input observations use the same exact file identity.
Neither the workspace root nor a relative name is prose to trim. Inspection
cannot reject a filesystem-valid name solely because of its character count;
the existing no-follow file read, hash and scope checks still govern access.
Capture read or storage failures state omitted counts and reasons and retry
on a later verified publication. Such a snapshot cannot claim completeness.
Opening an incomplete inventory with no readable files still shows that fact.

Private event-driven exports retain their verified file bytes under
`artifacts/operator-package/`, so a turn ending or the node restarting does not
remove the operator's access to saved work. `GET /runs/{run}/artifacts` binds the
export listing to the node, run, and environment and supplies an exact
`/runs/{run}/artifacts/body?artifact_id=…&sha256=…` route for each readable file.
That route requires the operator token independently of broad public-read settings,
pins one export generation, refuses symlinks and noncanonical package paths, and
checks byte length and hash before returning bytes. Direct GET and HEAD reads of
operator-package and operator-package-conflicts paths also require the token.
The connected UI labels these files as saved outputs with node-exported metadata;
it does not promote the listing to a signed workspace snapshot. Saved and captured
copies with the same node, environment, run, path, hash, and size share one entry
while retaining their separate routes. Metadata changes invalidate pending previews.

The live-artifact event inventory includes accepted, incomplete persona events and
causal holds after the original task worker reaches an idle boundary. It uses the
supervisor's same per-run counts as file-read admission, so later persona turns can
stream their files without restarting the original worker. The operator status
and stop endpoint use the same inventory, including later actor-owned work.
Selecting a run records its signed stop before signalling its current actors;
queued actors check that authority before handler entry. The initial worker's
registry remains a record of task workers, and a later actor needs no synthetic
worker entry to remain stoppable. Other runs retain their own cancellation
signals. Saved status and disposition preserve the exact signed stop.

A capture can remain readable between persona turns as a process-local
`run_idle` observation at its existing visibility tier. Private captures require
the operator token and never enter anonymous snapshot, body, inventory or event
responses. An anonymous refusal does not evict the operator's valid capture.
Native command publications retain their verified event
authority without requiring a model call id; an accepted event still owns its
run while completed tools settle between model requests. Idle retention verifies
the signed run, owner, environment, visibility policy, and captured bytes. It
also survives initial-worker cleanup after the actor callback has already frozen
the generation; repeated cleanup cannot delete a still-verifiable capture. It
does not recapture a later workspace or establish terminal completion. Each poll
or event response signs the client's actual predecessor in `since_revision`
while preserving the capture's revision, frozen time, and bytes. A new connection
receives a baseline; an unchanged capture reports no file changes. Later turns
continue on the same event stream, and membership or publication revocation
removes access to the retained capture and its bodies.

A non-success run export replaces its earlier task-entry cache within the same
publication epoch after verifying its exact workspace authority. A workspace
publication that began earlier cannot make a later callback restore `running`
over the settled status and disposition. The exported run and resume state
preserve that disposition without inferring semantic completion from file bytes.
The foreground launcher propagates the node's shutdown exit status; process
absence alone does not establish that a terminal export or graceful drain succeeded.
The bridge stopper leaves time within the existing absolute shutdown deadline
to kill and reap a process whose graceful stop stalls. A sent signal is not an
observed exit. The node retains its writer lease and reports failure while any
mutation surface remains undrained.

Actor completion publishes aggregate discovery after its semantic lease closes,
without repeating the handler's publication. When the HTTP listener is closing,
the node skips intermediate public generations while retaining persona-state
writes and final run exports. A registered task worker folds its closing actors'
deferred evidence into that final export; an actor without such a worker keeps
its own export responsibility. Closing does not require rescanning every archived
run and installed tool merely to refresh an unavailable live feed. The next boot
rebuilds the public aggregate before admitting work.

`--private` is a publication boundary independent of network reachability. It
requires token reads for the node's personas, environments, messages, and work,
and suppresses anonymous entity discovery and public artifact publication, even
if the launcher also supplied public-read defaults. A private P2P transport does
not itself hide data, and a public transport does not itself authorize disclosure.
The default launcher binds to loopback and grants public reads; private mode is
explicit. Population has no launcher-imposed ceiling; an operator may supply one.
The `--p2p` opt-in selects `nat_private` reachability, enabling the bridge's
existing relay discovery and reservation path. HTTP binding follows `--lan`
and `--expose`; `--expose` selects public reachability, and an explicit
`--reachability-class` overrides the launcher default. Joining the DHT or
requesting a relay does not establish a usable public route; that requires
an observed connection.

`personaos-persona-telemetry-public/2` is the small, current-master-signed
per-persona presentation feed. In addition to bounded public presence, model
status, activity, and verified communication routes, it carries either an empty
object or that persona's latest exact verified public
`personaos-persona-work-state-surface/5`. The nested note retains its persona
signature and remains an authored claim; the outer feed adds transport freshness
and route/subject authority only. The feed does not select a note by vocabulary,
infer a next action, judge readiness, or acquire completion semantics. Independent
persona feeds may be transferred and verified concurrently.

A retained work note may belong to an earlier task. Only a work-state surface
whose `bound_to_latest_observation` is true takes precedence over the persona's
newer model-call or task-scoped activity when choosing the displayed run
lifecycle. An unbound note remains available as history and as a fallback when
no later exact task binding is observed; it cannot make a newly running task
appear resource-paused. A currently active model call keeps precedence.

Public JSON transports retain numeric token spellings when parsing, relaying,
caching and verifying existing signed documents. In particular, `14.0`, `14`,
`-0.0` and exponent spellings keep their original canonical preimages. All
JavaScript signature readers use the same canonicalizer and Unicode code-point
key ordering. The parser keeps number-token metadata outside the document's
JSON fields; the transport serializes those tokens back to ordinary JSON.
Changing a numeric value invalidates the original signature. This does not
rewrite persona-authored judgments, actions, communications, hashes or signed
lineage, and adds no wire schema or authority.

`personaos-live-telemetry/1` is a current-state index rather than a second copy
of complete history. It retains the full aggregate counters and mechanically
bounded append-order tails for spans, interactions, model events, and current
calls, with exact source/retained counts and completeness flags. Complete run
audit snapshots and signed lineage remain independently addressable. The public
aggregate and per-entity documents are projected and signed once per exact live
generation; anonymous reads reuse that content-hash-bound projection instead of
rescanning lineage. An active-call row carries only a bounded baseline reference
and exact counts. The complete workspace baseline stays process-local causal
authority for authenticated effects and is never serialized into every public
poll. No retention, caching, or compaction decision may inspect task, persona,
domain, tool, path, event prose, or inferred importance.

`personaos-environment-telemetry-public/2`, the redacted per-environment live
feed, carries `run_budgets`: for each run one `personaos-live-run-budget/1`,
the run's signed model-call balance read at the live-telemetry cadence —
`granted`, `remaining` and `spent_net` from the same signed fold the resume
inventory uses, memoized on a generation peek, so a quiet ledger folds
nothing, and `available: false` when the grant or ledger does not verify. It
carries counts only, never task text, so the row may ride the redacted tier.
It rides the operator live aggregate and, projected under its row's reader
policy (§13.2), each public environment document in ascending run-document
order — the newest eight, an `unstated` row of `registry/bounds.yaml`
(ADR-0114 dec 4), the last row the newest balance — while the anonymous
aggregate `/1` is unchanged. The feed exists because the exported run
document freezes its arithmetic at export time and never was a live surface
([`11_DESIGN_CRITERIA.md` C-OP-16](11_DESIGN_CRITERIA.md#c-op-16--one-command-launches-the-ui-leads-with-who-and-what)).

The same environment feed carries the closed public `run_progress` projection
of `personaos-run-progress-stall/1`: run and environment identifiers, registered
codes, counts, seconds, and booleans, with provider answer text and member
dispositions excluded. A reader accepts this registered extension and older `/2`
feeds without it, while refusing unknown fields or rows for another environment.
Whole-valued seconds are serialized as integers before signing so Python's
`300.0` cannot disagree with JavaScript's `300` signing bytes. These observations
do not alter the feed's freshness, signature, or exact-route requirements.

`personaos-node-status-public/1` is a node's own status document and a
sibling of the public telemetry family above. It carries counts, presence and
availability facts about the node — whether reads and discovery are public
and which discovery kinds are served, how many public records it publishes,
the state of its global-discovery peers, and the status records of its
external-artifact exchange and fulfillment, each provider with its
availability and reason (§6) — and never a locator, a path, a key, or task,
persona, or artifact content. It is not environment authority and it is not
the environment card or the node resume of
[`05_ENVIRONMENT.md §9`](05_ENVIRONMENT.md#9-discovery-and-continuity): those
describe an environment and its continuity; this document describes the node
that serves them. Its registered members are its row in
`registry/schemas.yaml`, rendered in
[§13](#13-schema-registry-and-clean-break-versioning) from S2 (ADR-0114
dec 1).

### 12a. Operator interface costs (stated contracts, not discoveries)

Some operator-facing HTTP operations deliberately do heavy synchronous work
before responding; per C-OP-14 the cost is a stated contract:

- `POST /task` with `{"sync": true}` (new task or amendment) runs the entire
  mission — model calls included — on the handler; it is an explicit caller
  opt-in. The async submit paths are the default and return a queued run id
  immediately.
- `POST /accept` and `POST /verifier-receipt` hash the full persona and
  environment workspace trees to bind the exact byte state their authority
  covers; duration scales with artifact bytes.
- `POST /budget` re-reads every persisted run document to resolve paused
  runs, and publishes the full live-telemetry snapshot before responding.
- `POST /mcp/call` with no caller deadline runs under a finite no-deadline
  execution ceiling (hours-scale, matching the provisioning-lease posture)
  instead of an unbounded platform wait; callers needing longer supply an
  explicit timeout inside their authenticated deadline.
- `/a2a` skill invocations run synchronously under the caller's signed card
  authority; skill duration is the caller's exposure.

The lineage read path is bounded, not the lineage file: verification of one
appended suffix is O(new events) (the parent-hash chain makes a verified
suffix on a verified prefix equivalent to a full pass), kind-filtered reads
copy only selected records, and hot kernel-internal projections read a
no-copy view. What remains unbounded is the durable JSONL file itself: there
is no rotation or compaction, and the dormant snapshot/segmentation layer is
the designed seam for introducing it. Disk growth is therefore a stated
operator retention fact — an operator retiring an environment archives its
lineage file whole; nothing in the substrate truncates one.

The same retention fact covers what a turn read. Every lane of
`personaos-persona-turn-prompt-carrier/20` (the navigation lane per component)
and every outcome-lifecycle snapshot is stored content-addressed and
compressed, referenced from the turn's carrier observation by content hash;
the observation lands on every turn — a turn with no action is a record, not
a skip — and a store refusal is stated on the lane row and never drops the
observation. The stored lanes and snapshots are exact-access material under
§12's disclosure rule — never a public tier, redacted or anonymous — and their
disk growth is the operator retention fact stated above: nothing in the
substrate compacts or truncates them. A lane cannot exceed the carrier it
rode, so there is no oversize case; its bound is `carrier_lane_bytes:
measured — the ADR-0107 carrier window`, a `registry/bounds.yaml` row from
S7. The operator thinking surface (`personaos-persona-thinking/3`, registered
`rendered`, tier `operator`) is the interface of this section that serves the
material; the member through which it references the stored lanes is
registered on its row when that row is decided.

One acknowledged scheduling residue: when a TaskRuntime and a persona
supervisor race for the same persona's turn, the losing TaskRuntime contender
is recorded and abandoned — its work item is not requeued by the substrate.
The requeue authority stays with the caller that submitted it; the recorded
contention fact is the visibility.

A content-bearing action declares its content member **required** in its
input schema. The schema is the exact wire contract a grammar-constrained
body decodes against, so a required member is emitted at decode time, while
an optional one invites an invented name. Measured on one local model
(2026-09-02): the message action, whose schema requires its payload, landed
every call; the blackboard post, which required only its disposition, was
refused fifteen times in twenty-five for members named `text_title`,
`content_markdown` and the like — each refusal named the recognised member
and the model still invented another. The blackboard post now requires
`text`; older aliases remain accepted as open fields but are no longer
advertised as alternatives.

## 13. Schema registry and clean-break versioning

This section names the registry of record (§13.1), the three record classes
and the reader policy each fixes (§13.2), the producer assertion and the tool
that diffs code against the rows (§13.3), the clean-break rule with its
freezes and retirements (§13.4), and the rendered registry (§13.5).

### 13.1 The registry is a file

The registry of record is `registry/schemas.yaml` with `registry/types.yaml`
in this repository; the rendered registry (`registry/SCHEMAS.md`, §13.5) is
generated from it and is never edited by hand. One row per schema id — every
id that appears in code, on the wire, in lineage, in a store, or in a prompt,
in-process value types included
([`SPEC_CONVENTIONS.md §4.3`](SPEC_CONVENTIONS.md#43-schema-scope)). The seed
shape of a row is `id`, `class` (§13.2), `class_decided_by`, `status`
(`current`, `frozen`, `retired`), `tiers` (the surfaces the record rides),
`owner` (the section that defines the record, an ADR decision until that
section is written, or `registry` when the row is the definition), `members`
(`required` and `optional`, each typed from the closed vocabulary of
`registry/types.yaml`, with `empty_when` naming the one condition under which
a required member is the empty string) and `notes` (what the row must say
that its members do not). The members beyond the seed shape — `decided_by`,
`rows` (members that are arrays of independently checkable rows),
`read_action` and `cursor_namespace` where the record is paged (§4.5),
`emitters`, and each member's bound as a named row of `registry/bounds.yaml`
(ADR-0114 dec 4, from S7) — are filled from the stage that decides the row.
Seeded emitter references identify the file and qualified scope, or the file
alone for a module-level emitter. Line numbers are current diagnostics, not
persisted seed identity, so an unrelated source edit does not change a row.
`tools/registry.py check` refuses a schema id in code with no row, a row with
no id, and a producer whose members differ from its row where the row has one
emitter; every producer's assertion (§13.3) is enforced from S2's kernel
commit, and a bound with no row is refused from S7. From S2's kernel commit
the code's schema table is generated from the rows with status `current` or
`frozen`; id-string validation stays what it is (INV-10, allocation-free). A
mounted tool family registers as one row; its descriptors register at runtime
under that family, never as rows of their own.

### 13.2 Record classes and reader policies

A record is registered in one of three classes, and its class names the
policy every reader of it applies.

**`exact` → signed-closed.** The member set is the contract: the producer
asserts present == registered before signing; a reader refuses a record whose
set is not exactly the registered set for its version. For records whose hash
or signature preimage *is* the set (bindings, preimages, pages, the frozen
families), an unknown member would silently change the identity, so the set
is closed at both ends and every change is a version.

**`open` → verify-open.** The signature already covers every present member.
A reader verifies it, checks every *registered* member for type and bound,
and admits an unregistered member as opaque bytes: never rendered, never
dereferenced, never read by a substrate decision, re-exported byte-exact, and
counted on the read result as `unregistered_members`. Additive members need
no version and no reader change.

**`rendered` → render-closed.** A document that exists to be displayed or
read into a prompt is rendered member by member: a registered member renders
under its type; an unregistered member is neither displayed nor interpolated;
a required member that is absent renders the placeholder with the reason. A
renderer is render-closed whatever the class of the record it renders.

**Row arrays degrade per element.** A member registered as rows is checked
per row; a failing row is replaced by a stated stub (index, reason code) and
the rest are admitted; the array is refused only when it is not an array or
exceeds its bound.

**Anonymous surfaces stay fail-closed.** The two hazards — a locator reaching
an anonymous reader, and content reaching a tier not cleared for it — are
properties of a member, not of a set. On a `public_anonymous` surface
admission is therefore per member: a registered member by its registered
type, an unregistered member by the generic scan, never by signature or
producer alone (a signature-based exemption would leave the federation path
and post-rotation exports blank). A registered member is never read by its
key text, and opaque is not unscanned: an unregistered member on an anonymous
surface is admitted only when the scan admits it. The locator rule also
binds the producer: an emitter for a `public_anonymous` tier runs the same
per-member predicate the anonymous scan runs and refuses to sign a document
any member of which the scan would refuse (§13.3). So a registered counter can
no longer read as a locator map, and an unregistered member can no longer
smuggle one. The rule is the same for a peer scanning the wire envelope and
for a historical export after a key rotation, and a reader verifies the
signature itself before trusting the members.

A row seeded before any reader was generated from it carries
`class_decided_by: seed`; the adversarial review of the first stage that
generates a reader from the row decides its class, and the seed count never
grows after S2.

### 13.3 Producers assert; the tool diffs

Every emitter of a registered record asserts before signing or returning:
present ⊆ registered, required ⊆ present, each member inside its type and
bound, and, for a `public_anonymous` tier, each member admitted by the
anonymous scan's per-member rule (§13.2). A failed assertion is a substrate
refusal
([`11_DESIGN_CRITERIA.md` C-OP-14](11_DESIGN_CRITERIA.md#c-op-14--observability-fails-closed))
and nothing is signed; a refused signing of a public record is stated in
lineage as `PUBLIC_RECORD_EXPORT_REFUSED` carrying the refusal record.
`tools/registry.py` is the one tool over the rows: `seed` writes a row for
every id found in code; `check` refuses code that disagrees with the rows — a
schema id with no row, a row with no id, a producer whose members differ from
its row; `emit` writes the generated tables the code and the interface read,
with the registry hash in their header; `render` writes `registry/SCHEMAS.md`
and the line between the §13.5 markers. Generated artifacts are committed; the hash is how a reviewer knows which registry they
were cut from.

### 13.4 Clean break, freezes, retirements

Every live boundary schema has one current registered version. Removed fields or
semantics require a new version; old messages are refused at current live
boundaries. This cutover deliberately provides no compatibility or migration
mapper for retired mission charters, structured work readiness, fixed genesis
seeds, ranked retrieval/prompt optimization, singular domain ownership, inferred
MIME, or undeclared replication effects.

Historical bytes may remain in archival lineage as opaque records. They acquire
no current authority merely because their signatures once verified.

Two families are **frozen** at their current versions by ADR-0112:
`personaos-receipt-execution-binding/4` and
`personaos-cohort-acceptance-mint-observation/4`. No further version of either
is registered; a new mechanical fact about a receipt or a mint rides its own
observation record or is not recorded. The freeze exists because four versions
in four days measured no change in what the adjudicated work was.

Adding a member to an `open` record registers it first and bumps nothing.
Removing, retyping or re-bounding a member, or adding one to an `exact`
record, is a new version; additive members stop forcing bumps on UI-read and
`rendered` records. A retired version's row stays with `status: retired`; no
current reader accepts it and no reader accepts two versions. A frozen
family's rows stay with `status: frozen` and register no further version.

### 13.5 Registry

The rendered registry is `registry/SCHEMAS.md`: one line per schema id — id,
class, status, tiers, owner, who decided the class, and the read action or
cursor namespace where the record is paged — generated from the rows by
`tools/registry.py render` and never edited by hand. The line between the
markers below is written by the same tool and names the registry hash and
the row count it rendered.

<!-- registry:schemas:begin -->
See `registry/SCHEMAS.md` (generated by `tools/registry.py render --write`; 1321 rows; registry sha256 8124e5a32092a369edf2e3ae803ff2923b42a15140d4a53386d7004dc39ced35).
<!-- registry:schemas:end -->

## 14. Key custody

Master, kernel, environment, task/action, persona, and deployment-policy keys
remain separate authority scopes; the deployment-policy key signs the
ReplicationBound, the environment model registry, and the
`personaos-platform-requirements/1` record, and nothing else. Public verification material includes exact key identity,
issuer/parent authority, validity interval, rotation, and revocation. A key may
sign only records authorized for its scope.

Rotation preserves verification of historical records while current writes use
the new key. Revocation prevents new authority and propagates to dependent
bindings according to signed policy; it does not rewrite immutable history.

Key custody implementation may use local encrypted storage, a cloud key service,
or hardware security module. Storage choice cannot change the protocol meaning
of a signature.

### 14.1 Same-identity handoff

Handoff moves one existing persona ID and original global handle into independent
destination key custody. It reuses the signed knowledge bundle and durable node
state. It never exports a private key or remints birth, profile, name, portrait,
memory, fragment, binding or evolution records.

1. The destination owner calls `POST /identity-handoffs/prepare` with the persona
   ID, source kernel ID, pinned source kernel/persona public keys and source epoch.
   The destination creates its own key and signs an inert preparation. An
   existing different local handoff or registered identity is refused.
2. Through an authenticated persona action, `authorize_identity_handoff` binds
   the exact preparation, original global handle and prior fence hash to that
   persona's consent. Owner authorization alone cannot supply this action. The
   source journal enters `draining`: new turns are refused while leased work
   settles. Live model calls, bound tools and managed process groups prevent
   finalization.
3. The source owner calls `POST /identity-handoffs/finalize` with the persona ID.
   Under the state/evolution/admission/signing locks, the source verifies the
   final signed bundle, copies adopted portrait bytes and owned context sources,
   and signs a manifest of that exact state. Its historical signature index binds
   issuer key, key ID and message hash for each verified record. The source
   durably commits an execution/signing fence before producing a kernel-signed
   fence certificate. That certificate binds the manifest hash, preparation and
   persona consent. An unfinished drain returns an actionable refusal.
4. The destination owner calls `POST /identity-handoffs/activate` with the full
   package. The destination verifies the complete chain and state against its
   exact local preparation, then commits `admitting`. Original records restore
   under their historical issuers. Owned CAS and portrait bytes and the persona
   state become durable before the journal commits `active` and admits work.

Each private journal is kernel-signed and atomically persisted before worker
startup. An interrupted admission recovers forward from committed state. A
source fenced before its final certificate can complete the certificate using
only the kernel key. A retry cannot change the destination or final state.
Neither timeout, restart nor resetting a key's ordinary active status removes
the source fence. Corrupt journal authority stops startup before restoring an
actor. The fence covers turn admission, model dispatch, bound MCP execution and
persona signing. No source relationship, tool grant, run budget or imported
environment membership authorizes destination execution.

Normal task intake rejects a nonresident target before creating an environment
or scheduling work. Amendments and resumes retain their exact historical owner;
they reject a nonresident owner before successor grants or member fan-out. HTTP
target overrides require a fresh task and cannot be silently ignored by a
continuation. New wakes are refused at enqueue. If handoff starts after a
wake was queued, the existing turn-execution record reports
`identity_residency_unavailable` and the delivery settles without acquiring a
persona lease or entering a provider. Historical source runs remain exportable;
they do not publish the departed actor as a current source resident. Current
identity discovery belongs to the destination and its successor key.

`personaos-knowledge-bundle/3` extends `/2` with the prior handoff proofs; its
existing manifest binds that extra member. The shared historical verifier
accepts only the exact certified message hashes under their original issuers.
It grants no general authority to an old persona key or foreign kernel master.
Original parent and kernel birth evidence can verify without moving the parent.
Full source runtime records remain a private archive, exposed to that owner
through ordinary context references. Only recipient-authorized context references
with verified bytes enter the copied closure; a raw content hash is insufficient.
Missing or revoked sources remain explicitly unavailable. Reading the admitted
archive at the destination still requires current destination membership.

`GET`/`HEAD /identity-handoffs/<persona_id>` exposes only
`personaos-identity-residency/1` on a public node (or to its authenticated owner).
It contains the original identity, current host/key/epoch and minimal signed
fences. Private state and the historical message index are absent. A current
persona card and discovery record carry this same residency proof. Anonymous
readers verify native key-derived node identities, every consent and fence, and
the current destination pin before accepting an original DID on another host.
They can then verify retained public descriptors under their original keys.
This public presentation check grants no historical action authority. Anonymous
resolution of custom node aliases still requires an independently available pin.

## 15. Design criteria

1. Protocols carry exact authority and effects without selecting behavior.
2. Capability, memory, skill, and tool inventories are complete, paginated, and
   unranked.
3. Resume delivers the same signed resource event to every active member.
4. Replication effects and MIME are explicit signed facts.
5. Domain references are plural and non-semantic to the kernel.
6. Optional identity, notes, and gap-like content never gate ordinary work.
7. Objective completion comes only from exact authenticated acceptance
   authority.
8. Quiescence is nonterminal.
9. Coordination and prompt projections preserve exact totals, cursors,
   omission/truncation evidence, and content-neutral ordering.
10. Mechanical admission cannot become semantic behavior selection.
11. Ambiguous multi-model bootstrap fails closed without a matching signed
    persona choice.
12. Append paging preserves exact positions, cardinality, and duplicate
    accounting.
13. Persona-authored verdicts are signed key facts that enter acceptance only
    through declared verifier authority and mechanical invariants.

## 16. Open questions

- **OQ-PROTOCOLS-1** — Staged resumable capability provisioning: persist the
  provisioning staging directory keyed by recipe hash, record a per-build-step
  completion receipt, and let a later funded turn resume the remaining steps
  before smoke execution, verification, and freeze. This changes acquisition
  semantics — mutable cross-turn state, partial-failure receipts, per-stage
  budget accounting — and is deferred.
