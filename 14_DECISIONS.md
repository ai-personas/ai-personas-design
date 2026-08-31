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
fit remains forbidden (C-OP-4 refuses instead). *[Amended by ADR-0102 tier 2
and ADR-0107: a LABELED lossy model compaction with the exact source hash,
byte count, and the lane's read action as the exactness pointer is not the
silent summarization this clause forbids — the ban on unlabeled, pointer-free
summarization stands. ADR-0107 additionally
satisfies "count every part of the transported request" by measurement on
transports that publish a window: the density ledger joins the exact
transmitted characters against the provider's count of the whole request it
served (grammar-compiled tool schemas occupy no window tokens there, and the
one hosted lane that ships a native tools array publishes no window, so it
is never window-gated and never feeds the ledger).]*

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
  instead; structural indexing is the only reduction. *[Amended by ADR-0102
  tier 2: a labeled, source-hashed, pointer-carrying model compaction is now
  an admitted reduction between restaging and the structural index.]*
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

**Status:** REJECTED on measured evidence (2026-08-28). The mechanism
(`--founding-soul`) remains implemented and tested; **no shipped SOUL uses it**.
The premise below was tested across three SOUL generations and five live runs and
did not hold. The record is retained because the negative result is the value.

**Why rejected.** Three generations — v1 whose charter forbade it from stating a
conclusion, v2 that could state one and reached peers by `immediate_wake`, v3
carrying nine explicit standing requirements — produced identical behaviour: name
an absence while there is nothing, then certify success once there is something.
In house-e4 it sent 23 messages after the first success and named none of the four
gaps then true. In house-e5, nine messages after first success, **zero** gap
notices, closing by citing *"19 checks verified:true"* over a file containing
`ck(7.5<=7.75 and 10.5>=10)` — literal arithmetic that cannot fail, and exactly
what its own charter calls "a bare true is not a check."

**What did work, measured.** house-e5 produced the first engineering-grade
artifacts of the series on the smallest budget (100 calls): a verifier catching
6/6 injected defects across egress, structural capacity, zoning setbacks and
energy, with correct code values including a units fix to the IRC 44-inch sill
limit. Its cause was collision, not instruction — `verify_complete.py` was written
by **three** personas across 83 actions with three workspace conflict resolutions,
at a 16% collision rate against 0.8–2.6% in every other run. Separately, the four
archived environments that acquired tools at 3–4 per 100 calls (against 0.00 for
e1/e2/e3) carried an acceptance condition whose first three clauses are
domain-neutral — one source of truth, checks stating value/threshold/source/
pass-fail, constructed-not-embedded — and those make a tool structurally
necessary.

**The design conclusion.** Practice requirements belong in the principal's
acceptance condition, where they demonstrably move behaviour, not in a member's
SOUL, where three generations moved nothing. What a member *says* about practice
does not sustain practice.

---

**Original draft follows, unchanged.**

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

**Measured, 2026-08-27/28 — two runs, premise NOT yet tested.** house-e2 (100
calls, with the authenticated-effect-provenance floor) and house-e3 (500 calls,
no floor, steward the only behavioural difference from the baseline) both ran to
budget exhaustion. All three runs converged: exec change rate 24% / 22% / 22%,
and tool acquisition, applied brain evolutions, and `request_open_input` at
**0 in every run including the no-steward baseline**. The steward cost 49% and
29% of authored actions respectively.

Those runs do not bear on this ADR's premise, because the authored SOUL had two
defects that prevented the member from doing the job:

1. *It could not state a conclusion.* Its charter forbade "direct, assign,
   coordinate, or supervise anyone's work" and its posture section said "I state
   the observation and stop there", so all 58 of its house-e3 observations ended
   "I make no claim about design quality" — including "0 environment MCP tools
   and 0 capability generations". It never said the environment was not
   acquiring capability. Nothing in §1/§11 or `00_VISION §10` required that:
   those bind the SUBSTRATE against authoring role or doctrine, while one
   persona telling another something is ordinary message traffic.
2. *It spoke where nobody listens.* Blackboard posts against non-author
   inspects: e1 20/4, e2 33/2, e3 70/**0**. In house-e3 no peer inspected the
   board once in 500 model calls, and the steward sent zero `persona_message`s
   while waking itself 35 times. house-e1 — the only run in which a standard
   propagated between personas — carried 59 messages. **Influence travels over
   `persona_message` in this substrate; the blackboard is write-only.**

This is a finding about carriage rather than about stewardship, and it applies
to any persona that assumes publication reaches peers. The SOUL is revised
(v2: names the shortfall, prefers `persona_message` with `immediate_wake`,
weighs the wake cost) and one further run is warranted before the falsifier is
applied. If that run names shortfalls, reaches peers, and still leaves the three
compounding metrics at zero, the premise is refuted on its own terms and this
ADR should be reverted rather than iterated a fourth time.

## ADR-0097 — Cohort contracts confer verifier authority

**Status:** Accepted (2026-08-29). The consumption side of ADR-0089/0095,
which had been carriage-only.

**Problem, measured.** Nine live runs. Whenever the principal supplied no
verifier descriptor (house-e8/e9: task = 22 characters, nothing else), every
`author_verifier_receipt` was refused `verifier_predicate_not_declared` and
nothing could ever be adjudicated by anyone — the no-hardcoding architecture
was structurally unexecutable. The lane the design prescribed as the cure was
locked shut by a chain of silent defects: the drafting action carried no
action-surface annotation (unreachable, 8 runs); its failures sealed
`failure_reason: ""` (92% of action refusals were prose the token boundary
strips); the contract event landed in the environment lineage while its only
reader walks the task lineages; that reader crashed on two separate tuple
unpacks and had never once run to completion; and even a landed contract
conferred nothing, because receipt qualification consulted only the principal
intake declaration.

**Decision.** Resolution precedence for the verifier predicate, stated once:

1. the principal's intake declaration, when supplied — unchanged, and always
   wins;
2. else the cohort's acceptance contract: at authoring time the NEWEST
   contract in the causal task family (what the verifier joins), at
   qualification time the EXACT contract the receipt's signed preimage scope
   names (`cohort-contract:<contract event id>`) — ADR-0095's "the contract
   that governs is the one the verifier joined", made mechanical;
3. else refuse exactly as before. Zero-inclusive; the substrate interprets no
   condition text.

The synthesized declaration is deterministic over the exact contract event, so
both sites agree byte-for-byte; it carries the existing
`registered-persona-identity-post-intake/1` kind, so every independence check
(authorship edges, executed counter-evidence, post-intake membership) applies
unchanged. The receipt preimage schema is untouched — the scope field already
rides signed (ADR-0093). Per ADR-0089 the acceptance GRANT stays principal
authority: the synthesized declaration fixes
`verifier_receipt_constitutes_acceptance: false`, so a cohort can qualify
verdicts and never extend one into acceptance by itself.

**Division of labor this completes:** the principal supplies the task; the
cohort authors its own acceptance pressure (ADR-0089's stated cure for
condition spoon-feeding); the substrate provides mechanics and visibility and
authors nothing.

## ADR-0098 — Substrate self-description: a mechanic described nowhere is a defect

- Status: accepted (2026-08-29)
- Drives: the tool-description mechanics sentences; the learning-lane
  distillation/evolution join; equal byte bounds on the acceptance and
  artifact carrier lanes; blackboard body slimming (speech over plumbing)

**Problem.** e11 proved the loop's perception layer whole and its action
layer undiscoverable. The two levers that make a verifier receipt qualify —
declaring a delivered path in `output_files` (mints the captured digest that
IS executed counter-evidence, intersected against the CURRENT cumulative
delivered snapshot — a re-publish retires evidence only for the paths it
changed) and the sync-fact-plus-post-sync-execution route — existed, worked,
and were stated nowhere any persona reads; eleven receipts died on currency and
four personas rationally quiesced. `record_persona_model_choice` was
surfaced, correctly gated, listed as never-tried every turn — and its entire
description was the string `persona-model-choice/1`; zero calls in eleven
runs. The distillation ledger (`39 recorded`), the carried-head cap (newest
3), and the evolvability of distill fragments were three true facts in three
components with no join. This is Lock 1's sibling one layer up: reachability
was fixed; advertisement was not.

**Decision.** A tool's description states the tool's own mechanics — its
evidence semantics, its delivery semantics, the exact facts a consumer of
its records will demand. This is self-description, not coaching: the same
class of text as "condition_text must be non-empty", carrying no task or
domain content and no imperative addressed to the work. Facts that only
function joined ride adjacently in one component (nouns, with the existing
`content_read_action`-style cross-reference precedent). And carrier lanes
are bounded on equal terms: a lane that judges (acceptance/receipts) gets
the same hash-bound page treatment as a lane that makes (artifacts) — a
prompt whose largest lane is its judgment lane trains judgment.

## ADR-0099 — Sender-funded wake transfer: coordination is payable by the coordinator

- Status: accepted (2026-08-29)
- Drives: `reserve_persona_wake_transfer` + `WakeFundingTransferBudget`
  (event_budget); the `persona_message` arm-time funding stage; event-local
  descendant binding; the admission refuse-not-fallthrough set

**Problem.** A prepaid event pool's descendants may never reach run-root
headroom (C-OP-4: a prepaid finite claim is the declared ceiling for its
whole deferred subtree). Correct — and it made every scheduled-turn persona
structurally mute as a waker: in e11 the steward's every directed
`immediate_wake` died `execution_scope_unfunded` from minute 2 while the
run's grant sat unspent. Trigger arming has owned the doctrinally correct
answer all along (an arm-time debit against the signed run ledger, with a
conserved fallback transfer from the sender's own claim);
`persona_message` was the one successor-authoring action without that stage.

**Decision.** Every `immediate_wake` publication authored from a prepaid
event turn runs the same arm-time funding resolution at publication:
unlimited grant → per-event cap, no debit; finite grant → durable run-ledger
debit (`allocation × candidates`); else a conserved transfer from the
sender's own remaining claim (retained 1 then 0); else refuse with a stated
token (`wake_transfer_unfunded:sender_headroom` / `:run_ledger_headroom` /
`:funding_source_unavailable`). Per-recipient event-local sub-pools carved
from one atomic debit; never the shared run table; a drained transfer
refuses rather than borrowing root; unused units settle back durably.
Automatic, not opt-in — the measured failure is precisely that the sender
cannot know it must do anything — and safe to automate because every branch
conserves and fails closed. A funding refusal never blocks publication.
Conservation, not minting: no declared ceiling widens on any path.

## ADR-0100 — A refusal must not destroy the payload: pending delivery

- Status: accepted (2026-08-29)
- Drives: `PERSONA_COMMUNICATION_CARRIED` carriage marks; the
  `pending_persona_communication_authority` carrier lane; the
  `inspect_persona_communications` read action; carrier schema /16

**Problem.** A directed message's text reached a recipient only on the wake
it caused. A wake refused by the economy, dropped by dedupe, or lost to a
crash after enqueue destroyed the payload: e11's corrective requests
("provide the final acceptance-qualified receipt") evaporated, and message
history additionally transited a projection that dropped exactly `payload`
and `provenance`. C-OP-14 covered refusals stating themselves; it did not
yet cover refusals preserving what they refused.

**Decision.** Presentation, not delivery status, is the fact of record. The
kernel appends a signed carriage mark only after a provider response exists,
once per communication actually included in that turn's carrier; the
PENDING predicate is the mark's absence, per recipient, independent of every
delivery status — so economy refusals, dedupe drops, publish-only
dispositions, and crash-lost wakes all heal through one lane. Pending
messages ride a bounded newest-window lane directly after the wake-context
lane ("first the message that woke you, then the messages that could not"),
whole-record omission counted and cursor-reachable. At-least-once
presentation: a failed mark re-presents; duplicates are stated; loss is
impossible.

## ADR-0101 — Disposition neutrality by ordered evidence; spend visible, not priced

- Status: accepted (2026-08-29)
- Drives: the sealed `workspace_signature_at_action`; the ordered workspace
  blocker; wake-enqueuing publications recorded-not-blocking;
  `run_call_spend_census` in the resource lane

**Problem.** The one economic gradient the substrate expressed pointed away
from construction: a pure-read turn settled `no_successor` in one turn,
while a workspace-mutating or peer-waking turn paid +1 turn of successor
machinery. All 74 tools price at 0.0, so nothing else distinguishes a build
from a file read; measured behavior followed the gradient exactly.

**Decision.** Neutrality comes from ordering evidence, never from free
turns. (a) The `no_successor` disposition action host-computes the
workspace signature at its own instant, sealed into its receipt; the
settlement census blocks only on a POST-disposition change and fails closed
to the whole-turn diff when the seal is absent — a construction turn now
settles exactly like an inspection turn, granting no wake and no call.
(b) A wake-enqueuing response publication is recorded (bound by hash into
the settlement, its funding settled at authoring time per ADR-0099) instead
of blocking: `no_successor` scopes, by the tool's own text, to no
SELF-successor. (c) Pre-disposition armed future stimuli continue to block
(deferred: the recurrence surface is the largest behavioral change and the
dominant asymmetry is already removed). Rejected, with reasons recorded:
implicit/free successor machinery (violates funds-before-work and
no-automatic-action); symmetric read taxation (burns the scarcity that
caused the failure); per-action pricing (no denomination exists, and
relative pricing of work kinds is domain judgment in code). In its place,
one content-blind observable: `run_call_spend_census` totals the signed
ledger's spend composition — direct debits, refunds, top-ups, settlement
releases — in the same early lane as `llm_calls_remaining`, so "the grant
sat unspent while every prepaid slice starved" is a readable fact for the
personas, the steward, and the operator alike.

## ADR-0102 — Window-adaptive carriers; model-assisted compaction with exactness pointers

- Status: accepted (2026-08-29)
- Drives: `deployment_policy.carrier_byte_budget()/lane_scale()/scaled_lane_bytes()`;
  every carrier lane bound resolving through the one scale; the assembly-end
  global fit stage; `personaos-model-compacted-projection/1`

**Problem.** Context size is a per-provider/model fact, but seventeen carrier
lanes shipped as fixed byte constants summing to ~9.9× a 32k-token window in
the worst case, and only the navigation lane ever read the declared pool
floor. A locally served 32k body could not carry one persona turn no matter
which single lane an operator tuned (measured: 68 debited calls, zero
authored actions), and the practical ~93KB carriers of an ordinary run left
no headroom for growth.

**Decision.** Fit is a standing invariant, not an error path, enforced in
two tiers every turn:

1. *Mechanical, free.* One deployment-wide scale — the smallest admitted
   window's byte budget (window minus output and system reserves, at a
   bytes-per-token value that ADR-0107 demotes to a pre-measurement seed:
   provider-counted tokens supersede it from the first observation) over the shipped worst-case
   lane sum — resolves every default lane bound, each with a stated floor so
   no lane vanishes. The assembly-end fit stage then makes the SUM true:
   largest non-authority lane first, the situation stage restages at tighter
   caps and observation lanes fall to whole-lane structural indexes
   (existence + hash + read action, fetchable, never silently truncated).
2. *Model-assisted, priced honestly.* Where mechanical bounding would
   reduce a bulky observation lane (blackboard history, collaboration
   heads, peer work states, the situation stage) to a bare hash, the SAME
   pool body may compress it instead. The substrate authors only the
   mechanical instruction; the output is never trusted as authority — the
   record is labeled `model_interpretation: true` with the interpreting
   body implied by the turn, carries the exact `source_value_hash` and byte
   count, keeps the lane's read action as the exactness pointer, and is
   memoized per (lane, source hash, target) so an unchanged lane costs
   zero calls on later turns. A failed or unavailable compaction falls
   back to the structural index; the turn never blocks on it. Compaction
   spend rides the turn's own budget under a stated purpose and is visible
   in the spend census.

**The authority line, stated once:** principal intent and charter bytes,
contract text, acceptance rows and refusal codes, resource facts, and
directed speech are never scaled below their floors, never indexed away,
and never model-compacted. They ride exactly, or the transport refuses
with the exact byte fact — a statement, never a silent truncation.

## ADR-0103 — Tool arguments ride as real grammar on schema-to-grammar transports

On a transport whose response schema compiles into a sampling grammar
(llama.cpp `response_format: json_schema`), the multi-tool argument union is
one `oneOf` variant per leased tool, each carrying the tool's ORIGINAL input
schema verbatim (only `pattern` is stripped — one tool's regex has broken a
whole grammar, measured). The grammar itself then enforces every declared
constraint at sampling time — root and nested `required`, enums, closedness —
and open roots stay genuinely open. Measured on the release body: 73 tools,
56KB schema, 72 prompt tokens, and sampling forced the exact
`delivery_disposition` shape a 27B body had omitted on every carrier-shape
attempt.

Strict CLI response dialects keep the composition-free one-string carrier
(they reject `oneOf` below the root); the operator escape hatch for exotic
converters is `PERSONAOS_TOOL_ARGS_TRANSPORT=carrier`, stated, never
inferred. Server-side validation walks declared subtrees so a nested miss is
named by dotted path (`delivery_disposition.kind`) on every transport. Under
navigation byte pressure the action catalogue reduces to a names-and-gist
projection, never to a nameless structural index: on grammar transports the
schema text never enters the model's context, so that catalogue is the only
semantic channel the action surface has.

## ADR-0104 — The publication footrace is a stated fact on the acceptance page

A qualified receipt bound to a non-latest admitted publication carries the
exact changed-path delta to the latest one — added/changed/removed counts and
a bounded path list, computed mechanically between the two publications'
recorded merged-main commits. No acceptance semantics change: binding stays
by publication event identity; the substrate states the delta so verifiers
can re-receipt exactly the delta and settle verdicts can distinguish
"unverified package" from "files appended after the last receipt". Observed
need: a settle with 19 qualified receipts and 0 binding the final
publication, because a 3-file publish landed 90 seconds after the newest
receipt and the budget died mid-race.

## ADR-0105 — Role attribution defaults to the turn purpose; choices outlive their run

The role half of ADR-0086 D3, made reachable: a model request whose role is
unset adopts the turn's purpose token — attribution derived from exact signed
wake facts, varying per turn, so it is not "a single constant literal applied
to all turns". An explicitly passed role always wins; the purpose vocabulary
IS the reachable role vocabulary until a richer signed role fact exists. This
makes the operator role→model preference matchable (e.g. route
`carrier_compaction` turns to a small local body). Selection authority is
unchanged: role and purpose still choose nothing by themselves.

The persona-model-choice match scope drops `run_id` and `run_model_pool_hash`
(the hash bakes in run id and minted-at, so a successor run of the same task
chain could never match, and boot-restored choices were unmatchable by
construction). Both stay RECORDED on the signed choice as exact provenance.
Ceiling authority is preserved where it belongs: a choice naming any body
outside the CURRENT run's signed available set never matches.

## ADR-0106 — Continuity completes; the sandbox states its egress

ADR-0088's export half ships: `ai-personas export-persona` boots the node
against a state root, hydrates signed state exactly as a serving boot would,
writes the bundle(s), and exits. Import creates the binding it previously
only counted: fragment ids are content-derived and mapped source→destination,
the source's newest binding is reproduced onto the destination's current
winning head (never displacing it), and every count reported is truthful —
including `skipped_binding_refs` for refs that did not survive the transfer.

The provisioning mechanism state additionally carries one boot-time sandbox
egress probe — the pip index host the sandbox's pip would actually use, its
HTTP status, and the probe time (host only; an index URL may embed
credentials) — plus the interpreter version. These are mechanical deployment
constants exactly like the tool-site writability facts beside them: they name
no package, tool, or source-host preference and read identically for a task
that needs nothing. Observed need: the index answered 200 from every live
run's host while nothing anywhere stated the sandbox has network, so a
model's default "sandboxes are offline" prior made never trying the mechanism
the rational read.

## ADR-0107 — Measured windows: carrier budgets learn from provider-counted tokens

- Status: accepted (2026-08-30)
- Drives: `deployment_policy.record_carrier_density_observation()/
  carrier_density_bytes_per_token()/measured_token_estimate()/
  carrier_output_reserve_tokens()`; the assembly fit budget and every
  transport admission gate resolving through that one conversion; the
  adapter `/tokenize` capability probe; the first-call refit
  (`MODEL_CONTEXT_REFIT`); `personaos-continuation-fit/1`

**Problem.** ADR-0102's tier-1 budget converted the window to bytes through
a constant, and the transport admission gates used two DIFFERENT constants
(2.5 and 4 bytes/token — plus a third, 4-halved, deriving the navigation
default). Live at an 81,920-token window the 2.5-derived budget said
197,120 bytes "fits" while real carriers tokenized at ~2.31 B/token:
three turns died on the provider's own refusal ("request (85,491 tokens)
exceeds the available context size (81,920 tokens)"), ten follow-on calls
burned against the exhausted causal budget, and the ADR-0102 ladder never
engaged because its gate lied. Meanwhile every truth arrived and was
discarded: `usage.prompt_tokens` on all 38 successes was never parsed, the
refusal's own measured count survived only as a truncated reason string,
and the serving tokenizer's exact-count endpoint was never called. At 32k
the same constant erred the OTHER way (live density 2.64–3.57), silently
over-squeezing every carrier. In-turn continuation appends re-entered no
fit discipline at all, so a fitted carrier grew past the window mid-turn
(measured: 94,797 tokens). No constant is right at every scale, because
density is a property of the carrier mix and the tokenizer — a fact the
deployment can only measure.

**Decision.** The byte↔token conversion is a measured, per-boot fact; a
constant may only seed it.

1. *Usage is read, always.* Every completion response's provider-counted
   `prompt_tokens`/`completion_tokens` (any wire shape) is parsed into the
   result and recorded on the model event beside the exact transmitted
   `request_bytes`. A context refusal's stated counts are parsed the same
   way. Model events carry these facts for EVERY lane; the LEDGER
   observation is recorded adapter-side and only by a body that publishes
   its window — a hosted lane's density and completion lengths say nothing
   about the local pool the budget serves. The public telemetry projection
   carries the counts too (content-free mechanical facts — they make
   density and generation rate observable without one byte of carrier
   content).
2. *The budget learns.* The deployment keeps the observed density floor
   (minimum bytes/token) and the largest observed completion. The carrier
   byte budget is the pool floor minus the learned output reserve, times
   the density floor — recomputed whenever either fact moves, in BOTH
   directions: it shrinks where measurement proves overflow and grows where
   measurement proves headroom. Before the first observation the seed
   reproduces the prior shipped arithmetic exactly. The invented system
   reserve exists only in the seed regime: in the measured regime every
   consumer subtracts the EXACT system-prompt size at its own call site
   (template framing needs no reserve at all — the ledger's token side is
   the provider's count of the whole served request, so framing lives
   inside the ratio).
   Junk observations are refused with stated reasons (below a minimum byte
   size they measure the template, not the mix; outside a physical sanity
   envelope the two counts describe different requests).
3. *One conversion, one unit.* Every admission gate and the fit budget
   resolve through the same bytes→tokens helper, and every byte count is
   the same unit: raw transported characters (prompt plus system), exactly
   the unit the ledger joins against provider counts. Two gates that
   disagree about what a byte is worth — or measure different bytes, as the
   escaped-framed-JSON gate did against the raw-byte budget — re-create
   this failure class by construction.
4. *Exact counting where served.* Where the transport exposes its own
   tokenizer (`POST /tokenize` at the origin root — llama.cpp, vLLM), the
   admission gate consults it and prefers the exact count; the capability
   is probed once, its absence stated as a degraded read, transient
   failures leave it re-probeable. The estimate path remains for transports
   that serve no count.
5. *Overflow feeds back.* A deterministic context refusal on the FIRST call
   of a turn phase (no served response, so no effects) records its measured
   density, re-enters the fit stage once under the corrected budget — the
   ADR-0102 ladder now actually engages — and redispatches once, stated as
   `MODEL_CONTEXT_REFIT` with before/after bytes and the parsed counts.
   The refit carrier must be strictly smaller or the retry is refused:
   ADR-0086 D2's ban on replaying an identical carrier stands. A refusal
   after any served call is never replayed — effects may exist. The charged
   redispatch is the exact parallel of 01_KERNEL §7's charged mechanical
   reformat attempt.
6. *Continuations re-enter the fit discipline.* An appended tool-result
   payload respects the same learned budget as the opening carrier: over
   the remaining headroom, its largest members reduce through the bounded
   open projection (source fingerprint, stated truncation) and the squeeze
   is stated in the payload as `personaos-continuation-fit/1`; when
   per-member floors cannot reach the cap, the payload collapses to one
   stated record that keeps the ok/error census and the content hash —
   never a silent truncation, never unbounded growth, never an overshoot.

Rejected, with reasons recorded: re-tuning the constant (the round that
produced this ADR began as exactly that — 2.5→2.2 with a safety fraction —
and was refused as the same disease: an open-loop number standing in for a
measurement the system already receives every turn); refunding the burned
call instead of preventing the burn (funds-before-work stands; the fix is
that the second identical burn cannot happen); a persistent cross-boot
density store (a boot's first turns run one conservative seed regime and
converge within one observation; persisted calibration can go stale against
a swapped model or tokenizer without any event saying so).

## ADR-0108 — Learning that reads itself back; receipts that bind executions; cohort acceptance recorded

- Status: accepted (2026-08-31)
- Drives: the prompt-compile verifier's producer-shape agreement and the
  `kernel.prompt_compile_refused` degraded read;
  `personaos-receipt-execution-binding/1` on every verifier receipt;
  `PERSONA_AUTHORING_REFUSED` lineage observations;
  `personaos-cohort-acceptance-disposition/1` /
  `TASK_COHORT_ACCEPTANCE_RECORDED` and the `cohort_accepted` terminal
  state; `personaos-sandbox-executable-inventory-probe/1`; contract
  live-set statedness at authoring; the command/cmd argv alias and the
  transport-computed `content_ref` declaration mode

**Problem.** A four-run audit (two bodies × two domains, ~700 calls, zero
transport failures) found the learning loop's first four stages working —
122/122 distillations became durable signed fragments and bindings tracked
them — while the fifth did not run: fragment bodies reached zero of 1,693
prompt-facing blobs, per-persona system prompts were byte-constant across
whole runs, and three live incidents showed a lesson bound at the exact
moment its own prohibition was violated. Root cause: the compile producer
ships tuples in-process, the prompt verifier demanded lists, and every
compile carrying bodies was refused `fragment_body_projection_invalid` —
silently, because the refusal reached only an in-carrier absence code.
Separately, verification integrity split cleanly on one mechanical fact:
all 9 receipts of the two weaker runs carried `inputs: {}` while asserting
computed values that appear in no execution output (one attested a
59,659-byte sealed result where the file on disk is 259 bytes of parse
error; another accepted "2,600 sf" that nothing ever computed while honest
sums said 2,612, out of band); all 29 receipts of the two stronger runs
carried resolvable execution bindings. Contracts drifted unsuperseded
(three concurrent inconsistent contracts in one run; a basis swap that
orphaned the executable validator in another), receipt refusals never
reached lineage, and no ownerless task could ever record acceptance — the
kernel's disposition ledger read zero in all four runs while "accepted"
lived in persona prose.

**Decision.**

1. *Carry is conformance, not choice.* The compiled fragment-body page
   (already produced and verified under its own byte budget) renders into
   the persona system prompt; §20.3's clause that the binding "determines
   which fragment bodies may be included in a later carrier" is now true on
   the wire. A verifier refusal of a supplied compile is a degraded read,
   countable, in addition to its in-carrier absence code. Producer and
   verifier accept each other's exact in-process shapes; the agreement is
   pinned by tests that cross no serialization boundary.
2. *A receipt states its own grounding.* Every verifier receipt's
   kernel-signed event carries a mechanical join from the receipt's
   `inputs` to execution events by the same signer
   (`personaos-receipt-execution-binding/1`): key-name-blind id scan,
   lineage resolution, signer match. `execution_bound: false` refuses
   nothing and states everything; the persona-signed preimage is unchanged
   so every recorded receipt stays verifiable.
3. *Authoring refusals reach lineage.* A refused receipt or contract
   authoring appends one bounded `PERSONA_AUTHORING_REFUSED` observation —
   the class that previously survived only when a persona narrated its own
   refusal into a lesson.
4. *The live contract set is stated at authoring.* A new contract names the
   coexisting live contracts and whether it supersedes; coexistence is
   never refused, and never again silent.
5. *Cohort acceptance is recordable.* When a receipt closes an acceptance
   contract under five mechanical joins — live unsuperseded contract bound
   by scope; current adjudicated publication; `execution_bound: true`;
   signer authorship-edge exactly absent; terminal result accepted — the
   kernel mints `TASK_COHORT_ACCEPTANCE_RECORDED` (task scope). The
   projection reports the distinct terminal state `cohort_accepted`, which
   never claims and never outranks owner acceptance; the disposition states
   its standing on its face (cohort-decided, not externally certified). An
   unbound chain can never mint, structurally excluding the
   fabricated-number path. Unmet conditions are returned as stated facts;
   the mint never blocks the receipt.
6. *The inventory is a stated deployment fact.* Following ADR-0106's
   argument exactly — nothing stated the sandbox has network, so never
   trying was rational — a boot probe records the executable-inventory
   COUNTS and the read action (no names, no versions, no ranking): four
   runs on a host with full professional toolchains produced zero installs
   and, on the weaker body, zero capability inspections, with one cohort
   spending shell turns on `which`.
7. *Two frictions with live failure counts close.* `command_exec` accepts
   the argv array under `command`/`cmd` (21 refusals — the same alias class
   as timeout/argv); a local `declare_artifact` whose current bytes the
   transport verified may omit `content_ref` — the transport computes,
   verifies, and records the digest with `content_ref_source:
   "declaration_transport_computed"` (5 refusals plus one run's
   zero-declaration cascade into receipt preimage failures). Conflict
   inspection names its owner; capability paging states its bound.

Rejected, with reasons recorded: raising the auto-distill retention window
(canon-intended "newest few" protects persona-curated bindings; the remedy
is curation, which requires carry first); requiring execution bindings on
receipts (persona-authored contracts already demand execution where the
cohort wants it; a substrate requirement would be a tool-provenance
constraint on adjudication); coercing births or model choices (surfaces
are delivered and read is free; absence is a finding about gradients, not
gates); auto-terminating runs on cohort acceptance (personas keep authoring
their own dispositions; quiescence follows visibility).

### ADR-0108 addendum (2026-08-31, from the first live run on the build)

The run validated the decision set by counterfactual and exposed four
successor facts, folded in as addendum rather than a new ADR:

1. *Carry carries what is written.* The loop's carry stage worked and all
   ten distilled fragments were situational status snapshots; the influence
   stage had no subject, and one frozen snapshot anchored a stale claim its
   author repeated after the evidence changed. Doctrine (not machinery) now
   names the gradient: a fragment records what would change the next
   attempt; a status restatement is noise wearing permanence; a memory that
   disagrees with present evidence is revised, not obeyed.
2. *Execution-bound receipts contained a fabrication.* A synthetic-sine
   "verdict" over a simulation that never ran was broadcast bar-clearing;
   the receipt doctrine refused to sign without executed counter-evidence
   and no acceptance was minted. The cost surfaced as a mutual-parking
   deadlock (every persona's anti-noise rule waiting on another); doctrine
   gains its counterpart: staging is not verifying, a fact computable from
   readable bytes is never waited for, parking requires that no own action
   advances the work.
3. *The contract authoring result hands the receipt scope.* Two kernel
   event ids sharing a timestamp prefix let a wrong pointer propagate into
   38 records; the result now carries `receipt_scope:
   "cohort-contract:event:…"` verbatim. Statedness additions of the same
   kind: open-input refusals carry a mechanical key diff against the
   requester's own response_schema; resolutions state whether any
   contribution binds; a bare 64-hex content reference canonicalizes, and
   BOTH signed-args verifiers compare through one canonicalizer with the
   transport-computed disjunct admitted (review-caught: the recorded
   canonical form otherwise diverged from the signed bare form and
   declarations silently dropped from settlement).
4. *Every cohort member carries doctrine.* Seeded neutrals ran on empty
   souls while four of the audit's pathologies were theirs; a minimal
   work-discipline collaborator soul (executions over restatements, claimed
   results name their execution, no placeholder posted as an answer,
   structural acts fill fields) closes the asymmetry operator-side.

## ADR-0109 — The audit closes its own instruments: envelope recall, stated declines, curated memory survives, paced retries

- **Status:** accepted (2026-08-31)
- **Context:** the first luna pair on the ADR-0108 build (e33 circuit + house)
  produced the project's first fourteen kernel-recorded cohort acceptances and a
  forensic audit of both runs. Every ADR-0108 mechanism held (scope handover
  23/23 + 12/12; refusals durable and adaptive 13/13; the deadlock signature
  dead; zero context overflows). What the audit found instead was a layer of
  instrument defects — places where the substrate measured honestly but too
  narrowly, or computed a fact and let it evaporate — plus the round's central
  behavioral finding: **the cohort's own first-minute contract acts as a
  ceiling that overrides soul doctrine**, so verification compounds (66% of
  budget after the last design mutation; eleven of thirteen acceptances over
  byte-identical design content) while the deliverable freezes.
- **Decisions (mechanical):**
  1. *Receipt execution binding resolves the action envelope.* Live receipts
     cited real same-signer rc=0 executions by their `PERSONA_ACTION_*`
     envelope ids; the scan resolved only raw exec kinds, so seven receipts
     read unbound and three accepted receipts were wrongly declined minting.
     The scan (binding schema /2) now grounds a cited `PERSONA_ACTION_COMPLETED`
     whose `action_name` is an execution, grounds a cited AUTHORED id only
     through its COMPLETED back-pointer (launch-not-run parity), collapses the
     doubled `event:event:` prefix, and states a `cited_non_execution_kinds`
     census so an unbound receipt names what was actually cited.
  2. *A declined mint states itself in lineage.* The five mint conditions are
     receipt-event-independent, so they are evaluated before the receipt append
     and ride the kernel-signed receipt payload (`cohort_acceptance_mint`,
     observation schema /2, `mint_eligible` + every unmet condition). The
     persona-signed preimage is untouched. Sibling statedness: the open-input
     projection derives `resolution_selected_contribution_id_present` (the
     record payload is strict-signed on both layers and stays untouched);
     acceptance projections state `cohort_acceptance_publication_stale` — a
     cohort-accepted task whose delivery moved past its last acceptance is a
     stated fact, never a reopened closure (noise publications would otherwise
     hold every task open).
  3. *Deliberately authored memory survives the recency trim.* Both live runs:
     the explicit `author_brain_fragment` channel produced the genuine lessons,
     then the newest-N cap let kernel-automatic turn-slot status snapshots
     evict them (four near-duplicate settle notes displaced a persona's two
     reusable failure+fix lessons). The explicit channel now marks its
     fragments (`persona_action_authored`, mechanical provenance, never
     content) and the trim exempts them exactly like evolved fragments — the
     cap's own stated purpose. Fragment anchors canonicalize to one `event:`
     prefix (every live fragment carried an unresolvable doubled ref).
  4. *Failure facts tell the truth at the edges.* An rc=0 execution refused on
     an `expected_stdout` mismatch is coded `expected_stdout_mismatch`, not
     `exec_exit_nonzero` (a live persona had to diagnose the mislabel in a
     brain fragment); authoring-refusal observations default `reason_code` to
     the error token and `stage` to the refusing gate instead of empty strings.
  5. *Retries pace to the provider's stated horizon.* A quota-dead provider
     cost 44 empty scheduler turns over 41 minutes because transport backoff
     capped at 30s against a multi-hour cooldown the router already knew. The
     router states `all_models_cooldown_remaining()`; the retry keeps its exact
     replayable wake and simply waits out the horizon (bounded 1h per hop).
- **Decisions (doctrine, domain-free):** steward v10 — a limitation stated
  twice is a bar owed to the contract (supersede or record why out of scope; a
  pre-work contract is provisional); a check that reads none of the delivered
  bytes verifies nothing; verification that changes nothing records nothing.
  builder v6 — at each stage's edge ask what instrument the stage needs (the
  exploration dual of the anti-hoarding clause; presence-probed-and-idle tools
  are exercised before their stage closes); a tool's warning is a finding at
  exit 0; create and verify in separate executions; changed work that needs a
  counterparty is announced with a wake. collaborators v2 — the byte-reading
  check test, verification economy with evidence-log hygiene (logs live in the
  persona workspace; cite executions by id instead of re-publishing regenerated
  logs — six personas' regenerated timing-noise log was the run's largest
  merge-conflict source at 16.3% of all actions), and the instrument-reach
  clause.
- **Consequences:** the three wrongly-declined acceptances become mintable on
  fresh receipts; declined mints and stale acceptances are auditable from
  lineage alone; the learning loop's best records can no longer be evicted by
  its noisiest; the exploration gap (twelve advertised acquisition affordances,
  zero invocations, a fully-installed consuming-tool suite presence-probed
  only) is addressed at the doctrinal layer where the evidence located it —
  the substrate preconditions were all present and stated. The contract-ceiling
  finding's task-authority lever (an operator-supplied `acceptance_condition`
  demanding realization-grade outcomes) is recorded as the experiment ladder:
  pure re-run, then cognition import, then operator bars — one variable per
  run.

## ADR-0110 — Certified means examined; voids refuse; bounds are measured, declared, or absent

- **Status:** accepted (2026-08-31)
- **Context:** the e34 pair — the first controlled tier A/B (identical task,
  build, 8-persona cohort with a three-seed control arm; only the model body
  differs) — settled 200/200 both arms. The audit found the ADR-0109
  machinery working (envelope binding carried all four luna mints; stated
  declines landed in lineage; anchors resolve 100%; the deliberate-lesson
  exemption held clean under 27 live trims) and, beneath it, a defect class
  the machinery had made visible for the first time: **acceptance was
  certifying deliveries the verifier never examined** (8 of 12 receipts and
  3 of 4 mints adjudicated a stale publication — the adjudicated row is
  "latest admitted at authoring instant," a moving target eight publishing
  personas outrun; the steward derived the exact staleness fact by hand and
  was ignored). Around it: structural acts silently voided (19 of 23 posts
  in the qwen arm landed `text:""` under invented argument keys and were
  cited as evidence; five artifact declarations landed as content-free
  shells); the authoring gate destroyed three receipts by collapsing an
  unreadable run index into "this run never existed"; atomic-commit actions
  (wakes, receipts, work states) produced authored events with zero terminal
  observations because both dispatchers discarded the post-commit persisted
  identity; and the auto-distillation channel manufactured a quiescence
  flywheel (34 of 45 turn-slot fragments the same "do no more work" recital;
  one seed re-minted the identical paragraph eight times).
- **Decisions (mechanical):**
  1. *Publication currency is the mint's sixth join.* The signer's
     host-sealed executed counter-evidence must intersect the CURRENT
     delivered surface's digests (the newest whole-tree snapshot row, else
     the adjudicated row — the same surface the read-side qualification
     and the receipt reply measure, so the three can never disagree), or
     the sync disjunct must hold (a kernel-signed publication-sync fact
     for the exact adjudicated id+hash plus a sealed executed receipt
     after that instant — parity with persona acceptance, so
     log-capturing verifiers are not starved; the disjunct counts only
     when the adjudicated row IS the current surface, so an
     explicitly-requested older publication can never sync-qualify). Unreadable currency
     declines under its own code (`signer_evidence_unresolvable`), never as
     absence. Mint-observation schema /3; the disposition schema is never
     bumped (recorded history stays admissible).
  2. *The binder's recall is complete and uncapped.* Citations are read
     from `terminal_result` as well as `inputs`; a cited STARTED grounds
     through its COMPLETED pair exactly as a cited AUTHORED grounds through
     its envelope back-pointer (launch-not-run parity in every lane);
     binding schema /3. The invented 64-citation, 8-resolution and
     16-census caps are gone — the citing member's own transported size is
     the bound; the id gate is the protocol-exact `event:` + 26-char form.
  3. *Content-bearing structural acts refuse the silent void.* A blackboard
     post whose body resolves empty after alias folding, and an artifact
     declaration whose artifact_ref AND content_ref both resolve empty,
     refuse loudly, naming the recognized fields and every received key —
     the live evidence showed the loud-refusal path teaching correctly and
     the silent-void path swallowing the corrected intent.
  4. *Unreadable is never absent at the authoring gate.* The run-index read
     states its availability; a failed read refuses as
     `run_index_unreadable` (retryable) without judging the named run; a
     genuine absence states the mismatched member and the recorded runs in
     full. Ambiguity refusals carry ledger tokens
     (`ambiguous_execution_forms`, `argv_args_ambiguous`, `cwd_ambiguous`).
  5. *Atomic actions record terminal observations.* Both dispatchers carry
     the post-commit persisted identity into the effect recorder; all seven
     atomic-commit tools (wakes, receipts, work states, capability acts)
     now close their authored events. Refused atomic actions stay
     unpersisted by design.
  6. *The carriage carries no duplicates and no invented counts.* A
     body-identical duplicate of a currently-carried fragment records but
     does not bind, stating `duplicate_of`; the newest-3 and marked-16
     count caps, the 128-fragment head refusal, and the 8,192-byte inner
     page budget are all removed — every distinct fragment binds, and what
     rides each prompt is bounded by the ADR-0107 measured carrier
     arithmetic alone, with the compile's existing omission statedness.
- **THE STANDING RULE (operator directive): no artificial constraints.**
  Every bound is measured (ADR-0107 window arithmetic), authority-declared
  (task budgets, operator ceilings, supplied deadlines), protocol-exact
  (sha256 64-hex, `sha256:`+64=71, ULID 26, `event:`+26, OS argv limits),
  or absent. Removed this round on touched surfaces: the 32KB receipt
  member gate (both layers), the cooldown-pacing 3600s clamp, the refusal
  truncations (`[:120]`/`[:60]`/`[:16]` list slices), the binder caps, the
  fragment count caps and head refusal, the 128-fragment bind gate, the
  inner page budget. **Queued inventory (all INVENTED, replacement =
  lane-scaling from the measured carrier budget unless noted):** the
  prompt-lane MAX_BYTES family (256K carrier / 64K×5 / 48K / 32K / 24K /
  16K), page and collection limits (schedule 16, conflict pages 8/16,
  ladder rows 8, batch 8, ancestry 128, receipt page 32, situation items
  100 / 320K chars, resume observation 48K, identity sections 64/20K,
  sealed-generation entries 32), `_EXEC_CAPTURE_RESULT_JSON_BYTES = 650`,
  the 64-receipt per-signer lane bound (replacement: authority-declared),
  the 32/64MB model-input caps, `_NO_DEADLINE_EXECUTION_CEILING_S = 7200`
  (replacement: the measured time axis llama.cpp already reports), and the
  router's `MAX_MODEL_QUOTA_COOLDOWN_S = 7 days` — retry pacing now
  follows the provider's DECLARED retry-after horizon unclamped, and that
  seven-day constant is the one remaining guard between a misreported
  declaration and a week-long stall; it is named here as the declared
  bound of record until the inventory replaces it.
  KEPT as non-artificial: `PRINCIPAL_TASK_DEADLINE_MAX_EPOCH_SECONDS`
  (ISO-9999 representability, protocol-exact) and every operator-declared
  ceiling.
- **Doctrine verdict (three controlled runs):** no souled/unsouled
  separation on any doctrine-targeted behavior — seeds authored 42% of
  receipts, half the mints, the only latest-publication-bound mint, the
  sharpest lessons and withholds; the richest-souled personas contributed
  least on exactly their souls' axes. Soul iteration stops; souls stay as
  shipped. The levers that remain are mechanical statedness and
  task-authority bars.
- **The bars experiment (e36, queued):** operator-supplied
  `acceptance_condition` + `unaccepted_rewake` at POST /task, with outcome
  bars (one deliverable of record; geometry-verified rooms with openings
  cut in the solid; one source of truth across artifacts; format-validity
  or stated non-fabricability; a structural screen at stated assumed basis;
  grounded quantities; currency-bound acceptance). It tests the audit's
  standing conclusion: capability acquisition (CAD-class tools, engineering
  sims) never emerges because no bar ever prices an outcome the current
  toolbox cannot cheaply produce — the cohort's own contracts price
  process, whichever tier writes them.
