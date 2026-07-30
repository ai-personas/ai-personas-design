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

## 3. Persona navigation and use

During an ordinary wake, a persona may inspect a fragment by exact reference,
cite it, request its body under access authority, author a new or superseding
fragment, transfer it with consent, explicitly bind it to an action/model
carrier, or ignore it.

The exact persona-authored binding—not task words or host retrieval—determines
which fragment bodies may be included in a later carrier. The carrier preserves
fragment identity, content hash, provenance, and truncation facts. Provider
framing does not join fragments into new instructions or impose sections.

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
trace-to-fragment updates.

## 9. Design criteria

1. Fragments are optional opaque persona-authored signed records.
2. Inventories are complete within explicit pagination bounds and unranked.
3. Personas explicitly navigate, bind, transfer, and revise fragments through
   open signed decisions.
4. The host never assembles a behavioral prompt from task semantics.
5. Fragments grant no capability, expertise, continuation, or completion.
