---
title: PersonaOS — Persona-Owned Brain Fragments
status: Proposed
---

# 20 — Persona-Owned Brain Fragments

A brain fragment is optional persona-authored reusable material. The substrate
stores, verifies, inventories, and transports fragments; it does not retrieve,
rank, activate, compile, review, promote, or rewrite them based on task meaning.

This addendum is a clean break from semantic BrainCompile, active-agent specs,
utility counters, activation-cue matching, diversity selection, fixed edit
lifecycles, and host-assembled prompt programs.

## 1. Exact opaque fragment record

`brain-fragment/1` is one persona-owned signed record. Its substrate-visible
contract is mechanical: stable identity, owner persona, version and explicit
supersession/preimage lineage, visibility/consent and authority scope, bounded
open body and metadata, author-selected exact references, zero or more unranked
`domain_refs`, hashes/byte bounds/times, signing-key identity, and signature.

The body and metadata are opaque. There is no required fragment kind, label,
activation/deactivation cue, abstraction level, summary, keyword, embedding,
status vocabulary, affordance class, or semantic link type. A persona may write
those ideas inside its open material, but the substrate neither interprets nor
acts on them.

The substrate validates bytes, authority, references, access, consent, exact
preimages, and lineage. It does not interpret the body as an instruction,
decide when it applies, measure utility, or claim that it changed behavior.

## 2. Exact unranked inventory

Every authorized persona view exposes a bounded paginated complete inventory of
visible fragment identities and exact metadata. Pages bind snapshot/hash,
observed count, cursor, and explicit truncation.

Ordering is stable mechanical transport order only. There is no semantic
retrieval, embedding similarity, relevance score, helped/hurt count, recency
weight, hot set, graph expansion, diversity selector, top-K, recommendation, or
host-selected active subset.

The fixed append frontier for sealed turn-effect receipts is a separate causal
log projection, not fragment retrieval. It does not bind, activate, rank, or
select any brain fragment.

## 3. Persona navigation and use

During an ordinary wake, a persona may inspect a fragment by exact reference,
cite it, request its body under access authority, author a new or superseding
fragment, transfer it with consent, explicitly bind it to an action/model
carrier, or ignore it.

The exact persona-authored binding—not task words or host retrieval—determines
which fragment bodies may be included in a later carrier. The carrier preserves
fragment identity, content hash, provenance, and truncation facts. Provider
framing does not join fragments into new instructions or impose sections.

`brain-fragment-binding/1` is the exact signed decision record. Its fields are
`id`, `persona_id`, `version`, exact `fragment_refs`, exact
`carrier_scope_refs`, `evidence_refs`, bounded open `binding_payload`,
`prior_hash`, `binding_hash`, `owner_signing_key_id`, `owner_signature`,
`created_at`, and `updated_at`. Every fragment reference binds the current
fragment id, content hash, version, signing key, and signature. Every carrier
scope reference must be an exact identity already present in the authenticated
current persona/environment/task/cohort carrier, and the owner persona identity
must be among them. The host does not infer scope from body text.

Fragment authoring and fragment binding have distinct closed mechanical
contracts. `authority_scope` belongs only to the authored fragment revision;
`carrier_scope_refs` is the complete binding scope, must include the exact owner
persona reference, and accepts no parallel `authority_scope` field. A tool
surface that ambiguously accepts both is invalid even if the kernel later
refuses the extra field.

Fragment authoring follows the same exact-scope rule. Empty and universal scope
are explicit; every other scope must equal one current authenticated carrier
identity. An unavailable scope is refused before storage with the exact current
scope references exposed to the author. It is never stored as a semantic alias
that later compiles silently exclude.

Reusing a binding id creates a signed next revision bound to the complete prior
record. The new exact fragment set replaces the old set; an empty set is an
explicit unbinding. There is no host-defined enable/disable vocabulary.

`brain-compile/4` binds both the non-activating catalogue page and the current
`brain-fragment-binding-carrier/2`. A binding participates only when its exact
scope is a subset of the current carrier and its owner signature still verifies.
Each claimed fragment reference must byte-match the current signed revision.
Stale, unavailable, over-count, and over-byte records are named in exact
omission evidence. Admitted records are ordered only by binding identity and
the fragment position authored inside that binding. They precede the unselected
inventory because that precedence is the persona's signed selection, not a host
relevance judgment.

The kernel signs the exact compile before the model turn. Prompt admission
still verifies every selected binding and fragment against current storage.
After admission, that immutable signature lets the turn-effect receipt preserve
what the turn actually saw even if the same turn authors a newer fragment or
binding revision before effect capture. Recomputing the pre-turn carrier from
post-turn state, and thereby erasing causal learning evidence whenever learning
occurs, is forbidden.

A selected carrier retains two hash-bound representations. Its audit record
carries the exact binding and fragment references, signatures and hashes, the
complete authored fragment body, and all binding/fragment material. Its prompt
record is a deterministic field projection of that audit record: it carries the
exact source-record hash, binding/fragment ids, hashes and versions, complete
opaque authored body and metadata, scope, evidence and source references, and
the open binding payload, while omitting duplicated public signatures. The
kernel-signed compile binds both record lists and the runtime rejects any prompt
projection that cannot be reproduced byte-for-byte from its full signed source.
The carrier byte window measures the material actually rendered to the model;
otherwise repeated audit signatures can crowd later learning out without adding
usable knowledge. Repeated bindings of the same exact fragment revision collapse
mechanically to one visible projection, with every duplicate represented in
exact omission evidence. The smaller generic per-record cap for unselected
inventory entries does not apply to a selected record. A selected prompt record
that exceeds the total carrier bound is omitted explicitly while its omission
continues to name the exact full source record.

`list_brain_fragment_bindings` exposes the owner's exact hash-bound binding
inventory without activating it. Reusing a `binding_id` replaces its signed
fragment set; an empty set clears that exact binding. This lets a persona curate
a growing active repertoire instead of allowing old duplicate bindings to crowd
newer experience out of a finite carrier. Revision and clearing remain explicit
persona choices, not host relevance, recency, profession, or domain rules.

Using a fragment does not automatically prove influence, learning, competence,
quality, or completion. Exact citations establish only that the persona chose
to bind the record.

## 4. Persona-authored evolution decision

An owned fragment change is authorized by one signed
`brain-evolution-decision/1`. Its exact fields are `id`, `persona_id`, open
`operations`, `operation_hashes`, `evidence_refs`, `source_fragment_refs`,
`situation_hash`, `environment_id`, `task_id`, `authority_scope`, bounded open
`decision_payload`, `decision_hash`, `owner_signing_key_id`, `owner_signature`,
and `created_at`.

Operation bodies are open persona-authored data apart from exact mechanical
preimage bindings needed to prevent stale or unauthorized mutation. The
substrate defines no required create/supersede/split/merge/review/synthesize/
compose/promote vocabulary and no semantic fields within `decision_payload`.
One valid decision is admitted directly; there is no preliminary proposal,
review, disposition, or promotion record.

Within each open operation, `fragment_id` is the sole reserved caller-visible
storage key. Omitting it allocates a new stable identity; supplying an existing
identity replaces that fragment with a new exact version bound to its current
preimage. All remaining authored keys and values become the complete opaque
body unchanged. The substrate does not merge fields, parse an operation word,
interpret a tombstone, or infer links. A decision may revise a given identity at
most once so every operation binds one unambiguous preimage.

Applying the exact decision produces `brain-evolution-application/1`, a
mechanical receipt with exact `id`, `persona_id`, `decision_id`,
`decision_hash`, `operation_hashes`, `changed_fragment_ids`,
`rollback_fragments`, `resulting_fragments`, `authority_scope`,
`environment_id`, `task_id`, `applied_at`, and `application_hash`. The receipt
makes no authored claim and does not judge the edit. Every rollback entry
contains the exact prior fragment payload or an explicit absent marker plus its
exact preimage/operation hash, so reversal evidence does not rely on semantic
reconstruction.

There is no evidence threshold, rollback score, operational-change rubric, or
automatic edit at feedback, failure, tool, artifact, pause, or budget
boundaries. Historical signed revisions remain auditable under retention and
consent policy. Supersession never rewrites prior bytes.

## 5. Tools, skills, memories, and domains

Fragments may cite exact affordance, skill, memory, knowledge, artifact, peer,
or `domain_refs`. References are navigable context only. They do not mount a
tool, disclose a private body, grant access, derive gap state, select a teacher,
assign a role, or change another action schema.

Only current exact action descriptors and authority determine which tools are
available. Fragment prose cannot claim or manufacture a capability.

## 6. Empty by default

A new persona has no runtime-authored fragments. Birth `genesis_context`, task
intent, tool traces, messages, and receipts remain separate exact evidence and
do not become fragments automatically.

The repository and runtime provide schemas, storage, inventories, and ordinary
actions only. They ship no default domain/task/tool/team fragment library,
prompt sections, activation cues, labels, roles, workflows, semantic operation
catalogue, or behavioral content.

## 7. Causality and completion

A fragment, edit, missing fragment, citation, or host belief that learning would
help does not schedule cognition. Later work requires an authentic causal
delivery and resource authority.

Fragments and their use do not complete objectives, change work-note semantics,
gate capability, or establish expertise. Quiescence remains nonterminal.

## 8. Removed compatibility surface

There is no live compatibility for `situation-capsule/1`,
`active-agent-spec/1`, semantic `brain-compile/1`, selected-fragment prompts,
activation/deactivation cue matching, utility/recency/diversity scoring,
fixed mutation operators, BrainReview/BrainPromotion gates, or automatic
trace-to-fragment updates. Deprecated semantic brain-context/note actions, raw
episode injection, and K-line injection are not present in the persona-visible
registry or prompt path; exact histories remain navigable through their neutral
inventories.

## 9. Design criteria

1. Fragments are optional opaque persona-authored signed records.
2. Inventories are complete within explicit pagination bounds and unranked.
3. Personas explicitly navigate, bind, transfer, and revise fragments through
   open signed decisions.
4. The host never assembles a behavioral prompt from task semantics.
5. Fragments grant no capability, expertise, continuation, or completion.
6. A signed exact binding is replayed into later matching carriers, or its exact
   mechanical omission is visible; authored knowledge cannot disappear behind
   a permanently empty host-selected compile.
7. Authored, catalogued, bound, provisioned, acquired, invoked, practiced, and
   effect-producing are distinct evidence states; the substrate infers neither
   expertise nor a curriculum from them.
