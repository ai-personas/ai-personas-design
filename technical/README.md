# Implementation reference

The runtime is new Rust code using SQLite, ordinary files, and libp2p. The UI is new TypeScript and Preact code. All three rewrite branches begin with empty source trees; no previous AI Personas implementation, persona data, fixtures, or passing result is a source for this release.

The runtime contract generates the HTTP reference, machine-readable schema, and TypeScript declarations. The release record pins the runtime, design, and UI revisions plus contract and distribution digests. Browser and integration clients use the same public HTTP interface.

SQLite transactions preserve record revisions, action identities, state transitions, and event ordering. Files preserve command output, model request/response records, and content-addressed artifact bytes. WAL and a single owning node process coordinate database writes. These are application consistency measures, not a security boundary against other host programs.

Providers implement discovery and decision calls. A provider returns advertised capabilities and measured usage without a model ranking. An external JSON provider bridge is available in addition to the Codex adapter. No persona identity is keyed to a provider session. See the generated API reference for exact request types.

A decision containing only a progress summary records that account and continues the ordinary loop. Waiting requires the explicit `wait` operation; pause, submission and assessment also stop the corresponding run. Returned completed action results are already present in subsequent request history.
