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

`personaos-persona-work-state/3` contains a bounded open `work_note` with exact
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

`run-model-pool/1` is a signed unordered per-run ceiling. Canonical model-ID
sorting does not rank it. `persona-model-choice/1` supplies the persona-signed
ordered model/reasoning-effort pairs for one exact persona, environment,
task/candidate/mission task, run, pool hash, and situation generation.

Without a matching choice, substantive cognition is admitted only when exact
mechanical checks leave one callable body. Two or more eligible bodies fail
closed. Provider, registry, configuration, lexical, default-client, cost, or
tier ordering cannot supply bootstrap authority, and the host cannot choose a
model merely to ask it which model the persona would choose.

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

## Consequences

Emergence is attributable: useful births, communication, learned skills, tool
use, CAD/CAM artifacts, identity changes, and continued improvement must trace
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
