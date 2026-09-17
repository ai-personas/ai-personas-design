# Implementation status and evidence

[Start here](README.md) · [Full specification](technical/SPEC.md) · [Core changes](technical/CORE.md) · [Source register](SOURCES.md)

This document separates a design decision, a source report and an executed result. None is a substitute for the others. This update changes the **design repository's core contracts, implementation traceability and verification helpers only**. It does not change Rust runtime source or UI source.

## Repository correction

The `ai-personas-design` branch is now documentation-only. Actual product
implementation is the Rust `ai-personas/ai-personas:rewrite/design-first` branch;
UI implementation is `ai-personas/ai-personas-ui:rewrite/design-first`.
The former executable scripts/tests have moved to the runtime's
`tools/design_docs`; the screen fixture and browser tests have moved to the UI
repository. See [repository ownership and migration](REPOSITORIES.md).

This move changes no Rust feature behavior and makes no new runtime acceptance
claim. The existing runtime source also contains a
[direct HTTP inference increment](https://github.com/ai-personas/ai-personas/blob/c2b7d89a7d05f7f31e35d590ba39a3fcf80439fa/docs/HTTP-INFERENCE-INCREMENT.md),
with explicit limitations. The historical ledger below is not a complete audit
of that increment, nor proof that the remaining target design is implemented.
No private Rust source or execution log is copied into this public repository.

## Pinned scope

| Reference | Repository and branch | Commit |
|---|---|---|
| Current core implementation reference | `ai-personas/ai-personas`, `rewrite/design-first` | `c2b7d89a7d05f7f31e35d590ba39a3fcf80439fa` |
| Historical source inspected for the supplied v1.2 design | `ai-personas/ai-personas`, `rewrite/design-first` | `d3339d30fa883c21c7935a2d009e3a58f480a256` |
| Design before this core-only update | `ai-personas/ai-personas-design`, `rewrite/design-first` | `52bdbfadc3dc77ce15e3cb376036c7293acad5da` |
| Unchanged historical UI reference | `ai-personas/ai-personas-ui`, `rewrite/design-first` | `fa7cef7b748fb855e53857b1a8a351ddab458dda` |

Only the Rust runtime is the core implementation target. No Python-main code, capabilities or results are imported. The normative v1.2 document retains its historical source observations; the newer source report below does not retrospectively change them. The UI reference is retained for provenance, not claimed to be a freshly verified compatible build.

## What changed in the runtime reference

The [implementation report at the current Rust commit](https://github.com/ai-personas/ai-personas/blob/c2b7d89a7d05f7f31e35d590ba39a3fcf80439fa/docs/RUST-V1.2-IMPLEMENTATION.md) reports these source changes:

| Area | Reported increment | Evidence boundary |
|---|---|---|
| Saved decisions | Barrier persisted before asynchronous dispatch; old suffix suppressed; non-success receipts stop the batch | Reported source change; Rust regression execution remains to be established |
| Idle behavior | Empty decisions yield rather than automatically spend another call; newer-input protection retained | Yield is not completion; full authorized self-wake/resource control remains outstanding |
| Context | Participation-scoped selections, compaction and images; legacy global context not silently promoted | Context separation is not a complete confidentiality or context-budget guarantee |
| Ownership | Explicit execution directory cannot bypass run ownership; foreign uncertain actions cannot be resolved by another persona | Two guards are not a complete authenticated ACL/admission system |
| Continuity | Reported inclusion of explicitly selected run records/action receipts in exports | No distributed exclusivity or safe complete v2 active-state transfer is inferred |

The report says the Rust build/tests were not executed when that increment was prepared. Its fixture-generator tests are not Rust runtime evidence. This design update did not compile Rust, rerun those tests, call a live provider, run native engineering tools or demonstrate emergence. Do not mark a source increment as a passing acceptance gate.

## What remains implementation work

| Core area | Required implementation and evidence |
|---|---|
| Authority and resources | One-store authenticated admission, ExecutionRoot distinct from participation/bootstrap contexts, root-conserved reservations, leases/fences, cancellation and protected closeout |
| Identity and organization | Typed fragments, individual agendas/relationships, exact agreement endorsements, mandates, continuation acceptance, coverage and accepted commitments |
| Birth and lifecycle | Atomic capacity/funding/identity/bootstrap, restricted invitation preview, independent membership/commitment consent, bounded initialization, handoff and dormancy |
| Provider boundary | Direct HTTP adapters and startup defaults, exact capability/model/usage/error/media/cancellation handling; current README still describes process inference |
| Execution boundary | Enforceable containment, authorized snapshots/paths, resource/network limits, mediated credentials and protected assessor access; current README still describes unsandboxed host execution |
| Feedback and coordination | Conditional assumptions, durable blocker dispositions, unstarvable current facts, observed-version conflicts, version-ready interfaces and bounded iteration |
| Evidence and release | Exact input/criterion/policy binding, conservative staleness, coupled assembly CAS, scope review and atomic final release |
| Acceptance | Real mechanical tests, small peer-feedback-to-edit-to-review evidence, controlled learning/birth/restraint comparisons, house depth and unrelated needs |

See the dependency-ordered [core implementation contract](technical/CORE.md) and [machine-readable gate plan](technical/core-gates.json). Every core gate in this plan is `not_verified`. M14 remains explicitly deferred to UI integration, not removed from full product acceptance.

## Historical defect and retained protections

At the historical `d3339d30fa883c21c7935a2d009e3a58f480a256` revision, the supplied stress review identified a pending-action sequencing path that could publish previous bytes while a tool was still running. That was a static finding, not an executed reproduction in the design task. The newer implementation report describes a source correction; it must be tested with a delayed writer and a pre-existing old file, including failure and crash replay. Do not rebuild a second barrier or claim the old defect was reproduced on the newer commit.

The baseline `wait` already checks newer inbox items transactionally. Preserve that check. Local notification work belongs in runtime/store; `src/delivery.rs` is primarily continuity forwarding. The [storage guide](technical/STORAGE.md) describes target semantics, not a new verification result.

## UI is unchanged in this increment

The [historical UI integration note](https://github.com/ai-personas/ai-personas-ui/blob/fa7cef7b748fb855e53857b1a8a351ddab458dda/docs/RUST-V1.2-UI.md) remains the source for the previously reported read-only adapters and UI behavior. Those claims are not revalidated here. That earlier core-documentation increment changed no UI files. The later repository correction relocates the standalone fixture into the UI repository without changing production components.

Backend activity, acceptance, outside evidence and review applicability remain separate facts even while UI work is deferred. A read-only view is not evidence of backend enforcement.

## Verification boundaries and private evidence

The supplied scenarios and abstract protocol checks are not live persona traces, Rust regression tests, native CAD output, engineering simulations or security certification. Design checks validate links, structure, planning IDs and helper behavior. Their success does not satisfy runtime or behavioral gates.

The private-checkout runner, now in the runtime repository, executes only the existing locked Rust build/fixture/barrier/behavior suites, records command exits and stops on failure. Even when it succeeds, its report leaves full v1.2 acceptance `not_evaluated`; it does not invent verdicts for unimplemented tests. Missing tools, dirty or changed revisions, failures and interruption remain visible.

The runtime repository is private. Keep its source, logs, node state, build artifacts and credentials out of this public design repository. The runner stores evidence outside both checkouts; it does not publish or push it. A trusted disposable Linux test host is still required because the legacy process tests are not sandboxed. See [reproduction instructions](technical/CORE.md).

## Meaning of the word final

Version 1.2 is the agreed design target after the stress review, not a claim that every requirement is implemented or proven. [Mechanical and behavioral acceptance](technical/ACCEPTANCE.md) remains mandatory. Preserve old failed outcomes and source versions. A documentation pass, a successful build, an installed tool or a new persona identity cannot substitute for useful, independently checked work.
