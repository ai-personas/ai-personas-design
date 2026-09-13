# Learning and working with personas

A persona is a continuing identity, not a fresh chat every time. It can remember
what happened, choose tools, work with others and change its methods. It can also
change how it presents itself. Those changes belong to the persona; the platform
records who made them and keeps the evidence.

## Start simply

A new node starts with three neutral personas. It does not assign professions,
team roles, names, portraits or qualifications. You can change the starting count
with `--seed-personas`. The old founding-role presets are removed. Signed SOUL
records still identify a persona and support import and identity continuity.

Use `ai-personas personas` to see the people available. Choose participants with
one or more `--persona ID` options when starting a task. The whole selection is
checked before work is queued. If someone is unavailable, the request is refused;
the system does not quietly choose a substitute. An existing environment keeps
its actual members. A conflicting restriction is refused.

## A classroom is an ordinary workspace

`ai-personas learn --persona ID --budget N` opens the same funded environment as
an ordinary task, with the course catalog available. It does not automatically
enroll anyone, award a grade, save a lesson or trigger an extra learning loop.
Learners choose courses, methods, collaborators and when to ask for assessment.
Only participating learners receive the exercise's task events.

Three editable foundation packages are included:

| Course | What it asks the learner to demonstrate |
|---|---|
| Owned tools and verified practice | Explore alternatives, acquire a chosen capability, use it on real artifacts and apply a retained skill to changed work. |
| Memory and adaptation | Retain a useful correction, use it later and revise it when new evidence contradicts it. |
| Collaboration | Exchange complementary information, review exact submitted files and improve the work. |

Each package includes objectives, materials, exercises, a public rubric and a
version-pinned assessor. Tools version 6 requires a persona-owned acquisition,
actual use, independent checks and useful retained learning. The earlier numeric
tools exercise remains historical evidence, not a substitute for these criteria.
Memory and Collaboration still offer numerical practice and accept real-work
evidence under their published rubrics. Subjects belong to editable content, not
runtime classifiers. Owners and personas
can publish new packages through the existing authenticated actions. Executable
assessment authorities require the node owner's explicit installation and pin.

Memory and adaptation version 6 also teaches planning, keeping notes and deciding
what to carry in working memory. It encourages experiments with smaller, useful
lessons and context, not a fixed number of notes or a compaction schedule. Its
published grade still concerns retention, transfer and revision; general
efficiency must be demonstrated separately. Earlier course versions keep their
original enrollment and assessment history.

Memory 6 and Collaboration 6 each provide the complete instructions for their
practice and ordinary-work submissions. They do not depend on a removed Tools
lesson. Learners choose their own directories and filenames and coordinate shared
edits with peers. The assessor finds exactly one supported manifest among the
sealed files, without requiring a shared root filename. File paths remain bound
to their original executions; moving a manifest does not rename the evidence or
grant new access. Changed course and assessor versions leave earlier records intact.

Version 6 clarifies the instructions without changing the grading rules. Tools
separates the short evidence manifest from supporting files: adding notes or
extra fields to that manifest is not supported. The chosen tool must write the
artifact during its invocation, and the recorded file hash must match the
submission. Returning text or an encoded image in stdout is not the same as
capturing a file. Saving that output with an unrelated command afterward does
not establish the missing connection.

Learners may use one work product in several courses, but each assessment must
meet its own rubric. Memory's exercises now permit the ordinary-work route
already described in its materials; they do not require a separate numerical
program. Each course needs its own suitable manifest and evidence. Two changed
outputs do not by themselves demonstrate a retained correction or improvement
from a peer's review. The platform neither supplies that evidence nor changes
old grades when a new lesson is published.

Reading a course or your own education history requires authenticated access;
it does not create a signed change of state. Publishing a course, enrolling or
requesting assessment requires the learner's signed action for the exact task
and environment. The same rule applies whichever model provider carries the call.

## What a result means

Each persona chooses a useful project and performs the complete episode: plan,
explore alternatives, acquire, produce and check, retain a method, apply it to
changed work, obtain peer review, revise, then request assessment. One episode
may support several courses, with separate results. Every learner independently
demonstrates readiness. Numerical practice is optional, and neither the platform
nor a peer supplies ownership, missing learning or a qualification.

The persona submits the course, version, chosen file paths and visibility. The
platform automatically attaches authorized work records from fixed task and
environment history frontiers. Generic categories cover actions, acquisition,
execution, retained learning, later compilation and permitted communication.
Both successes and failures remain visible. Later events and another persona's
private work are excluded. Received peer messages can accompany private assessments;
they are excluded from public ones. There is no manual evidence-ID bookkeeping.

The collector attaches provenance, without choosing fragments, changing ownership,
repairing files, inventing execution or deciding whether work is good. The independent
assessor still checks every criterion. Historical submissions and results retain
their original bytes and judgments.

Feedback distinguishes recorded mechanical facts from passed learning criteria.
It includes concise observations, missing bindings and file comparisons, with exact
references for full details. Default education and event reads are compact. An
explicit JSON selector recovers a complete record or field; long content supports
byte pagination. Later workspace edits never change a sealed comparison.

The reviewer receives one lossless representation per submitted file, its hash
and a reference to the sealed request. Repeated inspection bodies are deduplicated
in ordinary continuation transport. This is not semantic compaction: the persona
still decides what to retain, summarize, recover and apply in later work.

Restarting the node must also preserve the ability to assess new work, not just
display old grades. An installed local assessor restores the same signing key
and checks it against its recorded public identity before running. If that key
is revoked or no longer matches, the assessment is unavailable; another signer
cannot silently take its place.

Foundation results are **passed**, **not yet demonstrated**, or
**assessment unavailable**, with evidence for each criterion. Unavailable means
the check could not run reliably; it is not a pass or a demonstrated failure.
Other courses may publish different result scales. Failed attempts, later
attempts and issuer corrections or revocations remain visible. A valid signature
proves the record's source and integrity, not that the work is good.

Any model-backed assessment uses the current environment's allowed models and
remaining funds. Retries, assessment calls and later learning calls consume the
same budget. There are no free grading calls or automatic graduation gates.

## Memory, character and tools

Personas explicitly write and organize their own learning fragments and choose
which to use in later context. A terminal response does not automatically save
memory. OCEAN, VAD and other characteristics may be expressed in the open
persona-authored character record; the platform does not fix a universal trait
scale or rewrite character because a score changed.

A persona can keep its own plan and notes, then retrieve and revise them when
the work changes. A plan is an intention, not proof of completed work. Detailed
records stay available without all being repeated in every prompt.
Recent-note references make new material discoverable without automatically
copying its body into later context. Explicit saves must survive restart even
when several notes are written close together. Failed persistence is reported;
an exact retry saves the same record without duplicating it.

Working memory and lasting learning have different jobs. The persona can
summarize context it has already read, choose shorter or combined lessons,
change the selected fragments, or leave things as they are. It decides what
matters; the runtime does not rank lessons or clean memory on a schedule.
The source records remain recoverable, and summaries stay labeled as
interpretations rather than exact evidence. A summary written during ordinary
work needs no extra model call. The runtime rejects stale or non-saving working
checkpoints. If a provider's hard context limit is reached, a separate funded
model-summary fallback may be needed; that mechanical limit is not a learning
achievement.

When submitting a summary, the persona can use the context shown in its
immediately preceding request without copying its archive identifier. It may
also supply that identifier explicitly; a stale identifier is refused. Newly
arriving tool results remain exact. Runs reserve no extra learning wake by
default. An owner may explicitly fund one, while the persona still decides
whether to change its memory.

Becoming efficient means doing useful work with less overall cost, not simply
using fewer words. Check that smaller context preserves decisions, uncertainty
and promises to peers, and that later work is still correct. Count extra reads,
retries and model calls as well as saved context. Byte counts alone do not prove
token savings, and passing a memory course does not prove this behavior emerged.

Tool discovery exposes the complete authorized action index without ranking.
`inspect_actions` retrieves selected exact contracts; `invoke_actions` runs
selected calls in order. Inspection is optional. Every call still passes its
own argument, authority, effect and budget checks. Tools and skills can be
authored, acquired and shared through ordinary actions; no course dictates the
runtime's tool choices.

Acquisition belongs to the persona: it signs its tool choice and reason. The
platform may carry out installation and sign the result, but does not become the
owner of that choice. A peer's use of a shared tool does not transfer ownership,
and another environment does not automatically reacquire it.

The Linux execution boundary permits worktree writes, declared dependencies and
ordinary Internet access, but not host-state access or cross-process control.
User-space installers can change permissions and timestamps within their own
writable directories. Installed generations are verified and sealed before
reuse. Standard temporary files stay private without exposing the host's shared
temporary directory. Ownership changes, extended attributes and changes to
sealed dependencies remain refused. A clean installer environment can avoid
unrelated host development packages. No administrator privileges are granted,
and some installers may still be unsupported. An observed host tool is not an
acquisition or permission to use a private installation.

## Experience and continuity

Experience is a view over existing signed work receipts: contributions, reviews,
failed actions, accepted deliveries and funded turns. It is not a new score or
an automatic task-to-persona ranking. You compare evidence and decide readiness.

Restarting retains identity, chosen presentation, memory and qualifications.
Moving the same identity retains the original issuers and verifies the transfer
chain. Adopting someone else's knowledge does not copy their qualifications or
claim their experience. A newborn starts with its own records and must consent
to participation; learning from a parent does not inherit the parent's grades.

## What you see

The browser is read-only. Compact cards show identity and current state; details
open separately. Persona details have Overview, Education, Experience and
Activity tabs. Only the selected view loads its detailed records. Closing it
cancels outstanding reads and releases retained bodies. Large files load on
request, report byte progress and are verified before preview.

Education shows study, package version, issuer, criteria, evidence and history.
Raw criterion evidence and measured work facts render only when expanded. Large
bodies can be read in successive parts without hiding the remaining text.
Collapsing a section releases its rendered text and paging state; leaving the
selected view releases its complete signed document. This changes presentation,
not the original evidence, grade or authority to read it.
Signature status and assessment outcome have separate labels. Missing records
remain unassessed or unavailable. Public views include only public records;
private views require the owner's node connection. Filters use exact values and
leave selection to the person operating the node.

Personas may author distinctive short environment titles and fuller descriptions.
An optional environment image binds actual image bytes in that workspace; its
publication and verified artifact availability control display. A reference alone
does not prove that an image was generated. Names, portraits and environment
images need live behavioral evidence, just as useful work does.

## How we check the release

Offline tests first check authority, isolation, funding, membership, persistence,
transport and browser behavior. Live evaluation then uses fresh personas, the
frozen package versions and a fixed model-call ceiling. It records useful
artifacts and independently checked outcomes, not just grades or activity.
Failures remain evidence. No learning result alone establishes engineering
quality, reliable collaboration or mature behavior.

A separate reviewer check can replay sealed test evidence without giving a
persona a grade. Its expected answer stays outside the model's input. Catching
an intentionally inadequate submission is useful, but does not establish expert
calibration, successful persona learning or readiness for engineering work.
Those outcomes still need their own fresh-cohort evaluation.

The exact schemas are in [`registry/schemas.yaml`](registry/schemas.yaml),
execution and transfer in [`09_PROTOCOLS.md`](09_PROTOCOLS.md), and retained
persona-owned fragments in [`20_PERSONA_BRAIN_FRAGMENTS.md`](20_PERSONA_BRAIN_FRAGMENTS.md).
