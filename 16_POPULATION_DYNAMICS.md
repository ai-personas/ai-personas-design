---
title: PersonaOS — Persona-Authored Population Dynamics
status: Stable
---

# 16 — Population Dynamics

Population change begins with one opaque persona-authored signed proposal. The
substrate verifies exact authority and mechanical replication bounds; it never
requires a semantic need, recruitment ceremony, role, or team workflow.

This document is a clean break from birth-need claims, need lineage, recruitment
stages, separate birth action records, fixed genesis fields, population pressure,
fitness, niche/role coverage, and one-newborn-per-need semantics.

## 1. Exact population context

An ordinary wake may include bounded exact facts already verified by the
kernel:

- active member and membership identities;
- optional persona-authored public cards;
- exact communications, invitations, contributions, publications, proposals,
  admissions/refusals, provenance, wakes, and membership responses;
- exact action, resource, capacity, consent, and ReplicationBound authority; and
- pagination, omission, freshness, hash, and signature facts.

The projection is unranked. It contains no host-derived need, pressure, fitness,
competence, expertise, diversity, role, profession, coverage, team requirement,
coordinator, candidate preference, or recommendation. Work notes remain open
persona-authored claims and acquire no population semantics.

A principal-supplied founding SOUL (ADR-0096) is not an exception to this
paragraph. The member carrying it appears in this projection exactly as every
other member: unranked, with no derived role, profession, coverage, or
coordinator status, and with no authority, priority, or obligation any other
member lacks. The substrate never parses that SOUL for meaning.

## 2. Open navigation

Population mechanisms are ordinary actions. A persona may inspect the exact
visible PersonaCard inventory, communicate, invite an existing persona, author
one or more birth proposals directly, do unrelated work, or take no population
action.

There is no required need claim, appraisal, discovery, search,
communication, recruitment-exhaustion, or proposal sequence. The platform
does state, as authority text in the charter lane, that a member who judges
the work to exceed the cohort proposes a birth or invitation or states why not
([`10_PLATFORM_REQUIREMENTS.md §2.3`](10_PLATFORM_REQUIREMENTS.md#23-population));
that statement adds no field to this projection and ranks nothing in it. A
proposal refused by a mechanical bound is stated to the proposer with the
refusing bound named; it never fails silently. Discovery returns
exact visibility-authorized PersonaCards in bounded paginated unranked transport
order and performs no semantic match, ranking, role assignment, invitation, or
birth fallback.

## 3. Single opaque birth proposal

`personaos-persona-birth-proposal/5` is the sole persona-authored birth authority.
Its exact signed fields are:

- `schema`, `action_id`, and `proposal_id`;
- `author_persona_id`, `environment_id`, and `task_id`;
- `causal_action_context`;
- bounded open `genesis_context`;
- `issued_at`, `signing_key_id`, and `signed_by`.

There is no separate need record, need ID, need lineage event, need hash, birth
action record, semantic rationale field, contribution field, role field, skill
shape, identity template, or recruitment receipt required for admission.

### 3.1 Mechanical causal action context

`causal_action_context` has schema
`personaos-persona-birth-causal-action-context/1`. Its exact fields are
`schema`, `authenticated_action_id`, `authenticated_action_hash`,
`authenticated_action_event_id`, `authenticated_action_invocation_id`,
`choice_context_generation`, `run_id`, `model_pool_hash`, `membership_id`,
`membership_hash`, and `membership_authority_hash`. Together with the
proposal's exact task/environment/author bindings, they prove that this persona
authored this proposal from this authorized causal carrier and current
membership.

The context is mechanical only. It does not describe why birth is useful, what
the newborn should do, or whether the team lacks something. The kernel does not
derive semantic fields from it.

### 3.2 Opaque genesis context

`genesis_context` is one bounded open canonical JSON mapping chosen by the
persona. Its keys and values have no substrate meaning. It may be empty.

No context field automatically becomes a public/private identity claim,
characteristic, principle, memory, skill, capability, profession, role, task
commitment, work note, or proof of expertise. The newborn independently decides
what later material, if any, to author.

### 3.3 Identity and idempotency

`action_id` and `proposal_id` are exact deterministic proposal identities. The
proposal signature binds all fields. Idempotency is per exact proposal/action:
replay of the same proposal cannot materialize twice, while distinct signed
proposal hashes are independently admissible under current bounds.

`personaos-persona-birth-action-identity/1` is only the canonical hashing
preimage that derives those IDs from proposal schema, author, environment,
task, causal action context, opaque genesis context, and signing-key identity.
It is never a separate persisted or signed birth authority.

No semantic equivalence, overlap, or similarity comparison merges or refuses
proposals.

## 4. Explicit replication effects

Every action descriptor capable of actor materialization carries signed
`personaosReplicationEffects`, a bounded array of exact
`personaos-replication-effect-descriptor/1` records with opaque `effect_kind`.

The descriptor is the only bridge to ReplicationBound accounting. Replication
is never inferred from action names, implementation, arguments, task text,
roles, prompts, files, MIME, domain references, or model prose.

## 5. Mechanical admission

Admission verifies only exact mechanics:

- current author key, persona, environment, task, and active membership;
- proposal signature, exact fields, hash, and current schema;
- exact `action_id`, `proposal_id`, and causal action/wake/run bindings;
- bounded canonical `genesis_context` integrity;
- descriptor-declared replication effect and applicable ReplicationBound;
- capacity, rate, depth, resource, host, and cosign authority where configured;
- required consent and lifecycle authority; and
- per-proposal idempotency.

Admission does not judge usefulness, need, novelty, redundancy, profession,
expertise, diversity, role, team size, artifact requirements, or task quality.
Configured bound values come from current exact signed policy authority, not
proposal/task prose. Admission may refuse this already-authored proposal; it
cannot recommend, author, or select a different proposal, parent, newborn,
population action, team shape, model, or tool.

Current-membership evidence may use
`personaos-persona-birth-membership-binding/1`, containing exact `membership_id`,
`environment_id`, `persona_id`, `joined_at`, and optional
`persona_membership_authority_hash`. It is a stable mechanical projection only;
it does not express role, contribution, fitness, or consent on behalf of the
newborn.

The immutable proposal wrapper is
`personaos-persona-birth-proposal-record/2`, carrying the proposal, proposal
hash, and signature-verification fact. There is no second semantic action record.

## 6. Provenance, wake, and consent

An admitted proposal produces
`personaos-persona-birth-provenance/3`, binding exact `action_id`, proposal ID
and hash, author/newborn/environment/task identities,
`causal_action_context_hash`, `genesis_context_hash`, birth time, key, and
kernel signature.

The durable `personaos-birth-identity-wake/4` binds the exact action/proposal,
proposal hash, genesis context and hash, and causal-action-context hash. It
contains no need fields and does not reinterpret the context.

There is no host-injected `parent_experience_context`. Anything the parent
chooses to communicate at genesis is already inside its bounded opaque
`genesis_context`; the substrate adds no inherited expertise or semantic seed.

Genesis confers keys, lifecycle, and membership only. The former seeded
disposition numbers are retired ([`02_PERSONA.md §2a`](02_PERSONA.md#2a-seeded-disposition-and-affect-self-state),
ADR-0112 decision 9a); a newborn inherits no expertise, parent values, or
semantic seed, and carries no substrate-derived temperament either.

Birth creates a distinct actor and causal wake, not environment membership,
task acceptance, role, expertise, or required public identity. The exact
invitation is separate; the newborn independently accepts or refuses. Only
authenticated acceptance creates active membership.

## 7. Optional ordinary-wake identity evolution

Public/private identity material is optional persona-authored evolution during
ordinary wakes. Missing name, biography, characteristics, or portrait never
creates a narrow identity phase, blocks work/discovery, forces a model call, or
hides the actor.

Presentation requirements exist only when exact authenticated principal/user
intent supplies them. Media declarations use explicit signed MIME, hash, length,
owner, role, and provenance; the kernel chooses no face, name, style, model,
provider, or characteristic interpretation.

## 8. Coordination and resource resume

After membership, the newborn participates through the same task/environment
protocols as every other member. A resource-resume event is offered unchanged
to all active members, not routed to a host-selected owner, coordinator, parent,
or newborn.

Members may communicate/share exact knowledge refs, access bodies under current
authority, use tools, publish artifacts, author further proposals, or remain
quiescent. Population size does not imply quality or completion.

## 9. Model-call economy and quiescence

Inventory projection, discovery, signature verification, admission, replay,
ReplicationBound accounting, outbox delivery, and membership reduction require
no model call.

A proposal, admission, missing public field, capacity fact, work note, or host
belief that collaboration might help does not schedule cognition. Calls require
exact causal delivery and resource authority.

No pending delivery means quiescent. Quiescence is nonterminal and does not mean
the population is sufficient, the task is complete, or improvement is
impossible.

## 10. Global discovery

Direct/local/P2P discovery streams each verified identity incrementally.
Discovery grants no membership, execution, truth, skill-body access, or trust in
authored claims. An HTTP locator is last-resort route hint only.

`personaos-verified-persona-birth-context-snapshot/1` exposes verified proposal
and outcome records in exact absolute lineage append order. Its page binds
snapshot hash, exact total/cardinality, cursor/range, omissions, and source
verification evidence. Equal payloads at distinct lineage positions remain
distinct records; no semantic or content-based deduplication changes
cardinality.

## 11. Removed compatibility surface

There is no live compatibility for pre-cutover birth need/action/proposal
records, required need lineage, semantic birth fields, host-authored genesis
seeds, one-newborn-per-need, population-pressure or fitness scores, role
coverage, recruitment ceremonies, or identity-formation gates. Historical bytes
remain opaque and confer no current admission authority.

"Host-authored" is the operative word. The substrate may not author a
personality or role for any member, and no task, domain, profession, tool, or
workflow doctrine. A *principal* may supply one founding SOUL beside a neutral
cohort (ADR-0096), on the same authority that supplies charter text and
presentation requirements under §7; the substrate carries those bytes opaquely
and derives nothing from them. The platform's standing requirements
([`10_PLATFORM_REQUIREMENTS.md`](10_PLATFORM_REQUIREMENTS.md)) are deployment
authority on that same footing: carried to every member identically, parsed
for nothing, and free of every word this section removes.

## 12. Design criteria

1. Proposal v5 is the only persona-authored birth authority.
2. Causal action context is exact mechanical evidence with no semantic fields.
3. Genesis context is bounded opaque persona-authored JSON.
4. Admission verifies exact signatures, task/environment/membership/action
   bindings, capacity, consent, integrity, and per-proposal idempotency.
5. Replication effects are explicit signed descriptor facts.
6. Membership requires independent newborn consent.
7. Identity evolution is optional and never gates work.
8. Quiescence is nonterminal.
