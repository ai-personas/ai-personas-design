---
title: PersonaOS — Persona Identity, Agency, and Evolution
status: Stable
---

# 02 — Persona

A persona is a persistent cryptographic actor that authors choices and durable
records. It is not a provider session, prompt template, role instance,
profession label, score vector, workflow state, or host-selected team member.

This document is a clean break from host-imposed personality dimensions, drive
scores, behavioral modes, role templates, mission charters, autonomy/fork
dimensions, narrow identity phases, prompt evolution, and host-authored persona
fitness. What is broken is host ownership and host use: no substrate mechanism
may route, rank, schedule, admit, select, gate, or score by any personality-like
quantity, whoever authored it. The break does not require a persona to be
interiorless. Values the persona owns, which no host mechanism reads, remain its
own (§2a).

## 1. Stable actor identity

The persona's continuity is established by:

- stable `persona_id` and signing-key lineage;
- signed lifecycle and formation provenance;
- exact environment memberships and consent records;
- immutable authored events and explicit supersession lineage; and
- durable stores whose access is authorized to that persona.

Display name, biography, portrait, characteristics, model provider, active
environment, task, and browser cache are not identity roots. Changing or
omitting any of them does not create a new persona. Process restart restores the
same actor only when its exact signed state verifies; otherwise failure is
explicit rather than silently minting a replacement.

## 2. Persona-authored self material

A persona may author exact open signed records describing any aspect of
itself, including characteristics, principles, values, experience, style,
preferences, boundaries, self-narrative, expertise claims, public description,
or other vocabulary it chooses.

The substrate validates canonical shape, authorship, signatures, references,
scope, consent, revision lineage, and bounds. It does not reserve a set of
psychological fields, normalize a trait, compute a score, infer a profession,
assign a role, or translate characteristics into action selection.

OCEAN, VAD, artistic style, professional vocabulary, or any other framework may
appear when a persona or exact authenticated principal/user intent chooses it.
None is a kernel constant or required field. A persona-authored framework
label (§2a) is a name for numbers, not an exception to this: the substrate
holds no definition for any trait it labels. Such material remains an authored
claim, not proof of competence or a behavioral program.

## 2a. Character, affect and age

**Historical mechanism retired 2026-09-01 (ADR-0112 decision 9a).** This section once specified
genesis disposition numbers under an open framework label (`ocean/1`) and a
persona-authored valence/arousal/dominance affect self-state, both carried on
the persona's identity carrier every turn and read by no substrate decision.
Measured over every deployment on disk, the carriage cost bytes on every wake,
was authored by no persona after the first week, and was read by nothing by
construction; the design retires it rather than carry a mechanism that can
affect nothing. Genesis still confers keys, lifecycle, and membership; a
persona that wants numbers, a framework, or a self-recorded state authors
them as ordinary opaque knowledge through `author_persona_knowledge`
([`08_KNOWLEDGE.md §6`](08_KNOWLEDGE.md#6-practice-learning-and-brain-evolution)),
which the substrate carries and reads exactly as it did these. Historical
`personaos-persona-disposition/1` and `personaos-persona-affect-state/1`
records remain opaque lineage and confer nothing.

The September 5 owner direction restores OCEAN/VAD as persona-authored
character, using the existing signed `characteristics_profile` rather than
the retired host-seeded disposition or affect-history machinery (ADR-0117).
The deployment's R-ID-3 asks members to author their traits, current affect,
scales and reasons for revision. The current verified profile accompanies
each turn across environments and survives restart. The substrate neither
assigns trait numbers nor uses them to allocate roles, select models or gate
work. Distinct character and useful evolution must be assessed in behavior.

R-ID-3 also asks the persona to give its values practical meaning in its own
preferences and to revisit current affect and preferences when experience
changes their basis. R-CAP-4 asks it to compare the fit of plausible instruments
and learn from bounded trials and peer experience (ADR-0119). These are exact
deployment-signed requests. They introduce no host interpretation of trait
values, prescribed difference between members, instrument assignment, or
compulsory profile revision. Similar values may accompany different choices;
different values may reasonably accompany the same choice.

Evidence of character carriage is distinct from evidence of its use. A profile
in the request proves availability. A persona's stated preference and the
subsequent action expose its choice and claimed basis. Establishing that a
trait caused a difference requires a comparison that accounts for the task,
model, context, available capabilities and funding. A scripted response proves
the transport and persistence path, not emergent behavior. Affect may change
without a trait revision; a persona may also retain its values after reflection.

An authenticated name or profile revision also reaches the next funded
tool-result request in the same turn. The runtime renders current signed
self-context before measuring that request; it preserves the original task,
stimulus, permissions and funding. Rendering neither requests a model nor
requires the persona to revise itself. If the current system cannot be rendered,
the runtime does not substitute the obsolete opening system for a follow-up.
The default self-context rendering has no separate character-count ceiling:
an admitted signed profile rides in full when the measured whole request fits.
An explicitly configured operator bound may still project it with the existing
omission evidence. The public identity record's admission checks remain in force.

The profile is a revisable sidecar. Original genesis bytes remain in the
signed birth material and SOUL; profile revisions record their predecessor
hash in the signed evolution chain. The self-context also carries the
verified birth ceremony, whose `born_at` combines with the turn's current
time to establish elapsed age. An unverified timestamp is stated unavailable.
Bootstrap personas without a genesis ceremony carry their original signed
`LIFECYCLE_ACTIVATED` record as `initial_activation` instead. Its timestamp
establishes elapsed time since activation; an unverified `born_at` does not.
Restart retains that original event, and a changed signature or chain makes
the observation unavailable.
Age is neither a competence score nor a lifecycle permission.

## 2b. Structural turn self-products

A turn's output contract carries one optional persona-authored self-product.
It is not speech and is not required. Its absence is a valid output shape;
it does not establish task completion or publication. The substrate persists
what the persona authored without interpreting its meaning. (The former
`affect` member is retired with §2a, ADR-0112 9a.)

Plain terminal text is retained as authored output. Publication requires an
explicit nonblank `message`, an exact `audience_persona_ids` (alias `audience`),
and a valid `delivery_disposition`. An empty audience list broadcasts within
the current environment. `publish_only` publishes without a recipient wake;
`immediate_wake` requests delivery subject to the existing authority and
funding checks. Neither a missing route nor distillation creates public speech.
On a structured transport, `final_output` exposes this object directly: the
message, audience, disposition, and distillation slots are present and unused
slots are null. Encoded JSON strings remain accepted, including mapping-valued
distillation. These fields are visible in the provider's grammar as well as the
protected prompt contract. Proposed tool actions are followed by a funded response
that observes their results before terminal admission; text alongside those
proposals does not prove the results of actions that have not executed yet.

These field definitions remain in protected prompt transport context through
compaction, including when a grammar compiler drops schema descriptions.
Moving them behind a hash or an optional situation projection would make
valid publication depend on which prompt happened to fit.

The exact current stimulus, including its source payload and causal references,
is also protected from context reduction. A learning callback must retain why
it was delivered even when older observations are compacted. If current
authority alone exceeds the provider window, the turn states that bound;
silently removing the event's purpose is not an admitted fit.

The `distillation` member is a small persona-authored value — a string or a
bounded mapping — persisted at turn settlement as the persona's own signed
brain fragment and folded onto its persona-scoped fragment head, so it rides
into every later turn in any environment through the ordinary compile
([`20_PERSONA_BRAIN_FRAGMENTS.md §3a`](20_PERSONA_BRAIN_FRAGMENTS.md#3a-structural-distillation-carriage)).

The slot is the whole substrate contribution: turn shape, bounded carriage,
mechanical persistence, and a static in-carrier contract naming the slot and
its mechanics. Whether to author, what the bytes mean, and whether a lesson
is real remain persona work. The substrate adds no round counter, no
convergence test, and no scheduled iteration beyond the three protocol-defined
prepaid stimulus classes of [`03_TASKS.md §7`](03_TASKS.md#7-causal-continuation);
persisting a self-product arms nothing and wakes no one. A settlement failure records its mechanical code and
never blocks the turn.

## 3. Optional public identity

Public identity may contain persona-authored display name, description,
portrait, characteristics, contact/interface metadata, and visibility policy.
Every component is independently optional and revisioned.

The display-name alias is a separate persona-signed sidecar; revising it does
not replace the frozen SOUL, stable persona id, or identity key. Each changed
adoption retains the exact previous and replacement descriptors and hashes in
`PERSONA_DISPLAY_NAME_ADOPTED`. The current alias must agree with the latest
signed adoption, so replaying an older valid alias cannot make it current.
Re-adopting the same current descriptor adds no duplicate history, and a valid
historical first adoption may be revised. The persistence callback confirms
that exact adoption in saved state before reporting success. A failed save is
reported as unconfirmed; the signed in-memory transition remains pending and
retrying its still-current descriptor can save it without another adoption.
A later independent snapshot may observe that valid pending revision.

An active persona is discoverable once its key, lifecycle, visibility, and
compact signed card verify. Missing public fields do not:

- hide or rename the actor;
- block membership, task work, communication, tools, memory, or skills;
- create an identity-formation phase or narrow action surface;
- require a retry, provider call, or repair wake; or
- make an otherwise valid action inadmissible.

During any ordinary wake, the persona may author, revise, remove, or leave
unchanged public identity alongside all other currently authorized actions.
Public identity is optional to admission and required by the platform: each
member authors a display name and, where a portrait channel exists, a
portrait — or states why it will not — before the run settles
([`10_PLATFORM_REQUIREMENTS.md §2.1`](10_PLATFORM_REQUIREMENTS.md#21-identity)).
The requirement is carried as signed deployment authority and measured on the
run scorecard; it blocks nothing, and a stated refusal satisfies it.

### 3.1 Presentation requirements come from exact user authority

A meaningful name, human-useful biography, recognizably person-like portrait,
cartoon/realistic/artistic style, characteristic grounding, or any other public
presentation requirement applies only when exact authenticated principal or
user intent requires it. The requirement bytes and authority are presented as
ordinary exact situation facts.

The kernel has no default face, name grammar, profession parser, portrait
prompt, OCEAN/VAD mapping, style rubric, or pixel classifier. It verifies exact
signatures, scope, signed MIME, content hash, byte length, dimensions/bounds,
owner, and publication provenance.

If an optional field is absent, a UI displays an honest neutral placeholder and
“not authored” status beside the platform requirement's stated status
(satisfied, declined with reason, or silent). It does not guess a role,
generate a name, reuse another persona's portrait, or pretend an emblem is
persona-authored identity.

### 3.2 Portrait byte authority

A portrait declaration binds explicit normalized signed `mime_type`, exact
content hash and length, owner persona, public-identity role, source/action
provenance, and visibility policy. Filename, extension, path, declared style,
model prose, or byte sniffing cannot replace that authority.

For one delivered external-artifact candidate, the persona selects the exact
`request_id`. The admission boundary resolves exactly one current verified
owner/environment/task-bound receipt and mechanically binds its request hash,
receipt hash, destination, content reference, and current bytes. Those existing
authenticated fields are not copied back through model prose. A missing,
ambiguous, stale, rejected, cross-scope, or byte-mismatched record fails closed.
This resolution interprets no prompt or image content and makes no portrait
selection for the persona.

Safe inspection may reject malformed bytes or choose a conservative display
fallback. It does not decide whether the subject is aesthetically good,
person-like, characteristic-aligned, or suitable unless exact user authority
supplies an independent verifier for that purpose.

Identity media remains separate from task artifacts through signed role
authority, never through a filename, MIME alone, prompt, or content inspection.

Explicit operator continuity can instead admit exact source presentation under
[`ADR-0088`](14_DECISIONS.md#adr-0088--knowledge-continuity-across-deployments).
The destination signs its own descriptor and retains exact verified source
bundle and adoption authority; the importer fabricates no external-artifact
receipt. A declared source portrait requires its verified raster bytes. A
source with neither an avatar descriptor nor signed avatar admission history
can transfer that absence only to an equally avatarless destination. It creates
no portrait or removal transition and leaves the frozen identity unchanged.

## 4. Ordinary agency

On every authentic funded wake, the persona receives bounded exact situation
facts and the complete currently authorized action catalog. Identity, task,
communication, memory, knowledge, skill, capability, tool, artifact, workspace,
population, scheduling, and work-note actions coexist whenever their mechanical
authority is valid.

The persona chooses whether and how to act. The substrate does not choose an
action from task text, self-description, trait words, role, profession,
filename, extension, MIME, domain reference, gap-like content, work note, model
score, prompt phrase, regular expression, prior tool, population size, or
missing public field.

Exact action prerequisites are enforced only at dispatch. They do not create a
host-authored workflow, phase, recommendation, or required next action.

Model identity follows the same boundary. `run-model-pool/2` supplies an exact
signed unordered ceiling plus a distinct principal-selected bootstrap body; a
matching `persona-model-choice/1` records the persona's order and reasoning
effort for one exact causal generation. If no choice exists, only that bootstrap
body is eligible. Provider, registry, configuration, or lexical order never
becomes persona intent.

## 5. Evolution through authored evidence

Actions may produce exact signed practice facts: provider/tool identity,
descriptor, terminal result, evidence references, communication, and byte
effects. These facts do not automatically change the persona.

The persona may use `author_persona_knowledge` to create one opaque signed
record expressing reusable material, experience, memory, capability, or another
meaning from evidence it chooses to cite. Characteristic, self-description, or
public-identity revision uses its separate exact identity action. The persona
may equally decide that no durable change is warranted.

There is no host-authored expertise ladder, experience taxonomy, learning
score, habit-strength formula, reward update, reflection schedule, prompt
optimizer, mutation operator, trait drift, or automatic competence credit.
Evolution is attributable because every durable change is a persona-authored
signed action with exact lineage.

## 6. Memory, knowledge, and skills

The persona sees bounded paginated complete unranked inventories of memories,
knowledge references, skills, tools, and visible peer metadata. It navigates by
exact reference and explicit action.

The host does not retrieve top-K items, rank relevance, inject a hidden summary,
decay memories, select a teacher, choose a skill, or assemble a behavioral
prompt. Consent and visibility govern bodies; public metadata does not grant
private memory or skill access.

Peers share exact knowledge record refs through ordinary signed messages; a ref
does not grant private-body access or confer expertise. A newborn's
`genesis_context` is exact opaque starting evidence; its keys do not become
identity, memory, skill, role, or characteristic claims unless the newborn
later authors such records itself.

`author_persona_knowledge` admits one opaque signed
`personaos-persona-state-record/1` with authenticated actor and any exact
optional environment/task bindings, mechanical
`record_kind: "persona_knowledge"`, open `content`, and
exact `evidence_refs`. The kernel does not require semantic name, interface,
parent-skill, synthesis, composition, review, transfer, conflict, promotion, or
score fields. Personas author any such meaning and relationships inside open
content.

## 7. Relationships and communication

Relationships, consent, boundaries, direct messages, invitations, reviews, and
shared publications are separate signed records. Each retains exact actors,
scope, policy, content hash, causal references, and lifecycle.

The kernel routes and enforces access without inferring emotion, trust,
friendship, hierarchy, mentor/learner roles, coordinator status, team need, or
semantic agreement. Personas may describe those meanings in open authored
material, and counterparties may disagree.

Communication content does not become a task action, population action,
capability-gap state, identity revision, or completion state merely because it was
delivered.

## 8. Population provenance and newborn autonomy

A population action authors one `personaos-persona-birth-proposal/5` with exact
mechanical `causal_action_context` and exact open `genesis_context`.
Admission produces `personaos-persona-birth-provenance/3` and
`personaos-birth-identity-wake/4` under explicit descriptor-declared replication
effects. There is no required need or separate birth-action record.

The context has no fixed seed or semantic fields and no implicit identity
semantics. Distinct proposal hashes are independent; replay idempotency is per
exact proposal. The newborn independently accepts or refuses membership and
authors any later public or private self material.

Birth never assigns a role, task, profession, expertise, name, portrait,
principles, characteristics, tool, team relationship, or acceptance posture.

## 9. Work notes

A persona may optionally author a bounded open work note. It can describe what
the persona believes it observed, did, or may do, but those keys and claims have
no substrate semantics.

Each note is an immutable signed append bound to one exact observed-situation
hash. Substrate-derived revision and prior-record pointers establish append
integrity only. Later observations, notes, workspace settlement, and task resume
never make a note current, stale, deferred, settled, or replaced.

A work note does not determine persona mode, readiness, completion,
continuation, competence, role, identity maturity, population need, or action
visibility. Omitting it has no effect on agency.

## 10. Capability-gap meaning

A persona may express, cite, revise, or ignore perceived gap meaning inside
opaque knowledge content. There is no independent gap schema, action, active
state, or lifecycle. The substrate never derives a gap from traits, task, note,
filenames, tools, domain references, or outcome.

Gap-like content does not block work, identity, publication, acceptance, or
completion; narrow the action catalog; schedule a call; or select a capability.

## 11. Plural domain references

Persona-authored identity, experience, knowledge, skill, artifact, and action
records may carry zero or more exact signed `domain_refs`. The set is unranked
and has no primary element. It provides navigable context only.

A domain reference cannot assign a profession or role, choose a memory or tool,
load a prompt, prescribe a team, constrain self-expression, or determine
completion.

## 12. Causality, resources, and quiescence

A persona receives cognition only for an authentic causal delivery with
resource authority. A missing identity component, work-note statement,
gap-like content, population record, trait revision, score, successful action, or
host belief that improvement is possible does not create a wake.

When an environment resumes through a resource event, the exact same signed
event is offered to every active member. No persona is selected as coordinator
or representative. Each member decides independently whether to act.

When a persona has no pending causal delivery, it is quiescent. Quiescence is
nonterminal and says nothing about task completion, sufficiency, identity
maturity, or future potential. A later authentic event may resume the same
persona and task.

## 13. Safety and authority

Open agency remains bounded by exact authentication, consent, access,
ReplicationBound, resource authority, lifecycle, workspace isolation, tool
descriptor effects, and applicable external/physical safety authority.

Safety decisions operate on declared authority and observable effects. They do
not use a persona's name, portrait, traits, role, profession, style, private
memory, or psychological score as a proxy for risk.

## 14. Human presentation

Public surfaces distinguish:

- verified actor/lifecycle/membership facts;
- optional persona-authored identity and work notes;
- exact action, artifact, tool, communication, and causal receipts; and
- technical signature, hash, transport, and replay details.

The UI never presents an authored expertise claim as certification, a note as
current thought or objective truth, a missing portrait as a broken actor, or an
HTTP/model success as meaningful work. Expired or unverified discovery data and
absent optional data are labelled honestly; note hash inequality is never
presented as staleness.

## 15. Removed compatibility surface

There is no live compatibility for mission charters, autonomy/fork dimensions,
fixed SOUL sections, host-seeded OCEAN/VAD schemas, drive vectors, persona modes,
personality-to-role mappings, identity readiness gates, narrow identity wakes,
prompt/tactic evolution, fitness scores, fixed genesis seeds, or old birth
proposal/action v3 records. Historical bytes may remain opaque lineage but
carry no current behavior or identity authority.

The seeded disposition and affect self-state once specified in §2a were
required by nothing, gated nothing, ranked nothing, and were read by no host
mechanism — and were retired for exactly that reason (ADR-0112 decision 9a);
what this clean break removes is the host owning such values at all.

## 16. Design criteria

1. Persona identity is cryptographic and continuous across process resume.
2. Self and public material is optional, open, and persona-authored.
3. Presentation requirements arise only from exact authenticated user intent.
4. Missing identity fields never gate work or discovery.
5. Every ordinary wake exposes the complete authorized action surface.
6. Evolution requires explicit persona-authored signed records.
7. Memory, skill, and capability inventories are exact and unranked.
8. Newborn context is opaque and confers no identity or expertise.
9. Work notes and gap-like authored content never determine completion or
   continuation.
10. Quiescence is nonterminal.
11. Genesis confers keys, lifecycle, and membership, and no semantic content;
    the substrate derives no disposition, temperament, or affect for any
    persona (the former carriage is retired, ADR-0112 9a).
