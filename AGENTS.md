# Repository scope

This is `ai-personas/ai-personas-design`, branch `rewrite/design-first`.
It is documentation-only: architecture, requirements, design decisions,
acceptance plans, prose examples and source/evidence references.

Do not add Rust or Python implementation, verification scripts, executable
prototypes, UI screens, browser tests, build pipelines or packaged applications
here. Code fences describing contracts are documentation, not implementations.
`technical/core-gates.json` is a non-executable design/acceptance plan.

Implement actual backend changes in the existing Rust source on
`ai-personas/ai-personas:rewrite/design-first`. Keep its runtime tests, schema
generation, build/package tooling and development checks with that implementation.
UI components, styles, standalone screen fixtures and browser tests belong to
`ai-personas/ai-personas-ui:rewrite/design-first`.

Do not replace implementation work with another design document or helper test.
A design check is not a Rust build, a runtime regression or product acceptance.
Keep historical evidence and explicit limitations. Never publish private runtime
source or logs here. Do not merge another runtime branch into the Rust target.
See [repository ownership](REPOSITORIES.md) and [status](STATUS.md).
