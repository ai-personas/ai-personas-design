---
title: PersonaOS — Persona-Owned Knowledge, Memory, and Skills
status: Stable
---

# 08 — Persona-Owned Knowledge, Memory, and Skills

Knowledge in PersonaOS is signed material a persona can inspect and navigate.
It is not a host-selected prompt layer, relevance ranking, behavior program, or
automatic claim of expertise.

This document is a clean break from ranked retrieval, fixed memory tiers,
importance/fitness scores, decay formulae, host consolidation schedules,
prompt-optimization pipelines, top-K selection, and substrate-authored tactic
promotion.

## 1. One opaque knowledge/capability authoring path

The model-visible `author_persona_knowledge` action admits one opaque signed
persona-owned record per invocation. The persona supplies only:

- required `metadata`, an arbitrary bounded canonical JSON object; and
- optional `refs`, a bounded set of distinct exact record-reference strings.

The current mechanical storage envelope permits at most 262,144 canonical JSON
bytes and nesting depth 64 for `metadata`. `refs` accepts one exact string or at
most 32 distinct exact strings, each at most 500 UTF-8 bytes. These are
content-neutral allocation/integrity bounds, not knowledge kinds or behavior
selectors.

Persona identity and any nonempty environment/task bindings come only from
authenticated dispatch context or exact optional public bindings; absent
optional context remains empty. Model-authored values never create authority.
The record is persisted as the
existing `personaos-persona-state-record/1` with exact fields `schema`,
`record_id`, `persona_id`, `environment_id`, `task_id`, `record_kind`,
`content`, `evidence_refs`, `issued_at`, `signing_key_id`, and `signed_by`.
`record_kind` is the fixed mechanical routing value `persona_knowledge`; it does
not classify the content semantically.

Memory, lesson, skill, experience, self-context, fragment, capability, or gap
are meanings a persona may express in `content`; they are not protocol variants,
creation stages, or a closed kind taxonomy. Other durable stores such as memory
and mutable brain fragments retain their own exact boundaries; the generic
persona-state record is not imposed as a universal wrapper over them.

Open `content` and exact `evidence_refs` are persona-authored. Content may
describe a name,
interface, method, derivation, relationship among records, or anything else,
but none of those is a required or reserved semantic field. In particular,
there is no required operation enum, parent-skill shape, synthesized-skill
payload, composition list, rationale, evidence category, review state,
disposition, promotion status, or score.

The substrate verifies canonical bounds, signatures, authenticated context,
authority, hashes, references, visibility, consent, revocation, and replay.
It does not decide whether a body is true, important, relevant, a lesson, a
profession, a capability, a derivation, or evidence of expertise. If a persona
combines or derives material, that meaning and the cited relationships remain
inside its one opaque authored record; the host does not require a second
finalization record. A later record may cite an earlier one, but does not
rewrite its bytes or acquire automatic supersession semantics.

## 2. Complete unranked inventories

For each authorized view, the substrate exposes a bounded paginated inventory
of every visible record identity and exact metadata needed to request it. The
inventory declares snapshot identity, observed count, page/cursor boundaries,
and whether capture was truncated. Pagination never silently substitutes a
small prefix for the complete set.

For append-derived inventories, observed count and cursor positions refer to
authoritative append positions rather than distinct payloads. Equal record
bytes at different positions and redundant cross-scope observations remain
separately navigable. A separate unique-identity view may normalize only with
explicit duplicate accounting and raw-page navigation.

`inspect_persona_learning_history` continues the exact hash-bound inventory
already carried into an ordinary wake. It exposes retained turn-effect
episodes, exact brain evolution receipts, and persona-authored state records in
mechanical order with total, page, omission, and cursor evidence. It does not
select a lesson, interpret an outcome, grant expertise, or create a wake.
Persona-authored state has its own exact append-ordered cursor so its later
records remain navigable as execution evidence grows. Its original task binding
remains evidence while owner-authorized state can inform later tasks in the same
environment.

Inventory order may be lexical, append order, or another stable mechanical
transport order. That order has no relevance meaning. The substrate provides
no:

- relevance, similarity, quality, confidence, provenance, importance, decay,
  fitness, or usefulness score;
- embedding-selected, stage-selected, role-selected, or task-selected subset;
- top-K cut, reranker, recommendation, “best memory,” or preferred skill;
- keyword, regular-expression, filename, extension, profession, prompt, or
  domain-vocabulary selector; or
- hidden summary that replaces omitted exact identities.

The same rule applies to local memories, inherited records, environment
knowledge, peer-visible metadata, public discovery, and tool/skill registries.

## 3. Persona navigation

The persona chooses how to navigate from the exact inventories available in an
ordinary wake. It may request a body by exact reference, issue an authorized
search or external query, follow provenance, inspect a peer's public metadata,
ask another persona, send or receive an exact record reference, obtain a body
under current access/consent authority, author another opaque record citing it,
invoke an authorized tool, or ignore the material.

These choices may occur in any order and may be interleaved with ordinary task,
identity, population, communication, artifact, and workspace actions. The
kernel supplies no fixed exploration phase, retrieval stage, gap-first rule,
teacher choice, action sequence, or definition of enough knowledge.

An action receipt proves that the exact action occurred and records its effects.
It does not prove that the chosen material was relevant or that the persona
learned from it.

## 4. Memory

A memory is an authored signed record, not a hidden mutation of provider
context. Its authority and visibility come from exact consent, scope, and
lineage. Personal, task, environment, public, and shared memories may coexist;
none is automatically promoted over another.

The runtime does not automatically decay, reinforce, consolidate, summarize,
rank, retrieve, inject, or delete memories based on elapsed time, frequency,
emotion, model scores, task words, or behavior outcomes. A persona may author a
summary, lesson, correction, relationship, self-narrative, or superseding memory
as an explicit signed action and cite the source records on which it relied.

Memory omission from a bounded model carrier does not revoke the record.
Truncation is explicit and the exact inventory remains navigable. Retention and
deletion follow authenticated authority, privacy policy, and lifecycle rules,
not an inferred importance score.

## 5. Persona-owned capability material and executable tools

A persona-owned capability claim is ordinary opaque `content` in a signed
`personaos-persona-state-record/1`. Its transport surface exposes only exact
identity, author/context, body hash/reference and byte facts, evidence refs,
time, signing key/signature, and visibility/access authority. Any name,
description, interface assertion, method, relationship to other material, or
claim of capability is opaque persona-authored content rather than a required
substrate field.

Executable tool inventory entries are separate. They expose exact descriptors,
input/output schemas, effect annotations, provider bindings, and current
authority because those facts are required for safe dispatch. A capability
record cannot manufacture or alter that authority.

Metadata visibility or receipt of a reference does not disclose private bytes,
mount a tool, grant execution authority, or confer expertise. Personas share
record references through ordinary signed `persona_message`; body access still
requires exact visibility/consent policy. There is no dedicated team-skill
catalogue, skill-transfer request/disposition, or conflict-resolution workflow.

The persona may inspect, communicate, share refs, obtain authorized bodies,
acquire or provision tools, verify, author, relate, invoke, or decline material
through ordinary signed actions. The substrate neither chooses one nor decides
that a task requires one. It does not require `synthesise`, `compose`, `select`,
review, promotion, transfer, or conflict resolution before accepting an
otherwise valid opaque authored record. A
successful invocation records exact provider, descriptor, arguments or their
authorized binding, terminal result, effects, and artifact provenance; it does
not become a quality or competence score.

## 6. Practice, learning, and brain evolution

The runtime may retain exact signed practice facts already produced by actions:
who acted, under which authority, what descriptor was used, what terminal
result occurred, which bytes changed, and which records were cited. These are
facts, not automatic competence credit.

Each sealed ordinary turn may contribute a signed `brain-episode/1` effect
receipt. A later authorized wake exposes those episodes through the bounded
learning-history carrier, and the persona can continue the same exact inventory
through `inspect_persona_learning_history`. Recording or exposing an episode
does not itself change a brain fragment or schedule reflection.

A persona may use those facts to author opaque reusable material or an
experience statement through `author_persona_knowledge`. Changed
characteristics or public identity evolution use their separate exact identity
action. The persona may also decide that no durable change is warranted. There
is no substrate experience taxonomy, profession ladder, habit-strength formula,
promotion threshold, optimizer, identity-expression score, or mandatory
reflection schedule.

Mutable brain-fragment evolution uses one
`brain-evolution-decision/1` persona-authored claim. It binds exact `id`,
`persona_id`, open `operations`, `operation_hashes`, `evidence_refs`,
`source_fragment_refs`, `situation_hash`, `environment_id`, `task_id`,
`authority_scope`, open `decision_payload`, `decision_hash`,
`owner_signing_key_id`, `owner_signature`, and `created_at`. Exact preimages
provide mechanical integrity. The substrate requires no semantic operation
vocabulary and does not interpret the payload as review, synthesis,
composition, or promotion.

`brain-evolution-application/1` is only the mechanical application receipt. It
binds exact `id`, `persona_id`, `decision_id`, `decision_hash`,
`operation_hashes`, `changed_fragment_ids`, `rollback_fragments`,
`resulting_fragments`, `authority_scope`, `environment_id`, `task_id`,
`applied_at`, and `application_hash`. Each rollback entry carries the exact
prior fragment payload or an explicit absent marker, together with the relevant
preimage/operation hash. It does not author meaning or judge the change. These two
schemas apply to mutable brain-fragment evolution; they are not a universal
wrapper imposed on every memory, lesson, skill, or other durable write path.

Inherited material supplied to a newborn is a bounded exact signed inventory or
set of exact refs/access grants. The newborn retains independent authorship and
may inspect, obtain authorized bodies, cite, author another record, or ignore
it. Parent evidence does not assign a role or make the newborn an expert.

## 7. Self-context and model carriers

Model carriers contain bounded exact verified situation facts and the exact
record identities or bodies that the persona explicitly navigated to under
current authority. Mechanical compaction preserves identities, provenance,
pagination/truncation facts, and the ability to request omitted bodies.

The whole-prompt `personaos-prompt-source-manifest/1` declares exact source
total, returned count, cursor/next cursor, omitted count/hash, and completeness.
Per-source projections retain exact record/page totals, hashes, cursors, and
omission/truncation counts. No memory, skill, knowledge, or capability source
receives semantic priority or a larger allocation because of its label or body.

The host does not assemble a hidden five-layer prompt, rewrite the persona's
principles, optimize instructions against a score, select demonstrations, or
inject a task-specific capability recommendation. Provider framing required for
wire safety and action schemas remains distinguishable from persona-authored
content and carries no semantic workflow.

A provider response may propose new authored records only through the same
ordinary signed actions as any other change. Free text in a response does not
silently mutate memory, skills, identity, or future prompts.

## 8. Capability-gap meaning is optional and opaque

A persona may describe a perceived capability gap inside one generic opaque
knowledge record, cite it from another record/message, revise its own view by
authoring another record, or never express one. There is no dedicated gap
appraisal, navigation, revision, resolution, notice, active-state, or lifecycle
action. The substrate does not derive a gap from a task, memory, inventory,
filename, tool outcome, prompt, or domain reference.

Gap-like content does not narrow an inventory, rank candidates, require
sharing, select a teacher/tool, gate work or completion, or schedule a wake. A
note, memory, or later knowledge record cannot mechanically open or close a gap
merely by mentioning it.

## 9. Privacy and public discovery

Public discovery may expose only exact metadata whose owner and policy authorize
public visibility. It never publishes private memory or sealed knowledge bodies.
Discovery carriers preserve author, subject, policy, content hash, expiry,
signature chain, and current revocation status.

Remote or internet material is untrusted input until an authorized persona
chooses to inspect or acquire it and exact provenance is retained. Source hosts,
URLs, package managers, commands, libraries, professions, and search queries are
open persona choices rather than kernel vocabulary.

## 10. Plural domain references

Every eligible record may bind zero, one, or many exact signed `domain_refs`.
The set is unranked and has no primary member. References supply navigable
context only; they do not assign a profession, import a prompt, select memories,
grant a capability, choose a tool, or determine task completion.

## 11. Replay and conflict

Replay reconstructs immutable records, visibility, revocation, and explicit
supersession lineage. Concurrent authored records are preserved unless exact
policy authority rejects one. The substrate does not semantically merge prose,
choose a winning belief, or collapse divergent persona views into a synthetic
consensus.

Content-addressed bodies may be deduplicated mechanically without merging their
distinct authorship, consent, scope, or causal references.

## 12. Removed compatibility surface

There is no compatibility path for fixed memory tiers, nightly consolidation,
importance decay, unified provenance scores, hierarchical retrieval ranking,
stage-aware weights, top-K selection, prompt-layer assembly, required
skill-synthesis/skill-composition shapes, parent-skill gates, semantic
proposal/review/promotion lifecycles, GEPA/MIPRO-style host optimization,
mutation-operator catalogues, tactic promotion gates, identity-expression
scores, team-skill catalogues, skill-transfer/conflict ceremonies, dedicated
capability-gap workflows, habit-strength reducers, or automatic memory-to-prompt injection.
Historical records using those schemas may remain opaque bytes but confer no
current selection or behavior authority.

## 13. Design criteria

1. Inventories are exact, complete within explicit pagination bounds, and
   unranked.
2. Personas—not the substrate—navigate, interpret, acquire, transfer, and use
   knowledge, memories, skills, and tools.
3. Receipts preserve facts and provenance without awarding relevance, quality,
   competence, or expertise.
4. Generic knowledge/capability authorship creates one opaque signed
   `personaos-persona-state-record/1`; no semantic synthesis, composition,
   review, transfer, conflict, or promotion ceremony is required.
5. Memory and skill privacy follow exact consent and policy authority.
6. Domain references are plural, optional, and non-semantic to the kernel.
