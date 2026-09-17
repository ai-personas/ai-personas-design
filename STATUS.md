# Implementation status and evidence

[Start here](README.md) · [Full specification](technical/SPEC.md) · [Source register](SOURCES.md)

This document separates a design decision, a static source observation and an executed result. None is a substitute for the others.

## Pinned scope

| Repository | Branch | Reference used for this documentation |
|---|---|---|
| Runtime | `ai-personas/rewrite/design-first` | `d3339d30fa883c21c7935a2d009e3a58f480a256` |
| UI | `ai-personas-ui/rewrite/design-first` | `fa7cef7b748fb855e53857b1a8a351ddab458dda` |
| Design before this update | `ai-personas-design/rewrite/design-first` | `07a86a728cb9eae3384f6c717fd3ccccf6b2ae97` |

Only the Rust runtime and its matching rewrite UI/design are implementation bases. No Python-main capabilities or results are imported. Rust-only does not prohibit TypeScript in the UI or authorized tools written in other languages.

## What is observed versus required

| Area | Observed baseline or published UI support | Still required for the proposed design |
|---|---|---|
| Identity | Rust creation/update, OCEAN/VAD, retained records | Work-linked bounded birth, initialization authority, consent and accepted responsibility |
| Organization | Work, runs, messages, artifacts, requests and exact submissions | Individual agendas, agreements, accepted commitments, explicit coverage and feedback dispositions |
| Learning | Rust document/context actions | First-class fragments, per-work selection and demonstrated useful transfer |
| Inference | Rust README describes Codex app-server and executable bridges | Direct HTTP adapters, scoped credentials, conformance and bounded usage |
| Execution | Rust host commands and tracked process groups | Isolation, protected assessment, scoped effects, resource limits and actual-completion barriers |
| Storage | SQLite records/revisions/actions/events/inbox/FTS | One transaction boundary for new grants, reservations, leases, assembly adoption and release seals |
| Assessment | Independent identity and exact-submission review primitives | Criterion/input/policy applicability, conditional claims, coverage review and atomic release |
| UI | Six work views, bounded read-only adapters, retained v1 actions, preview verification and lifecycle improvements | Future Rust-generated authoring controls and authoritative v2 completion/resource projections |
| Continuity | Existing transfers and paused identity import/handoff routing | No new cross-node exclusivity or automatic v2 active identity export in this release |

The full details of the UI boundary are in the [pinned UI integration note](https://github.com/ai-personas/ai-personas-ui/blob/fa7cef7b748fb855e53857b1a8a351ddab458dda/docs/RUST-V1.2-UI.md). Read-only rendering of a record does not establish backend enforcement, confidentiality or atomic acceptance.

## Specific static finding to reproduce

At the pinned runtime revision, `jobs::start` returns after spawning a supervisor. `operate` returns a running receipt and `apply_decision` proceeds unless it sees a failed receipt. Foreground waiting occurs on a later `work_loop` entry. A later same-decision action can therefore publish the previous bytes of a still-being-generated file. This is a static code-path finding, not an executed reproduction in this documentation task. See [runtime protocol](technical/STORAGE.md).

The existing `wait` mutation already checks newer inbox items transactionally. Preserve it. `src/delivery.rs` is primarily continuity forwarding, not the entire local actor notification implementation.

## Verification boundaries

The supplied v1.2 review used authored scenarios and small abstract protocol checks. Those are not live persona traces, Rust regression tests, native CAD output, engineering simulations or security certification.

The [UI CI run for the pinned UI commit](https://github.com/ai-personas/ai-personas-ui/actions/runs/35169941532) reports a production build, 34 unit checks and 36 desktop/mobile browser-fixture checks. Its synthetic HTTP data is not a full Rust integration campaign or proof of emergent capability. The Rust-backed load/live suites have separate prerequisites.

The checks introduced **in this design repository** validate documentation structure, local links and Mermaid diagrams. A green documentation run proves only those checks. It does not run models, Rust binaries, engineering tools or outside effects. Check the exact documentation commit's workflow before claiming that run passed.

## Meaning of the word final

Version 1.2 is the agreed design target after the stress review, not a claim that every requirement is implemented or proven. The implementation must pass [mechanical and behavioral acceptance](technical/ACCEPTANCE.md). Later corrections require explicit versioned decisions and preserved old evidence; neither documentation nor an evaluator may silently turn failure into success.
