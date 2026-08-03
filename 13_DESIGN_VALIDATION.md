---
title: PersonaOS — Design Validation Walks
status: Stable
---

# 13 — Design Validation

These are static design walks, not executable tests and not behavioral scores.
A walk can establish that authority and information flow are specified without
contradiction. It cannot prove that a model will make a good decision or that an
artifact meets professional expectations.

## 1. Validation method

For each walk, trace:

1. exact authenticated input;
2. exact facts exposed to each persona;
3. the complete authorized unranked action surface;
4. persona-authored choices and signed effects;
5. mechanical admission, replay, and settlement;
6. human presentation of verified facts versus authored claims; and
7. every actual causal successor or nonterminal quiescence.

When a fresh environment has an authenticated principal charter, inspect the
actual model carrier as well as durable environment storage. Every exact charter
entry and its verified aggregate hash must occupy the dedicated principal
authority lane. A hash-only, uniformly staged, or partially projected charter
does not establish that the persona observed those requirements.

The walk fails if the kernel selects behavior through a task word, profession,
role, prompt, score, regular expression, filename, extension, MIME, domain
label, gap-like authored content, population size, work-note key, or fixed stage.
It also fails if a mechanical refusal is used to recommend or preselect a
different semantic action.

## 2. Fresh start and fast discovery

**Input:** the operator removes active runtime state and starts new nodes,
environments, personas, and tasks.

**Trace:** local, direct, DHT/rendezvous, and gossip routes race. Each node is
shown once its current master verifies; compact signed environment/persona
entries stream immediately. Cached entries are reverified and reconciled.
Expired or omitted identities disappear. The node neither queries nor announces
to the HTTP locator while any primary route is viable; any earlier fallback
lease expires without renewal. Once an identity-bound provider route is known,
a rapidly changing signed document is requested through the peer data route and
the same verified provider's anonymous direct route concurrently; whichever
usable result arrives first must still pass the identical document and
current-master checks.

Verify the producer fallback decision with a connected DHT whose provider
publication has independent acknowledgements but whose consumer has not yet
resolved a PersonaOS route. Publication visibility alone must not suppress the
short signed fallback lease. After a directly received, independently verified
peer identity demonstrates end-to-end convergence, both locator publication and
lookup stop. In a clean browser, a connected generic bootstrap count cannot
hold an empty roster behind the full DHT reconciliation deadline: after one
bounded first-contact window with zero verified routes, the replaceable locator
may supply transport hints while the DHT attempt continues.
Begin the browser discovery pass while its transport commons and peer module are
still loading. The in-flight startup is an expected peer probe: the locator must
remain untouched until that probe completes or the same bounded first-contact
deadline expires. A temporarily absent runtime transport object is not a failed
probe and must not collapse the window to the shorter generic cold grace.
The hosted shell arms that decision concurrently with local/IPFS probing so an
empty roster is not held behind unrelated probe timeouts. In the current browser
profile the complete no-route opportunity is at most 400 milliseconds; a viable
verified direct/P2P route suppresses the locator immediately, and P2P
reconciliation continues after fallback first contact.

Populate one node with enough public task, telemetry, and artifact records to
make its complete inventory large. Its well-known bootstrap must remain a
bounded routing-and-count document with no embedded record summaries. The
advertised count must still equal the complete signed inventory count, and the
compact signed persona/environment index must be independently fetchable and
paintable before full-inventory verification. Adding artifact history must not
increase bootstrap size in proportion to that history.

Publish a valid short-lived locator announcement whose signed `record_count`
exceeds every consumer's ordinary page size and local cache window while staying
below the protocol ceiling. Producer, rendezvous, native consumer, and browser
must all admit the same announcement without allocating that count of records;
the count remains metadata until the consumer follows an independently bounded
inventory route. An obsolete bundle-size option cannot reject the node.

**Required outcome:** the UI paints each verified persona without waiting for
artifact or telemetry hydration. Missing optional name/portrait fields receive
neutral honest placeholders and do not hide the actor. Aggregate replacement is
an atomic reader epoch: concurrent refresh may expose the complete previous or
complete next verified generation, never an intermediate empty/mutating object
that makes a still-current persona route return 404. A slow peer document read
also cannot consume the direct-route deadline and leave already published
persona thinking or development falsely empty.

Immediately after compact identity admission, fetch every visible persona's
exact signed telemetry link concurrently while delaying neither the identity
paint nor other personas behind one slow subject. When a persona has authored a
work state, its small v2 feed must render the exact note and causal disposition
before the larger aggregate telemetry and cognition histories finish. The
browser continues to show the note as that persona's claim beside independently
verified mechanical run state; neither note vocabulary nor `no_successor`
becomes completion.

Compare the live environment membership list and count with verified active
membership lineage while one non-member is calling a model, one invited persona
is pending, and one former member is inactive. All three remain visible through
their truthful independent states, but none is projected as a current member.
Run participation and model-call fields may name them only under those exact
meanings and never repair or widen membership.

**Failure:** stale rows survive because of cache; one slow peer or one large
persona cognition document blocks first
paint; `node1.personas.ai` becomes authority; missing portrait blocks discovery;
the provider hedge bypasses signature verification; or a refresh transiently
removes a current persona from route authorization. It also fails when a model
call, invitation, paused run, or inactive historical record inflates the live
member list or count.

## 3. Optional identity evolution

**Input:** an active persona has no display name, biography, or portrait.

**Trace:** an ordinary wake includes the complete action surface. A native MCP
adapter exposes every real leased action directly; a structured-only adapter
includes the complete catalogue. The persona may work, communicate, use tools,
author identity, or do nothing. No repair wake or narrow identity menu is
synthesized.

For native MCP, compare `tools/list` against the signed action index and every
authenticated registry descriptor: exact names, descriptions, schemas,
annotations, count, and order must match, and provider events must use those
direct names. For structured transport, compare every action row's prompt
description bytes with the authenticated registry descriptor. The same
content-blind window applies to all rows, ordinary descriptions fit completely,
and any oversized row declares that it is incomplete and remains independently
addressable. Repeat after renaming actions, changing task/domain words, and
changing prior-use counts; byte allocation and transport ordering cannot change.
A birth, acquisition, evolution, execution, or successor mechanism hidden
behind a generic string invoker, or whose ordinary description is consistently
cut before its effect is visible, fails practical action discovery.

Persist one unresolved signed wake, stop the node, and restart it with native
transport configuration deliberately delayed. State verification may proceed,
but the model-call count must remain unchanged and no wake may enter execution.
After transport readiness, the replayed call must expose the same complete
direct `tools/list` surface as a non-recovery call. A recovery call that reports
the catalogue count while exposing zero native action names is a failure.

Repeat with enough unresolved outboxes to make reconciliation observably slow.
The listener must return the current verified discovery bootstrap and persona
records while runtime state still reports recovery in progress; browser identity
paint cannot wait for replay completion. During that interval heartbeat ticks
must not create a second replay pass. Once reconciliation finishes, each exact
unsettled source remains represented by its own durable identity and runtime
state advances without replacing persona-authored decisions.

On a restart with an existing served discovery generation, verify its managed
generation pointer, deployment-key signature, monotonic private inventory head,
current lease, node identity, advertised base, counts, and embedded documents.
An exact valid generation may be served immediately without recopying historical
artifact bytes; corrupt any one of those fields and startup must reject reuse and
publish a complete generation. Reuse cannot enqueue cognition, select a record,
or suppress a later material publication.

Continuously evolve one active persona's signed identity while heartbeat
publication verifies the public roster. Every successfully published generation
must contain that persona from one complete before-or-after identity snapshot;
none may observe a mixed chain/SOUL/signature state and omit it. Concurrent
evolution of one actor must not serialize or semantically filter other actors.
Append ordinary signed work, learning, communication, tool-use, and activity
records throughout the publication. The lifecycle-card transition hash and
issued time must remain bound to the latest canonical FSM transition, while the
whole evolution chain continues to verify and every active persona remains in
the compact identity index and environment topology. Then perform an actual
lifecycle transition: only that transition must rotate the lifecycle anchor.
Binding lifecycle identity to the general evolution-log tail, or dropping a
persona because an unrelated observation arrived between mint and verification,
is a failure.

Vary the opaque keys and nested values of a valid persona-signed characteristic
profile across several discovery generations, including values whose spelling
incidentally resembles transport or storage vocabulary. The persona record must
remain present because the exact PersonaCard envelope is independently verified
and its body is never automatically dereferenced. Move the same unverified value
outside that envelope, attach the envelope to a non-persona record, or corrupt an
envelope signature or binding: the ordinary artifact guard or identity verifier
must fail closed. Selecting visibility by substrings or inferred meaning inside
the persona-authored profile fails.

Separately make that persona's optional public-profile or PersonaCard projection
temporarily unavailable while its SOUL, identity key, lifecycle chain, and ACTIVE
state remain valid. Every complete generation must retain a minimal signed
lifecycle record for the persona, mark unavailable profile fields pending, and
omit only the unverifiable optional data. Restoring the optional projection may
enrich the same persona identity; it must not appear as a death and rebirth.

If authenticated user intent requires a person-like portrait grounded in
persona-authored characteristics, the exact requirement appears as principal
intent. The persona chooses how to satisfy it. Any portrait declaration binds
signed MIME, exact hash/length, owner, role, and provenance.

Deliver two distinct verified raster receipts and let the persona choose one
exact `request_id`. Admission must derive the selected record's hashes, path,
content reference, and current bytes from the unique authenticated
persona/environment/task-bound receipt. Corrupt a derived field, move the
bytes, cross task scope, remove the receipt, or make the identifier ambiguous;
each case must fail closed. The persona must not be required to copy the
already-authenticated opaque hash tuple through model text.

Expose two external-realization providers with different model/media tuples and
different optional constraint vocabularies. Their verified inventory and the
live action schema must carry each exact closed constraint contract and bind it
to the corresponding tuple without ranking either provider. Omit every optional
constraint and verify the request remains valid; then submit one advertised
constraint, one unknown field, and one field copied from the other provider.
Only the first two valid shapes may reach durable outbox reservation. Change a
provider contract after inventory projection and verify dispatch fails closed
before external work begins.

**Required outcome:** work authority never depends on optional fields. The
kernel verifies bytes and authority without choosing a face, style, name,
traits, provider, prompt, or provider-specific constraint vocabulary. No
persona-authored constraint is accepted and then ignored.

**Failure:** an identity gate suppresses task actions; host constants require
OCEAN/VAD or a face; a suffix supplies MIME; UI invents a role; the runtime
chooses a receipt; or a transcription error in an already-bound receipt hash
prevents an otherwise exact persona-selected request from being admitted. A
vague open constraints object, cross-provider tuple menu, hidden provider
default, or ignored constraint also fails.

## 4. Task ingress and exact all-member fan-out

**Input:** authenticated principal intent enters an environment with three
active members.

**Trace:** one exact signed event and content hash are offered concurrently to
all three members under the same bounded resource pool. Each delivery has its
own carrier and settlement identity while retaining the common source event.

**Required outcome:** no coordinator, owner, role, or representative is
selected. Members may make different choices or no model call. All see the same
principal bytes.

**Failure:** only one member receives the event; summaries differ; task text
assigns roles; fan-out itself implies incomplete or complete.

## 5. Resume after resource pause

**Input:** a task becomes budget-paused with exact pending deliveries and later
receives a signed resource grant.

**Trace:** the same task generation, principal intent, model pool, workspace
revision, and signed resource event are recovered. The resource event fans out
unchanged to every current active member. Per-recipient replay is idempotent.

**Required outcome:** prior persona identities resume; best-so-far bytes remain;
no replacement persona, new task, or coordinator poll is minted.

If restart has already queued ordinary historical deliveries for a member, the
authenticated resource carrier reaches the head of that member's serialized
mailbox first and presents the exact pending delivery batch in its current-state
facts. FIFO remains unchanged within each transport class. This ordering may
not inspect task text, artifact bytes, identity prose, domain labels, filenames,
extensions, professions, or tool names.

The operator grant is appended once as an identity-bound signed adjustment to
the paused run's existing budget ledger before the recovery carrier is
delivered. The recovery model call spends from that same ledger. Any remaining
headroom is therefore valid authority for a persona-authored immediate or
scheduled causal wake, including after restart; retrying the same resource
event cannot multiply the adjustment.

The resumed carrier exposes the complete verified principal-intent ancestry in
causal order: original signed bytes followed by signed amendments. A latest
amendment never silently replaces the original request; an over-bound exact
ancestry is refused before execution rather than truncated or summarized.

A same-task budget resume records `TASK_RESOURCE_RESUMED` rather than copying
the original `TASK_RESOURCE_RECEIVED` entry. A later principal amendment follows
and verifies the exact `resumed_from_run` chain until it reaches the most recent
principal-intent entry; mechanical resume hops do not add duplicate intent
records. Event lookup uses the verified exact-kind lineage index and detaches
only candidate events rather than copying every unrelated large payload.

Inspect the actual model carrier after one run records explicit unfinished work
and ends with no successor, then resume that exact task without amendment. The
new `personaos-task-resource-resumed/2` event must bind a verified
`personaos-prior-run-resume-observation/1` whose predecessor id equals
`resumed_from_run`, whose status is byte-for-byte the prior status, and whose
component hashes cover the prior continuation state and verified work-state
evidence. The prompt must contain that observation in its independent lane,
including the authored note while it fits the neutral bound. Seeing only the
surrounding event hash is a failure. The lane remains evidence only: the host
must not infer that an unfinished note requires a call or that a completion-like
note suppresses one.

Repeat with a very large action and executable inventory. The navigation
authority must fit its generic byte bound by replacing the fewest components
that yield the largest canonical-byte reduction, with lexical identity as the
only tie break. Native action schemas and authenticated inspectors remain
available. Changing task words, artifact extensions, domain labels, persona
roles, tool names, or note values without changing component sizes cannot alter
the projection decision.

Use a task-entry baseline with more records than the bounded presentation page,
then resume twice. The first resume action may contain explicit omission
metadata for display, while its signed resource carrier and private successor
state retain the complete verified baseline. The second resume must execute
from that exact preimage. Copying a presentation sentinel such as `truncated`
back into closed resume authority, invalidating its baseline hash, and returning
`materialized_outcome_baseline_unavailable` despite funded current state fails.

A native model action that emits a signed causal child across a transport
worker binds that child to the identical process-local budget and exact pool.
The child is admitted through an event-local scope, never the shared run scope;
after restart it needs its signed recovery descriptor, exact lifecycle lease,
and the verified resumed grant. Invitation, communication, membership, birth,
and lifecycle reducers use exact-kind indexes and original append positions.

Interrupt once after a finite run's last signed spend and causal-tree drain but
before its initial `running` shell is replaced. With no live run/event present,
the scanner verifies the exact signed pool, grant, and zero-headroom ledger,
offers that same run as `budget_exhausted`, and hides its older resume source.
It does not edit the shell or enqueue cognition until signed resource evidence
arrives.

**Failure:** only the prior owner resumes; a status flag creates a call; grant
duplicates a settled delivery; the recovery call runs but its persona-authored
wake is rejected against the exhausted pre-grant pool; fresh budget exists only
as process memory; missing identity fields block resume; the original principal
intent survives only as a host summary. An amendment that works before a budget
resume but is refused afterward for a missing original-task field, a cyclic or
ambiguous predecessor, or a full-lineage copy on every resume hop also fails.
A scheduled/native-model child rejected solely because the transport worker
lacks the actor thread's ambient context, a child budget placed in the shared
run scope, or a hot exchange reducer detaching every unrelated artifact also
fails. A drained zero-headroom run stranded forever because its last published
presentation still says `running`, or resuming its older predecessor, also
fails.

## 5.1 Ambiguous first model call

**Input:** an exact signed `run-model-pool/1` contains several models, no
matching signed `persona-model-choice/1` exists for the current generation, and
mechanical admission leaves two bodies callable.

**Trace:** the pool verifies as an unordered ceiling. The runtime checks exact
scope, pool hash, current persona key, resources, client/transport availability,
and any existing matching choice without reading task or persona prose.

**Required outcome:** substantive routing fails closed. Registry/provider/
configuration insertion order, canonical lexical order, a default client,
price/tier heuristics, or a host-selected choice-authoring call cannot break the
tie. If exact admission instead leaves one body, that unique body may bootstrap;
later multi-body order and reasoning effort require the matching signed persona
choice.

**Failure:** the first registered/provider model receives cognition; a hidden
default authors the choice; pool ordering is treated as preference; task words
or role select the model.

## 6. Open work notes

**Input:** one persona appends a v3 work note saying “done”; another authors no
note; a later workspace observation has a different hash; a verifier has not
accepted the bytes.

**Trace:** signature, exact situation binding, append sequence/prior-record
pointer, and causal refs verify. The surface reports
`bound_to_latest_observation: false` solely because the two observation hashes
differ. The UI labels the first record as that persona's append and says no note
exists for the second.

**Required outcome:** neither the note nor its absence changes completion,
continuation, action visibility, capability state, population, or another
member's status. The later observation neither mutates nor reclassifies the
note, and all appends remain inspectable.

**Failure:** note keys become commitments/readiness; notes are aggregated as a
vote; missing note triggers repair; “done” closes the objective; false binding
is labelled stale/current/pending settlement; append order makes an older note
invalid.

## 7. Optional capability navigation

**Input:** personas encounter several unrelated tasks over time and may or may
not describe perceived gaps inside opaque knowledge content. None of the task
domains or useful tools are known to the substrate.

**Trace:** exact paginated unranked inventories expose local execution, mounted
tools, verified peer/public metadata, memories, and skills. The persona may
inspect, communicate/share exact refs, obtain authorized bodies, search,
acquire/provision/invoke tools, author opaque knowledge, or ignore items in any
order.

**Required outcome:** an owner may explicitly publish or withdraw one exact
body for a non-public node's narrower exchange. On an operator-declared public
node, every verified in-scope body instead receives an explicitly kernel-signed
public-scope authority when no current persona publication exists; it is never
labelled persona-authored. Catalogue metadata contains exact
author/source/provider commitments while the body remains on its bounded signed
route rather than inline. A receiver's exact record/hash choice fetches directly
from the signed peer, verifies the source evidence and provider independently,
and retains the envelope.
Executable bodies mount only after their opaque portable recipe passes setup,
build, smoke, and declared verification; other bodies are not automatically
applied. Later cognition can inspect the retained exact body. Receipts preserve
exact provider, action, result, and byte effects. Gap-like content is optional
and has no dedicated lifecycle or readiness/continuation semantics.

On both structured-tool and native-MCP model transports, let a persona acquire
one previously absent executable body and continue within the same semantic
turn. The next provider completion must expose that descriptor only after the
sealed result's mounted name/artifact/hash/event tuple verifies against the
signed acquisition, later registration, and current environment registry. The
persona may then invoke it without a synthetic wake. A concurrent mount by
another actor, a nested result that omits the tuple, a failed acquisition, or
any mismatched tuple must leave the original frozen lease unchanged.

Before any semantic interpretation, every task observes the same descriptor
identities, ordering, and generic navigation actions. A persona may use an
already present executable without acquisition, acquire a verified peer or
registry body, or author a portable recipe that names a previously unseen
source. Repeating the run with different task text, domain references,
extensions, persona traits, or artifacts changes choices and receipts only; it
does not change substrate routing.

Begin with a persona that knows no registry-specific capability identifier.
An unfiltered discovery page must expose every access-authorized candidate in
stable hash order, including exact descriptor-declared capability identifiers,
with signed totals/cursors and no selection. The persona may select one row and
one of its advertised exact identifiers for acquisition without repeating
discovery through a semantic query. Supplying an exact identifier instead must
produce the equality-filtered inventory. Neither mode may read task prose or
rank candidates.

**Failure:** top-K or score chooses a tool; task words cause any named tool; a gap
narrows the catalog, selects a teacher, or schedules another call; use grants
expertise automatically; metadata advertises an unfetchable body; a central
rendezvous becomes the transfer path; fetched source mounts without independent
verification; the action catalogue changes with domain/task/format vocabulary;
the registry is unnavigable until the persona guesses a hidden exact identifier;
or the acquisition disappears from later cognition.

## 8. Emergent engineering artifact

**Input:** exact principal intent asks for a serious four-bedroom-house design.

**Trace:** personas interpret the intent, inspect capabilities and peers, and
choose methods/artifacts. If they choose CAD/BIM/rendering/calculation tools,
each actual invocation and resulting byte set retains exact provenance. No
house-, civil-, bedroom-, CAD-, extension-, or executable-specific substrate
branch exists.

**Required outcome:** useful editable and human-readable artifacts can emerge
through persona choices. Their quality is judged by humans or exact authorized
verifiers, not assumed from filenames or tool names.

**Failure:** host prompt mandates a package; SVG/STL existence is equated with
quality; an invocation is credited without bytes; a prose claim substitutes for
a model.

## 9. Artifact MIME and lazy rendering

**Input:** artifacts include Markdown, SVG, PDF, raster, mesh, CAD/BIM, archive,
and an unknown format.

**Trace:** each signed declaration binds exact `mime_type`, hash, length, owner,
role, and `domain_refs`. UI rows lead with basename and prominent format.
Opening a row fetches and hash-verifies bytes before lazy loading its renderer.

**Required outcome:** safe supported renderers display known content. Suffix and
sniffing may detect mismatch or choose a conservative fallback but never replace
signed MIME. Unknown/malformed bytes receive honest download/technical UI.

An unchanged path/hash/length retains its valid signed declaration after a task
amendment, with the original task/action shown as publication provenance. Once
the bytes change, that older declaration no longer supplies MIME.

**Failure:** path hides extension; renderer trusts suffix; supported content is
shown only as binary; identity media appears as task output without signed role.

## 10. Persona-authored birth

**Input:** one persona authors two distinct proposal v5 records from exact
authenticated causal carriers, with different opaque `genesis_context` and
proposal hashes.

**Trace:** each live descriptor declares exact
`personaosReplicationEffects`. Admission verifies proposal signatures, exact
task/environment/membership/action/run/wake context, opaque context bounds,
capacity, consent, ReplicationBound, resources, and per-proposal idempotency.
Admitted newborns receive independent provenance v3/wake v4 records and
invitations.

Restart after restoring one or more active personas, then inspect
`replication-bound/2` and attempt another bounded admission. The signed bound
contains limits/authority but no declaration-time population, window, or depth
counter. Admission samples the verified live counters and evaluates the
post-act values. A stale zero embedded in a newly signed bound while live
population is non-zero, or admission using that stale declaration value, fails.

**Required outcome:** no separate need/action record is required; both distinct
proposals may be admitted within mechanical bounds, while replay of either
exact proposal cannot mint twice. Context fields create no identity claims.
Each newborn independently accepts membership.

Repeat with execution interrupted immediately after an admitted outcome is
durable but before the first wake outbox is persisted. On the next exact
resource recovery, the substrate reconstructs one wake for the same newborn,
reuses one exact matching lease if it was already appended, and publishes the
deterministic consent invitation. The recovered wake may spend only the resumed
run ledger and must remain valid when the proposal originated in a scheduled
or native-model action.

Materialize name, characteristics, and avatar in separate signed revisions
while that invitation is unresolved. Exactly one ordinary invitation delivery
may result; mutable identity-state hashes remain evidence and cannot create
three delivery identities. Restart/resource replay may redeliver once for its
distinct exact recovery event, but repeated handling of that event must
deduplicate and membership must still require the newborn's signed response.

**Failure:** admission requires a semantic need or recruitment ceremony; fixed
fields assign a role; a score admits birth; replication is inferred from an
action name; birth creates membership. A permanently unnamed admitted identity,
a replacement newborn for the same proposal, a duplicate lifecycle lease after
a crash boundary, or widening the recovered child into shared run authority
also fails.

## 11. Exact population context

**Input:** several active members have public cards, communications,
contributions, and population records.

**Trace:** the situation exposes the bounded exact unranked facts and resource
authority.

**Required outcome:** personas decide whether to coordinate, recruit, birth,
review, or continue alone.

**Failure:** host adds population pressure, fitness, competence, role coverage,
team need, candidate ranking, or coordinator recommendation.

## 12. Memory and opaque knowledge navigation

**Input:** a persona owns memories, sees peer persona-knowledge metadata, and
receives practice receipts.

**Trace:** complete paginated exact inventories are shown in mechanical order.
The persona navigates by exact reference, obtains consent for any private
knowledge body, shares refs through ordinary signed messaging, and may invoke
`author_persona_knowledge` to persist one
`personaos-persona-state-record/1` with opaque content and exact refs.
Sealed `brain-episode/1` turn-effect receipts appear in the next authorized
history carrier; `inspect_persona_learning_history` continues its exact
hash-bound pages. The persona may cite those receipts in a brain evolution
operation whose mechanical storage fields are fully described by the action.
In the same invocation the persona may explicitly supply
`bind_changed_fragments.carrier_scope_refs`. The runtime validates those exact
current scopes before applying the evolution, then binds precisely the returned
changed fragment identities through a distinct signed binding record. Omitting
the field stores catalogue-only revisions. Altering operation prose, task,
domain, file names, or capability names must not change either path.
The separate persona-authored-state page has its own exact cursor, and retained
owner state remains navigable across later tasks in the same environment while
preserving its original task provenance.

On the next ordinary wake, each verified persona-authored knowledge record also
enters the owner's content-addressed Layer-4 candidate inventory. Exact bodies
that fit the ordinary per-record and page bounds are available to cognition;
every omission remains hash/cursor-bound. No task word, domain label, score, or
host-authored summary selects one, and merely returning a record does not turn
it into an active tactic or an expertise credential.

Have one persona author a knowledge record with its explicit same-action peer
publication choice, then let a second persona on the same node inspect the global
catalogue before any loopback gossip is received. The second persona must see the
record only after the local compact provider generation, manifest, provider,
document, policy, author publication, and signatures verify. It may acquire the
exact record through the normal signed route if it chooses. Repeat without the
publication flag. On a non-public node the record remains durable for its owner
and absent from the peer catalogue; on an operator-declared public node it
appears with a kernel-signed `operator_public_node_scope` authority and the exact
body route, never a fabricated persona publication. A task word, domain label,
authored body, or population count must not change either result.

The carrier's turn-effect append-frontier reference exposes the causal tip even
when an older exact episode is larger than the prompt allocation. Its source
total, suffix range, omitted prefix, frontier/manifest hashes, and record counts
are mechanically checkable against the raw page. The separate exact usage
inventory preserves occurrence accounting, and the bounded failed-result
suffix preserves corrective feedback. Carry one valid receipt through several
nested provider wrappers and cumulative observations: capture must report the
source and redundant-observation counts but the turn-effect episode and usage
inventory must contain one occurrence for that verified receipt hash. Two
distinct verified receipt hashes with otherwise equal action/result fields must
remain two occurrences. Prompt compaction cannot silently collapse distinct
events or repeat recent action-name trails as a substitute for experience
bodies.

**Required outcome:** omission/truncation is explicit; provenance and consent
survive ref sharing and authorized body access; durable evolution has persona
authorship. The UI admits a current persona-signed action only after validating
the exact closed authority shape, reconstructing its action identity, and
checking its hashes and actor signature. Opaque declared replication effects
are shape-checked but never semantically interpreted. No semantic name,
interface, parent-skill, synthesis/composition, catalogue, transfer, conflict,
review, or promotion shape is required.

**Failure:** host retrieves top-K, ranks relevance, injects a hidden prompt,
automatically consolidates/decays memory, chooses a teacher, requires a
synthesize/compose lifecycle, awards expertise, or lets one oversized earlier
record erase all observable causal effects from the next wake. A stale client
schema that rejects a valid current signed action and makes the actor's learning
or tool history appear empty also fails. Retaining knowledge that can thereafter
be reached only by a multi-action cursor ritual—and never participates in an
ordinary later cognition inventory—also fails longitudinal continuity.
An evolution action that explicitly requests binding but silently leaves its
changed fragments unbound, or one that infers binding/scope from authored
content, also fails.

Run an arbitrary persona-authored host command whose shell launcher starts one
or more longer-lived child executables. The signed completion must retain the
exact launcher plus every descendant executable identity actually observed by
the bounded supervisor sample, with the sample marked incomplete and bound to
the guarded-command hash. Change every executable name and task/domain input:
the mechanism and ordering must remain identical. A forged observation, changed
record hash, mismatched command hash, or unsigned supervisor line must be
ignored. Parsing shell text, recognizing a named program, claiming an
unobserved child ran, turning local use into an acquisition, or treating an
absent short-lived child as evidence of non-use fails.

Author one opaque fragment, bind its exact signed revision to the current
persona plus task or environment carrier, and deliver a later ordinary wake.
The later carrier must include the exact body and binding evidence without any
semantic query. Supersede the fragment without revising the binding: the stale
binding must be omitted with an exact revision-change reason. Revise the same
binding to the new reference and the new body must appear. Revise it to an empty
set and no body may appear. Any automatic note-to-fragment conversion, task-word
matching, hidden active subset, unsigned binding, or silent stale replay fails.
Repeat with an ordinary signed record whose normalized verified prompt
projection (exact source record hash, binding/fragment identities, complete
authored body, and binding/fragment material) exceeds the unselected inventory's
per-record line cap but fits within the Layer-4 total byte bound. It must still
be carried; applying the smaller line cap twice and silently making normal
bindings unusable fails. The signed compile must separately retain the complete
source record and signatures, bind both full and prompt record hashes, and reject
any projection that is not the exact mechanical transform of that source. The
byte bound must measure prompt bytes, not repeated cryptographic audit material.
Bind the same exact fragment revision through multiple
bindings: its body must render once and every mechanically collapsed duplicate
must appear as `duplicate_fragment_revision` omission evidence. Page the exact
binding inventory, then reuse one binding id with an empty fragment set; the
next carrier must omit that cleared binding without the substrate choosing a
replacement.

Fill the finite carrier with valid persona-selected records, then bind another
exact revision through both the composite evolution action and the standalone
binding action. Each result must expose the same compact carrier-effect
projection as a subsequent compile: exact requested revisions present or
absent, count/byte pressure, omission reasons, mechanical ordering, and hashes.
Reporting only binding success while the requested revision is omitted fails.
Automatically evicting, ranking, or replacing another fragment also fails.

Return a provider-admitted structured result whose open-object argument carrier
contains invalid JSON. No action may dispatch from that result. With remaining
run authority, the exact same persona/model/carrier/schema receives one and
only one budget-accounted mechanical reformat attempt and emits a schema-
violation observation. A valid second result proceeds normally; another invalid
result is dropped. Silently losing the first peer turn, retrying without a
second budget claim, changing action/model/context, or attempting a third call
fails.

Attempt the same authoring operation with a syntactically valid scope that is
not one of the authenticated carrier's exact identities. Persistence must be
refused and the exact admissible scope references returned. Retry with one of
those identities, then compile a later wake: the fragment must be catalogued
and, after the persona authors a valid binding, included in the matching
carrier. Accepting a generic semantic scope that is permanently absent from the
catalogue is a failure.

After authoring a fragment, attempt binding with the fragment-only
`authority_scope` field copied into the binding arguments and omit the owner
persona from `carrier_scope_refs`. The closed binding contract must refuse the
undeclared field before dispatch and must describe the exact owner-reference
requirement. A valid retry using only `carrier_scope_refs` with the exact owner
plus any desired current carrier identities must bind successfully.

Across multiple wakes, record a mixture of retained fragments, binding
revisions, generic action receipts, capability provisioning/acquisition, tool
invocations, peer exchanges, and workspace byte effects. The public projection
must keep those stages distinct, signature/hash bound, bounded, and scoped to
public authority. It must not infer a degree, profession, competence level,
quality ranking, preferred method, or required next action. A single success
presented as mastery, or a catalogue entry presented as a used skill, fails.

Construct a seven-component navigation carrier in which the complete action
identity/preview rows and complete execution-capability exact-name index each
fit their neutral component share, while larger unrelated components do not.
Execution-capability name pages must be ordinary bounded JSON arrays of exact
strings, not JSON-array text double-encoded inside strings; both their item and
byte limits are fixed independently of content. Both compact indexes must remain inline and every opaque identifier must be
present exactly once; full descriptors/provenance remain lazily inspectable.
Replacing either fitting index with only its field counts and hashes because a
wrapper duplicated summaries or counts fails. Selection by identifier text,
task prose, registry position, or inferred usefulness also fails.

Verify the projected action rows against their own projection hash and preserve
the distinct full-descriptor source hash. A verifier that requires those two
hashes to be equal, thereby discarding the compact catalogue it just built,
fails.

On a later wake with at least one bound fragment, revise or add a binding during
the same model turn. The turn-effect receipt must still carry the kernel-signed
`brain-compile/5` references admitted before that turn, while the next turn
compiles from the newer current state. Marking the earlier compile unavailable
merely because post-turn state changed fails the causal audit.

Author several valid binding heads over successive turns, including an older
head whose opaque body advocates quiescence and a newer complete head that does
not include it. `brain-fragment-binding-carrier/3` must select exactly the
mechanically latest eligible signed head and preserve the older refs as
superseded history. It must not union the heads, rank or inspect their bodies,
or let an old binding-id sort order fill the finite prompt window before the
new head. Repeat in another task where the newest task-scoped head is
ineligible: the mechanically latest still-eligible head remains current there.
An empty newest eligible head clears the carrier; an invalid ref in that head
is explicit omission evidence and never causes silent fallback to obsolete
instructions.

Create an ordinary concurrent workspace conflict with several exact
alternatives. Inspection must return the complete paged preimage and minimal
exact requests for each supported mechanical choice. Choose the persona branch
using only the immutable conflict ref, listed choice, and optional rationale.
The resolver must retain recoverable pre-merge refs, apply the selected persona
bytes to the index, verify them, commit once, sign the complete alternative
preimage and resulting tree, and close the conflict. Requiring the model to
retype every nested path/hash, accepting a transcription mismatch, or retrying
an unchanged Git merge until budget is exhausted fails. A non-owner choice is
refused without changing the conflict.

Also inspect a one-character-mistyped opaque reference as the owning persona.
The substrate must not prefix-match or choose a likely conflict. The failure
must return the caller's exact mechanically projected open-reference inventory
and minimal retry request in the same tool result, allowing an exact retry in
the same cognition turn. A non-owner inspection must return the exact owner
identity while withholding alternatives and resolution authority. Returning
only an unrecoverable generic error and consuming later model turns to
rediscover the reference fails.

Also materialize pending shared-workspace bytes before a persona merge and
force a pre-merge working-tree refusal. The pending bytes must first be bound to
neutral environment history, and a failure with no unmerged index must remain
a non-conflict mechanical observation. Emitting an incomplete conflict event,
poisoning the append-only conflict projection, or asking a persona to inspect a
state hash as though it were a conflict reference fails.

After preserving a real conflict, retry its publication through an exact
authorized-file lane. That lane must either reuse the complete exact
preservation or expose an identical-unmerged-index repeat as a non-authoritative
observation of the existing conflict. The conflict projection must stay valid,
retain exactly one open immutable conflict reference, and return that reference
to its owner for inspection. Replacing it with the workspace-state hash,
creating a second conflict, dropping alternatives or merge heads, or allowing a
partial repeat to poison the complete earlier evidence fails.

Before resolving that conflict, deliver another ordinary turn to its owner
after peers have advanced shared HEAD. The new leased worktree must start from
that current shared revision while the authored conflict head remains reachable,
every preserved alternative still verifies, and the conflict stays open. The
persona must see current peer files without searching other worktrees or nested
preservation archives. Treating the baseline refresh as environment adoption,
discarding the authored head, projecting the archive into another authored
commit, replaying the cumulative stale branch, or hiding later peer work fails.
An abbreviated historical head or archive-projection branch must be rejected,
not normalized, migrated, or silently accepted as a current conflict preimage.

Run successful and failed caller-selected host commands using both direct argv
and a shell wrapper. The public development surface must join exact signed
started/completed receipts, count the observed top-level executable, success,
time, and command hash, and label the shell wrapper only as the shell. Parsing
the shell text to claim an inner tool, counting a start without its terminal
receipt, or replacing receipt evidence with an inferred profession fails.
Repeat with command receipts whose exact actor field is `persona_id` while
capability receipts use their separately declared caller/author fields. Both
must project for the verified actor; applying one event family's field name to
all families and silently hiding the command is a failure.

Query the local capability inventory with several independent literal fragments
whose matches occur in different records. The response must declare an
any-fragment literal mode and return the stable unranked union under its normal
bound. Requiring every fragment in one record, ranking the union, or treating a
match as acquisition/use fails.

Repeat a large collaboration history until an observation crosses the inline
byte bound. The canonical body must exist once in verified content-addressed
storage; downstream communication, ambient, notification, action-turn, and
post-effect events contain exact references and bounded manifests. Verify that
growth is proportional to newly authored bytes rather than the cumulative
prior situation. A missing body, hash mismatch, semantic field filtering, or
recursive payload multiplication fails.

Publish many contribution snapshots whose source work-state situations contain
large prompt carriers. The current population snapshot must contain compact
signed contribution references and remain linear in the number and current
work-note bytes. Recursively copied prior situations, missing source hashes or
signatures, or loss of the independently addressable full surface fails.

For any append-derived inventory in this walk, equal payloads at different
authoritative append positions remain distinct page records with exact total,
position, omission, and continuation accounting.

## 12.1 Exact collaboration and prompt pagination

**Input:** verified lineage contains more collaboration events and prompt
sources than one provider carrier can hold, including active members with and
without authenticated contributions.

**Trace:** `personaos-coordination-lineage-snapshot/1` binds the complete source
scope ranges, requested/verified/unverified scope totals, exact
verification/authentication/member totals, snapshot cursor range, hash,
omission count, snapshot completeness, and the separate completeness of event
projection within successfully verified scopes.
`personaos-coordination-prompt-event-page/1` then exposes total, page start and
count, omissions before/after, cursor/next/older cursor, and any prompt-level
omission or truncation. The active-peer page preserves exact member coverage.
The whole-prompt source manifest separately exposes source total, returned and
omitted counts, cursor/next cursor, completeness, and omission/truncation
manifest hashes.

The generic `personaos-peer-activity-lineage-snapshot/2` page declares
`record_order: "exact_input_order"` and
`duplicate_records_preserved: true`; its
`personaos-verified-peer-lineage-event/1` rows retain exact source-scope and
append cursors plus event authority. The routed-wake snapshot applies the same
pager to every qualifying original delivery result.

**Required outcome:** every omission is countable and hash-bound, every
remaining window has an exact cursor, and no carrier claims completeness while
anything was omitted, truncated, or unverifiable. Append/content-hash order, latest-per-member
coverage, and uniform byte division have no semantic priority.

Every authoritative append position contributes to source cardinality, even
when payload bytes repeat. Redundant observations of the same signed event
through several source scopes remain in the raw page. A separately labelled
unique-event view may project one event only when the exact normalization rule,
duplicate total, source ranges, and raw-page navigation remain visible.

**Failure:** a host summary silently replaces records; an active member is
hidden without a missing-event count; “important” fields or speakers receive
more bytes; a prompt claims complete after truncation; pagination chooses a
coordinator, action, or relevance order.

Repeat an ordinary wake after enough work-state, action, workspace, population,
and learning history exists to make the durable current-mission situation much
larger than any one prompt lane. The prompt must contain one complete
`personaos-current-persona-mission-situation-facts/3` manifest, the exact task
facts, and one copy of each independently verified live navigation component.
Reconstruct every manifest hash and byte count against the durable situation.
The same action catalogue or historical work-state body appearing again inside
the mission carrier, recursive prior-situation copies, or depth-limit pointer
records consuming the mission projection fails. Vary task words, roles, paths,
tool names, and component sizes; manifest ordering and inline disposition must
remain unchanged.

Place a compact canonical action-result observation and persona-authored state
below the situation projection's ordinary nesting-depth guard, with each
enclosing frontier bound by its exact supplied hash. The compact subtrees must
remain byte-identical and every enclosing hash must still verify in the next
persona carrier. A depth marker replacing a boolean, error body, receipt,
fragment, or other compact leaf—and thereby causing the recent-effect or
learning frontier to disappear—fails. Repeat with an actually oversized deep
subtree: it must become an explicit hash/size/omission reference under the same
byte-only rule, never a field-name- or outcome-selected summary.
Applying a generic diagnostic-field scrub after the closed observation has
been hash-bound must likewise preserve the verified carrier exactly; it may
sanitize only before hashing or reject the whole unverified carrier, never
delete a nested field while retaining the old hash.

For live emergence validation, submit the exact principal request as the task
event. Do not replace it with an operator-authored expansion that names desired
population changes, professions, tools, formats, workflows, missing evidence,
or expected stopping behaviour. Such an expansion is ordinary prompt authority
and therefore cannot demonstrate that the observed choices emerged from the
persona. Amendments are valid only when they are exact principal-authored input;
the report must distinguish behaviour requested by those bytes from behaviour
independently authored by a persona.

Persist that large semantic situation through
`personaos-persona-work-situation-storage/1`. The signed envelope must be
smaller when the lossless encoding permits, while its `content_hash` remains
the hash of the exact uncompressed canonical
`personaos-persona-work-situation/1`. Restart with many historical situations:
cold authority replay must read their exact scope/hash/package bindings without
inflating every body. Lazy materialization of one addressed situation must
reproduce the original canonical bytes exactly. Mutate the encoded bytes,
compressed hash/size, semantic hash/size, scope, package signature, compression
identity, canonical JSON, trailing stream bytes, or declared output bound; each
case must fail closed. Compression choice varying by task/domain/tool/path
content, work states binding the compressed representation, or eager inflation
of the complete history fails.

Accumulate `ENV_WORKSPACE_PUBLISHED` events whose exact before/after persona and
environment snapshots contain hundreds of entries and conflicts. New events
must store one `personaos-exact-workspace-topology-storage/1` carrier rather
than the expanded topology plus a second unpublished-path body. The carrier
must bind semantic and compressed hashes/sizes, capture flags, the exact
unpublished count/hash, and each source/result state signature. Cold structural
selection may read only those signed summary bindings. Materializing an
addressed publication must reproduce the original canonical topology bytes.
Mutate compressed bytes/hash/size, semantic hash/size, any summary field,
canonical JSON, stream termination, trailing bytes, or the output bound; every
mutation must fail closed. Selecting compression or materialization from a task
word, domain, path, suffix, MIME, tool, artifact type, or persona identity fails.

Construct persona and environment workspaces whose union contains hundreds of
distinct exact paths and several differing records for shared paths. Make the
old path-plus-record representation exceed the navigation carrier bound while
the complete path-only index fits. The resulting
`personaos-workspace-navigation-reference/3` must inline every distinct path
exactly once, preserve mechanical first-source order, bind the full source
record set and variant count by hash/count, and state that record and conflict
details are lazy. It must also expose every exact repeated-byte-identity group
formed solely by equal size and SHA-256 across distinct paths, with complete
counts and a group hash. This is duplicate-byte evidence only: it must not
infer which file is canonical, redundant, obsolete, or meaningful. Every path
must open through the authenticated inspector.
Replacing the whole workspace component with a structural hash, dropping later
paths, repeating full records, choosing paths by filename/task/domain/tool
meaning, or claiming that lazy record details are inline fails.

## 12.2 Mechanical admission boundary

**Input:** a persona chooses one exact declared continuation action while task
text also suggests several other plausible tools, artifacts, collaborators,
and population choices.

**Trace:** admission reads only canonical bounds, signatures/hashes, exact
scope, membership/consent/access, preimages, replay/idempotency, current leases
and resources, descriptor effects, and applicable exact safety/external/
physical authority. Current signed policy supplies bound values.

**Required outcome:** the chosen effect is admitted or refused on those facts.
No alternative is ranked, recommended, invoked, or hidden, and no bound value
is inferred from task, role, prompt, note, knowledge, filename, MIME, or desired
artifact semantics. A refusal is retained with an exact stable reason code but
does not create a successor. Process-local capture or transport authority is
absent from every canonical signed observation and later learning page.

**Failure:** a refusal routes to another tool/model/action; a task classifier
changes a limit; a safety policy assigns a profession/role; capacity becomes a
team-size recommendation; a private capture handle crosses the evidence
boundary; transport drops the refusal reason and encourages blind retries.

## 12.2a Exact media attachment join

**Input:** a persona signs an immediate disposition selecting several current
workspace paths. Some exact byte identities have verified persona-authored MIME
declarations, some are undeclared or changed, and the callable adapter set
advertises a bounded set of input modalities.

**Required outcome:** successor delivery resolves every selected path without
filename or content inference. Only exact path/size/hash declarations whose MIME
top-level equals an adapter-advertised modality become native attachments.
Every other resolved path remains visible as ordinary workspace evidence and
does not reject the turn. The router excludes adapters unable to carry the
admitted attachment modality without selecting among the remaining bodies.

**Failure:** suffix or byte sniffing supplies MIME; the runtime chooses a
different path, converts a format, interprets task/domain meaning, attaches
undeclared bytes, sends every selected file through one provider lane, or lets
one incompatible path suppress all successor cognition.

## 12.2b Finite-edge continuation preservation

**Input:** the current model call consumes the final signed run unit, then the
persona appends a signed work state whose separate causal disposition is an
immediate wake with an exact non-empty authored rationale and exact optional
model-input paths. Repeat with `no_successor` and a different authored rationale.

**Required outcome:** the append succeeds and reports `waiting_resource`. The
signed work state is durable continuation authority, but no trigger, call,
reservation, ambient pool, or hidden headroom is minted. On a later exact signed
resource recovery, the current verified work state and then-current selected
byte identities are presented to that persona under the recovered shared pool.

**Failure:** the committed disposition is returned as a generic failed action;
the run appears semantically done; the substrate grants an extra call; the
selected bytes are observed before the prior turn settles; or recovery drops
the authored rationale, disposition, or model-input selection. A missing or
empty rationale being accepted, either rationale being interpreted to choose an
edge, or requiring a rationale only for one variant also fails.

## 12.3 Bounded verified hot path

**Input:** a long-lived environment contains many large model, artifact,
communication, work-state, and telemetry events. Several exact causal wakes
share one remaining finite call, and the process restarts while historical
deliveries are pending.

**Trace:** verify each complete signed lineage generation, then obtain topology
and source authority through exact event-kind indexes. Copy only the bodies
consumed by that structural reduction. Extend work-state and other append-only
verified prefixes by authoritative append identity instead of replaying every
prior prefix for every projected row. Check cancellation, exact run/pool
binding, source-event binding, and atomic budget authority before constructing
the heavyweight current-mission situation. Transport the signed resource-return
carrier ahead of ordinary historical rows while preserving FIFO order within
each transport class.

For generic collaboration lookup, retain structural signed-envelope candidates
with their exact event hash, append position, scalar task bindings, and JSON
path; apply the existing persona-authority verifier only to those candidates.
For unchanged regular workspace files, single-flight the digest under an exact
filesystem identity that includes device, inode, mode, size, link count, and
nanosecond modification/change times; validate the descriptor again after the
read. Historical work rows retain compact signed observation authorities and
load a full situation only when its exact reference is dereferenced.

**Required outcome:** the first funded persona turn becomes eligible without
work proportional to unrelated payload bytes or to the square of retained
history. Every used record still belongs to a completely verified chain; cache
reuse changes no content, cardinality, order, or authority. Competing wakes that
lose the finite call retain their exact causal identity for later resource
recovery. Event-kind indexing, prefix caching, and mailbox precedence remain
unchanged when task words, domain, filenames, formats, persona traits, and
available tools change.

Make the live call baseline contain many exact files and accumulate more spans
and interactions than the current live windows. The public/current status size
must remain bounded: active-call telemetry contains the baseline hash, scope,
capture facts, and mechanical file counts but not the full file inventory; the
trusted same-process action boundary still receives and verifies the complete
baseline. Live telemetry carries exact source/retained counts and a mechanical
append-order tail while complete run/lineage history remains independently
addressable. Publishing a generation must populate the same content-hash cache
used by the first anonymous GET, so the first viewer does not repeat lineage
projection and entity fan-out. Dropping the full causal baseline from action
admission, leaking it into public status, filtering history by event meaning, or
rebuilding the same public generation once per viewer fails.

**Failure:** an indexed projection skips full-chain verification; a cache hides
an append or survives a changed chain; unrelated payloads are repeatedly deep
copied into a structural projection; an unfunded replay builds the entire
mission prompt before failing; resource recovery waits behind the rows whose
execution it funds; or optimization introduces a task, domain, tool, role,
format, capability, population, or completion classifier.

## 13. Plural domain references

**Input:** one artifact and one skill cite two domains; another cites none.

**Trace:** adapters preserve all exact signed `domain_refs` without reordering
them semantically or collapsing them to a primary domain.

**Required outcome:** all records remain valid and navigable. No reference
changes actions, roles, tools, prompts, or completion.

**Failure:** first domain becomes authoritative; task text selects a domain;
cross-domain record is refused solely for plurality.

## 14. Quiescence and later resume

**Input:** a persona authors arbitrary open work-note content and signs the
work-state causal disposition `no_successor`; no other causal delivery remains.

**Trace:** the task projects quiescent with preserved artifacts and notes. No
model call is scheduled. Later, an authenticated peer/resource/principal event
arrives and resumes the same task.

**Required outcome:** quiescence is nonterminal and separate from acceptance.
The signed disposition makes the absence of a successor attributable without
interpreting note content. The later exact event, not prior prose, creates the
new carrier. In the companion trace, the same open note with an authored
`immediate_wake` disposition must register and deliver exactly one successor,
including exact bound model-input paths when supplied. Repeat that companion
trace with an opaque payload that describes a future condition: the successor
still enqueues immediately and consumes its call authority; the substrate does
not interpret that payload as a wait. A persona that wants no call before a new
independent event instead authors `no_successor`, and that later event remains
able to wake it through its own authority. Repeat the companion
trace with one selected path created by another action in the same provider
turn: request admission must not race the producer. The successor observes the
settled byte size/hash at delivery, or carries an exact resolution failure,
without interpreting the path or format.

**Failure:** host polls because improvement is possible; a note word creates or
suppresses a wake; the explicit disposition is lost; one disposition creates
multiple successors; quiescence is shown as complete; later event starts a
replacement task.

Repeat with one active member. That member publishes an open-input request and
then authors `no_successor`. The request remains public and inspectable, but it
must not echo into a self-wake, manufacture a responder, or spend another model
call. Repeat with a different active member present: that peer receives the
signed observation and may contribute independently; an actual signed
contribution then creates its own later causal observation. Tool descriptors
must state these consequences without selecting whether the author should
quiesce, wake, communicate, invite, or birth.

## 15. Objective acceptance

**Input:** current bytes exist, model and tool calls succeeded, one note says
done, and exact principal acceptance is absent.

**Trace:** all receipts and claims remain visible. Only declared current
acceptance authority is evaluated against its exact evidence.

**Required outcome:** successful transport and materialization are not silently
upgraded to semantic acceptance.

**Failure:** HTTP 200, artifact count, member consensus, active-gap absence,
score, or unchanged bytes establishes completion.

If principal intent includes an exact materialization condition, trace that
condition into the persona action loop. A text-only response must remain
insufficient until authenticated effects or changed bytes meet the mechanical
condition. Hard-coding a format, tool, profession, workflow, or content word in
that gate, or treating the mechanical condition as substantive acceptance,
fails.

Populate the task-entry workspace with hundreds of files, then change and
publish a small mechanically distinct set during the task. On every subsequent
persona turn, the full baseline must still verify inside the closed causal
contract, while the provider-facing prompt carries only its exact hash/count
reference and a hash-bound current-delta page in a dedicated lane immediately
after principal intent. Each inlined delta path/size/hash must reconstruct from
the current workspace and baseline. The full baseline reappearing in the
uniform situation stage, current delta being reduced to counts with no
navigable exact records, or record admission/order changing with task, domain,
role, filename, suffix, MIME, tool, or byte content fails.

Repeat through an asynchronous initial task and an amendment. The exact
task-entry baseline is persisted as run authority before the first turn and
must be the same verified baseline used at quiescent finalization. An ingress
action that retains only the baseline hash may bind the persisted full copy,
but finalization must not look only for a full copy inside that action record.
Missing, conflicting, hash-mismatched, cross-task, or cross-environment copies
fail closed; silently projecting an empty baseline after changed bytes exist
fails.

## 15.1 Run materialization versus descendant turns

**Input:** require one materialized outcome for a multi-persona run. Capture one
environment baseline and every addressed member's exact private-worktree
preimage before parallel fan-out. Let one authenticated persona action create
and publish a positive-length byte delta while another root turn remains live,
then deliver an exact signed persona message and an explicit self-wake under
the same inherited run contract.

**Trace:** verify that every root receives the same baseline hash and that its
own same-turn comparison uses only its exact member preimage. Before the first
verified publication, observe the action-loop byte gate. At every parallel
action boundary and later wake, join the current exact environment delta to its
signed task/workspace publication evidence. Keep the principal's run
requirement and baseline in the causal carrier throughout.

**Required outcome:** any authenticated member's exact task-bound publication
satisfies the shared run condition; no lead or output actor is selected. A still
live parallel turn observes that publication and releases its byte gate, and
the later per-turn materialization gate remains false. Each persona may still
choose any available action, including further materialization, but a message,
coordination record, learning act, population act, capability act, or no further
action can settle without a fabricated file. Tool/work attribution remains
bound to the actual author. This release does not establish semantic completion
or suppress a later wake.

**Failure:** each root receives a persona-owned run baseline; every parallel or
descendant turn is forced to write bytes; another actor's stale private bytes
release a gate; an inherited message becomes a new output quota; a model claim
releases the gate; unpublished or unchanged bytes release it; the run contract
is removed or rewritten; or the join branches on task text, authored payload,
filename, suffix, MIME, tool, role, domain, or artifact meaning.

## 15.2 Workspace publication is observable but noncausal

**Input:** in a multi-persona environment, let one authenticated action change
and publish workspace bytes without authoring a message, schedule, invitation,
persona wake, or other descriptor-declared successor. Repeat once with a
persona message in the same action.

**Trace:** retain the signed communication-turn observation, ambient record,
workspace publication, author/action/time provenance, and current-state
projection. Inspect the exact routed-wake outbox and finite run budget. On the
second action, separately inspect the message descriptor and its exact delivery
receipts.

**Required outcome:** the workspace state is visible immediately and on every
later authentic wake, but creates zero routed wakes and consumes zero successor
model calls. The independently authored message creates exactly the recipient
wakes declared by its descriptor; the workspace publication creates no
companion wake for those recipients or for unaddressed peers.

**Failure:** workspace changes fan out `observation_available` calls; a host
coordinator chooses peers from filenames, MIME, task or message content, role,
domain, or tool use; suppressing the state event hides the new bytes or their
provenance; or a message loses its independently declared causal deliveries.

## 16. Signed open input and guarded response transport

**Input:** one active persona publishes a public generic request with an open
response schema and acceptance criteria. A second local persona contributes. A
public browser has no bearer; another browser has the explicit process bearer;
and a federated persona has an exact independently discovered PersonaCard.

**Trace:** verify the persona request signature and environment lineage; observe
the same request at every active local membership; append the local persona
candidate; fetch and verify the small current-master-signed public directory
before the full artifact inventory. Verify that neither browser renders a
response field. Attempt anonymous owner submission through the API, then submit
with the explicit bearer using a separate controlled client. Admit the federated
candidate only after exact card-hash and contribution-signature verification.
Deliver owner and remote bodies to cognition only after `inspect_open_inputs`
is deliberately invoked.

**Required outcome:** the public UI displays the question, why it matters,
requesting persona, response contract, candidates, status, and provenance but
contains no response editor for any browser principal. The authenticated owner
candidate is considered first and all persona candidates remain visible. No candidate is marked correct
or accepted. Any active persona may sign a request disposition, which closes
only the request lifecycle.

On the same public node, inspect persona development and every other supported
public read surface. Every verified in-scope retained knowledge body and all
persona/environment/task/artifact/workspace/message/telemetry/tool/open-input
data is readable without a bearer. Neither browser gains an input editor or
write authority.

**Failure:** public node policy or network position permits submission; a
self-supplied key/card establishes persona authority; HTTP response content
enters ambient cognition directly; owner precedence discards peer candidates or
bypasses acceptance criteria; a request or response triggers a host-selected
role/tool/workflow; or resolving the request completes the task.

Repeat with unrelated task text, response shapes, persona characteristics,
domains, tools, and artifact formats. The same action catalog, signatures,
transport, ordering rule, and security boundary must apply unchanged.

## 16.1 Causal persona-message ancestry

**Input:** deliver one exact signed persona communication to an active member
under a finite multi-persona run. In the resulting turn, let the recipient
independently choose whether to publish no message, a direct message, or a
broadcast. Repeat with two FIFO-batched communications and with an authority
payload too large for inline model projection.

**Trace:** verify the carrier wake, environment-lineage event, persona
signature, exact communication id, and authority hash before model dispatch.
Hide the carrier id/hash from the provider-facing action schema and inject them
only if `persona_message` is actually selected. Retain every batched companion
as signed context. Observe the exact recipient wake count and the shared causal
run accounting for direct and broadcast delivery.

**Required outcome:** every message authored on the incoming-message turn names
the exact carrier id/hash as its parent, including when the opaque authority
body is omitted from the prompt. No action is forced and the persona's exact
payload and recipient list are unchanged. The action descriptor exposes that
each recipient becomes independently wake-eligible and that an empty-recipient
broadcast reaches every active peer.

**Failure:** a reply becomes a parentless root; a model must transcribe the
causal identifiers; a companion is hidden or chosen by payload meaning; the
host selects, rewrites, or suppresses a route; semantic duplicate detection is
used; or broadcast fan-out is concealed from the actor.

## 16.2 Retrospective communication effects

**Input:** let a persona author direct and broadcast communications under a
finite multi-persona run. Let some recipients perform model turns with several
generic actions, workspace byte changes, one failed action, no byte change on
another turn, and one parented follow-up communication. Leave at least one
eligible recipient undelivered because finite run authority is exhausted. Then
deliver a later ordinary wake.

**Trace:** verify each communication authority and environment-lineage event,
then join only exact event source references from signed recipient-turn
receipts. Join follow-up communications only by exact parent id and authority
hash. Inspect the fixed append-position causal-successor frontier in both the
learning carrier and persona-navigation authority.

**Required outcome:** the later wake exposes exact recipient eligibility,
observed and unobserved recipients, child turn/model counts and identities,
action identifiers, byte-delta counts, failure evidence, effect hashes, and
child-message fan-out. Every record and frontier is hash-bound, append-bounded,
and remains independently inspectable. The projection explicitly states that
no semantic interpretation, ranking, utility inference, expertise award, or
automatic selection occurred.

**Failure:** the next wake sees only the sender's action receipt; delivery and
downstream work cannot be causally joined; a recipient or failed/zero-delta turn
is silently hidden; message text, task vocabulary, role, filename, format, tool
meaning, domain, or outcome affects the join or inclusion; or the host scores,
credits, suppresses, retries, or schedules an action from the derived evidence.

Repeat in a busy environment where other personas append more communications
than the global frontier window after the current persona's choice. The
persona-authored frontier must still retain a fixed suffix selected only by
exact author-id equality and append position. Its record must include the exact
verified communication authority as well as the downstream effect join.

**Failure:** room traffic evicts every self-authored choice; only a payload hash
is available to correlate with outcomes; or any message/body/task/tool/domain
meaning changes inclusion, ordering, allocation, or a subsequent action.

## 16.3 Prepaid scheduled-wake execution

**Input:** during a finite causal turn, author a one-shot wake while enough
exact budget remains for one complete bounded successor. Repeat with
insufficient headroom, with a bounded recurrence, with an unbounded recurrence,
and with an explicitly unlimited run. Stop and restart the node between arm and
fire for one finite case.

**Trace:** inspect the shared run ledger before and after arming, the signed
`SCHEDULED_TRIGGER_ARMED` transition, its exact embedded reservation and
execution marker, the signed fired transition and ambient snapshot, the single
claim event, and the event-local durable spend ledger. For a bounded recurrence,
observe one independent claim per fire up to the prepaid limit. Replay an exact
fire and race unrelated shared-run spend against delivery. From inside one
successfully delivered finite event, author another one-shot successor and
observe a new arm-time debit against the same run ledger rather than an attempt
to reserve from the child event allowance.

**Required outcome:** finite arming atomically removes the full declared
successor allowance before reporting success. The allowance contains at most
one attempted provider call per eligible signed-pool body; tool exchanges do
not preallocate unrelated semantic turns. Append failure refunds the
unpersisted transfer. Insufficient funding creates no trigger. A finite fire
executes from its exact reservation even when the shared run later reaches
zero; replay does not mint or spend a second claim. A successor authored during
that turn is independently prepaid from the same run ledger at arm time. A
finite unbounded recurrence is refused, while an explicitly unlimited
recurrence uses only its signed per-event cap. Restart changes none of these
identities or outcomes.

**Failure:** the UI reports an unfunded timer as armed; delivery depends on
incidental shared-run headroom; another fire reuses a prior claim; a bounded
recurrence reserves fewer turns than it advertises; restart mints capacity; or
schedule purpose, task words, roles, domains, tool names, paths, formats, or
payload meaning affect funding or admission.

## 17. Static contradiction audit

A cutover is design-complete only when current normative text contains no live:

- mission charter or refinement reducer;
- task classifier, phase graph, keyword/regex selector, or prompt program;
- required fixed personality/public identity field;
- ranked/top-K memory, skill, tool, candidate, or population selection;
- structured work readiness or capability-gap lifecycle/completion gate;
- work-note defer, settlement, current, or stale classification;
- required birth-need/action staging or fixed genesis fields;
- inferred artifact MIME or singular primary domain;
- inferred replication effect;
- semantic admission bounds or refusal-driven action selection;
- provider/registry/default ordering as bootstrap model authority;
- paging that silently deduplicates authoritative append positions; or
- equation of quiescence with a terminal outcome.

This audit is performed by reading current design text and checking diffs. It is
not an executable unit, integration, canary, or performance test.
