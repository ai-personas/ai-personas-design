# Rust implementation, migration and release plan

[Specification](SPEC.md) · [Core implementation](CORE.md) · [Acceptance gates](ACCEPTANCE.md) · [Current status](../STATUS.md)

The only runtime target is `ai-personas/ai-personas`, branch `rewrite/design-first`. The supplied v1.2 source audit remains pinned at `d3339d30fa883c21c7935a2d009e3a58f480a256`; the current implementation reference for this core increment is `c2b7d89a7d05f7f31e35d590ba39a3fcf80439fa`. Use the existing Rust stack, not another runtime. Requirements here are implementation and verification work, not Rust patches applied by this design commit.

For the current core-only phase, follow [CORE.md](CORE.md) and its [gate manifest](core-gates.json). They distinguish the reported barrier/yield/context source increment from the historical defect and supply an exact-revision private-checkout runner. UI work remains deferred; the broader product-release requirements below are retained, not silently waived.

## Change the existing boundaries, not the language

| Rust target | Required delta |
|---|---|
| `src/contract.rs` | Typed fragments, mandates, continuation, perspectives, agreements, commitments, roots/bootstrap/birth/consent, assumptions/feedback, scope-bound assessment and release; no unrestricted record writer that mints authority |
| `src/types.rs` | Preserve IDs/revisions; distinguish root, participation and bootstrap contexts; exact context/usage manifests and orthogonal outcome projections |
| `src/runtime.rs` | Transactional admission, authoritative context, fences/epochs, bounded calls, accepted responsibility, pending-effect barrier, suppressed suffix replay, intentional yield/quiescence |
| `src/store.rs` | Extend the same SQLite authority for grants/reservations/population, exact heads/links, local inbox/outbox, applicability and atomic assembly/release |
| `src/delivery.rs` | Preserve continuity-forwarding semantics; do not treat this as the whole local actor-delivery subsystem |
| `src/provider.rs` | Replace supported process inference with direct HTTP adapters, capability/media/schema/usage/error/cancel handling |
| `src/main.rs` | Remove implicit process-provider defaults when replacement passes; exact model/configuration/secret references, resource/replication and isolation setup; preserve explicit empty-node startup |
| `src/jobs.rs` | Actual terminal receipts, isolation, snapshots, resource/network limits, mediated secrets, managed session lifetime and uncertain termination |
| `src/api.rs` | Authenticated actor/context scope, generated versioned operations, access-safe receipt/query/cursor/projection/artifact paths |
| `src/curricula.rs`, `curricula/` | Ordinary learning content using fragments and evidence bindings; no course/domain execution branch |
| `integtest/behavior.rs`, `integtest/live.rs` | Public-API regressions and funded behavioral campaigns; retained failed evidence and stable operation identities |
| `src/network.rs`, `src/continuity.rs` | Validate new schemas/access; deny unsafe automatic v2 activation/export; no transport or exclusive-identity redesign |
| Matching Preact UI | Generate controls from Rust; replace provisional read-only adapters only when real backend semantics exist; test exact currentness and lifetime |
| Runtime/design docs and `scripts/package.mjs` | Matching source/schema/distribution versions and honest evidence; retire old claims only when new paths pass |

Small modules such as work, fragments, birth, authority, context, evidence, sandbox or provider adapters may be extracted when they clarify implementation. These are not required separate services or existing files. Reuse SQLite/FTS, reqwest and the lockfile. Do not add a vector database, personality router, profession registry, fixed planner, mandatory skill/curriculum engine or population optimizer.

## Fix behavior, not just types

Moving to HTTP includes implicit registration and startup configuration. Adding fragments includes work-scoped selection and useful-transfer tests. Adding birth includes atomic capacity/funding/identity/initialization, restricted bootstrap and separate membership/commitment consent. Adding review includes actual agreed checks, conditional inputs, relevant blockers and exact currentness.

Keep stop-on-first-failure, stop-on-pending with permanent suppression of the old suffix, and explicit yield/quiescence. The current runtime report describes source changes for these mechanics; verify the existing increment before integrating roots/fences or adding duplicate implementations. An accepted subjective result need not run a ceremonial shell command; an executed-analysis claim cannot pass without actual execution.

An isolation configuration is not enforcement. Implement containment before autonomous installers or sensitive sessions. Validate filesystem publication against the accessible snapshot, not a user-supplied path/digest alone. Full-record API and search paths need scope guards too, not just writes.

## Implementation milestones

| Milestone | Build | Exit condition |
|---|---|---|
| P0 — pinned baseline and contract | Freeze runtime/UI/design/schema/fixtures, inventory equivalents, preserve failures/backups | One target and one authority boundary, source-supported gaps rather than duplicated systems |
| P1 — prerequisites | Pending-effect barrier/replay, roots/scope/grants/reservations, fences/outbox/recovery, HTTP conformance and actual isolation | Relevant M01–M13, M15, M17–M18 and race/resource cases pass on real paths before live autonomous tools |
| P2 — small real cooperation | Distinct context, accepted responsibilities, durable feedback and exact review | A peer's evidence changes a real artifact and independent checking verifies the change |
| P3 — adaptation and population | Bootstrap consent, protected closeout, interface iteration, useful correction, different groups, birth/restraint | Controlled B01–B10 and conserved resources; no competence claim from source/schema tests |
| P4 — house and generalization | Actual native disciplines/analyses, disturbances, scope review, release seal and unrelated needs | B11/B12, fresh repeats, honest digital-versus-external boundaries |
| P5 — release | Runtime/schema/UI/docs/package coherence, restored state, security/load/cost and UI lifecycle | Mechanical gates and predeclared behavioral thresholds, no unsupported completion claims |

Provider and isolation work may proceed alongside records and UI; they must pass before funded autonomous tool work. Do not delay those prerequisites to the final milestone. Start with the delayed-writer/old-file regression, not a larger house run or more personas.

## Baseline reproduction commands

For core regression work, use the exact-revision runner in [CORE.md](CORE.md); it covers the current staged-receipt and real-process barrier suites as well as the retained behavior tests. Its logs stay outside this public design repository.

The commands below remain the broader baseline build/package reference, including the later UI integration phase. This core-only design update does not claim to have executed them.

```sh
# In the Rust runtime checkout
git switch rewrite/design-first
git rev-parse HEAD
cargo build --locked --release
cargo test --locked --test behavior -- --test-threads=1

# In the matching UI checkout
npm ci
PERSONAS_BIN=../ai-personas/target/release/personas npm run contract
npm run build
```

Freeze exact compatible commits for the test campaign. Do not generate new authoring controls from a speculative Markdown API. Current v1 clients still use the unchanged [generated API](API.md). Target-incompatible authoring should use an explicit proposed `ai-personas/2` contract after Rust implementation and schema generation.

## Migration and rollback

The existing store refuses a mismatched development contract. Use fresh v2 pilot nodes by default, retaining v1 with its matching read-only build. An explicit importer may preserve original bytes and identities while marking missing bindings `legacy_unbound` or `unverifiable`. Never synthesize old signatures, grants, consent, acquisitions or learning.

Keep one mutation authority during cutover; old/new ledgers cannot both spend the same resources. Rebuild indexes and compare counts/hashes. Back up and restore before rollout; retain old readers only for actual retained formats. Freeze or deliberately migrate long-running jobs and ownership.

Rollback changes code/data/projections, not completed outside effects. Reconcile receipts and unknown exposure before resuming. Delete obsolete executable inference paths after the tested HTTP replacement exists; retain their historical logs as evidence.

## Installed release and operations

An installed release must pin runtime, design, UI, generated contract, fixtures/evaluators and distribution digests. Reconcile the installed `/api/release` information with the package and actual served UI. A green build or documentation renderer is not all-goals acceptance.

The old branch's package layout is baseline evidence, not a statement that isolation is unnecessary. Target deployment needs a supported Linux isolation backend, low-privilege node, private credentials, protected dependencies, bounded disk/logs and protected backups. Fail required startup/capability admission when isolation is unavailable.

Monitor queue age, lease loss, denied admissions, unknown costs/effects, context overflow, stale/missing evidence, projection lag and viewer errors. Correlate work/root/run/persona/call/action/job/artifact/review/grant/budget IDs. Metrics do not rank personas' worth.

Private work stays private by default; explicit publication governs discovery. Source restrictions extend to summaries, fragments, search, previews, caches, exports and backups. Deletion/redaction must respect retention policy. Revocation cannot promise to erase already exported copies.

## Federation boundary

Existing peer file/message transfer and continuity routing are retained. Pausing/importing/routing is not distributed exclusive identity activation. Until new root/grant/reservation/active-identity bindings transfer safely, reject unsupported active v2 exports/activation. Verified bytes or a remote Persona record are not automatic local membership, execution authority or money. No recipes auto-run.

## How to evaluate documentation itself

The tools in the Rust repository at `tools/design_docs` check local links/anchors, balanced code fences, required sections/invariants/gates and unchanged v1 API bytes. They extract/render Mermaid diagrams outside the design checkout. This documentation-only repository carries no executable checker, UI screen or build workflow. These checks remain separate from the Rust and live-persona gates. See [repository ownership](../REPOSITORIES.md).
