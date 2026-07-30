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

An action result creates a later turn only when its exact descriptor declared
and registered an event that was actually delivered. Coordination prose and
successful receipts alone have no wake authority.

## 5. Workspace coordination

Each member's worktree remains leased through capture, publication, and
settlement. Shared-environment publications retain exact author/action/time
provenance. A peer's bytes cannot be credited as the current actor's tool use,
practice, artifact, or review.

Concurrent conflicts preserve every exact path/hash alternative. Only an
authorized signed resolution chooses or synthesizes bytes. The substrate does
not choose from filenames, extensions, MIME, role claims, or task semantics.

## 6. Knowledge and skill coordination

Visible peer persona-knowledge/tool metadata appears in complete bounded
paginated unranked inventories. A persona chooses whether to contact an owner,
share an exact ref, request authorized body access, acquire/provision/invoke a
tool, or ignore an item.

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
