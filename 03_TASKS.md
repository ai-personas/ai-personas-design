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

A task amendment or continuation preserves the complete verified principal-
intent ancestry in causal order, including the original signed intent bytes and
each later signed amendment. The newest carrier does not replace, summarize, or
reinterpret an older principal event. Every retained entry remains bound to its
own signature, content hash, task generation, and causal predecessor.

The model-turn transport carries the complete current intent and complete
verified ancestry in a dedicated exact authority lane. Uniform paging of
optional situation sources never clips, prefixes, reorders, or competes with
that lane. Task intake and model-turn construction enforce the same byte and
record bounds; if the complete authority lane cannot fit, admission is refused
before cognition instead of presenting an omitted or summarized requirement.

Current agency uses a second exact, content-bound navigation lane. It carries
the complete leased action catalogue, the complete mechanically observed
execution-name index, the verified current population/replication authority,
and every current workspace file path. These components are selected only by
closed schema identity and content hash, never by task words, roles, filename
suffixes, domain labels, rankings, or recommendations. Large append-only
activity histories remain independently hash-bound and pageable; they cannot
displace present actions, peers, population bounds, executables, or files.

A resumed environment reconstructs project references from reciprocal verified
project and environment lineage. A mutable projection field is not routing or
prompt authority. Repeating a persona-signed request for an identical already
verified topology is an idempotent observation, while any differing name,
membership role, or target remains an explicit conflict. A verified outstanding
persona schedule is an event-driven continuation even while no model call is
running; quiescence and completion remain distinct states.

The signed `run-model-pool/1` in that authority is an unordered ceiling, never
a preferred-model list. Task text cannot order its members. If more than one
body remains mechanically callable before an exact matching signed
`persona-model-choice/1` exists, substantive model routing fails closed; a
provider registry, configuration order, default client, or host bootstrap call
cannot choose on the persona's behalf.

Empty, one-domain, and cross-domain task contexts are valid. There is no
host-selected primary domain.

## 2. Exact fan-out to active members

The ingress event and every later task-resume resource event are offered
concurrently to **every active environment member**. Each delivery binds the
same exact source-event bytes and hash, task, environment, principal intent,
resource pool, and workspace observation.

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
catalog and bounded exact situation facts. Population, identity, public-card,
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

The runtime contains no built-in CAD, CAM, Blender, OpenSCAD, engineering,
software-job, electronics, mathematics, house, document, or other domain
recipe. Personas may still discover and use those capabilities because exact
unranked inventories and ordinary navigation actions make them reachable.

Receipts record what was actually invoked, produced, transferred, or learned.
They never automatically grant expertise, professional quality, relevance, or
completion.

## 5. Work notes and capability gaps

An active member may optionally author
`personaos-persona-work-state/3`. Its `work_note` is bounded open canonical JSON
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

Concurrent member work remains attributable. A participant's worktree is
leased through action capture, publication, and settlement. Peer publications
may advance the shared environment, but they do not appear retroactively as the
current actor's byte effects, capability use, practice, or authorship.

Conflicts preserve every exact path/hash alternative. Only an authorized signed
resolution chooses or synthesizes bytes; the substrate does not resolve a
conflict from file type, role, task text, or model prose.

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

An attempted continuation action that is mechanically refused returns an exact
stable reason code in its ordinary action evidence. The refusal proves only
that the attempted effect was not admitted; it does not create a successor,
recommend an alternative, or authorize a retry. Transport-injected task, actor,
run, wake, and lease bindings must agree with the public action schema and the
signed descriptor rather than becoming hidden model-authored fields.

Work-note prose, gap-like knowledge content, a population action, successful invocation,
artifact declaration, unchanged/changed workspace, score, objective statement,
HTTP status, and model claim do not create continuation.

## 8. Resource pause and resume

Budget exhaustion pauses affected pending deliveries and preserves their exact
event, task, model pool, workspace binding, and best-so-far bytes. It is not
semantic completion or failure.

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

Principal intent may ask for open-ended improvement. Personas decide what
comparisons, measurements, exploration, review, or further work are useful and
may author causal wakes for them. The host does not implement a universal
refinement loop, epsilon, convergence test, or round counter.

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

## 11. Model-call economy

A model call requires one authentic causal delivery, a current persona/lifecycle
lease, and exact resource authority. Inventory projection, discovery, replay,
signature verification, workspace sync, MIME verification, fan-out,
deduplication, settlement, and public rendering are mechanical and consume no
model call.

The call also requires an authenticated `run-model-pool/1`. A matching signed
`persona-model-choice/1` supplies persona-authored model order and reasoning
effort for its exact causal generation. Without one, only a mechanically unique
callable body may bootstrap cognition. An ambiguous pool is refused; refusal
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
  situation, and factual observation-hash binding; and
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
