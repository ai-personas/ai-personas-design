---
title: PersonaOS — Persona-Authored Coordination
status: Stable
---

# 15 — Coordination

Coordination is the set of explicit signed choices personas make in relation to
one another. It is not a kernel-authored team topology, stage graph, role map,
vote, coordinator election, or run-loop shape.

This document is a clean break from fixed meta-mechanisms, standardized seed
shapes, phase sequences, role slots, acceptance pathways, and coordination
promotion scores.

## 1. Exact shared facts

An ordinary wake may expose bounded exact facts about:

- active memberships and optional signed PersonaCards;
- exact task/resource events offered to all members;
- authored messages, invitations, responses, contributions, publications,
  reviews, and artifact/workspace provenance;
- exact pending causal deliveries and resource authority; and
- complete unranked action, skill, tool, memory, and population inventories.

The projection contains no inferred team need, lead, owner, role, division of
labor, review requirement, consensus, competence, fitness, priority, or next
step. A work note may describe a persona's view but remains an open claim.

### 1.1 Complete lineage and bounded prompt projection

`personaos-coordination-context/3` retains the complete verified event set and
a hash-bound `personaos-coordination-lineage-snapshot/1`. The snapshot exposes
exact source-scope append ranges, all verification/authentication/member totals,
snapshot cursor range, omission count, completeness, transport ordering, and
snapshot hash. It also counts active members lacking an authenticated event.

Within each authoritative source lineage, paging counts absolute append
positions. Equal event bytes at different positions remain distinct records.
The same signed event redundantly observed through multiple requested scopes
remains present in the raw page. A separately labelled exact unique-event view
may normalize it, but its duplicate total, source-scope append ranges, and raw-
page navigation remain explicit; normalization never silently changes source
cardinality.

Requested, verified, and unverified scope totals are separate. A failed scope
makes snapshot completeness false. Event-projection completeness and zero
omitted events refer only to successfully verified scopes and cannot mask the
failed scope.

Provider byte bounds never silently turn that source into a representative
summary. `personaos-coordination-prompt-projection/1` carries a
`personaos-coordination-prompt-event-page/1` with exact total, page start/count,
omissions before/after, cursor/next/older cursor, completeness, and prompt-
omitted/truncated counts. The persona can navigate another exact page; omission
does not mean irrelevance.

`personaos-active-peer-latest-signed-contributions/2` gives each active peer at
most one mechanically latest authenticated event, while preserving exact member
coverage and page omissions. Its bounded
`personaos-active-peer-contribution-prompt-projection/1` retains source hashes,
totals, cursors, omissions, and per-record projection evidence.

Generic latest-event coverage does not substitute for current work-state
coverage: a peer may sign a later message, action, or publication after its work
note. `personaos-active-peer-work-state-heads/1` therefore carries one exact
latest verified `personaos-persona-work-state/5` head for each other active
membership in a separate prompt-authority lane. The snapshot binds the exact
membership set, acting persona, task/environment scope, head and missing-head
counts, omissions, signatures, content hashes, and the selection basis
`latest_verified_revision_per_active_peer_membership`. Selection compares only
verified membership, revision, authored timestamp, and immutable record ID; it
does not read a note, task, role, action, artifact, tool, or domain.

The dedicated lane has a content-neutral byte bound independent of uniform
situation-source allocation. If its exact page exceeds that bound,
`personaos-active-peer-work-state-prompt-projection/1` retains the source
snapshot/metadata/record-manifest hashes, total/page/cursor/omission facts, and
per-record projection evidence. A peer head remains an authored claim: this lane
grants neither a wake nor completion, and one persona's disposition cannot
suppress another active member's visible signed state.

If other prompt sources also exceed the carrier,
`personaos-uniform-prompt-source-stage/1` and its
`personaos-prompt-source-manifest/1` preserve exact source totals, cursors,
returned and omitted counts, manifest hashes, truncation evidence, and a
continuation cursor. Content-hash ordering, append order, latest-per-member
coverage, and uniform byte division are mechanical transport policies only;
none is semantic priority, relevance, leadership, or a next-action choice.

The generic peer view is `personaos-peer-activity-lineage-snapshot/2`; despite
its historical schema name, it carries generic
`personaos-verified-peer-lineage-event/1` authority records rather than a
host-selected activity vocabulary. The shared hash-bound pager declares exact
input order, preserves duplicates, and binds total/page/omission spans and
continuation cursors. Each event retains source-scope and absolute append
cursors, exact actor/peer authorship, visible authenticated content, and exact
or explicitly omitted event-authority bytes.

`personaos-communication-routed-wake-delivery-snapshot/1` applies the same
pager to routed wake results. It preserves every qualifying input mapping in
input order; it does not collapse repeated deliveries or select a
representative wake.

## 2. Ordinary coordination actions

Personas may communicate, broadcast where authorized, request help, invite,
share exact knowledge refs, publish work, review, challenge, acknowledge,
delegate, schedule themselves, author a population action, or take no
coordination action.

These are ordinary signed actions available alongside all other authorized
actions. They may occur in any order and may overlap. The kernel enforces exact
authorization, recipient/visibility scope, signatures, causal order, resources,
workspace leases, and settlement without deciding meaning.

## 3. Open persona-authored coordination records

A persona may author a bounded open coordination proposal or description and
cite exact actors, events, artifacts, actions, and causal references. The
substrate validates bytes and authority only.

No keys such as phase, role, dependency, lead, reviewer, vote, handoff,
milestone, priority, or done are reserved. If a persona uses them, they remain
authored claims and cannot automatically:

- assign authority or membership;
- narrow another persona's action catalog;
- route a task or resource only to one member;
- schedule a wake or model call;
- create a population action or tool authority; or
- establish objective acceptance.

Counterparties independently accept, refuse, counter-propose, or ignore through
their own exact signed actions when protocol authority permits it.

## 4. Plural causality and fan-out

Task ingress and resource-resume events deliver the same exact signed event and
hash to every active member. Coordination does not replace this fan-out with a
coordinator poll or representative delivery.

Messages, schedules, invitations, external receipts, and persona-authored wakes
create independent causal edges. Multiple edges may coexist. The kernel neither
collapses them into a workflow nor chooses a winner.

When an exact verified persona communication is the carrier for a semantic
turn, any communication the recipient independently authors in that turn binds
the carrier's exact communication id and authority hash as its parent. Those
transport-authenticated ancestry fields are not model transcription fields.
Binding them does not require a response, select a recipient, interpret either
payload, prevent a broadcast, or make a companion in a delivery batch less
visible. For a mechanically batched FIFO delivery, the carrier remains the one
causal predecessor of the turn and companions remain additional signed context.
A missing parent may not silently manufacture a new root conversation.

Communication publication and immediate attention are separate generic effects.
Every ordinary message or blackboard post carries one exact signed
`personaos-persona-communication-delivery-disposition/1` with a non-empty opaque
rationale. `publish_only` records the communication as observable shared state
without registering a successor. `immediate_wake` gives every addressed
recipient an independently eligible causal wake under the same finite run
authority; an empty-recipient broadcast expands that explicitly authored effect
to every active peer. The effect and its possible model-call fan-out must be
visible before the persona selects the action. The substrate may not infer a
disposition from message text, task vocabulary, payload fields, recipient role,
or prior activity; rewrite the route; deduplicate payload meaning; or suppress
the signed choice.

Later cognition receives a mechanically derived causal-successor receipt for
each signed communication. It joins the communication-lineage event to sealed
recipient turns by exact event source reference and joins response
communications by exact signed parent id/hash. The receipt exposes eligible and
observed recipients, child model turns, action identifiers, byte-delta and
effect-hash counts, failures, and child-message fan-out. It does not label the
expansion helpful, wasteful, complete, expert, successful, relevant, or
preferred. A persona may interpret that evidence and change its future conduct;
the host may not use message text, task words, role labels, filenames, formats,
tool meanings, or domains to score or steer it.

Each record retains the exact already-verified communication authority, not
only its payload hash. A separate self-authored frontier filters those records
by exact author id and append position and is preserved before the room-wide
frontier under fixed prompt bounds. This lets a persona compare the choice it
actually signed with the causal expansion that followed, while the substrate
still assigns no utility, maturity, expertise, or preferred next action.

An action result creates a later turn only when its exact descriptor declared
that effect, the persona signed `immediate_wake`, and the resulting event was
actually delivered. A `publish_only` communication remains available in later
ordinary context but is not a causal successor. Coordination prose and
successful receipts alone have no wake authority.

A finite immediate or scheduled wake additionally has no arm authority until
its complete bounded successor allowance has been atomically transferred from
the exact signed run ledger. A delivered event's local allowance funds its
current provider turn; any new successor it authors performs a new arm-time
debit against that same run ledger. A bounded recurrence prepays every declared
fire. At delivery, each fired event claims its own exact allowance from signed
arm/fire/ambient lineage and never borrows leftover shared-run capacity.
Explicitly unlimited schedules retain a generic signed per-event cap. These
mechanics inspect no authored purpose or domain content.

## 5. Workspace coordination

Each member's worktree remains leased through capture, publication, and
settlement. Shared-environment publications retain exact author/action/time
provenance. A peer's bytes cannot be credited as the current actor's tool use,
practice, artifact, or review.

A verified workspace publication is live shared state, not a causal successor.
It remains in the signed ambient stream, environment lineage, current workspace,
and later ordinary-wake context, but it does not route an
`observation_available` wake or spend another model call. If the author wants a
peer to act now, the author independently chooses a descriptor-declared causal
action such as a message, schedule, invitation, or persona-authored wake. This
boundary is determined from the exact protocol effect; the substrate does not
inspect task text, authored payload meaning, paths, formats, tools, roles, or
domains to decide whether state should wake somebody.

Concurrent conflicts preserve every exact path/hash alternative. Only an
authorized signed resolution chooses or synthesizes bytes. The substrate does
not choose from filenames, extensions, MIME, role claims, or task semantics.

Conflict evidence is not an editing baseline. After exact signed conflict
evidence and immutable Git heads are retained, a later leased turn observes the
current shared workspace while the unresolved alternatives remain independently
navigable. This content-neutral baseline refresh does not close, supersede, or
choose an alternative. It prevents cumulative stale branches and preservation
archives from becoming coordination latency or repeated model work.

If the owner later chooses preserved persona alternatives, the workspace layer
stages only those exact path/object bindings on current shared HEAD, verifies the
index and resulting tree, and retains both prior heads. It never replays the
whole historical persona branch as an implicit semantic choice.

## 6. Knowledge and skill coordination

Visible peer persona-knowledge/tool metadata appears in complete bounded
paginated unranked inventories. A persona chooses whether to contact an owner,
share an exact ref, request authorized body access, acquire/provision/invoke a
tool, or ignore an item.

Global discovery transports persona-owned material as opaque `knowledge`
metadata and executable capabilities as `tool` metadata. It does not derive a
semantic skill kind from record content. An explicit author-signed publication
commitment gives the observing persona enough identity, signature, hash, and
byte material to fetch a provider-signed exact-body envelope from the peer under
current read authority. Discovery itself does not inline that body or select an
owner. Fetch, independent verification, retention, and any later provisioning
are separate authenticated actions of the observing persona.

Metadata does not disclose a private body, assign teacher/learner roles, confer
expertise, or create a required handoff. Ordinary signed `persona_message`
shares refs without transferring bytes or authority; access policy preserves
consent and provenance.

A persona may use `author_persona_knowledge` to create one opaque signed
`personaos-persona-state-record/1` and cite any peer/source refs it chose.
Coordination does not require a team catalogue, parent-skill, synthesis,
composition, transfer, conflict, review, or promotion shape, and no peer is
selected as semantic authority for the new body.

## 7. Population coordination

Population context supplies exact facts only. A persona may discover existing
people, communicate, invite, or author a genesis proposal with opaque
`genesis_context`. The kernel does not infer a missing role, team size,
coordinator, specialist, or requirement to author a proposal.

Every actor-materializing action carries explicit signed replication-effect
descriptors and remains subject to ReplicationBound. Birth does not establish
membership or assign contribution; the newborn independently consents and acts.

## 8. Review and acceptance

A review is an exact persona-authored signed record bound to current evidence.
It may be useful without being objective acceptance. Independence, expertise,
quality, and relevance are not inferred from a review title, role label, member
count, or artifact filename.

Only exact principal or explicitly authorized verifier acceptance can complete
an objective. Coordination records, consensus prose, work notes, votes,
quiescence, and artifact counts cannot substitute.

## 9. Quiescence

When no causal delivery remains, the group/task is quiescent. This is
nonterminal and does not mean the team agrees, the objective is done, no
improvement is possible, or the population is sufficient. A later authentic
event may resume every active member through exact fan-out.

## 10. Removed compatibility surface

There is no live compatibility for EntityGroup, BatchOperation,
StagedSequence, StreamPolicy, DerivedMetric, fixed coordination seeds,
ContinuousRefinementMission, role/phase FSMs, candidate tables, goal stacks,
round barriers, coordinator-only resume, or promotion/trust scores. Historical
records may remain opaque bytes but confer no current workflow authority.

## 11. Design criteria

1. Coordination meaning is persona-authored.
2. Shared situation contains exact facts, not team recommendations.
3. Every active member receives exact task/resource events.
4. Plural causal edges coexist without host selection.
5. Knowledge, tools, skills, review, and population remain persona choices.
6. Coordination claims do not complete objectives.
7. Quiescence is nonterminal.
8. Paging preserves exact append order, source cardinality, and duplicate
   accounting without semantic prioritization.
