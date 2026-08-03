---
title: PersonaOS — Persona-Authored Work Notes
status: Stable
---

# 19 — Persona-Authored Work Notes

A persona may append a signed open note about an exact situation it observed.
The note is useful human-facing context and provenance. It is not task state,
current thought, a substrate judgment, or authority over what happens next.

This document is a clean break from structured readiness frames, commitment
reducers, completion votes, required status reports, and note defer,
settlement, pending, current, or stale lifecycles. None is part of the work-note
protocol.

## 1. Exact observed situation

The kernel may project `personaos-persona-work-situation/1` from exact facts
already in its possession, including:

- task, environment, persona, and active-membership identifiers;
- exact workspace, artifact, conflict, package, and materialized-byte facts;
- exact active-member cards and signed contributions;
- exact resource, action, tool, memory, skill, and knowledge inventories; and
- exact evidence, pagination, omission, and causal references.

The situation is bounded and content-addressed. Bounds, pagination, and
truncation are explicit. The kernel does not turn these facts into a role,
priority, workflow phase, recommendation, capability judgment, team need,
readiness, or completion claim.

## 2. Optional append-only authored observation

During any ordinary wake, an active member may invoke
`record_persona_work_state`. The action is optional and remains alongside all
other currently authorized actions. Omitting a note does not narrow that
catalog, trigger a repair wake, block work, or make the persona unready.

This is the only generic action for publishing a persona-authored progress or
work-state observation. A separate progress-only action would let a persona
publish an apparently terminal narrative without choosing the causal
disposition of that same observation, so fresh lifecycles expose no such action
and accept no legacy progress-report schema.

The persona authors only bounded open canonical JSON in `work_note` and
optional opaque exact `causal_refs`. The substrate derives the mechanical
fields, and the authorized action signs the
`personaos-persona-work-state/3` envelope with the persona identity key. It
contains:

- `work_state_id`, `persona_id`, `environment_id`, and `task_id`;
- the exact observed `situation_hash` and `membership_id`;
- substrate-derived `note_id`, integer `revision`, and
  `supersedes_work_state_ref`;
- the exact open `work_note` and `causal_refs`; and
- `authored_at`, signing-key identity, and signature.

Records are immutable and append-only. `revision` is only a mechanically
verified append sequence, and `supersedes_work_state_ref` is only an exact
pointer to the preceding record. Neither field makes an earlier note obsolete,
less true, settled, deferred, stale, or non-current. All verified appends remain
independently inspectable.

`work_note` keys and values are chosen entirely by the persona. The substrate
does not reserve fields such as status, role, plan, commitment, blocker,
confidence, competence, vote, next step, or done. If a persona uses such words,
they remain ordinary authored claims with no protocol semantics.

`causal_refs` prove only the identities and provenance of records the persona
chose to cite. They do not prove relevance, quality, correctness, or
completion.

## 3. Mechanical surfaces and the observation-binding fact

`personaos-persona-work-state-surface/5` exposes each verified append with its
exact note, authorship, signature/hash, append metadata, causal references, and
observation binding. `semantic_interpretation_performed` remains false.

The surface may carry `situation_hash`, `latest_observed_situation_hash`, and
`bound_to_latest_observation`. The boolean states only whether those two exact
hashes are equal at projection time. False does not mean stale, invalid,
outdated, superseded, deferred, pending settlement, irrelevant, or wrong. True
does not mean current, complete, sufficient, relevant, or accepted. A later
observation changes only this factual equality; it never rewrites or
reclassifies the signed note.

The surface also carries `active_membership_current` and `signature_verified`
as exact mechanical facts. They do not evaluate the note body.

`personaos-persona-work-note-state/1` is a compact reader for the mechanically
last verified append. It exposes append identity/sequence and open content for
transport convenience only. It is not a current-state reducer, a winning note,
or a semantic replacement for earlier history.

A run may expose independently verified notes in
`personaos-work-state-evidence/1` alongside exact workspace, conflict,
materialization, and quiescence facts. It has no required persona roster,
population aggregate, agreement rule, vote, or semantic outcome field. Any
mechanically last-per-persona view is an unranked convenience; complete note
history remains separately navigable.

During an active turn, `personaos-active-peer-work-state-heads/1` gives the
acting persona one separate latest signature-verified head per other active
membership. This prevents a newer generic message/action event or uniform
prompt-byte pressure from hiding the peer's current authored note. Latest means
only highest verified append revision with timestamp and immutable ID as exact
ties; it is not a relevance, readiness, quality, leadership, or completion
ranking. The bounded projection reports every omission and grants no causal
successor.

## 4. No note settlement or reclassification

Workspace, artifact, action, payment, delivery, and external-effect settlement
apply to their exact effects. A work note is already a terminal immutable signed
append; it is never deferred, settlement-pending, settled, reconciled, closed,
or reopened.

Workspace changes, peer publications, later notes, resource changes, task
resume, quiescence, or acceptance do not mutate or reclassify it. They produce
new exact facts that a persona may inspect and may choose to cite in another
append. No later fact silently adds meaning to an older note.

A same-task resume must nevertheless make the immediately prior evidence
observable. The kernel-signed `personaos-prior-run-resume-observation/1` may
carry the prior run's already verified `personaos-work-state-evidence/1`
unchanged, including each persona's exact latest signed note projection and its
`bound_to_latest_observation` value. This is historical causal evidence, not a
new current-note classification. It is transported in a dedicated bounded lane
so raw-event compaction cannot hide it; note content never controls whether the
lane is admitted, projected, or acted on.

## 5. No completion or continuation semantics

A work note never:

- satisfies, covers, waives, or closes any part of principal intent;
- proves that an objective, artifact, review, or professional standard is met;
- creates or resolves capability-gap state;
- creates, cancels, selects, or suppresses a causal successor;
- elects a coordinator, assigns a role, determines team size, or authorizes a
  birth;
- changes membership, action authority, tool availability, or resource
  allocation; or
- becomes a task-level vote through aggregation with other notes.

Objective acceptance comes only from its exact authenticated authority and
evidence mechanism. The kernel does not infer acceptance from note prose,
append order, revision, hash equality, or member count.

Continuation likewise comes only from an actual causal edge: a delivered
resource event, authenticated peer message, armed future receipt,
persona-authored wake, or another protocol-defined stimulus. Text such as
“continue,” “blocked,” “ready,” or “done” creates no edge.

The work-state action's separate signed causal disposition is action authority,
not meaning inferred from `work_note`. Both variants preserve one bounded exact
persona-authored rationale so the choice remains intelligible to humans, peers,
and the persona's later self. The substrate does not interpret that rationale or
turn it into a score, acceptance fact, or successor. When an immediate disposition is signed
at the finite resource boundary, the immutable work-state record preserves that
exact choice as `waiting_resource`; it is not itself an executable wake and
does not allocate a call. A later signed resource-recovery edge presents the
verified state unchanged and supplies the execution authority. This does not
settle, reopen, or reclassify the note.

When no causal delivery is pending, the run is **quiescent**. Quiescence is
nonterminal: it says only that nothing is presently scheduled. It does not mean
the objective is complete, abandoned, sufficient, or incapable of further
improvement. A later authentic event may resume the same task.

## 6. Capability-gap meaning remains optional and separate

A persona may describe a perceived gap in ordinary opaque knowledge content,
cite that record, author another view, or never express one. There is no
dedicated gap record/action/lifecycle. A work note may cite the knowledge record
like any other exact ref, but the kernel does not derive gap state from the note,
task text, filename, extension, role, prompt, regular expression, or outcome.

Expressed or absent gap meaning does not determine readiness, completion,
identity maturity, action availability, or whether another wake is required.
Tool discovery, communication/ref sharing, authorized body access,
acquisition/provisioning, generic knowledge authorship, invocation, and
delegation remain ordinary persona choices.

## 7. Human presentation

Human interfaces may lead with the most recently appended exact authored note,
but must label it by authorship and append time—not as current thought or task
state. They also show the task and exact observed situation, causal references,
signature/provenance, and the factual observation-hash binding. Technical hashes
and replay counters may remain in a secondary inspector.

The interface never labels a note current, stale, deferred, pending settlement,
settled, ready, or complete. If no note exists, it says so plainly without
inventing a summary, role, thought, activity, accomplishment, or completion
judgment. Earlier appends remain reachable.

Public display-name, portrait, biography, and style requirements are not work-
note fields. They apply only when exact authenticated principal/user intent
requires them and remain independent of whether the persona can work.

## 8. Removed compatibility surface

There is no compatibility path for the former structured work-state schema,
readiness lattice, durable commitment reducer, requirement-coverage reducer,
uncertainty disposition, collaboration checklist, population vote,
continuation status, or defer/settlement/current/stale note classifications.
Old records may remain opaque historical bytes but confer no current authority
or semantics.

## 9. Design criteria

1. Work notes are optional append-only persona-authored open claims.
2. The substrate validates exact mechanics and never interprets note keys or
   values.
3. Append metadata orders records but never replaces or reclassifies them.
4. `bound_to_latest_observation` is hash-equality evidence only.
5. Note content never determines objective completion, readiness, continuation,
   capability, population, identity, or settlement; the separately signed
   causal disposition remains exact action authority only.
6. Quiescence is a nonterminal absence of pending causal delivery.
7. Human presentation distinguishes authored claims from verified facts.
