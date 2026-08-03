---
title: PersonaOS — Kernel Substrate
status: Stable
---

# 01 — Kernel

The kernel is the minimal trusted substrate. It authenticates, authorizes,
verifies exact mechanics, transports causal events, enforces bounds, preserves
bytes and lineage, and settles declared effects. It never chooses persona
meaning, roles, workflows, tools, population strategy, or objective completion.

This document is a clean break from task classifiers, candidate FSMs, round
barriers, verifier cascades, claim scores, domain stages, prompt programs,
structured readiness, mission charters, and host-authored coordination loops.

## 1. Kernel authority

The kernel owns only:

- cryptographic identity, key scope, signature verification, and revocation;
- canonical bounded wire shapes and current schema admission;
- exact authorization, consent, access, lifecycle, and membership checks;
- immutable signed lineage, idempotent replay, and explicit supersession;
- causal event delivery, deduplication, leases, and settlement;
- byte, workspace, artifact, hash, length, MIME, and provenance verification;
- resource, time, call, rate, population, depth, and other mechanical bounds;
- explicit action-descriptor effect enforcement; and
- exact acceptance/stop/cancel authority supplied by the principal or an
  authorized verifier.

The kernel does not own a persona's identity description, task interpretation,
plan, current thought, role, profession, collaboration choice, capability
judgment, artifact choice, learning, population need, or next action.

### 1.1 Admission and selection are different powers

Mechanical admission may validate canonical byte/nesting/cardinality envelopes,
schema and hash integrity, signatures and key scope, exact membership/consent/
access, causal preimages, idempotency and replay, current leases, resource/time/
rate/depth/population ceilings, descriptor-declared effects, and exact current
external/physical/safety attestations. Bound values come from current signed
principal/operator/policy authority, apart from implementation envelopes needed
to parse and allocate safely; the kernel does not derive a bound or its value
from task meaning.

Those checks may refuse an effect a persona already chose. They cannot choose,
recommend, rank, or pre-hide which task interpretation, workflow, population
change, model, tool, skill, artifact, collaborator, or next action the persona
should attempt. A safety rule binds exact subjects, scopes, effects, and
authority—not words, inferred professions, prompts, roles, or desired outcomes.

## 2. Exact records and signatures

Every authority-bearing record has a current registered schema, canonical
bounded payload, exact subject/scope identities, signing-key identity,
signature, and immutable content hash. Bytes referenced outside the envelope
carry exact length and hash bindings.

Verification establishes that the authorized signer authored the exact bytes.
It does not establish semantic truth, relevance, quality, competence,
professional sufficiency, or completion.

An immutable later record may cite an exact predecessor through supersession.
The kernel validates identity and ordering without merging prose or deciding
that the revision is better.

## 3. Causal event model

A persona decision exists only because an exact authenticated event was
delivered under current lifecycle and resource authority. Event sources may
include principal/task ingress, persona-authored wakes/schedules, peer messages,
invitations, membership events, resource events, and explicitly registered
external/tool receipts.

Every causal edge retains its own signed identity, source, recipients/scope,
content hash, task/environment bindings, deduplication, lease, and settlement.
Plural valid successors coexist; the kernel does not choose a representative
next stage.

Work-note prose, gap-like authored content, population records, artifact changes, scores,
HTTP success, model output, and successful actions do not create another event
unless an exact action descriptor separately registered and delivered one.

### 3.1 Exact all-member fan-out

Task ingress and resource-resume events are delivered with the same exact
source-event bytes and hash to every active environment member under the same
bounded resource pool. Each recipient receives its own carrier/lease and may
act or not act.

The kernel does not select a coordinator, owner, lead, reviewer, role, oldest
member, or representative recipient. Fan-out carries opportunity and authority,
not a completion judgment or obligation to spend a model call.

### 3.2 Quiescence

When no causal delivery is pending, the affected task/persona is quiescent.
Quiescence is nonterminal and means only that nothing is currently scheduled.
It is not ready, complete, sufficient, abandoned, failed, or converged. A later
authentic event may resume the same identities and task.

## 4. Ordinary action surface

Every ordinary persona wake exposes the complete currently authorized unranked
action catalog. Exact prerequisites are checked at dispatch and cannot be used
to hide unrelated actions before the persona chooses.

The kernel must not rank, recommend, require, suppress, or synthesize an action
from task/domain/profession text, keywords, regular expressions, prompts,
filename, extension, MIME, role, characteristics, OCEAN/VAD, gap-like content,
work-note fields, population size, scores, embeddings, prior tool use, or
missing public identity.

Stable lexical/append ordering is transport order only. Pagination and
truncation are explicit and cannot masquerade as a complete inventory. An
append-derived page binds one snapshot and absolute append positions; equal
record bytes at different positions remain separate records. Redundant
observations of one exact signed identity across source scopes also remain in
the raw page. A separately labelled derived unique-identity view may normalize
them only under a declared exact equivalence rule, with duplicate cardinality,
source ranges, and raw-page navigation retained.

## 5. Action descriptors and effects

A live action descriptor binds exact action identity and hash, input/output
schemas, provider/authority bindings, mechanical effect annotations, terminal
result shape, retry semantics, signature, expiry, and revocation.

Reserved task, environment, membership, owner, workspace, and receipt bindings
are injected by trusted transport. Model-authored arguments cannot populate
them. Missing authority produces a signed refusal, not a host-selected repair
action.

An action causes only its declared authenticated effects. Names,
implementation, arguments, prose, task context, output filenames, and media
cannot create undeclared authority.

### 5.1 Replication effects

Every action capable of new actor materialization declares a signed
`personaosReplicationEffects` array of exact
`personaos-replication-effect-descriptor/1` records. Each carries one opaque
`effect_kind` used solely for ReplicationBound lookup.

The kernel never infers replication from an action name, executable, argument,
task, role, profession, prompt, file, MIME, domain, or result. A descriptor
without the effect cannot materialize an actor.

## 6. ReplicationBound

ReplicationBound applies only to explicitly declared replication effects. Its
mechanical axes may include population ceiling, creation rate, ancestry depth,
and required cosigns. Exact operator/principal policy supplies current bound
values; the substrate supplies the invariant enforcement shape.

Admission checks descriptor effect, bound identity, exact counters, causal
proposal/action identity, signatures, resources, and idempotency. It does not
judge why replication is useful, infer a niche or role, score fitness, choose a
parent, or author a birth.

`replication-bound/2` signs declared limits and authority only. Live
population, rate-window, and ancestry-depth counters are sampled from current
verified state at each admission check. They are not copied into the
long-lived bound: a declaration-time counter becomes stale after restoration
or any admitted effect and cannot be presented as current population authority.

## 7. Resource authority and model calls

Every model call consumes one exact causal carrier under an exact resource/model
pool grant. Resource state is observable fact. It does not become exploration
pressure, population pressure, completion, or a semantic continuation trigger.

Budget exhaustion preserves exact pending deliveries and best-so-far bytes and
projects a pause. A later signed resource event resumes the original generation
through all-member fan-out.

Mechanical projection, discovery, signature verification, replay, workspace
sync, inventory pagination, MIME/hash checking, fan-out, and UI rendering use no
model call.

Effect-free transient provider failure may retry the exact carrier under
bounded policy. Deterministic malformed requests are not infrastructure
outages. Effectful or uncertain turns are never replayed to obtain improved
prose.

A provider result that reaches the strict response boundary but cannot be
decoded against its advertised structured-output carrier is an effect-free
schema violation: no persona action has been dispatched. The same persona,
model, causal carrier, descriptors, and schema may receive one mechanical
reformat attempt, charged as another call to the same finite run. A second
failure is dropped as malformed output. This retry does not add repair prose,
choose a different action, substitute another model, or replay an effect.

### 7.1 Exact model ceiling and persona choice

`run-model-pool/1` is a signed per-run unordered ceiling. Canonical sorting of
its model IDs is serialization, not preference. `persona-model-choice/1` is the
persona-signed exact order and reasoning effort for one persona, environment,
task/candidate/mission task, run, pool hash, and situation generation.

Before a matching signed choice exists, a substantive call is admitted only if
current mechanical eligibility leaves exactly one callable body. More than one
eligible body is unresolved authority and fails closed. Registry or provider
insertion order, lexical order, a default client, price/tier heuristics, and a
host-selected bootstrap body cannot break the tie. A principal-authorized exact
one-body pool is unambiguous; later fallbacks follow only the matching signed
persona choice and remain subject to mechanical admission.

## 8. Workspace isolation and settlement

Every participant worktree and action lane is bound to exact persona,
environment, task, source event, turn lease, and entry revision. Byte capture,
publication, and settlement preserve exact authorship and temporal order.

Peer publications can advance shared environment state but cannot appear
retroactively as the current actor's tool effect, artifact, practice, or
authorship. Conflicts preserve all exact path/hash alternatives; only an
authorized signed resolution chooses or synthesizes bytes.

A workspace change may invalidate an exact preimage required by a not-yet-
admitted action. It never makes an immutable work note stale or pending
settlement. A note surface may report only whether its observed-situation hash
equals the latest observed hash; that equality has no semantic meaning.

## 9. Artifacts and signed MIME

Every media/artifact declaration signs normalized parameter-free `mime_type`,
exact content hash, byte length, owner/author, scope, artifact role, provenance,
and complete plural `domain_refs`.

The kernel verifies exact fetched bytes before publication or interpretation.
Filename, extension, path, domain kind, prompt, or byte sniffing cannot replace
signed MIME or role authority. Safe inspection may detect mismatch and force a
conservative fallback.

## 10. Persona identity boundary

Persona continuity comes from `persona_id`, signing-key lineage, lifecycle,
formation provenance, and membership. Public display name, biography,
characteristics, portrait, and style are optional persona-authored material.

Missing public fields never block discovery, membership, work, communication,
tools, or artifacts and never create an identity repair wake. Public
presentation requirements apply only when exact authenticated principal/user
intent supplies them. The kernel has no face, name, profession, style,
OCEAN/VAD, or portrait-prompt constant.

## 11. Work notes and capability-gap meaning

`personaos-persona-work-state/3` carries an optional bounded open `work_note`
with exact lineage and causal references. The kernel validates mechanics and
does not interpret keys or values. Notes never cover requirements, vote on
completion, determine readiness, schedule continuation, or change authority.

Notes are immutable append-only records. Revision/prior-record pointers order
verified appends without replacement semantics. Workspace settlement and later
observations do not defer, settle, reclassify, or mutate them;
`bound_to_latest_observation` is exact hash equality only.

Perceived capability gaps are optional meaning inside opaque persona-authored
knowledge. There is no dedicated gap record/action/lifecycle. Gap-like content
does not gate work, identity, acceptance, completion, action visibility, or a
wake. The kernel never derives gap state from task content, files, tools,
prompts, or notes.

## 12. Knowledge, skills, and population facts

The kernel exposes bounded paginated exact unranked inventories of visible
actions, local execution names, tools, skills, memories, knowledge, personas,
and population records. It validates access and signatures without scoring,
ranking, summarizing, recommending, retrieving top-K, or choosing a teacher,
tool, memory, role, or candidate.

Population context contains exact active-member, card, communication,
contribution, action, resource, and ReplicationBound facts only. It excludes
inferred pressure, fitness, competence, need, diversity, team coverage, and
recommendations.

Every page preserves the source snapshot's exact order and cardinality. Equal
payloads at distinct authoritative append positions are not deduplicated.
Where the same signed identity is observed through several discovery scopes,
the raw page preserves each observation; any separate exact unique view also
exposes duplicate observation totals/ranges and the raw-page reference.

## 13. Safety and policy

Safety policies bind exact subjects/scopes and declare mechanical admission or
refusal effects. More restrictive current authority wins when policies overlap.
No persona-authored record may weaken an applicable higher authority.

Safety cannot be assigned through semantic classification of a task, domain,
profession, persona trait, role, file, or prompt. When physical/external action
requires exact attestation, consent, cosign, or operator authority, absence
fails closed. The kernel does not manufacture a substitute verifier or approval.

## 14. Objective acceptance

Only exact authenticated principal acceptance, an explicitly authorized
verifier receipt bound to current evidence, or another principal-declared
acceptance mechanism can complete an objective.

The kernel may validate identities, signatures, evidence hashes, byte/current-
revision bindings, exact verifier descriptor/results, conflicts, and authority.
It does not infer completion from model prose, HTTP status, tool success, work
notes, gap-like content, member count, artifact count, filename, score, or stable
bytes.

## 15. Replay, shutdown, and recovery

Replay reconstructs current state only from verified current schemas and exact
event lineage. Idempotency prevents duplicate effects. Process shutdown does
not change record authority; pending durable carriers resume only under their
original exact bindings and later resource/lifecycle authority.

Cached or derived projections are accelerators, never sources of identity,
lease, membership, routing, or completion authority.

## 16. Clean-break schema policy

Current live boundaries refuse retired schema versions and semantics. There is
no compatibility or migration path for mission/refinement records, structured
work readiness, fixed task classes/pathways, candidate/round FSMs, fixed persona
psychology/modes, ranked retrieval, fixed genesis seeds, one-newborn-per-need,
singular primary domains, inferred MIME, or inferred replication effects.

Historical bytes may remain opaque audit data but cannot participate in current
reduction or admission.

## 17. Design criteria

1. The kernel applies exact authority and declared effects only.
2. Every ordinary wake has the complete authorized unranked action catalog.
3. Task/resource events fan out unchanged to all active members.
4. Identity evolution, notes, gaps, navigation, population, and learning are
   persona-authored and optional.
5. MIME, domain references, and replication effects are explicit signed facts.
6. Objective acceptance is exact authority, never substrate inference.
7. Quiescence is nonterminal.
8. Mechanical bounds may refuse declared effects but never select behavior.
9. An ambiguous multi-model pool cannot acquire a host-chosen bootstrap order.
10. Pagination preserves exact append positions, cardinality, and duplicate
    accounting.
