---
title: PersonaOS — User-Intent and Operating-Path Criteria
status: Stable
---

# 11 — User-Intent and Operating-Path Criteria

The authenticated principal's exact intent and this design specification are
the product criteria. A test corpus, model score, prompt phrase, keyword list,
regular expression, filename convention, profession catalogue, or host-authored
workflow is not a second specification.

## 1. Evidence policy

A criterion is supported only by current operating-path evidence, such as:

- verified signed node, environment, membership, persona, task, and workspace
  records;
- exact lineage, action, communication, resource, and tool receipts;
- exact artifact bytes, hashes, signed MIME declarations, and render results;
- persona-authored notes, identity material, capability records, learning, and
  population actions, each labelled as an authored claim rather than kernel
  truth; and
- direct human inspection or acceptance by the exact authority named by the
  task.

A model's claim, an HTTP success, an old persisted run, a score, a mock, or a
file named after an outcome is not evidence that the current operating path
achieved that outcome.

## 2. Operating-path criteria

### C-OP-1 — Fresh means fresh

After an explicitly requested clean start, no old node lease, environment,
membership, persona, task, workspace, route, or browser row is presented as
current. Historical bytes may remain outside the active projection, clearly
labelled as history, but cannot regain authority by being cached.

### C-OP-2 — Discovery is fast, concurrent, and incremental

Local, direct, rendezvous, DHT, and gossip routes may race concurrently. A node
appears as soon as its current master identity verifies; environments and
personas appear as soon as their compact signed inventory entries verify. The
UI does not wait for a global scan, artifact hydration, telemetry, or the
slowest peer before painting verified identities.

After identity and provider routing verify, independently signed dynamic
documents may race the peer data read with that same provider's anonymous
direct route. The first usable document still undergoes its full content,
identity, and current-master verification. A stalled peer transport therefore
cannot consume the whole refresh deadline and erase current thinking or
development from presentation; the race neither consults a locator nor changes
discovery authority.

Each verified compact persona row carries its exact per-persona telemetry
route. The UI requests those small subject-signed feeds concurrently as soon as
the identity slice is admitted, without waiting for the complete artifact/task
inventory or the node-wide telemetry aggregate. The current
`personaos-persona-telemetry-public/2` feed includes the latest exact verified
`personaos-persona-work-state-surface/4`, if one exists. It preserves the open
persona-authored note and causal disposition without interpreting either. Rich
cognition histories remain independent and may hydrate concurrently afterward;
one persona's bytes or signature work cannot serialize the rest of the visible
population.

Every carrier exposes the same current-master-signed compact identity index.
Cached verified bytes may accelerate the first paint but do not extend expiry,
create routing authority, or keep an identity omitted from fresh sources.
Readers and publishers share an atomic generation boundary when an aggregate is
updated in place. A reader may observe the complete prior or next signed
generation; it must not observe partial mutation as a real removal or cache that
false absence into a public-route authorization decision.

Live topology names only currently verified active memberships. A running model
call, active or paused run participant, invitation, birth record, or historical
inactive membership remains separately observable under its own exact state but
cannot widen the environment's member list or turn an away persona into an
active member. Public member counts apply the same rule, so historical
membership does not survive as a stale current row.

An HTTP locator, including `node1.personas.ai`, is a replaceable last-resort
route hint used only when no primary route is viable. It is never global
authority or an availability dependency. Source-scoped reconciliation and
signed expiry remove stale records.

A node renews a short self-signed fallback lease only while its own primary
plane is not viable. A healthy primary route suppresses both locator reads and
producer announcements; disconnected consumers independently enter fallback
from their own observed state. Earlier leases expire without renewal.

### C-OP-3 — Identity is optional evolution, never work admission

Persona continuity is established by keys, signed lineage, lifecycle, and
membership—not by a display name, portrait, role label, model session, or
browser cache. A persona may author or revise public identity during any
ordinary wake, alongside the full ordinary action catalog. Identity evolution
has no dedicated phase, readiness gate, required sequence, retry loop, or
work-blocking surface.

Public presentation requirements such as a meaningful display name,
description, portrait, person-like subject, artistic style, or characteristic
grounding exist only when exact authenticated principal or user intent requires
them. The kernel has no default name, profession, face, OCEAN, VAD, style, or
portrait-content constant. It verifies authority, signatures, exact byte
bindings, signed MIME, bounds, and provenance without inspecting pixels or
inventing identity.

When optional fields are absent, the UI uses an honest neutral placeholder and
labels the field as not yet authored. It never displays a guessed role, parses a
profession from a name, or hides an otherwise active persona.

### C-OP-4 — Continuity and resume preserve exact identity and causality

Resuming an environment restores exact verified members, keys, lineage,
workspace replicas, memories, skills, authored notes, communications,
capability records, and unsettled causal events. It does not mint replacement
personas because process memory was lost. A prior persona resumes only when its
signed durable state verifies; failure is explicit.

Every amendment and continuation also restores the complete verified signed
principal-intent ancestry in causal order. The latest prompt cannot replace or
summarize the original principal bytes. If the complete exact ancestry exceeds
its mechanical carrier bound, the amendment is refused before execution rather
than silently omitting or summarizing an older principal event.

The current intent and verified ancestry occupy their own complete prompt
authority lane. Generic uniform source projection applies only to the remaining
situation facts. Intake and prompt construction share the exact carrier bound,
so a task that fits durable storage but not cognition transport cannot be
silently admitted with a truncated principal instruction.

The prompt preserves one complete mechanical navigation authority alongside
the principal lane: every currently leased action identity with a uniform
content-blind description window, explicit completeness flag, and
required-input/effect shape, every exact
name in the execution-capability index, verified roster/birth/replication
authority, every current workspace file path, exact current identity/readiness
state, zero-inclusive capability-acquisition state, and the hash-bound
manifests and cursors of the persona's retained learning. Exact action
descriptors and history bodies remain behind their authenticated inspectors and
cursors; the navigation lane neither selects nor activates one. Its
construction and bounds are content-neutral. No task token, regular expression,
domain role, preferred tool, preferred team size, filename type, ranking, or
recommendation may choose what survives transport. Append-only contribution
and exact learning bodies remain independently pageable.

The uniform description window is large enough to carry ordinary current
registry descriptions whole. Oversized descriptions remain explicitly
incomplete and inspector-addressable. A mechanically complete action identity
whose description is always cut before the action's effect, successor,
acquisition, or application mechanics are visible does not satisfy practical
navigation.

Direct task/resource delivery and every event-driven wake construct this same
navigation authority from the same seven live sources. An event-wake path may
not silently fall back to the older four-source carrier. If the combined lane
crosses its byte bound, every component receives the same mechanical byte
opportunity; an oversized component becomes a hash-bound structural index.
Component meaning, task prose, field words, and record contents never decide
which whole lane disappears. A mechanically compact complete-identity index
that fits its equal share must remain inline: duplicating counts or summaries in
its wrapper may not push all action or execution-capability names behind a
hash-only outline.

The complete-descriptor catalogue hash and the compact prompt-projection hash
bind different canonical preimages. Validation must verify the compact rows
against the projection hash while retaining the source hash as the address of
the independently inspectable descriptors; equating the two would reject every
nontrivial projection.

The durable current-mission situation is not a second copy of those same live
lanes. `personaos-current-persona-mission-situation-facts/3` carries its exact
situation and lineage identities, canonical size, and a complete mechanically
ordered component manifest whose rows bind every field name, type, hash, byte
length, schema when present, and inline disposition. The exact task facts stay
inline because caller-authored continuation context participates in the signed
model-choice scope. Environment, package, team, resource, population,
workspace, learning, action, capability, identity, and work-state bodies use
their existing dedicated lanes and inspectors rather than being recursively
copied through the mission join. No field meaning determines manifest order or
inline admission, and the full signed situation remains durable by its exact
hash. A pointer-heavy bounded projection of a repeated full situation is not a
valid substitute: it consumes cognition bytes while obscuring current choices.

Project presence on resume is reduced from reciprocal signed topology, not a
disposable environment attribute. The model-visible environment state includes
the complete verified project-id set and exact topology event references. A
signed scheduled trigger that still verifies against its persona, environment,
task, run pool, and execution authority is reported as a bound event-driven
handoff rather than as an unbound or completed task.

When a resource event resumes work, the exact same signed event and content
hash are offered concurrently to **every active environment member** under the
same bounded resource pool. Each member receives its own delivery carrier and
deduplication identity, but the substrate does not select an owner,
coordinator, representative, role, or preferred recipient. Fan-out provides an
opportunity to act; it does not mean the task is incomplete, complete, or that
every recipient must call a model.

A causal descendant created by a native model action retains the exact signed
run/pool binding and the identical process-local budget object even when the
action crosses a transport worker. That authority remains event-local and is
never inserted into the run-wide inheritable scope. It is not serialized:
restart delivery still requires the descendant's signed recovery descriptor,
one exact positive lifecycle lease, and a separately verified resource grant.
Hot recovery and collaboration reducers select exact event kinds and preserve
their original append positions; they do not detach an entire lineage merely
to find a lease, invitation, communication, membership edge, or birth outcome.

An initially published `running` shell is presentation, not durable liveness.
If no process-local run/event remains and the exact kernel-signed pool's finite
grant has zero headroom in its verified adjustment ledger, that same run is
offered as an interrupted budget pause and supersedes its older resume source.
No task or output content participates, and this reconciliation neither changes
the shell nor calls a model; only later signed resource evidence can resume it.

### C-OP-5 — Human-facing work notes are claims, not completion state

The persona view may lead with the most recently appended exact persona-
authored work note and its provenance: author, task, exact observed situation,
append time, causal references, signature, and the factual observation-hash
binding. “Most recently appended” is presentation order, not current thought or
task state. Model name, HTTP status, raw latency, hashes, and replay mechanics
are secondary details.

`work_note` is a bounded open document. Its keys have no substrate semantics.
No note, collection of notes, status word, commitment, blocker, vote, or
persona-written “done” claim satisfies or defeats objective acceptance. A note
does not create continuation, a workflow phase, capability-gap state, a population
action, or a requirement-coverage result. Invalid signatures or envelopes are
refused mechanically. A false `bound_to_latest_observation` is only hash
inequality, never a stale/current label, and no note is repaired through a
hidden model call.

If no note exists, the UI says so rather than inventing current thought,
activity, accomplishment, or readiness.

Work-note revision and prior-record pointers are substrate-derived append
integrity only. Workspace/action settlement and later observations never defer,
settle, supersede, or reclassify a note; complete signed history remains
navigable.

### C-OP-6 — Artifact identity, format, and rendering are explicit

Every artifact row leads with a readable basename and a visually prominent
format badge; the parent path is secondary and the exact full path remains
available. Artifact role, filename, and extension are presentation hints, not
format authority.

Every artifact declaration binds an explicit normalized `mime_type` inside the
signed payload to the exact content hash and byte length. Renderer selection
begins from those verified bytes and signed MIME authority. Suffixes, declared
roles, and safe byte inspection may detect a mismatch or choose a conservative
fallback, but cannot silently replace the signed declaration.

That declaration continues to describe the same unchanged exact bytes across
later task amendments when persona, environment, path, hash, length, and access
authority still match. Its task/action binding remains original provenance; a
new current task identifier does not invalidate it. Changed bytes require a new
signed declaration and cannot borrow MIME from an older path revision.

Renderers load lazily and support the strongest safe view available for text,
Markdown, source, structured data, raster and vector images, PDF and office
documents, archives, audio/video, meshes, point clouds, and CAD/BIM. Unsupported
or malformed content receives an honest download/technical fallback, never a
misleading generic binary preview when a verified supported format exists.

Persona identity media and task artifacts remain distinct only through exact
signed role authority. Classification never depends on path words, extensions,
MIME alone, prompts, or content inspection.

### C-OP-7 — Capabilities, memory, skills, and artifacts are persona-navigated

The substrate presents complete bounded, paginated, exact, **unranked**
inventories of currently authorized actions, local execution names,
environment-mounted tools, visible peer tool/persona-knowledge metadata, memory
records, and accessible knowledge references. Deterministic lexical, append, or cursor
order is transport order only. There is no relevance score, similarity score,
fitness, top-K, host recommendation, task classifier, or prompt-selected subset.

For a native MCP body, each exact leased action is presented directly under its
real action name with the complete persona-facing descriptor. The model does not
first inspect a transport-private catalogue and then transcribe a selected name
into a generic invoker. For a structured-only body, the complete unranked
catalogue remains in-band. Both paths revalidate the same signed live descriptor
and principal at dispatch; neither path selects or ranks an action.

An exact local capability query may accept several independent literal
substrings and return their stable unranked union. It declares that mechanical
match mode; it must not silently require one record to contain every independent
query value. Exact identifier lookup remains separately available, and neither
mode recommends or invokes a result.

An append-derived inventory binds an exact snapshot, absolute positions, total,
returned and omitted counts, and continuation cursor. Equal payloads at
different authoritative append positions remain separately navigable. If one
signed identity is redundantly observed through several source scopes, the raw
page retains every observation. A separate exact unique-identity view must
expose duplicate counts/ranges and raw-page navigation rather than silently
reduce cardinality.

Personas may inspect, communicate/share exact refs, obtain authorized bodies,
search, acquire/provision/experiment with/invoke tools, author opaque reusable
material, delegate, create an artifact, revise identity, or ignore an inventory
item in any order they choose. A perceived gap is optional meaning inside opaque
persona-authored knowledge, without a dedicated record/action/lifecycle.
Expressing, revising, or omitting it never gates work, completion, identity,
action visibility, or another wake.

Body availability is never inferred from catalogue membership. One generic
persona-signed publication/withdrawal action must bind an exact owned source and
its canonical bytes. Discovery carries that commitment rather than the body.
When current policy grants public read, a protocol-derived peer route may serve
one provider-signed exact-body envelope. Acquisition requires the receiving
persona's separately authenticated exact record/hash choice, performs a direct
peer fetch without a central fallback, and independently verifies provider,
author, source, size, and hashes. It then retains the exact acquisition.
Executable structural bodies traverse the same opaque provision/smoke/declared-
verification boundary as locally authored recipes; non-executable structural
bodies have no automatic behavioral effect. Later cognition can navigate every
retained acquisition by exact id and content window. No task, domain, role,
filename, extension, MIME value, capability label, or tool name participates in
publication, selection, transfer, retention, or application.

`author_persona_knowledge` admits one signed
`personaos-persona-state-record/1` per invocation. Authenticated context supplies
the actor and verifies any optional environment/task binding; the record carries mechanical
`record_kind: "persona_knowledge"`, opaque content, exact evidence refs, time,
key, and signature. The substrate requires no semantic kind, name, description,
interface, parent-skill relation, synthesize/compose operation, rationale,
review, transfer, conflict, disposition, promotion, or score. A persona may
express and cite any such meaning inside open content.

That explicit authored record joins the owner's ordinary future-cognition
inventory. Exact same-environment records compete in one content-addressed,
unranked, mechanically count/byte-bounded Layer-4 page; the original task id is
provenance, not a later-task exclusion rule. The substrate does not infer a
lesson or activate a tactic. Persona-authored brain fragments and their exact
carrier bindings remain the separate mechanism for material the persona wants
to govern as active tactics.

Ordinary future cognition also receives a fixed bounded suffix of the owner's
exact signed state records, including their opaque bodies. Inclusion is solely
by authoritative append position, with exact source count, range, and hashes;
the complete lane remains pageable by cursor. The runtime does not inspect a
record to match the current task, choose a lesson, infer a profession, award
expertise, activate a tactic, or recommend an action. Thus authored experience
can actually inform later persona reasoning without becoming host-directed
behaviour.

Receipts prove exact provider, invocation, terminal result, byte effects, and
provenance. They do not prove expertise, professional quality, semantic
relevance, or that a particular workflow was followed. Reusable learning,
experience, and identity evolution arise only through explicit persona-authored
signed records, not automatic host credit. Returning those exact records to the
author's future unranked inventory is continuity of their choice, not a
competence judgment.

Sealed turn-effect episodes are included in the exact bounded history visible
on later authorized wakes. `inspect_persona_learning_history` pages that same
hash-bound inventory without semantic selection. `apply_brain_evolution`
exposes the exact fragment storage operations and open persona-authored fields
needed to turn cited experience into future persona-owned material; neither
action creates competence credit or continuation.

A persona may convert its own cited experience into an opaque fragment and bind
an exact signed revision to exact current carrier identities. The binding is a
separate owner decision: retaining a note or receipt never activates it. A later
matching carrier verifies the binding, current fragment preimage, and scope,
then includes the exact body under mechanical count/byte bounds with explicit
omissions. No task words, embeddings, role labels, domain names, utility score,
or host prompt template selects it. Revising the same binding to an empty exact
set removes it without a host-defined lifecycle vocabulary.

An authored fragment scope is either empty, universal, or one exact identity in
the authenticated current carrier. A syntactically valid but unavailable scope
is refused before persistence and the exact available carrier identities are
returned so the persona can revise its own choice. The substrate must never
accept a semantic alias such as a generic persona, task, profession, or domain
label and then silently omit that supposedly learned material from every later
compile.

Public presentation may project the verified evidence chain—authored fragment,
current exact binding, observed action identities and counts, persona-authored
acquisition/provisioning, invocation receipts, and exact completed host-command
receipt pairs. A host-command projection exposes only the mechanically observed
launcher and any HMAC-verified sampled descendant executable identities,
attempt/success counts, time, and command hash. Sampling is explicitly
incomplete, so absence proves nothing; the projection does not parse a shell
program to infer tools. It labels those facts as
development evidence, not an expertise award, education credential, quality
score, or inferred profession. Bodies outside public authority remain absent.
The actor join follows the exact field declared by each signed event family;
capability/tool receipts and host-command receipts need not reuse one actor
field name, and a projection may not drop valid command evidence by assuming
that they do.

The presentation verifier implements the current closed action-authority
schema exactly, including the dispatch-descriptor hash and the bounded array of
opaque declared replication-effect descriptors. It verifies descriptor shape,
action identity, hashes, actor key, and signature without assigning meaning to
an effect kind. An unsupported older envelope fails visibly; it is not guessed,
silently adapted, or used as a reason to discard a valid current envelope.

The bounded carrier includes a content-neutral reference to the append frontier
for sealed turn-effect episodes so an oversized earlier receipt cannot make the
causal tip opaque. It declares exact source count/range/hash, manifest hash and
record count, plus a bounded exact suffix of authenticated failed-result
observations. The complete manifest/effect page remains available from the
authenticated inspector, while the separate exact usage inventory carries
mechanical invocation counts. This is fixed log-position projection, not task-,
role-, outcome-, quality-, utility-, or vocabulary-based retrieval. Repeating
the same recent action-name list on every wake is not learning content and may
not crowd out the current action meanings or persona-authored state bodies. A
single verified action receipt observed in multiple provider wrappers counts as
one invocation; redundant observation cardinality remains diagnostic metadata.
Only its verified receipt hash is used for that coalescing, while distinct
verified identities remain separate without semantic comparison.

Large canonical observation bodies are persisted once behind verified
content-addressed references. Communication, ambient routing, notification,
action-turn, and post-effect records refer to that exact body or its signed
source event rather than recursively embedding prior situations. Reducers that
need a small event family use the verified exact-kind index and retain original
append positions; they do not detach and copy the unrelated lineage.

The persona-authored state lane has an independent exact append-order cursor,
so later records remain reachable as execution receipts accumulate. An exact
original task binding remains provenance, not a visibility fence: owner-
authorized state can remain navigable on later tasks in the same environment.

The runtime contains no task word, profession word, executable name, filename,
extension, media type, prompt, regular expression, domain label, or hard-coded
deliverable that chooses a capability, acquisition, specialization, population
change, collaborator, team shape, artifact form, or next action. When a persona
judges some capability or artifact necessary, the operating path must let it
discover or obtain the capability and materialize real bytes with exact
provenance.

### C-OP-8 — Population change is explicit, bounded, and persona-authored

Every action descriptor that can cause new identity materialization carries an
explicit signed `personaosReplicationEffects` array of
`personaos-replication-effect-descriptor/1` records. Each record declares one
opaque exact `effect_kind`. The descriptor is mechanical ReplicationBound
authority only; the substrate never derives it from an action name, arguments,
task text, role, executable, prompt, or domain vocabulary.

When the live registry is compacted for a bounded persona carrier, these exact
replication-effect descriptors remain attached to the corresponding action row;
a name/description-only projection is insufficient population authority.

Population context transports compact signed contribution references, not the
entire prior situation embedded inside every work-state surface. Each reference
retains exact persona/environment/task/work-state/note identities, hashes,
signatures, causal refs, supersession state, and the current authored work note.
The full signed surface remains independently addressable. Repeated population
publication therefore grows with new contributions rather than recursively
copying all earlier situation carriers.

A persona may choose an authorized population action during any ordinary wake.
One admitted `personaos-persona-birth-proposal/5` produces only its exactly
declared bounded effect and invitation. The newborn independently accepts or
refuses membership. The kernel verifies signatures, exact task, environment,
membership, action, wake and run bindings, capacity, consent, integrity,
replication bounds, and per-proposal idempotency; it does not judge a need,
invent a role, choose characteristics, assign expertise, or require a team
size.

Identity admission and first-wake durability are separate commit boundaries.
If execution stops between them, exact resource recovery may reconstruct only
the missing outbox of that already-admitted identity from its one signed
proposal, one signed admitted outcome, persisted provenance, and exact run/pool
binding. Recovery reuses the same persona and any exact prior lifecycle lease,
publishes the deterministic consent invitation, and treats `genesis_context`
as opaque bytes. It never admits a replacement birth or derives a role, need,
workflow, or capability choice from that content.

An unresolved invitation becomes deliverable when the addressed persona has a
materialized identity. Its ordinary delivery identity is bound to the exact
invitation, addressed persona, and environment—not to mutable name,
characteristic, or avatar revisions. Those revisions remain evidence on the
delivery but cannot each spend another invitation turn. Restart/resource
replay is a separate exact causal opportunity and is deduplicated by its replay
event; neither delivery form accepts membership automatically.

No birth is a valid emergent outcome. Multiple births are also possible when
distinct persona-authored proposals and mechanical bounds permit them.
Population context supplied to a persona contains only exact signed facts: active member
identities, authored public cards, memberships, contributions, communications,
population actions, receipts, and bounded resource authority. It contains no
host-derived pressure, need, fitness, competence, diversity, role coverage,
team requirement, or recommendation.

### C-OP-9 — Coordination is plural without a host-authored team doctrine

All active members may observe the exact same resumed resource event, inspect
the same shared facts, communicate, review, publish, request help, transfer
knowledge, or remain quiescent. The kernel does not elect a lead, enforce a
handoff order, divide tasks, count votes, demand independent review, or infer
that another persona is necessary.

Each communication, publication, invitation, review, and wake retains its own
signed authority and causal identity. Several successor edges may coexist. The
runtime neither collapses them into one representative next step nor converts
population prose into an action.

The complete verified collaboration source is hash-bound in
`personaos-coordination-lineage-snapshot/1`. Any provider-bounded collaboration
or whole-prompt projection exposes exact source totals, page/cursor ranges,
returned, omitted, and truncated counts, manifest hashes, continuation cursors,
and completeness. Latest-per-active-member coverage is an additional exact page,
not a coordinator or semantic priority. Content-hash ordering, append order,
contiguous event windows, and uniform byte allocation carry no relevance or
next-action meaning; omitted records remain explicitly navigable.

Shared workspace effects remain attributable. A persona's leased worktree is
settled before peer-arriving bytes are merged into it, so another member's
publication cannot be credited as the current actor's tool use or artifact.

### C-OP-10 — Model calls purchase persona decisions

A model call occurs only for an authentic causal delivery with exact resource
authority. Status reports, gap-like authored content, population records, identity omissions,
scores, retry prose, note fields, and host-derived “more work possible” signals
do not create calls.

`goal_progress` is an observational append even when its open status text says
work remains. Its receipt explicitly reports that objective acceptance was not
changed and no causal successor was enqueued. A work-state append must carry a
separate explicit persona-authored causal disposition in the same signed action:
either deliberately no successor or one exact immediate wake. The disposition
is not inferred from the open note, and neither choice establishes objective
acceptance. Other actions create later turns only when their descriptor declares
and registers a causal delivery.

Optional successor model-input paths are exact persona-authored selections.
Their byte observations occur at successor delivery after all current-turn
effects settle, not while potentially concurrent tool calls are still running.
The delivery record binds size and content hash or exposes exact resolution
failure. Path selection and delivery never infer a file kind or choose a
renderer, tool, or workflow. A generic path must not be sent blindly through an
image-only provider input; exact workspace navigation remains available for all
formats, while a native media attachment requires separate verified media
authority.

Each persona call is bound to an authenticated `run-model-pool/1`, which is an
unordered ceiling. An exact matching signed `persona-model-choice/1` supplies
persona-authored model order and reasoning effort for that causal generation.
Before such a choice exists, substantive cognition may begin only if mechanical
admission leaves exactly one callable model. Two or more eligible bodies fail
closed; provider/registry/configuration order, lexical order, a default client,
cost/tier heuristics, or a host-selected bootstrap model cannot decide for the
persona.

Action results return to the current persona decision when the transport permits
it. An asynchronous result creates a later delivery only through its exact
descriptor-declared and registered event. Effect-free transient transport may
retry the same delivery under bounded policy; an effectful outcome is never
replayed merely to obtain improved prose.

External delivery pressure is likewise exact and non-repeating. When a verified
persona lifecycle action accounts for one uniquely matching request, receipt,
destination, and content hash, later reasoning contexts carry a compact
content-bound disposition rather than the full delivery as still awaiting
action. The immutable exchange record remains inspectable. Prompt, provider,
filename, media meaning, task text, and artifact bytes never choose or imply the
disposition, and an ambiguous join fails closed without reducing pressure.

Continuation-action refusals carry exact stable mechanical reason codes through
the same evidence lane as successful receipts. A refusal does not create a
causal successor, recommend another action, or justify a model retry. Public
schemas, descriptor bindings, and transport-injected actor/task/run/wake
authority remain consistent so the persona is not asked to invent host-owned
credentials.

The live dispatch descriptor keeps its exact transport fields and hash, while
the provider-facing schema omits only fields already bound by the authenticated
current principal. Dispatch injects those values before live-schema validation,
and signed persona-authorship bytes exclude them. Conversely, an action's
persona-authored execution-directory argument is a real choice and must not be
overwritten by the authenticated workspace default. Relative execution
directories resolve from that workspace, and publication remains confined to
it. These rules are derived from descriptor authority, never an action name,
task word, profession, domain, or executable.

Every downstream effect verifier reads principal/task/environment identity from
the verified action envelope and compares only the remaining persona-authored
choices to `action_arguments`. A wake, population change, artifact declaration,
or presentation projection must not fail merely because authenticated
transport fields are correctly absent from persona-authored bytes.

When no causal delivery remains, the task is **quiescent**. Quiescence is
nonterminal and means only that nothing is currently scheduled. It does not
mean complete, ready, abandoned, converged, failed, or incapable of further
improvement. A later authenticated principal event, resource event, peer
message, external receipt, or persona-authored wake may resume the same task.

Objective acceptance comes only from the exact authenticated authority and
evidence mechanism named by the task. The kernel does not derive it from work
notes, gap-like authored content, population size, artifact count, unchanged bytes,
scores, HTTP success, or model prose.

### C-OP-11 — Mechanical bounds never become semantic selectors

The substrate may refuse an attempted declared effect using canonical parsing
envelopes, signatures, hashes, scope, current membership/consent/access,
preimages, replay/idempotency, leases, exact resource/rate/depth/population
limits, descriptor effects, and current external/physical/safety attestations.
Policy values come from exact signed authority; task or persona prose does not
choose their values.

Admission answers only whether the already-chosen exact effect may occur. It
cannot recommend, rank, pre-hide, or choose a task interpretation, workflow,
population action, model, tool, skill, collaborator, artifact, or next action.
A bound that branches on task words, profession/role, prompt, filename, media,
authored note/knowledge content, or desired output fails this criterion.

Process-local callbacks, capture handles, and transport capabilities are
authority, not evidence. They are stripped before an action observation enters
any canonical communication, memory, learning-history, or turn-effect record;
only exact public inputs, outputs, descriptors, receipts, and effects may be
signed or later shown to a persona.

## 3. Plural domain references

Task, environment, artifact, knowledge, skill, action, and experience records
may carry zero, one, or many exact signed `domain_refs`. The array is an
unranked set of references to independently verified domain records. There is
no host-selected primary domain, inferred profession, or semantic reduction
from domain membership to a role, tool, workflow, completion rule, or action
surface. Empty and cross-domain contexts are valid.

## 4. Current house-task intent

The current authenticated principal intent asks for a high-quality four-bedroom
house design comparable to serious human architectural/civil-engineering work
and improved through collaboration where useful.

The personas—not the substrate—choose the package and means. Human inspection
should be able to find, when the personas judge them appropriate:

- a coherent brief and explicit assumptions;
- dimensioned spatial information;
- editable CAD/BIM or other machine-usable geometry;
- readable drawings or rendered views;
- structural, site, services, safety, and unresolved professional inputs;
- calculations, schedules, or specifications supporting decisions;
- coordination, review, and revision provenance; and
- honest limitations, jurisdiction dependencies, and next professional actions.

This list is task-specific authenticated intent. It is not embedded in runtime
prompts, selectors, regular expressions, birth admission, tool routing,
identity formation, or completion substrate. The exact intent bytes survive
every resume and fan out with the exact resource event to every active member.

## 5. No executable test substrate

The repositories contain no unit, integration, canary, benchmark, or
performance-test suite and no running test process. Operating-path review uses
the signed evidence policy in §1 and actual live tasks; it cannot manufacture a
PASS independent of a useful result.
