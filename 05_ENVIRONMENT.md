---
title: PersonaOS — Environments
status: Stable
---

# 05 — Environment

An environment is a durable signed scope for membership, shared workspace,
resources, events, access, and discovery. It does not define a room type, team
shape, role hierarchy, task workflow, prompt, or completion rule.

## 1. Environment record

The environment record binds exact environment/principal identities, current
signing authority, authenticated charter/intent bytes where present, access and
visibility policy, resource pools, workspace head, lifecycle, zero or more
unranked `domain_refs`, and signatures.

The kernel validates exact mechanics without interpreting a charter as a role,
profession, deliverable list, tool requirement, team plan, or semantic action
surface.

## 1a. Persona-authored environment identity

An active member may append a signed environment-identity record carrying an
exact title and an exact purpose description. Both are bounded canonical bytes
chosen entirely by the persona. The kernel validates length, encoding, and
membership authority, and never reads those bytes as a room type, role, task,
domain, workflow, ranking, or completion claim.

Records are immutable and append-only. `revision` is only a mechanically
verified append sequence and `supersedes_ref` only an exact pointer to the
preceding record. The projected environment title and description are the
mechanically-latest verified record: highest verified append revision, with
authored timestamp and then immutable record id as exact ties. Latest is not
winner, consensus, correctness, or current truth; no append relabels or
obsoletes an earlier one, and every prior record stays independently navigable
and attributed to its exact author. Projections label the record by author
persona and authored time exactly as a work note is labelled.

Host-set name and description remain the projected fallback while no verified
persona-authored record exists, and are never overwritten by one. Authoring is
optional: it grants no authority, elects no coordinator, changes no membership,
and schedules no wake. A missing environment title or description never blocks
work, membership, discovery, or acceptance.

## 2. Membership and consent

Membership is an independently signed relation among exact persona,
environment, invitation/authority, consent response, lifecycle, and policy.
Birth, discovery, public identity, communication, or workspace visibility does
not imply membership.

Optional persona public fields are never membership prerequisites. Missing
name, portrait, description, characteristics, memory, skill, work note, or
gap-like authored knowledge cannot block active membership or work.

## 3. Exact event fan-out

Task-ingress and resource-resume events carry the same exact signed source bytes
and hash to every active environment member under the same bounded pool. Each
member receives an independent delivery lease and settlement identity.

The environment does not select a coordinator, owner, lead, reviewer, role,
representative, or preferred recipient. Members may act, communicate, schedule
themselves, or make no model call.

Other events retain their exact addressed recipients or visibility scope. The
kernel never expands or narrows recipients by reading content.

## 4. Workspace

The environment stores exact integrated workspace revisions and per-persona
worktree bindings. Every turn lease preserves task, source event, persona,
entry revision, byte capture, action effects, publication, and settlement.

Every projected workspace file row binds `modified_epoch_seconds` — the exact
filesystem modification instant of the captured bytes. Together with the
carrier's present-moment fact this makes an artifact's age perceivable to the
recipient; the row itself carries no age arithmetic, freshness label, or
ordering by recency.

The modification instant is an observation *of* the captured bytes, never a
byte difference. Workspace **byte identity** — the state signature and the
per-path publication diff — binds the instant-stripped row form, and covers
file, symlink, and device rows only: directories are implied by their
observable contents (an empty directory cannot travel the publication channel,
and a directory's link count moves with children outside the observable walk).
Two trees holding identical bytes are identical regardless of when or how each
was materialized. Rows keep the instant as an observation member. Surfaces the
publication channel structurally cannot carry (`external-artifacts/requests/`,
git metadata, conflict preserves, package staging) are excluded from the
identity walk symmetrically with staging.

Concurrent publications retain authorship. Peer bytes do not become another
actor's effects. Conflicts preserve all exact alternatives until an authorized
signed resolution chooses or synthesizes bytes.

A conflicted authored revision and a later editing baseline are separate
mechanical states. Once the conflicting head, merge preimage, exact alternatives,
and preservation manifest are durably bound, the disposable worktree for a
later turn starts at current shared HEAD. The displaced authored head remains
reachable through an immutable ref and the conflict remains open. Refreshing
that baseline neither adopts the environment alternative nor resolves the
conflict; it only prevents historical branch divergence from hiding current peer
work or making later calls rediscover it.

An authenticated resolution applies only the alternatives committed by the
exact conflict reference to the then-current shared tree. It does not replay an
unrelated cumulative persona branch. Both the pre-resolution shared head and
the preserved authored head remain recoverable, and the resulting complete tree
is verified before a persona-signed resolution claim can close the conflict.

This protocol has no migration or compatibility path for abbreviated heads,
archive-projection commits, or branches produced by an earlier conflict
lifecycle. A live conflict must bind exact full object identities and begin on
this lifecycle; incompatible state is refused and a fresh environment is used.

## 5. Resources and model calls

Environment resource pools provide exact call/byte/time/tool/payment or other
mechanical authority. Resource facts are visible to personas but never converted
into exploration breadth, population pressure, team size, tool choice,
completion, or automatic continuation.

The signed run-model pool is an unordered ceiling. A matching persona-signed
choice supplies model order for its exact generation; without one, more than
one mechanically callable body fails closed rather than using environment,
provider, or registry order.

One deployment-policy exception exists, and it is operator authority, not
substrate inference: the environment model registry may carry an
**operator-declared role→model preference** — an ordered model-id list per
exact role string. It supplies the default ordering ONLY for a turn whose
attributed role string it names, only inside the signed run-pool ceiling,
and only until a persona-signed model choice exists, which always supersedes
it. The registry never derives a role from persona characteristics, content,
or history; an unnamed role, an empty policy, or a policy entirely outside
the pool falls back to the principal-signed bootstrap member exactly as
before. Every selection remains recorded with its strategy on the model-call
record.

Activating a wider catalogue is a two-lever operator action, both levers
authenticated and neither implicit: (1) submit or resume a run whose
`available_model_ids` names the wider pool — a resume may widen the pool
relative to its predecessor because the resume authority is the same
principal authority that funded the run; (2) optionally declare the
role→model preference (deployment configuration) so role-attributed turns
order inside that pool. A deployment whose runs are submitted single-model
keeps both levers inert by construction; nothing in the substrate widens a
pool on its own.

Budget exhaustion pauses exact pending carriers and preserves best-so-far
state. A later signed resource event resumes the same task through all-member
fan-out. Status ticks, heartbeats, and headroom alone do not schedule cognition.

## 6. Actions, capabilities, and knowledge

Every ordinary member wake receives the complete currently authorized unranked
action catalog plus bounded paginated inventories of local execution, mounted
tools, visible memories/knowledge, peer persona-knowledge/tool metadata, and
population facts.

The environment does not select or rank items from task, charter, domain,
profession, filename, extension, MIME, prompt, regex, work note, gap, or role.
Personas navigate through explicit signed actions.

## 7. Communications and shared records

Messages, invitations, publications, reviews, schedules, work notes,
coordination proposals, and population actions are distinct signed records.
Their content has no implicit environment semantics.

The complete verified collaboration source is bound by
`personaos-coordination-context/3` and its lineage snapshot. Provider-bounded
event/member pages preserve exact totals, cursor ranges, omissions,
truncations, source hashes, and completeness. Whole-prompt staging does the same
for every source through an unranked uniform source manifest.

An environment does not aggregate notes into readiness, messages into consensus,
reviews into acceptance, or population prose into birth. Several causal edges
may coexist without a selected representative stage.

## 8. Artifacts and MIME

Environment artifact publication verifies explicit signed `mime_type`, exact
content hash/length, owner/author, role, workspace/action provenance, access,
and plural `domain_refs`.

Filename, extension, path, domain label, prompt, and content sniffing cannot
replace MIME or artifact-role authority. Lazy rendering begins only after exact
byte verification.

## 9. Discovery and continuity

An environment card is compact current-master-signed metadata with exact
visibility, expiry, content hash, and reachability. It streams as soon as it
verifies; discovery does not wait for artifact or telemetry hydration.

Process/node resume reconstructs the same exact memberships, workspace,
resource/pending-event state, persona identities, memories, skills, notes, and
communications from current signed records. It does not mint replacements.

Direct/local/P2P routes are primary. An HTTP locator is last-resort and never
environment authority.

## 10. Policy and safety

An environment policy can constrain exact subjects, actions, effects, access,
and resources within its signed scope and cannot weaken higher authority.
Current signed authority supplies its values; task/persona content cannot
derive them.

Policy is applied by exact bindings, not by classifying prose or artifacts. A
policy does not create a prompt, role, workflow, tool requirement, population
action, or completion rule unless exact principal acceptance authority
separately declares the latter.

## 11. Quiescence and lifecycle

With no pending causal delivery, the environment/task is quiescent. Quiescence
is nonterminal and does not mean complete, ready, empty, failed, abandoned, or
incapable of improvement.

Pause, resume, cancellation, archival, membership change, and termination
require their exact authenticated lifecycle events. A later authentic event may
resume quiescent work.

## 12. Removed compatibility surface

There is no live compatibility for fixed environment/room blueprints,
environment-assigned roles, coordinator schedules, attention/goal arbitration,
automatic ambient-event cognition, structured readiness, mission charters,
domain-selected tools, or status-driven resume. Historical records may remain
opaque audit bytes but confer no current behavior authority.

## 13. Design criteria

1. Environment state is exact, signed, durable, and replayable.
2. Persona-authored environment identity is optional, append-only, and never
   interpreted; latest is mechanical order, not authority.
3. Membership requires independent consent and no optional identity fields.
4. Task/resource events fan out unchanged to all active members.
5. Workspace, artifacts, and effects retain exact authorship.
6. Resource/policy facts never select semantic behavior.
7. Discovery is incremental and decentralized.
8. Quiescence is nonterminal.
