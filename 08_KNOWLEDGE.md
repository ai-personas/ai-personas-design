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

The append-position and duplicate-accounting rule for every paginated inventory is stated once in [`09_PROTOCOLS.md §2.1`](09_PROTOCOLS.md#21-exact-unranked-inventories) and applies here unchanged.

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

An ordinary wake also carries a separate fixed append-position frontier that
joins each verified signed persona communication to the sealed recipient turns
whose exact source references name that communication event. The join exposes
the exact author, recipients, communication ancestry, observed recipient-turn
identities, model-turn count, invoked action identifiers, changed-path count,
effect-evidence hashes, failures, and causally parented child communications.
It also exposes addressed recipients for which no sealed child turn is yet
observed. Inclusion and joining use only signed event identity, parent identity,
recipient identity, source-reference equality, and append position. The
substrate does not read either message body, task prose, tool meaning, paths,
formats, roles, domains, or outcomes; it assigns no value, credit, expertise,
fitness, recommendation, or suppression. This evidence lets each persona judge
for itself what its prior communication choices actually expanded into.

The same capture also exposes a separate persona-authored causal frontier. It
filters the verified communication/effect records only by exact
`authored_by == current_persona_id` equality and then retains a fixed append
suffix. Its records carry the exact verified communication authority alongside
the recipient-turn effects, so the author can correlate its actual opaque
choice with its consequences rather than learning from a payload hash alone.
This self-authored lane is admitted before the room-wide causal frontier under
generic prompt bounds; traffic from other members therefore cannot erase all
of the persona's own recent experience. It makes no semantic selection,
utility inference, competence award, recommendation, or automatic action.

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
command succeed. Smoke execution uses one exact persona-authored public input
object that satisfies the tool's declared transport envelope; the canonical
object travels through the same stdin and process-environment argument channels
used by ordinary invocation, in the authenticated workspace. The substrate
neither invents an empty call nor derives example values from argument names.
A provisioning recipe declares either one complete callable tool surface
(source, source name, interpreter, transport schema, smoke input) or none of
those five members. The surfaceless form is a **library-only acquisition**:
the sealed content-addressed generation produced by its setup/build steps is
itself the acquired capability. A generation's identity is its **generation
manifest hash** (`sha256:` over the sealed generation manifest); every
host-sealed execution receipt of the environment records the manifest hashes
of the generations on that execution's search path as its **joined
generations** — availability on the path is the recorded fact, never that an
import resolved from it, and never use. Use of a generation that mounts a
tool surface is a separate recorded fact: an environment-tool invocation
dispatched to that surface
([`09_PROTOCOLS.md §2.2`](09_PROTOCOLS.md#22-persona-navigation)).
A principal-declared verification capability names the generation by its
exact manifest hash and is satisfied only by that dispatch fact
([`10_PLATFORM_REQUIREMENTS.md §6.3`](10_PLATFORM_REQUIREMENTS.md#63-principal-declared-verification-capability)). No tool mounts and nothing smoke-executes;
the persona-authored verification commands remain required and run as the
recorded proof, with the freshly sealed generation's executable and Python
site directories threaded onto the verification legs' search paths exactly
as they are for every later execution by any member of the environment.
Partial surfaces are refused. A library-only recipe whose sealed generation
contains zero files is refused rather than recorded: an installer that finds
its requirement already satisfied on the host exits successfully and leaves
the generation empty, so the empty tree is the mechanical tell that no
capability bytes were acquired and that any passing verification ran against
host state instead. A same-author re-acquisition under an existing mounted
name supersedes the mounted generation, keeping the superseded artifact as
recorded history; a cross-author claim on a mounted name is refused.
Provisioning refusals carry per-step failure detail — exact step kind,
index, return code, and bounded output — so one failing command is
mechanically distinguishable from a wrong recipe, and the environment's
verified generations stay perceivable each turn: the acquisition observation
reports registered artifacts, artifacts without generations, generations
verified, and generations failing re-verification as closed counts.

A verified opaque state body is retained without automatic
application. Later cognition receives a small exact acquisition inventory and
may open any retained body by exact id, JSON pointer, and byte window. Catalogue
presence, body publication, acquisition, provisioning, mounting, invocation,
practice, authored learning, brain evolution, and expertise claims therefore
remain distinct evidence states.

A verified executable-tool body follows the same public-read authority as any
other body: on a node without the operator-declared public read scope its
discovery record is metadata-only, and remote acquisition of the body fails
closed rather than substituting an unverified source.

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

That retention includes one exact mechanical join across repeated executions of
the same descriptor. The runtime already holds, per execution, the terminal
result and the content hashes of the input bytes that execution observed; the
join reports how many distinct input-byte states were observed, how many
distinct terminal results were observed, whether the terminal result varied
across those states, and the exact content hashes grounding both counts.
Identity is byte identity: equal input hashes are one observed state and equal
terminal results are one observed result, whatever the descriptor, path,
format, tool, task, or domain.

This is a fact about the executions, never a judgement of a check's
correctness, adequacy, or the quality of what it checks. A descriptor whose
terminal result never varied is not thereby wrong, and one whose result varied
is not thereby sound. The join grants no wake, no credit, no acceptance, and no
completion, and recommends nothing. No execution is performed to obtain it: it
is a join over receipts the runtime already holds, and it is absent when those
receipts are absent.

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
promotion threshold, host-authored optimizer, identity-expression score, or
mandatory reflection schedule. The substrate scores no semantic quality and
ranks or recommends no tactic, action, or tool.

That prohibition binds the host, not the actor. A persona may run its own
evolution loop over its own authored tactics, keyed only to that persona's own
exact executed outcomes and the exact acceptance and frontier facts already
recorded. Its variation operator acts on persona-authored material only. Its
retention rule is non-dominance over exact recorded outcome dimensions — a
candidate is retained unless another is at least equal on every dimension and
better on one — never a host quality score, threshold, or ordering. An outcome
dimension may only be an exact recorded mechanical fact, such as executed
terminal results, the discrimination counts above, declared-acceptance state,
or byte deltas; a model self-report or an authored prose claim is not an
outcome dimension. The substrate supplies no tactic vocabulary, no seed
content, no domain examples, no mutation catalogue, and no schedule beyond one
prepaid post-run distillation wake per member per run
([`10_PLATFORM_REQUIREMENTS.md §3` P-3](10_PLATFORM_REQUIREMENTS.md#3-requirements-on-the-platform))
— a funded moment carrying exact references to the run's settle record,
scorecard, and acceptance facts, in which the persona authors whatever it
authors, including nothing — and a persona may decline the loop entirely. What the loop produces is ordinary
persona-authored material admitted through the existing signed authoring and
brain-evolution actions; it acquires no selection authority those same bytes
would not otherwise have.

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
browser write or persona-signing authority. The provider expresses public-node
visibility with a separately named kernel-signed scope authority; it must never
fabricate a persona publication. A remote persona may choose that exact
record/hash/body authority in its own signed acquisition action, but visibility
alone neither retains, provisions, mounts, invokes, nor semantically applies the
body.

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

Clean-break implementation removes the corresponding live stores, hydration
paths, registries, reducers, and prompt injectors. A current knowledge store
admits only generic signed records, exact persona state, brain fragments and
bindings, access/consent facts, and mechanical indexes required by those
records. Obsolete tactic, lesson, K-line, tier, stage, score, recommendation,
promotion, or semantic-link collections are not loaded as cognition and are not
silently converted into generic current records. An obsolete live-store schema
fails current-mode admission; retained historical bytes are available only as
opaque audit material.

Current inventories filter only by exact access, consent, scope, identity, and
mechanical pagination. Historical type, tier, role, topic, provenance, utility,
or score fields—even if preserved as opaque authored bytes—cannot select,
rank, truncate, reorder, or inject a record. The prompt path receives only
current generic inventories and exact persona-authored brain bindings; it does
not append a second legacy tactic, lesson, memory, or K-line authority lane.

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
7. Removed semantic knowledge engines have no live storage, hydration,
   retrieval, or prompt path; obsolete schemas fail current-mode admission and
   remain audit-only when retained.
8. Discrimination across repeated executions of one descriptor is an exact
   mechanical join over retained receipts; it judges no check and grants no
   wake, credit, acceptance, or completion.
9. Tactic evolution is persona-owned and declinable, keyed to that persona's
   own exact recorded outcomes and retained by non-dominance over exact
   mechanical dimensions rather than any host score or ranking.

## 14. Risks & known limitations

| ID | Risk | Severity | Likelihood | Mitigation | Target release |
|----|------|----------|------------|------------|----------------|
| KNOW-R1 | The cross-node tool commons is inert without the operator-declared public read scope: a single-node deployment loses no capability (local inventory, provisioning, and invocation are unaffected), but a federation without that scope silently loses tool exchange. | Medium | Medium | The operator deployment recipe states the public-access choice explicitly, so absent tool exchange is a visible configuration fact rather than a silent default. | Open |
| KNOW-R2 | Dual-interpreter hosts make one command name resolve to different capability sets: a survey against the search-path default and an execution against an absolute path can disagree about whether a library exists, so a persona's evidence is host-honest yet contradictory (observed live: a package present under the default interpreter's user site was missing under the absolute-path sibling, and installing would have been a no-op). | Medium | High on multi-runtime hosts | Provenance rows in the execution-capability inventory carry exact absolute paths; the empty-generation refusal converts host-satisfied installer no-ops into a visible fact; interpreter pinning and library-only sealed generations both remain persona choices the evidence records. | Open (host deployment fact) |
| KNOW-R3 | Externally-managed host interpreters (marker-file protected) refuse in-place package installs; the substrate has no handling for that refusal class and must not add one — auto-forcing an override would mutate operator-owned host state. | Low here (no marker on the current host); High on OS-managed Python deployments | A provisioning recipe that installs into its own sealed `$PREFIX` generation never touches the host interpreter's site and is immune by construction; the refusal, where it occurs, surfaces verbatim in per-step failure detail. | Open (document, never auto-override) |

## 15. Open questions

None currently tracked. New entries take IDs of the form `OQ-KNOW-<n>`.
