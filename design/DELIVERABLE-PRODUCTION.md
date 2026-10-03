# Delivery review: existing rules, not another production architecture

[Design index](README.md) · [Work and cooperation](03-work-and-cooperation.md#how-organization-emerges) · [Requirements](../implementation/REQUIREMENTS.md) · [Compatibility mapping](../implementation/DELIVERY-CONTRACTS.md)

## Finding and correction

**Review revision: 18 September 2026.** This page supersedes the delivery addendum's claim that a separate production-contract layer was needed. The design before that addendum already covered required outcomes, accepted owners, real capability acquisition, native artifacts, analysis mappings, review, integration, revalidation, and honest completion. The existing house fixture already called for reopening, editing, and reproduction. Documentation consolidation was not evidence of an architectural inability to produce artifacts.

| Question from the delivery review | Existing authoritative home |
|---|---|
| What is the actual required result, and who accepted it? | [Work and cooperation](03-work-and-cooperation.md): NED-01–NED-04 and COL-01–COL-05. |
| Can the selected means actually perform the operation? | [Capabilities and action](04-capabilities-and-action.md): ACT-01–ACT-04 and I10. |
| Are the sources meaningful, the analyses actually run, and the versions consistent? | [Evidence and completion](06-evidence-and-completion.md): EVD-01–EVD-05, with the native-output illustration in [worked examples](../examples/WORKED-EXAMPLES.md). |
| Can findings cause repair without infinite effort or stale passes? | [Work](03-work-and-cooperation.md), [resources](05-authority-and-resources.md), and [evidence](06-evidence-and-completion.md): COL-04–COL-05, GOV-02–GOV-04, and EVD-03–EVD-04. |
| Does the same foundation support unrelated needs? | I03 and [behavioral checks](../evaluation/ACCEPTANCE.md#behavioral-checks), especially B11–B12. |

The former DLV-01–DLV-10 identifiers are retired as a separate active requirement family. Their [historical mapping](../implementation/DELIVERY-CONTRACTS.md) preserves traceability; retirement does not waive an applicable original requirement. There are still 21 invariants and 45 active requirement identifiers. The additional D scenarios are evaluation refinements of those rules, not more runtime features.

## What is clarified now

[Chapter 3](03-work-and-cooperation.md#how-organization-emerges) and the [core contracts](../implementation/CONTRACTS.md#persona-owned-organization-and-capability-choice) make the boundary explicit: personas discover opportunities and capabilities, choose methods, propose divisions of work, accept commitments, revise plans, and form recurring practices. The supporting system supplies usable social and action affordances and enforces authority, privacy, resources, recovery, and evidence integrity. It does not solve tasks through a concealed profession map or domain pipeline.

Plans, method notes, output specifications, and delivery inventories can use the existing mandate, work, artifact, agreement, commitment, and release records. They need not become universally required new record types. Specialist tools and learned procedures are allowed; automatic task-to-role or task-to-workflow selection by the runtime is not. Reuse is compatible with emergence when its applicability and adoption remain attributable.

## Adequacy before commitment to a method

**Correction: 23 September 2026.** The earlier adequacy paragraph described useful
activities but was too prescriptive as universal runtime guidance. It is
superseded here, not elevated into a compulsory method-selection checklist.
Reviewing personas judge whether proposed scope, chosen means and actual results
address the request. Authors may seek a peer's view while exploring as well as
submit a finished candidate; other personas can challenge assumptions, identify
omissions, propose different approaches, disagree or decline. These are
participant-owned choices, not a runtime-imposed sequence.

An accepted obligation cannot disappear merely because a convenient alternative
is easier. Preserving that obligation is not a mechanical judgment of which
representation is adequate. A concept, prose response, native source, analysis
or other form can be suitable depending on the actual request. There is no
universal search-first rule, tool quota, required installation, trial count,
parser command, geometry checklist or automatic method-switch trigger.

A native-editability claim may lead a reviewer to reopen and edit the saved model;
a creative judgment may need discussion rather than execution. Those are examples
of claim-specific assessment, not a hidden production pipeline. Reviewers choose
relevant methods, explain their observations and limitations, and may ask for
repair. The [judgment and integrity boundary](06-evidence-and-completion.md#persona-judgment-and-mechanical-integrity)
keeps their verdict separate from byte integrity, user acceptance and outside
assurance. It neither bans mechanical tools selected by personas nor makes a
successful tool operation the judge.

[Context maintenance](02-memory-and-learning.md#bounded-maintenance-with-a-usable-continuation)
preserves actual obligations, peer findings, disagreements and source attribution.
It does not insert an evaluator's checklist or choose a next experiment.
[Evaluation cases](../evaluation/METHOD-CONTINUITY.md) remain outside runtime
policy; case-specific rubrics and historical results retain their own revisions.
These are requirements and specified scenarios, not demonstrated competence.

## An activity note is not a delivered answer

**Clarification: 27 September 2026.** A requested answer must reach an authorized
user-facing surface. A private activity summary, a saved draft without delivery,
or an operator's view of internal activity does not by itself deliver that
answer. A request for an in-app response with no outside action does not forbid
that requested response; it does not authorize unrelated messages or effects.
The persona may prepare and deliver the result in the same decision when the
existing capabilities and permissions allow it.

The primary provider decision declares either no reply or a reply with separately
authored text and explicit visibility: private or work. No reply is represented
by a null value. A non-null reply must supply both text and visibility; a plain
text string or an omitted audience is invalid. The private activity summary is
not a reply and never supplies missing reply text or visibility.

A private reply becomes an ordinary message to the user for the current work.
A work reply becomes an ordinary message to the current work's shared
environment, bound to that exact work rather than every task in the environment.
The persona chooses the audience; participation does not force a work-visible
reply. Audience selection does not grant access to private sources or make
earlier private correspondence readable to peers.

Both forms remain subject to the same action limit, permissions, source
restrictions, continuity-dependent delivery, cancellation, freshness, journaled
retry and decision barriers as a directly authored message. Delivery follows
preceding synchronous actions and precedes an explicit wait; failure or an
asynchronous boundary can suppress it. A work reply derived from unavailable
private sources remains restricted unless an authorized source owner explicitly
changes the applicable policy. This affordance does not authorize a reply in a
mode that prohibits delivery, or establish the outcome of an unobserved action.

An optional notice delivered atomically with a submission also carries authored
text and an explicit private or work audience. A plain string does not choose an
audience. Work-visible submission content must not silently create private
correspondence merely because the author attaches a delivery notice. The notice
and submission either commit together or neither commits. A notice refers to
its submitted version; the submission does not inherit private notice content.
Explicitly reading a private notice still brings its source restrictions into
later work. Choosing a shared notice changes only that new message, never the
audience of earlier correspondence or private source material.

Delivery evidence identifies the successful delivery receipt and the exact
message or submission for the relevant work and intended audience. Review its
contents and referenced outputs: a success flag, an empty set of failed actions,
or a generic notice alone cannot establish that the requested result arrived.
Delivery, substantive correctness, scope fulfillment, and acceptance remain
separate judgments under the existing evidence rules.

| Observation | What it establishes |
|---|---|
| Correct answer only in private activity, followed by waiting | Computation may be correct; no delivered answer is established. |
| A delivery was attempted but failed | An attempted action and its failure, not a delivered result. |
| A successful delivery contains only part of the requested result | Delivery occurred; remaining obligations still require assessment. |
| A successful delivery contains the requested result | Evidence for delivery, not automatic quality approval or acceptance. |

Waiting can still be an appropriate dependency wait or voluntary yield. Do not
publish private summaries automatically, force another model call, or treat
every wait as an error. Preserve unmet obligations and the actual delivery
state. An evaluation that previously checked only operation success must retain
its old result and criteria, record the missing delivery evidence, and require
an explicit delivery audit before claiming task success. A guidance change or
synthetic regression is not proof of improved live delivery.

## What has not been established

A missing specification is an intake question. A missing authoring or analysis interface may be an implementation capability gap. An unrun campaign is an evidence gap. A true design gap requires showing that the existing rules omit or contradict necessary behavior; lack of a domain-specific example alone does not establish one.

The [task illustrations](../examples/5W-INVERTER-AND-CROSS-DOMAIN.md) and [delivery stress scenarios](../evaluation/DELIVERY-ACCEPTANCE.md) remain outside the runtime decision policy. They supply possible scopes and failure cases, not mandatory tool choices, team sizes, or execution orders. Assess actual outcomes and [unscripted organization](../evaluation/README.md#evaluating-emergent-organization) separately. This revision is not a circuit design, a running persona society, or evidence of universal task competence.
