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

The fixed append frontier joining signed communications to sealed recipient
turns is likewise causal evidence rather than fragment retrieval or a host
lesson. Exact event/source and parent identifiers establish the join; the host
does not inspect message meaning or infer whether the resulting activity was
useful. A persona may independently retain, revise, or ignore what it learns
from that evidence through its authored fragment and state protocols.

## 3. Persona navigation and use

During an ordinary wake, a persona may inspect a fragment by exact reference,
cite it, request its body under access authority, author a new or superseding
fragment, transfer it with consent, explicitly bind it to an action/model
carrier, or ignore it.

The exact persona-authored binding—not task words or host retrieval—determines
which fragment bodies may be included in a later carrier. The carrier preserves
fragment identity, content hash, provenance, and truncation facts. Provider
framing does not join fragments into new instructions or impose sections.

`brain-fragment-binding/2` is the exact signed current-head decision record. Its fields are
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

Distinct contracts do not require two model/tool round trips. A single
authenticated evolution action may contain an optional, separately shaped
`bind_changed_fragments` decision. When present, it names the complete exact
`carrier_scope_refs`. Before mutating any fragment, the substrate freezes the
exact referenced binding head, or the mechanically current eligible head when
no binding id was supplied. If that verified head has the same exact scope, its
still-valid fragment identities are carried forward in authored order and the
revisions changed by this action are mechanically upserted in operation order.
If the scope differs or no valid head exists, the new complete set begins with
only the changed identities. Duplicate identities collapse by exact id; fragment
bodies, task text, domain values, action names, and claimed utility never
participate.

When `bind_changed_fragments` is absent, the revisions remain catalogued and
unbound. The substrate neither derives this field from an operation body nor
chooses a scope. The result states the prior binding preimage, carried, omitted,
changed, and resulting complete identities, whether binding was requested, and
whether the separate signed binding commit completed. Each successful binding
contains the complete fragment set the persona currently chooses for every
carrier where that exact scope is eligible. A persona uses the separate
`bind_brain_fragments` action when it intends exact replacement or an empty
clear; ordinary cumulative evolution cannot silently erase unchanged retained
material. Existing binding records remain independently inspectable and
revisable.

Fragment authoring follows the same exact-scope rule. Empty and universal scope
are explicit; every other scope must equal one current authenticated carrier
identity. An unavailable scope is refused before storage with the exact current
scope references exposed to the author. It is never stored as a semantic alias
that later compiles silently exclude.

Reusing a binding id creates a signed next revision bound to the complete prior
record. Omitting an id creates another signed head. For one carrier, the
mechanically latest valid eligible head—ordered only by exact authored time,
version, binding id, and binding hash—is the complete current set and supersedes
all older eligible heads. The older bytes remain immutable history and are not
unioned into the prompt. An empty current head is an explicit unbinding. An
ineligible task-scoped head cannot suppress a still-eligible head in another
task. There is no host-defined enable/disable vocabulary, semantic recency
score, or fragment-body inspection in head resolution.

`brain-compile/5` binds both the non-activating catalogue page and the current
`brain-fragment-binding-carrier/3`. A binding is eligible only when its exact
scope is a subset of the current carrier and its owner signature still verifies;
only the mechanically latest eligible signed head participates.
Each claimed fragment reference must byte-match the current signed revision.
Stale, unavailable, over-count, and over-byte records are named in exact
omission evidence. An invalid fragment in the current head is omitted and does
not silently resurrect an older head. Admitted records are ordered only by the
fragment position authored inside the selected binding. They precede the unselected
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

`list_brain_fragment_bindings` exposes the owner's exact hash-bound historical
binding inventory without activating it. Reusing a `binding_id` revises that
record; omitting it authors a new head; an empty newest eligible head clears the
current set. This lets a persona curate a changing repertoire instead of making
every lesson ever bound a permanent simultaneous system instruction. Current-
head resolution is append mechanics, not host relevance, profession, domain,
utility, or fragment-content ranking.

Every successful binding action returns a compact
`personaos-brain-fragment-binding-carrier-effect/1` projection computed from the
same current signed bindings and mechanical carrier bounds used by the next
compile. It names the requested revisions that are present or absent, every
mechanical omission reason, current byte/count pressure, ordering, and the exact
carrier hash. A stored binding therefore cannot be reported ambiguously as if
its body were guaranteed to reach later cognition. This projection ranks and
recommends nothing: only the persona may reuse a binding identity, replace its
fragment set, clear it, retain the omission, or take no action.

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

If the same authenticated action explicitly includes
`bind_changed_fragments`, successful application is followed by the distinct
owner-signed `brain-fragment-binding/2` commit. The binding request and any
same-scope prior head are validated and frozen before fragment mutation. The
commit's complete set is the verified carried-forward identities followed by
the returned `changed_fragment_ids`, with the changed identities resolving to
their new exact revisions. Invalid or stale prior identities are named as
omissions rather than resurrected or guessed. A different scope has no prior
carry-forward authority and commits only the changed identities. A rare
post-application binding-commit failure is reported as a partial commit rather
than pretending that evolution was rolled back. No fragment content, task text,
tool identity, or domain value affects this mechanical join.

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
`active-agent-spec/1`, semantic `brain-compile/1`, unsigned
`brain-compile/3`, accumulated-head `brain-compile/4`,
`brain-fragment-binding/1`, `brain-fragment-binding-carrier/2`, selected-fragment prompts,
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
   a permanently empty host-selected compile. Every compiled carrier states
   the current binding state as mechanical fact: the admitted binding's exact
   identities and counts when one is admitted, and the exact omission fact
   when zero fragments are bound — the mechanical cause of the empty state and
   the replay rule and position an eligible signed head would receive. The
   statement is nouns only; it recommends, requests, ranks, and schedules
   nothing.
7. Authored, catalogued, bound, provisioned, acquired, invoked, practiced, and
   effect-producing are distinct evidence states; the substrate infers neither
   expertise nor a curriculum from them.
8. A persona can explicitly author and bind newly changed fragments in one
   authenticated action without the substrate selecting content or scope. An
   unchanged exact scope carries its valid prior selection forward and upserts
   changed revisions; a changed scope begins with changed revisions only; an
   omitted binding request remains catalogue-only; and explicit replacement or
   clearing remains a separate persona-authored binding decision.
