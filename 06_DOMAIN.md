---
title: PersonaOS — Open Domain Context
status: Stable
---

# 06 — Domain Context

A domain is an independently signed, navigable context record authored under
exact authority. It is not a host classifier, profession, task router, prompt,
tool prescription, knowledge ranking, workflow stage, or completion rule.

This document is a clean break from domain-detection signals, probe phases,
promotion stages, trust/relevance scores, stage-weighted retrieval, fixed kind
families, top-K tool discovery, primary-domain semantics, and automatic domain
harvest.

## 1. Domain record

A current domain record contains only mechanical envelope data and bounded open
authored material:

- stable domain identity and signing authority;
- owner/curator principals where exact policy requires them;
- canonical open description and optional authored metadata;
- exact visibility, access, expiry, revocation, and supersession policy;
- content hash and byte length;
- exact source, evidence, lineage, and parent/related references; and
- complete bounded inventory references for any published knowledge, skills,
  tools, artifacts, policies, or other records.

The kernel verifies shape, signatures, authority, hashes, access, and lineage.
It does not interpret the description, decide whether the domain is real,
assign a profession, infer a role, or determine which records belong together.

## 2. Plural `domain_refs`

Task, environment, persona-authored identity/evolution, knowledge, skill, tool,
artifact, action, experience, and verifier records may carry zero, one, or many
exact signed `domain_refs`.

The array is unranked. There is no primary domain, automatic parent, most
specific domain, or host-selected canonical domain. Empty and cross-domain
records are valid.

A reference supplies navigable context only. It cannot:

- select or hide an action, memory, skill, tool, verifier, artifact, or member;
- assign a role, profession, expertise, team, or workflow;
- load or modify a prompt;
- derive capability-gap state, birth, wake, or acceptance rule; or
- establish truth, relevance, quality, safety, or completion.

Adapters and discovery carriers preserve the complete array and exact order as
signed, while consumers treat ordering as non-semantic.

## 3. Persona-authored domain evolution

A persona may author a new domain record, propose a revision, cite existing
domains, publish related material, communicate with other curators, or ignore
domain context. These are ordinary signed actions available alongside other
authorized actions.

There is no required recognition, probe, discovery, ingestion, inference,
proposal, curation, promotion, standardization, harvest, or deprecation phase.
The substrate does not create domain actions from task words, terminology
disagreement, missing skills, retrieval results, filenames, extensions, MIME,
regular expressions, embeddings, or model confidence.

Revisions use explicit immutable supersession. Concurrent alternatives remain
visible under their exact authorship and access policy; the kernel does not
merge their meanings or choose a winner.

## 4. Exact unranked domain inventories

A domain may publish bounded paginated inventories of exact record identities
and metadata. Every page binds snapshot identity, cursor, observed count,
truncation state, content hashes, authors, policy, and signatures.

Ordering is lexical, append, or another stable mechanical transport order only.
There is no trust, relevance, kinship, maturity, adoption, popularity, quality,
fitness, provenance, or stage score; no top-K; and no host recommendation.

Personas navigate inventories by explicit reference and ordinary actions. A
persona may search, inspect, contact an author, acquire or transfer a body,
invoke a tool, cite a record, author a derivative, or ignore it. The host does
not choose a path.

## 5. Tools and skills associated with domains

A domain record may cite exact signed tool or skill metadata. Association is
informational; it neither mounts a capability nor declares it required.

Tool descriptors retain their exact provider, schemas, effects, authority,
signatures, and receipts. Skill metadata retains owner, body hash/reference,
consent/transfer authority, interfaces, and provenance. Private bodies remain
sealed until exact access/consent permits delivery.

The persona chooses whether to inspect, communicate, acquire, provision,
author, invoke, or ignore a capability. The kernel performs no semantic match,
smoke-test phase, success-count promotion, class assignment, trust-score update,
or automatic retry. Exact action receipts establish only what ran and changed.

## 6. Knowledge and evidence

Domain-associated knowledge is ordinary signed knowledge as defined in
[`08_KNOWLEDGE.md`](08_KNOWLEDGE.md). References preserve exact authorship,
scope, content hash, evidence, derivation, revocation, and supersession.

The substrate does not rank knowledge by a domain stage, decay a record because
of a domain state, compute provenance or confidence, automatically consolidate
it, or inject it into model context. Personas choose which exact records to
navigate to and how to interpret them.

An authored domain description or citation is not a verified fact. Any
principal/verifier acceptance must name its own exact authority and evidence.

## 7. Kind and format openness

Open persona-authored labels may describe artifact kinds, capability kinds,
knowledge kinds, or other concepts. The kernel treats them as opaque identifiers
unless an exact descriptor separately declares mechanical behavior.

Artifact MIME is always explicit in the artifact signature and bound to exact
bytes. A domain label or kind registry does not supply MIME, renderer, artifact
role, edit semantics, verifier, or storage authority by inference.

Mechanical descriptors may explicitly cite reusable parser, renderer, edit,
verification, or tool interfaces. Their exact schemas and effects—not their
names or domain association—supply authority.

## 8. Safety and policy

Domain records cannot weaken the kernel safety floor, access controls,
ReplicationBound, user consent, workspace isolation, or external/physical
authority. An exact authorized policy may add constraints for records or
actions in its declared scope.

Policy application follows exact signed scope and effect declarations. The
kernel never assigns policy by semantically classifying a task into a domain.
If no exact binding exists, the domain policy does not apply by inference.

## 9. Discovery and federation

Public or peer discovery may expose visibility-authorized signed domain records
and compact inventories. Location is not authority. Consumers independently
verify signature chain, current key, policy, expiry, revocation, content hash,
and subject binding.

Discovery is incremental and unranked. Direct/local/P2P routes are primary; an
HTTP locator is last-resort only. A remote record does not become locally
trusted, executable, or prompt-visible merely because it was discovered.

## 10. Domain context in a persona wake

An ordinary wake may include exact domain identities referenced by current
task/environment/artifact/knowledge records and the exact inventory cursors
needed to navigate further. It does not include a host-authored domain summary,
primary-domain selection, action recommendation, profession, role, phase, or
tool requirement.

The complete ordinary action catalog remains available. Missing, unfamiliar,
multiple, disputed, or absent domain context never narrows cognition or creates
an automatic model call.

## 11. Human presentation

Interfaces label domain material by exact authored name/description, authorship,
scope, signature status, freshness, related references, and access. They do not
show a trust/quality score, imply standardization, or present one referenced
domain as primary unless exact authenticated user intent explicitly asks for
that presentation preference.

## 12. Removed compatibility surface

There is no live compatibility for domain stages, trust or relevance scores,
probe records/phases, domain classifiers, domain-unknown triggers, top-K/stage-
weighted retrieval, DiscoveredTool promotion classes, automatic domain harvest,
MetaRegistry promotion, fixed kind families, kinship scoring, singular
`domain_id` selection, or primary-domain completion hooks. Historical bytes may
remain opaque audit records but confer no current selection or policy authority.

Clean-break implementation means those concepts are absent from current domain
storage, hydration, kernel calls, action descriptors, prompt construction,
discovery projection, and public task state—not merely disabled by a flag or
wrapped by a generic name. A current domain manager stores and verifies open
records, exact material, plural references, and mechanical access/lineage only.
It exposes no stage transition, trust update, requirement derivation, probe,
harvest, promotion, or semantic registry method for another live subsystem to
call.

A store carrying an obsolete semantic-policy schema is not migrated or coerced
into current cognition. It fails current-mode admission. If retained for audit,
its bytes remain in a separate opaque historical surface and never populate a
domain object, action catalogue, prompt carrier, policy decision, ranking, or
completion projection.

## 13. Design criteria

1. Domain context is optional, exact, signed, and open.
2. Eligible records carry plural unranked `domain_refs`.
3. No domain is primary by substrate interpretation.
4. Inventories are complete within explicit pagination bounds and unranked.
5. Personas navigate domain knowledge, skills, and tools explicitly.
6. Domain labels never select behavior, policy, MIME, roles, teams, or
   completion.
7. Removed semantic domain engines have no live storage, hydration, call, or
   prompt path; historical bytes remain audit-only.
