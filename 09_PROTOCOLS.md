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

1. Every authority-bearing record is canonical, bounded, signed, replayable,
   and bound to exact subjects and scopes.
2. Descriptors declare mechanics and effects explicitly. The runtime never
   derives them from names, prose, arguments, prompts, task words, filenames,
   extensions, executables, professions, regular expressions, media types, or
   domain vocabulary.
3. Inventories are complete within explicit pagination/truncation bounds and
   unranked. Stable ordering is transport order only. Append-derived pages
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
- exact bounded input and output schemas;
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

An authenticated workspace is publication authority and the default execution
base, not an authored working-directory choice. When an action schema exposes a
working-directory argument, a persona-provided value survives transport;
relative values resolve from the authenticated workspace. With no authored
value, the handler uses that workspace itself. In either case only effects
inside the authenticated workspace can be published as task artifacts. The
dispatcher never replaces a persona-authored working directory with a host
path, and the host workspace identifier is absent from persona-authored action
bytes.

### 2.1 Exact unranked inventories

The model-visible situation and inspection actions expose bounded paginated
complete inventories of:

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

When the provider supports native MCP tools, `tools/list` exposes every exact
leased action under its real name with its complete persona-facing description,
input schema, and structural annotations in the signed action-index order.
`tools/call` dispatches that same name through the existing principal- and
descriptor-bound node boundary. A generic catalogue inspector plus string-based
invoker is non-conformant because it hides every actual choice behind a second
model selection problem and makes the advertised action count differ from the
provider-visible surface.

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

When an adapter requires an in-prompt structured catalogue, it carries every
exact action identifier and applies one identical content-blind description
window to every registry or persona-authored descriptor. Ordinary registry
descriptions fit whole in that window. Any oversized description carries an
explicit incomplete flag and its exact descriptor remains independently
addressable. The window cannot vary by action name, task, role, domain, prior
use, tool, or inferred importance. A catalogue that repeatedly cuts
descriptions before their effect, acquisition, or successor mechanics are
visible is addressable but not practically navigable and is non-conformant.

The adapter verifies native provider events against the exact Cartesian surface
of current server identity and leased action names. A result counts as an
authenticated action only when the node receipt binds that same direct name and
environment. Transport wrappers around one backend observation are coalesced by
their exact mechanical observation identity before experience accounting; they
never become repeated practice merely because several routers retained them.

### 2.2 Persona navigation

A persona may inspect an exact descriptor, use an already mounted action,
communicate with an owner, share an exact record ref in `persona_message`,
obtain an authorized body, search an authorized registry or internet source,
acquire or provision a tool, author one opaque knowledge record, invoke a tool,
delegate, or ignore the inventory. Those are ordinary signed actions and may
occur in any persona-authored order.

A capability gap is optional meaning a persona may express in opaque knowledge
content. There is no dedicated gap action or lifecycle. Expressing, revising,
resolving, or omitting that meaning never changes another descriptor's schema,
action visibility, completion, or wake authority.

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
signature. Discovery does not carry the body or an arbitrary locator. Under a
current publication and public-read grant, the publication id mechanically
derives a bounded peer-body route whose provider-signed envelope binds the
exact discovery record and publication. This transport does not create a
semantic `skill` subtype, task match, recommendation, or executable authority.

`acquire_global_capability` accepts only an exact current verified catalogue
record id and its expected body/envelope hashes. It fetches the derived route
from that record's signed peer base, rejects a changed network origin, consults
no central rendezvous fallback, and independently verifies the provider key,
host identity, author key, publication signature, source identity, sizes, and
hashes. The exact authenticated action and verified envelope are retained in
signed environment lineage. Structural executable-tool bodies are passed as
opaque portable recipes through the ordinary provisioning and verification
boundary; structural persona-state bodies are retained without automatic
application. `inspect_acquired_capabilities` exposes a complete mechanically
ordered summary inventory plus exact-id, JSON-pointer, and byte-window reads.
No field in either action expresses a domain, profession, task match, preferred
provider, required capability, teacher, curriculum, or expertise award.

### 2.3 Receipts and retry

Every authenticated action receives one kernel-signed terminal outcome bound to
the action identity and exact effects. A successful receipt proves only what
ran, which provider/descriptor ran it, its terminal result, and which bytes or
records changed. It does not prove semantic relevance, artifact quality,
independent review, competence, or expertise.

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

A descriptor-declared asynchronous result creates a later turn only through its
exact registered event. Successful tool, population, capability, identity, or
experience actions do not automatically schedule cognition.

### 2.4 Signed model ceiling and persona-authored order

`run-model-pool/1` is the signed unordered per-run ceiling. Its signed fields
are exactly `schema`, `run_id`, `available_model_ids`, `minted_at`,
`signing_key_id`, and `signed_by`; the model IDs are duplicate-free and sorted
for canonical signing, and `pool_hash` is derived from the signing payload.
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
first substantive call may proceed only when current mechanical admission
leaves exactly one callable model. If two or more remain, routing fails closed.
Provider/registry/configuration insertion order, canonical sort order, default
clients, cost/tier heuristics, and a host-selected choice-authoring transport
are not authority to break the tie. A signed exact one-model pool is the normal
unambiguous bootstrap; declared fallbacks follow only a matching persona choice.

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

### 4.1 Exact resume fan-out

When a resource event resumes an environment task, the exact signed event bytes
and event/content hash are offered concurrently to every active member under the
same bounded resource pool. The substrate does not send only to a workspace
owner, coordinator, oldest member, named role, or selected representative.

Each recipient receives its own signed delivery carrier and deduplication/
settlement identity, but all carriers bind the same source event. A recipient
may act, communicate, schedule itself, or make no call. Fan-out has no objective
completion meaning and does not require identical behavior.

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

If bodies on that page exceed the prompt carrier,
`personaos-active-peer-contribution-prompt-projection/1` preserves source
schema/snapshot/metadata/record-manifest hashes, source totals, page and
omission/cursor facts, projected/omitted/truncated record counts, exact per-
record hashes and byte lengths, and the byte bound.

### 4.3 Exact uniform prompt-source manifest

If the entire prompt exceeds its byte carrier, the runtime uses
`personaos-uniform-prompt-source-stage/1`. It binds original/current byte bounds,
exact `source_total`, source-byte total, full source-manifest hash, schema-record
source total/hash, cursor range, content-hash source order, and the fact that
source byte allocation was uniform.

Its `personaos-prompt-source-manifest/1` binds `total`, `cursor`, `returned`,
`next_cursor`, exact descriptor records, `omitted_count`, `complete`, and an
omitted-manifest hash when incomplete. Each
`personaos-prompt-staged-source/1` retains its source cursor/identity/hash/byte
facts, projected value, projected byte count, and `projection_complete`.

The stage separately reports staged, projection-omitted, and projection-
truncated counts, `next_source_cursor`, and `complete`. When applicable,
`personaos-prompt-source-omission/1` and
`personaos-prompt-source-truncation/1` bind the exact omitted/truncated counts
and descriptor/cursor manifest hashes. A carrier with any omission or
truncation cannot claim completeness.

Source IDs and uniform byte division are content-neutral resource mechanics,
not semantic priority. The substrate does not reserve more prompt space for a
task field, persona, role, message, tool, memory, schema kind, or record whose
prose appears important. Manifests make every omitted source/window navigable
without silently replacing it with a host summary.

A canonical situation assembled from sources already present in dedicated
prompt lanes enters this stage only through
`personaos-current-persona-mission-situation-facts/3`: exact situation/lineage
identity, canonical size, a complete field/type/hash/size/schema manifest, and
the exact task facts needed for continuation-context binding. The prompt does
not re-inline the joined environment, package, team, resource, action,
population, workspace, learning, capability, identity, or work-state bodies.
This is equality-preserving transport deduplication, not semantic omission: the
component preimages remain in their independently verified lanes and the full
situation remains bound by its durable content hash.

All totals are cardinalities of the bound source snapshot, not counts after an
undisclosed payload deduplication. Cursor movement follows the declared order
exactly and preserves every distinct source position.

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
`event_authority_complete`, `event_authority_max_bytes`, and
`event_authority`. Authority bodies are carried exactly through 65,536
canonical bytes; beyond that, the body is an explicit `{content_hash,
content_bytes, omitted: true}` pointer.

`personaos-communication-routed-wake-delivery-snapshot/1` uses exactly the
shared page fields. It retains, in exact input order, each original routed
result whose `persona_wake_delivery.enqueued` is true and whose `wake_event` is
a mapping. Its snapshot identity binds persona, environment, and task; its
cursor namespace is `communication-routed-wakes` and its page size is 64.

## 5. Global discovery and distribution

Local routes, configured direct peers, libp2p/Kademlia provider discovery,
rendezvous, and gossip may operate concurrently. Each verified node,
environment, persona, skill/tool metadata record, and artifact manifest is
streamed as soon as its independent signature and authority checks succeed.
Consumers do not wait for a complete global scan or the slowest responder.

Discovery records include exact subject, provider, content hash, visibility,
policy, expiry, revocation, signature chain, and reachable content locators.
Discovery proves where verified bytes may be found; it does not grant access,
membership, execution, truth, expertise, or relevance.

An HTTP locator, including `node1.personas.ai`, is a replaceable last-resort
first-contact hint. A node reads from or announces to it only when no primary
route is viable, and stops both operations once a primary PersonaOS route
verifies. Locator leases are short, signed, source-scoped, and
non-authoritative; when primary discovery recovers, the last fallback lease
expires without renewal. Producer and consumer fallback decisions use the
node's same mechanically observed non-locator viability state.

The locator announcement's `record_count` is bounded signed metadata about the
remote node's complete inventory; it is not a bundled record collection and
does not allocate, transfer, or cache that many objects. Locator admission may
enforce the protocol-wide integer ceiling, but cannot reject a valid node merely
because its count exceeds a local page, cache, or obsolete bundle-size setting.
Inventory transport applies its own independently bounded pagination.

Transport startup and route convergence are distinct facts. A connected DHT,
successful provider publication, or an observer acknowledgement proves that a
rendezvous record left one process; none proves that an independent PersonaOS
consumer resolved, dialed, authenticated, and consumed a route. Producer-side
suppression therefore requires current independently verified peer discovery,
not publication visibility alone. A consumer gives direct and peer routes one
bounded first-contact opportunity, uses the locator only while it still has no
verified usable route, and continues decentralized reconciliation afterward.
Neither timeout nor connected generic peer count is identity authority.

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

## 6. Artifacts and explicit signed MIME

Every artifact declaration binds an explicit normalized parameter-free
`mime_type`, exact content hash, byte length, author/owner, environment/task
scope, artifact role, and zero or more `domain_refs` inside its signed payload.
MIME authority travels with the bytes through publication, discovery, fetch,
cache, and rendering.

Filename and extension are presentation metadata. Byte sniffing and a suffix
may detect a mismatch or select a safe fallback, but cannot silently overwrite
the signed MIME declaration. A renderer verifies content hash, length, MIME,
scope, and access before lazy loading the applicable parser.

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

`author_persona_knowledge` accepts only persona-authored bounded canonical
`metadata` and optional distinct exact `refs`. Authenticated dispatch supplies
persona identity and verifies any optional environment/task binding. One
invocation persists one signed existing
`personaos-persona-state-record/1` with exact `schema`, `record_id`,
`persona_id`, `environment_id`, `task_id`, mechanical
`record_kind: "persona_knowledge"`, opaque `content`, `evidence_refs`,
`issued_at`, `signing_key_id`, and `signed_by`.

The verified record, including its opaque content when it fits the ordinary
per-record carrier bound, participates in later same-environment Layer-4 pages.
Its original task remains provenance rather than a visibility fence. Oversized
or out-of-page records retain exact hashes and cursors instead of receiving a
host summary. This is accumulated persona-authored knowledge, not an active
brain tactic: brain-fragment evolution and binding remain separate explicit
persona decisions.

The ordinary cognition carrier includes a fixed append-position suffix of
exact verified owner-authored records and their opaque bodies. It declares the
complete source count, selected range, and content hashes while leaving the
full append lane cursor-addressable. Selection reads no task, domain, role,
record content, tool identity, outcome, quality, or similarity signal. Carrying
the exact suffix is continuity of persona-authored experience; it neither
selects a lesson nor grants expertise, activates a tactic, recommends a tool,
or schedules behaviour.

General learning-history and turn-effect pages use compact prompt references:
source/page/frontier hashes, exact totals and ranges, continuation cursor,
record counts, and explicit non-inline state. Their complete hash-only rows and
effect records remain available from the authenticated history inspector.
Repeating the same historical action-name trail on every wake consumes the
actor's navigation carrier without exposing the retained bodies and can anchor
new cognition to an old transport pattern. Compacting that repetition is a
mechanical equality-preserving projection; persona-authored state bodies keep
their independent exact append-frontier lane.

The current content-neutral storage envelope is 262,144 canonical JSON bytes
and nesting depth 64 for `metadata`; `refs` accepts one exact string or at most
32 distinct exact strings of at most 500 UTF-8 bytes each. These limits protect
parsing/storage and carry no semantic knowledge or capability taxonomy.

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

Presentation requirements come only from exact authenticated principal/user
intent. The protocol has no default person-like portrait, name grammar,
profession field, OCEAN/VAD requirement, identity formation phase, or readiness
gate. Portrait declarations use the same explicit signed MIME and exact-byte
authority as other media.

## 10. Work notes, completion, and quiescence

`personaos-persona-work-state/4` carries a bounded open `work_note`, exact
observed-situation and append lineage, and one explicit signed
`personaos-persona-causal-disposition/1`. Protocols preserve it as one immutable
authored claim. They do not extract commitments, blockers, stages,
requirements, votes, readiness, or next actions from the note.

The persona authors open note content, optional causal references, and its
causal disposition. The disposition is either an exact deliberate
`no_successor` record or one exact `immediate_wake` request with persona-authored
opaque kind/payload and optional exact model-input paths. The signed request
binds the persona's path choices, not a speculative pre-settlement file read.
Only successor delivery—after the current persona turn has settled—observes
each selected path's exact size and hash and reports any unavailable or changed
bytes. This remains mechanical and performs no filename, extension, MIME, or
format inference. A generic selected file is not coerced into an image-only
provider attachment; it remains available through the authenticated workspace
and ordinary persona-selected inspection/execution tools. Media-specific native
attachments require their own independently verified carrier. The disposition
is never derived from note content. Record
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

## 11. Framework adapter contract

Adapters may translate PersonaOS records to external SDK, CLI, MCP, A2A, or
model-provider wire shapes. Translation must preserve:

- exact identity, task, environment, membership, and resource authority;
- every live action identity in ordinary navigation, a uniform bounded
  descriptor preview, and authenticated lazy access to each complete descriptor
  and its reserved bindings;
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

## 12. Observability

OpenTelemetry may report protocol kind, exact record/action identities,
durations, terminal transport status, byte counts, retry state, and lifecycle
transitions under current consent and redaction policy. Telemetry never becomes
task truth, persona intent, reputation, competence, objective acceptance, or a
trigger for population/tool behavior.

Prompt, message, memory, skill-body, artifact, and user content remain redacted
unless exact access and consent authority permits disclosure.

`personaos-persona-telemetry-public/2` is the small, current-master-signed
per-persona presentation feed. In addition to bounded public presence, model
status, activity, and verified communication routes, it carries either an empty
object or that persona's latest exact verified public
`personaos-persona-work-state-surface/4`. The nested note retains its persona
signature and remains an authored claim; the outer feed adds transport freshness
and route/subject authority only. The feed does not select a note by vocabulary,
infer a next action, judge readiness, or acquire completion semantics. Independent
persona feeds may be transferred and verified concurrently.

## 13. Schema registry and clean-break versioning

Every live boundary schema has one current registered version. Removed fields or
semantics require a new version; old messages are refused at current live
boundaries. This cutover deliberately provides no compatibility or migration
mapper for retired mission charters, structured work readiness, fixed genesis
seeds, ranked retrieval/prompt optimization, singular domain ownership, inferred
MIME, or undeclared replication effects.

Historical bytes may remain in archival lineage as opaque records. They acquire
no current authority merely because their signatures once verified.

Current cutover records include:

- `personaos-persona-work-situation/1`,
  `personaos-persona-work-state/4`,
  `personaos-persona-work-state-surface/4`,
  `personaos-persona-causal-disposition/1`,
  `personaos-persona-work-note-state/1`, and
  `personaos-work-state-evidence/1`;
- `personaos-persona-telemetry-public/2`;
- `personaos-persona-birth-proposal/5` and
  `personaos-persona-birth-proposal-record/2`;
- `personaos-persona-birth-causal-action-context/1`;
- `personaos-persona-birth-action-identity/1` as a deterministic ID preimage,
  not signed birth authority;
- `personaos-persona-birth-membership-binding/1` and
  `personaos-verified-persona-birth-context-snapshot/1`;
- `personaos-persona-birth-provenance/3` and
  `personaos-birth-identity-wake/4`;
- `brain-evolution-decision/1` and
  `brain-evolution-application/1`;
- `run-model-pool/1` and `persona-model-choice/1`;
- `personaos-persona-state-record/1` with mechanical
  `record_kind: "persona_knowledge"`;
- `personaos-coordination-context/3`,
  `personaos-coordination-lineage-snapshot/1`,
  `personaos-coordination-prompt-projection/1`, and
  `personaos-coordination-prompt-event-page/1`;
- `personaos-active-peer-latest-signed-contributions/2` and
  `personaos-active-peer-contribution-prompt-projection/1`;
- `personaos-peer-activity-lineage-snapshot/2`,
  `personaos-verified-peer-lineage-event/1`, and
  `personaos-communication-routed-wake-delivery-snapshot/1`;
- `personaos-uniform-prompt-source-stage/1`,
  `personaos-prompt-source-manifest/1`,
  `personaos-prompt-staged-source/1`,
  `personaos-prompt-source-omission/1`, and
  `personaos-prompt-source-truncation/1`; and
- `personaos-replication-effect-descriptor/1`.

## 14. Key custody

Master, kernel, environment, task/action, and persona keys remain separate
authority scopes. Public verification material includes exact key identity,
issuer/parent authority, validity interval, rotation, and revocation. A key may
sign only records authorized for its scope.

Rotation preserves verification of historical records while current writes use
the new key. Revocation prevents new authority and propagates to dependent
bindings according to signed policy; it does not rewrite immutable history.

Key custody implementation may use local encrypted storage, a cloud key service,
or hardware security module. Storage choice cannot change the protocol meaning
of a signature.

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
