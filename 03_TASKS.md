---
title: PersonaOS — Tasks, Causality, and Acceptance
status: Stable
---

# 03 — Tasks

A task is exact authenticated principal intent plus its signed causal history.
It is not a host-classified workflow, mission charter, phase graph, prompt,
score, team plan, or prescribed tool sequence.

This document is a clean break from seed task classes, routing modes, acceptance
pathways, task classifiers, keyword promotion triggers, round/refinement
reducers, structured readiness, and mission-charter compatibility.

## 1. Task ingress

Task ingress records an immutable signed task event containing:

- task, principal, environment, and authority identities;
- exact principal-authored intent bytes and their content hash;
- exact resource/model-pool authority and limits;
- exact workspace entry revision and ownership facts;
- zero or more exact unranked `domain_refs` supplied by authenticated
  authority; and
- acceptance, deadline, stop, cancellation, or materialization authority only
  when the principal explicitly supplies it.

The kernel validates canonical shape, signatures, access, lifecycle, resource
authority, and exact references. It does not infer a task class, profession,
domain, objective decomposition, role, required artifact, quality rubric, tool,
team size, prompt, or completion rule from the intent text.

Explicit principal authority is one optional intake object with exactly these
optional members: `acceptance_condition` (opaque canonical JSON chosen by the
principal, bounded in bytes, never interpreted by the substrate),
`verifier_descriptor` (exactly one of three exact member sets, every member an
exact string: {`verifier_key_id`, `scope`}; {`kind`, `verifier_key_id`,
`scope`} with `kind` exactly `"exact-key/1"`; or {`kind`, `scope`} with `kind`
exactly `"registered-persona-identity/1"`; any other member set is refused),
`verifier_receipt_constitutes_acceptance` (exact boolean, valid only
with a supplied descriptor, absent means false), `deadline_epoch_seconds`
(absolute integer epoch seconds), `unaccepted_rewake_count` and
`unaccepted_rewake_interval_s` (both exact positive integers, valid only when
supplied together), and `require_authenticated_effect_provenance` (exact
boolean, absent means false). Intake records this as one declaration with
an explicit per-member supplied/omitted marker and a content hash for each
supplied member; the declaration travels unchanged inside the task-resource
fan-out authority. Recording it validates shape and bounds only — it schedules
nothing and infers nothing. A declared re-wake bound is no exception: intake
still schedules nothing. The bound becomes executable only through §7's
prepaid finite-recurrence path, with every declared fire independently prepaid
from the exact signed run ledger at arm time; each armed fire is held while
the run it re-wakes has not produced its terminal result, and the whole bound
is cancelled by exact authenticated acceptance.

A task amendment or continuation preserves the complete verified principal-
intent ancestry in causal order, including the original signed intent bytes and
each later signed amendment. The newest carrier does not replace, summarize, or
reinterpret an older principal event. Every retained entry remains bound to its
own signature, content hash, task generation, and causal predecessor.

Public amendment intake is asynchronous by default: after exact admission it
returns the new run identity and poll surface before any persona model work can
delay the HTTP response. Synchronous execution is an explicit caller choice.
The exact prior-run identity, submitted amendment bytes, authenticated
submitter, and explicitly supplied execution authority form one
content-addressed admission identity. Execution authority includes the exact
submitted model ceiling, its bootstrap member, model-call grant, and
outcome-evidence floor, including whether each optional value was omitted.
Concurrent or retried requests with the same full identity converge on the same
run. A change to any member creates a distinct amendment; it must never replay a
run admitted under different authority merely because the prose is unchanged.
A caller that wants only to add resources uses the resource-grant surface rather
than replaying an amendment. Fresh lifecycles provide no duplicate-amendment
compatibility path.

The model-turn transport carries the complete current intent and complete
verified ancestry in a dedicated exact authority lane. Uniform paging of
optional situation sources never clips, prefixes, reorders, or competes with
that lane. Task intake and model-turn construction enforce the same byte and
record bounds; if the complete authority lane cannot fit, admission is refused
before cognition instead of presenting an omitted or summarized requirement.

A newly admitted task with no exact environment or project address forms a
fresh environment. An actor's existing membership, including a sole active
membership, is not implicit routing authority for unrelated principal intent.
Environment reuse requires an exact principal-supplied target or authenticated
causal resume/amendment authority. This routing rule is independent of task,
charter, persona, domain, arrival order, and concurrent worker timing.

A deployment may seed a node with a neutral cohort of several blank personas
instead of one. A task admitted to such a node with no exact environment,
project, or persona address founds its fresh environment with that exact seeded
deployment cohort as the environment's initial membership, and the ingress event
fans out to every founding member under §2. The founding cohort is the node's
deployment identity, selected by exact seeded-persona identity alone; it is not
implicit reuse of any existing environment's membership — reuse still requires an
exact principal-supplied target or authenticated causal resume/amendment
authority — and founding selects no role, leader, coordinator, or division of the
task. A single-persona deployment founds the environment with exactly that one
persona. An exact persona address instead forms a fresh environment whose sole
founding member is that persona, and a targeted or resumed environment keeps its
own exact signed membership rather than absorbing the seed cohort.

Current agency uses exact, content-bound navigation authority. On a native-tool
adapter, every complete leased action descriptor is a first-class provider tool
under its real action name; the prompt does not duplicate that catalogue behind
an inspector/invoker carrier. On a structured-only adapter, the same complete
unranked catalogue remains in the navigation lane. The lane also carries the
mechanically observed execution inventory, verified current population/
replication authority, and current workspace state. These components are
selected only by closed schema identity and content hash, never by task words,
roles, filename suffixes, domain labels, rankings, or recommendations. If the
combined carrier crosses its content-neutral byte bound, the fewest components
needed are replaced by hash-bound structural indexes in descending canonical-
byte reduction order. Their ordinary authenticated inspectors remain leased;
the host does not choose a useful executable, peer, file, or action to retain.
Large append-only activity histories remain independently hash-bound and
pageable; they cannot displace current population and navigation authority.
An exact situation-source snapshot may be removed from the uniform remainder
only after canonical-byte equality proves that a non-indexed navigation
component already carries that same snapshot.

The provider wire uses one closed component-identity order: identity, retained
learning, population, capability acquisition, workspace, execution inventory,
action catalogue, and action-usage history. This order changes neither
admission nor the byte-reduction rule and grants no action or component semantic
priority. It ensures that the actor can encounter its exact self, experience,
and peers before traversing large mechanical registries; task prose, authored
content, counts, outcomes, domains, and tool names cannot alter the order.

The exact same-run model transport inventory occupies a separate early
authority lane before navigation and the uniformly staged situation remainder.
It is admitted only after its run, signed pool hash, unordered-set declaration,
principal bootstrap authority, unique model identities, exact equality with the
signed model ceiling, bootstrap equality/membership, and whole-inventory hash
verify. The byte-identical staged copy is then removed.
This lane exposes available bodies and observed transport facts but does not
select, order, score, recommend, or invoke a body.

One small exact action-usage component remains separate from both the catalogue
and retained-learning body. It joins current action identifiers to exact zero-
inclusive receipt observations by string equality and carries a complete,
registry-ordered, equal-window descriptor preview table when those descriptors
are not already present in the native action transport. This allows the
persona to observe repetition or non-use and understand the corresponding live
mechanisms even when either larger source is structurally indexed. Counts and
descriptor prefixes never cause the runtime to rank, recommend, suppress, or
invoke an action.

A mechanical nesting-depth guard must not rewrite a compact canonical subtree
inside a signed or hash-bound observation. If such a subtree fits the declared
content-neutral byte bound, it is carried exactly regardless of nesting depth.
If it does not fit, the projection carries an explicit content hash, canonical
size, omission state, and independently addressable source rather than altered
bytes beside the source's unchanged hash. This applies equally to successful
and failed action results, persona-authored retained state, peer contributions,
and every other schema; field names and result meaning never affect the rule.

A resumed environment reconstructs project references from reciprocal verified
project and environment lineage. A mutable projection field is not routing or
prompt authority. Repeating a persona-signed request for an identical already
verified topology is an idempotent observation, while any differing name,
membership role, or target remains an explicit conflict. A verified outstanding
persona schedule is an event-driven continuation even while no model call is
running; quiescence and completion remain distinct states.

The signed `run-model-pool/2` in that authority contains an unordered ceiling
and a distinct principal-selected bootstrap body inside that ceiling. It is
never a preferred-model list, and task text cannot order its members. Before an
exact matching signed `persona-model-choice/1` exists, only that bootstrap body
may receive substantive cognition. Provider registry, configuration order,
default clients, health ordering, or a host bootstrap call cannot choose on the
persona's behalf.

When a newly minted run has no matching persona-signed choice yet, its signed
bootstrap authority must name one exact member of the ceiling before persona
cognition starts. Omitting it from a multi-body request is unresolved authority,
not provider downtime: intake refuses before creating a retrying run. A
single-body ceiling is structurally unambiguous and may use its sole member as
the bootstrap. A later multi-body order still requires the matching persona
signature.

Empty, one-domain, and cross-domain task contexts are valid. There is no
host-selected primary domain.

## 2. Exact fan-out to active members

The ingress event and every later task-resume resource event are offered
concurrently to **every active environment member**. Each delivery binds the
same exact source-event bytes and hash, task, environment, principal intent,
resource pool, and workspace observation.

A same-task resume additionally binds one kernel-signed
`personaos-prior-run-resume-observation/2`. It carries the immediately prior
run identity and exact terminal status, content-bound continuation state,
verified persona-authored work-state evidence, and a mechanically projected
materialized-file reference. The prior observation occupies an independent
prompt lane; generic raw-event compaction cannot replace it with only the
resume event hash. Its words and values grant neither completion nor a
successor—they are visible causal evidence for each recipient's own decision.

The `/2` observation additionally binds the task-family situation as exact
ledger facts, because a re-invocation is itself causal evidence the recipient
must be able to perceive:

- `task_family_invocation_ordinal` — this run's position (1-based) in the
  verified causal task family (the same verified principal-intent ancestry
  that scopes verifier receipts).
- `family_run_records` — a newest-bounded array of per-prior-run exact
  records: run identity, initiation instant (epoch seconds), the instant of
  the newest verified event attributed to the run, model turns delivered
  (derived from the run's own signed budget ledger, with an explicit
  recorded/unrecorded flag; `null` when the ledger records no charges),
  authored-action counts by exact action name (count-bounded with an
  explicit omitted-count member), declared-artifact count, and budget
  granted/spent. Only the immediately prior run carries a terminal status
  (the observation core's `prior_run_status`); earlier family runs bind no
  terminal status or settlement instant, because no verified lineage event
  records one — the record set states only what verified events prove.
  Every count is derived only from verified signed lineage events, with
  attribution bounded to each run's verified append window and an explicit
  unattributed-event count for anything outside every window; a run whose
  events cannot be verified appears only as an explicit unverifiable
  marker with `null` members, never as invented counts — and `null`
  (unknown) is never rendered as zero (known-none).
- `resume_carried_principal_amendment: false` — the structural fact that a
  same-task resume carries no new principal text (an amendment mints a new
  task identity and never travels this lane).
- `family_acceptance_events_recorded` and
  `family_verifier_receipts_recorded` — exact counts over the verified causal
  family from the same verified acceptance and receipt readers. Zero is
  stated as zero: "no acceptance has ever been recorded for this family" is
  an exact ledger state, and under a silent principal it is the ordinary
  state of a standing deliverable. Stating it is not appraisal — suppressing
  it renders delivered-but-never-accepted indistinguishable from closed.

The whole observation stays byte-bounded: bounded arrays declare their
omitted counts, and when even the bounded family members cannot fit, the
lane keeps the immediately-prior-run core and replaces the family members
with one explicit declared-overflow member — never a silent truncation. No
member ranks runs, computes ages or deltas, labels any state stale or
stagnant, or infers that anything remains to be done or is finished. The
substrate states instants, counts, ordinals, and ledger states; every
conclusion is the recipient's.

Each member receives its own carrier, lease, deduplication identity, and
settlement record. The kernel does not select a coordinator, owner, lead,
reviewer, specialist, preferred role, or representative recipient. The fact
that all members may observe an event does not require all of them to invoke a
model or take the same action.

If there are no active members, the event remains exact durable pending work
under its lifecycle and resource policy; the runtime does not invent a persona
or assign a role merely to consume it.

## 3. Ordinary persona decision surface

Every ordinary funded wake exposes the complete currently authorized action
surface—direct exact native descriptors or the structured catalogue—and
bounded exact situation facts. Population, identity, public-card,
communication, memory, skill, knowledge, capability, tool, artifact, workspace,
work-note, scheduling, and task actions coexist on that surface whenever their
mechanical authority is valid.

When collaboration or the complete prompt source set exceeds a carrier, the
situation includes exact snapshot/manifest hashes, source and record totals,
page/cursor ranges, omissions before/after, truncation counts, continuation
cursors, and completeness. A bounded page never presents itself as the complete
task situation, and transport order supplies no semantic priority. Append-
derived pages retain exact absolute positions and cardinality, including equal
records at distinct positions and redundant cross-scope observations. A
separate declared unique-identity projection may normalize observations only
while retaining exact duplicate counts/ranges and raw-page navigation.

The substrate does not narrow the catalog or require an action because of:

- task words, profession words, filenames, extensions, MIME, or `domain_refs`;
- missing artifacts, unchanged bytes, gap-like authored content, population size, or
  absent public identity fields;
- prompt phrases, regular expressions, model scores, work-note keys, status
  labels, previous action names, or HTTP results; or
- a fixed explore/acquire/act/review/refine/complete phase.

Exact action prerequisites remain dispatch-time authority checks. They do not
become a host-authored cognitive menu or recommendation.

## 4. Persona-authored navigation and emergence

From the same exact facts, a persona may inspect the workspace, communicate,
explore memories or opaque knowledge, share exact refs, obtain authorized
bodies, discover/acquire/provision/invoke a tool, author a knowledge record or
artifact, revise identity, invite or birth another persona, review work,
schedule itself, leave a work note, or do none of those things. Choices may be
interleaved and revised as new evidence arrives.

The runtime contains no built-in task, profession, format, tool, or domain
recipe. Personas may still discover and use needed capabilities because exact
unranked inventories and ordinary navigation actions make them reachable.

Receipts record what was actually invoked, produced, transferred, or learned.
They never automatically grant expertise, professional quality, relevance, or
completion.

## 5. Work notes and capability gaps

An active member may optionally author
`personaos-persona-work-state/5`. Its `work_note` is bounded open canonical JSON
bound to one exact observed situation, with exact provenance and append
lineage. It is the persona's claim, not task state.

Substrate-derived revision and prior-record pointers order immutable appends;
they do not replace earlier notes. Later task/workspace/resource facts do not
defer, settle, reclassify, or mutate any note.

A work note never covers principal requirements, votes on completion, gates
another participant, creates a successor, elects a coordinator, or changes the
action catalog. Its omission creates no correction call.

Perceived capability-gap meaning is optional opaque knowledge content, not an
independent substrate record/action/lifecycle. Expressing, revising, citing, or
omitting it does not make a task unready, block publication or acceptance,
select a tool, require another wake, or change another action schema.

## 6. Artifacts and workspace effects

Task artifacts cross authenticated action/workspace publication lanes and
retain exact author, action, provider/tool, byte, and settlement provenance.
Every artifact declaration binds explicit signed `mime_type`, content hash,
byte length, role, scope, and complete `domain_refs`. A filename or extension
does not supply MIME or role authority.

Current task and public projections must rejoin each declaration to the exact
current path/hash/length and its verified action/publication lineage. The
persona carrier exposes the bounded complete declaration authority before the
general workspace remainder. If several valid declarations bind the same exact
bytes but disagree on authored media claims, the projection preserves the
alternatives as explicit declaration ambiguity and selects no MIME from that
channel.

Concurrent member work remains attributable. A participant's worktree is
leased through action capture, publication, and settlement. Peer publications
may advance the shared environment, but they do not appear retroactively as the
current actor's byte effects, capability use, practice, or authorship.

Conflicts preserve every exact path/hash alternative. Only an authorized signed
resolution chooses or synthesizes bytes; the substrate does not resolve a
conflict from file type, role, task text, or model prose.

Before a branch merge, any pending bytes already materialized in the shared
workspace are committed as neutral environment history. A failed merge is
attested as a conflict only when Git produced a non-empty exact unmerged index;
a dirty-worktree refusal or other pre-merge obstruction remains a mechanical
failure and must not create a conflict reference or preservation authority.

Preserved conflict state does not pin later cognition to a stale worktree. Once
the exact authored head and preservation preimage are retained, each later turn
starts from current shared HEAD while the conflict remains open. This baseline
refresh selects no bytes and changes no resolution claim.

The immutable conflict reference commits the complete exact alternatives,
merge heads, and unmerged index. Inspection exposes those bytes for judgment
and also returns complete minimal resolution requests. The persona authors the
conflict reference, one mechanical resolution kind, and optional open rationale;
it does not retype a large hash preimage already committed by that reference.
An unknown or mistyped opaque reference is never prefix-matched, guessed, or
silently repaired by the substrate. Its authenticated inspection response
returns the exact current open-reference inventory owned by the caller, with
minimal inspection requests, so the persona can retry without spending another
turn rediscovering host state. A known non-owner reference instead returns its
exact owner identity without granting inspection or resolution authority.
Every publication lane, including an exact authorized-file publication, must
emit that same complete preservation evidence when it encounters a real
conflict. A later signed observation with the identical branch and exact
stage/blob unmerged index but no new preservation preimage is only a repeated
mechanical observation of the already-open conflict: it cannot replace or
invalidate the earlier complete authority, create another conflict, or count as
resolution. A differing or otherwise incomplete record fails closed.
For a persona-alternative choice, the workspace layer applies only the exact
selected alternatives to current shared HEAD, verifies every selected byte and
the resulting tree, commits any changed paths, and retains recoverable prior
refs before the persona signs the full resolution claim. It does not merge the
unrelated cumulative branch. Merely retrying the same unresolved merge is not a
resolution mechanism.

A delivered external artifact is active disposition pressure only until an
exact persona-authorized lifecycle action accounts for that same request,
receipt, destination, and content hash. Later situation projections compact a
uniquely matched resolved delivery into a content-bound disposition reference;
the immutable request and receipt remain available through their authenticated
inspection surface. This join never examines the prompt, provider, filename,
media meaning, task text, or bytes, and ambiguity retains the original pressure
instead of guessing. A resolved delivery must not consume later model calls by
presenting itself as perpetually unhandled.

An unresolved request registers one finite terminal-receipt successor rather
than a polling loop. Its delivery preserves the exact causal scope and the same
transferred signed budget that funded the request; a transport worker may not
replace that scope with an ambient allowance or reject it merely because the
actor thread's process-local context is absent. Replayed receipt delivery
deduplicates against the exact request/terminal event and cannot multiply model
calls.

## 7. Causal continuation

Another persona decision exists only through an exact causal event, such as:

- a persona-authored wake or schedule;
- a delivered peer message or invitation;
- an accepted membership event;
- a registered and delivered external/tool receipt;
- an authenticated principal, environment, lifecycle, or resource event; or
- another descriptor-declared event whose authority has actually been armed.

Every authentic successor is retained independently. Several may coexist. The
runtime does not choose one as a representative next stage or treat plural
successors as conflict.

Two stimulus classes are protocol-defined instances of the final bullet, not
new implicit successors. The sealed-turn-failure replay carrier re-delivers
the exact reference to a prior sealed turn-failure receipt to the persona that
authored the failed turn. The tool-mount correlation carrier delivers,
together, the exact reference to a sealed capability-mount receipt and the
exact reference to a prior sealed turn-failure receipt recorded under the same
environment and task. Each is executable only as a descriptor-declared event
whose authority has actually been armed: one-shot, prepaid from the exact
signed run grant at arm time under the same ledger rule as any finite wake,
bounded by a signed exact per-class fire cap and a mechanically increasing
minimum re-arm interval, held un-fired while the run it is bound to remains
live, and cancelled by exact authenticated acceptance. The carrier payload
contains exact record references only — never repaired arguments, a retry
instruction, a diagnosis, or new prose. Delivery gives the persona one
ordinary wake with its complete authorized action catalogue; whether anything
is retried, revised, or ignored remains entirely the persona's decision.
Sealing a failure receipt or mounting a capability still creates no
continuation by itself; only the armed descriptor does.

Exact authenticated acceptance retires exactly the governed carriers — the two
sealed-failure replay stimulus classes above and the §1 principal-declared
unaccepted re-wake bound — and nothing else. It neither cancels a
persona-authored armed wake nor confiscates the remaining signed run ledger;
every already-prepaid fire stays funded and deliverable, and any funded
post-acceptance turn may arm a further bounded successor under the ordinary
arm-time transfer rule below. Standing improvement after acceptance therefore
exists exactly where a persona authored it or a principal declared it; the
substrate implements no refinement loop, round counter, or convergence test.

A finite persona-authored immediate or scheduled wake is executable only when
its arm transition atomically transfers a complete bounded turn allowance from
the exact signed causal run ledger. The currently delivered event-local
allowance pays only for that already-admitted turn; recursively debiting its
remaining transport headroom would make a valid chain stop independently of the
run grant. Arming a new successor therefore debits the same exact run ledger at
arm time, while delivery still spends only the independently prepaid successor.
The signed marker binds the reservation hash, per-fire call cap, persona,
environment, task, request, run, and model pool. A bounded recurrence prepays
one independent allowance for every declared fire; an unbounded recurrence
requires explicitly unlimited authority. The arm append encloses the exact
reservation, and an append failure returns the uncommitted transfer. A
successful result therefore means the future work is durably armed and funded,
not merely that a timer was recorded.

Explicitly unlimited authority is the signed run budget grant whose closed
`budget_mode` member is exactly `"unlimited"`. It exists only when the
authenticated principal's intake names no finite model-call allocation: a
positive integer allocation creates a finite grant, an absent allocation
member creates the unlimited grant, and any other value is refused. The grant
is recorded as a signed lineage fact before any spend; it is never inferred
from schedule shape, task content, model identity, elapsed time, or exhaustion
of another grant. An unlimited grant removes only the finite run ledger: the
signed generic per-event call cap, the signed exact per-class fire bound, and
declared deadline/stop authority survive unchanged. Under a finite grant an
unbounded recurrence is refused with exact resource evidence and creates no
trigger.

One allowance is the bounded transport envelope for a single semantic turn:
at most one attempted call per eligible signed-pool body. Tool exchanges remain
inside that admitted provider turn and do not justify speculative extra model
turns. When the trigger fires, the kernel claims exactly one reserved allowance by
joining the signed arm transition, the signed fired transition, and its exact
ambient carrier. Each fire can claim at most once and the claim count cannot
exceed the prepaid bound. Finite scheduled work never falls back to whatever
shared run headroom happens to remain at delivery time. An explicitly unlimited
run instead receives the signed generic per-event cap. None of these operations
reads the schedule purpose, task text, domain, role, tool, filename, or payload
meaning.

An attempted continuation action that is mechanically refused returns an exact
stable reason code in its ordinary action evidence. The refusal proves only
that the attempted effect was not admitted; it does not create a successor,
recommend an alternative, or authorize a retry. Transport-injected task, actor,
run, wake, and lease bindings must agree with the public action schema and the
signed descriptor rather than becoming hidden model-authored fields.

One boundary case is not represented as a contradictory refusal: when a signed
work-state action explicitly carries an immediate disposition but the current
finite call has consumed the last run unit, that signed work state is durable
pending continuation authority. It is not an armed or executable successor and
allocates no resource. The action reports the exact `waiting_resource` delivery
state. A later independently authorized resource event delivers the current
work state back to its author under the recovered shared pool; only that event
creates executable call authority.

The same truthfulness applies before a wake arm exists. If a finite action
cannot prepay its requested future fire set, the action is refused with exact
resource evidence and creates no trigger. The UI and later cognition may show
the authored work state as waiting for resources, but may not show an unfunded
timer as an armed continuation.

Work-note prose, gap-like knowledge content, a population action, successful invocation,
artifact declaration, unchanged/changed workspace, score, objective statement,
HTTP status, and model claim do not create continuation.

## 8. Resource pause and resume

Budget exhaustion pauses affected pending deliveries and preserves their exact
event, task, model pool, workspace binding, and best-so-far bytes. It is not
semantic completion or failure.

Resource recovery also presents each active persona's latest verified work
state. If its exact disposition selected model-input paths, resolution occurs
against current bytes at this new delivery, after the prior turn settled. No
stale pre-exhaustion byte observation is reused.

A later exact resource grant resumes the original task generation. One signed
resource event fans out unchanged to all active members under the same bounded
pool; it does not transfer capacity only to a coordinator, owner, or one
host-selected pending edge. Per-recipient carriers enforce their own leases and
deduplication while preserving the common event identity.

Concurrent grants and replays are idempotent by exact authority. They cannot
duplicate a settled delivery, mint a new task, or manufacture another persona.

## 9. Objective acceptance

Acceptance comes only from exact authority and evidence declared by the
authenticated principal or an explicitly authorized verifier. Examples may
include a principal's signed acceptance, an authorized verifier receipt bound
to exact current bytes, or a principal-declared materialization condition.

When the principal declares that materialized output is required, that exact
causal requirement reaches the ordinary persona action loop. The run cannot
satisfy that objective until authenticated action effects and a published byte
delta against the exact task-entry baseline satisfy the mechanical condition;
prose alone cannot bypass it. One environment-wide baseline is captured before
the all-member ingress fan-out, with an exact private-worktree preimage for every
addressed member. It is not owned by a lead or output persona. Before published
evidence exists, an enforcing action turn may require bytes that differ from
that actor's exact preimage. As parallel turns proceed, every action boundary
may observe the current signed environment publication state; the first exact
task-bound publication by any authenticated member satisfies the shared run
condition and releases the remaining per-turn gates. This release chooses no
winner and credits tool use only to the actual author.

Once the run-level condition is verified, a causal descendant is not assigned
a fresh byte quota merely because the same signed contract remains in its
ancestry: communication, coordination, learning, population, and capability
actions may settle without manufacturing another file. Releasing the per-turn
gate is not semantic completion and does not suppress any persona's choice to
continue materializing or self-wake. This propagation does not choose a file
format, executable, profession, workflow, minimum team, or semantic quality
threshold. Those remain principal intent and persona action, while objective
acceptance remains separately authoritative.

The complete task-entry workspace baseline is closed enforcement state. It is
verified in full wherever the byte gate is evaluated, but it is not replayed as
an equal-share situation source on every model turn. The model-facing carrier
uses a dedicated, causally ordered materialization lane containing the exact
baseline hash, environment source-state signature, member-preimage and file
counts, the current mechanical outcome summary, and a hash-bound page of exact
current delta path/size/hash records. Fixed byte and page bounds may project that page with
explicit totals, cursors, omissions and manifests; they may not select records
from task words, paths, suffixes, media types, tools, domains, roles or content.
The full baseline remains available to enforcement and durable audit rather
than competing with principal intent, population, capabilities and current
progress in the prompt.

When the principal supplies `require_authenticated_effect_provenance` as true,
the mechanical condition additionally requires that each satisfying delta
record join to a signed execution receipt through that receipt's
`captured_output_hashes`, sealed under host authority: the exact published
path, content hash, and byte length must equal a captured output entry in an
authenticated action receipt of the same run. Bytes whose hashes join no such
receipt do not satisfy the floor, whatever their authored provenance prose.
The join compares only exact path, hash, and length equality; it reads no file
content, filename meaning, tool identity, or task text. When the member is
absent or false, the ordinary published byte delta suffices unchanged.

A resource-resume carrier and its private continuation state preserve that
complete verified baseline preimage. A bounded task-entry or UI projection may
summarize or page it, but that presentation can never be copied back as resume
authority. If a presentation compactor replaces records with an omission
marker, the exact baseline remains unchanged in the signed carrier and durable
continuation state; treating the compacted value as the next resume baseline
and stranding a funded task fails closed.

The substrate may verify:

- exact signatures, keys, scopes, and causal precedence;
- current artifact/workspace hashes, lengths, signed MIME, and publication
  provenance;
- current conflicts and access authority;
- exact verifier identity, inputs, descriptor, terminal result, and receipt;
  and
- exact principal acceptance or stop/cancel/deadline authority.

It does not infer substantive sufficiency from work notes, gap-like content,
member count, roles, file count, filenames, a successful tool call, stable
bytes, model confidence, a score, or prose saying “done.”

A verifier receipt extends into objective acceptance only under the named
`terminal_verdict_contract`: its terminal result carries the closed boolean
member `accepted`. Exactly true extends into acceptance under the declared
verifier authority; exactly false records a rejection fact; a terminal result
without the exact boolean member carries no verdict and is refused as
acceptance authority rather than interpreted. Receipts recorded before the
contract existed keep their recorded authority unchanged; the contract does
not rewrite, reclassify, or invalidate an already-verified receipt.

A currently registered persona identity key is a valid declared verifier key.
Verifier authority binds to exact signing-key facts — the declared key
identity or registration predicate, scope, current registration, and signature
verification — never to a species of key holder. Where principal intent
requires independent review, that independence is likewise established by
exact reviewer identity and the declared acceptance mechanism
([`04_PROJECT.md §5`](04_PROJECT.md#5-coordination-and-review)), not by which
kind of actor holds the key.

A persona-authored verifier receipt enters lineage only through the signed
`author_verifier_receipt` action
([`09_PROTOCOLS.md §2.5`](09_PROTOCOLS.md#25-persona-authored-verifier-receipts))
inside an ordinary funded turn. The action mechanically binds the exact
environment, task, run, scope, intake declaration, and adjudicated publication
it speaks about; it is refused outside an authenticated turn; and it creates
no continuation, wake, or successor. No other ingress exists: prose in a note,
artifact, or message never becomes a verifier receipt.

A predicate-mode declaration names a registration predicate instead of one
key: a `verifier_descriptor` whose exact member set is `{kind, scope}` with
`kind` exactly `"registered-persona-identity/1"`. The declaration schema is
unchanged; the descriptor's `kind` member is itself the era-visible marker,
and a reader that predates it refuses the whole declaration rather than
misreading it. Under that declaration a receipt extends into acceptance only
when three mechanical invariants all hold: (i) the receipt signature verifies
over the hardened preimage against a currently registered persona identity
key; (ii) the signing key has zero authorship edges to the delivered bytes —
an exact size/sha256 identity join over the signed authorship claims: the
run family's `ENV_WORKSPACE_PUBLISHED` records and `ARTIFACT_DECLARED`
records return no intersection with the adjudicated delivered identities for
that signer. Turn-effect byte deltas are deliberately not authorship edges:
byte identity cannot distinguish independent re-derivation of the same bytes
from authorship, and an executed counter-check that captured the delivered
bytes must not disable the very receipt it evidences; and (iii) the signer
holds executed counter-evidence — the host-sealed executed-effect digests of
the signer's own authenticated turns intersect the adjudicated publication's
digest set. Each invariant is a signature, hash, or exact join over
already-signed records; none reads file content, verdict prose, tool
identity, or task text. A receipt failing any invariant is recorded as a
fact and carries no acceptance authority; unknown or ambiguous authorship
fails closed.

Invariant (ii) is the self-acceptance exclusion: a key with an authorship edge
into the delivered bytes cannot extend those bytes into acceptance, whatever
its terminal result says. The refusal is a recorded fact about the receipt,
never a substrate appraisal of the work.

The invariants carry a perceivability duty: an invariant a candidate cannot
mechanically see is an invariant it can only guess at. Under a predicate-mode
declaration the acceptance projection therefore always carries the
adjudicated-delivery page — the exact byte identities (opaque path, size,
sha256) of the latest admitted publication, its publication event identity,
and its publisher — in the acceptance facts, the dedicated prompt lane, and
every `author_verifier_receipt` reply, before any receipt exists. The page is
pure carriage of already-verified identity rows; the first live predicate run
demonstrated why it is load-bearing: three disjoint signers re-derived the
package deterministically yet authored seventeen non-extending receipts,
because the exact digest set their sealed captures had to intersect was
recorded but nowhere perceivable.

The same duty covers the improvement ratchet. "Not acceptance-worthy if it
only matches evidence classes already accepted" is a counterparty judgement
the substrate never scores — but its comparison set is a recorded fact, so
the projection carries the accepted-evidence baseline: for every acceptance
so far, the exact delivered byte identities its signer held sealed executed
evidence of. A candidate verifier judging a successor delivery can therefore
compare mechanically whether the new delivery and its own counter-evidence
include any identity absent from every prior acceptance's evidenced set,
instead of guessing what an earlier round already proved. The baseline is
empty until the first acceptance exists; the substrate still records any
verdict either way.

Predicate-mode verdicts rest on the hardened preimage contract. A recorded
receipt carries two era members beside `terminal_verdict_contract`
`"closed-boolean/1"` above: `receipt_authority_contract`
`"persona-disjoint/1"` — receipts recorded under it submit every
persona-identity-key signer to the invariants — and `signature_scheme`,
`"domain-separated-bound-preimage/1"` for a signature over the hardened
preimage versus `"open-canonical-preimage/1"` for the legacy open form,
which retains acceptance authority only for non-persona keys of the
exact-key declaration. The signed preimage
binds the exact run, byte-state, and declaration hashes it adjudicates;
[`09_PROTOCOLS.md §2.5`](09_PROTOCOLS.md#25-persona-authored-verifier-receipts)
defines the exact member set. A signature over fewer members carries no
verdict under the predicate declaration. Receipts recorded before this
contract keep their recorded authority unchanged, under the same era rule as
the terminal-verdict contract.

Principal intent may ask for open-ended improvement. Personas decide what
comparisons, measurements, exploration, review, or further work are useful and
may author causal wakes for them. The host does not implement a universal
refinement loop, epsilon, convergence test, or round counter. Acceptance of
one exact byte state does not terminate that authority: personas may keep or
newly arm bounded causal wakes from the remaining prepaid allowance under §7,
and a later acceptance is a new exact authority fact over the then-current
bytes.

## 10. Quiescence and terminal authority

When no causal delivery is pending, a task is **quiescent**. Quiescence is
nonterminal: it means only that no work is currently scheduled. It does not mean
ready, complete, sufficient, abandoned, failed, converged, or incapable of
further improvement.

A later authentic principal event, resource grant, peer message, external
receipt, membership event, or persona-authored wake may resume the same task.

Only exact authenticated acceptance, cancellation, stop, deadline, lifecycle
termination, or other explicitly declared authority can create its corresponding
terminal state. Budget exhaustion remains a pause unless that authority says
otherwise.

A persona's signed `no_successor` remains attributable but represents the
current mechanical frontier only when its exact observed situation—or a
kernel-signed isolated-disposition settlement—rejoins the current workspace
state signature. Later exact state does not invalidate the historical record,
but it makes that terminal-frontier binding visibly unbound until the persona
independently authors another disposition. This fact neither schedules the
persona nor implies that more work is semantically required.

## 11. Model-call economy

A model call requires one authentic causal delivery, a current persona/lifecycle
lease, and exact resource authority. Inventory projection, discovery, replay,
signature verification, workspace sync, MIME verification, fan-out,
deduplication, settlement, and public rendering are mechanical and consume no
model call.

The call also requires an authenticated `run-model-pool/2`. A matching signed
`persona-model-choice/1` supplies persona-authored model order and reasoning
effort for its exact causal generation. Without one, only the separately signed
principal bootstrap body may receive cognition. A pool lacking that authority
is refused; refusal
does not trigger a host-selected choice-authoring call or fallback.

Effect-free transient provider/transport failure may retry the exact carrier
under bounded policy. Deterministic malformed requests are not infrastructure
outages. An effectful or uncertain turn is never replayed to obtain nicer
terminal prose.

Process-local capture handles, transport capabilities, callbacks, and other
host-only authority are removed before action observations enter a canonical
communication, memory, learning-history, or turn-effect record. Signed evidence
contains exact public inputs, outputs, descriptors, receipts, and effects, never
a reusable private runtime capability.

No host-generated status poll, readiness repair, identity completion call,
capability appraisal, population appraisal, completion appraisal, or automatic
reflection call exists.

## 12. Public projection

Human-facing task state distinguishes verified facts from authored claims:

- exact principal intent and task identity;
- active members and delivery/resource state;
- current artifacts, formats, provenance, conflicts, and render availability;
- exact causal events and pending/settled carriers;
- persona-authored note appends labelled by author, append time, exact observed
  situation, and factual observation-hash binding;
- each persona's exact causal disposition, terminal-frontier binding or
  re-authorship fact, and the unranked aggregate disposition frontier;
- exact verifier verdict facts — each recorded terminal verdict with its
  verifier identity and closed `accepted` boolean, where a rejection remains a
  fact about the verifier's exact signed result, never a substrate appraisal
  of the work, zero recorded verdicts is stated as zero, and a predicate-mode
  verdict additionally records which of its mechanical invariants held, as
  exact booleans; and
- explicit acceptance, pause, cancellation, or quiescence facts.

It never relabels quiescence as done, a singleton note as team consensus, an
artifact title as independent review, or model/tool success as objective
acceptance.

## 13. Removed compatibility surface

There is no live compatibility for task classes, task classifiers, routing
modes, acceptance-pathway seeds, mission charters, mission frames,
ContinuousRefinement, objective/epsilon/round schemas, structured work
readiness, requirement-coverage reducers, promotion triggers, horizon keyword
detectors, host-defined team roles, or task-specific tool recipes. Historical
bytes may remain opaque lineage but carry no current task authority.

## 14. Design criteria

1. Exact principal intent is preserved through every carrier and resume.
2. Task and resource events fan out unchanged to every active member.
3. Every ordinary member wake exposes the complete authorized action surface.
4. Personas choose navigation, tools, collaboration, population, artifacts, and
   further work without substrate selectors.
5. Work notes and gap-like authored content never determine completion or
   continuation.
6. Artifact MIME and plural domain references are explicit signed facts.
7. Objective acceptance comes only from exact authenticated authority.
8. Quiescence is nonterminal.
9. Model selection comes from exact persona choice or an unambiguous one-body
   admission, never task semantics or provider order.
10. Public task state distinguishes historical persona dispositions from those
    bound to the current exact mechanical frontier.

## 15. Risks & known limitations

| ID | Risk | Severity | Likelihood | Mitigation | Target release |
|----|------|----------|------------|------------|----------------|
| TASKS-R1 | Predicate-mode verifier collusion / rubber-stamping: a distinct persona key can execute minimal counter-evidence and sign `accepted: true`. The §9 invariants price acceptance in executed evidence and forbid self-acceptance; they cannot make verification rigorous. | High | Medium | Behavioral by design: principal charter text carries withhold/deficiency norms; population and economic dynamics ([`16_POPULATION_DYNAMICS.md`](16_POPULATION_DYNAMICS.md), [`17_ECONOMY.md`](17_ECONOMY.md)) carry selection pressure; the §12 projection records which invariants held so a principal can audit cheap verdicts. | Open (behavioral) |

## 16. Open questions

- **OQ-TASKS-1** — Should the executed counter-evidence join (§9 invariant
  (iii)) require a minimum causal depth — a joined execution receipt
  post-dating the adjudicated byte state — or does the preimage's
  publication-hash binding suffice?
- **OQ-TASKS-2** — Should a future intake schema require an explicit
  affirmative unlimited member instead of deriving the unlimited grant from
  member absence (§7)?
