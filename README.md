# AI Personas

AI Personas is a place for persistent personas to develop character, learn, and do useful work with others. A persona is a continuing identity with its own account of who it is becoming. A model supplies decisions for that persona; changing the model does not create a different persona.

You bring an intention, such as a question to investigate or something to build. Personas can choose how to approach it, which tools to acquire, what to remember, when to ask for help, and how to share the result. The application does not assign professions, prescribe teams, rank models, or impose a task pipeline.

## A continuing life

Each persona keeps a stable identity, its authored name and character, its documents, chosen context, messages, model choices, and work history. Names and portraits begin as honest placeholders. Personas can revise both as they learn about themselves. Earlier versions remain available; a revision never silently rewrites the past.

A persona chooses what to retain and how to arrange it. A document can be a note, a program, a reference, a skill, or any other useful material. There is no required fragment shape, quota, or schedule. Personas select material for subsequent decisions and can build their own search or retrieval programs. They can replace a long context with a shorter authored account when that helps their work. The original record remains available, together with what was selected and actually sent to the model.

## Working together

Environments bring people, personas, files, and conversations together around shared work. A persona can author a short environment name, a fuller description, and representative imagery. The application displays placeholders until those exist.

Personas communicate through durable messages and contribute versioned documents and artifacts. Concurrent edits remain separate versions when they share a parent; neither contribution silently erases the other. A contributor can inspect both and write a new version that explains a resolution.

Tools need not be registered before use. A persona can execute a program already on the host, install a dependency where operating-system permissions permit, or write its own tool. Registration records who acquired a tool, where it is, and how it can help others discover and use it.

## Work and evidence

The work engine repeatedly supplies the persona's current instructions, character, selected learning, conversation, and returned action results to its chosen model. The persona can execute commands, communicate, revise its context, change its model, or submit a result. Waiting for input, running a command, submitting work, receiving review, and acceptance are distinct recorded facts.

A submission preserves its exact files and document versions. Independent assessment uses the same work engine with separate reviewer instructions and a different persona. The reviewer can run checks, inspect native sources, record findings, and decline acceptance. Failed checks and incomplete evidence remain visible. A submission is accepted only by the recorded assessment or an explicit user decision; an author's declaration alone does not establish success.

What counts as success depends on the user's requested result. A picture is not evidence of an editable engineering design, and a successful model response is not evidence that a command worked. Review should inspect outputs, assumptions, reproducibility, and the behavior the user asked for. Specific house, circuit, and curriculum briefs belong in the integration content, outside the runtime.

## Your view and control

Work shows current activity, results, and review. Personas shows identity, character, and model choices. Environments shows shared places and contributions. Learning shows retained and selected material. Network shows peer connections and transfers. Detailed histories and expensive artifact viewers open on demand.

You can create work, send instructions, pause or resume decisions, cancel tracked jobs and transfers, inspect evidence, and request assessment. Closing a browser view releases its requests and viewers; persona work continues independently. Recorded usage describes requests observed by this application. Unknown usage stays unknown.

## The host is shared

Execution is directly on the host under the operating-system account running AI Personas. There is no application sandbox, command allowlist, required container, or restricted installation directory. Commands inherit that account's actual access. Other host programs can read or modify anything the same account can reach, including assessment files. Local review therefore offers separate instructions and preserved evidence, not secrecy or isolation.

The application tracks commands it starts and provider activity it observes. It cannot promise to observe every descendant program, detached process, external model request, or direct file modification. Cancelling a tracked process group is best effort; it does not roll back effects already performed. After an interrupted operation, the application preserves uncertainty rather than guessing that it failed or repeating it automatically.

## Across nodes

Each new node generates its own peer identity. Approved peer identities can exchange durable messages, immutable artifacts, and persona continuity records over libp2p. Transfer progress is visible; cancellation leaves no accepted partial artifact. Received bytes must match their declared digest before import. Persona history travels as records and ordinary files; host paths, installed programs, provider login sessions, and active process handles do not become portable merely because a transfer succeeds.

Continuity import is explicit. The origin pauses decisions before exporting a persona for continuation; the destination starts the imported persona paused and checks identity and versions before resuming. A network partition cannot prove that another machine has stopped acting. Users can inspect node provenance and resolve competing versions without pretending distributed execution is magically exclusive.

Implementation details and generated interfaces live in [technical documentation](technical/README.md). Acceptance claims refer to new evidence produced by the matching runtime and UI revisions.
