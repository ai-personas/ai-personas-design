# Sources, decisions and publication history

[Introduction](README.md) · [Specification](technical/SPEC.md) · [Implementation status](STATUS.md)

## Requested design basis

The user supplied the earlier Markdown proposal and then clarified complete multidisciplinary work, useful improvement, emergent individual/group behavior, birth and the **Rust-only** implementation target. The supplied final v1.2 specification and stress-test report are the primary basis for this publication.

| Source | Role in this edition | SHA-256 of supplied file |
|---|---|---|
| `deep-research-report (1).md` | Earlier design basis; later explicit corrections take precedence | `5b61b8e8b5f35a3a5a05f68bef0eaaca1cbeda8a7600ec0e930d41c73f34e02e` |
| `AI-PERSONAS-RUST-SPEC-v1.2.md` | Final Rust-only target and C01–C09 corrections | `09c15df2757071aba36dc4854df0d8fe8c919090d0b929c004b14a6b83e00608` |
| `STRESS-TEST-REPORT.md` | Authored house/team scenarios and counterexamples; not a live run | `55d345984838a6451b746cbbac2bfa81da32202473646db03b32d28d4b1d5b1f` |

The hashes identify the input attachments, **not** the rewritten repository files. The repository edition reorganizes explanations and replaces chat-local delivery references with repository navigation. It is not represented as a byte-identical copy. All runtime guarantees remain proposed unless separately supported in STATUS. No new domain requirement or professional role is silently introduced.

## Traceability to the source specification

| Original v1.2 sections | Repository location | Meaning retained |
|---|---|---|
| 0–4 | SPEC 0–4, introduction and glossary | Decisions, invariants, Rust-only scope, identity, relationships and collective behavior |
| 5–7 | SPEC 5–7 | Root/run/bootstrap distinction, mandate, continuation, assumptions, agendas, commitments and improvement |
| 8–9 | SPEC 8–9 | Bounded birth, preview/consent, lifecycle, interfaces, iteration and actionable feedback |
| 10–13 | SPEC 10–13, PROVIDERS, STORAGE | Memory/context, ordinary tools, HTTP inference, isolation, authority and resources |
| 14–18 | SPEC 14–18, STORAGE | Exact evidence/currentness, release seal, record bodies, lifecycles, admission/replay and proposed command families |
| 19–21 | SPEC 19–21, UI and house example | Six workspace views, full house scope, other needs and evidence limits |
| 22–24 | SPEC 22–24, RELEASE and ACCEPTANCE | File mapping, deployment/migration/privacy/federation, M01–M26, B01–B12 and prerequisite-first rollout |
| 25 and source register | SPEC 25, this page and STATUS | Prior-delivery limits separated from this publication and the separately updated UI |

The nine review corrections remain C01–C09 and the invariant IDs remain I01–I21. These links name the focused documents: [SPEC](technical/SPEC.md), [PROVIDERS](technical/PROVIDERS.md), [STORAGE](technical/STORAGE.md), [UI](technical/UI.md), [RELEASE](technical/RELEASE.md), [ACCEPTANCE](technical/ACCEPTANCE.md), [house example](examples/HOUSE.md).

## Pinned implementation sources

All runtime links below point to the Rust revision `d3339d30fa883c21c7935a2d009e3a58f480a256`. A source description is not a claim of independently executed tests.

| Source | Supports |
|---|---|
| [Rust README](https://github.com/ai-personas/ai-personas/blob/d3339d30fa883c21c7935a2d009e3a58f480a256/README.md) | Empty-node startup, matching UI/design, process inference, unsandboxed host, build/acceptance boundaries |
| [Cargo manifest](https://github.com/ai-personas/ai-personas/blob/d3339d30fa883c21c7935a2d009e3a58f480a256/Cargo.toml) | Existing Rust stack, dependencies and test/binary entry points |
| [Command contract](https://github.com/ai-personas/ai-personas/blob/d3339d30fa883c21c7935a2d009e3a58f480a256/src/contract.rs) | Existing v1 operations, identity primitive, review checks and continuity limits |
| [Wire types and protocol](https://github.com/ai-personas/ai-personas/blob/d3339d30fa883c21c7935a2d009e3a58f480a256/src/types.rs) | IDs, revisions, ModelRequest, context, stop-on-error and empty-decision continuation |
| [Store](https://github.com/ai-personas/ai-personas/blob/d3339d30fa883c21c7935a2d009e3a58f480a256/src/store.rs) | SQLite tables/FTS/transaction boundary and contract mismatch refusal |
| [Runtime](https://github.com/ai-personas/ai-personas/blob/d3339d30fa883c21c7935a2d009e3a58f480a256/src/runtime.rs) | Source-path review of operate/dispatch/request/work_loop/apply_decision, wait and assessment |
| [Jobs](https://github.com/ai-personas/ai-personas/blob/d3339d30fa883c21c7935a2d009e3a58f480a256/src/jobs.rs) | Supervisor launch/terminal receipt distinction and process tracking, not containment |
| [Delivery](https://github.com/ai-personas/ai-personas/blob/d3339d30fa883c21c7935a2d009e3a58f480a256/src/delivery.rs) | Continuity-forwarding responsibility, not a universal local mailbox service |

The supplied review's source reads were targeted ranges. The mapping to an existing file is not proof every proposed behavior is absent or present in that file; inspect before duplicating a helper. The documented pending-effect race is a static finding, not a production reproduction in this task.

## UI reference

The matching UI at [fa7cef7b748fb855e53857b1a8a351ddab458dda](https://github.com/ai-personas/ai-personas-ui/commit/fa7cef7b748fb855e53857b1a8a351ddab458dda) was updated separately. Its [integration note](https://github.com/ai-personas/ai-personas-ui/blob/fa7cef7b748fb855e53857b1a8a351ddab458dda/docs/RUST-V1.2-UI.md) distinguishes implemented views, v1 actions and read-only adapters from missing Rust authority, consent, funding and release guarantees. Its [CI run](https://github.com/ai-personas/ai-personas-ui/actions/runs/35169941532) is frontend fixture evidence only.

## Historical design and generated interface

The earlier [design tree at 07a86a728cb9eae3384f6c717fd3ccccf6b2ae97](https://github.com/ai-personas/ai-personas-design/tree/07a86a728cb9eae3384f6c717fd3ccccf6b2ae97) remains recoverable in Git history. Its unsandboxed/process-provider descriptions are retained as historical baseline, not current target instructions. Do not import another runtime branch's guarantees.

`technical/API.md` remains byte-identical to its generated v1 baseline blob `367a31cc31e6e6283a8014eac3f7763d49b28188`. The checker verifies that Git blob ID. A new backend contract must be generated from actual Rust code; this publication does not hand-edit API.md to manufacture v2 support.

## Documentation tooling

Mermaid fences express diagrams with adjacent prose equivalents. CI renders them with the pinned [Mermaid CLI 11.4.2 release](https://github.com/mermaid-js/mermaid-cli/releases/tag/11.4.2); this is a documentation-only tool choice, not a runtime dependency or recommendation to change the product stack. Check reports and rendered figures identify the documentation commit. No provider or engineering capability follows from them.


## Repository-placement correction

The source for the moved public helpers and UI fixture is design commit
`9b1fd0a82ee4c5c6eb6f87aac4f2f9495f14d41d`. Prior manifests and test history remain
bound to their original revisions; moving files does not transfer a passing
verdict to new runtime features. Current ownership is documented in
[REPOSITORIES.md](REPOSITORIES.md). The normative specification and generated v1
API remain byte-identical in this correction. No private runtime source is
published here.
