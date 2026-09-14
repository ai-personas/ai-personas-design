# Implementation reference

The runtime is new Rust code using SQLite, ordinary files, and libp2p. The UI is new TypeScript and Preact code. All three rewrite branches begin with empty source trees; no previous AI Personas implementation, persona data, fixtures, or passing result is a source for this release.

The runtime contract generates the HTTP reference, machine-readable schema, and TypeScript declarations. The release record pins the runtime, design, and UI revisions plus contract and distribution digests. Browser and integration clients use the same public HTTP interface.

SQLite transactions preserve record revisions, action identities, state transitions, and event ordering. Files preserve command output, model request/response records, and content-addressed artifact bytes. WAL and a single owning node process coordinate database writes. These are application consistency measures, not a security boundary against other host programs.

Providers implement discovery and decision calls. A provider returns advertised capabilities and measured usage without a model ranking. An external JSON provider bridge is available in addition to the Codex adapter. No persona identity is keyed to a provider session. See the generated API reference for exact request types.

A decision containing only a progress summary records that account and continues the ordinary loop. Waiting requires an explicit `wait` operation. Submission preserves an immutable version and continues work. Assessment delivers findings to the owner and leaves the reviewer waiting. Pause stops further decisions without cancelling host jobs.

An identity has one active model decision at a time. Durable queued runs share that identity fairly. Inputs have an acknowledged cursor; work-specific inputs stay with their work, while general messages are delivered to the identity once, including messages arriving before its first task. Shared submitted versions and findings are delivered to the work’s contributors, including a peer waiting for those results. Waiting releases model execution. Unread inputs or completed jobs queue further decisions unless explicitly paused or cancelled.

A model response is saved before its actions run. Each action identity derives from the call and its position. Restart resumes the saved response and reuses completed results. An interrupted effect whose outcome cannot be established stays uncertain. No application-level mechanism can establish every effect of arbitrary programs on a shared host.

A failed action returns its receipt to the model before later actions from that decision run. The original response and the stopping action remain recorded. This prevents a dependent effect or a later wait from hiding an error the model has not yet seen; the next decision can correct the request or choose to wait.

The typed Rust command enum supplies server validation, the provider decision schema, UI types and generated technical arguments. Browser lists use indexed pages and lightweight change events; viewers and expensive detail load only when opened. Original output and artifacts stream from files with byte ranges.
