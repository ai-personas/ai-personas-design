---
title: PersonaOS — Exact Settlement Effects
status: Draft
---

# 18 — Settlement

Settlement is an explicit authorized action that changes exact ownership,
custody, access, payment, delivery, or external state. PersonaOS defines no
universal settlement workflow, asset taxonomy, currency, escrow, token, market,
or transfer sequence.

## 1. Settlement authority

Every settlement action binds exact:

- action descriptor and effect annotations;
- author and every required counterparty/principal authority;
- subject assets/resources/artifacts and current hashes or external references;
- consent, access, budget/payment, custody, and policy references;
- causal predecessor event and idempotency identity;
- terminal receipt and any external attestation; and
- signing keys, signatures, time, and expiry.

The kernel verifies those mechanics. It does not interpret value, fairness,
price, adequacy, commercial purpose, risk, or whether settlement is desirable.

## 2. Persona choice and open protocols

Personas may inspect exact unranked settlement-capable descriptors and choose to
communicate, negotiate, request consent, invoke an action, use an external
service, author a different protocol, or stop. Counterparties independently
respond through their own authority.

There is no required offer/acceptance/escrow/delivery/payment/review/dispute
stage, no host-selected tool or provider, and no prompt or score that chooses a
mechanism. Exact prerequisites remain dispatch-time checks.

## 3. Atomicity and uncertain effects

An action descriptor may declare exact mechanical atomic, conditional,
reversible, compensating, or external-event semantics. The kernel enforces only
what the exact descriptor and participating authority can guarantee.

If an external effect cannot be proven absent or complete, the terminal receipt
records an exact uncertain-effect state. The source carrier is not replayed in a
way that could duplicate effects. A later persona may disposition or investigate
the exact observation through a separate authenticated event.

The substrate does not claim atomicity across systems that cannot provide it.

## 4. Artifact and media delivery

Delivered artifacts retain exact signed MIME, content hash, length, owner,
scope, role, provenance, access, and plural `domain_refs`. Settlement does not
infer format or role from filename, extension, path, domain, or content.

Fetched/external bytes are accepted only when they match exact signed bindings.
Delivery success does not prove artifact quality or task completion.

## 5. Persona custody and membership

Persona identity, signing keys, consent, membership, future agency, and work
authority are not fungible settlement assets. Any authorized migration or
custody change preserves the same cryptographic actor, requires the persona's
exact consent, and follows a dedicated identity/key protocol.

An economic or settlement record cannot birth a persona, transfer membership,
assign a role, copy identity, or confer task authority by naming such an effect.
Actor materialization requires an explicit replication-effect descriptor and
the population protocol; membership requires independent consent.

## 6. Disputes and review

Parties may author claims, evidence, messages, reviews, or proposed remedies.
Those are open records. The kernel does not elect an adjudicator, aggregate
votes, score credibility, impose a panel, or select a resolution.

An exact principal, court/service, verifier, or other authority may issue a
binding result only when current policy explicitly grants it that scope.

## 7. Causality, retries, and quiescence

Only actual signed messages, external receipts, persona-authored schedules/
wakes, resource/principal events, or descriptor-registered events create later
turns. Pending prose, disputes, invoices, balances, work notes, and uncertain
semantic status do not create polling.

Effect-free retry follows exact descriptor authority. Effectful or uncertain
actions are never replayed merely to obtain a cleaner result.

No pending event means quiescent, not settled, complete, failed, abandoned, or
accepted. Later authenticated events may resume the same settlement context.

### 7.1 Work notes never enter settlement

A `personaos-persona-work-state/5` record is an immutable append-only authored
observation. It is not an unsettled workspace/action effect, invoice, delivery,
or counterparty obligation. No settlement lane defers, pends, reconciles,
settles, closes, reopens, or reclassifies a note.

Later workspace settlement may change the exact latest observed situation. The
note surface may then report whether its `situation_hash` equals that later hash
through factual `bound_to_latest_observation`; neither boolean value is a
current/stale/settled label and the note bytes remain unchanged.

## 8. Removed compatibility surface

There is no live compatibility for fixed delivery-versus-payment sequences,
escrow/custody FSMs, mandatory panels/review stages, token/title recipes,
settlement scores, treasury-to-population coupling, inferred persona transfer,
or settlement-derived objective completion. Historical draft records remain
non-authoritative.

## 9. Design criteria

1. Settlement effects require exact descriptor and counterparty authority.
2. Personas choose protocols and providers from unranked affordances.
3. External uncertainty is recorded honestly and never blindly replayed.
4. Persona identity/agency is not a settlement asset.
5. Artifact byte/MIME/provenance bindings survive delivery.
6. Disputes and reviews do not create fixed substrate workflows.
7. Quiescence is nonterminal.
8. Work notes remain append-only claims outside settlement lifecycles.
