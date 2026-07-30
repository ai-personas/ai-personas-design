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
Expired or omitted identities disappear. The HTTP locator remains unused while
any primary route is viable.

**Required outcome:** the UI paints each verified persona without waiting for
artifact or telemetry hydration. Missing optional name/portrait fields receive
neutral honest placeholders and do not hide the actor.

**Failure:** stale rows survive because of cache; one slow peer blocks first
paint; `node1.personas.ai` becomes authority; missing portrait blocks discovery.

## 3. Optional identity evolution

**Input:** an active persona has no display name, biography, or portrait.

**Trace:** an ordinary wake includes the complete action catalog. The persona
may work, communicate, use tools, author identity, or do nothing. No repair wake
or narrow identity menu is synthesized.

If authenticated user intent requires a person-like portrait grounded in
persona-authored characteristics, the exact requirement appears as principal
intent. The persona chooses how to satisfy it. Any portrait declaration binds
signed MIME, exact hash/length, owner, role, and provenance.

**Required outcome:** work authority never depends on optional fields. The
kernel verifies bytes and authority without choosing a face, style, name,
traits, provider, or prompt.

**Failure:** an identity gate suppresses task actions; host constants require
OCEAN/VAD or a face; a suffix supplies MIME; UI invents a role.

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

**Failure:** only the prior owner resumes; a status flag creates a call; grant
duplicates a settled delivery; missing identity fields block resume.

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

**Input:** a persona encounters unfamiliar work and may or may not describe a
perceived gap inside opaque knowledge content.

**Trace:** exact paginated unranked inventories expose local execution, mounted
tools, verified peer/public metadata, memories, and skills. The persona may
inspect, communicate/share exact refs, obtain authorized bodies, search,
acquire/provision/invoke tools, author opaque knowledge, or ignore items in any
order.

**Required outcome:** receipts preserve exact provider, action, result, and byte
effects. Gap-like content is optional and has no dedicated lifecycle or
readiness/continuation semantics.

**Failure:** top-K or score chooses a tool; task words cause CAD/Blender; a gap
narrows the catalog, selects a teacher, or schedules another call; use grants
expertise automatically.

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

**Required outcome:** no separate need/action record is required; both distinct
proposals may be admitted within mechanical bounds, while replay of either
exact proposal cannot mint twice. Context fields create no identity claims.
Each newborn independently accepts membership.

**Failure:** admission requires a semantic need or recruitment ceremony; fixed
fields assign a role; a score admits birth; replication is inferred from an
action name; birth creates membership.

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

**Required outcome:** omission/truncation is explicit; provenance and consent
survive ref sharing and authorized body access; durable evolution has persona
authorship. No semantic name, interface, parent-skill, synthesis/composition,
catalogue, transfer, conflict, review, or promotion shape is required.

**Failure:** host retrieves top-K, ranks relevance, injects a hidden prompt,
automatically consolidates/decays memory, chooses a teacher, requires a
synthesize/compose lifecycle, or awards expertise.

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

## 12.2 Mechanical admission boundary

**Input:** a persona chooses one exact declared action while task text also
suggests several other plausible tools, artifacts, collaborators, and
population choices.

**Trace:** admission reads only canonical bounds, signatures/hashes, exact
scope, membership/consent/access, preimages, replay/idempotency, current leases
and resources, descriptor effects, and applicable exact safety/external/
physical authority. Current signed policy supplies bound values.

**Required outcome:** the chosen effect is admitted or refused on those facts.
No alternative is ranked, recommended, invoked, or hidden, and no bound value
is inferred from task, role, prompt, note, knowledge, filename, MIME, or desired
artifact semantics.

**Failure:** a refusal routes to another tool/model/action; a task classifier
changes a limit; a safety policy assigns a profession/role; capacity becomes a
team-size recommendation.

## 13. Plural domain references

**Input:** one artifact and one skill cite two domains; another cites none.

**Trace:** adapters preserve all exact signed `domain_refs` without reordering
them semantically or collapsing them to a primary domain.

**Required outcome:** all records remain valid and navigable. No reference
changes actions, roles, tools, prompts, or completion.

**Failure:** first domain becomes authoritative; task text selects a domain;
cross-domain record is refused solely for plurality.

## 14. Quiescence and later resume

**Input:** no causal delivery remains, although personas could plausibly improve
the result and a work note says “continue.”

**Trace:** the task projects quiescent with preserved artifacts and notes. No
model call is scheduled. Later, an authenticated peer/resource/principal event
arrives and resumes the same task.

**Required outcome:** quiescence is nonterminal and separate from acceptance.
The later exact event, not prior prose, creates the new carrier.

**Failure:** host polls because improvement is possible; “continue” creates a
wake; quiescence is shown as complete; later event starts a replacement task.

## 15. Objective acceptance

**Input:** current bytes exist, model and tool calls succeeded, one note says
done, and exact principal acceptance is absent.

**Trace:** all receipts and claims remain visible. Only declared current
acceptance authority is evaluated against its exact evidence.

**Required outcome:** successful transport and materialization are not silently
upgraded to semantic acceptance.

**Failure:** HTTP 200, artifact count, member consensus, active-gap absence,
score, or unchanged bytes establishes completion.

## 16. Static contradiction audit

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
