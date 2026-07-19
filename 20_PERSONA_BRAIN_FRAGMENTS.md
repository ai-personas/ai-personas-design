---
title: PersonaOS v1.0 Addendum - Persona Brain Fragments and Active Agent Specs
status: Proposed
audience: [implementers, memory engineers, prompt engineers, research]
normative: partially
---

# 20 - Persona Brain Fragments and Active Agent Specs

This addendum defines the mutable prompt-learning substrate for personas. The
problem it addresses is narrow but load-bearing: PersonaOS can record experience,
but recorded experience does not reliably become active future behavior unless it
is retrieved, compiled, used, evaluated, and revised.

The substrate must not hardcode domains, artifact contracts, tool choices, or
task-specific rules. Learned behavior belongs to the persona. The runtime stores,
signs, retrieves, logs, reviews, and rolls back.

## 1. Problem

Flat memories and prompt notes are passive. They can preserve a lesson, but they
do not guarantee that the lesson reaches the next model call in the right form.
For long-lived personas, this creates the wrong learning shape: a persona may
observe repeated failures or opportunities, but still act as if those experiences
never happened.

The missing mechanism is an active compile path:

1. store persona-authored operating fragments;
2. retrieve the relevant fragments for the current situation;
3. compile them into a per-turn agentic operating spec;
4. log which fragments influenced behavior;
5. update fragments from evidence after the turn.

## 2. Core Records

`brain-fragment/1` is the durable source of truth. Each fragment is a small
persona-owned agentic instruction. Runtime-owned fields are limited to identity,
versioning, status, signatures, timestamps, lineage, and usage counters.
Persona-owned fields include:

- `body`;
- `activation_cues`;
- `deactivation_cues`;
- `labels`;
- `links`;
- `evidence_refs`;
- `source_refs`;
- `affordance_refs`;
- `change_summary`.

`situation-capsule/1` is the neutral state packet used for compile: task text,
environment id, phase, active pathway/mode, artifact refs, peer refs, available
affordance refs, pressure refs, failure refs, resume refs, and budget refs.

`active-agent-spec/1` is the per-turn operating spec compiled from selected
fragments. Its active prompt material is the selected persona-authored fragment
text. The substrate may record selected fragment ids, hashes, timestamps, and
opaque section metadata, but it must not impose fixed prompt sections or a
runtime-owned behavioral taxonomy. If a persona wants recurring operating
concepts, it authors them inside its own fragments.

`brain-compile/1` records the situation hash, candidate fragment ids, selected
fragment ids, active spec hash, and timestamp.

`brain-edit-proposal/1`, `brain-review/1`, and `brain-promotion/1` record the
evidence-backed edit lifecycle.

## 3. BrainCompile

BrainCompile runs before a meaningful persona model call. It must not send the
whole brain to the model. It builds candidates through bounded retrieval:

- hard filters: owning persona or allowed lineage, active status, valid
  signature, readable scope;
- semantic retrieval over persona-authored fragment material;
- hot-set retrieval from the current environment;
- artifact, tool, MCP, skill, pressure, and failure refs;
- bounded one-hop or two-hop expansion over persona-authored links;
- utility prior from helped/hurt counts;
- diversity selection to avoid duplicate fragments.

The selected fragments are compiled into `active-agent-spec/1`. The runtime may
join or frame selected persona-authored bodies, but it must not create prompt
instructions, domain-specific instructions, artifact requirements, tool choices,
or fixed behavioral categories. The compile record is persisted so later success
or failure can credit the selected fragments.

## 4. BrainEdit

Durable fragment edits happen only at evidence boundaries, such as user feedback,
verifier result, artifact diff, tool trace, peer critique, failure, accepted
progress, pause/resume, or budget exhaustion.

BrainEdit proposals may create, update, split, merge, retire, link, unlink, or
adjust fragment cues and refs. A proposal must cite evidence and describe an
operational change. Vague updates that do not affect future behavior are not
promoted.

BrainReview checks that the proposal is evidence-grounded, preserves frozen
identity, never deletes signed pressure lineage, and does not claim unavailable
tools or MCPs as available. The latest persona-signed pressure appraisal is the
current snapshot: omission retires an item from current pressure but never erases
the prior appraisal, evidence refs, or learning history. Closure evidence may
explain that retirement, but the runtime does not require count-matched closure
records or revive historical pressure as a readiness gate. Accepted proposals are
promoted as signed fragment versions; rejected proposals remain auditable.

## 5. Tools, MCP, Skills

Available tools, MCP servers, command affordances, and learned skills are exposed
to BrainCompile as neutral capability manifests. Fragments may reference those
capabilities through `affordance_refs`, but the persona decides whether to
inspect, use, provision, register, or ignore them.

Tool success and failure traces feed back into BrainEdit, allowing personas to
learn when a capability helped or hurt.

## 6. Empty By Default

A new persona brain starts with no runtime-authored prompt fragments. Contexts,
episodes, traces, peer messages, artifacts, tool receipts, and feedback are
evidence. They do not become active prompt fragments unless a persona proposes
or applies a fragment edit through the signed brain tools.

This avoids the bootstrap trap where the substrate appears to "teach" the
persona by preloading fixed lessons. The substrate exposes records and edit
mechanics; the persona decides what, if anything, should become reusable prompt
material.

The repository must not ship a default fragment library, domain fragment set,
tool-use fragment set, or task-specific starter fragments. Examples in tests or
design prose are illustrative fixtures only; they are not initial state. Runtime
code may create empty signed storage, retrieval indexes, compile records, and
tool schemas, but it must not author fragment bodies, activation cues,
deactivation cues, labels, or prompt sections on behalf of the persona.

## 7. Risks and Controls

| Risk | Control |
|---|---|
| Prompt drift | Signed versions, reviews, rollback. |
| Generic self-improvement fluff | Require operational edits with evidence refs. |
| Memory bloat | Split, merge, retire, utility counters, bounded retrieval. |
| Retrieval miss | Combine lexical, semantic, hot-set, link, and utility retrieval. |
| Tool hallucination | Only runtime capability manifests count as available. |
| Overfitting | Promote risky edits only after review or repeated evidence. |
| Conflicting fragments | Preserve links and expose conflicts during compile. |

## 8. Tests

- fragment signing, hash lineage, retirement, rollback, and stale index rebuild;
- retrieval over large fragment sets without full-brain model scans;
- BrainCompile shape, activation logging, and active-spec prompt injection;
- BrainEdit rejection for evidence-free, vague, identity-mutating, or
  unavailable-tool edits;
- integration where evidence from one run changes future active prompt behavior;
- substrate-purity regression: no domain words, artifact contracts, tool gates,
  or task-specific regexes in runtime logic.
