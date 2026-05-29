---
title: PersonaOS v1.0 — Specification Conventions
status: Stable
---

# Specification Conventions

> **Reader guide.** This is the style guide for v1.0 spec documents — how they are formatted, how normative language works, and how schemas and cross-references are written. Read this if you are *writing or reviewing* v1.0 docs. Skip it if you are only *reading* the spec — the conventions are applied consistently, so you can absorb them by example. **No prerequisites.**

This document defines the formatting, normative-language, and structural conventions that all v1.0 design documents (`00_VISION.md` … `13_DESIGN_VALIDATION.md`) follow. It is itself non-normative for system behaviour but **normative for documentation** — any v1.0 design document that diverges from these conventions is a documentation defect.

## 1. Front matter

Every v1.0 design document MUST begin with a YAML front-matter block:

```yaml
---
title: <Document Title>
status: <Draft | Proposed | Stable | Living | Superseded>
version: <semver — matches v1.0 release line, e.g. 1.0.4>
date: <ISO 8601, YYYY-MM-DD>
authors: [<list>]
reviewers: [<list>]
audience: [<one or more values from §1.3>]
normative: <true | false | partially | documentation>
supersedes: <optional — list of files / sections this replaces>
depends_on: <optional — list of files that MUST be read first>
---
```

### 1.1 `status` values

| Value | Meaning |
|---|---|
| Draft | Under active authorship; expect changes. |
| Proposed | Complete; awaiting review. |
| Stable | Reviewed and accepted; changes require version bump. |
| Living | Append-only catalog / validation log; entries accrete without supersession. Used only for `13_DESIGN_VALIDATION.md`. |
| Superseded | Replaced; consult `supersedes` reverse link in successor. |

### 1.2 `normative` values

| Value | Meaning |
|---|---|
| true | Document defines behaviour that implementers MUST follow. |
| false | Document informs without binding (e.g. `README.md`, `13_DESIGN_VALIDATION.md`). |
| partially | Document has both normative claims and non-normative narrative; normative status is declared per section in `## 0. Status & scope`. Examples: `00_VISION.md` (invariants normative; narrative not), removed. |
| documentation | Document binds documentation form, not runtime behaviour (e.g. this file, `12_GLOSSARY.md`). Implementers do not derive runtime obligations from it. |

### 1.3 `audience` values (registered set)

The audience field MUST list one or more values from the registered set below. New audience tokens are added by amending this section.

| Value | Description |
|---|---|
| implementers | Engineers building the kernel, persona body framework, or adapters. |
| reviewers | Internal architecture/design reviewers. |
| auditors | External or compliance auditors. |
| operators | Deployment owners, SREs, those setting deployment policy. |
| research | Researchers studying or building on PersonaOS. |
| persona authors | Authors of `SOUL.md` files and persona-seed contributors. |
| project leads | Owners of project-workspace environments. |
| environment authors | Authors of `EnvironmentBlueprint` instances. |
| domain curators | Holders of the `DomainCurator` role; gate domain promotion. |
| artifact authors | Authors producing artifacts under verifier recipes. |
| memory engineers | Engineers tuning memory tiers, retrieval, consolidation. |
| prompt engineers | Authors tuning DSPy programs, MetaPrompts, GEPA pipelines. |
| integrators | Engineers wiring v1.0 into Claude Code / OpenAI SDK / LangGraph / etc. |
| security auditors | Auditors specifically reviewing key custody, signing, threat model. |
| planners | Release and capacity planners. |
| QA | Test engineers, acceptance-test authors. |
| all | Use only on entry / navigation / glossary documents. |

## 2. Normative language (RFC 2119 / RFC 8174)

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** in v1.0 documents are to be interpreted as described in [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174), **only when they appear in ALL CAPS** (or are bolded in tables for legibility).

When a word appears in lowercase ("should", "may"), it carries its ordinary English sense, not the normative force.

Rules:

- A normative claim MUST be expressed with the appropriate RFC 2119 keyword, not as a passive imperative or paraphrase.
- Each document with normative content MUST cite this section in its front matter or first body paragraph.
- Non-normative narrative (rationale, examples, history) MUST use lowercase forms.

## 3. Section structure

All documents (except `README.md`, `SPEC_CONVENTIONS.md` (this file), `12_GLOSSARY.md`, `13_DESIGN_VALIDATION.md`, and `14_DECISIONS.md`) MUST carry the three **bookend sections** and SHOULD carry the full ten-section skeleton below. The five exempt documents are entry-point / convention / catalog artefacts whose own structures (a reading-order index, a numbered convention list, an A-Z glossary, an append-only scenario catalog, an append-only ADR catalog) carry no normative behavioural claims that need a §0 scope, a risks table, or open-question tracking; their conformance is judged against the inherent shape of their genre, not §3.1.

### 3.1 Required bookends

Every normative v1.0 document MUST include the three bookend sections below. The integer prefix in the actual heading is per-document and reflects the document's own section numbering (e.g. `## 12. Risks & known limitations` in `01_KERNEL.md`, `## 27. Risks & known limitations` in `04_PROJECT.md`); the "Topic" column lists the canonical heading text without its prefix.

| Topic (heading text after the integer prefix) | Required position | Purpose |
|---|---|---|
| `Status & scope` | `## 0.` (always) | Front-matter recap; in-scope / out-of-scope statements; supersession notes; declaration of any deviation from §3.2. |
| `Risks & known limitations` | Any integer-numbered H2 at §7 or later | The six-column table prescribed in §7. |
| `Open questions` | Any integer-numbered H2 at §8 or later (lowercase letter-suffix permitted per §3.4 Pattern A) | Listed open questions with `OQ-<doc>-<n>` IDs per §8. |

A normative document that omits any bookend is non-conformant.

### 3.2 Recommended ten-section skeleton

```
# <Number> — <Title>            (H1 once; matches front-matter title)

## 0. Status & scope            (REQUIRED — front-matter recap + scope + deviation notes)

## 1. Background                (why this exists; prior versions; problem)

## 2. Goals / Non-Goals         (what this MUST achieve; what it explicitly does not)

## 3. Definitions               (terms used here; cross-link to glossary)

## 4. Normative specification   (the substance — invariants, schemas, FSMs, protocols)

## 5. Worked examples           (illustrative; non-normative)

## 6. Open questions            (REQUIRED — known unknowns with OQ IDs)

## 7. Risks & known limitations (REQUIRED — severity-rated 6-column table)

## 8. Acceptance tests          (cross-link to 11_ACCEPTANCE_TESTS.md)

## 9. Cross-references          (related v1.0 docs; deprecated terms; ancestor versions)
```

### 3.3 Compressed opening (permitted)

A document MAY fold §1 Background, §2 Goals / Non-Goals, and §3 Definitions into a single combined opening section, provided that:

1. `## 0. Status & scope` remains as a standalone section.
2. The compressed opening is titled `## 1. <Topic> in v1.0` or equivalent and explicitly carries Background, Goals, and Definitions material.
3. `## 0. Status & scope` documents the deviation with a one-line note (e.g. "Background / Goals / Definitions are folded into §1; cross-link to [`12_GLOSSARY.md`](12_GLOSSARY.md) covers definitions.").
4. Risks (§7) and Open Questions (§6) bookends remain as standalone sections.

This deviation reflects the v1.0 corpus reality: most normative docs are reference manuals, not Background/Goals essays. The compressed opening is conformant; the ten-section form remains the gold standard.

### 3.4 Heading numbering

H2 headings primarily use integer numbering (`## 1.`, `## 2.`, …). Letter-suffix H2 numbering (`## 11a.`, `## 3A.`, …) is permitted under two specific patterns and forbidden otherwise.

**Pattern A — patch-level insertion (lowercase suffix `a, b, c, …`)**

Used when a new H2 section is inserted into a previously published document within a minor-version line, where renumbering the following sections would invalidate cross-document references. Example: `## 26a. External participants and physical assets` was inserted into `04_PROJECT.md`without renumbering `## 27`.

Rules:

1. The letter-suffix heading is a peer of the preceding integer heading in scope (same H2 level).

3. Letter ordering is `a, b, c, …` immediately after the integer (no skipping).
4. New top-level sections in a major or minor revision MUST use the next integer, not a lowercase suffix.

**Pattern B — structural pillars (uppercase suffix `A, B, C, …`)**

Used when a numbered parent section has 3+ peer pillars that share a unifying theme but exceed what `###` nesting can carry without deep H3 chains. Example: `## 3A.` … `## 3E.` in `09_PROTOCOLS.md` decompose the §3 federation topic into five federation pillars.

Rules:

1. Uppercase suffix is admissible only when the parent H2 (e.g. `## 3.`) is itself a meaningful integer-numbered section that introduces the theme.
2. All pillars under one parent SHOULD be uppercase-suffixed (no mixing `3A` with `## 4.` peer-style ungrouped headings).
3. Lowercase patch-insertion suffixes (Pattern A) MAY co-exist with Pattern B pillars (e.g. `## 3F.` as a patch addition to the federation pillar family).

**Forbidden patterns**: Mixed-case (`## 11Ab.`), numeric-letter chains (`## 11a1.`), arbitrary alphabetic ordering (`## 11x.`).

Pre-existing letter-suffix sections in the v1.0 corpus are conformant under one of these patterns:

| Section | Pattern | File |
|---|---|---|
| `## 8a-d.`, `## 9a-d.`, `## 9e.`, `## 9f.` | A (acceptance-test patch insertions; §9e/§9f added in v1.0.4 for Risks/OQ bookends) | `11_ACCEPTANCE_TESTS.md` |
| `## 13a.` | A (inserted section) | `01_KERNEL.md` |
| `## 13a.` DomainHarvest, `## 21a.` Open questions | A (inserted sections) | `06_DOMAIN.md` |
| `## 11a.` ApprovalWorkflow, `## 26a.`, `## 27a.` Open questions | A (v1.0 additions to project + OQ bookend) | `04_PROJECT.md` |
| `## 11a.` Alert, `## 11b.`, `## 12a-c.`, `## 19a.` Open questions | A (inserted sections) | `05_ENVIRONMENT.md` |
| `## 16a.` MeasurementFact + UncertaintyEnvelope, `## 18a.` Open questions | A (inserted section) | `08_KNOWLEDGE.md` |
| `## 13a.` Open questions | A (OQ bookend added in v1.0.4 without renumbering the §13 acceptance/test sections) | `02_PERSONA.md` |
| `## 9a.` Open questions | A (OQ bookend added in v1.0.4 without renumbering §9 acceptance tests) | `03_TASKS.md` |
| `## 16a.` Open questions | A (OQ bookend added in v1.0.4 without renumbering §16 acceptance tests) | `07_ARTIFACTS.md` |
| `## 3A-E.` federation pillars, `## 10a.` Open questions | B (federation pillars under §3) + A (OQ bookend) | `09_PROTOCOLS.md` |

The recurring `## Na. Open questions` insertion is Pattern A: in v1.0.4 the OQ bookend (§3.1) was retro-fitted across the eight normative docs that already had an integer-numbered "Acceptance tests" or equivalent terminal section. Renumbering would have invalidated outbound cross-references from `11_ACCEPTANCE_TESTS.md` and others; the lowercase-suffix insertion preserves the existing anchors. Future minor revisions SHOULD prefer integer numbering when adding new terminal sections.

### 3.5 Sub-section nesting

Sub-sections use `##` (top-level), `###` (one nesting), `####` (rare; only where structurally necessary). Documents that need deeper nesting (e.g. `06_DOMAIN.md`) MAY use H5/H6 but SHOULD prefer breaking the section into a numbered child.

## 4. Schemas

All schemas in v1.0 MUST be expressed in **one** of three canonical forms:

1. **Python `@dataclass`** (preferred for kernel-side entities; reflects the reference implementation).
2. **JSON Schema** (preferred for wire-format and inter-agent contracts).
3. **TypeScript `interface`** (acceptable for protocol payloads where TS is idiomatic).

The form is implied by the code-fence language (`python`, `json`, `typescript`) and explicitly stated in the registry's `Form` column ([`09_PROTOCOLS.md §7`](09_PROTOCOLS.md#7-schema-registry)).

Each schema declaration MUST include:

- A **`schema` field** carrying a version string of the form `<name>/<integer>` (e.g. `schema: str = "soul-state/6"`, `"schema": "domain-context/2"`). The field name is `schema` (not `schema_version`); the value carries both the registry name and the integer version.
- A one-line purpose statement immediately above or below the schema block (markdown prose; not part of the schema itself).
- A list of fields with type + units + nullability.
- Cross-reference to the doc section that defines its lifecycle (where applicable).

### 4.1 Per-form rules

| Form | Required shape of the `schema` field |
|---|---|
| Python `@dataclass` | One of the two forms below (§4.2). |
| JSON Schema instance | A `"schema": "<name>/<n>"` property in the document. |
| TypeScript `interface` | `readonly schema: "<name>/<n>";`. |

### 4.2 Python `@dataclass` schema-field forms

Two forms are conformant; authors MAY choose either per schema, but SHOULD NOT mix forms within a single schema. The choice has no runtime semantics — both produce the same wire payload — but each carries different ergonomic trade-offs:

**Form A — default-valued literal field (used throughout the v1.0 corpus for hand-written kernel entities):**

```python
@dataclass(kw_only=True)
class SoulState:
    schema: str = "soul-state/6"
    # ...required and optional fields below...
```

When using Form A together with non-defaulted (required) fields, the dataclass MUST be declared with `@dataclass(kw_only=True)` so that `schema` (which has a default) may precede required-without-default fields without violating Python's "non-default arg follows default arg" rule. The default value of `schema` is a constant string; instances MUST NOT override it.

**Form B — type-only `Literal` annotation (RECOMMENDED for generated wire-format types and tagged unions):**

```python
@dataclass
class DomainContext:
    schema: Literal["domain-context/2"]
    # ...required and optional fields below...
```

Form B is preferred when the schema string is treated as a discriminant for static-type narrowing (e.g. `Union[SchemaA, SchemaB]` tagged on `schema`). Form B does not constrain field ordering, since the annotation has no default value.

**Snippet convention.** Schema declarations throughout the v1.0 corpus are illustrative pseudo-Python — the snippets describe the *shape* of each entity, not its literal implementation. Authors typeset Form A snippets with the bare `@dataclass` decorator for visual brevity; an implementer translating any Form A snippet into executable Python MUST add `kw_only=True` (or restructure to place defaulted fields after non-defaulted ones) to satisfy Python's argument-ordering rule. Form B snippets translate verbatim.

Either form satisfies the §4 "`schema` field" requirement. INV-10 (in [`00_VISION.md §4`](00_VISION.md#4-inherited-kernel-invariants-inv-1inv-10)) enforces that the kernel MUST refuse any message whose `schema` value is not registered in [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md#7-schema-registry).

### 4.3 Schema scope

The `schema` field is REQUIRED on every entity that crosses a process, signing, or persistence boundary — i.e. anything that lands on the wire (A2A / MCP / blackboard / queue), in a signed lineage event, or in a long-lived store (memory tiers, soul.state.json, ProjectLineage). Internal kernel value-types that exist only within a single in-process call (e.g. transient FSM-state containers like `Candidate`, evaluator return types, stack-allocated record types) are exempt and MAY omit the field; such types MUST NOT appear in [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md#7-schema-registry).

### 4.4 Schema registry

Schema version registry: see [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md#7-schema-registry) for the master table. Adding or modifying a schema MUST be accompanied by a registry entry per [`09_PROTOCOLS.md §7.13`](09_PROTOCOLS.md#713-adding-or-modifying-schemas).

## 5. Diagrams

Diagrams MAY be:

- **Monospaced ASCII** (current v1.0 default; portable, diff-friendly).
- **Mermaid** (RECOMMENDED for new sequence diagrams, state machines, and flowcharts; renders in GitHub).

### 5.1 Captioning

Captioning requirements depend on diagram form:

| Form | Caption requirement |
|---|---|
| Mermaid | MUST carry a caption of the form `Figure N.M — <description>.` immediately below the diagram. Figure numbering resets per document. |
| Monospaced ASCII | A preceding H3/H4 heading (e.g. `### Safety floor sources`) or an inline bold lead-in (e.g. **Safety floor sources.**) is sufficient identification; a `Figure N.M — <description>.` caption is OPTIONAL but RECOMMENDED for diagrams cross-referenced from another section. The heading-only form is the conformant default for the v1.0 corpus. |

A diagram referenced by `Figure N.M` from anywhere in the same document MUST carry the matching `Figure N.M — <description>.` caption verbatim, regardless of form.

### 5.2 Diagram fidelity

Diagrams are normative for the relationships they depict (state transitions, message sequences, layering). When a diagram and the surrounding prose conflict, the prose is authoritative and the diagram is a documentation defect to be corrected. Authors SHOULD prefer Mermaid for any new FSM or sequence whose transitions exceed what an ASCII box-and-arrow can carry without ambiguity.

## 6. Cross-references

### 6.1 In-repo cross-reference forms

In-repo cross-references MUST use one of the following forms:

| Form | When to use |
|---|---|
| **Anchored** — `` [`<file>.md §<section>`](<file>.md#<anchor>) `` | Inline prose references that the reader follows. The anchor lets the reader jump straight to the section. REQUIRED for prose. |
| **Visible-only** — `` [`<file>.md §<section>`](<file>.md) `` | Tabular registry cells (e.g. schema registry "Defined in" column) and cross-reference indexes where the visible `§<section>` identifies the target and the link points to the document root. PERMITTED. |
| **Document-only** — `` [`<file>.md`](<file>.md) `` | Top-level "see also" references where no specific section is named. PERMITTED. |

Mixed forms (visible text names a section but the URL has neither anchor nor visible match) are non-conformant.

### 6.2 Anchor format

Section anchors are auto-generated from headings by GitHub-flavoured Markdown; use lowercase, hyphenated form (e.g. `## 2.4 Principal collapse` → `#24-principal-collapse`). Letter-suffix headings (e.g. `## 11a. Alert`) generate anchors of the form `#11a-alert-first-class-attention-primitive-v1.0-additions`.

### 6.3 External references

External references (papers, RFCs, standards) MUST include either a stable URL or a DOI. Cited papers SHOULD also appear in the bibliography of `00_VISION.md` or `09_PROTOCOLS.md`.

## 7. Risks & known limitations

Each normative document MUST include a `## Risks & known limitations` section, expressed as a table:

| ID | Risk | Severity | Likelihood | Mitigation | Target release |
|----|------|----------|------------|------------|----------------|

Severity values: **Critical** (data loss / safety floor bypass / identity compromise), **High** (incorrect acceptance verdict / lineage gap), **Medium** (degraded performance / poor UX), **Low** (cosmetic / debt).

Cross-document risks (those that touch ≥2 documents) MUST also appear in a root risk register at [`00_VISION.md §11`](00_VISION.md#11-risks--known-limitations).

## 8. Open questions

Open questions MUST be tracked inline in the relevant document under `## Open questions`, each with an ID `OQ-<doc>-<n>` (e.g. `OQ-DOMAIN-3`). Closing an open question requires either resolving it in a subsequent revision or moving it to risks.

## 9. Acceptance test linkage

Every normative claim that has a corresponding acceptance test MUST cross-reference the test by ID. Test IDs follow the schema in [`11_ACCEPTANCE_TESTS.md §2`](11_ACCEPTANCE_TESTS.md#2-test-id-scheme): `A-<category>-<n>` (e.g. `A-J1`, `A-K23`, `A-P5`).

## 10. Terminology

A term defined in [`12_GLOSSARY.md`](12_GLOSSARY.md) MUST be used with its glossary meaning. First occurrence in a normative document SHOULD link to the glossary using the letter-group anchor form:

```
[term](12_GLOSSARY.md#<letter>)
```

Example: `[persona](12_GLOSSARY.md#p)` jumps to the `## P` letter group where bold-text definitions live. Per-term anchors (`#persona`) are RESERVED for a future v1.1+ glossary restructuring; until then letter-group anchors are the canonical form.

Synonyms are forbidden — pick one and use it.

Forbidden synonyms (always use the left form):

| Use | Not |
|---|---|
| persona | character, agent (when referring to a persona) |
| environment instance | env, workspace (in normative text) |
| project workspace env | project (historical term; retained only in "logical filter" contexts; see [`04_PROJECT.md §0`](04_PROJECT.md)) |
| lineage scope | log, audit chain |
| acceptance pathway | verdict path, accept flow |
| safety floor | guardrails (informal only) |
| kernel | runtime, host (informal only — but see §10.1 below for the **host kernel** federation-role exception) |

### 10.1 Federation-role compound — `host kernel`

The two-word compound **`host kernel`** is admissible as a defined federation-role term in [`09_PROTOCOLS.md §3A-§3E`](09_PROTOCOLS.md#3-a2a--agent-to-agent-federation) and dependent prose. Within that scope it denotes the kernel that owns a federated entity (persona, project, environment, domain) and stands opposite to **`peer kernel`** (the receiving / non-owning kernel in an A2A federation).

This carve-out applies ONLY when:

1. The compound is `host kernel` (or its plural, `host kernels`) — bare `host` remains informal-only.
2. The usage names a federation role, not a deployment role. "The host kernel signs the AgentCard before federation" is conformant; "the host environment" or "the host machine" is not.
3. The doc is `09_PROTOCOLS.md` or a section that cites a federation-role contract defined there.

In all other contexts, the §10 row continues to apply — use `kernel` (qualified by the owning scope when needed, e.g. "owning kernel", "primary kernel", "issuing kernel") rather than `host`.

## 11. Citation style

Inline citation: `[Author Year]` or `[ProtocolName Year]`. Bibliography entry: `Author(s) (Year). Title. Venue. URL or DOI.`

## 12. Versioning

v1.0 documents are versioned as a set. The version field in front matter MUST equal the v1.0 release line (`1.0.x` / `1.1.x` / `1.2.x`) at the time of last substantive edit. Cosmetic edits MAY skip a bump; substantive edits (any change to a normative claim, schema, FSM, or acceptance criterion) MUST bump the patch.

`status: Stable` documents require both (a) all referenced acceptance tests defined and (b) cross-doc consistency sweep passed.

## 13. Document index

| # | File | Normative? | Audience | Read time |
|---|------|-----------|----------|-----------|
| — | `README.md` | No | All | 4 min |
| — | `SPEC_CONVENTIONS.md` (this file) | Documentation-normative | Authors, reviewers | 6 min |
| 00 | `00_VISION.md` | Partially (invariants are normative; narrative is not) | All | 12 min |
| 01 | `01_KERNEL.md` | Yes | Implementers | 14 min |
| 02 | `02_PERSONA.md` | Yes | Implementers, persona authors | 18 min |
| 03 | `03_TASKS.md` | Yes | Implementers | 14 min |
| 04 | `04_PROJECT.md` | Yes | Implementers, project leads | 16 min |
| 05 | `05_ENVIRONMENT.md` | Yes | Implementers, environment authors | 16 min |
| 06 | `06_DOMAIN.md` | Yes | Implementers, domain curators | 18 min |
| 07 | `07_ARTIFACTS.md` | Yes | Implementers | 12 min |
| 08 | `08_KNOWLEDGE.md` | Yes | Implementers, memory engineers | 18 min |
| 09 | `09_PROTOCOLS.md` | Yes | Implementers, integrators | 14 min |
| 11 | `11_ACCEPTANCE_TESTS.md` | Yes (defines the test corpus) | Implementers, QA, auditors | 8 min |
| 12 | `12_GLOSSARY.md` | Documentation-normative | All | 6 min |
| 13 | `13_DESIGN_VALIDATION.md` | No (validation log) | Reviewers, auditors | 8 min |
| 14 | `14_DECISIONS.md` | No (ADR catalog) | Reviewers, auditors, research | 10 min |

## 14. Compliance

A v1.0 document is **conformant** to these conventions when:

1. Front matter is present and complete, with all enum-valued fields drawn from §1.1 / §1.2 / §1.3.
2. Normative claims use RFC 2119 keywords in ALL CAPS per §2.
3. Section structure carries the three §3.1 bookends (`## 0. Status & scope`, `## Risks & known limitations`, `## Open questions`). Any deviation from the §3.2 ten-section skeleton is documented in `## 0. Status & scope` per §3.3.
4. H2 headings use integer numbering per §3.4; letter suffixes are permitted only when they match Pattern A (lowercase patch insertion) or Pattern B (uppercase structural pillars). Forbidden mixed-case (`## 11Ab.`), numeric-letter (`## 11a1.`), and arbitrary alphabetic (`## 11x.`) forms are absent.
5. Schemas declare a `schema` field with `<name>/<integer>` value per §4 and appear either in the [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md#7-schema-registry) headline catalogue (broadly load-bearing schemas) or in the generated registry produced by the schema-extractor CI job (narrower schemas). The two together form the authoritative registry for INV-10 runtime version checks per [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md#7-schema-registry).
6. Cross-references use one of the three forms in §6.1: prose inline references use the anchored form `[`file.md §N`](file.md#anchor)` with non-empty anchor fragments; tabular registry cells and cross-reference indexes MAY use the visible-only form (`[`file.md §N`](file.md)`); top-level "see also" entries MAY use the document-only form (`[`file.md`](file.md)`). Mixed forms (visible text names a section but the URL has neither anchor nor visible match) are non-conformant.
7. Risks (§7 six-column table) and Open Questions (§8 with `OQ-<doc>-<n>` IDs) are present, or `N/A` is explicitly justified in `## 0. Status & scope`.
8. Normative claims with corresponding acceptance tests carry inline test-ID cross-references per §9.
9. Terminology matches §10; forbidden synonyms are not used in normative text.
10. First mention of each glossary term in the document links to [`12_GLOSSARY.md`](12_GLOSSARY.md) per §10.

A conformance audit SHOULD run before each release gate (see the release gate process). A conformance defect is documentation-blocking but not behaviour-blocking: it does not affect runtime correctness, but it does affect spec-readability and reviewer trust.
