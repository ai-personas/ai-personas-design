---
title: PersonaOS — Artifacts and Rendering
status: Stable
---

# 07 — Artifacts

An artifact is exact produced media with signed identity, byte authority, role,
scope, and provenance. The substrate does not prescribe artifact kinds,
packages, filenames, workflows, reviews, verification stages, or lifecycle
transitions.

This document is a clean break from fixed bundle recipes, media-kind seeds,
verifier cascades, draft/review/verified/accepted FSMs, required test stages,
panel gates, standardized co-editing patterns, and completion-by-artifact state.

## 1. Exact artifact declaration

Every current artifact declaration binds:

- stable artifact identity and optional bundle/package reference;
- exact owner, author, environment, task, action, and workspace provenance;
- exact filename/path as storage identity and optional authored display title;
- required normalized parameter-free signed `mime_type`;
- exact content hash and byte length;
- exact content locator or inline/body reference;
- open persona-authored artifact role;
- zero or more exact signed unranked `domain_refs`;
- exact predecessor/supersession/derivation references where present;
- access, visibility, expiry, and revocation authority; and
- signing-key identity and signature.

The signature covers MIME, hash, length, owner/scope, role, domain references,
and provenance. A changed byte body, MIME, role, or scope is a new signed
revision—not presentation metadata.

## 2. Explicit signed MIME

`mime_type` is the authoritative format declaration bound to exact bytes. The
kernel verifies hash and length before publication, transfer, parsing, or
rendering.

Filename, extension, path, an open media-kind label, domain association, prompt,
model prose, and byte sniffing cannot supply or replace MIME authority. Safe
byte inspection may detect inconsistency and refuse parsing or select a
conservative download/technical fallback.

MIME declares format, not semantic quality, artifact role, authorship,
professional sufficiency, or completion.

A verified declaration remains authoritative for its exact bytes across later
task amendments or continuations while persona, environment, path, content
hash, and byte length are unchanged and its access authority remains valid. Its
signed task/action fields continue to identify the original publication
provenance; a newer current task identifier does not erase that MIME evidence.
Changed bytes require a new matching signed declaration and never inherit an
older declaration by path or extension.

## 3. Open roles, kinds, and bundles

Artifact roles, kind labels, bundle descriptions, relationships, and package
structure are bounded open persona-authored records. Personas may group related
files, describe dependencies, designate a primary view, cite a source model,
publish derivatives, or leave artifacts unbundled.

The substrate reserves no role such as primary, supporting, verification report,
test plan, drawing, CAD, review, or deliverable. If authored, those labels remain
claims. The kernel does not choose a package recipe from task/domain words,
filename, extension, MIME, executable, profession, prompt, or regular expression.

Identity media and task artifacts remain separate only through exact signed role
and scope authority. A portrait is never counted or shown as task output merely
because it shares a workspace.

## 4. Persona-authored creation and tools

Personas choose whether to create an artifact, which format to use, which tool
or skill to acquire/invoke, how to structure files, and whether to derive or
render further views. The ordinary action catalog and exact unranked capability
inventories make these choices reachable.

Each actual tool/action receipt records exact descriptor/provider, terminal
result, byte effects, and causal provenance. Invoking Blender, OpenSCAD, a CAD
tool, renderer, compiler, converter, or verifier does not automatically establish
quality, expertise, artifact role, or completion.

Directly model-authored, code-generated, converted, compiled, and externally
realized bytes remain distinguishable when the signed action chain establishes
that provenance.

## 5. Revisions, concurrent edits, and conflicts

Artifact revisions are immutable signed records linked explicitly to exact
predecessors. Personas may use any authorized edit/merge tool or protocol.
The substrate does not mandate CRDT classes, merge algorithms, review rounds,
or co-editing team patterns.

Concurrent changes preserve exact alternatives and authorship. A safe exact
mechanical merge may be declared by an authorized action descriptor. Otherwise
conflict remains visible until an authorized persona-authored signed resolution
chooses or synthesizes bytes.

No filename, MIME, role, domain label, or host recipe decides a semantic merge.

## 6. Optional review and verification evidence

Personas may author reviews, measurements, calculations, tool checks,
comparisons, or other evidence and cite exact artifact revisions. An authorized
verifier may issue a signed receipt whose authority, descriptor, exact input
hashes, result, and effects are independently verified.

There is no universal verifier cascade, required stage order, test suite,
panel, peer-review round, threshold, score, or artifact-state transition. A
principal may explicitly require particular evidence in authenticated task
intent; that task-specific authority remains exact and is not generalized into
the kernel.

A review or tool receipt proves only its exact authorship and mechanical result.
It does not become objective acceptance unless the principal explicitly granted
that verifier acceptance authority.

## 7. Human-facing names and format presentation

The exact full path remains the storage, fetch, routing, and verification
identity. The UI derives a separate non-authoritative presentation:

- readable basename/title as the primary label;
- a large, high-contrast, always-visible format badge from verified signed MIME
  (with exact extension shown separately when present);
- a short parent-folder breadcrumb;
- full filename/path and technical integrity details on demand; and
- clear author, role claim, provenance, freshness, and byte status.

The extension must remain easy to see without scanning a long path, but it is
never format authority. Presentation grouping may follow exact authenticated
user preferences or persona-authored bundle metadata. The UI does not hard-code
CAD-first, document-first, role-based, or task-specific grouping as substrate
meaning.

## 8. Lazy format-aware rendering

Artifact list hydration is lightweight. Bytes and renderer code load only when
a person opens an artifact. The renderer verifies access, signature, hash,
length, and signed MIME before parsing.

A renderer registry may support text, Markdown, source, structured data,
raster/vector images, PDF/office documents, archives, audio/video, meshes,
point clouds, CAD/BIM, and other formats. Registry entries are mechanical MIME/
interface declarations, not domain or task knowledge.

Supported verified content receives the richest safe local view available.
Unknown, malformed, mismatched, or unsupported content receives an honest
bounded technical inspector and intact download. The UI never presents a
generic unexplained “binary” view when a verified supported renderer exists.

Archive inspection remains bounded and does not execute content. Heavy parser
and viewer dependencies load lazily.

## 9. Discovery, storage, and replicas

Artifact discovery cards expose only exact visibility-authorized signed
metadata, content hash, length, MIME, role claim, owner/scope, and locators.
Discovery does not grant read/write access or establish artifact quality.

Bytes may remain local or in an authorized provider/replica. Every fetched body
must match exact signed hash and length. Credentials stay outside public cards;
consumers use their own authorized access.

Cache and replication cannot extend expiry, visibility, or authority. A stale
locator or mismatch fails closed and remains visible as a technical failure.

## 10. Plural domain references

Artifacts may cite zero or more exact signed `domain_refs`. The array is
unranked and has no primary domain. References support persona navigation only;
they do not choose MIME, renderer, tool, verifier, package role, review process,
or completion.

## 11. Objective acceptance and quiescence

Artifact existence, count, MIME, filename, tool provenance, review, successful
check, score, unchanged bytes, or bundle label does not complete a task.
Acceptance comes only from exact authenticated principal or explicitly
authorized verifier authority bound to current evidence.

No pending artifact-related causal event means quiescent, not accepted,
verified, delivered, shipped, complete, or incapable of further improvement.

## 12. Removed compatibility surface

There is no live compatibility for artifact/bundle lifecycle FSMs, required
verifier stages, verifier cascades, candidate/panel states, tests-pass gates,
fixed bundle-kind recipes, fixed media-kind seeds, required peer review,
standardized CRDT/co-editing patterns, extension-derived MIME, implicit access,
or backward-compatible absent owner/policy semantics. Historical records may
remain opaque audit bytes but confer no current format, workflow, or acceptance
authority.

## 13. Design criteria

1. Every artifact has exact signed byte, MIME, role, owner, scope, and
   provenance authority.
2. Artifact kinds, packages, creation methods, reviews, and evidence are
   persona-authored choices.
3. No universal lifecycle, verifier, test, panel, or co-editing workflow exists.
4. Filenames and extensions are human-useful but non-authoritative.
5. Renderers are safe, format-aware, and lazy.
6. Domain references are plural and non-semantic to the kernel.
7. Artifact state never substitutes for objective acceptance.
8. An unchanged exact byte revision retains valid signed format provenance
   across task continuation; changed bytes require new signed authority.
