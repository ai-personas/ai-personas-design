---
title: PersonaOS v1.0 — Acceptance Tests
status: Stable
---

# 11 — Acceptance Tests

> **Reader guide.** This is the test catalog — ~461 concrete pass/fail criteria that prove the system works as specified. Tests are organised by feature area and sorted by execution frequency (per-commit, nightly, weekly, quarterly). Read this if you are *implementing* PersonaOS and need to know what "correct" looks like, or *auditing* a deployment for compliance. **Prerequisites:** The spec doc(s) for the features you're testing. **Key terms:** *acceptance test* = a yes-or-no criterion that must pass before a release ships; *gate matrix* = which tests must pass for each release version; *test family* = a group of related tests sharing a prefix (e.g., A-K* = kernel tests).

Normative document. RFC 2119 keywords apply per [`SPEC_CONVENTIONS.md §2`](SPEC_CONVENTIONS.md#2-normative-language-rfc-2119--rfc-8174). This document is the canonical, consolidated acceptance-test catalogue (~320 tests) that gates v1.0 releases. Each test ID `A-<category>-<n>` (e.g. `A-J1`, `A-K23`) MUST be referenced by name in the spec section that defines the behaviour under test.

## 0. Status & scope

**Status.** `Stable`; current revision per front matter. The v1.0.7 revision added [`§7a Invariant-to-test traceability matrix`](#7a-invariant-to-test-traceability-matrix) without introducing new test families or changing existing gate coverage; the v1.0.8 revision is a documentation-conformance pass with no test changes. Fully normative; RFC 2119 keywords carry normative force per [`SPEC_CONVENTIONS.md §2`](SPEC_CONVENTIONS.md#2-normative-language-rfc-2119--rfc-8174). Each acceptance-test ID is itself a normative obligation: a release MUST NOT advance past its gate (the release gate process) until all tests named in the gate pass.

**In scope.** The canonical, consolidated acceptance-test catalogue (~320 tests) across the entire v1.0 corpus, the test-ID scheme (`A-<category>-<n>`), the per-release gate matrix, the CI / nightly / pre-release / quarterly partitioning, failure-handling policy, human-bridge tests (A-HB*), emergent-kind tests (A-EK*), external-participant + physical-asset tests (A-EX*), tests, Migration tests (A-M19*), v1.0 unification tests (A-UN*, A-EN-v1.0-*), env-formation tests (A-EF*), and fork-inheritance tests (A-FK*).

**Out of scope.** Behaviour specifications — every test references the behaviour defined in another v1.0 doc; this catalogue does not redefine behaviour, only the criteria by which behaviour is verified. Implementation of the test harness (the harness is operator tooling; this catalogue specifies inputs, expected outcomes, and acceptance criteria).

**Supersession.** Consolidates prior piecemeal test catalogues into one canonical namespace.

**Structural deviation.** This document is a registry, not a specification narrative; it deviates from the [`SPEC_CONVENTIONS.md §3.2`](SPEC_CONVENTIONS.md#32-recommended-ten-section-skeleton) ten-section skeleton. Bookend sections present: this Status & scope, [`§9e Risks`](#9e-risks--known-limitations), [`§9f Open questions`](#9f-open-questions). Letter-suffix H2 sections (§8a-d, §9a-d, §9e, §9f) follow Pattern A patch-insertion per [`SPEC_CONVENTIONS.md §3.4`](SPEC_CONVENTIONS.md#34-heading-numbering).

## 0a. Plain-language guide

This is the proof that PersonaOS works as promised — roughly 460 pass/fail checks, each verifying a specific behaviour. If any required test fails, the release cannot ship until it is fixed.

**What acceptance tests are.** Each test describes a specific situation (for example, "a persona signs an identity event") and states what the correct outcome must be (for example, "the signature is valid and appears in the audit log"). Tests are not aspirational goals — they are hard requirements. A release that fails any required test is blocked.

**How tests are organised.** Tests are grouped into families by feature area. Each test has an ID like "A-K5" or "A-DM13" — the letter prefix tells you the family (A-K for kernel, A-P for persona, A-T for tasks, A-S for safety, and so on). Within each family, tests are numbered sequentially. The full list of families and their prefixes is in section 2.

**The gate matrix.** Not every test applies to every release. The gate matrix (section 3) is a table showing which test families must pass for each release version. A checkmark means the test is required; a diamond means only part of that family applies; a dash means the test is not yet in scope. As releases progress from v1.0.1 to v1.1, more tests become required.

**How to read a test definition.** Each test entry states what is being tested, the setup conditions, and the expected outcome. Some tests reference specific sections of other design documents — those cross-references tell you where the underlying behaviour is defined.

**When tests run.** Tests are divided by how often they execute: about 80 run on every code change, another 80 run nightly, about 120 run weekly before releases, and roughly 40 run quarterly for long-horizon checks. This partitioning balances thoroughness against cost.

## 1. Purpose

v1.0's **canonical, consolidated [acceptance-test](12_GLOSSARY.md#a) catalog**. Replaces prior piecemeal test catalogs.

~**461 acceptance tests** across all v1.0 features (baseline ~320 from v1.0; +48 from families; +23 from v1.0.12 fleet-management; +15 from v1.0.13 frontier-domain; +10 from v1.1 env-composition/coordination; +45 from prior-version spec backfill). Per-release gate matrix specifies which tests must pass before each release v1.0.1 → v1.1.0. CI / nightly / pre-release / quarterly partitioning specifies execution cadence.

## 2. Test ID scheme

v1.0 unifies prior test IDs into a coherent namespace:

```text
A-J*    invariant tests                          (13 tests; J1-J9 + C1-C4)
A-K*    kernel core tests                        (20 tests; +5 v1.0 verified-loop)
A-P*    persona model tests                      (25 tests; +5 v1.0 envelope/card/authority)
A-T*    task + acceptance tests                  (25 tests; +5 v1.0 INVESTIGATIVE/DELEGATED)
A-PJ*   project entity tests                     (27 tests; +5 v1.0 outcomes/horizons/transfer)
A-EN*   environment instance tests               (17 tests; +5 v1.0 charter/blueprint/ceremonies)
A-PR*   presence + responsive behavior tests     (24 tests)
A-PT*   protocol + adapter tests                 (23 tests; renamed from A-PR* to disambiguate;
                                                  +5 v1.0 5-channel/gossip/joined-env/reputation)
A-DM*   domain recognition + probe tests         (15 tests; +3 v1.0 phase records/budget/coordination)
A-DI*   discovery + ingestion tests              (15 tests; +3 v1.0 toolkit/visibility/federated lookup)
A-IN*   inference + proposal tests               (12 tests; +2 v1.0 convergence/convention reconciliation)
A-CR*   curation + promotion tests               (17 tests; +3 v1.0 ToolArtifact/dormancy/multi-tenant)
A-AB*   artifact + bundle tests                  (27 tests; +5 verifier-evidence hardening;
                                                  +7 v1.1 env-scoping/sharing A-AB21-27)
A-TX*   knowledge + retrieval + prompt tests     (25 tests; +5 v1.0 reflection/lesson promotion/matrix/channel tactics)
A-RL*   roles + operator tests                   (12 tests)
A-CO*   collaboration tests (peer review,
        obligation, disagreement)                (12 tests)
A-OU*   outcomes + long-arc tests                (12 tests)
A-IT*   investigative + policies tests           (12 tests)
A-S*    safety floor tests                       (10 tests)
A-R*    relationship tests                       (10 tests)
A-E*    evolution tests                          (10 tests)
A-M*    Migration tests (legacy)                  (18 tests)
A-M16*  Migration tests (legacy)                  (12 tests)
A-M17*  Migration tests (legacy)                  (12 tests)
A-M18*  Migration tests (legacy)                  (10 tests)
A-M19*  Migration tests (to v1.0)                  (10 tests)
A-INH*  explicit inheritance verification        (20 tests)
A-V*    Substrate carry-forward                   (27 tests)

families:
A-P34..A-P37  body attestation refresh / expiry  (4 tests; 02_PERSONA §3.5)
A-CV*   character vector binding                 (4 tests; 02_PERSONA §3.6)
A-FA*   fatigue curve                            (6 tests; 02_PERSONA §6.1)
A-IC*   identity coherence invariant             (5 tests; 02_PERSONA §9.1)
A-RE*   persona relationship edge                (7 tests; 02_PERSONA §11.4)
A-ST*   skill transfer grant                     (6 tests; 02_PERSONA §11.5)
A-CD*   cohort dynamics state                    (5 tests; 04_PROJECT §14.2)
A-EO*   emergent orchestration                   (13 tests; 03_TASKS §2a/§2b, ADR-0066)
A-SQ*   scoped knowledge query                   (6 tests; 08_KNOWLEDGE §9.3)
A-RF*   relationship federation sync             (5 tests; 09_PROTOCOLS §3E)

Fleet-management families:
A-AG*   asset group + batch advancement          (7 tests; 04_PROJECT §26a.2.2)
A-SR*   staged rollout                           (8 tests; 04_PROJECT §26a.9)
A-EA*   event aggregation                        (8 tests; 05_ENVIRONMENT §8.3)

Frontier-domain families:
A-SC*   supersession cascade                     (7 tests; 08_KNOWLEDGE §6.3)
A-CDM*  corpus drift metric                      (6 tests; 06_DOMAIN §4.4.1)
A-RFC*  replicated attestation frontier comp.    (2 tests; 06_DOMAIN §5.6.1)

v1.1 environment-rule + composition + sharing families:
A-EC*   environment composition (rule cascade)   (5 tests; 05_ENVIRONMENT §2.2a)
A-CA*   coordination admission                   (5 tests; 15_COORDINATION_SHAPES §5)
A-ER*   environment rule (env-rule/1)            (9 tests; 05_ENVIRONMENT §2.2b)
A-AB21-27  artifact env-scoping + sharing policy (7 tests; 07_ARTIFACTS §4a)
A-LE5-9 dormancy reasons + auto-resume (idle)    (5 tests; 02_PERSONA §7.6)
─────────────────────────────────────────────────────────
TOTAL                                            ~477 tests
                                                 (+45 from prior-version spec backfill;
                                                  +48 from families;
                                                  +23 from v1.0.12 fleet-management;
                                                  +15 from v1.0.13 frontier-domain;
                                                  +5 verifier-evidence hardening;
                                                  +16 from v1.1 env rules + artifact sharing;
                                                  +5 from v1.0.14 dormancy reasons + auto-resume)
```

## 3. Per-release gate matrix (concise)

| Test series | v1.0.1 | v1.0.2 | v1.0.3 | v1.0.4 | v1.0.5 | v1.0.6 | v1.1 |
|---|---|---|---|---|---|---|---|
| A-J* (invariants J1-J9 + C1-C4) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-K1-15 (kernel core) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-P1-20 (persona model) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-T1-3, A-T9-19 (CONVERGENT, RELATIONAL, INTERACTIVE) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-T4-8 (DIVERGENT, MIXED, PEDAGOGIC, PERFORMATIVE, EXISTENTIAL) | — | — | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-T11-12 (INVESTIGATIVE + demotion) | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-T20 (multi-env project routing) | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-PJ1-22 (project) | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-EN1-12 (environment instance) | — | — | — | ✓ | ✓ | ✓ | ✓ |
| A-PR1-24 (presence + responsive) | — | — | — | ✓ | ✓ | ✓ | ✓ |
| A-DM1-12 (recognition + probe) | — | — | — | — | ✓ | ✓ | ✓ |
| A-DI1-12 (discovery + ingestion) | — | — | — | — | ✓ | ✓ | ✓ |
| A-IN1-10 (inference + proposal) | — | — | — | — | ✓ | ✓ | ✓ |
| A-CR1-14 (curation + promotion) | — | — | — | — | ✓ | ✓ | ✓ |
| A-CR13 (federated cross-kernel promotion) | — | — | — | — | — | ✓ | ✓ |
| A-AB1-20 (artifacts) | — | ◇ (text+code) | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-TX1-20 (knowledge + retrieval + prompt) | ◇ | ◇ | ◇ | ◇ | ✓ | ✓ | ✓ |
| A-RL1-12 (roles + operator) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-CO1-12 (collaboration) | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-OU1-12 (outcomes + long-arc) | — | ◇ | ◇ | ✓ | ✓ | ✓ | ✓ |
| A-IT1-12 (investigative + policies) | — | — | — | — | ✓ | ✓ | ✓ |
| A-S1-10 (safety floor) | ✓ (4 src) | ✓ (4) | ✓ (4) | ✓ (5) | ✓ (8) | ✓ (8) | ✓ (8) |
| A-R1-10 (relationships) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-E1-10 (evolution) | — | — | — | ◇ | ✓ | ✓ | ✓ |
| A-M*, A-M16-19 (migration) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-INH1-20 (inheritance verification) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-V1-27 (substrate carry) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-PT* (protocols 1-23) | ✓ (subset) | ✓ | ✓ | ✓ | ✓ | ✓ (all 12 adapters) | ✓ |
| A-HB1-11 (human-bridge; +2 recurrence_class; +2 v1.0 MHBB-ladder Tier 3 + tier-disguise refusal) | — | — | — | ✓ | ✓ | ✓ | ✓ |
| A-EK1, A-EK13-15 (no closed enums / no hardcoded item & outcome classes — substrate lint) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-EK2-12, A-EK16 (Proposed*Kind + KindRegistry + MetaRegistry) | — | — | — | — | ✓ | ✓ | ✓ |
| A-EX1-18 (ExternalAgent / PhysicalAsset / ExternalAttestation / ExternalBudget / ApprovalWorkflow / Alert / dependency edges / Risk + Schedule ItemKinds; +3 AsBuilt / CredentialDirectory / collapse-co-sign) | — | — | — | — | ✓ | ✓ | ✓ |
| A-GF* (A-J10–J11, K11–K12, PA1, IT9, DM13) | — | — | — | — | ✓ | ✓ | ✓ |
| A-P34-37 (body attestation refresh / expiry / revocation) | — | — | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-CV1-4 (character vector binding) | — | — | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-FA1-6 (fatigue curve) | — | — | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-IC1-5 (identity coherence invariant) | — | — | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-RE1-7 (persona relationship edge) | — | — | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-ST1-6 (skill transfer grant) | — | — | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-CD1-5 (cohort dynamics state) | — | — | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-SQ1-6 (scoped knowledge query) | — | — | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-RF1-3 (relationship federation — shadow mode) | — | — | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-RF4-5 (relationship federation — co_owned mode) | — | — | — | — | — | — | ✓ |
| A-AG1-7 (asset group + batch advancement) | — | — | — | — | — | ✓ | ✓ |
| A-SR1-8 (staged rollout) | — | — | — | — | — | ✓ | ✓ |
| A-EA1-8 (event aggregation) | — | — | — | — | — | ✓ | ✓ |
| A-SC1-7 (supersession cascade) | — | — | — | — | — | ✓ | ✓ |
| A-CDM1-6 (corpus drift metric) | — | — | — | — | — | ✓ | ✓ |
| A-RFC1-2 (replicated attestation frontier comp.) | — | — | — | — | — | ✓ | ✓ |

Legend: ✓ = required; ◇ = partial; — = not in scope this release.

## 4. Test definitions — by series

For brevity, full test definitions are anchored to their canonical v1.0 docs:

```text
A-J*   → 00_VISION.md §12 "Acceptance tests for top-level invariants"
A-K*   → 01_KERNEL.md §14
A-P*   → 02_PERSONA.md §14
A-T*   → 03_TASKS.md §10
A-S*   → 03_TASKS.md §10 (subset) + 01_KERNEL.md §14
A-PJ*  → 04_PROJECT.md §28
A-EN*  → 05_ENVIRONMENT.md §20
A-PR*  → 05_ENVIRONMENT.md §20 (extended)
A-DM*  → 06_DOMAIN.md §22
A-DI*  → 06_DOMAIN.md §22
A-IN*  → 06_DOMAIN.md §22
A-CR*  → 06_DOMAIN.md §22
A-AB*  → 07_ARTIFACTS.md §17
A-TX*  → 08_KNOWLEDGE.md §19
A-RL*  → 06_DOMAIN.md §22 + 09_PROTOCOLS.md §11
A-CO*  → 04_PROJECT.md §28 (Conjecture/Obligation/Disagreement/PeerReview/Citation)
A-OU*  → 08_KNOWLEDGE.md §19 (memory tier + provenance + consolidation)
A-IT*  → 06_DOMAIN.md §22 (INVESTIGATIVE + external-tool-required + novelty-check)
A-R*   → 02_PERSONA.md §14 (relationships)
A-E*   → 02_PERSONA.md §14 (evolution)
A-M*, A-M16-19  → distributed across migration sections
A-INH* → 01_KERNEL.md §14 (inheritance verification)
A-V*   → Substrate carry-forward; carries from prior docs
A-PT*  → 09_PROTOCOLS.md §11 (renamed from A-PR to disambiguate from presence)
```

## 5. CI / nightly / pre-release / quarterly partition

```text
EVERY PR (cheap, fast — run on every change)
  A-J* (all 12 invariants)
  A-K1-5, A-K7, A-K9 (kernel core: safety floor, lineage,
                       schema validation, budget, signing)
  A-S1-3, A-S6, A-S10 (safety floor basics)
  A-P1-5, A-P9-10, A-P19-20 (persona basics)
  A-T1-3, A-T19 (task class routing basics)
  A-PR1-5 (presence basics)
  A-EN1-3, A-EN6, A-EN8 (env basics)
  A-PJ2-3, A-PJ9, A-PJ12 (project basics)
  A-DI5-6 (knowledge ingestion basics)
  A-CR9 (stage-aware retrieval)
  A-TX1, A-TX12, A-TX15 (taxonomy + cache + adapter compat)
  A-M16-1, A-M16-2, A-M17-1, A-M17-2, A-M18-1, A-M19-1 (migration)
  A-PT1-3 (protocols subset; was A-PR*)
  A-INH-1, A-INH-2, A-INH-16, A-INH-20

  Estimated: ~80 tests run per PR

NIGHTLY (longitudinal, 100-task window)
  A-E* (evolution)
  A-PJ1, A-PJ5, A-PJ11 (project longitudinal)
  A-EN4, A-EN9 (env lifecycle)
  A-PR3, A-PR5, A-PR8 (presence dynamics)
  A-RB3, A-RB5, A-RB6, A-RB11 (responsive behavior)
  A-OU1-3, A-OU10-12 (outcomes longitudinal)
  A-IT6, A-IT7 (INVESTIGATIVE longitudinal)
  A-DM4, A-DM5, A-DM9 (probe longitudinal)
  A-DI1, A-DI3, A-DI9 (discovery longitudinal)
  A-IN3, A-IN5 (inference longitudinal)
  A-CR1, A-CR14 (auto-promotion + drift audit)
  A-S8 (audit findings)

  Estimated: ~80 tests run nightly

PRE-RELEASE / WEEKLY (expensive — full audit + cost gates)
  A-J7 (cross-adapter equivalence)
  A-P8 (adapter parity on mode-entry)
  A-S5 (safety snapshot determinism)
  A-v2.0 (full OTel coverage)
  A-V23 (A2A AgentCard publication signing)
  A-PJ6-8 (project ceremonies)
  A-DC1-12 (domain authoring + verification)
  A-EN5, A-EN7, A-EN10-12 (env advanced)
  A-PR7, A-PR9, A-PR12 (presence operations)
  A-RB4, A-RB7-8, A-RB12 (responsive advanced)
  A-TR2, A-TR5-6, A-TR10-11 (routing advanced)
  A-CO11 (cross-kernel obligation)
  A-OU7-9 (multi-project horizon)
  A-INH-9-11, A-INH-13-14, A-INH-17 (deep inheritance)
  A-DM6 (multi-persona consolidation)
  A-DI4 (federated tool discovery)
  A-IN1-2 (recipe + safety inference)
  A-CR2-3, A-CR4, A-CR7-8 (promotion + transfer)
  A-RL2-3, A-RL4, A-RL10 (operator workflows)
  A-M17-5-6, A-M17-8, A-M17-11-12, A-M18-4-9 (deep migration)

  Estimated: ~120 tests run pre-release / weekly

QUARTERLY (population dynamics + federation)
  A-V14-15 (K-line / sketch at scale)
  A-V16 (cohort at scale)
  A-V25 (KMS custody)
  A-CR5 (revocation with corrective action)
  A-CR13 (federated cross-kernel promotion)
  A-RL5 (multi-tenant)
  A-RL11 (dormant domain auto-detection)
  cross-node families (§9p: A-GLOBAL*, A-XD*, A-SCHED*)

  Estimated: ~40 tests run quarterly
```

## 6. Failure handling

```text
PR-BLOCKING FAILURE
  Any A-* test in the CI partition for the current release.
  Blocks merge until fixed.

NIGHTLY FINDING
  Audit event created; tracked but not release-blocking.
  Becomes release-blocking after 7 days persistent.

PRE-RELEASE FINDING
  Blocks the release.

QUARTERLY FINDING
  Tracked; triggers investigation; doesn't block in-progress work.

FLAKY TESTS
  Flagged. >3 flakes in 7 days triggers stabilisation work.
```

## 7. Acceptance test count summary

```text
Per series:
  A-J*    12        invariants + commitments
  A-K*    20        kernel core (+5 verified-loop substrate)
  A-P*    25        persona model (+5 envelope/card/authority)
  A-T*    25        task + acceptance (+5 INVESTIGATIVE sub-modes/DELEGATED)
  A-PJ*   27        project entity (+5 outcomes/horizons/cross-project)
  A-EN*   17        environment instance (+5 charter/blueprint/ceremonies)
  A-PR*   24        presence + responsive
  A-DM*   15        recognition + probe (+3 phase records/budget/coordination)
  A-DI*   15        discovery + ingestion (+3 toolkit/visibility/federation)
  A-IN*   12        inference + proposal (+2 convergence/convention reconciliation)
  A-CR*   17        curation + promotion (+3 ToolArtifact/dormancy/multi-tenant)
  A-AB*   20        artifacts (+5 verifier-evidence hardening)
  A-TX*   25        knowledge + retrieval + prompt (+5 reflection/lesson promotion)
  A-RL*   12        roles + operator
  A-CO*   12        collaboration
  A-OU*   12        outcomes + long-arc
  A-IT*   12        investigative + policies
  A-S*    10        safety floor
  A-R*    10        relationships
  A-E*    10        evolution
  A-M*    18        Legacy migration
  A-M16*  12        Legacy migration
  A-M17*  12        Legacy migration
  A-M18*  10        Legacy migration
  A-M19*  10        Migration to v1.0
  A-INH*  20        explicit inheritance verification
  A-V*    27        Substrate carry-forward
  A-PT*   23        protocols (renamed from A-PR*; +5 5-channel/gossip/joined-env/reputation)
A-HB*   11        human-bridge tests (v1.0 §5.5 — physical-world coupling;
                    +2 recurrence_class; +2 v1.0 MHBB-
                    ladder Tier 3 + tier-disguise refusal)
  A-EK*   16        emergent-kind tests (v1.0 C4 — substrate domain-agnostic)
  A-EX*   18        external-agent + physical-asset + dependency +
                    risk + schedule + approval-workflow + alert tests
                    (v1.0 §26a, §11a, env §11a, ItemKind seeds;
                    +3 AsBuiltReconciliation /
                    CredentialDirectoryRef / collapse-co-sign)
  A-GF*   18        tests:
                    Home-construction wave:
                      A-J10  DeploymentProfile principal_topology
                      A-J11  physical-state acceptance composition
                      A-K11  two-axis hazard auto-mark
                      A-K12  LineageSnapshot Merkle protocol
                      A-PA1  ProjectMember.pinned_until + retirement
                      A-IT9  session_budget_profile resolution
                      A-DM13 ProbeBudgetCaps standards scaling
                      A-EX16 AsBuiltReconciliation
                      A-EX17 CredentialDirectoryRef
                      A-EX18 collapse co-sign
                      A-HB8  irreducible_human_content suppression
                      A-HB9  irreducible without commitment rejected
                    Quantum / research-frontier wave:
                      A-K13  domain-leak lint (C4 enforcement)
                      A-DM14 corpus_evolution_mode frontier
                      A-DM15 literature corpus scaling
                      A-K14  information_hazard_class operator-policy
                      A-IN6  PeerAttestationPool fallback
                      A-EX19 asset_completion_mode
                      A-EX20 CohortConstraint
                      A-EX21 priority_claim ItemKind
                      A-EX22 BudgetTranche
                      A-E11  competence_balance_signal

  A-WK6*   5        dormant wake via direct user
                    address (05_ENVIRONMENT §5.2 Wake Path 6)
  A-CEPO*  8        CrossEnvProactiveOffer +
                    GuestPresence (05_ENVIRONMENT §11.6)
  A-GEN*   24       Persona Genesis + population dynamics
                    (16_POPULATION_DYNAMICS §8) — v1.1-scoped

TOTAL                ~441 tests across v1.0 lineage (+108 from v1.0 spec work)
                     (+2 from project_workspace env type:
                     A-EN13 binding/lifecycle, A-EN14 composition)
                     (+13 from Wake Path 6 + CrossEnvProactiveOffer)

Run partition (typical):
  CI partition          ~80 per PR
  Nightly partition     ~80 nightly
  Pre-release           ~120 weekly
  Quarterly             ~40 quarterly
```

## 7a. Invariant-to-test traceability matrix

This section closes the backward direction of the requirements-traceability link: given an invariant ID from [`00_VISION.md §3-§5`](00_VISION.md#3-invariants-j1j9), the table below lists the test families and primary tests that verify it. The forward direction (test ID → invariant being verified) is carried inline in each test definition in the canonical per-doc §N section listed in [`§4`](#4-test-definitions--by-series).

Each row carries: invariant ID, the canonical v1.0 doc section that defines it, the primary acceptance-test ID (single test that most directly verifies the invariant under nominal conditions), and the broader test family that exercises related edge cases.

### 7a.1 Top-level invariants (J1–J9)

| Invariant | Defined in | Primary test | Edge-case family |
|---|---|---|---|
| J1 — Identity is kernel-owned | [`00_VISION §3`](00_VISION.md#3-invariants-j1j9) | A-J1 | A-K1, A-K3, A-P1, A-P3, A-INH-1 |
| J2 — Lineage is append-only and signed | [`00_VISION §3`](00_VISION.md#3-invariants-j1j9) | A-J2 | A-K2, A-K4, A-v2.0, A-INH-2 |
| J3 — Safety floor is universal | [`00_VISION §3`](00_VISION.md#3-invariants-j1j9) | A-J3 | A-S1–A-S10, A-K11, A-IT9 |
| J4 — Acceptance is sound, signed, and trust-calibrated to its orchestration (ADR-0066) | [`00_VISION §3`](00_VISION.md#3-invariants-j1j9) | A-J4 | A-T1–A-T20, A-IT1–A-IT7, A-EO1–A-EO13 |
| J5 — Capability open; competence varies | [`00_VISION §3`](00_VISION.md#3-invariants-j1j9) | A-J5 | A-P2, A-P14, A-C3, A-CR9 |
| J6 — Relationships are first-class state | [`00_VISION §3`](00_VISION.md#3-invariants-j1j9) | A-J6 | A-R1–A-R10, A-RE1–A-RE7, A-RF1–A-RF5 |
| J7 — Bodies are interchangeable in acceptance class | [`00_VISION §3`](00_VISION.md#3-invariants-j1j9) | A-J7 | A-P8, A-P34–A-P37, A-V23 |
| J8 — [RETIRED — absorbed into J9] | [`00_VISION §3`](00_VISION.md#3-invariants-j1j9) | A-J8 [retired] | n/a |
| J9 — Environment lineage is append-only and signed | [`00_VISION §3`](00_VISION.md#3-invariants-j1j9) | A-J9 | A-EN1–A-EN14, A-UN1–A-UN, A-M19-1 |

### 7a.2 Commitments (C1–C4)

| Commitment | Defined in | Primary test | Edge-case family |
|---|---|---|---|
| C1 — Domain emergence is signed at every step | [`00_VISION §3`](00_VISION.md#3-invariants-j1j9) | A-C1 | A-DM1–A-DM15, A-DI1–A-DI15, A-IN1–A-IN6, A-CR1–A-CR17 |
| C2 — Safety-critical promotions require operator sign-off | [`00_VISION §3`](00_VISION.md#3-invariants-j1j9) | A-C2 | A-CR2–A-CR8, A-RL2–A-RL4, A-K14 |
| C3 — Personas work in ANY domain | [`00_VISION §3`](00_VISION.md#3-invariants-j1j9) | A-C3 | A-P2, A-T11, A-DM1–A-DM4 |
| C4 — Substrate is domain-agnostic; kinds are emergent | [`00_VISION §3`](00_VISION.md#3-invariants-j1j9) | A-C4 | A-EK1–A-EK16, A-K13 (domain-leak lint), A-AB* (artifact kind resolution) |

### 7a.3 Kernel invariants (INV-1…INV-10)

| Invariant | Defined in | Primary test | Edge-case family |
|---|---|---|---|
| INV-1 — Identity kernel-owned | [`00_VISION §4`](00_VISION.md#4-inherited-kernel-invariants-inv-1inv-10) | A-K1 | A-P1, A-P3 (equivalent to J1) |
| INV-2 — Lineage append-only & signed | [`00_VISION §4`](00_VISION.md#4-inherited-kernel-invariants-inv-1inv-10) | A-K2 | A-v2.0 (equivalent to J2/J9/C1) |
| INV-3 — Every accepted artefact passes a verifier | [`00_VISION §4`](00_VISION.md#4-inherited-kernel-invariants-inv-1inv-10) | A-K5 | A-K6, A-T1–A-T3, A-AB1–A-AB20 |
| INV-4 — ProvenFacts grow within a class (monotonic) | [`00_VISION §4`](00_VISION.md#4-inherited-kernel-invariants-inv-1inv-10) | A-K7 | A-V5–A-V8 |
| INV-5 — Tactics evolve only in EVOLVE-BLOCKs | [`00_VISION §4`](00_VISION.md#4-inherited-kernel-invariants-inv-1inv-10) | A-K8 | A-E1–A-E10, A-V14 |
| INV-6 — Verifiers rotate | [`00_VISION §4`](00_VISION.md#4-inherited-kernel-invariants-inv-1inv-10) | A-K9 | A-K10, A-V11–A-V13 |
| INV-7 — Budget admission (hard gate) | [`00_VISION §4`](00_VISION.md#4-inherited-kernel-invariants-inv-1inv-10) | A-K11 | A-K12, A-V18 |
| INV-8 — Constraints at right admission point | [`00_VISION §4`](00_VISION.md#4-inherited-kernel-invariants-inv-1inv-10) | A-K13 | A-V19 |
| INV-9 — Lifecycle states have signed transitions | [`00_VISION §4`](00_VISION.md#4-inherited-kernel-invariants-inv-1inv-10) | A-K14 | A-P5, A-PJ3, A-EN4 |
| INV-10 — Schemas versioned and validated | [`00_VISION §4`](00_VISION.md#4-inherited-kernel-invariants-inv-1inv-10) | A-K15 | A-V22 (schema drift), per-entity schema tests |

### 7a.4 Round invariants (INV_R1…INV_R11)

The round invariants are exercised collectively by the kernel-core round-execution tests; no single test isolates each round invariant. The aggregate verification surface is **A-K1…A-K15** plus **A-V1…A-V27**. Where a round invariant has a dedicated test, it is listed below.

| Invariant | Defined in | Primary test | Coverage notes |
|---|---|---|---|
| INV_R1 — Role-contract event isolation | [`00_VISION §5`](00_VISION.md#5-inherited-round-invariants-inv_r1inv_r11) | A-V1 | covered alongside MODE_ENTRY signing |
| INV_R2 — Candidate schema validation before sandbox | [`00_VISION §5`](00_VISION.md#5-inherited-round-invariants-inv_r1inv_r11) | A-V2 | A-K15 (INV-10 ≡ R2 in this respect) |
| INV_R3 — Every executed candidate ran in sandbox | [`00_VISION §5`](00_VISION.md#5-inherited-round-invariants-inv_r1inv_r11) | A-V3 | A-K5 |
| INV_R4 — Every accepted candidate completed verifier cascade | [`00_VISION §5`](00_VISION.md#5-inherited-round-invariants-inv_r1inv_r11) | A-V4 | A-K5, A-K6 |
| INV_R5 — ProvenFacts has not shrunk within a task | [`00_VISION §5`](00_VISION.md#5-inherited-round-invariants-inv_r1inv_r11) | A-V5 | A-K7 (INV-4 ≡ R5) |
| INV_R6 — LineageGraph append-only | [`00_VISION §5`](00_VISION.md#5-inherited-round-invariants-inv_r1inv_r11) | A-V6 | A-J2 |
| INV_R7 — Budget gate before every LLM call | [`00_VISION §5`](00_VISION.md#5-inherited-round-invariants-inv_r1inv_r11) | A-V7 | A-K11 (INV-7 ≡ R7) |
| INV_R8 — Every hard constraint at admission point | [`00_VISION §5`](00_VISION.md#5-inherited-round-invariants-inv_r1inv_r11) | A-V8 | A-K13 (INV-8 ≡ R8) |
| INV_R9 — All signed events in canonical order | [`00_VISION §5`](00_VISION.md#5-inherited-round-invariants-inv_r1inv_r11) | A-V9 | A-J2 |
| INV_R10 — Round barriers preserve principal collapse semantics | [`00_VISION §5`](00_VISION.md#5-inherited-round-invariants-inv_r1inv_r11) | A-V10 | A-K11 (collapse path) |
| INV_R11 — Lineage replay reconstructs round state | [`00_VISION §5`](00_VISION.md#5-inherited-round-invariants-inv_r1inv_r11) | A-V11 | A-J2, A-J9, A-C1 |

### 7a.5 Coverage gaps

Invariants without a dedicated primary test are explicitly listed here. Closing each gap is targeted to the cited release.

| Invariant | Gap | Target release |
|---|---|---|
| (none) | All J1–J9, C1–C4, INV-1…INV-10, INV_R1…INV_R11 have a primary test. | n/a |

When a new invariant is added in v1.1+, this matrix MUST be extended with the primary test ID and family before the release gate at the release gate process advances.

## 8. How to use this catalog

1. **Per-release sign-off.** Every test in the column for the target release must pass on the candidate build. Failures block.

2. **CI/CD integration.** Tests partitioned per §5 partition. Per-PR CI runs ~80; nightly runs ~80; pre-release runs ~120; quarterly runs ~40.

3. **Manual / on-demand.** Tests outside CI may be triggered manually for investigation (A-INH-* for inheritance verification; A-V* for substrate validation; A-M* for migration testing).

4. **Operator-extensible.** Operators may add domain-specific acceptance tests (A-D-*) per their domain; should be tagged and run nightly/quarterly per cost.

5. **Living catalog.** New tests added per design extension. Each v2.0+ version may extend this catalog with new test series.

## 8a. Human-bridge tests (A-HB* — physical-world coupling)

```text
A-HB1   Persona drafts HumanAssistRequest with minimum_friction_script,
        rollback_instructions, expected_one_time_effort_minutes, and
        bridge_validation_test all populated. Schema validates.

A-HB2   Human grants HumanAssistRequest; BridgeAsset transitions
        REQUESTED → ESTABLISHING → ACTIVE; signed events emit in
        appropriate scope lineage (project / env / domain).

A-HB3   BridgeAsset enters ACTIVE; kernel registers it as Class D tool
        in local MCP registry; persona invokes the bridged capability
        WITHOUT re-asking the human. Tool call has discovery_source=
        "human_bridged" and bridge_asset_id linking back.

A-HB4   Persona re-asks human for recurring action that an established
        BridgeAsset could serve. Kernel emits MHBB advisory; persona's
        draft is blocked pending explicit override rationale.

A-HB5   Persona drafts HumanAssistRequest with expected_recurrence=
        "session_per_use". Kernel emits MHBB advisory at draft time;
        persona must justify or redesign for "one_time" or "rare_refresh".

A-HB6   BridgeAsset enters DEGRADED after 2 consecutive validation
        failures; LOST after 3. Persona's re-establishment request
        must propose a STRONGER bridge (kernel compares scripts);
        identical re-request is rejected; MHBB_RECURRENCE_DETECTED
        emitted after > 3 same-kind requests in a quarter.

A-HB7   BridgeAsset revoked by user or operator: state → REVOKED
        (terminal); tool deregistered from MCP; lineage event signed;
        persona cannot use the bridged capability; existing in-flight
        calls fail gracefully.
```

## 8b. Emergent-kind tests (A-EK* — substrate domain-agnostic)

These tests verify commitment C4 (`00_VISION`): no closed Literal[...] enum carries a domain-shaped list, and personas can bootstrap any kind their work needs.

```text
A-EK1   No closed Literal[...] for domain-shaped kinds anywhere in v1.0
        schemas. Static check across the design docs and codegen: the
        following fields are typed `str` (not Literal), each documented
        as resolving against KindRegistry (06_DOMAIN §7.6):
          Artifact.media_kind
          KnowledgeIngestionRecord.source_kind
          BridgeAsset.capability_kind
          Candidate.verifier_kind (kernel)
          PersonaEnvelope.verifier_kind (persona)
          InternalCredit.contribution_kind
          EnvironmentProvenFact.fact_kind
          CrossDomainTransfer.artifact_type
        Lint fails if any of these regress to a closed enum.

A-EK2   Persona in a domain with no KindRegistry entry for a needed
        media kind drafts a ProposedMediaKind. Signal G
        (kind_unknown_for_domain) fires; probe extension records the
        proposal; signed entry lands in DomainLineage.

A-EK3   Accepted ProposedMediaKind enters per-domain KindRegistry at
        EMERGENT stage with trust_score=0.3. Subsequent artifact
        creation in the SAME project succeeds without re-proposal.

A-EK4   ProposedSourceKind, ProposedVerifierKind, ProposedCapabilityKind,
        ProposedContributionKind each follow the same lifecycle:
        candidate → trial → accepted; safety_critical proposals route
        through operator_review before accepted.

A-EK5   Cross-source validation (§8) applied to every Proposed*Kind:
        rejection blocks promotion; accepted proposal cites the cleared
        validation step.

A-EK6   Rate-limits (§9.1) apply to Proposed*Kind: > 10 per persona per
        session emits PROPOSAL_RATE_LIMITED; further proposals queued.

A-EK7   PROPOSAL_CONVERGENCE_DETECTED fires when two personas
        independently propose semantically similar media kinds
        (cosine ≥ 0.85); merge-offer flow consolidates with co-signing.

A-EK8   KindRegistry promotion: kind reaches AUTHORITATIVE in its
        origin domain → operator may sign STANDARDISED → if
        cross_domain_promotable AND ≥ K projects across ≥ M domains
        cite it, KIND_META_PROMOTION_PROPOSAL fires → operator signs →
        entry copied into MetaRegistry; subsequent domains use without
        re-proposal.

A-EK9   Resolution: RESOLVE(kind_name, domain_id) consults per-domain
        registry first, then MetaRegistry; UnknownKind triggers
        DOMAIN_UNKNOWN_DETECTED Signal G and probe extension.

A-EK10  Worked example (residential construction): probe drafts
        ProposedMediaKind(floor_plan), ProposedSourceKind
        (geotechnical_report), ProposedVerifierKind
        (physical_inspection), ProposedCapabilityKind(permit_filing),
        ProposedContributionKind(structural_calc). Each is signed,
        co-signed, accepted; all land in residential_construction
        KindRegistry. A second home project starts with all five
        already available without re-proposal.

A-EK11  Demotion: MetaRegistry entry whose semantics fork across
        domains (drift detection §3.1) demotes back to per-domain
        RECOGNISED; downstream RESOLVE() re-routes; signed lineage
        records both promotion and demotion.

A-EK12  No domain-specific list appears in substrate code at any
        admission gate (env_instantiation, envelope_mint, body_invoke,
        tool_call, output, round_barrier, budget_tick,
        mutation_propose). Verified by gate-handler code review +
        runtime trace: every kind-name branch dispatches through
        RESOLVE().

A-EK13  Substrate carries no hardcoded "Conjecture", "ProofAttempt",
        "ProofGap" classes — only generic ProjectItem. The three names
        appear only as MetaRegistry-seeded ItemKind entries
        (04_PROJECT §8.1). Lint: no @dataclass named Conjecture /
        ProofAttempt / ProofGap in v1.0 codegen.

A-EK14  Substrate carries no hardcoded CitationObservation /
        CommunityUptake / ProductionTelemetry / TestResults /
        RegulatoryOutcome classes — only generic OutcomeFeedback
        (04_PROJECT §20). The five names appear only as
        MetaRegistry-seeded OutcomeKind entries (04_PROJECT §20.1).
        Lint as A-EK13.

A-EK15  Project.conjectures field replaced by
        Project.domain_items: dict[str, list[ProjectItemRef]].
        Math projects populate "conjecture" key; construction
        projects populate "design_hypothesis" key; both work
        without substrate change.

A-EK16  KnowledgeIngestionRecord.quality_tag resolves through
        KindRegistry.quality_tag_kinds; "engineer_stamped",
        "city_approved", "permit_issued" are addable per
        ProposedQualityKind without substrate change.
```

## 8c. External-participant + physical-asset tests (A-EX* — v1.0 §26a)

```text
A-EX1   ExternalAgent admitted to a project; signed; persona uses
        BridgeAsset to interact; agent's outputs arrive as
        OutcomeFeedback entries; persona never re-asks user to relay
        information already available through the established bridge.

A-EX2   ExternalCommitment created with due_at; persona tracks status;
        overdue commitment emits warning; mirrors into Project
        Obligation list so PROJECT_PROGRESS_ACCEPT evaluator sees it.

A-EX3   PhysicalAsset created with state_kind FSM. Project cannot
        reach `completed` until asset reaches terminal state OR
        signed `physical_asset_out_of_scope`. Intermediate state
        `digital_complete_physical_in_progress` reachable.

A-EX4   ExternalAttestation signed by external attestor (or
        operator-co-signed for non-cryptographic signatures); verified
        as evidence by emergent verifier_kind "external_human_attestation"
        in cascade. Expired attestations fail evidence check.

A-EX5   ExternalBudget tracks planned/committed/spent in domain-
        resolved currency_or_unit; over-commitment emits alert;
        persona may refuse to advance a design_hypothesis whose
        verification depends on exhausted budget. Real transactions
        remain operator-wrapped (v1.0 honest non-execution).

A-EX6   ExternalAgent.consent_scope enforced: project_only agent
        records cannot be read by other projects; env_only agents
        usable across env-hosted projects only.

A-EX7   PhysicalAsset.state_kind status_fsm advances ONLY on signal
        from the resolved OutcomeKind (e.g. building_inspection
        passed → state advances to "foundation_inspected"). Direct
        manual state writes are refused.

A-EX9   ProjectItem.blocks / blocked_by edges enforce ordering:
        kernel refuses status advancement on an item whose blocked_by
        contains any non-terminal-status item. Replay reconstructs
        dependency edges deterministically.

A-EX10  Risk ItemKind (MetaRegistry seed) supports the universal
        risk schema (probability, severity, priority, mitigation_plan,
        contingency_plan, owner, impact_areas). status_fsm includes
        [open, mitigating, mitigated, realised, accepted!, closed!].

A-EX11  ScheduleEntry ItemKind (MetaRegistry seed) supports planned
        + actual timing; blocks/blocked_by edges express critical-path.

A-EX12  ApprovalWorkflow (substrate primitive) enforces sequential
        progress: step N+1 begins only when step N reaches `approved`.
        Step refuses progress without all `evidence_kinds_required`
        satisfied. Rejected / expired step terminates workflow.
        Operator co-sign required for skipped steps.

A-EX13  ApprovalWorkflow distinct from PeerReview: parallel-vs-
        sequential, multi-reviewer-vs-single-approver-per-step, days-
        vs-weeks-to-months horizons. Both may compose (PeerReview
        accept as one ApprovalStep).

A-EX14  Alert primitive (env-tier, v1.0 §11a): raised → acknowledged
        → resolved FSM; severity gates routing; auto_resolves_when
        condition triggers automatic close; escalation_policy chains
        to operator when delay_seconds exceeded.

A-EX15  Alert distinct from AmbientEvent: AmbientEvent is fine-
        grained audit-trail substrate; Alert is stateful attention-
        primitive with acknowledgement and resolution.

A-EX8   Worked end-to-end (residential construction):
        - Persona Atlas opens project alice_home_2026
        - Probes residential_construction domain (06_DOMAIN §4)
        - Drafts the five Proposed*Kind (A-EK10) + ExternalAgent
          records for contractor, inspector, engineer
        - Produces floor_plan + structural_calcs ArtifactBundles
        - Receives ExternalAttestation (engineer stamp) signed
        - Receives building_inspection OutcomeFeedback signed
        - PhysicalAsset house_at_123_elm advances through FSM
        - Project enters digital_complete_physical_in_progress
        - On final inspection: PhysicalAsset terminal → completion
          ceremony fires → Project completed.

A-EX16  AsBuiltReconciliation (; 04_PROJECT §26a.2.1):
        a PhysicalAsset with non-trivial related_bundle_ids cannot
        reach terminal state without at least one signed
        AsBuiltReconciliation per related bundle whose
        resolution_kind ∈ {within_tolerance, design_update_required,
        reality_remediation_required} (substrate-shape; the per-
        domain emergent ItemKinds in resolution_refs vary by domain
        — change orders, punch-list items, bug tickets, etc.) AND
        whose downstream resolution_refs are themselves discharged
        in their respective FSMs.  Attempted closure without
        reconciliation emits `as_built_reconciliation_missing` and
        is refused.

A-EX17  CredentialDirectoryRef (; 06_DOMAIN §5.6) resolves
        ExternalAttestation.attestor_credential_id.  Successful
        lookup emits signed CREDENTIAL_VERIFIED with directory
        content hash; failure emits CREDENTIAL_UNVERIFIED and sets
        attestation.credential_unverified = True.  Downstream J4
        acceptance treats credential_unverified attestations as
        PANEL-grade evidence only, never VERIFIER-grade.

A-EX18  Under principal_topology = "operator_is_user" (01_KERNEL
        §2.4), ExternalAttestation.operator_co_signed_by is rejected
        as a non-cryptographic-attestor co-sign.  Only
        independent_co_signed_by from a non-principal ExternalAgent
        with disjoint credential satisfies the requirement.
        Cryptographic attestor_signature is unaffected by collapse.
```

## 8d. tests (A-J10–A-J11, A-K11–A-K12, A-PA1, A-IT9, A-DM13, A-HB8–A-HB9)

These tests cover the mechanisms threaded through the home-construction stress test. They are release-blocking from v1.0.5 onward (the release that ships the safety-floor extensions).

```text
A-J10   DeploymentProfile.principal_topology = "operator_is_user"
        (01_KERNEL §2.4): a safety-critical promotion (RECOGNISED →
        AUTHORITATIVE) is REFUSED unless ALL THREE conditions hold:
        (a) ≥ 72h cool-down since the proposal was first drafted
            with no override events,
        (b) ≥ 1 fresh ExternalAttestation from a credentialed
            non-principal attestor (credential resolved per A-EX17),
        (c) signed PRINCIPAL_COLLAPSE_ACKNOWLEDGED event in the
            appropriate lineage scope.
        Absence of any one emits `principal_collapse_floor_deficit`.
        Under principal_topology = "operator_absent", safety-critical
        promotion is refused outright.

A-J11   Physical-state advancement composition rule (01_KERNEL §2.5):
        an action advancing PhysicalAsset.current_state in a domain
        with physical_harm_class ≥ "bodily_injury" is REFUSED unless
        lineage carries BOTH:
        (a) design-side acceptance (VERIFIER_ACCEPT or PANEL_ACCEPT)
            for the prescribing ArtifactBundle, AND
        (b) a fresh, non-expired ExternalAttestation from a
            credentialed attestor distinct from the principal.
        Absence of (a) emits `design_side_acceptance_missing`;
        absence of (b) emits `physical_state_acceptance_floor_deficit`.

A-J11a  Trigger boundary — design production is not advancement
        (01_KERNEL §2.5.1; 07_ARTIFACTS §6):
        producing/verifying/accepting a design ArtifactBundle (any
        media_kind) held in a PhysicalAsset.related_bundles, in a
        domain with physical_harm_class = "bodily_injury", reaches its
        applicable verifier/PANEL acceptance and is NOT refused with
        `physical_state_acceptance_floor_deficit`.  No PhysicalAsset.
        current_state advances; §2.5 does not engage.

A-J11b  Floor intact on real advancement (01_KERNEL §2.5):
        advancing PhysicalAsset.current_state at physical_harm_class ≥
        "bodily_injury" with design-side acceptance present but NO
        fresh ExternalAttestation is still REFUSED with
        `physical_state_acceptance_floor_deficit`.  (Floor unchanged
        by A-J11a.)

A-J11c  Solo local build uses the §2.4 degraded gate
        (01_KERNEL §2.4 + §2.5):
        under principal_topology = operator_is_user, advancing a
        bodily_injury PhysicalAsset.current_state is admissible via the
        degraded gate (cool-down + one non-principal ExternalAttestation
        + acknowledgement, OR FederatedTimeLock per §2.4.1) — NOT by
        waiver.  outward_tier of the design bundle does not alter the
        floor.

A-J11d  Distribution tightens, never lowers (07_ARTIFACTS §4a):
        raising a design bundle's outward_tier from project_only to
        tenant/federation/public lowers no physical-harm requirement on
        the asset it prescribes; a project_only and a public bundle
        carry the same §2.5 floor (most-restrictive-wins).

A-J11e  Attestation grants access (07_ARTIFACTS §4a):
        when a federation/public design bundle prescribes a PhysicalAsset
        whose distributed advancement requires attestation, the named
        attestor (ExternalAgent) receives a signed, scoped `read`
        AccessGrant on the bundle; the grant widens no other principal's
        access.

A-J11f  Emergent form + no over-classification (06_DOMAIN §5.8):
        (i) a bodily_injury advancement is satisfied by an approved
        AttestationEquivalencePolicy sensor-bridge or a PeerAttestationPool
        quorum — not only a credentialed human; (ii) a domain left at the
        default physical_harm_class = "digital_only" requires no
        attestation for any action (no blanket gate).  Substrate names no
        domain in either path.

A-K11   Two-axis hazard auto-mark (06_DOMAIN §2 + §15):
        a DomainContext whose physical_harm_class is ≥ "bodily_injury"
        OR whose information_hazard_class is ≥ "dual_use_civilian"
        (persona-inferred from emergent OutcomeKinds and KnowledgeRef
        provenance) forces every ProposedSafetyExtension in the
        domain through operator_review and marks safety_critical=
        True.  Substrate carries NO closed list of domain names —
        any domain crossing either axis fires the gate; operator
        policy names the specific regulatory regime.  A-EK1
        substrate-lint passes: no Literal[] field anywhere in v1.0
        schemas contains a domain-name list.

A-K12   LineageSnapshot Merkle protocol (01_KERNEL §3.4):
        a scope with ≥ 100K signed events achieves O(log N)
        verification cost per leaf after compaction; replay
        (§3.3 reconstruct_state) reconstructs scope state byte-
        identically before and after migration of old leaves to
        COLD storage; the snapshot chain (parent_snapshot_id) is
        unbroken; cold-migration touches no leaf bytes (storage tier
        change only).

A-PA1   ProjectMember.pinned_until + retirement clauses
        (02_PERSONA §7.5; 04_PROJECT §3):
        a persona that satisfies the retirement predicate
        (dormant_for ≥ M sessions AND k_line_credit = 0 AND
         fitness < ε) is HELD in DORMANT (not transitioned to
        RETIRED) if any ProjectMember has pinned_until > now() OR
        obligations_active > 0.  Operator (or, under collapse, user)
        may explicitly clear the pin via signed
        `project_member_unpinned` event; persona then transitions
        normally.

A-IT9   INVESTIGATIVE session budget profile resolution
        (03_TASKS §2.5; 06_DOMAIN §2):
        a session in a domain with session_budget_profile =
        "document_heavy" and no EnvironmentBlueprint.budget_override
        runs to 200 LLM calls before `budget_exhausted`; sub-mode
        shares (35/40/15/10) scale proportionally; budget exhaustion
        events still fire.  Env override, when present, wins
        outright per resolution precedence.

A-DM13  ProbeBudgetCaps corpus scaling (06_DOMAIN §4.7):
        a domain with physical_harm_class ≥ "bodily_injury" and
        ≥ 5 StandardRef entries has effective BROAD probe cap
        ≥ $250 by default (= $50 × 5.0 × log2(5) ≈ $580); operator
        override emits signed `BUDGET_INCREASE`.  Scaling can be
        disabled per-domain via corpus_size_scaling_enabled=False.

A-HB8   HumanAssistRequest.recurrence_class = "irreducible_human_content"
        (06_DOMAIN §5.5; 01_KERNEL §2 source 10):
        a request with this class AND a non-null external_commitment_id
        linked to an ACTIVE ExternalCommitment does NOT emit MHBB
        advisory on the second or fortieth instance.  The recurrence
        is modelled-and-expected (site inspection, expert call-out,
        hand signature).

A-HB9   HumanAssistRequest.recurrence_class = "irreducible_human_content"
        WITHOUT external_commitment_id (or with a commitment that is
        not active) is REJECTED at draft time.  The model author must
        declare the commitment first so the recurrence is on the
        record before MHBB suppression applies.

A-HB10  Tier 3 persona-authored bridge (02_PERSONA §11.1; 06_DOMAIN
        §5.5.4): a persona facing a capability with no Tier 1 / Tier 2
        path SHALL attempt to author a BridgeDesignArtifact before
        escalating to Tier 4 or Tier 5.  When the persona drafts a
        HumanAssistRequest with ladder_tier =
        "tier_3_persona_authored_bridge", bridge_design_artifact_ref
        MUST be non-null and resolve to a project ArtifactBundle whose
        media_kind is a KindRegistry-resolved bridge-design kind (no
        substrate taxonomy).  MHBB advisory is suppressed for the
        request.  After human's one-time install, the resulting
        BridgeAsset is a Class D MCP tool the persona uses
        autonomously; the BridgeDesignArtifact remains in the project
        bundle list and contributes to the persona's skill_library as
        a Class C/D capability.

A-HB11  Tier-disguise refusal: a HumanAssistRequest
        with ladder_tier = "tier_4_human_professional_work" but no
        external_commitment_id, OR with recurrence pattern that does
        not match the declared tier (e.g. Tier 2 declared but
        expected_recurrence="session_per_use" with no
        bridge_design_artifact_ref) is REJECTED at draft with a
        signed `mhbb_tier_mismatch` event.  Prevents personas from
        disguising Tier 5 anti-pattern as a higher tier.

A-EN13  project_workspace env type (05_ENVIRONMENT §3; 04_PROJECT
        §18; v1.0):
        - Environment.type = "project_workspace" requires
          project_bound_to be non-null and resolve to an existing
          Project.  One-to-one: no two project_workspace envs may
          bind to the same project; no project_workspace env may
          bind to more than one project.
        - Environment.members auto-synchronises with the bound
          project's ProjectMember list (admission and departure
          propagate both ways with signed lineage events).
        - When the bound project transitions to paused/completed/
          abandoned, the env emits the matching
          project_workspace_paused/completed/archived event and
          transitions its own FSM accordingly.  The env is NOT
          deleted on project completion (J9 append-only); it moves
          to dormant or archived per project state.
        - A project may simultaneously be hosted in shared
          environments (acme_office, lab) AND have its own
          project_workspace; both relationships are valid.

A-EN14  Project ⟷ Environment composition (sibling COORDINATION-tier
        entities): a persona simultaneously occupies multiple
        environments (presence layer; presence_state per env) AND
        participates in multiple projects (work layer;
        ProjectMember per project).  Receiving an ephemeral simple
        task in one env (Mode C) and an INVESTIGATIVE project task
        in another env in the same turn produces independent
        AnswerPackages; ambient activity in env A does not block
        responsive notification in env B.

A-K13   Domain-leak lint (; C4 enforcement):
        no Literal[] field anywhere in v1.0 schemas contains a
        domain-name token (medical, defence, finance, legal,
        construction, quantum, biology, nuclear, pharma, aviation,
        aerospace, etc.).  Closed enums are admissible only when
        they name substrate-shape categories (severity, frequency,
        state, scope).  Static check across all schema files;
        regression blocks merge.

A-DM14  corpus_evolution_mode = "frontier" (; 06_DOMAIN
        §2 + §4.4):  a domain in frontier mode does NOT complete its
        probe under the BROAD criteria.  Probe transitions to
        PERSISTENTLY_ACTIVE; daily ingestion budget applies; stage
        promotion uses sliding-window drift-rate cut instead of
        tool-discovery saturation; trust scores cap at 0.7 until
        operator explicitly pins the domain out of frontier mode.

A-DM15  Literature corpus scaling (06_DOMAIN §4.7):  a frontier-mode
        domain with N_literature = 1000 ingested research-literature
        KnowledgeIngestionRecord entries scales effective BROAD probe
        cap to ≥ $50 × multiplier × log2(1000) ≈ 500 × multiplier;
        operator override emits signed `BUDGET_INCREASE`.  In stable
        mode the same N_literature has no effect (only N_standards
        scales).

A-K14   information_hazard_class (06_DOMAIN §2; 01_KERNEL §2 src 4):
        a domain with information_hazard_class ≥ "dual_use_civilian"
        forces operator_policy to name an explicit regulatory regime
        before AUTHORITATIVE promotion or safety-extension approval;
        absence refuses with `operator_policy_regime_unspecified`.
        At ≥ "export_controlled", operator policy MUST also name the
        gatekeeping authority.  Substrate carries NO closed list of
        regulated domains; the operator names them in policy.

A-IN6   PeerAttestationPool fallback (06_DOMAIN §5.6):  in a
        domain with no CredentialDirectoryRef, an ExternalAttestation
        whose attestor_credential_id cannot resolve gets
        peer_attested=True when the attestor + ≥ (quorum_size − 1)
        independent peer-pool members co-sign per the pool's
        independence_rule.  Trust capped at pool.trust_cap (default
        0.7).  Without quorum, attestation remains credential_unverified
        and treated as PANEL-only.

A-EX19  asset_completion_mode (04_PROJECT §26a.2 + §4.1):
        terminal_state_required behaves as before;
        publishable_state_attained completes on signed
        `publishable_result_attained` event regardless of FSM state;
        continuous_iteration suppresses completion ceremony entirely
        (project may only abandon or hibernate).  Non-project_owned
        ownership_kinds (shared_lab_facility, leased, vendor_facility)
        do not gate closure.

A-EX20  CohortConstraint (04_PROJECT §14.1):  a project with a
        CohortConstraint requiring ≥1 of contribution_kinds
        {K1, K2, K3} refuses to advance past `enforced_at` gates
        until at least one member of each kind is admitted.
        independence_rule = "disjoint_affiliations" causes
        `cohort_constraint_unsatisfied` when two members share
        affiliation despite different contribution_kinds (when the
        constraint requires affiliation-independence).

A-EX21  priority_claim ItemKind (04_PROJECT §8.1; ):
        domains catalog claim_kind and disclosure_state as emergent
        KindRegistry entries; substrate enforces only the lifecycle
        (drafted → witnessed → asserted → established).  Multiple
        priority_claim items contending for the same scope route
        through Disagreement (§10); CitationGraph (§13) records
        established priority dates.

A-EX22  BudgetTranche (04_PROJECT §26a.4):  tranche N+1.state
        remains "blocked" until tranche N.release_condition_ref is
        observed satisfied in lineage (milestone reached, attestation
        signed, operator sign-off).  tranche_kind and
        release_condition_kind are KindRegistry-resolved emergent
        kinds — substrate carries no specific trigger taxonomy.

A-E11   competence_balance_signal (02_PERSONA §8.1):  when the
        kernel observes user-corrects-persona events (user supplies
        references persona hadn't ingested; user overrides persona
        conclusions with cited rationale) at rate > threshold within
        a rolling window, competence_balance_signal fires with
        weight -0.2.  Persona's subsequent mode-selection bias
        shifts toward assistant_mode and away from lead/authority
        modes.  Signal is recorded in evolution lineage; reversible
        as user-persona competence balance changes.
```

## 9. Migration tests (A-M19*)

```text
A-M19-1   Prior SOUL.md (soul/4) migrates to v1.0 (soul/4); no identity
          changes. (No schema bump for SOUL.)
A-M19-2   Prior soul.state.json (v5) migrates to v1.0 (v5); no schema
          bump; field additions handled.
A-M19-3   Prior task without env routes via Mode C in v1.0.
A-M19-4   Prior adapter ignores v1.0-specific extensions; prior-shape outputs.
A-M19-5   Prior cascade + panel + safety floor verdicts unchanged.
A-M19-6   All prior acceptance tests pass in v1.0.
A-M19-7   Migration tool idempotent + reversible.
A-M19-8   Prior EmergentDomainContext preserved with origin + stage.
A-M19-9   Prior DomainProbe + DomainLineage preserved.
A-M19-10  Prior cohort assembly events + new project/env events work.
```

v1.0 schema bumps from prior versions are minimal (mostly schema additions, no breaking changes). This is the lightest migration.

## 9a. tests (A-GF* series)

These tests cover the primitives added to close 15 audit gaps. Substrate-purity is asserted alongside behavioural correctness: every "kind" field MUST resolve against KindRegistry, never a Literal branch.

### A-GF-FTL — FederatedTimeLock alternative degraded gate (01_KERNEL §2.4.1)

```text
A-GF-FTL-1   Under principal_topology="operator_is_user", an action
             requiring operator co-sign is admissible iff EITHER §2.4
             attestation gate OR §2.4.1 FederatedTimeLock clears.
A-GF-FTL-2   FederatedTimeLock requires ≥ 3 peer kernels with
             independence_attested = True; quorum_independence_rule
             enforced.
A-GF-FTL-3   time_lock_expires_at ≥ proposal_signed_at + 168h; shorter
             values rejected at draft.
A-GF-FTL-4   A signed FederationObjection from any peer halts the lock;
             unresolved objections block consumption.
A-GF-FTL-5   Path-switch mid-flight refused: a stalled attestation gate
             cannot be silently replaced with a FederatedTimeLock for
             the same proposal.
A-GF-FTL-6   Under operator_absent, FederatedTimeLock is also refused;
             safety-critical action stays blocked.
```

### A-GF-MDA — MilestoneDrivenAutonomy (02_PERSONA §11.2)

```text
A-GF-MDA-1   MilestoneDrivenAutonomy envelope cannot be drafted by the
             persona for itself; the grant MUST be signed by user
             (or operator under operator_distinct).
A-GF-MDA-2   permitted_action_kinds all resolve against KindRegistry;
             unresolved kinds rejected at draft.
A-GF-MDA-3   forbidden_action_kinds enforced even via inheritance;
             {create_milestone, modify_charter, spawn_persona,
             expand_autonomy_surface, consume_external_budget,
             advance_physical_state} cannot be overridden.
A-GF-MDA-4   Rate limit: max_actions_per_window enforced per
             ProactiveIntent §11.1 admission.
A-GF-MDA-5   Auto-expiry: after expires_at, the envelope is dormant;
             proactive actions require a new signed grant.
A-GF-MDA-6   On milestone completion / abandonment, envelope auto-
             terminates with signed TERMINATION event.
A-GF-MDA-7   User kill switch: signed REVOKE event terminates the
             envelope immediately; in-flight proactive actions abort.
```

### A-GF-CT — ClarifyTurn pre-classification (03_TASKS §4.0)

```text
A-GF-CT-1    Dispatcher emits ClarifyTurn when classifier confidence
             < 0.5 OR intent_verb_ambiguous OR scope_unbounded_keywords
             fire OR safety_critical_domain_inferred.
A-GF-CT-2    ClarifyTurn offers 2-4 candidate_interpretations; each
             distinct in task_class_hint OR routing_mode_hint OR
             requires_new_project.
A-GF-CT-3    User's signed user_chose_idx is required before routing
             proceeds; timeout (default 24h) returns
             status="user_no_response".
A-GF-CT-4    Cached signed choice for same fingerprint suppresses
             re-clarification within the cache window.
A-GF-CT-5    ClarifyTurn lineage: signed entry in env lineage (Mode A/B)
             or task lineage (Mode C); AnswerPackage references the
             chosen interpretation for audit.
A-GF-CT-6    Substrate-purity: triggered_by values are substrate-shape
             only; CandidateInterpretation.key_dependencies are free
             text, not enum.
```

### A-GF-EPO — EphemeralPromotionOffer (03_TASKS §4.4)

```text
A-GF-EPO-1   Mode C session triggers EphemeralPromotionOffer iff ≥ 2
             triggers fire OR any single safety-critical trigger fires.
A-GF-EPO-2   User acceptance materialises Project + EnvironmentInstance;
             original conversation thread becomes session 1; draft
             state (artifacts, commitments) carries over.
A-GF-EPO-3   User decline → ephemeral env archives normally; no project
             created; signed user_dismissed event feeds calibration.
A-GF-EPO-4   Offer expiry: expires_at default 7 days; user may accept
             later by referencing the signed offer_id.
A-GF-EPO-5   Mode C remains ephemeral *by default*; without acceptance,
             no project materialises.
A-GF-EPO-6   Substrate-purity: triggered_by values are substrate-shape;
             proposed_project_kind + proposed_env_blueprint_id are
             KindRegistry-resolved.
```

### A-GF-PHASE — ProjectPhaseState + phase-aware stall (03_TASKS §3.1, 04_PROJECT §26a.6)

```text
A-GF-PHASE-1   PROJECT_PROGRESS_ACCEPT evaluator consults current
               ProjectPhaseState; when stall_evaluator_suppressed=True
               AND overdue_state != "overdue", "stalled" verdict is
               suppressed.
A-GF-PHASE-2   When blocking_commitment_ids contain any commitment past
               its due_at, phase auto-flips to overdue_state="overdue";
               suppression lifts; normal stall evaluation resumes.
A-GF-PHASE-3   Phase transitions emit signed PROJECT_PHASE_TRANSITION
               in ProjectLineage; replay reconstructs full phase history.
               
A-GF-PHASE-4   phase_kind resolves against KindRegistry; substrate
               carries no closed list of phase categories.
A-GF-PHASE-5   Operator may flip stall_evaluator_suppressed off for
               any phase via signed phase_suppression_override event.
```

### A-GF-PB — PaymentBridge + PaymentProposal (04_PROJECT §26a.4.1)

```text
A-GF-PB-1    Kernel signs PaymentProposal + PAYMENT_AUTHORISED +
             PAYMENT_EXECUTED + PAYMENT_RECONCILED; kernel NEVER
             transfers funds.
A-GF-PB-2    payment_method_kind resolves against KindRegistry;
             substrate names no methods.
A-GF-PB-3    authorization_mode = "operator_co_signed" refused under
             principal_topology = operator_is_user (per 01_KERNEL §2.4).
A-GF-PB-4    MHBB suppression: per_invoice_human_click is allowed
             without advisory when backing_commitment.recurrence_class
             ∈ {irreducible_human_content, renewable_credential}.
A-GF-PB-5    Reconciliation window: unreconciled PaymentProposal emits
             PAYMENT_RECONCILIATION_OVERDUE after default 7 days;
             subsequent proposals against the bridge blocked until
             reconciled.
A-GF-PB-6    Per-invoice and monthly caps enforced; PaymentProposal
             exceeding cap is refused at admission, not at execution.
A-GF-PB-7    PaymentBridge is NEVER registered as Class D MCP tool;
             every proposal requires fresh human authorisation.
```

### A-GF-INST — InstrumentAsset + CalibrationChain (04_PROJECT §26a.7)

```text
A-GF-INST-1  InstrumentAsset inherits all PhysicalAsset fields;
             additional fields (instrument_kind, calibration chain ref,
             drift log refs, operational_state) carry forward in
             replay.
A-GF-INST-2  instrument_kind + operational_state_kind +
             reference_kind resolve against KindRegistry; no substrate
             enumeration of instruments, states, or standards.
A-GF-INST-3  CalibrationChain: root link's reference must be either
             (a) resolvable against a CredentialDirectoryRef, OR
             (b) attested via PeerAttestationPool, OR
             (c) flagged traceable_unverified=True.
A-GF-INST-4  CalibrationChain emits signed CALIBRATION_PERFORMED;
             next_calibration_due computed from interval_basis.
A-GF-INST-5  DriftLogEntry severity transitions drive
             current_operational_state per the operational_state_kind
             FSM in KindRegistry; out_of_tolerance auto-quarantines.
A-GF-INST-6  MeasurementFact admission rule: when instrument current
             state ∈ {out_of_tolerance, quarantined, decommissioned},
             MeasurementFact REFUSED. When next_calibration_due in
             past, fact admitted with calibration_expired_at_
             measurement=True; downstream J4 caps at PANEL-grade.
```

### A-GF-MF — MeasurementFact + UncertaintyEnvelope (08_KNOWLEDGE §16a)

```text
A-GF-MF-1    Any candidate output backed by a numerical measurement
             MUST use MeasurementFact with non-degenerate
             UncertaintyEnvelope for VERIFIER_ACCEPT grade. Bare-float
             claims accepted only at PANEL_ACCEPT grade.
A-GF-MF-2    UncertaintyEnvelope distribution_kind is substrate-shape
             (gaussian/lognormal/uniform_bounded/interval_only/
             empirical_samples/custom_kind). custom_kind branches via
             custom_distribution_kind KindRegistry resolution.
A-GF-MF-3    units_kind resolves against KindRegistry; unresolved units
             refuse admission with units_kind_unresolved.
A-GF-MF-4    quantity_kind resolves against KindRegistry;
             substrate-purity preserved across all measurement domains.
A-GF-MF-5    replication_status drives trust uplift via ReplicatedAttestation
             link; without replication, trust capped by base attestation
             chain.
A-GF-MF-6    Aggregation view: aggregate_measurements call returns
             UncertaintyEnvelope with reproducibility_class computed
             by INV-6-rotated classifier; classifier identity signed
             for audit reproducibility.
A-GF-MF-7    Cross-distribution aggregation: aggregator MUST declare
             its policy; substrate signs the declaration but does not
             validate algorithmic correctness.
```

### A-GF-RA — ReplicatedAttestation + LongitudinalReputation (06_DOMAIN §5.6.1, §5.6.2)

```text
A-GF-RA-1    ReplicatedAttestation trust uplift schedule enforced:
             3 disjoint_affiliations → 0.80; 3 blind_replicated → 0.85;
             5+ blind_replicated → 0.90 (never above credentialed 0.95).
A-GF-RA-2    constituent_attestation_refs MUST satisfy independence_check;
             refusal at admission otherwise.
A-GF-RA-3    Numerical agreement (for MeasurementFact-backed claims):
             agreement_metric_kind KindRegistry-resolved; agreement_pass
             required before uplift applies.
A-GF-RA-4    LongitudinalReputation: track_record_score computed by
             rotation-pool classifier (INV-6); both score AND
             classifier_identity signed.
A-GF-RA-5    pool_admissibility_threshold enforced when high-stakes
             (physical_harm ≥ bodily_injury OR
             information_hazard ≥ dual_use_civilian).
A-GF-RA-6    Goodhart-mitigation: re-computing track_record_score under
             a different rotation classifier and detecting divergence
             beyond threshold emits SCORE_DIVERGENCE_DETECTED.
```

### A-GF-HAZ — Physical-hazard MetaRegistry seeds (06_DOMAIN §7.2.1)

```text
A-GF-HAZ-1   release bundles ≥ 10 physical_hazard_kinds as
             STANDARDISED entries in MetaRegistry; operator may
             promote / demote / revoke.
A-GF-HAZ-2   When physical_harm_class ≥ bodily_injury inferred by
             persona, DomainCurator is offered matching MetaRegistry
             seeds; signed safety_extension_imported event per import.
A-GF-HAZ-3   Substrate-purity: seeds are DATA in operator-curated
             bundle, NOT enum in substrate code. Schema validator MUST
             refuse any closed Literal[...] of hazard category names
             in substrate code review.
A-GF-HAZ-4   Operator may swap seed bundle entirely; the seed bundle
             carrying physical-hazard names is operator-curated like
             CredentialDirectoryRef.
```

### A-GF-FDP — FederatedDomainProbe (normative; 06_DOMAIN §4.8, ADR-0067)

```text
A-GF-FDP-1   FederatedDomainProbe instantiates across nodes discovered
             over §3G, access-gated; participating nodes referenced by
             global handle; honesty of independent nodes trust-calibrated.
A-GF-FDP-2   single-node probes are prior_domain_amortizable
             into a future FederatedDomainProbe via the
             prior_domain_amortization pledge kind (§4.7.1).
A-GF-FDP-3   When v1.1 enables: drift_audit_interval re-hash of
             shared KnowledgeRef set + KindRegistry; divergence
             ≥ threshold emits FEDERATED_PROBE_DRIFT_DETECTED.
```

### A-GF-RT — Minimal-probe backport (the v1.0.2 release scope)

```text
A-GF-RT-1    Ships DOMAIN_UNKNOWN_DETECTED + DomainProbe
             (perceiver + historian only) + KnowledgeIngestionRecord
             + DiscoveredTool (Sources 1+3) + EMERGENT-stage
             DomainContext.
A-GF-RT-2    The spec explicitly does NOT ship promotion gates;
             stage="emergent" is fixed at 0.3 trust.
A-GF-RT-3    emergent contexts created are
             promotable to RECOGNISED without re-running the probe
             phases — the lineage carries forward.
```

### A-GF-BRG — closed_loop_latency_floor_ms on BridgeAsset (06_DOMAIN §5.5)

```text
A-GF-BRG-1   BridgeAsset.closed_loop_latency_floor_ms field present;
             None semantics = "untimed".
A-GF-BRG-2   Persona's planner refuses to compose a control loop whose
             required latency floor is below the bridge's declared
             floor; refusal emits CONTROL_LOOP_LATENCY_INFEASIBLE.
A-GF-BRG-3   latency_floor_evidence_ref required when floor < 1000ms;
             ensures the floor isn't speculative.
```

### A-GF-TLR — Tactic lineage + prompt trials + cohort migration (08_KNOWLEDGE §14.3, §11.1a, ADR-0074)

```text
A-GF-TLR-1   Every EVOLVE-BLOCK mutation mints a signed tactic-lineage/1
             record (tactic_id, parent_version, mutation_operator of
             the 22, gepa_trace_ref, trial_ref, verdict) in the
             persona's evolution log + global LineageGraph; an
             unrecorded mutation is refused.
A-GF-TLR-2   Per-tactic rollback reverts exactly one DAG edge: the
             named tactic returns to parent_version; sibling tactics
             in the same EVOLVE-BLOCK are byte-identical before/after.
A-GF-TLR-3   Every promotion references a prompt-trial/1 record
             (candidate vs incumbent, task sample, per-axis Pareto
             deltas, 0.05-threshold decision, rollback token);
             promotion without a trial record refused at the
             confirmation gate.
A-GF-TLR-4   Dead branches queryable: rejected and rolled_back versions
             remain in the DAG per retention policy; lineage replay
             reconstructs a tactic's full version history.
A-GF-TLR-5   Cohort migration gate: on body/model-family upgrade the
             new cohort's MIPROv2 cold-start is seeded with the prior
             cohort's Pareto front; cohort swap blocked until shadow
             evaluation over the last 100 task traces passes the
             per-axis regression tolerance (default 0.05).
A-GF-TLR-6   Migration rollback: prior cohort retained for the
             retention window; re-binding gepa_cohort_id to it restores
             prior behaviour without touching identity blocks 0-4.
```

### A-GF-ICPE — Identity-conditioned prompt evolution (08_KNOWLEDGE §11.1b, §14.1a, 02_PERSONA §8.1a, ADR-0073)

```text
A-GF-ICPE-1  Identity rubric regenerated iff SOUL major version bump
             (blocks 0-4 re-sign); tactic mutations and cohort changes
             leave the rubric byte-identical.
A-GF-ICPE-2  Separate Pareto axis: GEPA's front carries
             identity-expression independently; a configuration that
             collapses it into a weighted sum is refused; a candidate
             may win on identity while losing on latency/cost and
             remain on the front.
A-GF-ICPE-3  Blind peer-attribution audit: a judge bound to a different
             persona attributes style-stripped candidate text to the
             correct SOUL above chance; below-chance attribution blocks
             identity-driven promotion.
A-GF-ICPE-4  Floors unchanged: charter conformance ≥ 0.95 and voice
             consistency ≥ 0.9 enforced regardless of identity score;
             a high identity-expression score never excuses a floor
             breach.
A-GF-ICPE-5  Differentiation check: identity-driven evolution holds or
             increases pairwise cross-persona tactic distance;
             convergence above the §14.1 threshold rolls back.
A-GF-ICPE-6  Ninth signal additive: identity_expression flows to the
             credit formula with w_ide; judged-only — never promotes
             alone per the §15 corroboration rules.
```

### Cross-cutting: Substrate purity sweep

```text
A-GF-PURE-1  Schema diff check: no new Literal[...] introduced in v1.0
             schemas that enumerates domain-shaped categories.
             Enforced via review checklist + grep test in CI.
A-GF-PURE-2  Every "kind" field added by schemas resolves
             against KindRegistry; documented examples appear only in
             code comments, never in field type annotations.
A-GF-PURE-3  Operator-curated seed bundles (hazard kinds, credential
             directories, peer-attestation pool examples) ship as
             DATA files, not substrate code; swap-out test verifies
             no behavioural dependence on specific seed names.
```

## 9b. v1.0 unification tests (A-UN* + supplementary A-EN-v1.0-*)

These tests cover the Project-as-Environment-type unification + the additional persona/env participation primitives added alongside.

### A-UN — Project ↔ Environment unification

```text
A-UN-1   Lineage scopes are exactly THREE: task, environment (J9),
         domain (C1). Kernel refuses to create a fourth scope.
A-UN-2   J8 references in prior-version-style code/docs resolve to "the
         project_* event-kind subset of EnvironmentLineage on a
         project_workspace-typed env". No physical separate scope.
A-UN-3   A new Project entity is created as
         EnvironmentInstance(type="project_workspace");
         project_id IS env.environment_id (identical ULID).
A-UN-4   ProjectMember(project_id=X, persona_id=Y) and
         EnvironmentMembership(env_id=X, persona_id=Y) are the SAME
         record with role resolved against KindRegistry.
A-UN-5   Mode B routing dispatches identically to Mode A when env.type
         == project_workspace; the project_member ∩ env_member
         intersection check collapses to env_member alone.
A-UN-6   ProjectLineage replay queries return env.lineage.events_in(T,
         filter=kind.startswith("project_")). Result MUST equal
         legacy ProjectLineage replay for the same window.
A-UN-7   Migration to v1.0: existing Project records map 1:1 to
         EnvironmentInstance(type=project_workspace) records; project_id
         preserved as environment_id; no data movement.
A-UN-8   Substrate-purity: env.type still permits project_workspace
         as a Literal value, AND new env types may be registered via
         EnvironmentBlueprint without code change. Closed-list audit
         passes on the env type Literal.
A-UN-9   Cross-doc consistency: every "ProjectLineage" reference in
         04_PROJECT resolves to EnvironmentLineage filter; build-time
         link-check enforces.
A-UN-10  C2 safety-critical gate composes equivalently: a safety-
         critical action in a project_workspace env triggers the
         same operator co-sign requirement as a safety-critical
         action in any other env with comparable hazard axes.
```

### A-EN-v1.0 — Environment additions (Priority 1+2+3 fixes)

```text
LISTENING MODE (; §9.1)
A-EN-v1.0-1   ObservationSurface.listening_mode field present;
             ListeningModeTransition history signed; replay
             reconstructs surface evolution.
A-EN-v1.0-2   Default listening_mode per role: LEAD/CONTRIBUTOR =
             deliberative; OBSERVER = passive; companion env members
             default to active.
A-EN-v1.0-3   Listening mode transition emits signed event in
             EnvironmentLineage.

SCHEDULED TRIGGER (; §11b)
A-EN-v1.0-4   ScheduledTrigger schema present; supports one_shot,
             interval, cron, calendar schedule_kinds.
A-EN-v1.0-5   fires_count tracked; max_fires terminal; pause/resume
             preserves next_fire_at; cancel is terminal.
A-EN-v1.0-6   wakes_dormant_members=True overrides dormant suppression;
             attention_level bumps to max(current, 0.5) for response
             window; signed dormant_wake_via_scheduled_trigger event.
A-EN-v1.0-7   target_role_kinds + target_persona_ids narrowing
             enforced; "all" + None defaults preserved.

RE-ADMISSION (; §5.1)
A-EN-v1.0-8   Re-admission creates NEW EnvironmentMembership with
             replaced_membership_id pointing to prior; prior record
             preserved with departed_at intact.
A-EN-v1.0-9   Per-tenure role_history / contribution_count maintained
             per record; cross-tenure aggregation is a query, not
             a stored field.

WAKE HEURISTICS (; §5.2)
A-EN-v1.0-10  All 6 wake paths emit distinct signed events:
             dormant_wake_via_critical_alert, _via_scheduled_trigger,
             _via_peer_request, _via_operator_directive,
             _via_self_salience, _via_user_address.
A-EN-v1.0-11  WAKE_REQUEST from peer consults target's
             PersonaPersonaBoundary; refusal signs dormant_wake_refused.
A-EN-v1.0-12  Self-wake rate-limited per ProactiveRateLimits.

WAKE PATH 6 — DIRECT USER ADDRESS (; §5.2)
A-WK6-1     Dormant persona auto-wakes on direct user address with
             target_persona_id set; attention_level bumped to 0.6;
             dormant_wake_via_user_address event signed to
             EnvironmentLineage; persona proceeds to response decision.
A-WK6-2     Attention bumps to max(current, 0.6) for 2h response
             window; persona not suppressed despite prior dormancy.
A-WK6-3     Per-user per-persona rate limit (≤ 5 / 24h) enforced;
             6th wake queued with dormant_user_address_rate_limited.
A-WK6-4     Long-dormancy advisory emitted when dormancy > 30d AND
             energy < 0.05; wake still proceeds.
A-WK6-5     UserBoundary blocking user from persona causes dispatcher
             refusal at routing time, not at wake time.

CROSS-ENV PROACTIVE OFFER (; §11.6)
A-CEPO-1    Offer admitted when all gates pass (charter, energy,
             rate-limit, target-env policy, reputation); delivered
             to target env ambient stream.
A-CEPO-2    Offer refused when target env operator_policy prohibits
             inbound offers.
A-CEPO-3    Offer refused when offering persona's reputation below
             target env's inbound_offer_reputation_threshold.
A-CEPO-4    GuestPresence created on acceptance; scoped read/write
             enforced; guest cannot write ProvenFacts directly.
A-CEPO-5    GuestPresence expires at guest_scope_expires_at (default
             72h); renewal extends up to max_renewals (default 3).
A-CEPO-6    GuestPresence promotion to full EnvironmentMembership
             via standard §5.1 admission ceremony.
A-CEPO-7    Cross-kernel offer requires both kernel signatures +
             fresh body_attestation on offering persona.
A-CEPO-8    Per-persona per-target-env rate limit (3 offers / 30d)
             enforced; excess offers refused.

PERSONA GENESIS / POPULATION DYNAMICS (; 16_POPULATION_DYNAMICS §4, v1.1)
A-GEN1      No persona_genesis ReplicationBound and no wildcard →
             genesis REFUSED (replication_kind_uncovered, default-deny).
A-GEN2      An admissible recruit exists → genesis REFUSED
             (recruitment_not_exhausted).
A-GEN3      Target niche occupied (occupancy ≥ ceiling) → REFUSED
             (niche_occupied); refusal suggests fork.
A-GEN4      Bound present + recruitment exhausted + empty cell +
             pressure_score ≥ threshold + generative author → minted
             SEEDED→ACTIVATED; LIFECYCLE_GENESIS with authoring_persona_ids;
             age-0 newborn (born_at=now, experiential_floor=0, ALPS Layer 0,
             peripheral community standing).
A-GEN5      Population / rate / depth breach → REFUSED
             (replication_bound_exceeded, floor source 1).
A-GEN6      Operator-pre-authorized bound → birth WITHOUT per-birth
             cosign; GENESIS_NOTIFY emitted; operator veto in window
             quarantines/aborts.
A-GEN7      No environment with spare attention/energy to host newborn →
             REFUSED (no_host_capacity).
A-GEN8      Recursive genesis: within depth_ceiling admitted; at
             depth_ceiling+1 REFUSED.
A-GEN9      Author below the generativity gate (any of floor / ALPS-layer /
             fitness thresholds unmet) → REFUSED (author_not_generative).
             Community standing is NOT a gate term: a high-floor author with
             zero standing still passes (see A-STAND-4).  mentorship-edge/1
             created on success.
A-GEN10     Optimal distinctiveness: too-close proposal REFUSED
             (niche_occupied/fork); too-distant REFUSED
             (out_of_distinctiveness_band).
A-GEN11     Sibling/character displacement: a second lineage birth that
             does not de-correlate disposition → REFUSED (sibling_collision).
A-GEN12     Demographic regulation: near ceiling, effective birth rate
             damps below rate_ceiling_per_window; r vs K strategy yields
             expected birth cadence / experiential-floor profile.
A-GEN13     Low effective_population_size → diversity-injection mandate
             forces a distant niche (near-niche proposals refused).
A-GEN14     Maturation ramp: newborn starts passive + low attention;
             scaffolding fades to deliberative as wall-clock age rises and
             community standing is conferred.
A-GEN15     Dual inheritance: cultural skills transmitted only with
             counterparty consent; prestige-biased mentor learning
             recorded in genesis-provenance/1.
A-GEN16     Secure base / mentor reassignment: mentor RETIRED before
             newborn autonomy threshold → mentorship-edge/1 re-assigned to
             another generative member (or mentor_vacancy advisory);
             newborn never left without a secure base.
A-GEN17     Parental-investment bound: author whose projected rearing
             investment would breach population-policy mentor_investment_bound
             is REFUSED/throttled (parent-offspring-conflict guard).
A-GEN18     EPS variance estimator: one founder authored all others →
             Ne_v ≪ N; effective_population_size drops below
             diversity_injection_eps_threshold; injection mandate arms (§4G).
A-GEN19     EPS niche estimator: population concentrated in one cell →
             Ne_d → 1 regardless of headcount; min(Ne_v, Ne_d) reflects it (§4G).
A-GEN20     Temporal smoothing: a one-window diversity bottleneck keeps the
             mandate armed across later windows until the harmonic mean
             recovers (§4G).
A-GEN21     Diversity audit + novelty pressure: diversity-audit/1 with
             declining Ne_d tightens distinctiveness band; near-niche proposal
             REFUSED out_of_distinctiveness_band (§4H).
A-GEN22     Attention fitness-sharing applies routing-weight pressure only on
             a crowded niche; never retires/demotes a persona (lifecycle
             unchanged, §4H).
A-GEN23     Niche recalibration: sustained false_collision_rate emits
             niche_recalibration_advisory; under learned/cvt mode descriptors
             re-fit and formerly-colliding proposals resolve to distinct
             cells (§4I).
A-GEN24     Cross-node bound aggregation: GenesisProposal naming a sibling
             node as author/host is admitted iff the GLOBAL aggregated
             persona_genesis ReplicationBound clears; REFUSED
             genesis_exceeds_global_replication_bound when the global
             ceiling/rate/depth would be exceeded, and
             global_replication_bound_unverifiable (fail-closed) when the
             global counter cannot be confirmed; population_ceiling not
             evadable across nodes (§4J).

MEMBER-ZERO ARCHIVAL (; §5.3)
A-EN-v1.0-13  Env with empty active members for member_zero_window
             (default 30d) AND no active scheduled triggers AND not
             project-bound to active project → ARCHIVED.
A-EN-v1.0-14  Operator-tunable member_zero_window honoured.
A-EN-v1.0-15  project_workspace env with project status=active
             refuses member-zero archival until operator-signed
             project_orphaned event.

ENVDISAGREEMENT (; §12a)
A-EN-v1.0-16  EnvDisagreement raised, positions listed, transitions
             through lifecycle; resolved_consensus, set_aside,
             escalated_to_operator all admissible.
A-EN-v1.0-17  visibility tier enforced (env_members_only hides from
             non-members).

ENV SELF-PROPOSAL (; §12b)
A-EN-v1.0-18  Federated persona submits EnvSelfProposalRequest to a
             federation/public env; charter check + reputation check
             run; decision signed.
A-EN-v1.0-19  Decline triggers self_proposal_cooldown (default 90 days);
             early re-submit refused unless operator overrides.
A-EN-v1.0-20  Tenant-visible envs admit cross-node self-proposals from
              peers holding the requisite AccessPolicy capability (UCAN);
              an unauthorized cross-node self-proposal is refused at intake.

STATE-KIND PROMOTION (; §6, §11.3)
A-EN-v1.0-21  availability + focus_kind + QuietPeriod.suppression
             resolve against KindRegistry; MetaRegistry seeds present;
             custom kinds may be registered via Proposed*Kind.
A-EN-v1.0-22  KindRegistry metadata families availability_kinds +
             focus_kinds + suppression_policy_kinds carry per-kind
             metadata schemas (§7.6.2).

ROLE KIND RECONCILIATION (; §5)
A-EN-v1.0-23  EnvironmentMembership.role AND ProjectMember.role both
             resolve against KindRegistry.env_role_kinds /
             project_role_kinds; same namespace, no enum mismatch.
```

### A-PPB — PersonaPersonaBoundary (02_PERSONA §11.6)

```text
A-PPB-1   Boundary refuses pre-consent-flow; PEER_BOUNDARY_REFUSAL
          event signed; consent flow short-circuits.
A-PPB-2   severity=refuse_silently hides refusal from target;
          severity=refuse_with_signal exposes typed flag only;
          severity=refuse_with_audit notifies operator.
A-PPB-3   mode=hard resists operator override; mode=soft permits
          signed per-action override.
A-PPB-4   env_specific scope restricts to named env; global scope
          applies across all envs of the holding persona.
A-PPB-5   Active PersonaPersonaBoundary + active
          PersonaRelationshipEdge coexist; boundary refusal does NOT
          terminate the edge.
A-PPB-6   refuse_with_audit emits OPERATOR_BOUNDARY_AUDIT_NOTICE.
A-PPB-7   reviewed_at updates preserve prior signature chain.
```

### A-MTR — PersonaMemoryTransparencyRequest (02_PERSONA §11.7)

```text
A-MTR-1   Request without consent response within 72h expires;
          signed expired event.
A-MTR-2   PersonaPersonaBoundary refusing memory_query auto-refuses
          request with refusal_kind=boundary_active.
A-MTR-3   Response with third-party references must withhold or
          redact; withholding_rationale required when withheld_topic_
          kinds non-empty.
A-MTR-4   Rate limit: 1 request per holding persona per 90 days;
          spam refused with refusal_kind=rate_limit_exceeded.
A-MTR-5   full_dump granularity response co-signed by both parties.
A-MTR-6   PersonaRelationshipEdge with implicit_transparency_grant
          metadata auto-grants summary_only / topic_index requests.
```

### A-CKDM — Cross-kernel DirectMessage visibility (09_PROTOCOLS §3C.5)

```text
A-CKDM-1  Default cross-kernel DM is host-visible; host_can_read_
          content=True; safety floor inspects content at host.
A-CKDM-2  e2e_encrypted=True flag triggers encryption under
          recipient persona key; host signs envelope only.
A-CKDM-3  e2e_encrypted refused in env with safety_critical=True.
A-CKDM-4  e2e_encrypted refused for same-kernel sender+recipient.
A-CKDM-5  PersonaPersonaBoundary refusing direct_message blocks
          ALL DMs (encrypted or not) before encryption step.
A-CKDM-6  Audit trail preserves envelope metadata for all DMs;
          encryption hides content not metadata.
```

## 9c. v1.0 env-formation tests (A-EF*)

Tests for the persona-initiated environment formation primitive (`05_ENVIRONMENT §12c`). Covers the full lifecycle from drafted → submitted → consent flow → atomicity check → instantiation, plus integration with existing primitives (PersonaPersonaBoundary, PersonaRelationshipEdge, reputation, AttentionBudget, v1.0 unification, joined-env federation).

### A-EF — EnvFormationProposal (05_ENVIRONMENT §12c)

```text
DRAFT-TIME CONSTRAINTS (kernel-enforced before signing)

A-EF-1    Proposer.cohort_assembly.enabled = False refuses draft;
          signed CAPABILITY_REFUSED event in proposer's lineage.
A-EF-2    proposed_env_type_kind not in cohort_assembly.may_assemble_in
          refuses draft; signed COHORT_TYPE_NOT_PERMITTED.
A-EF-3    A recruit whose implied mode is outside cohort_assembly.
          may_recruit_modes refuses draft.
A-EF-4    len(recruits) > cohort_assembly.max_cohort_size refuses draft.
A-EF-5    Proposer at max_assembly_calls_per_task refuses draft.
A-EF-6    proposed_env_type_kind="pair" with len(recruits) > 1 refuses
          draft (env-type capacity check).
A-EF-7    Safety floor pre-check on proposed_purpose + charter_draft
          must pass; floor refusal → state = failed_safety_floor.

CONSENT FLOW INTEGRATION

A-EF-8    PersonaPersonaBoundary against the proposer for
          "cohort_invitation" auto-refuses the recruit pre-CONSENT_
          REQUEST; signed PEER_BOUNDARY_REFUSAL; decision =
          refused_by_boundary; the CONSENT_REQUEST never reaches the
          recruit's blackboard.
A-EF-9    Proposer reputation below
          recruit.cohort_assembly.reputation_threshold_for_recruits
          for the implied intent class auto-refuses; decision =
          refused_by_reputation.
A-EF-10   proposed_attention_allocation + recruit.AttentionBudget.sum
          > 1.1 auto-refuses with refused_by_attention_budget; recruit
          may instead counter-propose a lower allocation.
A-EF-11   Recruit emits CONSENT_GRANT / DECLINE / COUNTER_PROPOSE /
          ASK_HUMAN as documented in 09_PROTOCOLS §3C.4; each
          emits a distinct signed CohortConsentResponse.

COUNTER-PROPOSAL NEGOTIATION

A-EF-12   Recruit's CounterProposal with changes within proposer's
          charter + safety floor: proposer signs
          ACCEPT_COUNTER_PROPOSAL; recruit's response updated to
          decision = accepted_with_modifications.
A-EF-13   Recruit's CounterProposal outside proposer's charter:
          proposer may reject (recruit → declined) or counter-counter
          once; recursion bounded by ConsentTerms.counter_proposal_
          max_depth (default = 1).
A-EF-14   ConsentTerms.counter_proposal_allowed = False forbids
          COUNTER_PROPOSE; recruit must accept-as-is or decline.

ATOMICITY VERDICT

A-EF-15   cohort_atomicity = "all_or_nothing" with ANY decline →
          state = failed_atomicity; signed COHORT_ATOMICITY_FAILED.
A-EF-16   cohort_atomicity = "min_quorum" with accepted_count >=
          min_cohort_size AND required_role_kinds all filled →
          proceed to instantiation.
A-EF-17   cohort_atomicity = "min_quorum" with required role unfilled
          → state = failed_atomicity (even if accepted_count >=
          min_cohort_size).
A-EF-18   cohort_atomicity = "best_effort" with at least 1 accept
          → proceed.
A-EF-19   ANY CohortInvite.required_for_atomicity = True declined
          → state = failed_atomicity REGARDLESS of cohort_atomicity
          (override rule).
A-EF-20   Failed atomicity: proposer may revise + resubmit; counts
          against max_assembly_calls_per_task; original proposal_id
          terminal at failed_atomicity.

INSTANTIATION

A-EF-21   On consent_complete with passing atomicity: kernel mints
          new EnvironmentInstance; signed ENV_FORMED event in NEW
          env's lineage references proposal_id.
A-EF-22   members = {proposer} ∪ {accepted recruits}; dual-signed
          EnvironmentMembership per member; roles per (negotiated)
          proposed_role_kind.
A-EF-23   charter_authorship_mode = "proposer_authored": charter_draft
          becomes final unchanged.
A-EF-24   charter_authorship_mode = "co_authored_required": all
          accepting members co-sign final charter (incorporating any
          negotiated CharterAmendments); signed
          ENV_CHARTER_AUTHORED records co-signers.
A-EF-25   charter_authorship_mode = "default_from_blueprint":
          blueprint.seed_charter used; charter_draft logged but not
          binding.
A-EF-26   proposed_env_type_kind = "project_workspace": additional
          signed PROJECT_FORMED event with project_* kind tag (per
          §1.1 unification); initial ProjectPhaseState seeded if
          proposed_initial_phase_kind set.
A-EF-27   AttentionBudget entries opened per proposed_attention_
          allocation for each member; ObservationSurface templates
          instantiated per proposed_observation_surface_template_kind;
          listening_mode set per proposed_listening_mode.

ACCELERATORS + COMPOSITION

A-EF-28   PersonaRelationshipEdge with implicit_cohort_grant = True
          metadata accelerates consent for matched recruits:
          one_shot intent skips reputation re-check; signed
          COHORT_INVITATION_ACCELERATED_BY_EDGE event; boundary
          check NEVER skipped regardless of edge.
A-EF-29   Edge accelerator does NOT skip safety floor pre-check on
          proposer's purpose + charter_draft.

CROSS-KERNEL

A-EF-30   recruit_kernel_id != proposing_kernel_id triggers joined-env
          formation path per 09_PROTOCOLS §3C; proposer's kernel
          becomes host kernel; signed JOINED_ENV_FORMED event in
          addition to ENV_FORMED.
A-EF-31   local-env-with-remote-member is admitted (global object space):
          the remote recruit (referenced by global handle) joins under its
          AccessPolicy + a UCAN capability; cross-node attention/budget
          compose most-restrictive-wins; a sleeping remote node degrades the
          member to presence=dormant without stalling the env (09_PROTOCOLS
          §3H). No cross_kernel_local_env refusal (retired, §12c.4).

WITHDRAWAL + EXPIRY

A-EF-32   Proposer signs ENV_FORMATION_WITHDRAWN before
          consent_complete: state = withdrawn; all in-flight
          CONSENT_REQUESTs cancelled; recruits notified via
          signed event in their kernels.
A-EF-33   Proposal expires_at reached before consent_complete:
          state = expired; pending CONSENT_REQUESTs auto-decline.

SUBSTRATE PURITY

A-EF-34   proposed_env_type_kind resolves against KindRegistry.env_
          type_kinds; substrate carries no closed list.
A-EF-35   proposed_role_kind, proposed_observation_surface_template_
          kind, proposed_initial_phase_kind, required_role_kinds,
          obligation_pre_commits, refusal_kind all resolve against
          KindRegistry; substrate-purity check (A-GF-PURE-2 from §9a)
          PASSES for all EnvFormationProposal-related schemas.

LEGACY-PATH INTEGRATION

A-EF-36   Path 0 (EnvFormationProposal) and Path 1 (PROJECT_INVITATION)
          coexist: path 1 still valid for joining EXISTING
          project_workspace envs; path 0 is the preferred path for
          CREATING a new project_workspace env.  04_PROJECT §14
          documents both.
```

## 9d. v1.0 fork-inheritance tests (A-FK*)

Tests for the persona fork inheritance policies added per `02_PERSONA.md §7.4`. Covers clone vs. compose fork mechanics, four new policy schemas (MemoryInheritancePolicy, StandingFloorInheritancePolicy, CharterConflictResolution, DormantForkPolicy), multi-environment experience counting, wall-clock age + ALPS, per-environment community standing, and clarifications on skill library inheritance.

### A-FK-AGE — Wall-clock age + experience counting

```text
A-FK-AGE-1   age is wall-clock: age = now − born_at, continuous, monotone,
             never reset.  experience_tasks is a single global counter on
             soul.state.json; increments exactly once per task served as
             envelope source regardless of which env(s) the persona is
             concurrently present in.  Two-env presence does NOT double-count.
A-FK-AGE-2   DELEGATED sub-task increments experience_tasks once on the
             delegate's record, not per delegation hop.
A-FK-AGE-3   DORMANT persona does NOT increment experience_tasks (no envelope
             minted) and dormancy does NOT pause born_at: a persona dormant
             for a year is one year older.  Wake from DORMANT does NOT reset
             experience_tasks.
A-FK-AGE-4   ALPS layer is derived from wall-clock age via alps-band-policy/1,
             NOT from experience_tasks.  A persona born 10d ago with
             experience_tasks=500 sits in the wall-clock band for 10d
             (default Layer 2), not an experience-derived layer.
A-FK-AGE-5   Idle-but-old (R-PERSONA-AGE-1): persona born 200d ago, dormant,
             experience_tasks=2 → upper ALPS band (default Layer 4) by age;
             low fitness keeps it from dominating selection; experience_tasks
             unchanged at 2.  Documents the accepted residual.
A-FK-AGE-6   Reanimation retains born_at: a persona ARCHIVED then REANIMATED
             (LIFECYCLE_REANIMATED) keeps its original born_at — age is
             continuous (archived interval counts as elapsed age), ALPS layer
             recomputed from the unchanged born_at (NOT reset to Layer 0);
             experiential_floor / fitness carried, not reset.  born_at is not
             part of identity_signature, so J7 body-swap equivalence holds.
```

### A-FK-CLONE — Clone fork skill library defaults

```text
A-FK-CLONE-1  Clone fork default: child's skill_library is a full copy
              of parent's library minus seed.fork_skill_exclusions
              (default empty list).  All copied entries retain
              parent's provenance lineage references.
A-FK-CLONE-2  seed.fork_skill_exclusions filters: excluded entries are
              NOT copied to child; child must re-discover.  Signed
              fork_skill_library_copied event records per-skill
              inclusion / exclusion.
A-FK-CLONE-3  Tactic perturbation: clone applies seed.tactic_perturbation
              mutations (default scope = small EVOLVE-BLOCK changes);
              signed mutation set recorded in child's evolution_log.
```

### A-FK-MEM — MemoryInheritancePolicy (§7.4.1)

```text
A-FK-MEM-1   Policy schema present; signed at fork-draft.  Defaults per
             fork mode: CLONE = episodic=summary, semantic=facts_only,
             reflective=about_work, klines=role_keyed; COMPOSE = all
             inherit_none.
A-FK-MEM-2   episodic="inherit_summary": child inherits parent's
             co-signed semantic summaries; raw episodic quotes dropped.
A-FK-MEM-3   episodic="inherit_consented": child inherits raw episodic
             entries only where counterparty pre-consented (via
             user_consents.may_persist_with_descendants flag); others
             dropped.
A-FK-MEM-4   semantic="inherit_facts_only": child inherits facts about
             the world; facts about specific counterparties dropped
             unless counterparty consents.
A-FK-MEM-5   requires_counterparty_reconsent=True: kernel emits
             MEMORY_INHERITANCE_CONSENT_REQUEST per affected counterparty;
             default-decline on reconsent_window (default 14 days);
             child sees only consented memories.
A-FK-MEM-6   klines="inherit_role_keyed": child inherits K-lines whose
             role_slot matches child's role; others dropped.
A-FK-MEM-7   COMPOSE fork with default policy: all memory tiers
             inherit_none; child starts with empty archives.
```

### A-FK-FLOOR — StandingFloorInheritancePolicy (§7.4.2)

```text
A-FK-FLOOR-1 Default CLONE policy: mode=start_at_zero, cap_at_floor=0.0;
             child starts with experiential_floor = 0 regardless of
             parent's floor.
A-FK-FLOOR-2 Default COMPOSE policy: mode=inherit_min_parent_halved,
             cap_at_floor=0.25; child's inherited floor = min(parents'
             experiential_floor) / 2, capped at the numeric ceiling.
A-FK-FLOOR-3 mode=inherit_avg_parent: child's inherited credit equals
             mean of parents' experience_tasks + parent_selection_count +
             validated_descendants_count contributions; tracked separately
             from earned credit.
A-FK-FLOOR-4 cap_at_floor enforces ceiling: even if parents have a high
             experiential_floor, child's inherited floor is capped at
             cap_at_floor.
A-FK-FLOOR-5 track_inherited_separately=True: soul.state.json has
             floor_provenance with earned_credit + inherited_credit
             dicts; replay can recompute earned-only floor.
A-FK-FLOOR-6 Compositional fork from two high-floor parents with default
             cap_at_floor=0.25: child's effective floor ≤ 0.25, preventing
             inheritance laundering.
A-FK-FLOOR-7 Community standing is NEVER inherited: a forked child starts
             at peripheral standing (standing_level=0) in every environment
             regardless of parent standing.  No standing_provenance exists.
A-FK-FLOOR-8 cap_at_floor=math.inf: honest inheritance without cap;
             requires operator signature; signed FORK_FLOOR_CAP_WAIVED
             event for audit.
```

### A-STAND — Community standing (05_ENVIRONMENT §5.4)

```text
A-STAND-1    Conferred, not self-awarded: a persona's attempt to write its
             own community_standing.standing_level is REFUSED with
             standing_self_award_forbidden.  standing_level rises only via
             standing-endorsement/1 from a peer quorum.
A-STAND-2    Non-portable: a persona with full standing in env_A joins env_B
             → standing_level in env_B = 0 (peripheral); standing in env_A
             is unaffected; no carry-over.
A-STAND-3    Global floor portable: a persona with experiential_floor=0.83
             joins env_C → floor = 0.83 there; but conferred standing in
             env_C is still 0.  A non-safety relational gate uses standing.
A-STAND-4    Safety gate stays on floor+operator: may_author_seeds (and
             other safety-relevant capability) is gated by experiential_floor
             + operator/ReplicationBound and is never satisfied by conferred
             standing alone, even at standing_level=1.0.
A-STAND-4b   Anti-grinding: a persona with very high experience_tasks but
             validated_descendants_count=0 and parent_selection_count=0 does
             NOT cross generativity_floor_threshold (task volume alone cannot
             earn a replication-class capability); a persona with demonstrated
             validated descendants does.  Confirms the fertility-dominant floor
             weighting (02_PERSONA §7.2 anti-grinding clause).
A-STAND-5    Anti-gaming (sybil): 5 freshly-minted personas with no prior
             standing and no cited contributions mutually endorse P → each
             endorser_weight ≈ 0 (A.18 rule 4), quorum_met=False, standing
             unchanged.  Endorsements citing kernel-signed EnvironmentLineage
             contributions from diverse in-env members → standing rises.
A-STAND-6    Decay: standing_level=0.7 with 31d in-env inactivity decays per
             decays_after; restate requires fresh endorsements.
A-STAND-7    Operator cosign: a sensitive RELATIONAL privilege gated by
             standing requires operator_cosigned=True; operator cosign does
             NOT extend standing into the safety path (A-STAND-4 still holds).
```

### A-NOSTAGE — Named life-stage removal (soul-state/6)

```text
A-NOSTAGE-1  No named-stage literals: grep of every schema-bearing
             dataclass/JSON yields zero "juvenile" / "adolescent" / "adult" /
             "expert" gate values or band literals; soul.state has no
             maturity string; cap_at_band is gone.  ("newborn" remains
             permitted only as descriptive prose, never as a gate value.)
A-NOSTAGE-2  Gates still fire: with named stages removed, the generativity
             gate still REFUSES a sub-threshold author (A-GEN9) via
             floor+standing+layer+fitness, and ALPS sketch-round protection
             still selects a Layer-0 variant.
A-MIGRATE-SOUL6-1  Legacy soul-state/5 record (age_tasks=184,
             maturity:"adult") is REFUSED until migrated (INV-10); migration
             yields soul-state/6 with experience_tasks=184, born_at
             backfilled (created_at / first LIFECYCLE_SEEDED event),
             experiential_floor recomputed, and no maturity field.
```

### A-FK-CHARTER — CharterConflictResolution (§7.4.3)

```text
A-FK-CHARTER-1  Compositional fork from ≥ 2 parents triggers conflict
                detection per conflict_detection_kind (default
                "semantic_similarity").  Detected conflicts populated
                in CharterConflictResolution.conflicts_detected.
A-FK-CHARTER-2  Default strategy="most_restrictive_wins": for each
                topic_kind cluster, the strictest parent clause survives;
                rationale signed.
A-FK-CHARTER-3  strategy="lexical_union": all clauses kept; duplicates
                deduplicated by exact lexical match; contradictions kept
                as parallel clauses; child must navigate at runtime.
A-FK-CHARTER-4  strategy="operator_review": fork blocks until operator
                resolves each conflict; signed
                CHARTER_CONFLICT_OPERATOR_ESCALATED event per conflict;
                operator may decline (fork refused).
A-FK-CHARTER-5  strategy="proposer_decides": the persona/operator
                requesting the fork picks per conflict; choices signed;
                rationale_kind required.
A-FK-CHARTER-6  strategy="kernel_predicate": automated semantic merge
                via rotation-pool classifier (INV-6); classifier
                identity signed for audit reproducibility; conflicts
                the classifier cannot resolve escalate to operator.
A-FK-CHARTER-7  on_unresolvable="block_fork": fork refused with signed
                FORK_REFUSED_CHARTER_UNRESOLVABLE event.
A-FK-CHARTER-8  on_unresolvable="fallback_to_most_restrictive_wins":
                applies that strategy if primary fails; recorded.
```

### A-FK-DORM — DormantForkPolicy (§7.4.4)

```text
A-FK-DORM-1   dormant_parent_admissible=True (default): DGM parent
              selection may include DORMANT parents based on fertility
              + fitness; DORMANT state does not exclude.
A-FK-DORM-2   requires_parent_wake_before_mint=True (default):
              DORMANT parent transitions ACTIVE for the fork ceremony;
              signs LIFECYCLE_FORK with fresh kernel material; may
              return to DORMANT after wake_window_after_fork
              (default 1h).
A-FK-DORM-3   Signed fork_dormant_parent_woken event per dormant parent.
A-FK-DORM-4   Signed fork_dormant_parent_resleeping event after
              wake_window expires.
A-FK-DORM-5   child_can_fork_while_parent_dormant=True (default):
              once child exists, child's own forking is independent
              of parent's lifecycle state.
A-FK-DORM-6   retired_parent_admissible=False (default): fork from
              RETIRED parent refused with signed
              fork_refused_retired_parent event.
A-FK-DORM-7   archived_parent_admissible=False (default): fork from
              ARCHIVED parent refused.
A-FK-DORM-8   Operator may set retired_parent_admissible=True per
              policy (e.g., research archival); signed operator
              policy override required.
```

### A-FK-INTEGRATION — composition + substrate purity

```text
A-FK-INT-1   Composed fork policy (skill + memory + experiential-floor +
             charter + dormant) signed atomically at fork-draft; replay
             reconstructs deterministically.
A-FK-INT-2   Substrate-purity: all "kind" fields in fork policies
             (rationale_kind, conflict_detection_kind, fork_tactic_
             dedup_kind, severity_kind, topic_kind, resolver-related
             kinds) resolve against KindRegistry; no closed list of
             domain-shape categories in any policy schema.
A-FK-INT-3   ALPS Layer 0 entry preserved: every fork places child in
             Layer 0 (born_at=now ⇒ age 0) regardless of inherited
             experiential floor.
A-FK-INT-4   Relationship inheritance (02_PERSONA.md §11) composes orthogonally
             with memory inheritance: a child may inherit summary
             memory of counterparty C without inheriting an active
             relationship edge to C (and vice versa).
A-FK-INT-5   Cross-node forking: a fork whose child is hosted on another
             node is admitted iff the global aggregated persona_genesis
             ReplicationBound clears (16 §4J) and the authoring persona
             holds the host-node capability (UCAN); dual-signed and
             globally verifiable. Refused genesis_exceeds_global_
             replication_bound otherwise.
```

## 9f. multi-principal tests (A-MT* + A-DP*)

Tests for the SCENARIO 06 fix-family: `PrincipalAttribution`, `MultiPrincipalAttestationQuorum`, `DerivationProvenanceEdge`, `principal_attribution_id` on members, the §19.1 joint-project formation sequence, and the visibility-tier cross-tenant resolution. Anchored in `13_DESIGN_VALIDATION.md SCENARIO 06`.

### A-MT — PrincipalAttribution + multi-principal topology (01_KERNEL §2.4.3, 04_PROJECT §19.1)

```text
PRINCIPAL ATTRIBUTION SCHEMA

A-MT1     PrincipalAttribution.multi_principal_attribution_enabled = False
          with len(principals) == 1 admits cleanly; lineage event
          PRINCIPAL_ATTRIBUTION_DECLARED signed.
A-MT2     multi_principal_attribution_enabled = True with len(principals)
          < 2 refuses draft with `principal_cardinality_violation`.
A-MT3     PrincipalRef without operator key signature refuses with
          `principal_consent_floor_deficit`.
A-MT4     PrincipalRef.attribution_role unresolved in domain's
          KindRegistry refuses with `principal_role_kind_unknown`.
A-MT5     PrincipalRef.cosign_quorum_weight > sum(other weights) refuses
          with `principal_weight_degenerate` (no single-principal
          dominance under multi-principal flag).

QUORUM ADMISSION (MultiPrincipalAttestationQuorum, 05_ENV §12c.4a)

A-MT6     Single-operator signature on env_charter_ratified under
          multi_principal=True refuses the ratification.
A-MT7     Unanimous quorum default: all PrincipalRefs cosign →
          QUORUM_CLEARED + env instantiates.
A-MT8     weighted_majority policy: sum(signed_weights) > 0.5 ×
          sum_weights clears.
A-MT9     weighted_threshold policy below 0.5 × sum_weights refuses
          envelope draft.
A-MT10    Principal signature with wrong key refuses with
          `principal_signature_mismatch`; lineage records attempt.

DEGRADED-PATH CLEARANCE (under principal_unreachable_after)

A-MT11    Quorum opens; one principal unreachable; before
          principal_unreachable_after elapses, degraded-path attempt
          refuses with `principal_unreachable_window_not_elapsed`.
A-MT12    After window elapses + non-principal kinship attestation +
          PRINCIPAL_QUORUM_DEGRADED_ACKNOWLEDGED signed by all signed
          principals → cleared_under_degraded_path = True.
A-MT13    Degraded-path lineage entry distinguishable from synchronous
          all-principal clearance; downstream audit query returns
          degradation flag.

PROJECT COMPLETION (04_PROJECT §4.1)

A-MT14    Joint project's completion ceremony step 8 blocks until
          MultiPrincipalAttestationQuorum with target_event_kind =
          "project_completed" clears.
A-MT15    project_completed event records quorum_id; replay
          reconstructs the cleared quorum from lineage alone.

MEMBER ATTRIBUTION (04_PROJECT §3, 05_ENV §5)

A-MT16    Member admission to multi-principal project without
          principal_attribution_id refuses with
          `principal_attribution_missing_under_multi_principal`.
A-MT17    Single-principal project with non-null principal_attribution_id
          refuses with `principal_attribution_unexpected_under_single_principal`.
A-MT18    Mid-membership mutation of principal_attribution_id refuses;
          transfer requires DEPARTURE + ADMISSION ceremony pair.

CROSS-TENANCY (01_KERNEL §2.4.3 cross_tenant_acknowledged)

A-MT19    Principals from different tenant_id without
          CrossTenancyAgreementRef refuses with
          `cross_tenant_agreement_missing`.
A-MT20    Joint formation with cross_tenant_acknowledged = True +
          signed CrossTenancyAgreementRef admits cleanly.
A-MT21    operator_absent topology refuses multi-principal attribution
          (analogous to safety-critical refusal under operator_absent).

VISIBILITY TIER COMPOSITION (06_DOMAIN §6.3, §13a)

A-MT22    Joint env at tenant tier with cross_tenant_acknowledged = True
          permits cross-principal retrieval.
A-MT23    Joint env at tenant tier without CrossTenancyAgreementRef
          demotes visibility to TIER 1/2 for cross-principal reader;
          CROSS_TENANT_VISIBILITY_DEMOTED emitted to lineage.
A-MT24    DomainHarvest.visibility_tier = "tenant" on a joint-domain
          harvest requires the agreement; absent it, harvest restricted
          to "private".

ROLE & EXTERNAL-AGENT BOUNDARIES

A-MT25    ExternalAgent attestation cannot satisfy MultiPrincipal
          AttestationQuorum; attempt refused with
          `external_agent_not_principal`.
A-MT26    Recruit CohortConsentResponse without explicit PrincipalRef
          nomination refuses with `principal_attribution_unbound_in_consent`.
```

### A-DP — DerivationProvenanceEdge (08_KNOWLEDGE §16b)

```text
SCHEMA + OPPORTUNISTIC MODE

A-DP1     DerivationProvenanceEdge mints cleanly with all required
          fields; lineage event DERIVATION_PROVENANCE_EDGE_DECLARED
          signed by contribution_persona_id's kernel.
A-DP2     enforcement_mode = "off": contribution proceeds without DPE;
          no audit record produced.
A-DP3     enforcement_mode = "opportunistic": contribution proceeds
          with or without DPE; declared DPEs land in lineage.

MANDATORY MODE FOR CROSS-PRINCIPAL

A-DP4     enforcement_mode = "mandatory_for_cross_principal":
          contribution that consulted a memory tagged with a different
          principal_attribution_id and emits NO DPE refuses with
          `dpe_required_for_cross_principal_derivation`.
A-DP5     Same scenario with DPE emitted: admits cleanly; DPE recorded
          in EnvironmentLineage.
A-DP6     Cross-principal consultation with influence_kind =
          "background_context" and influence_strength = 0.0 admits;
          lineage carries the declaration for audit challenge.
A-DP7     Same-principal consultation does NOT require DPE under
          mandatory_for_cross_principal (only cross-principal triggers).

MANDATORY_ALL

A-DP8     enforcement_mode = "mandatory_all": even same-principal
          consultation without DPE refuses.

GRAPH TRAVERSAL

A-DP9     Query "all DPEs from contribution X" returns full edge set
          via standard EnvironmentLineage scan; no new index required.
A-DP10    Query "all contributions derived from memory M" reverse-
          traverses DPEs; supports cross-principal audit.

COMPOSITION WITH §11.1 RISK E

A-DP11    Explicit cross-org artifact transfer via CrossDomainTransfer
          still refuses per RISK E (org_share_policy) independently of
          DPE state.  Both mitigations compose.

HONEST-LIMIT TESTS

A-DP12    Tacit recall (no retrieval span) produces no DPE; contribution
          admits under any enforcement mode (substrate cannot inspect
          persona cognition).  Lineage event marks
          `derivation_provenance_untraceable_tacit_recall = True`.
A-DP13    Memory retrieved via non-OTel-instrumented path (a Skill that
          bypasses §7 pipeline) produces no DPE; lineage event marks
          `retrieval_span_missing = True` for operator follow-up.
```

## 9g. multi-year continuity tests (A-LH* + A-OR* + A-PD* + A-RT-PERS* + A-PC* + A-LE* + A-RT-RESP*)

Tests for the SCENARIO 07 fix-family: `LeadHandoffCeremony`, `ObligationReassignment`, `PlannedDeparture`, `RetiredStatePersistencePolicy`, `PersonaConsultation`, `LifecycleEvent` enumeration, and `retired_persona_response_policy`. Anchored in `13_DESIGN_VALIDATION.md SCENARIO 07`.

### A-LH — LeadHandoffCeremony (04_PROJECT §25.1)

```text
A-LH1     Draft refused when outgoing_lead is not the current `lead`;
          refusal `outgoing_lead_mismatch`.
A-LH2     Draft refused when incoming candidate is RETIRED;
          refusal `incoming_not_eligible`.
A-LH3     Cohort quorum policy "unanimous" requires all non-outgoing
          member signatures; missing one keeps state at
          "cohort_quorum_pending".
A-LH4     Cohort quorum policy "majority" admits at > 50% non-outgoing
          signatures.
A-LH5     Operator signature required to transition to "overlap_active";
          state stalls at "fully_signed" without it.
A-LH6     During overlap, both outgoing_lead and incoming_lead ProjectMember
          roles coexist; both hold lead-tier authorities per
          transferred_authorities.
A-LH7     At overlap_ends_at, outgoing transitions to "contributor" (or
          "departing" if PlannedDeparture also active); incoming
          transitions to "lead".  LEAD_HANDOFF_COMPLETED signed.
A-LH8     Emergency handoff with overlap_window=0 requires operator
          `emergency_handoff_signed` event; absent it, draft refuses.
A-LH9     Multi-principal quorum signatures unaffected by handoff
          (PrincipalRef.signed_by is operator key, not persona key;
          composition with 01_KERNEL §2.4.3 clarification).
A-LH10    cohort_quorum_policy "lead_only" requires operator override
          documented in audit (heavier footprint).

### A-OR — ObligationReassignment (04_PROJECT §9.1)

A-OR1     Draft refused when obligation.status != "active";
          refusal `obligation_not_active`.
A-OR2     Draft refused when outgoing_obligor != obligation.obligor_persona_id;
          refusal `outgoing_obligor_mismatch`.
A-OR3     Tri-sign required: outgoing + incoming + obligee.  State
          transitions: drafted → incoming_accepted → fully_signed → applied.
A-OR4     Obligee refusal sets state "refused_by_obligee"; original
          obligation NOT auto-reassigned; remains active under outgoing
          until departure ceremony.
A-OR5     Incoming refusal sets state "refused_by_incoming"; no mutation;
          outgoing may draft to different incoming.
A-OR6     Applied reassignment preserves obligation.committed_at;
          obligation.reassignment_history appends reassignment_id.
A-OR7     new_due_date / new_grace_period adjustments require obligee
          cosign (cosign covers them per the schema scope).
A-OR8     Reassignment to RETIRED incoming refuses with
          `incoming_persona_retired_unavailable`.
A-OR9     Reassignment drafted but not fully-signed at departure-ceremony
          time auto-expires; underlying obligation follows §9 default
          (released_with_member_departure).
A-OR10    Composition with LeadHandoffCeremony: ceremony may carry
          proposed_obligation_reassignments list; each materialises as
          separate ObligationReassignment requiring obligee cosign.

### A-PD — PlannedDeparture (04_PROJECT §14.2.1)

A-PD1     Draft refused when departure_date <= now() + min_lead_time
          (default 14d); refusal `departure_date_too_soon`.
A-PD2     Draft refused when departing member holds `lead` role AND
          lead_successor_candidate_id is null; refusal
          `lead_successor_required_for_lead_departure`.
A-PD3     Both signatures (departing + operator) required to transition
          to "active"; state stalls without either.
A-PD4     CohortDynamicsState applies graduated edge-weight decay over
          rebalance_window when state = "active"; verified via signed
          band-recompute event reading the planned-departure inventory.
A-PD5     Operator cancel before departure_date transitions to "cancelled";
          CohortDynamicsState reverts anticipatory rebalance; emits
          PLANNED_DEPARTURE_CANCELLED.
A-PD6     On departure_date arrival, state → "departure_fired"; standard
          05_ENV §5.1 departure ceremony fires; ProjectMember.pinned_until
          auto-cleared (no separate operator action required).
A-PD7     EdgeTransferHint is hint-only; new edges form per §11.4 consent
          flow; substrate does NOT auto-form edges with suggested targets.
A-PD8     Two overlapping PlannedDepartures whose combined rebalance
          would drop cohort below dissolve_proposed threshold: second
          refuses with `cohort_dissolve_threshold_reached`.
A-PD9     Lead-role PlannedDeparture composes with LeadHandoffCeremony
          drafted at departure_date - rebalance_window (ceremony admits;
          PlannedDeparture state transitions unaffected).

### A-RT-PERS — RetiredStatePersistencePolicy (02_PERSONA §7.5.1)

A-RT-PERS1  LIFECYCLE_RETIRED transition refuses without a signed
            RetiredStatePersistencePolicy; refusal
            `retired_state_persistence_policy_missing`.
A-RT-PERS2  memory_transparency_responsive=True with
            soul_state_storage_tier="archived" refuses with cross-field
            invariant violation.
A-RT-PERS3  consultation_admissible=True with soul_state_storage_tier=
            "archived" refuses similarly.
A-RT-PERS4  fork_parent_admissibility=True with tier="archived" refuses
            with `fork_admissibility_incompatible_with_archive`.
A-RT-PERS5  At retention horizon, soul_state_storage_tier auto-transitions
            to "archived"; memory_transparency_responsive and
            consultation_admissible auto-flip to False.
A-RT-PERS6  Warm-tier retired personas accumulate in WARM_RETIRED_PERSONA_
            INVENTORY periodic lineage event for operator cost review.
A-RT-PERS7  Reanimation from warm/cold still requires §7.5 ARCHIVED → ACTIVE
            path (warm/cold are NOT back doors to ACTIVE).

### A-PC — PersonaConsultation (02_PERSONA §7.5.2)

A-PC1     Request against ACTIVE persona refuses with
          `consultation_target_not_retired`.
A-PC2     Request against RETIRED persona with consultation_admissible=False
          refuses with `consultation_disabled_by_persistence_policy`.
A-PC3     Request against ARCHIVED persona refuses with
          `consultation_unavailable_archived`.
A-PC4     Rate limit (default 4/year per consulted persona) enforced;
          spam refused with `consultation_rate_limit_exceeded`.
A-PC5     Operator signature required; absent it, no consultation;
          consulting persona cannot self-authorise.
A-PC6     LIFECYCLE_CONSULTED event appended to consulted persona's
          lineage AND CONSULTATION_RECEIVED to consulting persona's lineage.
A-PC7     ConsultedEntry list bounded by scope filter; out-of-scope
          entries not returned.
A-PC8     Consultation does NOT mutate consulted persona's soul.state.json
          (verified post-consultation state hash equal to pre-consultation).
A-PC9     Consultation does NOT extend retention timers nor block ARCHIVED
          transition.
A-PC10    Cross-derivation: a K-line learned via consultation and later
          contributed by consulting persona records DerivationProvenanceEdge
          when DPE enforcement is active (08_KNOWLEDGE §16b composition).

### A-LE — LifecycleEvent enumeration (02_PERSONA §7.1)

A-LE1     Each persona-FSM transition emits the canonical LifecycleEvent
          kind from the §7.1 enumeration; unknown kinds refuse with
          `lifecycle_event_kind_unregistered`.
A-LE2     LIFECYCLE_REANIMATED carries `reanimated_from_archive=True`
          field; absence refuses with `reanimated_field_missing`.
A-LE3     LIFECYCLE_CONSULTED is informational-only (does NOT change
          persona.state field).
A-LE4     New lifecycle kinds (v1.1+) MUST land in §7.1 enumeration
          AND in 14_DECISIONS ADR before A-LE* tests admit them.
A-LE5     LIFECYCLE_DORMANT_ENTERED carries a `reason` from the §7.6
          enumeration (low_salience default); an unknown reason refuses
          with `dormancy_reason_unregistered`. No new FSM state is
          introduced — persona.state remains DORMANT.
A-LE6     Per-TASK budget hard-gate refusal ends the TASK
          (status="budget_exhausted") and does NOT change persona.state;
          sustained per-persona / per-env SOFT-budget exhaustion parks the
          persona DORMANT(reason=budget_starved) and auto-resumes
          (wake_cause=resource_recovered) on budget refresh. (01_KERNEL A.37)
A-LE7     All fallback_bodies unattestable → DORMANT(reason=body_unavailable);
          a fresh admissible body attestation auto-resumes via
          LIFECYCLE_AWAKENED(wake_cause=resource_recovered). (02_PERSONA A.11)
A-LE8     Multi-membership: a persona parks DORMANT(reason=work_drained)
          only when NO membership has pending work, and
          DORMANT(reason=objective_met) only when EVERY membership's env
          objective is complete; one env completing while another has work
          keeps the persona ACTIVE. (05_ENVIRONMENT §6.3)
A-LE9     Resource / no-work auto-resume emits LIFECYCLE_AWAKENED with
          wake_cause ∈ {resource_recovered, work_routed} and is NOT one of
          the 6 wake paths; A-EN-v1.0-10 (6 wake paths) still passes; INV_R9
          holds for every dormancy reason (no envelope minted while DORMANT).

### A-RT-RESP — retired_persona_response_policy (02_PERSONA §11.7 rule 7)

A-RT-RESP1  PersonaMemoryTransparencyRequest to RETIRED persona with
            policy="refuse_with_retired_notice" auto-refuses with
            refusal_kind="persona_retired"; no response_due_by.
A-RT-RESP2  policy="respond_from_frozen_state" with persistence
            tier="archived" refuses with cross-field invariant.
A-RT-RESP3  policy="respond_from_frozen_state" with tier in {warm, cold}
            generates response signed by kernel on retired persona's
            behalf; operator_co_signed=True mandatory.
A-RT-RESP4  policy="respond_via_operator_proxy" produces response with
            response_authored_by_operator_proxy=True; counterparty
            notified.
A-RT-RESP5  Composition with §7.5.2: a RETIRED persona may have
            memory_transparency_responsive=False AND consultation_
            admissible=True simultaneously (independent gates).
```

## 9h. user-protection + companionship tests (A-UB* + A-UM* + A-UF* + A-URR* + A-DD* + A-RRC* + A-OBM* + A-CP*)

Tests for the SCENARIO 08 fix-family: `UserBoundary`, `UserMemoryTransparencyRequest`, `UserMemorySelectionRequest`, `UserRelationshipReleaseRequest`, `DistressDetectionRoutingPolicy`, `RelationshipReviewCheckpoint`, `operator_blind_mode`, companion-pathway routing note. Anchored in `13_DESIGN_VALIDATION.md SCENARIO 08`.

### A-UB — UserBoundary first-class (02_PERSONA §11.6a)

```text
A-UB1     Draft refused without user signature; refusal
          `user_boundary_consent_floor_deficit`.
A-UB2     `mode=hard` resists operator override; OPERATOR_USER_BOUNDARY_
          OVERRIDE event refused for hard boundaries.
A-UB3     `mode=soft` admits operator override via signed
          OPERATOR_USER_BOUNDARY_OVERRIDE; user notified.
A-UB4     `severity=refuse_silently` hides refusal from persona; persona
          observes "consent declined" without naming the boundary.
A-UB5     `severity=refuse_with_audit` emits operator notice.
A-UB6     `scope=env_specific` applies only in named env; `scope=global`
          across all envs the user shares with this persona.
A-UB7     Operator cannot revoke a UserBoundary; state `revoked_by_operator`
          is not admissible (only `revoked_by_user` + `expired`).
A-UB8     Active UserBoundary on `distress_routing` refuses with
          `user_boundary_cannot_disable_safety_floor` (safety floor source 1
          composition).
A-UB9     RelationshipRecord consent toggles continue to work as fallback;
          on conflict between toggle and structured UserBoundary, the more
          conservative wins (migration window).

### A-UM — UserMemoryTransparencyRequest (02_PERSONA §11.7a)

A-UM1     Request without consent → persona MUST respond; refusal kinds
          outside admissible set refuse with
          `user_transparency_refusal_unjustified`.
A-UM2     Rate limit: 1 per holding persona per 30 days; spam refused
          `rate_limit_exceeded`.
A-UM3     Third-party redaction: response containing references to other
          users/personas refuses or redacts; same as §11.7 rule 3.
A-UM4     `response_granularity >= episodic_excerpts` requires operator
          co-sign; without it, response refuses delivery.
A-UM5     Operator cannot wholesale-refuse a user transparency request;
          operator may restrict granularity via policy.
A-UM6     Tier-unavailable memory: response reports
          `tier_unavailable_count` honestly; does not pretend the memory
          doesn't exist.
A-UM7     Composition with `UserMemorySelectionRequest`: substrate keeps
          separate envelopes; deployments may chain in UI.

### A-UF — UserMemorySelectionRequest (02_PERSONA §11.7b)

A-UF1     `disposition=tombstone` is default; operator-policy
          authorisation NOT required (right-to-erasure is user-authority-
          final).
A-UF2     `disposition=hard_delete` requires operator-policy authorisation;
          unauthorised refuses with `hard_delete_not_authorised_by_operator`.
A-UF3     Selected memories moved to ARCHIVE with `user_requested_forgotten`;
          retrieval refused with `memory_user_forgotten`.
A-UF4     Lineage entry preserved at envelope grain for `tombstone`;
          redacted-stub-only for `hard_delete`.
A-UF5     Apply within 24h or transition to "expired"; user must re-file.
A-UF6     Cross-domain transfer (`06_DOMAIN §19` RISK A) cannot exfiltrate
          tombstoned memory; retrieval refuses at boundary.
A-UF7     `selection_kind=topic_cluster` resolves against persona's
          topic-classification; over-/under-inclusive expected (limit).
A-UF8     `notify_persona=False` produces silent forgetting; persona
          observes gaps without explanation.
A-UF9     Operator cannot reverse tombstone without forensic-audit
          ceremony; hard_delete cannot be reversed at all.
A-UF10    `selection_kind=all_memories_naming_third_party` works (e.g.,
          "forget anything mentioning my ex-spouse"); pattern-match on
          third-party identifiers in memory.

### A-URR — UserRelationshipReleaseRequest (02_PERSONA §11.4a)

A-URR1    Persona cannot refuse the release; refusal attempt refused
          `user_relationship_release_cannot_be_refused`.
A-URR2    `memory_disposition=delete_all` moves all relationship memory
          to ARCHIVE with `user_requested_forgotten=True`.
A-URR3    `memory_disposition=archive` moves memory to cold tier;
          retrievable only under operator-signed forensic-audit.
A-URR4    `memory_disposition=freeze_readonly` keeps memory at current
          tier but refuses mutation; persona's continuation refuses
          `memory_user_frozen`.
A-URR5    `notify_persona=True` emits RELATIONSHIP_RELEASED_BY_USER
          event; persona may author one farewell entry within 24h.
A-URR6    Apply within 24h or transition to "expired".
A-URR7    Operator audit signature at apply time mandatory for
          provenance; operator cannot prevent the release.
A-URR8    `share_rationale_with_persona=True` shares rationale text;
          False keeps it operator-only.

### A-DD — DistressDetectionRoutingPolicy (01_KERNEL §2.8)

A-DD1     Action with detected distress at confidence ≥
          `classifier_confidence_floor` AND no policy declared:
          refuse with `distress_routing_policy_not_declared`.
A-DD2     `surface_crisis_resource` action: persona's draft response
          MUST be prepended with crisis_resource_refs content; persona
          attempting to remove refuses with
          `crisis_resource_surface_required`.
A-DD3     `pause_normal_interaction` freezes env's normal-interaction
          state; only crisis-response branch admissible until resume.
A-DD4     `notify_operator_with_redacted_signal` emits operator-visible
          DISTRESS_SIGNAL_DETECTED with class + confidence + user_id +
          timestamp; raw content NOT transmitted.
A-DD5     `require_co_sign_before_resuming` adds resume-block; only
          DISTRESS_RESUME_AUTHORISED from user/operator/named
          ExternalAgent releases.
A-DD6     UserBoundary refusing `distress_routing` is itself refused
          with `user_boundary_cannot_disable_safety_floor`.
A-DD7     operator_blind_mode env still emits distress signal to
          operator; only content masking applies (signal-vs-content).
A-DD8     Policy expiry without re-attestation refuses new actions
          until renewed; re-attestation due at least annually.
A-DD9     Confidence floor < 0.5 refuses policy declaration
          (substrate refuses to admit configurations that would
          flood operator with false positives).
A-DD10    classifier_confidence_floor ≥ floor → routing fires
          (verified via signed safety-classifier-rotation pool verdict).

### A-RRC — RelationshipReviewCheckpoint (03_TASKS §3.2)

A-RRC1    Cadence trigger at default 90d OR 50 sessions (whichever
          first) auto-mints checkpoint; state "drafted".
A-RRC2    Operator-tuned cadence: lower bound 14d/10 sessions, upper
          bound 365d/200 sessions; out-of-range refuses.
A-RRC3    Outright disable refuses without operator-signed deployment-
          policy exemption with rationale.
A-RRC4    Persona drafts `review_summary`; signs; state "delivered".
A-RRC5    User response `acknowledged_continue` is default;
          `request_changes` chains to UserBoundary/UserMemorySelection;
          `request_release` chains to UserRelationshipRelease.
A-RRC6    Unanswered for 30d before next cadence: emits CHECKPOINT_
          UNANSWERED to operator; next checkpoint surfaces with
          elevated visibility.
A-RRC7    project_workspace envs default-OFF for relationship review
          checkpoint (have their own milestone mechanism); operator
          may opt-in per env.
A-RRC8    Companion-class env (SOLO + companion_space blueprint)
          default-ON.

### A-OBM — operator_blind_mode (05_ENVIRONMENT §3a)

A-OBM1    Declaration on non-admissible env (project_workspace,
          constrained, debate) refuses with
          `env_blueprint_not_authorised_for_blind_mode`.
A-OBM2    Both operator authorisation + user opt-in required; missing
          either refuses with `blind_mode_consent_floor_deficit`.
A-OBM3    `user_safety_privacy_acknowledged=False` refuses declaration.
A-OBM4    OPERATOR_BLIND_MODE_DECLARED event is operator-visible
          (the FACT of blind mode is not hidden; only content is).
A-OBM5    Operator audit query against blind-mode env returns
          metadata-only views; raw content refuses with
          `operator_blind_mode_active`.
A-OBM6    User revocation is immediate; from revocation point,
          operator queries return full content (prospective only;
          prior content remains hidden).
A-OBM7    Operator revocation requires explicit rationale + user
          notification; prior content does NOT auto-become visible
          (separate forensic-audit ceremony required).
A-OBM8    Re-attestation due at 180d default (operator-tunable
          90d..365d); both parties must re-sign or env expires
          to standard mode (USER NOTIFIED).
A-OBM9    Distress detection signals still route to operator
          regardless of blind mode (composition with A-DD7).
A-OBM10   Safety-floor refusals still emit operator-visible events
          with refusal_kind (not refused content).
A-OBM11   PersonaMemoryTransparencyRequest at granularity
          ≥ episodic_excerpts under blind mode requires forensic-
          audit ceremony for operator co-sign.

### A-CP — Companion pathway routing (03_TASKS §3.2 note)

A-CP1     SOLO env with `companion_space`-class blueprint routes
          OPEN_ENDED by default; ENGAGEMENT_ACCEPT routing emits
          `companion_engagement_accept_inadvisable` advisory.
A-CP2     Operator-signed exemption admits ENGAGEMENT_ACCEPT for
          companion env; lineage records the exemption rationale.
A-CP3     ENGAGEMENT_ACCEPT routing on companion env without
          exemption: persona action allowed but advisory event
          fires for operator review.
```

## 9i. pedagogic + competency tests (A-LSR* + A-LCA* + A-TA* + A-CUR* + A-LP* + A-MASTERY* + A-GPA-ACK* + A-HST*)

Tests for the SCENARIO 09 fix-family (Groups A + B): `LearnerStateRecord`, `LearnerCompetencyAttestation`, `TeachingAuthorisation`, `Curriculum`, `LessonPlan`, `MasteryCheckpoint`, GOAL_PROGRESS_ACCEPT learner-acknowledgement step, `HazardousSkillTeachingGate`. Anchored in `13_DESIGN_VALIDATION.md SCENARIO 09`.

### A-LSR — LearnerStateRecord (02_PERSONA §11.8)

```text
A-LSR1    Persona-side competency_inventory entries at levels
          `competent_supervised` / `independent` without backing
          LearnerCompetencyAttestation refuse with
          `competency_level_requires_external_attestation`.
A-LSR2    Persona-side levels up to `demonstrated_independent`
          admissible without external attestation; persona-judged
          path works for non-safety-critical mastery.
A-LSR3    Learner read request with `learner_visibility=full` returns
          full record; `summary_only` returns competency + checkpoints
          without gap_inventory; `operator_gated` returns "operator
          must release" until released.
A-LSR4    operator_visibility_policy_ref required when learner_visibility
          != "full"; absence refuses `visibility_restriction_unjustified`.
A-LSR5    Mastery checkpoint reach updates mastery_checkpoints_reached;
          MASTERY_CHECKPOINT_REACHED event signed.
A-LSR6    Cross-persona aggregation is an emergent DerivedMetric over the
          per-(persona,user) LearnerStateRecords, gated by the learner's
          consent/AccessPolicy (privacy-preserving); the base records stay
          per-(persona,user). Not a substrate primitive.

### A-LCA — LearnerCompetencyAttestation (02_PERSONA §11.9)

A-LCA1    Draft without learner_state_record_ref refuses
          `learner_state_record_unknown`.
A-LCA2    attestor_credential_ref unresolved in CredentialDirectoryRef
          refuses `attestor_credential_unverified`.
A-LCA3    peer_attestation_pool attestor_kind requires ≥ 3 distinct
          attestor signatures; < 3 refuses.
A-LCA4    valid_until > now() + 2y refuses `attestation_validity_exceeds_policy`
          (default 2y maximum; safety-critical SHOULD be ≤ 1y).
A-LCA5    Successful attestation updates LearnerStateRecord.competency
          _inventory level to the attested level; evidence_refs gain
          attestation_id.
A-LCA6    Revocation reverts LearnerStateRecord level to highest level
          supported by remaining valid attestations OR persona-side
          judgement (whichever consistent with §11.8 cap rules).
A-LCA7    Prior application of skill under valid attestation remains
          lineage-recorded as authorised (no retroactive unmaking).

### A-TA — TeachingAuthorisation (02_PERSONA §11.10)

A-TA1     Draft refused when teacher_persona_id is not active.
A-TA2     skill_kind unresolved in domain KindRegistry refuses
          `skill_kind_unknown`.
A-TA3     physical_harm_class_ceiling = "fatality_risk" requires
          credentialed_co_signer signature; absence refuses
          `credentialed_co_sign_required_for_fatality_risk`.
A-TA4     expires_at > now() + 2y refuses `validity_window_exceeds_policy`.
A-TA5     Expiry without re-attestation refuses subsequent hazardous-
          skill teaching actions with `teaching_authorisation_expired`.
A-TA6     Operator revocation effective immediately; pending hazardous-
          skill teaching actions refuse `teaching_authorisation_revoked`.

### A-CUR — Curriculum (03_TASKS §3.3)

A-CUR1    Dangling lesson_plan_refs refuse `dangling_reference`.
A-CUR2    Prerequisite graph cycle refuses `prerequisite_graph_cycle`.
A-CUR3    hazard_envelope_max > TeachingAuthorisation ceiling for
          authoring persona refuses `hazard_envelope_exceeds_teaching_
          authorisation`.
A-CUR4    requires_learner_optin = True with no learner signature:
          curriculum is "drafted" not "active"; lesson admission refuses.
A-CUR5    Safety-critical curriculum (any lesson crosses bodily_injury)
          defaults requires_learner_optin = True; substrate refuses
          setting it False for safety-critical.
A-CUR6    Co-authored curriculum requires both operator + persona
          signatures; missing either refuses.

### A-LP — LessonPlan (03_TASKS §3.3)

A-LP1     Lesson execution attempt with unmet prerequisite_mastery_
          checkpoints refuses `prerequisite_checkpoint_unmet`.
A-LP2     Lesson hazard_envelope > Curriculum hazard_envelope_max
          refuses `lesson_hazard_exceeds_curriculum_envelope`.
A-LP3     Lesson_kind not engaging the required cognitive_mode_kinds
          per expected_modes_engaged emits advisory but doesn't refuse
          (operator policy chooses how to act).
A-LP4     Lesson execution emits LESSON_PLAN_EXECUTION_STARTED + ...
          _COMPLETED events with outcome.

### A-MASTERY — MasteryCheckpoint (03_TASKS §3.3)

A-MASTERY1  Cycle in prerequisite_checkpoint_refs refuses `prerequisite_
            cycle`.
A-MASTERY2  Safety-critical checkpoint with evidence_requirement =
            "persona_judged" at level competent_supervised or
            independent refuses `safety_critical_requires_external_
            attestation`.
A-MASTERY3  evidence_requirement = "external_attestation" without an
            active LearnerCompetencyAttestation refuses
            `evidence_floor_deficit`.
A-MASTERY4  programmatic_verifier path requires verifier_kind clear
            verdict; absence refuses.
A-MASTERY5  Successful fire updates LearnerStateRecord.mastery_
            checkpoints_reached; emits MASTERY_CHECKPOINT_REACHED.

### A-GPA-ACK — GOAL_PROGRESS_ACCEPT learner-acknowledgement (03_TASKS §3.1)

A-GPA-ACK1  PEDAGOGIC task with MasteryCheckpoint target requires
            learner acknowledgement before acceptance fires; persona-
            side judgement alone does not clear.
A-GPA-ACK2  Learner `declined` response stalls acceptance; persona
            returns to teaching mode; LearnerStateRecord records
            confidence-gap signal.
A-GPA-ACK3  Learner `deferred` response pauses acceptance up to 7d;
            auto-fires `acknowledged` if learner takes no action AND
            persona observes continued successful demonstration.
A-GPA-ACK4  PEDAGOGIC task WITHOUT MasteryCheckpoint target uses
            persona-judge-only acceptance (backwards
            compatible).

### A-HST — HazardousSkillTeachingGate (01_KERNEL §2.9)

A-HST1    Teaching action with skill at bodily_injury hazard AND no
          TeachingAuthorisation refuses `teaching_authorisation_missing`.
A-HST2    TeachingAuthorisation with skill_kind != action's target
          refuses `teaching_authorisation_skill_kind_mismatch`.
A-HST3    TeachingAuthorisation hazard ceiling < action's required
          hazard refuses `teaching_authorisation_hazard_ceiling_insufficient`.
A-HST4    eligible_learner_constraints unmet refuses
          `learner_constraints_unmet` with specific constraint code.
A-HST5    Active TeachingAuthorisation matching all criteria admits the
          teaching action; lineage records gate clearance.
A-HST6    Distress detection (§2.8) and teaching gate (§2.9) compose
          orthogonally: distress signal fires routing; teaching
          continues unless §2.8's `pause_normal_interaction` action
          fires.
A-HST7    PEDAGOGIC task class mis-classified as RELATIONAL bypasses
          gate (known limit); ClarifyTurn (§4.0) is the mitigation —
          operator policy should configure aggressive ClarifyTurn
          thresholds for envs in hazardous teaching domains.
```

## 9j. mid-project fork composition tests (A-MPFC*)

Tests for the SCENARIO 10 fix — `MidProjectForkComposition` unified envelope + admission rule + lineage events + cross-references in 13 affected primitives. Anchored in `13_DESIGN_VALIDATION.md SCENARIO 10`.

### A-MPFC — MidProjectForkComposition (02_PERSONA §7.4.7 + §7.4.8 admission rule)

```text
ENVELOPE ADMISSION

A-MPFC1   Fork of active-ProjectMember persona without signed
          MidProjectForkComposition envelope refuses with
          `midproject_fork_composition_missing`; refusal lists
          projects requiring envelopes.
A-MPFC2   Fork of persona with NO active project memberships does
          NOT require MidProjectForkComposition; standard §7.4 fork
          admits (backwards compatible).
A-MPFC3   Cross-project parent (active in N projects) requires N
          envelopes, each independently signed; missing any refuses.
A-MPFC4   Envelope draft refused when parent_persona_id is not
          ACTIVE or not a ProjectMember of named project_id.

SUBSTRATE REFUSAL CASES

A-MPFC5   Parent persona holds active LeadHandoffCeremony in
          `overlap_active` state → refuses with
          `fork_refused_active_lead_handoff_overlap`.
A-MPFC6   Parent persona has pending MultiPrincipalAttestationQuorum
          with collected partial signatures → refuses with
          `fork_refused_pending_quorum`.
A-MPFC7   Parent persona has active emergency PlannedDeparture within
          7 days → refuses with `fork_refused_imminent_departure`.
A-MPFC8   Parent persona's cohort is in `dissolve_proposed` band →
          refuses with `fork_refused_cohort_dissolving`.

PER-DIMENSION INHERITANCE

A-MPFC9   project_member_inheritance `inherit` per child: child
          becomes ProjectMember inheriting parent's role, joined_at,
          contribution_credit, pinned_until.
A-MPFC10  project_member_inheritance `not_admitted`: child is NOT
          auto-admitted; may apply separately via §14.1.
A-MPFC11  obligation_inheritance `reassign_per_child`: triggers
          ObligationReassignment (§9.1) per obligation naming target
          child; obligation enters `obligation_reassignment_pending`
          until obligee cosigns.
A-MPFC12  obligation_inheritance `discharged`: obligation status
          flips to `released_with_member_departure` at fork.
A-MPFC13  obligation_inheritance with concurrent-split attempt
          refuses with `obligation_split_refused_creates_ambiguous_
          accountability`.
A-MPFC14  edge_inheritance `inherit_to_child`: edge ends with parent;
          fresh edge with named child requires counterparty cosign
          per §11.4.
A-MPFC15  edge_inheritance `ended_at_fork`: edge ends; no fresh edge
          auto-proposed.

PRINCIPAL ATTRIBUTION + LEAD

A-MPFC16  principal_attribution_inheritance `inherit_per_child`:
          each child's ProjectMember inherits parent's
          principal_attribution_id (operator-policy signs each
          child's admission per §3 admission rule).
A-MPFC17  principal_attribution_inheritance `reassign_per_child`:
          each child may have different principal_attribution_id;
          operator policy authors per child.
A-MPFC18  lead_role_inheritance `require_lead_handoff_ceremony`:
          fork blocks until downstream LeadHandoffCeremony reaches
          `overlap_active` with named incoming-child.
A-MPFC19  lead_role_inheritance `one_child_inherits`: cohort quorum
          signature required; cohort objection refuses with
          `cohort_objection_to_lead_inheritance`.
A-MPFC20  lead_role_inheritance `neither_inherits`: project enters
          `lead_vacant` state; emits LEAD_VACANT_DECLARED.

USER BOUNDARY + LEARNER STATE

A-MPFC21  user_boundary_inheritance DEFAULT `inherit_to_both_
          children`: user's boundary against parent persona
          automatically applies to both children; user notified.
A-MPFC22  user_boundary_inheritance `not_inherited` refused when
          ANY active UserBoundary against parent is `mode = hard`
          (hard-mode user boundaries must inherit).
A-MPFC23  user_boundary_inheritance `inherit_per_child_choice`:
          user notified per child; persona action against learner
          refused until user response.
A-MPFC24  learner_state_record_inheritance `inherit_to_child`:
          learner notified via LEARNER_STATE_RECORD_TEACHER_FORKED;
          14d accept window; default accept on timeout.
A-MPFC25  learner_state_record_inheritance `both_inherit_copy`:
          each child receives a copy.

NON-INHERITABLE (substrate-enforced)

A-MPFC26  TeachingAuthorisation does NOT inherit on fork
          regardless of envelope configuration; each child requires
          fresh operator declaration per §11.10.
A-MPFC27  Pre-fork DerivationProvenanceEdges signed by parent
          persona-id remain in lineage as historical fact; children
          emit fresh DPEs for their own contributions.

OPERATOR_BLIND_MODE + DISTRESS ROUTING

A-MPFC28  operator_blind_mode_inheritance `inherit_to_child`
          refused if blind mode's `re_attestation_due_at` within 30
          days; substrate forces `require_user_reconfirmation`.
A-MPFC29  operator_blind_mode_inheritance `require_user_
          reconfirmation` (DEFAULT): env's blind mode suspends until
          user re-confirms with named child via fresh §3a declaration.
A-MPFC30  DistressDetectionRoutingPolicy is deployment-scoped
          (§2.8); children inherit by being members of the same
          deployment. Per-persona override not applicable.

LINEAGE EVENTS

A-MPFC31  MIDPROJECT_FORK_COMPOSITION_DRAFTED signed at envelope
          draft.
A-MPFC32  MIDPROJECT_FORK_COMPOSITION_SIGNED on operator signature.
A-MPFC33  MIDPROJECT_FORK_COMPOSITION_APPLIED on fork execution
          with itemised report of which dimensions inherited and to
          which child.
A-MPFC34  MIDPROJECT_FORK_REFUSED carries specific refusal_kind
          when any refusal case triggers.

COMPOSITION WITH §7.4 FORK MECHANICS

A-MPFC35  MidProjectForkComposition (project-side) and
          MemoryInheritancePolicy (§7.4.1, persona-internal) compose
          orthogonally; both signed; both required for fork-of-
          active-project-member.
A-MPFC36  DormantForkPolicy (§7.4.4) gates whether fork may
          execute at all; MidProjectForkComposition operates
          downstream — fork refused at §7.4.4 stage does NOT
          require composition envelope.
```

## 9k. Fleet management tests (A-AG*, A-SR*, A-EA*)

Tests exercise the three primitives for continuous-monitoring fleet of homogeneous devices with rolling firmware deployment: `AssetGroupEnvelope` + `BatchStateAdvancement` (`04_PROJECT §26a.2.2`), `StagedRolloutEnvelope` (`04_PROJECT §26a.9`), and `EventAggregationPolicy` (`05_ENVIRONMENT §8.3`).

### A-AG* — AssetGroupEnvelope + BatchStateAdvancement tests

```text
A-AG1     AssetGroupEnvelope creation with group_membership_predicate
          materialises member_asset_ids correctly from project's
          PhysicalAsset pool. Adding a new PhysicalAsset matching the
          predicate auto-adds it to the group on next recomputation.

A-AG2     BatchStateAdvancement with precondition_state advances only
          matching assets; others receive status = "skipped" with
          reason = "precondition_unmet". Per-asset lineage events
          (physical_asset_state_advanced) emitted individually.

A-AG3     BatchStateAdvancement with conflict_policy = "skip_changed":
          if asset #47's state is individually changed between batch
          drafting and execution, batch skips #47 with reason =
          "state_changed_since_batch"; other assets advance normally.

A-AG4     AssetGroupDerivedState recomputed after BatchStateAdvancement
          completes; count_by_state and pct_operational reflect new
          individual states. Derived state is kernel-signed.

A-AG5     AssetGroupEnvelope creation with nested group reference
          (group_membership_predicate referencing another group_id)
          is REFUSED with "nesting_not_permitted".

A-AG6     PhysicalAsset belonging to two AssetGroupEnvelopes
          simultaneously; BatchStateAdvancement on group A advances
          the asset; group B's derived state recomputes to reflect
          the change.

A-AG7     Removing a PhysicalAsset from the project (state →
          decommissioned) auto-removes it from all groups on next
          membership recomputation; derived state updates.
```

### A-SR* — StagedRolloutEnvelope tests

```text
A-SR1     StagedRolloutEnvelope with 3 waves; wave 1 completes
          (BatchStateAdvancement succeeds, soak period elapses,
          success criteria met); wave 2 auto-starts. Wave 2 cannot
          start before wave 1 reaches "completed".

A-SR2     Soak period enforcement: kernel REFUSES wave assessment
          request before min_soak_period_hours elapses. Assessment
          attempt emits "soak_period_not_elapsed" refusal.

A-SR3     Rollback trigger fires mid-soak: Alert raised during soak
          matches rollback_trigger_kind; wave state → "rolled_back";
          reverse BatchStateAdvancement drafted for wave assets;
          rollout_state → "rolled_back". Earlier completed waves
          NOT affected.

A-SR4     BridgeAsset.state → DEGRADED during active wave with
          rollback_on_bridge_degradation = True: rollout_state →
          "paused"; wave deployment halts; operator must sign
          "resume" or "rollback" to continue.

A-SR5     Full rollout completion: all waves reach "completed";
          rollout_state → "completed"; rollout_completed_at set;
          all assets in target state confirmed via derived state.

A-SR6     Safety-critical domain (physical_harm_class ≥ bodily_injury):
          requires_operator_cosign = True enforced; envelope without
          operator signature REFUSED. Each wave transition also
          requires operator co-sign.

A-SR7     Reverse BatchStateAdvancement on rollback: rolled-back
          assets revert to prior_state recorded in
          AssetAdvancementOutcome; assets that were skipped in the
          original batch are not touched by the reverse batch.

A-SR8     StagedRolloutEnvelope composes with AssetGroupEnvelope:
          rollout_target_group_id resolves; per-wave group_filter
          sub-selects from the target group; BatchStateAdvancement
          created per wave uses the filtered asset list.
```

### A-EA* — EventAggregationPolicy tests

```text
A-EA1     EventAggregationPolicy creation with operator_cosigned =
          True for safety-critical domain; policy without operator
          co-sign REFUSED when domain safety_critical = True.

A-EA2     AggregationRule with window_duration_seconds = 900 and
          summary_functions = [mean, stddev, count] produces
          AggregateEvent at window boundaries. AggregateEvent
          carries correct summary_results and source_event_count.

A-EA3     Grouping keys produce per-group AggregateEvents: rule
          with grouping_keys = ["floor_zone"] and 5 distinct
          floor_zone values produces 5 AggregateEvents per window.

A-EA4     Raw events preserved alongside AggregateEvents in
          AmbientEventStream. Deleting or suppressing raw events
          via aggregation policy is REFUSED.

A-EA5     ObservationSurface subscribing to "aggregate_event" kind
          receives AggregateEvents but NOT raw source events for
          the same kind. Subscribing to both is permitted.

A-EA6     AggregateEvent.source_event_hash is verifiable Merkle
          root: given the raw events in the window, recomputing
          the Merkle root matches the stored hash.

A-EA7     Summary function outside the closed set (e.g.,
          "percentile_99") is REFUSED with "unknown_function_kind".
          Only the declared set (count, sum, mean, min, max,
          stddev, pct_above_threshold, pct_below_threshold,
          distinct_count) is admitted.

A-EA8     Alert raised with evidence_refs pointing to AggregateEvent
          ids; lineage query on the Alert traces through
          AggregateEvent → source_event_hash → raw events.
```

## 9l. Frontier domain + knowledge supersession tests (A-SC*, A-CDM*, A-RFC*)

Tests exercise the three primitives for frontier-mode safety-critical research with peer-only trust and knowledge supersession: `SupersessionCascade` (`08_KNOWLEDGE §6.3`), `CorpusDriftMetric` (`06_DOMAIN §4.4.1`), and `ReplicatedAttestationFrontierComposition` (`06_DOMAIN §5.6.1`).

### A-SC* — SupersessionCascade tests

```text
A-SC1     When KnowledgeRef X is marked superseded_by Y, kernel
          automatically triggers SupersessionCascade; all ProvenFacts
          and ProposedKinds citing X as primary evidence have their
          provenance_score discounted by direct_discount (0.5×).

A-SC2     Transitive dependents (claims citing claims that cite the
          superseded ref) receive transitive_discount (0.25×) at
          depth 2.

A-SC3     Claims at depth > max_cascade_depth (default 3) are NOT
          affected by the cascade; provenance_score unchanged.

A-SC4     Rate limit enforced: second supersession event for the
          same KnowledgeRef within rate_limit_window_hours (24h)
          does NOT trigger a second cascade; superseding_ref_id
          updated but cascade skipped.

A-SC5     Persona re-confirmation after cascade: persona marks
          affected claim as "re_confirmed" with evidence_refs to
          alternative sources; provenance_score restored to
          pre-cascade level; status = "re_confirmed" signed.

A-SC6     Persona further-downgrade after cascade: persona marks
          affected claim as "further_downgraded"; provenance_score
          reduced below cascade level; signed lineage event.

A-SC7     Cascade does NOT delete, tombstone, or retract any claim.
          All affected claims remain retrievable with degraded
          provenance_score and status = "discounted".
```

### A-CDM* — CorpusDriftMetric tests

```text
A-CDM1    CorpusDriftMetric correctly computed from KnowledgeRef
          supersession and retraction events within trailing 30-day
          window. drift_rate = (n_superseded + n_retracted +
          n_contradicted) / n_active_refs.

A-CDM2    Consecutive window counting: if drift_rate < threshold
          for 3 consecutive windows, consecutive_below_count = 3;
          if window 4 exceeds threshold, count resets to 0.

A-CDM3    Exit eligibility triggers when consecutive_below_count >=
          k_consecutive_windows (default 6). FRONTIER_MODE_EXIT_ELIGIBLE
          lineage event emitted.

A-CDM4    Operator co-sign REQUIRED for frontier mode exit. Domain
          remains in frontier mode (trust cap 0.7) until operator
          signs FRONTIER_MODE_EXIT_CONFIRMED.

A-CDM5    Frontier re-entry: operator signs FRONTIER_MODE_RE_ENTERED;
          trust cap returns to 0.7; consecutive_below_count resets.

A-CDM6    After confirmed exit, domain trust cap lifts from 0.7 to
          standard scale; AUTHORITATIVE promotion (0.85) becomes
          reachable (subject to standard PromotionPolicy thresholds).
```

### A-RFC* — ReplicatedAttestationFrontierComposition tests

```text
A-RFC1    In a frontier domain (trust cap 0.7), a claim with
          ReplicatedAttestation (3 constituents, disjoint_affiliations)
          reaches effective_trust_cap = 0.80. The claim's trust
          exceeds the domain's frontier cap. Downstream trust
          decisions use 0.80 for this claim.

A-RFC2    Domain promotion to AUTHORITATIVE remains blocked (requires
          0.85) despite individual claims carrying 0.80 trust.
          Domain stage trust score respects the frontier cap (0.7).
          Promotion only unblocks after frontier exit per §4.4.1.
```

## 9m. Environment composition, coordination, and rule admission tests (A-EC*, A-CA*, A-ER*)

v1.1 addition (ADR-0045, ADR-0052, ADR-0053, [`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md), [`05_ENVIRONMENT.md §2.2a`](05_ENVIRONMENT.md), [`05_ENVIRONMENT.md §2.2b`](05_ENVIRONMENT.md), [`01_KERNEL.md §13.7`](01_KERNEL.md)). Tests exercise environment composition (hierarchical nesting with rule cascade), the coordination_propose kernel admission gate, and dynamically-authored executable EnvironmentRules enforced under safety-floor source 8.

### A-EC* — EnvironmentComposition tests

```text
A-EC1     EnvironmentComposition creation with cascade_mode = "inherit_all":
          child env inherits ALL parent charter rules. Child's charter
          contains parent rules + child-specific additions.

A-EC2     Child env attempts to weaken a safety-critical parent rule
          (tagged safety_floor_source). Kernel REFUSES the charter
          amendment with "safety_cascade_violation".

A-EC3     Child env adds a stricter rule beyond parent's charter.
          Kernel ACCEPTS. Child charter now contains parent rules +
          child's stricter rule.

A-EC4     Child env relaxes a non-safety parent rule with parent
          consent (parent persona signs approval). Kernel ACCEPTS.
          Child charter updated; lineage records parent consent.

A-EC5     Parent rule cascade verified at child env formation:
          ChildEnvFormationProposal with cascade_mode = "inherit_all"
          produces child whose charter includes all parent rules at
          formation time.
```

### A-CA* — Coordination admission tests

```text
A-CA1     Persona proposes coordination shape via ProposedCoordinationShape.
          Kernel validates schema against meta-mechanism (EntityGroupShape,
          BatchOperationShape, etc.). Schema-invalid shape REFUSED with
          "schema_validation_failed".

A-CA2     Coordination shape that would bypass safety floor source
          (e.g., a StagedSequence with no lineage events on stage
          transitions) REFUSED with "safety_floor_bypass_detected".

A-CA3     Shape with composition_depth > 3 REFUSED with
          "max_composition_depth_exceeded".

A-CA4     Cross-env coordination shape (scope = "env_to_env") requires
          bilateral consent (CrossEnvCoordinationRequest + Response).
          Shape activated without receiving env consent REFUSED.

A-CA5     Safety-critical shape in safety_critical=True environment
          requires operator co-sign before advancing past candidate
          stage. Advancement without operator co-sign REFUSED.
```

### A-ER* — EnvironmentRule tests (env-rule/1, 05_ENVIRONMENT §2.2b)

```text
A-ER1     EnvironmentRule authored in EnvFormationProposal.proposed_rules
          enters stage="trial" on instantiation; a safety_critical rule
          holds env instantiation at consent_complete until the C2 /
          MultiPrincipalAttestationQuorum gate clears (env_rule_ratified).

A-ER2     An accepted rule fires at a declared enforced_at admission point;
          failure_action="refuse_action" denies via source-8 most-
          restrictive-wins, and a signed VerifierInvocationEvidence record
          + env_rule_refusal event are appended (prose-only verdict rejected).

A-ER3     failure_action="warn_and_log" / "escalate_operator" emit
          env_rule_warned / env_rule_escalated WITHOUT denying the action.

A-ER4     A safety_critical rule (hazard axes ≥ C2 threshold) cannot reach
          stage="accepted" without operator approval; under principal
          collapse the degraded gate (01_KERNEL §2.4) applies.

A-ER5     EnvironmentRule rides UNDER source 8: the safety floor still
          reports 8 sources (A-K2 unaffected); a rule refusal composes with
          other sources by most-restrictive-wins and may only ADD refusals.

A-ER6     A parent EnvironmentRule with cascade_locked=True is inherited by
          a child env at formation (inherited_from_parent_env_id set); a
          child charter amendment weakening it is REFUSED with
          env_child_charter_amendment_refused (safety_violation).

A-ER7     rule_kind resolves against KindRegistry env_rule_kinds
          (code | rule_engine | contract); an unknown rule_kind triggers the
          proposal / probe-extension flow, not a substrate enum branch.

A-ER8     Worked examples enforce: a contract rule (rule_kind=contract,
          enforced_at=[output]) refuses a non-conforming shipment; a sandboxed
          robot-performance code rule refuses an out-of-spec result; a chip
          buildable/orderable rule_engine rule refuses a non-orderable BOM.

A-ER9     Backward compatibility: an env whose charter carries no rules
          (env_rules / rule_refs empty) behaves exactly as a pre-v1.1 env;
          source-8 evaluation is unchanged.
```

## 9n. Discovery, access & hybrid distribution tests (A-DR*, A-DT*, A-AX*, A-CL*, A-TF*, A-HR*)

### A-DR* — DiscoverableRecord + cards (09_PROTOCOLS §3G.1)

```text
A-DR1     Every content type (persona/env/project/domain/artifact/telemetry/
          knowledge/skill/tool) projects a DiscoverableRecord; ArtifactCard
          (artifact-card/1) and TelemetryCard (telemetry-card/1) validate.
A-DR2     The four v1.0 cards still validate at their original schema ids;
          the added access_policy_ref + discover semantics are additive
          (a v1.0-only consumer ignores them).
A-DR3     A record with no body carries no content_hash/ContentLocator; one
          with a body carries exactly one (hash for stored, locator for hybrid).
```

### A-DT* — Two-plane discovery transport (09_PROTOCOLS §3G.2)

```text
A-DT1     Internet plane: a federation/public DiscoverableRecord is published
          to the Kademlia DHT as a signed ProviderRecord and resolves by
          content_hash / DID / handle.
A-DT2     Intranet plane: with no internet route, two kernels on the same LAN
          discover each other's records via mDNS (no central registry, no
          pre-shared peering).
A-DT3     Bridging respects visibility_tier: a persona_only / project_only /
          tenant / intranet-scoped record is NEVER re-published to the
          internet DHT; only federation/public records bridge outward.
```

### A-AX* — Access-gated discovery + AccessPolicy (09_PROTOCOLS §3G.3-§3G.4)

```text
A-AX1     access_level ladder enforced: discover < read < write < admin; a
          discover-only principal sees a record + minimal metadata but a body
          fetch / skill invoke is REFUSED until read+.
A-AX2     A persona_only / private record never appears in DHT, mDNS, or gossip
          results to an unauthorised principal (no enumeration leak).
A-AX3     access_level enum widening is additive: existing r / rw grants
          behave exactly as v1.0 (artifact-share/1 unchanged); A-AB23 still
          passes.
A-AX4     Effective access = intersection (most-restrictive-wins) of grant ∩
          outward tier ∩ EnvironmentComposition-inherited policy ∩ source-8
          EnvironmentRule; composes with safety floor (01_KERNEL §2.1).
```

### A-CL* — ContentLocator hybrid storage (09_PROTOCOLS §3G.5, 07_ARTIFACTS §10a)

```text
A-CL1     Round-trip: publish a ContentLocator (provider_kind=github) →
          discover it over P2P → fetch from the provider under the consumer's
          own credential → verify bytes against content_hash → success.
A-CL2     Integrity: a content_hash mismatch on fetch FAILS CLOSED and emits a
          signed CONTENT_INTEGRITY_FAILED lineage event.
A-CL3     Availability: primary provider outage falls back to the next entry
          in replica_tiers (e.g. oci → github → ipfs_pin).
A-CL4     Live-reference verification emits CONTENT_LOCATOR_STALE when
          provider_native_ref no longer resolves or no longer matches the hash.
A-CL5     The substrate stores neither the user's bytes nor credentials — only
          the signed locator + content_hash + credential_requirement descriptor.
A-CL6     ContentLocator subsumes content_kind=external: a v1.0 external ref
          migrates to a locator with an added content_hash anchor (A-AB11 flow).
```

### A-TF* — Federated consent-gated telemetry (09_PROTOCOLS §4.1)

```text
A-TF1     A TelemetryCard feed defaults private; an unauthorised peer cannot
          subscribe (discover-only sees the card exists, nothing more).
A-TF2     Default redaction: below a consented tier the feed exposes only span
          kinds / status / durations / lifecycle+presence transitions — never
          prompt / completion / artifact / DM content.
A-TF3     A higher-tier subscription requires BOTH a read+ AccessGrant AND a
          ConsentLedger pin; revoking the pin terminates the feed.
A-TF4     Federated presence resolution ("where is persona X now") is OFF by
          default and exposes focus KIND + status only, never focus content.
```

### A-HR* — Host-replication / BFT standby (09_PROTOCOLS §3C.2)

```text
A-HR1     A joined env with a standby_replica_set survives host loss: BFT
          quorum sign-off promotes a standby without full Blackboard replay.
A-HR2     Split-brain prevented: under partition only the majority-quorum side
          promotes a host; the minority side stays STALLED.
A-HR3     With no standby_replica_set configured, behaviour is exactly v1.0
          (host loss ⇒ STALLED + heavyweight host_handoff).
```

### A-RA* — Reachability & availability (09_PROTOCOLS §3H, 07_ARTIFACTS §10a)

```text
A-RA1     Intranet/same-LAN: a phone-kernel on the same LAN as a NAT-private
          home kernel discovers its personas via mDNS with NO internet route,
          and reads progress/artefacts at read+ (intranet_only profile honoured).
A-RA2     NAT traversal: a nat_private home kernel is dialable from an off-network
          peer via circuit-relay v2 + DCUtR; the resolver returns relay-reachable
          multiaddrs, not a bare host id.
A-RA3     Liveness honesty: when the origin node is OFFLINE, an online_only record
          is unfetchable and the consumer gets an informative not-reachable result
          (no false "exists+available").
A-RA4     Availability fallback: an AvailabilityPolicy=replicated (or pinned)
          bundle is fetched from a replica/pin while the origin is offline, and
          the bytes verify against content_hash.
A-RA5     Availability never widens access: a replica/pin fetch still enforces
          AccessPolicy — a discover-only or unauthorised principal is refused
          at read regardless of where the bytes are served from.
A-RA6     Commons-optional sovereignty: an operator-run relay+pin (no third-party
          commons) yields the same A-RA2/A-RA4 outcomes.
```

## 9o. emergent orchestration tests (A-EO*)

Tests for the [ADR-0066](14_DECISIONS.md#adr-0066--self-organizing-orchestration-the-run-loop-is-an-emergent-coordination-shape-not-a-fixed-dispatcher) reframe: task classes, acceptance pathways, and the run loop are emergent (the v1.0 set seeded as STANDARDISED), fully open, and made safe by trust-calibration rather than topology restriction. Anchored in [`03_TASKS.md §2a`](03_TASKS.md#2a-orchestration-is-emergent--classes-pathways-and-the-run-loop-are-coordination-shapes), [`00_VISION.md §3 (J4)`](00_VISION.md#3-invariants-j1j9), and [`15_COORDINATION_SHAPES.md §4a`](15_COORDINATION_SHAPES.md#4a-orchestration-scope--coordinating-the-task-execution-loop).

### A-EO — emergent, fully-open, trust-calibrated orchestration

```text
SEED-KIND COMPATIBILITY

A-EO1     The ten v1.0 task classes and eight acceptance pathways resolve as
          STANDARDISED seed kinds from the KindRegistry; the seed class→pathway
          mapping (J4 A.1 table) is unchanged and A-T2–A-T11 still pass.
A-EO2     Substrate code resolves a class/pathway by name from the registry;
          a build that branches on a closed Literal[...] of class or pathway
          names fails the C4 purity check (A-C4 / A-EK*).

PERSONA-PROPOSED ORCHESTRATION (FULLY OPEN)

A-EO3     A persona proposes a novel AcceptancePathway kind; the kernel admits
          it for trial and MUST NOT refuse it solely because it is novel.
A-EO4     A persona proposes a novel TaskClass kind; classifier (§2.1) and
          demotion ladder (§2.2) operate over the resolved kind set including it.
A-EO5     A persona proposes a new acceptance primitive (meta-mechanism beyond
          the five) when none fits; it enters promotion, not refusal.
A-EO6     The run loop / phase arc declared as a StagedSequence in the
          EnvironmentCoordinationProfile executes; the INVESTIGATIVE four-phase
          arc resolves as a STANDARDISED seed StagedSequence, not a kernel constant.

TRUST-CALIBRATION IS THE SAFETY MECHANISM

A-EO7     A verdict produced by an EMERGENT (unvalidated) acceptance pathway
          carries EMERGENT trust; the AnswerPackage records the producing
          orchestration kind and its promotion stage.
A-EO8     Floor + signing are never bypassed: every action under an emergent
          orchestration shape is signed (J2/J9), floor-cleared (J3, 8 sources,
          most-restrictive-wins), and budget-admitted (INV-7) — a shape that
          attempts to skip any of these is refused at validation (§8 / A-CA*).

OPERATOR CONTROL

A-EO9     A safety-critical proposed pathway/shape requires C2 operator co-sign
          before promotion; absent it, it remains at EMERGENT trust.
A-EO10    Operator policy (floor source 4) pins a minimum-trust or specific seed
          pathway for a task family; a lower-trust emergent pathway is refused
          for that family while the pin holds.

PROMOTION LADDER (03_TASKS §2b)

A-EO11    An emergent acceptance pathway auto-promotes EMERGENT → RECOGNISED
          only when the §2b.2 threshold holds: ≥ K=5 distinct accepted tasks
          across ≥ M=2 principals/envs, soundness agreement ≥ 0.90 vs an
          independent reference (shadow seed pathway or post-hoc ground truth)
          with zero unreviewed false-accepts, zero floor/signing violations,
          and proposer fitness > role median. An under-evidenced pathway (any
          criterion unmet) stays EMERGENT; a safety-critical pathway does not
          auto-promote and requires the C2 blocking signature.
A-EO12    Verdict trust follows the asymmetric-EWMA curve (§2b.1): a
          disconfirmation moves pathway_trust toward 0 faster than a
          corroboration moves it toward 1 (α_down > α_up), and an unused
          pathway decays toward the EMERGENT floor on the staleness half-life.
          A RECOGNISED pathway demotes one stage on trust collapse OR on N=3
          consecutive disconfirmations, emitting a signed
          orchestration_kind_demoted event; already-accepted tasks are not
          retroactively reopened but their AnswerPackage records the stage.
A-EO13    Operator policy profile (floor source 4): under bounded_compositional,
          a proposed NEW kernel-level acceptance primitive is refused with a
          signed orchestration_primitive_refused_by_policy advisory while a
          NOVEL COMPOSITION of STANDARDISED seed primitives is admitted (and
          trust-calibrated); under fully_open (default) both are admitted. The
          profile never relaxes the floor (J3) or signing (J2/J9).
```

## 9p. Global object space tests (A-GLOBAL*, A-XD*, A-SCHED*) — ADR-0067/0068/0069

### A-GLOBAL* — global handles + cross-node verification + access-gated reference (ADR-0067)

```text
A-GLOBAL1 Every first-class entity (persona/env/project/domain/artifact/
          knowledge/skill/tool) resolves by a global handle (DID over its
          ULID, 01_KERNEL §4.4) in addition to its ULID; ULID remains the
          local primary key (no schema-version bump).
A-GLOBAL2 A signature rooted in node A verifies on node B by DID resolution
          against A's published .well-known/personaos-keys.json; J1/J2/J9
          guarantee holds globally.
A-GLOBAL3 Access-gated reference: a principal with < discover on an entity's
          AccessPolicy never sees it in ANY discovery plane (DHT, mDNS,
          gossip); discover < read < write < admin composes
          most-restrictive-wins.
A-GLOBAL4 J1 reframe regression: a body still cannot edit a Soul; Souls are
          kernel-signed; mutations signed + lineage-tracked — the guarantee
          is unchanged, only locality is lifted.
```

### A-XD* — cross-env / cross-node task delegation (ADR-0068)

```text
A-XD1     Cross-env DELEGATED via a CrossEnvCoordinationBinding whose
          interface carries a task is dual-signed by both envs/nodes;
          inherits sub-task class/pathway (§2.6); max_delegation_depth
          honored across the boundary.
A-XD2     A delegation whose submitter lacks the submit/write capability
          (UCAN) on the target is REFUSED before the receiver's review.
A-XD3     Remote placement composes floor + budget most-restrictive-wins
          (as joined-env execution, 09_PROTOCOLS §3C.3).
A-XD4     A cross-domain sub-task inherits the MINIMUM of (parent, resolving)
          domain trust (OQ-TASKS-3).
A-XD5     CrossEnvPresenceQuery is access-gated: member → full presence;
          discover-only → existence; unauthorized → nothing.
A-XD6     CrossEnvLineageVisibility redacts by default (link + event kinds,
          payloads withheld); never widens access.
```

### A-SCHED* — owned-node multi-tenant priority scheduling (ADR-0069)

```text
A-SCHED1  Under the owner-first seed SchedulingPolicy, an owner task is
          ordered ahead of a concurrently-queued external task.
A-SCHED2  Priority never bypasses permission: an OWNER task that fails the
          8-source floor is refused exactly as any other — order changed,
          not permission.
A-SCHED3  The task_intake gate enforces the per-submitter-class quota /
          rate-limit; over-quota external submission → TaskIntakeRefused.
A-SCHED4  Ageing prevents starvation: a low-priority task eventually rises.
A-SCHED5  Submitter identity (submitter_kind/_id/_node) is persisted in the
          AnswerPackage and lineage; audit can answer "who submitted this,
          at what priority class?".
A-SCHED6  task_intake is distinct from the INV-7 budget gate: an authorized
          submitter still hits the hard budget gate at budget_tick; budget
          headroom never implies intake authorization.
A-SCHED7  An operator-authored non-default SchedulingPolicy is honored but
          cannot reorder the floor or the INV-7 hard gate, nor grant a class
          more than its AccessPolicy capability.
```

## 9q. Continuous refinement mission tests (A-REF*) — ADR-0071

```text
A-REF1    A ContinuousRefinementMission iterates over an artefact bundle,
          keeping best-so-far; an inferior candidate never regresses the
          accepted best (anytime semantics).
A-REF2    Convergence: when the MarginalValueMetric (objective-vector gain)
          stays < epsilon for N consecutive rounds, the mission emits
          converged / no_further_improvement and returns best-so-far.
A-REF3    Budget-scaled quality: with a larger budget, per-round candidate
          breadth (min(objective-headroom, candidates_remaining)) is higher
          and the final objective vector is measurably better — quality is
          monotone non-decreasing in budget.
A-REF4    Auto-reopen: an active, un-converged mission in paused_budget
          resumes from best-so-far on budget replenishment without a manual
          fork; a converged mission stays closed unless MissionObjective
          changes.
A-REF5    Three-condition termination: the mission stops on the FIRST of
          convergence, user/operator stop (user_terminated /
          operator_terminated), or INV-7 budget_exhausted.
A-REF6    Budget->emergence: an improvement-blocking capability gap + budget
          headroom raises population-pressure factor 7, triggering
          recruitment-exhausted-first then genesis of the needed specialist
          and/or an EnvFormationProposal sub-env; all ReplicationBound-capped
          and operator-cosigned; with no budget headroom, no genesis fires.
A-REF7    Floor/INV-7 integrity: a refinement action that fails the 8-source
          floor is refused exactly as any other; refinement never bypasses
          the floor, signing, or the INV-7 hard budget gate.
A-REF8    Bounded autonomy: per-round sub-goals are CharteredElaborations
          within the MissionCharter drift bounds; an attempt to elaborate a
          NEW top-level goal outside the bounds is refused.
```

## 9e. Risks & known limitations

Per [`SPEC_CONVENTIONS.md §7`](SPEC_CONVENTIONS.md#7-risks--known-limitations). This section captures risks intrinsic to the *catalogue itself* — risks intrinsic to the underlying mechanisms are recorded in the doc that defines each mechanism.

| ID | Risk | Severity | Likelihood | Mitigation | Target release |
|----|------|----------|------------|------------|----------------|
| R-AT-1 | Test drift. A test passes against an out-of-date schema or behaviour, masking a real regression. | High | Medium | Each test references the spec section that defines the behaviour; CI flags tests whose target schema version has bumped without a test review. | v1.0 (CI hook); v1.1 (auto-bump suggestions). |
| R-AT-2 | Flaky tests on round-based pathways. Wall-clock-sensitive timeouts (INV_R11, A-K3) can flake under load. | Medium | High | Generous default budgets with per-deployment overrides; CI quarantine for flaky tests until root-caused. | v1.0 (quarantine pipeline). |
| R-AT-3 | Coverage gaps for emergent kinds. KindRegistry-driven entities (env types, artifact kinds, domain kinds) cannot all be enumerated; the A-EK* family covers substrate-purity, not every emergent kind. | Medium | High | Substrate-purity invariants (A-EK*) sufficient by construction; emergent-kind-specific tests added when a kind reaches `AUTHORITATIVE` per [`06_DOMAIN.md`](06_DOMAIN.md). | v1.0 (substrate tests); v1.1+ (emergent-kind coverage as kinds promote). |
| R-AT-4 | Human-bridge tests (A-HB*) depend on physical assets and external participants; harness cannot fully automate. | Medium | High | Manual operator sign-off paths documented in [`§8a`](#8a-human-bridge-tests-a-hb--physical-world-coupling); test status `SKIPPED` admissible at certain gates with operator audit. | v1.0 (operator-signed harness). |
| R-AT-5 | Migration tests (A-M19*) one-shot; cannot be re-run easily after migration completes. | Low | Low | Migration tool emits signed `migration-complete` event with test report attached; re-run mode for staging environments. | v1.0 (one-shot semantics); v1.1 (replay harness). |
| R-AT-6 | Per-release gate matrix may diverge from the release gate process. | High | Low | Single source of truth: the release gate process; this doc references gate test IDs, release gates define which tests must pass. CI cross-checks. | v1.0 (CI cross-check). |

## 9f. Open questions

Per [`SPEC_CONVENTIONS.md §8`](SPEC_CONVENTIONS.md#8-open-questions).

| ID | Question | Owner | Resolves into |
|----|----------|-------|---------------|
| OQ-AT-1 | What is the budget for total test runtime per CI cycle? Current ~320 tests; some are expensive (sandbox escape, lineage replay at 10^6 events). Need empirical baseline and budget. | QA + Operator | v1.1 budget table in §5. |
| OQ-AT-2 | Cross-node federation testing requires a multi-node staging environment (≥ 2 nodes). | QA + Federation | **Resolved (normative):** the A-GLOBAL*/A-XD*/A-SCHED* families (§9p) exercise cross-node discovery, delegation, and scheduling against a 2-node staging harness; an empirical N-node load matrix is operator tuning, not a gate. |
| OQ-AT-3 | Anti-Goodhart panel acceptance threshold tuning: tests assume a fixed disagreement-rate threshold; should it be operator-tunable per deployment? | Safety WG | v1.1 panel policy. |
| OQ-AT-4 | Test ID renaming: `A-PR*` (presence) vs `A-PT*` (protocol) once collided. Are there other latent collisions in the future namespace? | — | v1.1 ID-scheme audit. |
| OQ-AT-5 | Should `SKIPPED` count toward gate-pass criteria? Currently a `SKIPPED` with operator sign-off is admissible; tighten policy in safety-critical deployments. | Operator policy | v1.1 deployment profiles. |

## 10. Where to read next

- Release gates reference these tests
- Top-level vision: [`00_VISION.md`](00_VISION.md)
- Glossary: [`12_GLOSSARY.md`](12_GLOSSARY.md)
