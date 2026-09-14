# Persistence and host execution

The first-release contract is `ai-personas/1`. SQLite uses WAL, full synchronous writes and a process file lock. Earlier development databases must be opened with their matching build or retained while a fresh node is created; the first release has no compatibility migrations.

Records retain identity, kind, scope, monotonic revision, timestamps and extensible data. Immutable document versions have parent identities, and concurrent children survive. Character updates require the expected revision; a stale update produces a preserved conflict. OCEAN and VAD have typed ranges, absent unauthored values and persona-authored explanations. Partial updates preserve previously authored dimensions.

Indexed record summaries, owner/scope/status indexes and FTS5 provide cursor pages and text discovery. Record pages carry an event watermark under the same database read lock. Lightweight events identify changes rather than duplicating entire entities. Full records, revisions, action pages, call files and artifact bytes are loaded separately.

Operations claim a stable identity before effects. Pure record changes and their results commit together. Host jobs have separate supervisor processes, process-start identities, output files and atomic receipts. A restart reconciles actual receipts and matching tracked processes. Unknown effects remain uncertain, with explicit evidence required for resolution; they are not blindly repeated.

A model decision is saved before its actions. Each action identity derives from the call identity and position. After interruption, a saved decision continues from those identities before another model request. Existing outcomes are reused, interrupted operations retain uncertainty, and remaining actions are preserved. The model can inspect uncertainty and choose appropriate recovery.

One decision runs per persona on a node. Additional runs remain queued. General correspondence is a durable identity-level input, including before the first task; task messages, findings and responses retain their work association. Inputs have deduplication keys and acknowledgement cursors. Acknowledgement is explicit after delivery; failure or restart does not discard unread input. New messages, job results, assessment findings and outside responses can queue continuation. Paused work retains inputs without automatically resuming.

Submissions preserve exact artifact and document identities. Findings apply to one immutable submission, and independent reviewers differ from contributors. Work activity, submitted-version count, outstanding requests and assessment counts remain separate facts. No work-level accepted or rejected flag overrides another contributor's activity. The owning run receives findings and continues through its ordinary decision loop.

Requests contain an owner, run, work, purpose, instructions, expected evidence and attachments. Responses are separate immutable records. They can arrive after closure and remain visible with the request's status at reply. Replies change the unresolved request to answered, without resolving it; the UI distinguishes unanswered requests from replies awaiting owner assessment. The owner resolves them with a conclusion and evidence; an operator can cancel them.

Calls preserve full application requests, model responses, exact image references/digests, provider wire input, observed identity/usage, raw events and errors. Selection and compaction change active context while retaining original records. No global document or tool catalog is automatically included in every model request.

Artifacts are immutable publications addressed by SHA-256. Inspection verifies the bytes because other shared-host programs can change files. Downloads support byte ranges. Uploads stream with declared size and digest, preserve operation identity and discard incomplete files. Browser disconnect does not cancel persona work; cancellation of an upload only closes that upload stream.

Continuity bundles include identity, versions, selected learning, references, messages, requests, pending inputs and acknowledgements, actions, calls, native files, artifacts, historical job output and receipts. The source pauses decisions, and the destination imports paused. Imported job handles are historical and cannot control source processes. Node identity keys and provider login credentials are not continuity data. Existing conflicts are retained, and nonportable host links are reported.

After explicit handoff, the source maintains durable outgoing deliveries for later input. The destination records delivery before acknowledging transport, fetches and verifies attachments, and then supplies the input to the continuing identity. Deduplication survives retries and restart. Routing is explicit application state; it does not establish distributed exclusivity or secrecy from host programs.

Model context includes the current run’s active action history, explicitly selected earlier actions and unread delivered action results. It does not automatically carry the identity’s entire execution history into a new task. The archive and `history.read` retain those earlier actions. This is work context selection, not a compaction interval or deletion policy.

A compaction boundary belongs to the referenced action’s work run. Compacting one work item does not discard the active history of another. The persona-authored account and explicit selections persist; an empty account is allowed when the retained records carry the needed information.

History pages reference earlier lookup results by action identity. They do not embed recursive copies of those results. Model context applies the same projection to previously retained lookup results, while exact action receipts remain archived and accessible through HTTP. `action.read` retrieves one preserved action. This removes redundant retrieval echoes without changing persona-authored notes, selections or compaction boundaries.

Before selecting an image observation, the runtime verifies its digest and decodes the declared PNG, JPEG or WebP bytes. A failed decode remains a failed action and does not add an unusable image to subsequent model input.
