---
title: PersonaOS — User-Intent and Operating-Path Criteria
status: Stable
---

# 11 — User-Intent and Operating-Path Criteria

The design specification and the principal's current intent are the source of product criteria. An executable unit, integration, canary, benchmark, or performance-test corpus is not a second product specification and is not an operating-path substitute.

This document records observable outcomes, admissible signed evidence, and failure states. It deliberately contains no test harness, fixture, mock, assertion code, synthetic canary, or score optimized independently of useful work.

## 1. Evidence policy

A criterion is satisfied only by evidence from the real operating path, such as:

- current signed node, environment, persona, task, and workspace projections;
- persona identity signatures and lineage events;
- exact workspace bytes and content hashes;
- artifact manifests and format-aware rendered views;
- persona-authored work states, communications, actions, and birth decisions;
- provider model-call receipts and tool execution receipts; and
- direct human inspection of the produced deliverable.

A source file named like a criterion, a mocked response, a self-authored review label, a model claim that work succeeded, or an old persisted run is not evidence that the current operating path works.

## 2. Criterion structure

Every criterion has four parts:

1. **Intent** — the principal or normative design outcome.
2. **Observable outcome** — what a person can see or use.
3. **Admissible evidence** — current signed state and exact artifacts that support it.
4. **Failure state** — what must remain visible when the outcome is not yet achieved.

Criteria are open to stronger evidence. They do not prescribe hidden reasoning, role names, prompt phrases, exact filenames, or a fixed persona count.

## 3. Operating-path criteria

### C-OP-1 — Fresh means fresh

After an explicitly requested clean start, no old node lease, persona, environment, run, workspace, discovery record, or browser directory row is presented as current. Historical material may exist only outside the active runtime and must not be announced.

### C-OP-2 — Discovery is fast and incremental

Direct routes, local discovery, and libp2p/Kademlia discovery run concurrently. A verified node is shown as soon as its master identity verifies; environments and personas appear as soon as their signed inventory records verify. The UI does not wait for a complete global scan.

The browser begins its first bounded temporal rendezvous scan immediately after transport startup and streams each routed provider candidate into the existing authority gates as that responder returns. Retry delay follows a miss; it is not paid before the first attempt, and one slow first-contact peer cannot hold a faster verified provider behind an all-responder barrier.

An HTTP locator is consulted only when no primary route is viable. `node1.personas.ai` is a replaceable last-resort route hint, never a dependency or authority. Expired records disappear by signed expiry and source-scoped reconciliation rather than accumulating as stale global nodes.

Every public node transport, including the peer-bound public-data protocol, exposes the same compact current-master-signed persona/environment identity index. The browser requests that index concurrently with the complete provider inventory and paints each fully verified identity at the next render opportunity; artifact and telemetry verification cannot gate this first roster. It may persist only the exact verified signed index and verified content-addressed portrait bytes. Every warm hydration re-verifies signatures, policy, expiry, persona binding, hash, MIME, byte length, and dimensions, and then reconciles against fresh primary routes. A cache accelerates presentation but never extends a lease, supplies routing authority, or preserves an omitted identity.

### C-OP-3 — Personas look and read like people

Before identity materializes, the surface says `Forming identity` and shows a neutral person silhouette. A materialized persona presents its exact persona-authored meaningful name, a human-useful description of how it contributes, and a recognisably person-like portrait. The persona selects the portrait's artistic style and grounds it in its stable characteristics, including OCEAN or baseline VAD when present.

IDs, hashes, schemas, and lifecycle mechanics remain verification detail. The UI does not parse a role from a name with a profession regex or invent one from task text.

### C-OP-4 — Persona continuity survives environment and node resume

Resuming an environment restores its exact members, identity keys, memory, commitments, work replicas, and unresolved communications. It does not mint replacement personas because process memory was lost. A previous persona resumes only when its signed durable state verifies; otherwise the failure is explicit.

### C-OP-5 — Human work state leads the persona view

The first activity surface answers: how the persona sees the task, what it is doing, what it completed, what comes next, what it has committed to, what remains uncertain, and how it is collaborating. Model names, HTTP status, raw latency, kernel snapshot labels, and opaque IDs are secondary technical detail.

The view rejects an invalid, stale-as-current, unsigned, wrong-persona, or wrong-node work-state document.

### C-OP-6 — Artifact names and formats are immediately legible

Every artifact row leads with the basename and a visually prominent extension or format badge. The parent folder is secondary; the full path is available without dominating the row. A person must not have to scan a long path to discover the file type.

Opening an artifact lazily loads the renderer selected from verified bytes, declared media type, signature, and filename evidence. Markdown, text, source, structured data, raster, SVG, PDF, office/document, archive/package, audio/video, mesh, point-cloud, and CAD/BIM formats use the strongest safe supported view. Unsupported or malformed bytes receive an honest download/technical fallback, never a misleading “binary” preview when a supported format is identifiable.

### C-OP-7 — Engineering tools and artifacts emerge from the work

Personas inspect generic execution and tool capabilities, acquire or author a capability when needed, and create the artifacts they judge necessary. Every successful invocation has a mechanically bound capability-use receipt, capability gaps have durable actor-authored IDs and explicit transitions, and a sufficiency claim is ineffective while any such gap remains active. The runtime contains no task-word, profession-word, filename, extension, or domain-regex branch that causes CAD, CAM, a specialist birth, or a particular deliverable.

For the current four-bedroom-house intent, useful evidence includes an editable spatial model and human-readable engineering package when personas judge those necessary for a credible result. A prose-only answer that claims a model exists is not equivalent to model bytes.

### C-OP-8 — Population change is causal and persona-authored

A new persona appears only after a signed need, exact unranked discovery receipt, persona-authored disposition for every returned candidate, signed genesis proposal, and mechanical admission. The newborn independently authors public identity and membership decisions.

No birth is also a valid emergent result when current participants can cover the work. The evidence is the causal decision trail, not an expected headcount.

### C-OP-9 — Multiple personas genuinely coordinate

Each active participant receives current signed peer cards and bounded recent contributions. Messages have exact recipients and causal references. A participant can challenge, review, improve, request evidence, or remain quiescent. One persona's ready state cannot close another persona's commitments or be labelled collective review.

### C-OP-10 — Model calls purchase useful decisions

Every model call is attributable to a funded persona contribution or decision. Discovery, signing, replay, stale-state invalidation, public projection, and completion reduction are token-free. The runtime makes no separate model call for host-authored orientation, pressure scoring, generic “is this sufficient?” appraisal, timestamp refresh, or unchanged-wake restatement.

When a persona's first authenticated principal task and its still-unobserved
signed activation are both pending, the activation fact MUST be co-delivered in
that exact `task_received` carrier. One verified persona turn atomically settles
both observation deliveries; the substrate MUST NOT reserve or spend a separate
activation/orientation model call before exposing the principal task. This
changes no persona choice: identity actions, ordinary work, communication, or
inaction remain available from the same live descriptor catalog.

For live operation in this release, routed models must be GPT-5.5 or lower. A higher model request is a visible configuration failure, not an automatic substitution.

## 4. Emergence boundary

The following belong to personas and may use open vocabulary:

- task understanding and decomposition;
- expertise and contribution descriptions;
- collaboration and review choices;
- tool and artifact choices;
- birth need and candidate dispositions;
- genesis characteristics, principles, and experience material;
- public name, description, and portrait choice; and
- work commitments and readiness.

The following belong to the kernel:

- authentication and authorization;
- exact signatures and hashes;
- lifecycle and membership state;
- bounded canonical wire shapes;
- causal lineage and replay;
- budget and replication ceilings;
- workspace isolation, conflicts, and exact byte settlement; and
- mechanically reducing explicit commitment transitions.

The kernel must not bridge these lists by interpreting persona prose.

## 5. Persona continuity and identity

Identity is established by the persona key, signed SOUL lineage, and current lifecycle projection—not by a model session, display name, avatar URL, or browser cache. A name or portrait revision does not create a new persona. A forming shell is visible without pretending that unmaterialized fields are authored identity.

## 6. Global discovery and coordination

Global discovery is a set of independently verifiable provider routes, not one global server. Records are source-scoped and expiry-bound. Direct/P2P success suppresses last-resort locator use. Browser storage cannot extend a signed lease or keep a removed provider alive. A verified PersonaCard found anywhere in the global object space remains subject to visibility, invitation, consent, and local execution policy.

Compact identity transfer is an ordering optimization over the same signed authority, not a second directory. HTTP and P2P race as equivalent byte carriers after peer identity is bound; the first valid result paints while full-inventory, DHT, gossip, and route reconciliation continue independently.

## 7. Completion and continued improvement

Completion requires current materialized outcome evidence, no unresolved exact workspace conflict, and current ready work states for every required active participant. A ready state with open commitments, open uncertainties, active capability gaps, or an inconsistent causal successor is invalid. Each uncertainty has actor-authored identity and an explicit `open` or `accepted_assumption` disposition; accepted assumptions remain human-visible without falsely keeping the causal graph open. `PERSONA_WORK_STATE_AUTHORED` is the single authoritative task-progress/readiness signal, so a separate task-progress action cannot present a premature completion label. The persona authors one real successor mechanism or blocker; progress, successor identity, and work-state continuation are mechanically projected from it instead of being three duplicated semantic fields. A same-revision commitment may be satisfied only by an explicit evidence-bearing transition, and capability reconciliation receives the reducer's exact post-transition active commitment IDs rather than asking the model to repeat them. Quiescence with open work requires an evidenced external blocker naming every exact blocked issue. A schema-valid but cross-field-inconsistent terminal value receives at most two effect-free corrections inside the same bounded turn; it is never accepted, semantically repaired by the host, or allowed to replay actions. Provider normalization cannot erase required or explicitly nullable fields from that authored correction, and every rejected correction records its current structural or cross-field validation stage rather than reusing a prior failure. A peer state bound to older bytes is stale. A singleton result must be labelled a singleton assessment unless the principal explicitly required and received independent review.

Budget exhaustion pauses open work and preserves best-so-far artifacts; it is not semantic completion. A later exact resource grant resumes the causal work rather than restarting it as a new identity.

## 8. Current house-task intent

The current principal intent is a high-quality four-bedroom-house design comparable to serious human architectural/civil-engineering work and improved through collaboration where useful.

The personas—not the substrate—decide the exact package. Human inspection should nevertheless be able to find, as appropriate to their authored plan:

- a coherent brief and stated assumptions;
- dimensioned spatial information;
- editable CAD/BIM or other machine-usable geometry;
- readable drawings or rendered views;
- structural/site/services considerations and unresolved professional inputs;
- calculations, schedules, or specifications supporting decisions;
- coordination/review evidence and revision history; and
- honest limitations, code/jurisdiction dependencies, and next professional actions.

The package may exceed this list or use better formats. The list expresses principal intent for this task; it is not embedded in runtime prompts, regular expressions, tool routing, birth admission, or completion substrate.

## 9. No executable test substrate

The repositories contain no unit, integration, canary, benchmark, or performance-test suite and no running test process. Operating-path verification uses the signed evidence policy in §1 and the actual live task. Design review may record gaps and inspect evidence, but it cannot manufacture a PASS independent of the useful result.
