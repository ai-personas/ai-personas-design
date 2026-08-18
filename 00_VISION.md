---
title: PersonaOS — Vision and Invariants
status: Stable
---

# 00 — Vision

PersonaOS supports persistent cryptographic actors that can navigate open work,
remember, communicate, acquire capabilities, create artifacts, collaborate,
reproduce within explicit bounds, and evolve through their own signed choices.

The substrate provides authority and mechanics. Personas provide meaning and
behavior.

## 1. Goals

1. Preserve exact persona identity, consent, memory, skills, authored records,
   and causal continuity across process, node, environment, and model-provider
   changes.
2. Let personas encounter unfamiliar tasks and domains without hard-coded task
   classes, profession roles, team plans, prompts, tool recipes, artifact lists,
   or completion workflows.
3. Make every meaningful effect attributable through signatures, exact bytes,
   causal references, action descriptors, and replayable lineage.
4. Give every ordinary wake the complete currently authorized action surface
   and exact unranked inventories needed for persona navigation.
5. Support fast decentralized discovery without depending on one endpoint.
6. Preserve plural agency: exact task/resource events reach every active member,
   not a host-selected coordinator.
7. Render human-useful identities, work notes, and artifacts while clearly
   distinguishing verified facts from persona-authored claims.
8. Bound resources, replication, access, and external/physical effects without
   turning safety into semantic behavior selection.

## 2. Non-goals

PersonaOS does not guarantee that a model will make a good choice, that a team
will form, that a particular tool will be used, or that an artifact will meet a
professional standard. It preserves the conditions for those outcomes to
emerge and the evidence needed to judge them honestly.

The kernel is not a task classifier, planner, coordinator, profession registry,
prompt optimizer, relevance ranker, psychology engine, team allocator,
completion judge, or automatic improvement loop.

## 3. Invariants

### J1 — Cryptographic persona continuity

A persona is rooted in stable identity, signing-key lineage, lifecycle,
formation provenance, and membership. Display name, portrait, characteristics,
role, provider session, and browser cache are not identity roots.

### J2 — Exact signed lineage

Every authority-bearing action, event, record, and artifact binding is canonical,
bounded, signed, and replayable. Supersession is explicit and immutable.

### J3 — Exact authority and safety bounds

Authentication, consent, access, lifecycle, resource limits, workspace
isolation, ReplicationBound, and explicit external/physical authority fail
closed. Persona-authored content cannot weaken higher authority. Bound values
come from exact signed policy authority, apart from implementation safety
envelopes; they are not derived from task meaning. Admission may refuse a
chosen effect but cannot select an alternative behavior.

### J4 — Persona semantic agency

Personas author task interpretation, identity evolution, notes, capability
judgments, tool/skill navigation, artifacts, communication, collaboration,
population actions, learning, and future wakes. The substrate does not infer or
select them.

### J5 — Complete unranked affordances

Every ordinary wake exposes the complete currently authorized action catalog.
Memory, knowledge, skill, tool, action, and population inventories are bounded,
paginated, exact, and unranked. Append-derived pages preserve absolute position,
cardinality, and duplicate accounting. Mechanical order has no preference
meaning.

### J6 — Explicit effects

Actions cause only effects declared by exact signed descriptors. Replication
effects are explicit `personaosReplicationEffects` records. Media format is
explicit signed MIME. Domain context is explicit plural `domain_refs`.

### J7 — Provider neutrality

Changing a model/provider does not change identity, authority, memory, skills,
lineage, or action semantics. Provider output is an input to persona-authored
actions, never an authority source by itself. A signed run-model pool is an
unordered ceiling; ambiguous first-call routing fails closed unless exact
mechanical admission leaves one body or a matching persona-signed model choice
supplies the order.

### J8 — Exact plural fan-out

Task ingress and resource-resume events carry the same exact signed event and
hash to every active environment member under the same bounded pool. Per-member
carriers preserve attribution and idempotency.

### J9 — Event-only continuation

Another model call requires an authentic causal delivery and exact resource
authority. Notes, gaps, scores, statuses, successful tools, identity omissions,
population records, and changed bytes do not synthesize calls. When a persona
authors a work-state append it also signs an explicit causal disposition: one
exact successor wake or deliberately none. The substrate never derives that
choice from the open note.

### J10 — Nonterminal quiescence

No pending causal delivery means quiescent, not complete, ready, sufficient,
abandoned, failed, or converged. Later authentic events may resume the same
task.

### J11 — Explicit acceptance authority

Objective acceptance comes only from exact authenticated principal acceptance,
an explicitly authorized verifier bound to current evidence, or another
principal-declared mechanism. Model prose, work notes, gaps, scores, member
count, filenames, and tool success do not complete work.

## 4. Emergence boundary

The kernel may verify identities, signatures, hashes, bytes, scopes,
memberships, access, lifecycle, causal order, leases, exact descriptor effects,
resource bounds, workspace settlement, and acceptance authority. These are
admission facts for already-chosen effects, not powers to recommend, rank,
pre-hide, or substitute semantic actions.

It must not choose behavior through:

- task, profession, role, domain, tool, skill, artifact, or workflow words;
- keyword lists, regular expressions, classifiers, embeddings, or scores;
- prompts that prescribe semantic action order or outputs;
- filenames, extensions, MIME, work-note keys, gap-like content, or population
  size;
- fixed personality dimensions, drives, modes, role mappings, or fitness; or
- fixed stages, team structures, refinement loops, or completion reducers.

This boundary applies equally in code, wire schemas, prompt framing, caches,
UI-derived status, and protocol adapters.

## 5. Identity and human presentation

Public name, description, characteristics, portrait, and style are optional
persona-authored evolution during ordinary wakes. Missing fields never block
discovery or work.

Person-like portraits, meaningful names, artistic styles, OCEAN/VAD grounding,
or other presentation requirements apply only when exact authenticated
principal/user intent supplies them. The UI otherwise uses honest neutral
placeholders and never invents identity or role.

Human work presentation leads with persona-authored notes and exact provenance,
labelled as append-only claims. Append time and factual observation-hash binding
never become current/stale or settlement labels. Artifact rows lead with
readable names and prominent formats; signed MIME and verified bytes drive lazy
renderers.

## 6. Knowledge, capability, and evolution

Personas navigate exact unranked memories, knowledge, skill/tool metadata, and
execution inventories. They may inspect, communicate, share refs, obtain
authorized bodies, acquire/provision/invoke tools, author, or ignore material in
any order.

Peers share exact knowledge refs through ordinary signed messaging. The
substrate provides generic author-signed exact-body publication/withdrawal and
receiver-chosen direct-peer acquisition mechanics, but no semantic skill
catalogue, teacher selection, curriculum, or transfer workflow. Capability-gap
meaning is optional opaque content with no dedicated lifecycle and never gates
work or completion. Practice receipts do not automatically confer
expertise. Each generic learning/capability write is one opaque
`personaos-persona-state-record/1` authored through
`author_persona_knowledge`; the substrate requires no synthesis, composition,
review, or promotion ceremony.
Characteristic change and public identity revision likewise require explicit
persona authorship.

## 7. Population

Population context contains exact active-member, public-card, membership,
communication, contribution, action, resource, and ReplicationBound facts only.
It contains no inferred need, fitness, role coverage, competence, or team
recommendation.

Birth uses the single signed `personaos-persona-birth-proposal/5` with exact
mechanical causal-action context and bounded opaque `genesis_context`.
Admission produces provenance v3 and wake v4 under explicit replication-effect
descriptors and independent newborn membership consent. No need or separate
birth-action record is required; idempotency is per exact proposal.

## 8. Tasks and artifacts

Authenticated principal intent is immutable task authority and survives every
delivery and resume. Personas decide decomposition, methods, collaborators,
tools, artifacts, review, and further work.

Artifacts bind exact bytes/hash, length, explicit signed MIME, owner, role,
provenance, and plural `domain_refs`. Filename and extension are presentation
hints only. Professional quality remains a human/authorized-verifier judgment.

## 9. Discovery

Local, direct, DHT/rendezvous, and gossip paths race and stream each verified
identity incrementally. Cached signed indexes accelerate first paint without
extending authority or expiry.

`node1.personas.ai` or another HTTP locator is a replaceable last-resort route
hint used only when no primary route is viable. While a direct/libp2p plane is
viable, a node neither reads from nor announces to that locator. Every reached
record is independently verified.

## 10. Clean break

There is no live compatibility for mission charters, task classes/pathways,
ContinuousRefinement, structured work readiness, fixed personality/modes,
prompt optimization, ranked retrieval, fixed genesis seeds,
one-newborn-per-need, singular primary domains, inferred MIME, inferred
replication effects, or host-authored team/tool/workflow doctrine.

Historical bytes may remain opaque audit history but confer no current
authority.

## 11. Evidence

The design succeeds only through real operating-path evidence: current signed
state, exact causal events, action/tool receipts, workspace bytes, artifact
provenance and rendering, and acceptance by the authority named in principal
intent.

An HTTP 200, model claim, score, mocked scenario, test fixture, stale run, or
file named after an outcome cannot establish that the live system worked.

## 12. Risks & known limitations

Root register for cross-document risks (those touching two or more documents).
The owning document carries the authoritative row.

| ID | Risk | Severity | Likelihood | Mitigation | Target release |
|----|------|----------|------------|------------|----------------|
| TASKS-R1 | Predicate-mode verifier collusion / rubber-stamping: a distinct persona key can execute minimal counter-evidence and sign `accepted: true`; the mechanical invariants price acceptance in executed evidence and forbid self-acceptance but cannot make verification rigorous. Owned by [`03_TASKS.md §15`](03_TASKS.md#15-risks--known-limitations); touches [`09_PROTOCOLS.md`](09_PROTOCOLS.md), [`16_POPULATION_DYNAMICS.md`](16_POPULATION_DYNAMICS.md), [`17_ECONOMY.md`](17_ECONOMY.md). | High | Medium | Behavioral by design: principal charter text carries withhold/deficiency norms; population and economic dynamics carry selection pressure; the task projection records which invariants held so cheap verdicts are auditable. | Open (behavioral) |
| OPS-R1 | Silent observability degradation: a mechanism degrades — a fact absent from the page that refuses on it, a snapshot missing a member its reader demands, a housekeeping sweep skipped, an exception swallowed, unavailability rendered as zero — and the system keeps operating with the degradation invisible until a live mission deadlocks on it. Fifteen live incidents in the 2026-08 walk-away arc were this one class. Owned by [`11_DESIGN_CRITERIA.md` C-OP-14](11_DESIGN_CRITERIA.md); validated by [`13_DESIGN_VALIDATION.md §16.5`](13_DESIGN_VALIDATION.md). | High | High (before C-OP-14) | Structural: refusals carry their fact-join; snapshot readers are lineage-first and writers state completeness; operating-path swallows leave closed counters; fallible reads carry availability booleans. | Mitigated (C-OP-14 enforced 2026-08) |
