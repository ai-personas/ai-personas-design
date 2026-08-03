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
persona-owned record per invocation. The persona supplies:

- required `metadata`, an arbitrary canonical JSON object;
- any additional open persona-authored JSON fields it chooses; and
- optional `refs`, a bounded set of distinct exact record-reference strings.

The same action may carry `publish_for_peer_acquisition: true` and one exact
`publication_rationale`. This is the persona's explicit choice to publish the
record being authored, not a host default. The resulting publication binds the
same authenticated action, exact signed state record, body hash, byte count,
scope, and rationale. Omitting the flag retains the record without publishing
it. No content field, task text, domain, role, filename, or available peer can
turn the flag on or choose a recipient.

`metadata` and every additional open persona-authored field are retained
verbatim as one opaque `content` object. Transport-owned authority fields,
optional public scope bindings, and `refs` are not copied into that body. The
current mechanical storage envelope permits at most 262,144 canonical JSON
bytes and nesting depth 64 for the resulting `content`. `refs` accepts one exact
string or at most 32 distinct exact strings, each at most 500 UTF-8 bytes. These
are content-neutral allocation/integrity bounds, not knowledge kinds or
behavior selectors.

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

Authoring the record is also the persona's explicit decision to retain it for
later cognition. Every verified same-environment `persona_knowledge` record
therefore joins the owner's ordinary Layer-4 candidate inventory on later
turns. That inventory is content-address ordered, unranked, and mechanically
count/byte bounded; records outside the current page remain exact and
cursor-addressable. This does not make the record true, relevant, active as a
tactic, or evidence of competence. Persona-authored brain fragments and their
exact bindings remain a separate mechanism for active tactics.

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

An ordinary wake also carries a bounded, hash-bound append frontier for the
sealed turn-effect lane. The frontier is a fixed suffix by authoritative append
position, not a relevance result: it exposes exact episode identities, action
invocation identities and occurrence counts, terminal effect hashes, and
workspace byte deltas while binding every compact projection to the signed raw
episode. Repeated authoritative invocations may be represented by one invocation
row plus exact occurrence positions and source hashes. Repeated transport
wrappers around one backend observation are first coalesced by exact mechanical
observation identity and do not increase occurrence count or practice evidence.
The raw history page preserves authoritative source cardinality. The frontier declares its
source total, included range, omitted prefix, and full-manifest hash. This
causal-tip view is additional to the complete cursor-navigable inventory and
does not replace it.

Large exact observations are stored once as canonical content-addressed bytes.
Subsequent signed events carry the exact hash, byte length, encoding, and
verified content reference rather than embedding the observation again.
Inline-versus-referenced storage is chosen only by a fixed byte bound. Ambient
routing carries a signed reference to the source lineage event, not another
copy of its payload. Authorized inspection may materialize the exact referenced
bytes lazily and must reverify the hash and length. Field names, task meaning,
media type, profession, tool identity, and outcome do not affect this storage
decision.

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

A fixed append-position frontier of signed effect receipts is not a recency
weight or selected active subset. It is a current log boundary: every retained
position remains in the complete inventory, the suffix rule is invariant to
record content, and no record receives inferred importance or behavioral
authority.

## 3. Persona navigation

The persona chooses how to navigate from the exact inventories available in an
ordinary wake. It may request a body by exact reference, issue an authorized
search or external query, follow provenance, inspect a peer's public metadata,
ask another persona, send or receive an exact record reference, obtain a body
under current access/consent authority, author another opaque record citing it,
invoke an authorized tool, or ignore the material.

Catalogue presence, persona-authored retention, exact carrier binding,
capability provisioning, tool acquisition, tool invocation, observed practice,
and artifact effects remain separate evidence stages. None implies any other,
and none independently certifies expertise. Over time a persona can build an
evidence chain across those stages through its own signed choices and repeated
work. The substrate exposes that chain without assigning a curriculum,
profession, level, utility score, or next action.

These choices may occur in any order and may be interleaved with ordinary task,
identity, population, communication, artifact, and workspace actions. The
kernel supplies no fixed exploration phase, retrieval stage, gap-first rule,
teacher choice, action sequence, or definition of enough knowledge.

An action receipt proves that the exact action occurred and records its effects.
It does not prove that the chosen material was relevant or that the persona
learned from it. One cryptographically verified receipt identity contributes
one action occurrence even when a provider carries that same receipt through
several nested wrappers or cumulative observations. The capture surface reports
those redundant sightings separately, but they do not become additional
practice. Distinct verified receipt identities remain distinct regardless of
equal action names, arguments, result bytes, paths, or task meaning.

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
requires exact visibility/consent policy. A persona may separately sign an
exact publication or withdrawal decision for one body it owns. That generic
decision binds the source identity, canonical body hash and size, environment,
task provenance, rationale, and authenticated action. It neither creates a
semantic skill type nor publishes any other private material. There is no team-
skill catalogue, teacher selection, skill-transfer request/disposition, or
conflict-resolution workflow.

On the global peer plane, a verified public persona-state record may therefore
appear as `knowledge` metadata alongside executable `tool` metadata. The public
metadata preserves the exact record/author/scope identities, body commitment,
byte and evidence-reference facts, time, signing material, access authority,
and any current author-signed publication decision. The catalogue does not
inline the body or accept an arbitrary body locator. When both author
publication and public-read authority are current, a protocol-derived route may
serve a provider-signed envelope containing those exact bytes. The envelope
binds the provider kernel, discovery record, author publication, body hash, and
body size. A receiving persona explicitly chooses one exact record and expected
hashes, fetches it from that record's signed peer base rather than a rendezvous
fallback, and independently verifies both signatures and all bindings before
retention. The substrate does not inspect the body to label it a skill, match it
to a task, or prefer its author.

A node expands its own current-master-signed compact provider index through the
same provider/document/policy verification used for received P2P envelopes and
merges the exact verified rows into the unranked catalogue. Consequently a
co-resident persona can discover an explicitly published record immediately;
publication does not depend on the bytes first leaving the node and returning
through loopback gossip. Remote and local rows have identical acquisition
authority and are deduplicated only by exact record bytes.

A verified executable-tool body may carry its exact portable setup, build,
implementation, interpreter, environment, schema, declared effects, and
verification recipe. Acquisition reruns those opaque steps and mounts nothing
unless provisioning, smoke execution, and every author-declared verification
command succeed. A verified opaque state body is retained without automatic
application. Later cognition receives a small exact acquisition inventory and
may open any retained body by exact id, JSON pointer, and byte window. Catalogue
presence, body publication, acquisition, provisioning, mounting, invocation,
practice, authored learning, brain evolution, and expertise claims therefore
remain distinct evidence states.

The capability plane is source-plural. Exact local execution inventory,
persona-published peer bodies, signed registry candidates, and a persona-authored
portable provisioning recipe are independent routes through the same ordinary
action boundary. A recipe's setup/build/source choices may name any reachable
package manager, source host, library, command, or interpreter; those values are
opaque authored bytes, not a kernel catalogue. No particular executable,
profession, file format, provider, or internet source is privileged or required.
Network reachability is an execution fact, not permission to trust fetched
material: the persona still chooses the source and the resulting acquisition
retains exact receipts and verification outcomes.

This surface is universal rather than domain-installed. Changing the principal
intent, workspace contents, persona characteristics, domain references, or
prior artifacts cannot add, remove, reorder, rename, or preselect the generic
inspection, publication, discovery, acquisition, provisioning, verification,
communication, and invocation actions. Only a persona-authored action may put a
particular tool, library, source, peer record, setup command, or method into the
causal history. A tool already present in the exact local inventory may be used
directly; absence of an acquisition receipt in that case is not evidence that
the substrate preferred it.

The zero-inclusive capability-acquisition observation joins both transport
planes without collapsing them: local registry/provision/mount/invocation
counts and verified global publication/acquisition/outcome/body-kind counts are
reported independently from signed lineage. Empty counts remain visible. This
is causal memory, not a deficiency detector, curriculum, recommendation,
domain classifier, or automatic reason to acquire or invoke anything.

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

On an operator-declared public node, all in-scope persona, environment, task,
artifact, workspace, message, telemetry, knowledge, tool, and open-input data is
anonymous read-level data. Public persona-development projections therefore
include every verified in-scope retained knowledge body, not only a recent
action excerpt. A non-public node exposes only metadata and bodies whose exact
owner/policy authority permits that narrower visibility. Discovery carriers
preserve author, subject, policy, content hash, expiry, signature chain, and
current revocation status in either mode. Public read publication never grants
browser write or persona-signing authority.

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
capability-gap workflows, habit-strength reducers, or host-selected automatic
memory-to-prompt injection. Mechanically returning every eligible record to an
unranked owner inventory is continuity of the persona's explicit authoring
decision, not a semantic retrieval policy.
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
