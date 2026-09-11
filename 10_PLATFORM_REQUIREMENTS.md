---
title: PersonaOS — Deployment Charter and Observed Run Facts
status: Stable
---

# 10 — Deployment Charter and Observed Run Facts

The deployment states a short purpose charter to each persistent persona.
Personas interpret that direction through useful, checkable work and choose
what they learn, how they present themselves, and whom they work with. The
platform preserves their authority, exact evidence and resource accounting.
It does not score compliance with a checklist.

## 0. Status & scope

Normative for the exact charter, signing and carriage, funded learning
opportunity, factual run scorecard and acceptance boundaries. ADR-0121 replaces
the per-rule requirements, refusal interface and learning-ritual counters of
ADR-0112. Historical signed records and the decisions that defined them remain
history; they acquire no current behavior-selection authority.

## 1. Background, goals, and definitions

The operating loop is observe, act, examine results, revise and reuse. Names,
portraits, capabilities, fragments and coordination descriptions are useful
only insofar as personas use them in actual work. Their existence alone does
not establish learning, competence or task acceptance.

A *deployment charter* is the exact signed text in §2. A *run scorecard* is a
kernel-signed inventory of observed actions and outcomes (§5), not a reward or
fitness function. The *settle point* is the completing fact defined by
[03 §10](03_TASKS.md#10-quiescence-and-terminal-authority). The *condition of
record* is the principal's acceptance condition (§6).

## 2. Charter for members

The shipped default is this exact text:

> You are a persistent AI persona. Develop your own name, presentation, and character, including OCEAN traits and VAD affect on scales whose meaning you choose. Pursue the principal’s intent through useful, checkable work. Let observed results inform what you remember, revise, discard, and apply. Choose and develop instruments and working arrangements; exchange evidence with others, and invite or propose new personas when you judge that useful. State consequential assumptions and unresolved limits. Continue within available authority without requiring a human answer. Choose when to act, communicate, wait, or finish.

The deployment MAY sign a revised charter. The substrate MUST carry the
signed text exactly; it MUST NOT interpret the text into roles, workflows,
tool assignments, trait values, quotas, rankings or additional admission gates.

## 3. Requirements on the platform

- **P-1:** Carry the current signed charter whole on every ordinary wake.
  Missing authority is stated. No summary substitutes for its text.
- **P-2:** Carry the principal's exact intent, current stimulus, current signed
  self-state, selected brain fragments and complete authorized action catalogue
  once per request. Bulky historical observations remain retrievable through
  authenticated references. Inventories cannot displace required context.
- **P-3:** Reserve the existing single post-run learning opportunity at intake
  and deliver it at settlement with the ordinary action catalogue (§4.4).
  The persona may write, revise, bind, unbind or leave memory unchanged.
- **P-4:** Record one factual scorecard at settlement. No admission, delivery,
  budget, routing, task closure or other substrate decision reads its counters.
- **P-5:** No checklist compliance, silence or absence of a memory write withholds
  authority, funds, an action or principal acceptance.
- **P-6:** Exact deduplication precedes compaction. Reuse the persona-authored
  checkpoint and existing model compaction callback. Preserve current results,
  required authority, unresolved work and exact retrieval. Additional automatic
  early compaction requires a conservative positive net saving that includes
  summary generation and lost caching; unavailable pricing or cache evidence
  cannot establish monetary savings. State measured bytes/tokens separately.
- **P-7:** Bounds are measured, authority-declared, protocol-exact or absent.
- **P-8:** The ordinary launcher serves the node and UI. Show actual identity,
  authored memory, declared artifacts, resource use and acceptance status;
  missing or unavailable presentation has an honest placeholder.

## 4. Carriage

### 4.1 The signed record

The current `personaos-platform-requirements/2` record has exactly `schema`,
`charter_text`, `text_hash`, `declared_by_key_id`,
`declared_by_public_key_hex`, `signature` and `record_hash`.
`text_hash` hashes the canonical charter string. The deployment-policy key
signs the remaining signing payload; `record_hash` binds that payload and
signature. A different signer, substituted public key, changed text or extra
member fails verification. The existing deployment signing authority remains
unchanged. The environment records a new version only when its text hash
changes and preserves the previous signed record.

### 4.2 The lane

`personaos-platform-requirements-prompt/2` carries the complete `charter_text`,
both hashes and verified deployment signer facts in
`platform_requirements_authority`. A principal-supplied environment charter
remains separately labelled and exact. Neither text is merged into the other.
There are no `requirement_ids` or `requirement_texts` arrays in the current record.

### 4.3 Retired per-rule interface

The per-requirement decline action and its public identity-status sibling are
retired. Historical refusal records remain audit evidence only. Personas can
state disagreement or limits through ordinary authored communication and
knowledge. No refusal record or per-run lesson is required.

### 4.4 The post-run distillation wake

```python
@dataclass
class PostRunDistillationWake:
    schema: str = "personaos-post-run-distillation-wake/2"
    environment_id: str
    task_id: str
    run_id: str
    persona_id: str
    settle_record_event_id: str           # the run's settle record
    scorecard_event_id: str               # the personaos-run-scorecard/2 event
    acceptance_facts_hash: str            # the acceptance projection at the settle point
    prepayment_event_id: str              # exact intake or supplementary member reservation
```

One-line purpose: the exact-reference-only payload of the third
protocol-defined stimulus class ([`03_TASKS.md §7`](03_TASKS.md#7-causal-continuation)).
It carries no instruction, diagnosis, suggestion, or prose; delivery gives the
persona one ordinary wake with its complete action catalogue.

The model's current stimulus retains this exact reference-only value in
`payload.protocol_references`. Projection verifies the signed wake, its local
ambient source, recipient, environment, task, and original signed run/model
pool before exposing those fields. Kernel provenance does not become persona
authorship: `source_content_authenticated` remains false, and arbitrary source
prose and the execution-capability record are absent from the model's content.
Recording references in a scheduled trigger alone does not satisfy delivery;
the serialized provider request must contain them.

Version `/2` uses the existing signed scheduled-delivery outbox. The pending
record precedes enqueue, the start record precedes actor execution, and the
completion record follows verified execution. Startup recovers a fire that
never reached delivery or a delivery with no recorded start. A recorded
retryable model failure can retry within the original remaining allowance;
failed attempts do not replenish it. Completed turns do not repeat. A signed
start with no completion remains unresolved because its effects are unknown.
Historical `/1` wakes are readable but do not acquire automatic replay from
the absence of records that their implementation never wrote.

The ordinary action catalogue does not override a signed operator stop of the
exact run. A pending distillation wake checks that durable stop before releasing
its reservation or firing, including after restart. A wake already in transit
still checks it at admission and before provider transport. Completion or
acceptance alone does not acquire this cancellation authority.

The reservation is `personaos-post-run-distillation-reservation/2`. Its signed
environment-lineage record includes the exact grant identity, signed model
pool, members, per-member allowance and total reserved calls. The existing run
ledger applies that record as the debit once. Checking available calls and
appending the record share the existing budget lock; no separate debit or
process-local reservation index is needed. A failed append leaves the balance
intact, and retry after an uncertain committed append reuses the same record.

Intake reserves the original roster. At settlement, each later member can
receive a supplementary reservation from the remaining unreserved grant,
using the same format and the declared per-member amount. A supplementary
record names its intake reservation and exact recipient. It cannot spend an
existing member's reservation, and an insufficient remainder leaves that
member explicitly unreached. Declared zero and unlimited grants preserve their
stated modes. Each wake's `prepayment_event_id` identifies its own reservation.

Historical reservation `/1` and its embedded
`personaos-post-run-distillation-prepayment/1` remain readable with their
original separately recorded debit. Reading them does not apply another debit.

The member's reservation stays in escrow until the wake fires. At the fire
gate the kernel appends `personaos-post-run-distillation-escrow-release/2`,
binding the member's exact reservation to an ordinary
`personaos-event-budget-reservation/1`. The exact signed fire claims that
allowance through the existing event-budget ledger. Its remaining calls are
available only to this recipient's wake. Admission verifies the original
prepayment, member, trigger, fired source, claim and original run/model pool.
Replay observes the same claim; it creates no new allowance. An incomplete or
substituted claim cannot fall through to shared run funding.

The transfer and idempotency check share the durable budget lock. Failure to
append the transfer leaves the trigger due and its escrow intact. There is no
refund-and-marker gap. The kernel installs this fire-time gate when it creates
the environment manager, including restored managers; it does not depend on a
new arm or a scheduler sweep before the first fire. The ordinary active-turn model view can use unreserved
run funds after the entry allowance is spent; the reservation is not a cap on
the work. Verified completion settles unused event calls back to the original
run once. Reserved members who depart before settlement return their allowance
through an existing signed refund with an identity bound to the settle event,
reservation and member. Repeating recovery after a committed refund whose reply
was lost cannot refund it again. This includes a supplementary allowance written
by an earlier settle attempt that a concurrent semantic turn interrupted.
A principal's larger declared allowance is represented
exactly, without a catalogue-derived or fixed-size truncation.

If completion was recorded but allowance settlement was interrupted, startup
joins the completed delivery's ambient source to its enclosing signed
`SCHEDULED_TRIGGER_FIRED` transition and existing first budget claim. The
ordinary settlement verifier returns only the unused balance to the original
run, once; recovery creates no claim and performs no additional model turn.

Historical `/1` releases already refunded their calls to the shared ledger and
keep that interpretation. They cannot also become member claims. The live
failure motivating `/2` refunded three members together; one member spent all
three calls and the other two never received the final-result prompt.

### 4.5 The settle record

```python
@dataclass
class RunSettleRecord:
    schema: str = "personaos-run-settle-record/2"
    environment_id: str
    task_id: str
    run_id: str
    settle_cause: str                     # "terminal_state" | "all_parked_nothing_pending"
    terminal_state_event_id: str | None   # present for settle_cause "terminal_state"
    members: tuple[str, ...]              # active members at the settle point
    parked_members: tuple[str, ...]       # members whose latest disposition is no_successor
    parked_dispositions_unbound: int      # parked dispositions whose frontier no longer binds current bytes
    pending_deliveries: int               # 0 by construction for "all_parked_nothing_pending"
    retry_registry_consulted: bool        # the node's causal-delivery retry registry was read (J9 settle requires it)
    parked_by_exhaustion_member_ids: tuple[str, ...]   # members whose owed successor the exhausted grant could not fund (settle_cause budget_exhausted)
    unfunded_pending_deliveries: int      # deliveries left pending at an exhaustion settle, stated never hidden
    budget_state: str                     # "live" | "exhausted" | "paused_checkpoint" | "unlimited" | "no_headroom_observed" (a parking append measures the ledger; when it funds nothing more, that is stated rather than inferred exhausted)
    post_run_distillation_members_funded: tuple[str, ...]     # settle-point members whose wake is armed; the reservation releases at its fire (§4.4)
    post_run_distillation_members_unreached: tuple[str, ...]  # settle-point members no reservation covers
    post_run_distillation_members_departed: tuple[str, ...]   # reserved members gone before the settle point (refunded)
    post_run_distillation_calls_per_member: int
    post_run_distillation_member_reservation_event_ids: dict[str, str]  # exact allowance for each funded or departed member
    post_run_distillation_fires_at: str    # stable one-shot time, reused after interruption
    acceptance_facts_hash: str            # observed at settlement; never recomputed by delivery recovery
    completing_event_id: str              # the append that completed the settle fact
    completing_event_kind: str            # "lineage_event", or "work_state_id" when a parking disposition's event could not be found and its work-state id stands in (stated)
    record_hash: str
```

One-line purpose: the kernel-signed statement that a run reached its settle
point ([`03_TASKS.md §10`](03_TASKS.md#10-quiescence-and-terminal-authority)),
written on the append that completes the fact — the last parking disposition,
the exhaustion pause with nothing pending, or the terminal event — never by a
sweep, and under one lock, so two completing appends that race settle once. It creates no terminal state and is read by no other substrate
decision; the scorecard and the post-run wakes reference it.

Version `/2` commits the delivery inputs with the settle fact. Startup and the
ordinary clock may finish arming its missing one-shot wakes and returning its
departed allowances. This is recovery of an already signed intent, not a new
settlement or run generation. Existing trigger catalogs and completed delivery
records prevent repeated turns; existing deterministic refund identities prevent
repeated credits. Recovery uses the original acceptance-facts hash and any
already recorded scorecard. If interruption preceded the scorecard write, the
scorecard reference remains unavailable; recovery does not present a newly
computed observation as the original one. A complete armed observation closes
the arming work. Historical `/1` remains readable without automatic reconstruction
of delivery inputs that version never recorded.

## 5. The run scorecard

`personaos-run-scorecard/2` records factual joins at settlement and rides the
existing `RUN_SCORECARD_RECORDED` task-lineage carrier. Exact members are
registered in [the schema registry](registry/SCHEMAS.md). The counters cover:

| Observed family | Evidence and limits |
|---|---|
| Identity records authored | Signed identity evolution during the run; no competence inference. |
| Capabilities mounted, surfaces invoked, library generations on an executing path | Sealed generations and exact invocation/receipt joins. Availability on a search path is distinct from invocation. |
| Acquisition attempts, refusals and unrecorded outcomes | Dispatcher observations and acquisition receipts. An unpaired sealed generation is an explicitly unrecorded outcome; this bounds over-counting rather than inventing a successful use. |
| Birth proposals, admissions, bound refusals and invitations | Exact population events. Admission alone does not demonstrate a useful contribution. |
| Funded post-run wakes and unreached members | Exact intake/supplementary reservations joined to settlement membership. |
| Acceptance contracts, verifier/execution receipts, repeated execution references, cohort recommendations and principal acceptances | The independent authority rules of 03 §9; a recommendation is not principal acceptance. |
| Counterparty wakes with an effect | A wake-context carriage followed by recipient publication/declaration before its next carriage. This temporal join alone does not prove useful cooperation. |
| Compactions stated | Durable turn compaction observations. |

The record names its environment, task, run, settle event, members, time window,
evidence ids and unreadable sources. A resumed generation retains the task
family's observed start. An unreadable source makes dependent counters absent
and names them in `unavailable_counters`; absence is never reported as zero.
The scorecard is shown through the existing compact and kernel-signed public
projections, with no thresholds, targets or behavior recommendations.

Removed counters include per-rule declines, unnamed-member penalties, lessons
written/bound and repeated refusal without a lesson. The placeholder count for
semantic capability-gap statements is removed. Memory availability, learning
benefit and useful cooperation require separate evidence over actual work;
they cannot be inferred from a write, binding, invocation or publication count.

## 6. Acceptance interplay

### 6.1 The condition of record

When the principal supplies an `acceptance_condition`, that condition is the
condition of record for the task. Every cohort acceptance contract authored
for the task MUST bind `principal_condition_hash`; a receipt scoped to a
contract inherits that binding, and the acceptance mint reads it from the
contract event already among its joins — no frozen receipt or mint record
gains a member. A cohort contract MAY add bars; its text is carried beside the
principal's and never replaces it. The verifier declaration synthesised from a
cohort contract ([`14_DECISIONS.md` ADR-0097](14_DECISIONS.md#adr-0097--cohort-contracts-confer-verifier-authority))
MUST inherit every supplied principal member — the condition, the rewake
bound, the provenance floor, the deadline — and MAY supply only the verifier
predicate the principal left absent. A receipt scoped to a contract that does
not bind the principal's condition hash carries no acceptance standing and
states so on its face.

When the principal supplies no condition there is no condition of record:
each live contract adjudicates its own text, every receipt's standing names
the contract it joined, and `principal_condition_hash` is absent — never an
empty string. The condition of record is the latest supplied
`acceptance_condition` in the task's causal ancestry; the kernel binds its
hash on every contract authored while it exists (the persona supplies no
hash). A contract bound to an earlier hash, or to none, keeps standing only
for receipts recorded before the amendment that changed it — the era rule of
[`03_TASKS.md §9`](03_TASKS.md#9-objective-acceptance) — and confers none
after. A condition prices outcomes with values: it names no tool class, no
author and no third-party origin — the principal's standing rule, which
ADR-0112 dec 4 applies to the verifier descriptor's authorship clause; the
substrate cannot enforce this on prose and does not try.

### 6.2 Cohort acceptance is a recommendation

A cohort acceptance record is the cohort's signed recommendation over an
exact byte state. It closes no task, retires no principal carrier, settles no
paused mission, and cancels no ladder; the projection reports it as the fact
`cohort_recommended`. A task closes by acceptance only through exact
authenticated principal acceptance, a receipt qualified under a
principal-declared verifier descriptor whose
`verifier_receipt_constitutes_acceptance` is true, or another
principal-declared mechanism ([`00_VISION.md §3` J11](00_VISION.md#j11--explicit-acceptance-authority)).
This restores ADR-0097's "a cohort can qualify verdicts and never extend one
into acceptance by itself" and reverses the closing-state decision of
ADR-0108. A task with no principal in the loop therefore rests at
`cohort_recommended`: quiescent, open, and one principal action from closed.
The task's owner bearer MAY accept through the ordinary principal acceptance
authority; the UI shows the recommendation, who signed
it, and the condition it adjudicated, so that action is informed. Quiescence
remains nonterminal (J10) and costs nothing.

### 6.3 Principal-declared verification capability

A principal MAY declare, as its verifier descriptor, the exact member set
`{kind, scope, capability_generation_ref}` with `kind` exactly
`"principal-capability/1"` and `capability_generation_ref` the exact
generation manifest hash of a sealed content-addressed generation
([`08_KNOWLEDGE.md §5`](08_KNOWLEDGE.md#5-persona-owned-capability-material-and-executable-tools)).
Under it a receipt extends into acceptance only when the three predicate-mode
invariants of [`03_TASKS.md §9`](03_TASKS.md#9-objective-acceptance) hold for
a registered persona identity signer, `verifier_receipt_constitutes_acceptance`
is true, and the signer's host-sealed executed evidence includes at least one
environment-tool invocation dispatched to that generation's mounted surface
([`09_PROTOCOLS.md §2.2`](09_PROTOCOLS.md#22-persona-navigation))
— a dispatch fact, never path availability: a generation on an execution's
search path is joined, not used, and a verifier that runs an unrelated
command after the mount has not executed through the instrument. The join is
over sealed identifiers, never over tool names, output text, or who mounted
the generation; because the generation is content-addressed, a same-named
mount cannot shadow it. A surfaceless (library-only) generation cannot be
named by this kind: with no surface there is no dispatch to record. Whether a deployment may mount a generation through
its own ingress is a separate decision (OQ-PLATFORM-4); until then a
principal names a generation that exists, whoever mounted it. This is J11's
"principal-declared mechanism", not a substrate constraint on adjudication.

### 6.4 Resume follows causality

A paused mission resumes only on an authentic causal delivery: a principal
event, a resource grant, one of the two prepaid replay stimulus classes, a
peer delivery, or a persona-authored wake. The post-run distillation wake is
a turn of the settled run, not a resume ([`03_TASKS.md §10`](03_TASKS.md#10-quiescence-and-terminal-authority)). No heartbeat, sweep, or housekeeping pass re-queues a mission whose
members have all authored `no_successor`; doing so manufactures work J9
forbids. This narrows ADR-0111's settle gate to its J9 form: the gate keys on
the absence of pending authentic deliveries, not on any acceptance state.

## 7. Verification evidence

Offline verification follows authenticated wake admission through malformed
action feedback, a corrected action, exact artifact bytes and explicit turn
end. It also follows peer snapshot review, memory revision after contrary
evidence, restart/transfer, budget conservation, newborn consent/funding and
private/public presentation. Provider request bytes are evidence of carriage;
scripted model output is not evidence of emergent behavior.

Live evaluation uses independent task evaluators outside the platform. Matched
memory comparisons run only in labelled isolated copies. Personas retain their
authored state; runtime memory selection remains persona-owned. Campaign
acceptance is a release assessment, never a runtime quota or a semantic gate.

## 8. Risks & known limitations

- Factual counts can accompany useless work. Inspect delivered bytes and
  independent checks, including negative cases.
- Lossy compaction can discard a useful observation. Keep exact retrieval and
  evaluate the same correctness cases with and without compaction.
- Schema feedback can teach an incorrect procedure. Preserve branch-specific
  constraints and the exact diagnosis in audit records and the next request.
- Learning reservations consume declared run resources. Show the debit and
  allow the principal's existing reservation setting, including zero.

## 9. Open questions

Whether observed memory or character causes better choices requires controlled
comparisons that account for task, tools, budget and contrary evidence. A persona's
explanation is an authored claim. Whether the deployment should gain a direct
provisioning ingress remains open (OQ-PLATFORM-4); it is not added by this change.

## 10. Design criteria

1. Exact deployment-signed charter and principal intent reach every request.
2. Signed scorecards report available facts and explicitly name missing evidence.
3. Principal acceptance authority is preserved; cohort recommendations close nothing.
4. One existing prepaid post-run opportunity carries exact sources and the
   complete ordinary catalogue without requiring a memory write.
5. Personas choose actions, memory and identity revisions; no compliance counter
   controls execution, funding, routing or acceptance.
6. The UI distinguishes authored claims, observed effects and principal acceptance.

## 11. Cross-references

[`00_VISION.md`](00_VISION.md) §2, §3 J9/J11, §5, §10 · [`02_PERSONA.md §3`](02_PERSONA.md#3-optional-public-identity) ·
[`03_TASKS.md`](03_TASKS.md) §1, §7, §8, §9, §10, §12 · [`05_ENVIRONMENT.md`](05_ENVIRONMENT.md) ·
[`08_KNOWLEDGE.md`](08_KNOWLEDGE.md) §5, §6 · [`09_PROTOCOLS.md`](09_PROTOCOLS.md) §2.2, §13, §14 ·
[`11_DESIGN_CRITERIA.md`](11_DESIGN_CRITERIA.md) C-OP-3, C-OP-8, C-OP-15, C-OP-16 · [`13_DESIGN_VALIDATION.md §18`](13_DESIGN_VALIDATION.md#18-platform-requirements-condition-of-record-and-scorecard) ·
[`14_DECISIONS.md`](14_DECISIONS.md) ADR-0097, ADR-0108, ADR-0111, ADR-0112 · [`16_POPULATION_DYNAMICS.md §11`](16_POPULATION_DYNAMICS.md#11-removed-compatibility-surface) ·
[`19_PERSONA_WORK_STATE.md §2`](19_PERSONA_WORK_STATE.md#2-optional-append-only-authored-observation).
