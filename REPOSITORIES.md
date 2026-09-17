# Repository ownership and correction

All three targets use `rewrite/design-first`.

| Repository | Owns | Must not substitute for |
|---|---|---|
| [ai-personas](https://github.com/ai-personas/ai-personas/tree/rewrite/design-first) | Actual Rust backend, API/schema generation, persistence, providers, execution, runtime tests and development/build tools | Design prose or browser fixtures presented as runtime implementation |
| [ai-personas-design](https://github.com/ai-personas/ai-personas-design/tree/rewrite/design-first) | Architecture, requirements, decisions, acceptance plans, prose examples and provenance | Backend code, executable tools, UI screens or test pipelines |
| [ai-personas-ui](https://github.com/ai-personas/ai-personas-ui/tree/rewrite/design-first) | Preact components, styles, UI fixtures and browser tests | Backend authority, evidence or resource enforcement |

## Corrected placement

The misplaced files were present in design commit
`9b1fd0a82ee4c5c6eb6f87aac4f2f9495f14d41d`. They remain recoverable in Git history.
No force-push or history rewrite is part of the correction.

| Former design path | Destination |
|---|---|
| `design/` | UI repository `design/`, including source-image and historical verification manifests |
| `tests/browser_design.py`, `tests/browser_reference.py`, `tests/*.test.cjs` | UI repository `tests/` |
| `scripts/` | Rust repository `tools/design_docs/scripts/` |
| `tests/test_core_contract.py`, `tests/test_docs.py` | Rust repository `tools/design_docs/tests/` |
| `.github/workflows/design-docs.yml` | Removed here; each code repository owns its own validation workflows |

The migrated screen scripts, styles, markup and tests are unchanged. A local
CommonJS package boundary in the UI repository preserves Node test loading
without changing the production UI's ESM package. Documentation links point to
the proper repositories. The prototype is still illustrative, not a backend.

The migrated helper scripts accept a separate design checkout. Their output
stays outside this documentation-only repository. The runtime helper tests do
not become Rust product code or proof of completed v1.2 functionality.

## What implementation means

A backend requirement is implemented only by changes to the real Rust
contract/runtime/store/provider/job/API paths and relevant executed tests.
Adding types, a plan, a mock fixture or a test runner alone does not establish
that a feature is complete. The canonical specification remains
[technical/SPEC.md](technical/SPEC.md); [STATUS.md](STATUS.md) distinguishes
source observations and test evidence from that target.

This repository correction does not add new Rust feature behavior. Existing
Rust source at `c2b7d89a7d05f7f31e35d590ba39a3fcf80439fa` is preserved, including
the HTTP adapter and earlier barrier/context changes. Their reported limits
remain; this move is not a completed implementation or live acceptance campaign.
