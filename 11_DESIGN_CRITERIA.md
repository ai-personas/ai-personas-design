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

A new persona appears only after a signed need, exact unranked discovery receipt, persona-authored disposition for every returned candidate, signed genesis proposal, and mechanical admission. The admitted birth action materializes one deterministic parent-signed environment invitation and delivers it to the newborn. The newborn independently authors public identity and the invitation response; membership exists only when that response explicitly commits it.

No birth is also a valid emergent result when current participants can cover the work. The evidence is the causal decision trail, not an expected headcount.

One exact signed need can materialize at most one newborn. Distinct signed
needs may proceed concurrently under the configured mechanical bounds; one
broad need or an unintegrated newborn cannot lock unrelated persona-authored
contributions out of the whole task. Newborn formation receives exact bounded
parent practice evidence, never a host-assigned profession.

An admitted newborn is not considered a usable team member merely because its
identity is discoverable. The operating path must show the exact invitation,
newborn consent, active causal membership, and subsequent peer-visible work.
Interrupted replay recovers the same invitation authority without duplicating
the birth or bypassing consent. A durably persisted identity outbox whose first
enqueue meets a busy actor is pending delivery, not a refused birth; the signed
invitation must still materialize so identity-completion replay can deliver it.
Identity and invitation-decision turns expose no artifact-package transport and
cannot publish a persona branch or package to the shared environment. Consent
may activate only a subsequent member turn; it never retroactively authorizes
task artifacts emitted while the persona was still forming or deciding.

Membership and public-identity readiness remain independent after consent. If
an identity turn leaves verified components incomplete and has no exact pending
external-artifact successor, the persona's next causally authored wake retains
the narrow identity action surface. A pending request permits ordinary work
only while its dispatcher state proves a live successor. A terminal blocker
may deliberately leave the authored request unresolved, but its already
delivered blocker wake is not still a future event; the next causally authored
wake therefore reopens the narrow surface. A delivered identity artifact
returns there for persona-authored admission. This liveness rule observes only
exact request/hash and dispatcher state and never supplies portrait content,
provider choice, semantic role, or an unsolicited wake.

A pinned external-action helper may publish at most one bounded, pattern-safe
failure code from its sealed stderr protocol. Arbitrary stderr, response
content, credentials, and exception text remain private. This makes retry and
blocker state diagnosable without turning provider output into persona intent.

An ordinary communication response cannot satisfy that narrow readiness turn.
Verified missing components require only their descriptor-annotated transition;
delivered raster bytes require one persona-authored admit-or-reject disposition.
This guarantees causal progress without choosing identity content or forcing an
unwanted portrait to be accepted.

Every narrow portrait turn also receives the public-portrait contract as
bounded structured facts: a recognisably person-like subject is required, an
emblem or role icon alone does not satisfy it, artistic style remains the
persona's choice, and the stable characteristic profile (including OCEAN or
baseline VAD when present) grounds that choice. This is an identity protocol
invariant, not a generated prompt or a semantic routing rule. The runtime does
not inspect the candidate pixels or invent a face; it attaches the exact
receipt bytes and the persona authors the visual disposition.

A retryable validation rejection is not a completed readiness transition. The
same bounded turn retains the exact required descriptor until it succeeds,
returns a terminal refusal, or registers an authenticated future stimulus that
owns the next attempt. Free text after a rejected call cannot settle the gate.
Retryability is reduced across both the transport wrapper and its exact nested
dispatcher result; wrapper shape cannot erase a live correction obligation.

If a required descriptor mechanically registers an asynchronous terminal
event, budget admission MUST atomically pre-fund both the current semantic turn
and every required terminal successor before the first model call. The two
allowances remain separate capabilities, and unused units return to the exact
source budget after settlement. Insufficient combined authority pauses the
carrier without making an LLM call. This admission rule is derived only from
the signed action descriptor and run model pool; it cannot inspect task text,
profession, provider, output format, or action name.

The semantic-turn allowance covers the initial decision, one bounded
correction or tool-result exchange, and an effect-free terminal response. If
that allowance is exhausted before any authenticated effect, the outcome is a
retryable model-resource unavailability state, not actor failure or inferred
persona intent. Once an effect has occurred, it remains authoritative and the
turn is never replayed merely to obtain nicer terminal prose.

Each asynchronous terminal successor receives that same three-stage bounded
allowance. Funding only a decision and one correction strands a valid
provider-neutral action before its required terminal carrier and converts a
prepaid callback into deterministic budget exhaustion. This allocation shape
is uniform across terminal event kinds.

When the transition is disposition of a verified delivered raster, the exact
receipt-bound workspace bytes MUST be attached as visual model input when the
selected body supports that transport. Path containment, byte length, digest,
media type, owner, environment, and receipt lineage are reverified first. A
historical rejected receipt is not an awaiting candidate and cannot keep the
disposition gate open. The attachment supplies observation, never admission.
If a later causal carrier reopens that gate, it MUST attach the same uniquely
awaiting verified bytes. The request ID, request hash, and receipt hash for
rejection and admission, together with the destination and content references
for admission, are hidden transport bindings to that one candidate. Admission
MUST NOT degrade from an owner-matching receipt to an arbitrary file merely
because those bytes are visible in a shared environment workspace. The exact
verified delivery authority is retained in the persona-signed identity
transition. The persona still chooses the action and authors its rationale; the
substrate performs no semantic disposition.

Receipt delivery to the exact authorized persona workspace is sufficient for
the owner's next inspection and disposition turn. Publishing those bytes into
the shared environment workspace is a separate durable mechanical effect. A
slow or refused shared-workspace reconciliation MUST NOT hold the receipt-state
lock, consume the terminal callback allowance, or delay owner-local cognition.
Its retry path is serialized independently and may settle after the persona
turn. Unrelated branch divergence therefore cannot strand a valid delivered
artifact or turn an available callback into model-budget exhaustion.

A raster descriptor and persona signature are necessary but not sufficient
identity authority. The current descriptor counts as admitted only when the
latest avatar evolution transition is signed by that persona, matches every
descriptor and byte-derived field, and retains the exact owner/request/receipt
authority for those bytes. An orphan descriptor or a transition without that
source lineage fails closed as absent. Birth and restore MUST NOT copy,
re-personalize, or re-sign a parent's or peer's identity asset for a newborn.

### C-OP-9 — Multiple personas genuinely coordinate

Each active participant receives current signed peer cards and bounded recent contributions. Messages have exact recipients and causal references. A participant can challenge, review, improve, request evidence, or remain quiescent. One persona's ready state cannot close another persona's commitments or be labelled collective review.

When a local persona authors a communication inside a turn, delivery to its
peer is causally fenced until that source turn's completion boundary has
settled the associated workspace and package effects. The fence is derived
only from the verified communication envelope and active source lease. It does
not inspect the message, task, artifact paths, profession, or tool choice. The
recipient therefore sees the bytes the sender just referenced without spending
a call racing a publication that is still in flight.

### C-OP-10 — Model calls purchase useful decisions

Every model call is attributable to a funded persona contribution or decision. Discovery, signing, replay, stale-state invalidation, public projection, and completion reduction are token-free. The runtime makes no separate model call for host-authored orientation, pressure scoring, generic “is this sufficient?” appraisal, timestamp refresh, or unchanged-wake restatement.

When a seed persona's first authenticated principal task and its still-unobserved
signed activation are both pending, activation MUST be delivered first as a
distinct identity-formation turn. That turn exposes only the live actions whose
trusted descriptors declare identity-formation authority and the exact current
name, characteristic, portrait, external-artifact, provider, and readiness
state. It exposes no native command lane, task-artifact package lane, mission
work-state disposition, or ordinary work catalog. The later principal-task turn
gets the ordinary complete action surface after activation and its already
authored descendants settle. This call is useful identity authorship rather
than host-authored orientation: the substrate chooses no name, characteristics,
portrait prompt, style, provider, model, role, profession, or task action.

After any provider-native completion produces authenticated non-read-only
persona activity, a missing or invalid required terminal response MUST move
directly to the bounded effect-free response carrier. The ordinary tool-bearing
continuation MUST NOT be reissued against that completion's frozen situation.
This boundary is derived only from signed receipts, descriptor annotations,
required byte evidence, and response validation; it does not classify task
text, action names, commands, filenames, formats, professions, or tools.

For live operation in this release, routed models must be GPT-5.5 or lower. A higher model request is a visible configuration failure, not an automatic substitution.

Every substantive tool, peer, communication, or workspace effect appends one
signed idempotent practice observation without another model call. The same
turn's required persona-authored experience reconciliation says whether the
practice changed the persona. Its closed agency evidence must remain admissible
up to that protocol's declared bounds; the surrounding open-collaboration
limits cannot invalidate it and erase an otherwise valid successor. Exact
practice references are attached from signed receipts, and reusable-learning
state exists only when the persona actually used a descriptor-annotated skill,
brain, or characteristic evolution mechanism. Asking the model to transcribe
those hashes or a mechanically known boolean, generating a host competence
score, automatically promoting a profession, or adding a periodic reflection
call is a failure. Projection and verification MUST use the same bounded exact
practice-evidence reducer. A reference mechanically attached by the runtime
cannot be rejected by a narrower traversal or consume a correction call.

A population need visible in effective work state must be backed by unresolved
verified birth lineage or a successful current-turn need, search, or genesis
receipt. Population desire expressed only as prose is not an action and cannot
hold a task open. The mechanism annotation is generic and trusted descriptor
state; task words, profession names, filenames, extensions, and executable
names are never population triggers.

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

A work-state freshness comparison excludes only protocol-declared transient
transport and same-turn history projections: a contextual action menu, an
already-verified peer card's renewed lease/route/enclosing signature, and the
append-only verified action/practice account already reconciled inside the
signed state. Their renewal cannot make current cognition stale. Exact task,
environment, membership, persona-authored peer identity, domain, acquired
capability, artifact, conflict, and workspace facts remain freshness authority.

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
