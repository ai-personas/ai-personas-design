---
title: PersonaOS — Persona-Owned Work State
status: Stable
---

# 19 — Persona-Owned Work State

A human needs to understand how a persona sees the task, what it is doing, what it completed, what remains uncertain, and what it intends to do next. Model status, HTTP status, latency, hashes, and a generic “snapshot” label do not answer those questions.

PersonaOS therefore persists a persona-authored, signed work-state revision. This is public working context, not hidden chain-of-thought and not a host-generated summary.

This document is a clean break. It replaces task-orientation outputs, pressure appraisals, and situation-sufficiency judgments.

## 1. One situation, one persona revision

The kernel mechanically projects `personaos-persona-work-situation/1` from exact observable facts:

- task identity and principal-authored task material;
- environment and membership state;
- exact workspace tree, artifact and conflict state;
- active team PersonaCards and signed contributions;
- resource, budget, tool, request, and action availability; and
- exact evidence and causal references.

It signs `PERSONA_WORK_SITUATION_OBSERVED` but does not interpret the facts.

During its ordinary substantive turn, the persona may invoke `record_persona_work_state`. That single action writes `personaos-persona-work-state/1` and `PERSONA_WORK_STATE_AUTHORED`. No second “orientation” or “are we done?” call is made.

## 2. Work-state fields

Each revision contains:

- stable `frame_id`, monotone `frame_revision`, and exact `supersedes_frame_ref`;
- the persona's `working_understanding`;
- explicit `assumptions` and `uncertainties`;
- durable `commitments` with stable IDs, parent references, and evidence expectations;
- explicit `commitment_transitions`;
- `current_contribution`, `current_focus`, `accomplished`, and `next_intent`;
- an open persona-authored `collaboration` document;
- `continuation = continue | quiescent | ready`; and
- exact evidence, action, and request references.

All prose and open documents belong to the persona. The kernel validates bounded canonical shape, current authority, signature, revision lineage, and exact references only.

The persona authors the initial `frame_id`. After a signed revision exists, the structured turn contract mechanically binds the same frame ID, the next integer revision, and the exact prior `work_state_id` as the supersession reference. These are ledger-order consequences, not repeated semantic choices. This prevents a useful completed turn from being discarded merely because a model retyped lineage bookkeeping incorrectly.

## 3. Durable commitments

The `commitments` array contains introductions only. An active commitment is never repeated or silently reworded in a later revision. Omitting it does not close it; the reducer carries it forward until the persona explicitly transitions its exact ID:

- `satisfied`, with at least one exact evidence reference;
- `superseded`, with a rationale;
- `principal_waived`, with exact principal authority; or
- `blocked_external`, which remains active and visible.

For each structured revision, the transition-ID schema is mechanically restricted to the complete set of exact prior active commitment IDs. The reducer reads IDs, transition states, and references. It never decides whether a statement is substantively complete.

`ready` remains the persona's signed judgment even when it conflicts with its own open commitments or reported uncertainties. The reducer preserves that judgment but projects effective readiness as false until no active or unknown commitment and no persona-reported uncertainty remains. This keeps the disagreement visible to humans instead of discarding the whole work state, while preventing one persona's optimistic posture from closing material work.

### 3a. Persona-authored agency reconciliation

Every task-bound final cognition envelope MUST include a closed `agency_reconciliation` document. The runtime stores that exact authored document inside the work state's open `collaboration` mapping; it does not synthesize or summarize it. Before choosing a continuation posture, the persona explicitly reconciles:

- the exact prior active commitment IDs and prior uncertainties, plus any introduced in the current revision;
- exact remaining model-call and mission-deadline authority;
- whether it judges meaningful progress to remain;
- any genuine external blocker and its evidence references;
- the causal successor it actually authored, if any; and
- whether its own characteristics and experience lead it to want a distinct contribution or independent review; and
- whether its exact open commitments are supported by its own retrieved skills and experience, the complete current action surface, the bounded complete unranked local execution-capability index, and signed acquisition / invocation evidence; any material capability gaps; and the capability action it actually took or authored next.

When the persona judges that meaningful progress remains, it authors an actual successor through the existing generic self-wake, scheduling, or peer-coordination mechanisms, or records an evidenced external blocker. `next_intent`, progress prose, and a filename do not schedule work. When the persona itself wants a distinct contribution or independent review, it initiates or continues the existing need → exact discovery → candidate disposition → genesis path from [`16_POPULATION_DYNAMICS`](16_POPULATION_DYNAMICS.md). The kernel does not infer the judgment from task words, assign a role, choose a peer, force a team size or birth, or mint a semantic wake.

Capability reconciliation is also persona-owned. The signed work situation MUST carry the bounded complete exact-name index of the currently observed local execution namespace, its snapshot hash and pagination cursor, the complete unranked action catalog, current environment-mounted tools, and the persona's retrieved skill evidence. Prompt compaction MUST preserve the compact exact-name index rather than retaining only a lexically early provenance page. Brain compilation receives the mechanically derived exact affordance identifiers; it does not receive a host-selected subset based on task text. The persona MAY conclude that existing capabilities are sufficient. Discovery, acquisition, provisioning, skill authoring, invocation, and delegation remain explicit persona actions with ordinary signed intent and effect evidence; the runtime MUST NOT rank, select, provision, or invoke a capability merely because the reconciliation reports a gap.

## 4. Workspace settlement

A work state is bound to the exact situation and workspace bytes the persona observed. If the workspace changes between observation and signature, the intent becomes settlement-pending rather than being silently attached to different bytes. A stable recapture may bind it through `PERSONA_WORK_STATE_SETTLEMENT_BOUND` without changing the persona's authored choice.

Any later durable change to the task, environment, membership, artifacts, conflicts, acquired capabilities, or workspace makes the prior state stale. A transient tool menu or transport flag does not.

## 5. Population-aware completion

One persona's ready state is never collective readiness.

For a task with more than one required active participant, completion requires each participant's latest effective signed work state to be current, ready, free of active commitments, and free of persona-reported unresolved uncertainties. The materialized outcome and conflict state must still match the exact workspace revision those states observed.

The reducer does not wake personas, select reviewers, infer missing work, or call a model. Open work continues because a persona authored a commitment, another participant remains non-ready, a causal message remains unsettled, workspace evidence changed, or an explicit user/operator continuation exists.

## 6. Human presentation

`personaos-persona-public-cognition/2` exposes a bounded `current_work_state` and `work_state_history` as `personaos-persona-work-state-surface/1` rows. Public rows contain the authored human fields and counts for private exact references; operator rows may expose the full signed preimage.

The UI leads with:

1. how the persona sees the task;
2. what it is contributing and focusing on;
3. what it completed in this pass;
4. what it intends to do next;
5. open commitments and expected evidence;
6. uncertainties and assumptions; and
7. its collaboration plan.

Model calls, provider events, latencies, run IDs, schemas, hashes, and signatures remain available in a collapsed technical or verification disclosure. They do not become the human headline.

A stale row is labelled as the last authored update, never as current activity. Provisional provider output is labelled provisional and never presented as the persona's signed cognition.

## 7. Model-call economy

The work-state protocol must reduce calls, not add an appraisal loop.

- Situation projection, signature verification, settlement, replay, stale invalidation, public projection, and completion reduction are token-free.
- A direct task receives one ordinary substantive persona turn unless new causal work justifies another.
- While an exact materialized-outcome byte/future gate remains open, a non-read-only action descriptor that was already invoked without satisfying that mechanical gate MUST lose replay authority for the remainder of the same semantic turn. Every other currently authorized descriptor remains available. This is descriptor/result/byte evidence, not a semantic tool ranking: the substrate does not name a preferred replacement, infer whether the action was useful in another sense, or prevent a later causally distinct turn from choosing it again.
- If that turn commits an authenticated non-read-only action but the provider omits the required terminal work-state response, the same semantic turn MAY spend at most one remaining call to recover only that response. The recovery call receives the exact sealed action results and the unchanged signed situation, exposes no action or command capability, and offers one effect-free structured carrier whose argument schema is exactly the required terminal response schema. The carrier is never dispatched and grants no file, MCP, routing, scheduling, or wake authority; its arguments still pass through the unchanged response validator before persona signing. It cannot replay the source effect, schedule a host-selected wake, infer task meaning, or override a persona-authored continuation choice. If an authenticated future stimulus was already registered, no recovery call is added because that stimulus owns the next observation.
- No host-authored task orientation is generated.
- No host-authored pressure or sufficiency appraisal is generated.
- A resume may reproject and close a ready state token-free when every exact binding still verifies.
- An unchanged wake cannot spend a call merely to renew timestamps or restate a prior state.

## 8. Non-goals

Work state is not:

- hidden reasoning or chain-of-thought;
- a task classifier;
- a domain checklist;
- a filename or artifact-extension rule;
- an automatic birth, invitation, acquisition, or tool trigger;
- a host-authored role assignment; or
- proof that the underlying work is correct.

Correctness comes from exact artifacts, verifiers, measurements, peer work, and principal intent. Work state explains the persona's public working position and preserves its commitments.

## 9. Design criteria

The current live-path criteria are in [`11_DESIGN_CRITERIA.md`](11_DESIGN_CRITERIA.md). No prior work-state, appraisal, orientation, or cognition schema is accepted as a compatibility input.
