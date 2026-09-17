# Core implementation contract and next changes

[Canonical specification](SPEC.md) · [Current status](../STATUS.md) · [Acceptance](ACCEPTANCE.md) · [Release plan](RELEASE.md)

**Scope: the Rust core only.** This is an implementation companion to the supplied v1.2 specification, not another runtime, a new public API, or a claim of implementation. `SPEC.md` remains normative. No UI, prototype, stylesheet, generated API, or federation transport is changed by this increment.

The machine-readable [core gate plan](core-gates.json) carries the same implementation scope and requirement IDs. It is a planning manifest, **not a Rust-generated command schema**. Logical operations below must be mapped to the existing typed Rust commands or implemented there before they are exposed.

## 1. Baseline and what not to rebuild

The September 16 specification inspected Rust commit `d3339d30fa883c21c7935a2d009e3a58f480a256`. A fresh branch read resolves `ai-personas/ai-personas`, `rewrite/design-first`, to `c2b7d89a7d05f7f31e35d590ba39a3fcf80439fa`. The requested design branch started this update at `52bdbfadc3dc77ce15e3cb376036c7293acad5da`.

The [current runtime implementation report](https://github.com/ai-personas/ai-personas/blob/c2b7d89a7d05f7f31e35d590ba39a3fcf80439fa/docs/RUST-V1.2-IMPLEMENTATION.md) reports a foundational source increment for completion barriers, non-success receipts, explicit yield, run-scoped selections/compaction/images, legacy-context handling and two ownership guards. It explicitly says its Rust tests were not compiled or run when prepared. Treat these as **reported source changes requiring execution**, not missing designs to recreate and not passing gates.

The runtime [README at the same revision](https://github.com/ai-personas/ai-personas/blob/c2b7d89a7d05f7f31e35d590ba39a3fcf80439fa/README.md) still describes process inference and unsandboxed host execution. HTTP inference, containment, a full authority/funding boundary, typed group records and currentness/release enforcement remain implementation work. This update did not independently compile or execute the runtime.

Keep the historical defect and failures. Do not describe the original pending-action defect as an executable failure reproduced on the newer commit. Preserve the existing transactional newer-input check in `wait`. Local actor notification work belongs in runtime/store; `delivery.rs` retains its continuity-forwarding purpose.

The runtime repository is private. Do not copy its source, logs, credentials, node state or build artifacts into this public design repository to obtain a public runner. Links and source identifiers are not permission to republish private contents.

## 2. One transactional authority, three execution contexts

Follow specification sections 5, 8, 13, 15 and 17. Extend the existing SQLite `Store::write` boundary; do not create an independent grant, budget or population database.

| Concept | Persistent meaning | Forbidden shortcut |
|---|---|---|
| Work | The continuing need, original request, accepted mandate and outcome history | Replacing the original need with the latest team summary |
| ExecutionRoot | One authorized and funded episode, shared by all participating descendants | Treating each persona run as a fresh team budget |
| Participation run | One persona's decision/participation context in a work, bound to its root | Sharing active memory or authority with the persona's other work |
| BootstrapContext | Restricted newborn initialization before membership | An empty work/run ID implying unrestricted access |

The actor lease spans participation and bootstrap contexts. Two work contexts cannot give one identity two simultaneous decision leases. Neither a model response nor a generic record body may select a different actor, funding root, authority epoch or lease fence.

### Admission and replay

For each authenticated command, use the existing identity/revision formats and the following transaction boundary:

1. Check access to the requested scope before looking up or returning a prior receipt. Resolve the actual actor and causal context; normalize typed arguments and compute the request digest on the server.
2. The same authorized actor/operation identity and digest returns its existing receipt. Changed arguments conflict. A different actor cannot inspect another actor's receipt by guessing an operation ID. Do not silently change the baseline ID namespace during migration.
3. For a new mutation, check current grants, membership or bootstrap rights, cancellation epoch, lease fence, expected heads and the relevant versions actually observed by the call. A newer value fetched during admission is not evidence that the model considered it.
4. Reserve the applicable resource allocation and capacity. Commit record versions, head updates, action or job intent, and addressed notification/outbox entries together.
5. Dispatch only committed intents outside the database transaction. Record actual outcomes, usage uncertainty and delivery state. No network request, installer, inference call or arbitrary process runs while holding the store transaction.

Canonical normalization must reject duplicate JSON keys and ambiguous numeric encodings at the digest boundary. A digest establishes request integrity, not persona cryptographic authorship or technical correctness. A unique constraint plus transactional admission must arbitrate concurrent identical requests; a preflight lookup alone is insufficient.

After an ambiguous outside effect, preserve `effect_unknown` and reconcile before retry. Local idempotency cannot promise exactly-once behavior at arbitrary destinations. Cancellation blocks new admissions; late receipts remain accounting evidence but cannot adopt results into canceled work.

## 3. Calls, pending effects, waits and protected closeout

Follow specification sections 9, 10, 13 and 17. Verify the reported barrier increment first, then integrate it with root funding and fences rather than building a competing batch executor.

| Situation | Required transition |
|---|---|
| Successful synchronous receipt | The next command may be admitted under fresh mechanical guards |
| Pending asynchronous action | Retain the unapplied suffix as not admitted; permanently suppress automatic replay of that suffix |
| Terminal failure or unknown effect | Stop the batch; preserve earlier receipts and expose the diagnostic |
| Effect finishes before restart | Its old suffix still cannot be resurrected; a fresh decision must observe the receipt |
| Empty decision | Explicit bounded yield/await/quiescence, not unlimited idle cognition or task completion |
| Terminal event races await registration | In one transaction, either the predicate is already satisfied and the run remains runnable, or a durable wait/notification is installed |
| Inbox acknowledgement | Acknowledge delivered input only; do not resolve a finding or accept an outcome |

A foreground job awaits its actual terminal outcome. A background job can coexist with independent work selected in a subsequent funded decision. Do not infer independence from narrative prose. Authoritative changes and current blockers enter the mandatory core independently of ordinary message pagination.

Reserve a call before HTTP dispatch. All initialization, descendants, retries, compactions and reviews consume the same root or a conserved sub-allocation. Calls, tokens, currency, time, storage and capacity remain distinct dimensions. For every dimension with an enforceable ceiling:

```text
consumed + uncertain exposure + outstanding reservations <= authorized allocation
```

Unknown exposure is not a refund. A hard currency limit with no trustworthy price upper bound must deny the spend or request another authorized bound. Do not relabel a call allowance as a money guarantee.

The principal/resource delegate may protect review, bounded repair and reporting allocations inside the same root ceiling. Ordinary exploration, birth and metadata work cannot use them without an authorized transfer. No universal percentage is prescribed. Mechanical stopped-state reporting must not depend on one more funded model call.

Narrative activity does not reset finite root/self-wake limits. Track activity separately from artifact/check/request-disposition changes. Deliver bounded, deduplicated no-progress observations to accepted continuation owners; the runtime does not judge the semantic worth of their ideas.

## 4. Continuing identities, fragments and consent

Follow specification sections 3–10. Keep identity, preference, capability evidence and accepted responsibility separate. No profession registry, OCEAN-to-tool mapping, aggregate group personality or universal priority score is introduced.

| Record or transition | Required core guard |
|---|---|
| Character, modeled state, agenda, relationship perspective | Attributed self-authorship, visibility and exact revisions; relationship interpretation remains directional |
| Fragment write/revise | Owner, sources, applicability, limitations, counterevidence and supersession; preserve ordinary documents as documents |
| Context selection/compaction | Default active scope is persona/work; preserve mandatory current constraints, grants, cancellations and unresolved blockers |
| Agreement endorsement | The actual endorser accepts the exact version; no invented unanimity or authority obtained through votes |
| Commitment offer/accept | Offering work to a peer does not bind that peer; only its acceptance or accepted delegation creates responsibility |
| Continuation acceptance | Work is awaiting acceptance/unowned until someone accepts an honest continuing disposition; this does not create a compulsory leader |
| Handoff | Offer, consent and current-ownership check; the previous owner remains accountable until transfer or authorized cancellation |

The shared board is unranked unless a participant explicitly authors a scoped ordering. Individual agendas remain visible beside missing owners and uncovered outcomes. Coverage is coverage of adopted outcomes; material scope review must also check the original need and accepted clarifications.

Birth must atomically reserve authorized capacity and initialization resources, create one distinct identity/provenance/seed manifest, persist a restricted bootstrap context, and emit one deduplicated wake. Check seed read/share rights again at use after revocation. The newborn receives no credentials, parent worktree, general execution right or cloned budget.

A restricted invitation preview allows an informed accept/decline before membership. Membership acceptance atomically creates its attenuated work grant and participation context; commitment acceptance remains separate. Decline does not automatically trigger replacement births. Initialization retries are bounded; dormancy may free active capacity without resetting total birth/rate counters. Outstanding commitments require explicit handoff, cancellation or visible blocked ownership.

A persona may remain interested without claiming expertise. Receiving a fragment is not first-hand experience. Installation, representative operation, project use and reviewed outcome competence are distinct. Useful learning and useful birth require later behavioral evidence, not counts or biographies.

## 5. Assumptions, actionable feedback and negotiated iteration

Follow specification sections 5, 6, 9, 10 and 14. The minimum distinction is between an authored hypothesis, permission to explore it, an observed fact and a qualifying claim.

An assumption records its source, affected claims, interpretation/range, validity conditions and disposition. `authorized_for_exploration` never implies `confirmed_by_evidence`. Conditional evidence may qualify the corresponding conditional claim only. Changing an assumption invalidates dependent applicability like any other input change.

Actionable feedback binds the exact subject version, accountable commitment, required disposition and adopted blocking policy. Accept with linked repair/check, dispute with evidence, defer/waive with the actual authority, or escalate. Message delivery, acknowledgement, response and verified repair are different facts. A blocking finding cannot disappear through acknowledgement, compaction or a friendly group summary.

Participants may agree on interfaces and bounded iterations using ordinary versioned agreements. Distinguish `requires_version_ready` from `requires_final_acceptance`. A provisional version is usable only for explicitly bounded exploration whose claims retain the limitations. Cycles of final prerequisites create visible deadlock observations; the personas negotiate the repair.

An iteration records its baseline version vector, provisional interfaces, checks/questions, finite allowance and stop/escalation conditions. Independent alternatives use isolated copies. Coupled canonical adoption checks and replaces the entire compatible version vector atomically; partial uploads are not an adopted integrated assembly. The runtime checks authority and references, not architectural or engineering convergence.

## 6. Providers and tools are prerequisites, not final polish

Follow specification sections 11–13. Do not start funded autonomous tool campaigns until direct HTTP inference, scoped authority and enforceable containment pass on the actual Rust paths.

The supported inference path must not spawn Codex app-server, another autonomous CLI or an executable provider bridge. Replace both the adapter and implicit startup registration/defaults. Test fixtures may retain process-shaped scaffolding, clearly separated from supported inference. Configure exact endpoints, credentials, model IDs and capability metadata; do not infer media, context-window or pricing support from model names.

Provider conformance must cover complete structured decisions, exact requested/reported model IDs, usage or explicit unknowns, cancellation, rate limits, timeouts, malformed/partial output, refusal, context overflow and the authorized model ceiling. Never execute partial streamed commands. Keep credentials server-side and continuation material confidential. Any optional subscription adapter needs its own supported endpoint/authentication evidence; do not treat a subscription token as an ordinary platform credential.

Generic tool execution requires immutable recipe/input references, unambiguous argv or shell source, explicit environment, isolated writable scope, resource/deadline/network bounds, managed process/session lifetime and retained output/termination receipts. Installation is untrusted execution. Do not expose the node home, keys, unrelated work or assessor material. Fail closed when required isolation is unavailable; a process group or a permission label is not containment.

Credential mediation must enforce effect scope at execution, not merely trust a hostname or a program saying it is read-only. Check resolved paths/tool bytes/destinations without a substitution race. A publish operation may read only authorized snapshot bytes, not arbitrary host paths. Physical effects and external publication remain separately authorized.

## 7. Evidence applicability and atomic release

Follow specification sections 14–18. Keep the following chain inspectable:

```text
accepted original need / criterion version
  -> accepted commitment
  -> exact observed input versions and assumptions
  -> actual action / observation receipt
  -> immutable native output and assembly
  -> claim-specific assessment under exact review policy
  -> current applicability and release disposition
```

A submission seals exact versions, criteria, assumptions and limitations. A qualifying assessment binds the claim/criterion, assembly, inputs, review policy, reviewer/conflict disclosures, performed checks, verdict and limitations. Separate identity, independent execution, distinct reasoning evidence and professional review are not interchangeable.

Changed criteria, input, assumption, assembly or review policy make the old verdict inapplicable to the new scope. Preserve the historical verdict. When declared impact is incomplete, conservatively invalidate the whole affected scope; an asynchronous invalidator must immediately expose `revalidation_pending`, not a stale current pass.

Final release checks the current mandate, criteria, assumptions, assembly vector, review policy, qualifying assessments, blockers, expected heads and root cancellation/authority epoch **in one transaction**. Reject any relevant intervening change. When the release wins the race, it remains immutable history while a later candidate proceeds.

Expose independent activity, ownership/coverage, submission, applicability/review, principal acceptance, outside evidence and optional-improvement axes. `answered` is not `resolved`; an approval is not a fact response. `delivered_with_conditions`, `partial_delivered`, `blocked_external` and `unaccepted` cannot be collapsed to a single done badge. An explicitly accepted limited result must retain its limits.

No current pass may be assembled from an old review and new inputs. A completed run is not a completed need. House/circuit/domain requirements belong in frozen acceptance fixtures and acquired validators, not kernel branches. Native design, actual calculations and reproducible checks are required where adopted; an intent paragraph or image is not their substitute.

## 8. Implementation batches and exit evidence

These are dependency-ordered engineering batches, not a runtime workflow imposed on personas.

| Batch | Core deliverable | Exit evidence |
|---|---|---|
| K0 | Reproduce the reported barrier/yield/context increment | Locked Rust build, staged-receipt tests and real delayed-writer/old-file tests; failures retained |
| K1 | Single-store admission, root funding, leases, cancellation, inbox/outbox and scoped API | Real concurrent/restart/idempotency/privacy/resource tests; unknown costs/effects preserved |
| K2 | HTTP adapters and isolated supervised tools | Mock-HTTP conformance plus containment/credential/effect negative tests; no autonomous live tools before these pass |
| K3 | Typed fragments, individual context, mandates, continuation/coverage, agreements and commitments | Public-API consent, cross-work memory, mandatory-core and ownership tests |
| K4 | Restricted birth bootstrap, lifecycle, protected closeout and conserved population resources | Atomic race/retry, pre-membership-access, decline, handoff and no-budget-minting tests |
| K5 | Assumptions, persistent feedback, version-ready interfaces and bounded iteration | Conditional-claim, acknowledgement-versus-disposition, cycle/iteration and current-observation regressions |
| K6 | Exact artifacts, scope assessment, staleness, assembly CAS and release | Both update-versus-release orderings; no old pass on new scope; outside obligations retained |
| K7 | Small real cooperation, correction transfer, useful birth/restraint, then house and unrelated needs | Repeated matched B01–B12 evidence with actual outputs and independently frozen criteria |

The machine plan maps every core mechanical gate M01–M26 except UI gate M14, plus B01–B12. M14 is deferred, not removed or passed; full product release still requires it. No core gate is marked verified by this design increment.

## 9. Run the checks without inventing results

In this design checkout:

```sh
python3 scripts/check_core.py
python3 -m unittest discover -s tests -v
python3 scripts/check_docs.py
```

Those commands validate documentation and helper behavior only. The existing documentation CI discovers the added Python tests without modifying UI code or its workflow.

On a disposable trusted Linux development host with the private Rust checkout and its toolchain:

```sh
python3 /path/to/ai-personas-design/scripts/verify_rust_core.py \
  --runtime /path/to/ai-personas \
  --expected-revision c2b7d89a7d05f7f31e35d590ba39a3fcf80439fa \
  --trusted-test-host
```

The runner verifies the requested exact clean revision, runs the existing fixture/build/barrier/behavior suites, stops at failure, and retains exit codes and logs in a private directory outside both repositories. For a future candidate, explicitly supply its full commit SHA. It does not switch branches, install tools, push, call a live provider, or claim to implement missing v1.2 tests. This runner provides no isolation. Keep production secrets and live nodes off the test host.

A successful runner result means **the selected existing suites passed for that commit**, not M01–M26 or B01–B12 all passed. An unavailable toolchain, failed check or interrupted run must remain visible. Private logs stay local and must not be automatically uploaded to the public design repository.

Core implementation still belongs in `ai-personas/ai-personas`. This design update changes neither that runtime's source nor its generated authoring contract. It makes the next changes and their evidence gates explicit while leaving the attached UI designs untouched.
