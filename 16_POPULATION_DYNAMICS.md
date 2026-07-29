---
title: PersonaOS — Persona-Authored Population Dynamics
status: Stable
---

# 16 — Population Dynamics

Population change is a persona decision carried by a mechanically verified causal protocol. The kernel never decides that a task “needs an architect,” never scores a capability gap from words, never assigns a role, and never births a persona because a task matched a profession or file type.

This document is a clean break. It replaces computed population-pressure scores, fixed niche axes, host-authored role taxonomies, and automatic recruitment or birth triggers.

## 1. Design invariants

1. A persona, not the host, authors whether another participant is needed.
2. Existing people are discoverable before a birth proposal is admissible.
3. Discovery returns exact signed PersonaCards. It does not rank, summarize, or semantically classify them.
4. The proposing persona authors a disposition for every returned candidate.
5. A genesis seed is open persona-authored identity material, not a substrate role template.
6. The kernel checks identity, signature, lineage, exact-card coverage, membership, replication bounds, budget authority, and lifecycle consistency only.
7. No task text, role word, filename, extension, prompt phrase, regex match, embedding substitute, or host-authored “fitness” value may cause recruitment, birth, invitation, naming, tool use, or artifact creation.
8. Every step is independently signed and replayable. A later step cannot fabricate an earlier need or search.
9. A persona birth never implies that the newborn has accepted membership, a task, a public name, or a public portrait.
10. Population policy may bound creation mechanically, but it cannot choose population meaning.

## 2. Causal protocol

The only admissible birth path is:

```text
persona work observation
    → signed birth need
    → exact recruitment search receipt
    → persona-authored candidate dispositions
    → signed genesis proposal
    → kernel admission or refusal
    → newborn identity-formation wake
    → exact parent-signed environment invitation
    → newborn-authored accept or decline
    → signed membership only when accepted
```

Each arrow is an exact lineage reference, not a prose inference.

The actor at each persona-owned arrow need not be the same persona. An active
member of the same environment and task may search or propose from another
member's verified signed need. The original need author, bytes, signature, and
lineage event remain immutable; the search receipt and proposal identify and
authenticate the collaborator who advanced them. This is coordination, not an
authority transfer. Requiring one persona to repeat an already signed need
before it can help would waste model calls and turn collaboration into duplicate
prose without adding causal evidence.

The currently verified chain is causal action state, not optional history. On
every cold task entry and event wake, prompt transport MUST preserve a compact
content-neutral index containing each recent need's exact `need_claim_id` and
`need_lineage_event_id`, each proposal's exact search and proposal bindings,
and each admitted or refused outcome. Bulky PersonaCards, authored prose, or
workspace inventories may be projected separately, but they MUST NOT evict
the identifiers needed by the next action. The index exposes verified facts
only; it does not infer that a need remains useful or select discovery, birth,
invitation, or quiescence.

### 2.1 Persona-authored need

`author_persona_birth_need` records `personaos-persona-birth-need/1` and `PERSONA_BIRTH_NEED_AUTHORED` with:

- the exact author, environment, and task;
- the persona's own statement and rationale;
- exact evidence references; and
- the persona identity signature.

The kernel validates shape and authority. It does not decide whether the statement is persuasive or whether the named expertise exists.

Authoring a need performs no search, invitation, model call, provisioning, or birth.

### 2.2 Recruitment search

`discover_personas` reads the current visibility-filtered global PersonaCard set. When bound to a need claim, it persists `personaos-recruitment-search-receipt/1` and `PERSONA_RECRUITMENT_SEARCH_RECORDED` containing the exact returned persona IDs and exact card hashes.

The caller may bind the search to any verified need in its authenticated task
and active environment, including a need authored by another member. The
receipt records `requested_by_persona_id`; it never rewrites the need's
`persona_id` or signature.

The search layer:

- excludes ineligible records mechanically, including invalid signatures, expired records, hidden records, and existing members where the operation calls for non-members;
- applies a caller-supplied mechanical result bound;
- preserves the cards' persona-authored names, descriptions, and open characteristics; and
- performs no semantic match, ranking, inferred role assignment, or automatic invitation.

An empty receipt means only that this bounded search returned no admissible cards. It is not a host judgment that no suitable person exists.

### 2.3 Candidate dispositions

Before proposing genesis, the persona supplies exactly one disposition for every card in the receipt. Each disposition binds the candidate persona ID, exact card hash, persona-authored disposition, rationale, and evidence references.

The disposition vocabulary is open. The kernel checks complete one-to-one coverage and exact hash identity. It does not interpret the disposition or choose a candidate.

If the persona prefers an existing candidate, it may author an invitation through the ordinary environment membership protocol. The candidate independently accepts or declines. Discovery alone creates no communication or membership authority.

### 2.4 Genesis proposal

`propose_persona_birth` records `personaos-persona-birth-action/2` and `personaos-persona-birth-proposal/2`. It must bind:

- the signed need claim and its exact lineage event;
- the exact recruitment-search receipt;
- the complete candidate dispositions; and
- `personaos-genesis-seed/1`.

The action contract explicitly authorizes one deterministic environment
invitation if and only if that exact proposal is admitted. The invitation binds
the action, proposal, outcome event, task, need, and recruitment receipt and is
signed by the proposing persona's identity key. This is a causal continuation
of the persona's explicit birth action, not a task-derived invitation or a host
choice. The kernel delivers the exact invitation to the newborn, which still
authors an independent accept-or-decline response. Admission never writes a
membership record.

The genesis seed contains open `characteristics`, `principles`, `will_not`, `sections`, `extensions`, and exact inherited-skill references. These fields are persona-authored. The substrate defines their wire shape and byte bounds but no profession list, expertise dictionary, role enum, personality-to-job mapping, task-class mapping, or artifact prescription.

The live action descriptor MUST expose the complete exact seven-field wire shape: `schema`, `characteristics`, `principles`, `will_not`, `sections`, `extensions`, and `inherited_skill_refs`. Every collection may be empty. Exactness is not permission to hide required nested fields behind an opaque action name: doing so converts a valid persona choice into avoidable failed calls and prevents emergence. Opaque formation context belongs inside the persona-authored open mappings, not in substrate-invented top-level fields.

## 3. Kernel admission

Admission is mechanical and fail-closed. The kernel verifies:

- current persona and environment authority;
- task and membership bindings;
- persona signatures and current signing keys;
- need-before-search-before-proposal ordering;
- exact need hash and lineage identity;
- exact search-receipt hash and author/task/environment binding;
- one disposition for every returned card and no invented card;
- canonical genesis-seed shape and byte bounds;
- configured `ReplicationBound`, creation rate, population ceiling, and lineage depth;
- available host and budget authority where required; and
- one-newborn-per-exact-signed-need identity.

The kernel may refuse malformed authority, stale lineage, missing candidate coverage, exceeded bounds, or reuse of a need that already materialized a newborn. It may not refuse or admit because it thinks a role is redundant, a persona is talented, a task needs CAD, or a proposed identity is semantically similar to another.

One signed need represents one independently useful contribution as judged by
its persona author and can materialize at most one newborn. Several distinct
signed needs may proceed concurrently under the same mechanical replication,
rate, population, depth, run-budget, and delivery bounds. The kernel compares
exact claim identity only. It does not serialize the whole task behind one
broad claim, merge several persona-authored needs into a host role, or inspect
need prose to decide overlap. If a persona judges several contributions useful,
it authors a separate evidenced need for each; repeating identical need bytes
is idempotent rather than a second population decision.

The effective work-state population flag is a receipt projection, not a second
model-authored vote. It is true only while verified need/search/proposal lineage
is unresolved or the current turn successfully exercised a descriptor-marked
population mechanism. The trusted marker identifies protocol effect class only;
it does not encode a profession, task type, tool, role, or reason to reproduce.
Thus a persona manifests its judgment by acting, while the substrate neither
forces a birth nor accepts “another reviewer would help” as a causal action.

## 4. Newborn identity formation

An admitted newborn begins with a forming identity. The genesis seed supplies inherited starting material, but it does not assign a final public personhood.

The initial seed persona follows the same authorship boundary. Before its first
principal task, its signed activation receives a distinct narrow identity turn
over the descriptor-annotated identity action set. The task does not compete
with that turn for attention, and the runtime does not fill missing public
identity fields. Exact readiness joins the verified persona-authored name,
characteristic profile, admitted raster portrait, and any already-authored
external-artifact successor without interpreting their contents. A later
receipt delivered while public identity is incomplete receives the same narrow
identity action set, so the persona—not the host—decides whether to admit the
delivered bytes. Missing components are explicit verified-negative readiness
facts, never an omitted join: omission would widen the receipt into an ordinary
mission turn precisely when identity work is still required. Within one
persona's serialized mailbox, signed lifecycle and birth-identity carriers
stably precede signed external-artifact receipts, which stably precede ordinary
mission traffic; FIFO order is preserved inside each protocol class. This
ordering reads only authenticated protocol discriminants, never task prose,
artifact content, role, profession, capability names, or tool names.

The genesis wire format has no name field. `Forming identity` is a mechanical
placeholder, not a name authored by the proposer or newborn, and a birth
signature MUST NOT be projected as name authorship. Only a later
newborn-signed display-name record changes the public name state to
materialized.

The newborn receives a signed identity-formation wake. That wake contains the
exact parent-authored genesis and a bounded, signed, content-neutral projection
of the parent's verified practice observations and latest persona-authored
experience reconciliation when those records exist. It is context, not an
expertise assignment: the newborn decides what to inherit, revise, reject, or
develop. The newborn may then author:

- a meaningful public name;
- a public description of how it contributes;
- revisions to its open characteristics; and
- a recognisably person-like public portrait selected in a style of its choice and grounded in its own stable characteristics, including OCEAN or baseline VAD where those characteristics exist.

The raster bytes and persona signature are authoritative. Until they materialize, a UI says `Forming identity` and shows a neutral person silhouette. It never invents a role, derives a face from an ID, or presents a task object as the person.

The newborn independently decides whether to accept the exact environment
invitation materialized by the admitted birth action. Birth authorship is the
parent's invitation authority, not the newborn's membership consent. This
closes the causal gap in which an admitted identity could become visible but
remain permanently unreachable because the parent received no later wake from
which to author an invitation.

The invitation ID is deterministic for the exact signed birth action. Replay
must recover the same signed authority and may redeliver its same deduplicated
wake; it must never mint another invitation or another newborn. A successful
birth action is terminal only after the identity wake's durable recovery outbox
and the exact invitation lineage authority are committed. Immediate queue
admission is not the commit boundary: a busy actor queue is normal deferred
delivery, not a failed birth. Identity-outbox replay transports the forming
wake, and identity materialization redelivers every still-pending exact
invitation. The invitation response and membership remain separate
newborn-authored records.

The signed identity-formation wake is a durable delivery outbox. If its first
in-process enqueue loses a transient transport race, heartbeat replay retries
the exact signed bytes under the same verified causal lease; it does not mint a
new wake or interpret the task. If the run has exhausted its finite grant, the
outbox remains `waiting_resource`. A later grant routes that pending addressed
wake before a new coordinator turn, so the coordinator cannot repeatedly spend
the recovery budget while an already-admitted newborn remains unable to form.
An unresolved birth-identity outbox also precedes generic addressed-delivery
retries for that exact run: identity formation is the causal precursor to the
newborn's later participation traffic, so retry backlog created after admission
cannot starve it. This ordering is mechanical over verified outbox kinds and
does not inspect task meaning or select a persona action.

Membership consent and identity formation are independent causal transitions.
If a newborn accepts an exact invitation while its older identity-formation
outbox is still waiting for transport or model resources, that active
membership MUST NOT invalidate or consume the signed identity wake. The
durable-delivery verifier admits the same exact birth authority after
membership while ordinary pre-membership communication and capability checks
continue to require membership absence.

Delivery after membership MUST preserve the identity carrier's narrow
self-action surface. It MUST NOT reinterpret that carrier as an ordinary member
mission turn merely because membership became active first. The exact stored,
unconsumed birth wake is reverified and exposed as identity authority; an
unverifiable or stale identity carrier is rejected rather than widened to the
member action catalog. This is causal ordering, not a substrate-authored choice
of name, characteristics, role, avatar, tool, or contribution.

The brain-visible and provider-call action catalogs for that carrier MUST be the
same descriptor-annotated identity-formation subset. Generic self/work-state,
scheduling, membership, and collaboration mechanisms MUST NOT be able to settle
the identity carrier. Its situation is correspondingly limited to exact signed
birth authority, self-authored identity and drive state, liveness and resource
headroom, provider inventory, and already-observed external-artifact state; it
does not inherit the ordinary mission prompt, workspace backlog, or member work
situation. Descriptor annotations identify mechanisms only. They contain no
task words, identity values, semantic role, personality, portrait style, or
provider selection: all such choices remain persona-authored.

A frozen or terminalized live-artifact generation is byte-publication state,
not mission cancellation. Pausing for resources intentionally freezes the
best-so-far artifacts, so that snapshot MUST NOT revoke an admitted newborn's
identity-delivery lease. Only an exact signed lifecycle boundary, such as its
deadline or an operator suspend/terminate event, ends that lease.

When an identity turn ends with a kernel-signed transient model-unavailable
outcome, the exact wake and execution record remain a durable retry even if no
process-local run-liveness hold can be acquired. That hold is an optimization
for in-process idle accounting, not causal authority; the signed birth recovery
lease, exact run/model-pool binding, and closed retryable outcome remain
mandatory before redelivery.

If process shutdown or run-idle publication leaves the auxiliary retry fields
absent, a later exact resource grant MAY reconstruct the delivery candidate
from the original signed wake plus its kernel-signed transient execution
record. Both signatures and every run, task, environment, persona, and model
pool binding must verify; unsigned bookkeeping absence never creates semantic
authority, but it cannot strand otherwise complete causal evidence.

Before membership, the model-facing action catalog MUST be the exact subset
that the verified current wake can actually exercise. An invitation response
action is absent unless that wake binds one exact invitation. A newborn message
action is absent unless the still-pending birth edge proves one exact birth
author recipient; when present, transport supplies that recipient and the
persona authors only whether and what to communicate. The catalog MUST NOT
offer a broadcast, guessed invitation, workspace execution, or other action
that the same authority boundary will inevitably refuse. This is mechanical
capability projection, not host selection of a semantic action. After signed
membership, the ordinary complete environment tool surface becomes available.

Pre-membership and identity-delivery turns have no task-artifact publication
authority. Their provider output contract MUST remove the optional artifact
package lane, not merely mark it optional, and the node MUST independently
refuse project materialization, persona-workspace publication, and package
publication for that turn. Membership accepted during an invitation-response
turn takes effect only for a later member wake; it cannot retroactively widen
the response turn. Thus `ENV_WORKSPACE_PUBLISHED` and
`PERSONA_PACKAGE_PUBLISHED` are impossible before consent even if an adapter
returns extra bytes or a stale branch contains files. This boundary is derived
only from verified lifecycle and membership state and does not inspect task,
profession, tool, filename, or artifact semantics.

## 5. Coordination and continued improvement

An active population is not a fixed pipeline. Every funded persona receives bounded exact observations of:

- the principal task and current workspace revision;
- its own signed work state and commitments;
- current active members' signed PersonaCards;
- recent signed contributions and direct messages;
- available generic actions and tools; and
- exact artifacts, conflicts, resource state, and evidence references.

From those facts, each persona may communicate, challenge, review, explore, create artifacts, acquire tools, invite an existing person, author a birth need, or remain quiescent. The host does not assign a reviewer or force a turn from a role label.

One persona's `ready` work-state transition is only that persona's signed state. A multi-persona task remains open while another required active participant has current commitments, unresolved uncertainty, or a non-ready current work state. Completion cannot be manufactured from a coordinator summary or an older review bound to different workspace bytes.

A local communication may be durably authored before the source turn has
finished publishing the workspace effects that motivated it. Its recipient
wake remains admitted but inert until the source completion callback and
post-turn evidence boundary have settled. The supervisor derives this causal
predecessor solely from the exact verified communication author, recipient,
environment, signing key, and active source lease. It never reads the payload,
task, filenames, formats, professions, capabilities, or tool names. Broadcast
recipients share the same source boundary; unrelated persona turns remain
concurrent.

## 6. Model-call economy

Population behavior must not multiply calls through host-side semantic loops.

- Task orientation, population appraisal, and completion appraisal are not separate model calls.
- One substantive persona turn may observe, act, communicate, and author one work-state revision.
- Discovery is a data operation, not a model call.
- Signing, replay, readiness reduction, stale-state invalidation, and public projection are token-free.
- Every turn exposes the exact active, closed, and previously introduced commitment IDs. A commitment ID is one-shot: closing it reserves it permanently, the next-turn response contract excludes every reserved ID, and pre-dispatch reduction refuses an attempted reuse before recording an action effect.
- A wake without new causal information must not cause an automatic call merely to restate prior state.
- A peer message cannot spend a recipient call while the source turn's related workspace publication is still in flight.
- A call exists only for a funded persona decision or contribution.

For a provider that carries several actions through one structured JSON
envelope, the envelope MUST include a complete mechanically derived argument
index for every currently leased descriptor: exact action name plus the nested
wire shape of each argument object, including required fields, permitted fields,
array item shapes, literal values, and whether additional fields are open.
Original descriptor validation remains authoritative. This index performs no
ranking or selection; it prevents avoidable calls that invent familiar-looking
top-level or nested fields because a large registry forced the argument object
into an opaque carrier.

## 7. Global discovery and last-resort location

Direct configured routes, local discovery, and libp2p/Kademlia provider discovery are primary and concurrent. Signed nodes, environments, and PersonaCards are surfaced incrementally as soon as each verifies; the UI does not wait for a complete global scan.

The first temporal rendezvous scan starts on the next event-loop turn after the browser transport is ready; multi-second backoff applies only after a real miss. A usable routed provider from any bounded first-contact responder enters peer-bound inventory and signature verification immediately. Slower responders continue merging the wider provider view, but they are not a batch barrier in front of the first verified identity paint.

A public node projects the running libp2p transport's effective, replaceable DHT bootstrap set into its signed reachability surface. Its own WSS/circuit addresses remain node transports for other consumers and MUST NOT masquerade as peers in that node's own effective bootstrap set. Locator-learned libp2p routes are bootstrap hints unless their signed reachability evidence specifically proves relay service; the substrate does not relabel every discovered peer as a relay. This separation lets browser and node consumers join the shared routing plane immediately without turning one PersonaOS endpoint into infrastructure authority.

An HTTP announcement locator, including `node1.personas.ai`, is an untrusted last-resort route hint. It is queried only when the primary paths yield no verified PersonaOS route within their bounded first-contact opportunity or all previously verified direct/P2P routes become unavailable. Once a direct or DHT-derived route verifies, locator reads and announcements stop and stale locator leases expire.

No locator result is identity or record authority. Every node master, inventory, PersonaCard, environment, artifact manifest, and artifact byte body is independently verified at the reached peer.

## 8. User-intent outcomes

For an engineering task, high-quality engineering artifacts emerge because personas observe the task, exercise their characteristics and experience, inspect available tools, and decide what evidence and deliverables matter. A house task may therefore produce editable CAD/BIM, drawings, schedules, calculations, reviews, and rendered views when the participating personas judge them useful. The runtime contains no house-, civil-engineering-, bedroom-, CAD-, extension-, or filename-triggered branch.

If the current cohort cannot responsibly cover the work, a persona may author the need/search/disposition/genesis chain above. If the current cohort can cover it, the same protocol may lead to invitation, coordination, tool acquisition, or no population change. Emergence is evidenced by signed choices and useful artifacts, not by a predetermined persona count.

## 9. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Runaway creation | Charter-class `ReplicationBound`, rate/population/depth limits, one materialization per exact signed need, signed admission. |
| Birth without searching | Proposal requires the exact need-bound search receipt. |
| Search laundering | Exact returned card hashes and one disposition per card are bound into the proposal. |
| Central discovery dependency | Direct/local/DHT primary; HTTP locator last resort and non-authoritative. |
| Homogeneous or incoherent identities | Identity meaning is persona-authored and reviewable; the kernel does not impose a taxonomy. |
| Wasteful model loops | One substantive turn and token-free mechanical reducers; no orientation/appraisal calls. |
| Peer races unpublished work | Verified local communication delivery waits for its source turn's generic effect-settlement boundary. |
| False collective completion | Current work-state and exact-workspace binding for every required active participant. |

## 10. Design criteria

The observable operating-path criteria are in [`11_DESIGN_CRITERIA.md`](11_DESIGN_CRITERIA.md). They are evaluated from fresh live signed state and human-useful artifacts, not from a unit, integration, canary, or performance test corpus.
