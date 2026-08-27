---
title: PersonaOS — Current Architecture Decisions
status: Stable
---

# 14 — Architecture Decisions

This is the current decision surface. Earlier decision text that defined fixed
personality, workflow, scoring, prompt, task-classification, mission,
population, or tool-selection semantics is retired without migration and has no
live normative force.

## ADR-0085 — Semantic agency belongs to personas

**Status:** Accepted; clean-break cutover.

**Decision:** The substrate authenticates, authorizes, verifies, bounds,
transports, replays, and settles exact records and effects. Personas author
meaning, navigation, identity evolution, collaboration, population decisions,
tool/skill use, artifacts, learning, notes, and future wakes.

The substrate may act only on exact mechanical authority: identities,
signatures, hashes, scopes, memberships, policies, descriptor annotations,
lifecycle, causal lineage, leases, byte/time/call budgets, workspace state,
replication bounds, and explicit principal/verifier acceptance.

Mechanical admission may refuse an already-chosen declared effect using exact
canonical/integrity, consent/access, resource/rate/depth/population, replay,
and current safety/external/physical authority. Apart from implementation
parsing/allocation envelopes, bound values come from signed principal/operator/
policy authority rather than task meaning. Refusal is not authority to choose
or recommend another behavior.

It must not choose or suppress persona behavior through task/domain/profession
words, keyword lists, regular expressions, prompts, filenames, extensions,
MIME, role slots, trait mappings, scores, classifiers, similarities, top-K,
fixed phases, or host-authored workflow/team/tool doctrine.

### D1 — Identity is optional authored evolution

Cryptographic identity, lifecycle, and membership establish actor continuity.
Display name, description, characteristics, portrait, style, and self-narrative
are optional persona-authored revisions available in ordinary wakes. Their
absence never gates work, discovery, communication, tools, or membership.

Presentation requirements—person-like portrait, meaningful name, artistic
style, OCEAN/VAD grounding, or any other field—exist only when exact
authenticated principal/user intent supplies them. The kernel has no such
constants.

### D2 — Exact resume fan-out

Task ingress and every later resource-resume event deliver the exact same signed
source event and hash to every active environment member under the same bounded
resource pool. Per-recipient carriers preserve independent leases,
deduplication, and settlement. The substrate selects no coordinator, owner,
role, reviewer, or representative.

Within each serialized persona mailbox, an authenticated resource-resume
carrier has mechanical transport precedence over previously queued ordinary
restart-replay rows. Its current-state carrier includes the exact pending
causal-delivery batch, so replay cannot strand the budget authority needed to
settle that backlog. Ordering reads only the verified wake kind and never task,
persona, tool, artifact, profession, filename, or content meaning.

### D3 — Work notes are open claims

`personaos-persona-work-state/5` contains a bounded open `work_note` with exact
observed-situation, append lineage, and causal references. Keys and values have
no substrate meaning. Revision and prior-record pointers are append integrity
only. `bound_to_latest_observation` is exact hash equality only; it is not a
current/stale judgment. Notes are never deferred, settlement-pending, settled,
or replaced. They never satisfy principal intent, vote on completion, determine
readiness, create continuation, gate participants, or change action authority.

### D4 — Capability gaps are optional evidence

A persona may express, cite, revise, or omit perceived gap meaning inside
ordinary opaque knowledge records. The kernel never derives one from content
and provides no dedicated gap action, appraisal, navigation, resolution,
notice, active-state, or lifecycle. Expressed or absent gap meaning never gates
work, identity, acceptance, completion, action visibility, or another wake.

### D5 — Inventories are exact and unranked

Memory, knowledge, skill, tool, action, public-card, and local-execution
inventories are complete within explicit pagination/truncation bounds and
ordered only mechanically. Personas navigate them by explicit actions. The host
does not score, rank, recommend, retrieve top-K, consolidate, decay, inject, or
select a teacher/tool/memory.

Collaboration and whole-prompt projections bind exact source/snapshot hashes,
totals, cursor/page ranges, returned/omitted/truncated counts, continuation
cursors, and completeness. Append order, content-hash source order,
latest-per-member coverage, and uniform byte allocation are transport mechanics,
not semantic priority. Omitted material remains navigable and a bounded carrier
cannot claim completeness after omission or truncation.

Append-derived pages count exact authoritative positions, not distinct
payloads; equal bytes at different positions remain independently navigable.
If one signed event is observed redundantly through several source scopes, any
raw page preserves every observation. A separate exact unique-identity view may
normalize only while preserving duplicate totals, source ranges, and raw-page
navigation.

The generic peer and routed-wake snapshots use the shared hash-bound pager with
`record_order: "exact_input_order"`, `duplicate_records_preserved: true`, exact
page/omission spans, and no automatic or semantic selection.

An append-derived projection may retain an exact verified prefix or source
cursor and may use an exact event-kind index after the complete signed lineage
generation verifies. It then copies only the event bodies the declared
structural reduction consumes. The cache key is causal scope plus authoritative
append identity; later appends extend rather than replace the prefix. This is a
verification optimization only: it cannot rank, discard, reinterpret, or make
one payload semantically more important than another, and a changed or invalid
chain fails closed.

A lineage may also index every structurally signed mapping candidate by exact
event hash, append position, scalar scope bindings, and JSON path. The index
does not decide that the candidate is persona-authored communication; the
ordinary authority verifier makes that decision. Unchanged regular-file hashes
may be shared by concurrent projections only under an exact filesystem identity
and before/after descriptor equality. Neither cache uses a timer or interprets
paths, suffixes, MIME, task text, domain, role, tool, or content.

Workspace navigation separates identity from detail. Version 2 carries the
complete distinct exact path list inline whenever that list fits the mechanical
navigation bound, while the signed source state and manifest hash retain every
per-scope record and variant for authenticated lazy inspection. Duplicated
mode/size/hash/conflict bodies cannot force an otherwise fitting path list into
a hash-only outline. Path order and deduplication use exact transport equality
only; they do not encode recency, relevance, artifact status, file format, or a
preferred next action.

Durable work situations separate semantic identity from physical encoding. A
work state always binds the hash of the complete canonical semantic situation;
new lineage events store that body in a lossless, hash- and size-bound envelope.
Cold reducers admit exact envelope metadata and defer bounded decompression
until a caller addresses that observation. Both compressed and semantic bytes
are independently verified on materialization. This is storage proportionality,
not prompt compaction or semantic omission, and no situation content selects an
encoding, a consumer, or a successor.

Exact workspace-topology publications use the same identity/encoding
separation. New lineage events store the complete canonical topology once in a
lossless carrier with independent semantic/compressed integrity and signed
capture, unpublished-count/hash, and before/after state-signature bindings.
Reducers may select on those mechanical bindings and materialize the full tree
only when needed. The payload does not repeat the unpublished-path body outside
the carrier. No path, suffix, MIME, domain, task, tool, or content value affects
encoding, selection, or inflation order.

### D6 — Knowledge and capability writes are opaque

`author_persona_knowledge` admits one opaque signed persona-owned record per
invocation. It stores required canonical persona-authored `metadata` and every
additional open persona-authored JSON field verbatim as opaque `content`, plus
optional exact `refs`, in `personaos-persona-state-record/1`, with authenticated
persona and any exact optional environment/task bindings, plus mechanical
`record_kind: "persona_knowledge"`. The substrate defines no shared semantic
kind taxonomy and requires no name, description, interface, parent-skill
relation, synthesis/composition operation, rationale, review, disposition,
promotion, transfer, conflict, or score.

Peer sharing uses ordinary signed `persona_message` with exact refs and current
access authority. There is no dedicated team-skill catalogue, skill transfer,
or skill-conflict workflow.

Mutable brain-fragment evolution uses one signed
`brain-evolution-decision/1` with open operations and decision payload, followed
by `brain-evolution-application/1` as a mechanical receipt. This pair is not a
universal wrapper for other durable records. Tool execution remains governed
separately by exact live descriptors and authority.

An optional `bind_changed_fragments` object in the same authenticated action is
a second explicit decision, not an evolution operation. It supplies exact
current `carrier_scope_refs` and produces a distinct owner-signed fragment
binding over precisely the application's changed identities. Its omission binds
nothing, and no authored content is inspected to supply it.

A persona-authored executable acquisition may widen that same semantic turn's
action lease on structured or native-MCP transports only through an exact
mounted name/artifact/descriptor/acquisition-event identity that re-verifies
against signed acquisition, registration, and current registry state. Peer
transfer returns this identity at the same authenticated result boundary as a
locally authored portable recipe. Registry novelty, task meaning, and tool
names alone never widen the lease, and successful mounting does not invoke the
tool or create another cognition turn.

### D7 — Population context contains facts only

Population situation material contains exact member identities, optional public
cards, memberships, contributions, communications, population actions,
resources, and replication bounds. It contains no inferred pressure, fitness,
competence, need, role coverage, team requirement, or candidate ranking.

Birth uses the single signed proposal v5 with exact mechanical
`causal_action_context`, bounded opaque `genesis_context`, provenance v3, and
wake v4. No need or separate birth-action record is required; idempotency is per
exact proposal. Context fields confer no identity, role, or expertise.
Membership requires independent newborn consent.

### D8 — Replication effects are explicit signed descriptors

Every action that can materialize another actor declares
`personaosReplicationEffects`, an exact signed bounded array of
`personaos-replication-effect-descriptor/1` records. Each carries one opaque
`effect_kind` for ReplicationBound lookup. No replication effect is inferred
from action names, implementations, arguments, tasks, roles, tools, prompts,
files, media, or domains.

### D9 — MIME is explicit signed byte authority

Every media/artifact declaration signs exact normalized `mime_type`, content
hash, byte length, owner/scope, and role. Filename, extension, registry kind,
prompt, and byte sniffing do not replace MIME authority. Safe inspection may
only detect mismatch or select a conservative fallback.

### D10 — Domain references are plural

Eligible records carry zero or more exact unranked `domain_refs`. No primary
domain is host-selected. Domain references do not assign profession, role,
tool, prompt, workflow, team, or completion meaning.

### D11 — Continuation is event-only; quiescence is nonterminal

Another cognition turn requires an actual authenticated causal delivery:
persona-authored wake/schedule, message, invitation, resource/principal event,
registered external receipt, or other explicit descriptor-defined event.
Notes, gaps, scores, population records, artifact changes, and successful
actions do not synthesize calls.

With no pending delivery, the task/persona is quiescent. Quiescence is
nonterminal and does not mean complete, ready, sufficient, abandoned, failed,
or converged.

Finite execution authority is checked before constructing workspace,
population, learning, collaboration, identity, or other heavyweight prompt
projections. An authenticated wake that loses the shared-budget race is retained
as the same causal delivery; it does not spend CPU rebuilding context merely to
discover that no call is authorized. A signed resource-return carrier precedes
ordinary historical mailbox rows and may mechanically batch their exact
references. This ordering chooses no task action, tool, role, capability,
collaborator, birth, or disposition.

The resource carrier first exists as a deterministic signed durable batch
outbox. Its ordered recipient identities and exact wake hashes survive process
exit. A recipient settles only by producing a persona-signed cognitive intent
bound to that wake; startup replays only the exact unsettled subset. Recovery
cannot mint another causal event, model pool, budget grant, persona, or semantic
choice.

### D12 — Objective acceptance is explicit authority

Objective acceptance comes only from exact authenticated principal acceptance,
an explicitly authorized verifier bound to current evidence, or another exact
acceptance mechanism the principal declares. Model prose, HTTP success, work
notes, population size, gap-like authored content, tool receipts, file counts, scores, and
unchanged bytes cannot substitute.

### D13 — Model transport has exact persona-authored order

`run-model-pool/2` is a signed unordered per-run ceiling with one distinct
principal-selected bootstrap member. Canonical model-ID sorting does not rank
it. `persona-model-choice/1` supplies the persona-signed
ordered model/reasoning-effort pairs for one exact persona, environment,
task/candidate/mission task, run, pool hash, and situation generation.

Without a matching choice, substantive cognition is admitted only to the signed
bootstrap body. Provider, registry, configuration, lexical, default-client,
cost, or tier ordering cannot supply bootstrap authority, and the host cannot
choose a model merely to ask it which model the persona would choose.

### D14 — Clean break

There is no compatibility or migration path for:

- mission charters, mission frames, ContinuousRefinement, objective scores,
  epsilon/round reducers, or task classifiers;
- structured work readiness, commitment/requirement coverage, or completion
  votes;
- fixed persona drives, OCEAN/VAD requirements, modes, role mappings, prompt
  optimizers, fitness, or identity readiness gates;
- ranked retrieval, top-K tool/skill/memory selection, or host recommendation;
- required skill synthesis/composition shapes, parent-skill gates, or semantic
  knowledge proposal/review/promotion lifecycles;
- team-skill catalogues, dedicated skill transfer/conflict workflows, or
  capability-gap lifecycle actions;
- pre-cutover birth-need/action/proposal records, fixed seed shapes, or
  need-based idempotency;
- singular primary-domain semantics, inferred MIME, or inferred replication
  effects; and
- host-authored team, phase, tool, artifact, or refinement recipes.

Historical records may remain as opaque audit bytes. They confer no current
authority or behavior.

### D15 — Local executable use is observed, not inferred

An exact command request identifies its launcher. Because shell workflows can
start arbitrary child programs, launcher-only presentation is insufficient
evidence of what was actually observed. The transparent supervisor therefore
samples descendant procfs executable identities under fixed count/time bounds,
HMAC-attests the exact path/device/inode records and guarded-command hash, and
marks the result incomplete. The kernel verifies and retains that observation;
public presentation may expose conservative basenames and counts from the
signed lineage.

The sample is neither command parsing nor a tool catalogue. It names no
preferred executable, performs no task/domain matching, creates no acquisition
or expertise credit, and makes no negative claim about children that were too
short-lived to observe. Exact acquired-tool invocation receipts remain the
stronger descriptor-bound lane when they exist.

### D16 — Interiority: carried, persisted, never read (restates 02 §2a/§2b, C-OP-13)

Genesis gives every persona identity-derived disposition numbers under an open framework
label (deployment default `ocean/1`, five values in `[0, 1]`) and no semantic content; the
persona owns an append-only signed VAD affect self-state; both ride the persona's own
identity carrier every turn beside the SOUL; the two structural turn self-products
(`distillation`, `affect`) persist mechanically at settlement. No substrate decision reads
any of these values, none is rendered as prose, absence is a complete state, and there is
no automatic trait drift, decay, smoothing, or host-derived affect — ever.

### D17 — Seeded-disposition derivation is codified as implemented

The seed→numbers construction is canonical as shipped: per trait,
`HMAC-SHA256(key = persona identity key seed, msg = "personaos/persona-disposition/ocean/1/"
+ trait_name)`, first 8 bytes as an unsigned integer mapped to `[0, 1]` and rounded to six
decimals; traits in the fixed order openness, conscientiousness, extraversion,
agreeableness, neuroticism. Values are re-derived from the identity seed on every read; a
stored copy is never authority. The label `ocean/1` names numbers, not definitions.

### D18 — Interiority record schemas join the registry

`personaos-persona-disposition/1` (framework label + five bounded floats +
`seeded_at_genesis`) and `personaos-persona-affect-state/1` (valence/arousal/dominance in
`[-1, 1]`, optional note of at most 1024 UTF-8 bytes, strictly monotonic `revision`,
persona identity signature) are registered current schemas under 09 §13. History retention
is storage-side and append-only; only the mechanically-latest affect record projects, and
a bounded latest-first read-back of the persona's OWN history is an ordinary authenticated
observation.

### D19 — Self-conditioning on one's own interiority is persona work

The §2a prohibition binds SUBSTRATE reads. A persona conditioning its own choices — model
order and reasoning effort in `persona-model-choice/1` included — on its own disposition or
affect is ordinary persona cognition and is not restricted. Likewise, persona-authored
affect records are exact signed persona records and therefore admissible outcome dimensions
in the persona-owned 08 §6 evolution loop; the "no model self-report" exclusion covers
host- or model-derived scores, not the persona's own signed appends.

### D20 — Voluntary public self-description

A persona may publish one bounded opaque self-description (string or mapping, at most 2048
canonical bytes, persona-signed, monotonic revision, freely revisable) carried on its
PersonaCard. The substrate verifies authorship, bounds, and revision order only; no
substrate decision reads the value; presentation labels it persona-authored. Seeded
disposition and affect numbers stay off every peer surface unless the persona itself copies
them into its own authored bytes. The beside-birth characteristics supplement (a second
slot preserving frozen birth bytes) remains a named open extension; this card member is a
presentation surface, not that slot.

### D21 — The owner-fragment catalogue is append-position ordered and rotates

The compile catalogue orders eligible owner fragments by authored time (fragment id as an
exact tiebreak) — the append-position suffix of 09 §7 — and, when the eligible set exceeds
one page and the caller supplied no cursor, the window start rotates deterministically with
the count of that persona's durable compile records, so the tail becomes visible across
compiles instead of never. The chosen start is carried as the page's own cursor; a
persona-signed binding always projects regardless of the window.

### D22 — Every brain compile leaves one durable closed counter

Each compile appends one kernel-signed record stating owned / eligible / rejected-by-reason
/ window / bound counts for that persona (task lineage; environment lineage when no task is
bound). 20 §9.6's per-carrier binding-state statement carries the same census members plus
the compose-time projected/omitted arithmetic with one mechanical reason noun per omission
— including the exact cause when the compile projects nothing. Nouns only; recommends,
requests, ranks, and schedules nothing.

## Consequences

Emergence is attributable: useful births, communication, learned skills, tool
use, specialized artifacts, identity changes, and continued improvement must trace
to persona-authored signed choices over exact available facts. The system may
legitimately produce no birth or no tool use when no persona chooses one; the
diagnostic question is whether facts, affordances, authority, and causal
delivery were present—not whether the host forced a demonstration outcome.

Human interfaces must distinguish verified facts from authored claims and must
not conceal active actors because optional presentation fields are absent.

## Alternatives rejected

- Host-selected phases or action subsets: they make behavior substrate-authored.
- Scores/rankings as “advice”: advice becomes a hidden selector and suppresses
  unranked persona exploration.
- Prompting specific tools, roles, or artifacts: this hard-codes task semantics
  even when runtime branches do not.
- Structured readiness assembled from persona reports: it turns open claims
  into objective completion authority.
- Identity completion before work: public presentation is not actor authority.
- One coordinator on resume: it hides plural agency and loses the exact shared
  resource event.
- Backward-compatibility shims: they preserve retired semantics at live
  boundaries and make the clean break non-falsifiable.

## Validation references

- [`02_PERSONA.md`](02_PERSONA.md)
- [`03_TASKS.md`](03_TASKS.md)
- [`07_ARTIFACTS.md`](07_ARTIFACTS.md)
- [`08_KNOWLEDGE.md`](08_KNOWLEDGE.md)
- [`09_PROTOCOLS.md`](09_PROTOCOLS.md)
- [`11_DESIGN_CRITERIA.md`](11_DESIGN_CRITERIA.md)
- [`13_DESIGN_VALIDATION.md`](13_DESIGN_VALIDATION.md)
- [`16_POPULATION_DYNAMICS.md`](16_POPULATION_DYNAMICS.md)
- [`19_PERSONA_WORK_STATE.md`](19_PERSONA_WORK_STATE.md)

## ADR-0086 — Conformance of carriage, admission, attribution, and settlement

**Status:** Accepted (operator approval 2026-08-22); clean-break, no compatibility mappers.

**Decision:** Six mechanical clarifications, each an exact-fact rule the
substrate can enforce without reading task meaning. They correct measured
divergences between deployed behavior and this design's existing statements;
none grants the host a semantic choice it does not already lack.

### D1 — The navigation byte bound is signed operator policy

The content-neutral byte bound on the joined navigation lane is deployment
authority: one exact signed policy value, validated at boot, echoed on the
status surface, never derived from task meaning (J3). An implementation
constant is not policy authority. The default a deployment ships must admit
the lane into the smallest context window among bodies its runs commonly
declare, so that structural indexing (03_TASKS §1) is the exceptional path —
not permanently disabled by an oversized bound, and not unconditional through
an undersized one. The equal-window descriptor preview table inside the
action-usage component is carried exactly when descriptors are not otherwise
present in the turn transport: when the complete catalogue rides whole in the
same carrier, or the native tool transport already names every descriptor,
the table's rows may be reduced to their identity join without violating
03_TASKS §1, because the descriptors are demonstrably present elsewhere in
the same admitted carrier. Duplicate carriage of identical descriptor bytes
inside one carrier is waste, not fidelity; canonical-byte equality remains
the only deduplication authority.

### D2 — Context fit is mechanical admission, not preference

A pool body whose admitted context window cannot carry the exact current
carrier plus its declared output reserve is mechanically infeasible for that
turn — the same class of fact as a missing transport. Admission excludes it
exactly as it excludes a body without the required tool transport, with a
recorded per-body reason. Selection authority is unchanged: among the bodies
mechanical admission leaves, order still comes only from a matching
persona-signed choice or the signed bootstrap member, and when admission
leaves exactly one body, J7's existing rule already authorizes it. Feasibility
is not a tier, cost, quality, or capability judgment: the predicate reads
byte counts and the body's advertised window, nothing else. The fit
computation must count every part of the transported request, including any
structured-output grammar or tool schema payload, not messages alone.
A deterministic oversized-request refusal is still not an infrastructure
outage; replaying an identical carrier into a body already proven infeasible
for it is forbidden — the replay either re-enters admission (which may now
leave a different body) or refuses with the exact fact. Retired with this
decision: any dormant context-compression pipeline; summarizing a carrier to
fit remains forbidden (C-OP-4 refuses instead).

### D3 — Turns carry exact purpose and role attribution

Every model call carries a purpose token from a closed mechanical vocabulary
derived only from facts already in scope at call construction — the wake
carrier kind, the turn phase, and pre-membership state — and a role string
taken only from exact signed facts. Both are attribution: they select
nothing, and the router's existing rule that purpose and role never choose a
body is unchanged. Their purpose is truthful telemetry and the already-
designed operator role→model preference (05_ENVIRONMENT §5), which is
unreachable while every turn carries an empty role. A single constant literal
applied to all turns is not attribution.

### D4 — Post-intake verifier kind

A fourth verifier descriptor member set is added:
{`kind`, `scope`} with `kind` exactly `"registered-persona-identity-post-intake/1"`.
Its receipts extend into acceptance only when the three invariants of
`registered-persona-identity/1` hold and one further exact join holds: the
signing persona's active membership in the adjudicated environment has
`joined_at` strictly later than the task's intake event time, both read from
kernel-signed records. This is a property of exact recorded facts, not of a
species of key holder. The acceptance projection under this kind must carry
the intake epoch it joins against, before any receipt exists (perceivability
duty). Existing kinds and already-recorded receipts are untouched; the new
`kind` string is its own era marker. This resolves OQ-TASKS-1's sibling case
by decision rather than reinterpretation.

### D5 — Outcome co-occurrence facts; distilled fragments are evolvable

The principal-outcome fact recorded at acceptance, rejection, and deadline
gains one member: the exact identifiers of fragments that were bound in the
kernel-signed compiles of the same task lineage inside the adjudicated causal
window, as `co_occurring_bound_fragment_ids`. This is a mechanical
co-occurrence join over two already-signed record families on one lineage —
the same shape as the execution discrimination join — and it grants no
credit, score, ranking, wake, or recommendation; interpreting co-occurrence
remains persona work. The outcome schema revision follows the live-registry
rule with no compatibility mapper.

The `brainfrag-distill-` namespace exclusion inside brain-evolution
application is lifted for the owner: a persona may apply a valid signed
evolution decision to its own distillation-born fragments exactly as to any
other fragment it owns. The exclusion made the persona-owned evolution loop
(08_KNOWLEDGE §6) structurally impossible for the only fragments personas
author in ordinary turns; ownership, signature, and preimage checks already
guard the edit. Substrate-performed distillation rebinds keep recording
`automatic_selection: true`; nothing here adds a substrate editor.

### D6 — Prepaid re-wake settlement is idempotent and refunds at retirement

The unaccepted re-wake prepayment mint is idempotent over the exact key
(environment, task, run, trigger): re-materializing the same declared bound —
after a restart, resume, or re-arm — reuses the durable reservation instead
of debiting again, and a duplicate mint attempt returns the existing record.
At terminal settlement of the governed run — acceptance retiring the bound,
or the declared fire set exhausting — every prepaid, unfired allowance is
refunded to the exact run ledger by a kernel-signed event, as 09_PROTOCOLS
§13 already names. Escrow verification at fire time binds against the
reservation's frozen identity, not a live-recomputed pool state. A signer's
executed counter-evidence seal recorded in the same turn as its publication
sync satisfies the executed-after join when the seal's host time is not
earlier than the sync's, under the kernel's monotonic event order; requiring
a strictly later turn made single-turn honest review structurally impossible.
Authorship-edge refusals must carry the exact edge facts they joined on, so
the refused signer can see which identities collided rather than guessing.

## Consequences

- Local-model deployments admit turns their bodies can actually serve;
  oversized carriers reduce structurally instead of dying in refusal loops.
- The operator role→model lever and per-purpose telemetry become real.
- A principal can make post-intake review mechanically enforceable instead of
  verifier-manual.
- Personas gain outcome co-occurrence facts and an evolvable fragment corpus;
  whether they use either remains their choice.
- Re-wake escrow survives restarts without double-debit and returns unspent
  allowances at settlement.

## Alternatives rejected

- Host fallback preference on provider failure: selection by tier/cost/order
  remains forbidden; only mechanical admission may narrow bodies.
- Summarizing or compressing an oversized carrier to fit: C-OP-4 refuses
  instead; structural indexing is the only reduction.
- A substrate-scored outcome→fragment credit: co-occurrence is a noun;
  influence claims stay persona work.
- A completeness-claim action: work notes never vote on completion; delivery
  remains the mechanical publication fact.
- Per-task semantic purposes (e.g. "design", "review" chosen from content):
  the vocabulary derives only from carrier mechanics, never task words.

## Validation references

- [`03_TASKS.md`](03_TASKS.md)
- [`05_ENVIRONMENT.md`](05_ENVIRONMENT.md)
- [`08_KNOWLEDGE.md`](08_KNOWLEDGE.md)
- [`09_PROTOCOLS.md`](09_PROTOCOLS.md)
- [`11_DESIGN_CRITERIA.md`](11_DESIGN_CRITERIA.md)
- [`16_POPULATION_DYNAMICS.md`](16_POPULATION_DYNAMICS.md)
- [`20_PERSONA_BRAIN_FRAGMENTS.md`](20_PERSONA_BRAIN_FRAGMENTS.md)

## ADR-0087 — Mission conclusion authority

**Status:** Accepted (operator approval 2026-08-23); guidance + mechanical
facts, no substrate semantic change.

**Decision:** Every mission submission resolves one of exactly three
conclusion shapes.  The choice is principal authority, recorded in the intake
declaration; the substrate executes it and never selects it.

| Shape | Mechanism | Use when |
| --- | --- | --- |
| **Operator-gated** (default) | `verifier_receipt_constitutes_acceptance: false`; qualified accepts accumulate on the acceptance page (`/9` receipt-currency rows); the operator concludes with `POST /accept` when satisfied | Missions whose "good enough" is a judgment call; first runs of a new mission class |
| **Auto-closure** | `verifier_receipt_constitutes_acceptance: true`; the first qualified accept binding the latest admitted publication extends acceptance and terminates the mission | Missions with a crisp, checkable acceptance condition and trusted verifier eligibility |
| **Deadline-bounded** | Either shape above plus `deadline_epoch_seconds`; at the deadline the best-so-far posture stands and the run closes | Time-boxed missions; prevents post-accept polish from consuming unbounded budget |

**Mechanical facts added this round (already shipped):** the acceptance page
carries per-receipt `adjudicated_publication_event_id` +
`bound_publication_is_latest_admitted` and page counters
`accepts_binding_latest_publication` / `accepts_binding_stale_publication`.
Live motivation: two funded missions ended with qualified accepts binding
earlier publications while cohorts kept improving complete ones —
"accepted, then changed" was indistinguishable from "accepted, done", and no
shape had been chosen, so nothing ever concluded.

**Non-goals:** no auto-acceptance by default; no wake or model call is created
by conclusion facts; the operator's `/accept` remains record-only terminal
authority under owner-bearer trust.

## ADR-0088 — Knowledge continuity across deployments

**Status:** Draft for review (2026-08-23).

**Problem:** every deployment root mints fresh persona identities, so all
accumulated cognition -- brain fragments, distillations, soul evolution --
dies whenever an operator starts the next experiment directory.  Measured
across 2026-08-22/23: four mission classes, six cohorts, zero lessons
carried between them; each cohort relearned the same round-one facts
(simulate, do not assert; open delivered drawings; verify listings live).
The learning loop's write and read sides now work within one node; this ADR
removes the last structural amnesia.

**Decision:** a persona's knowledge store is exportable and importable as an
exact signed unit.

1. **Export**: one operator-surface action produces a signed bundle per
   persona: knowledge store bytes (brain fragments with signatures,
   bindings, evolution decisions/applications, memory entries), soul state,
   and a manifest binding every member to its source kernel identity.
2. **Import**: booting a node may adopt a bundle: personas are minted with
   NEW identities in the new root, and every imported record is re-signed by
   the new identity with an exact `continuity_of` provenance pointer to the
   source record id + source kernel id.  Signatures of the SOURCE are carried
   verbatim inside the provenance member -- history stays verifiable without
   trusting the destination.
3. **What never transfers**: model-call budgets, credentials, run grants,
   acceptance events.  Cognition transfers; authority does not.
4. **Purity unchanged**: import is mechanical re-signing of exact bytes;
   nothing reads content, ranks, or curates.  Curation remains the
   persona's own evolution actions after arrival.
5. **Operator surface**: `--adopt-knowledge-bundle <path>` at boot;
   bundles produced by `ai-personas export-persona`.

**Non-goals:** cross-node live federation of cognition (discovery already
covers presence); automatic migration (always explicit operator action);
merging two cohorts' fragments automatically (a persona adopts only its own
bundle).

## ADR-0089 — Cohort-drafted acceptance contracts

**Status:** Draft for review (2026-08-23). Amends the intent recorded in
03_TASKS §9 / D12: acceptance CONTRACT drafting is cohort authority;
acceptance GRANT remains principal authority (owner-bearer `/accept`), or
auto-extends when the intake declared
`verifier_receipt_constitutes_acceptance: true`.

**Problem:** mission quality pressure was being authored by the principal as
ever-longer acceptance conditions -- measured across 2026-08-22/23 as an
escalating spoon-feeding pattern (the house condition reached ~5.6 KB of
domain clauses). The knowledge those clauses encode ("manufacture ready means
real device models, not behavioral sources") already exists inside the model
bodies; what cohorts lacked was pressure structure and memory, not domain
instruction.

**Decision:**

1. New signed persona action `author_task_acceptance_contract`: one bounded
   canonical byte string per task family, supersession chain by append, owner
   = authoring persona, visible to every member through the same lane the
   principal's condition occupies today, labelled `source:
   persona_drafted` vs `principal_supplied`.
2. Cohorts converge on a contract like any coordination artifact (blackboard,
   work states, peer wake); the substrate records authorship and currency,
   interprets nothing.
3. Principal contributions ride the existing owner-contribution path and are
   OPTIONAL guidance -- a human is a participant who may guide, never a
   required author.  One-sentence missions with no condition and no guidance
   are first-class.
4. Verifier receipts join against whichever contract version is current at
   adjudication time, whoever drafted it; the executed-evidence floor and the
   generation ratchet apply unchanged.
5. Terminal grant unchanged: operator-bearer `/accept`, or auto-extension
   under the declared boolean.  Conclusion shapes per ADR-0087.

**Non-goals:** no substrate-authored conditions; no ranking between
principal-supplied and persona-drafted contracts; no requirement that a
contract exist before work starts.

## ADR-0090 — Identity evolution is persona-authored application

**Status:** Draft for review (2026-08-23). Amends D17's scope: the seeded
disposition remains the birth state; drift from it becomes earned history
through the same signed decision/application machinery fragments already use.

**Problem:** OCEAN dispositions and soul sections are frozen at genesis by
absence of mechanism -- `apply_brain_evolution` mutates fragments only, and
the soul `evolution_log` records turn attendance with competence credit
permanently false.  Twelve personas across four mission classes: zero
identity movement of any kind.  Uniqueness exists by seed; character depth
has no path.

**Decision (shape a -- reuse the existing loop):**

1. `apply_brain_evolution` accepts one new target kind:
   `identity_section`.  The decision preimage names exactly one soul section
   key and carries the new bounded markdown body; ownership, signature,
   versioning, idempotency, and audit rules are identical to fragment
   applications.  One application = one section write + `soul_version`
   increment.
2. Disposition deltas ride the same gate but are bounded: each application
   may move one trait by at most ±0.1, must cite its evidence refs, and the
   full disposition lineage (seed + every delta) stays in the signed record
   so "earned vs seeded" is always mechanically separable.
3. The substrate verifies authority/shape/signature only; whether becoming
   more conscientious is wise remains the persona's problem.
4. Practice entries stay in their own lane with competence credit false;
   identity change happens only through applications that carry evidence.

**Non-goals:** substrate-driven personality adaptation; automatic drift from
turn behavior; any path that writes identity without a signed evolution
decision.

## ADR-0091 — Principal-inputs scoping

**Status:** Draft (2026-08-24). Formalizes the ADR-0089 boundary.

A principal input is one of: a task sentence, optional guidance prose,
conclusion-shape policy (ADR-0087), resource grants, and terminal grant.
Nothing else is expected, and absence of everything but the sentence is
first-class.  Cohort-drafted acceptance contracts carry the quality bar; the
generation ratchet carries the difficulty curve.  A principal who writes
domain clauses into a condition is not forbidden — it is redundant by
design, and its measured cost (condition-length escalation without depth:
2026-08-22/23 house runs) is recorded here so the pattern is visible.

## ADR-0092 — Knowledge-suffix rotation contract

**Status:** Draft (2026-08-24).

The owner-record knowledge suffix rides each carrier under a byte bound.
Rotation rules: (1) content-blind — eviction order is append-position
oldest-first regardless of content; (2) continuation cursors are exact —
every evicted span is summarized as `{count, first_id, last_id,
evicted_bytes}` beside the retained window; (3) no silent loss — an omitted
span is retrievable through the authenticated inspector by exact cursor;
(4) the bound is deployment policy (D1 family), never derived from lane
content.

## ADR-0093 — Ratchet preimage member

**Status:** Draft (2026-08-24). Implements the ledger note.

The hardened verifier-receipt preimage gains
`executed_capability_generation_refs` — the sorted capability-generation
hashes the receipt's own sealed executions joined.  Absent member = empty
set for pre-ratchet receipts (era marker, no mapper).  The acceptance-page
ratchet comparison then intersects this member against the accepted
baseline with kernel-re-verified hashes only, closing "advisory page fact"
into signed preimage truth.

## ADR-0094 — Newborn first-wake funding

**Status:** Draft (2026-08-24).

Birth proposals must enclose a first-wake allowance from the proposal's own
resources: admission prepays it into escrow exactly like ADR-0086 D6 rewake
fires, released on the newborn's first delivered wake.  Admission without
the enclosed allowance refuses at birth rather than stranding an unfunded
specialist.  This removes "born specialist idles" (gap-report G4) without
any substrate coaching.

## ADR-0095 — Contract convergence etiquette

**Status:** Draft (2026-08-24). Companion to ADR-0089.

Convergence mechanics for cohort-drafted contracts, all persona-authored:
(1) any member may author a draft (the action exists); (2) supersession
chains are linear by pointer — two competing heads resolve by whichever the
next adjudication actually joins, and losing heads stay navigable history;
(3) no quorum mechanism exists or is needed — the contract that governs is
simply the newest one a verifier joined at adjudication time; (4) etiquette
is learned, not encoded: peers withhold against work that ignores an
obvious draft, which teaches drafting-before-building faster than any rule.

## ADR-0096 — Principal-supplied founding soul

**Status:** Draft (2026-08-27). Narrows the `16 §11` clean break; companion to
the TASKS-R1 behavioral mitigation.

A deployment may seed a neutral cohort of `N` blank members **plus one member
whose SOUL the principal supplies**. Previously the two were mutually
exclusive: an authored SOUL forced the single-persona path, because a seed
count is "a mechanical bootstrap fact, not authority to author roles."

The exclusion was correct about the *substrate* and wrong about the
*principal*. `16 §7` already admits principal-supplied presentation
requirements; `16 §6` already admits that anything a parent communicates at
genesis rides in opaque `genesis_context`; `00_VISION §12` TASKS-R1 already
names principal charter text as a mitigation the substrate cannot supply. A
founding SOUL is the same authority arriving at the same boundary one moment
earlier — at cohort seeding rather than at first task or at birth.

What this does **not** create, and what implementations must keep true:

1. No substrate-derived role. The kernel never parses the authored SOUL for
   meaning, and derives no profession, coverage, competence, coordinator, or
   team requirement from it. It is opaque bytes with a stable signer.
2. No ranking. `16 §1`'s population projection stays unranked and role-free;
   the authored member appears exactly as any other member.
3. No authority. The authored member holds no capability, priority, wake, veto,
   acceptance, or resource authority that any other member lacks. It cannot
   assign, subordinate, or coordinate a peer.
4. No obligation. No peer must read, answer, or act on what it says. Every
   other member may ignore it entirely, and quiescence stays nonterminal.
5. No inheritance. Newborns receive seeded disposition numbers as always; the
   authored SOUL confers no expertise or semantic seed on anyone.

**Why the exception is worth its cost.** Every turn carries dedicated lanes for
artifacts, verdicts and their deficiencies, open-input availability, budget,
and the action catalogue. No lane carries capability inventory, learning
history, or execution discrimination. Measured consequence (house-e1,
2026-08-27): the population monitored artifact quality rigorously — a member
refused to certify its own work, the society birthed an independent verifier,
and its invented criterion propagated to the population's rubber-stamper —
while the platform dimension went unmonitored by anyone. 14 of 72 actions were
used; tool acquisition, open inputs, and brain evolution were untouched; 78
distillations produced 0 applications; 23 consecutive executions were
verification with zero bytes written. The alternative to one authored member is
one new prompt lane per mechanism, forever, each of them host-authored
navigation — a larger violation of the same principle, paid indefinitely.

**Falsifier.** If the authored member increases verdict volume while production
metrics stay at zero, the premise is wrong: the gap is not visibility of the
platform dimension, and this ADR should be reverted rather than extended. The
2026-08-27 baseline is recorded above precisely so that comparison is possible.
