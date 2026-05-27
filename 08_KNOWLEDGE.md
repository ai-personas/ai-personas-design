---
title: PersonaOS v1.0 — Knowledge, Retrieval, and Prompt Evolution
status: Stable
---

# 08 — Knowledge, Retrieval, and Prompt Evolution

> **Reader guide.** This document covers how AI Personas *remember*, *find relevant information*, and *improve over time*. Memory in PersonaOS is structured: what happened (episodic), what is true (semantic), and what I've learned about myself (reflective). In this document, you'll learn how memory works across sessions, how retrieval finds the right knowledge at the right time, and how prompts evolve automatically to get better at specific tasks. **Prerequisites:** `02_PERSONA.md`, `06_DOMAIN.md`. **Key terms:** *memory tier* = four levels of storage from recent to archive (importance-weighted); *hybrid retrieval* = combining text search, knowledge graphs, and AI reranking to find relevant memories; *provenance score* = how trustworthy a memory is (decays with age, rises with use).

Normative document. RFC 2119 keywords apply per [`SPEC_CONVENTIONS.md §2`](SPEC_CONVENTIONS.md#2-normative-language-rfc-2119--rfc-8174). This document specifies the 5-tier ontology, 7-scope memory tagging, the 8 knowledge artefacts (Tactic / Skill / Tool / Rubric / Lesson / K-line / ProvenFact / Meta-prompt), the 4-tier memory model + provenance, hybrid retrieval (6-stage pipeline), hierarchical graph memory, consolidation (CLS-grounded), DSPy GEPA + MIPROv2, and the 5-layer prompt assembly.

## 0. Status & scope

**Status.** `Stable`; current revision per front matter. Fully normative; RFC 2119 keywords carry normative force per [`SPEC_CONVENTIONS.md §2`](SPEC_CONVENTIONS.md#2-normative-language-rfc-2119--rfc-8174).

**In scope.** The five-tier ontology (coordination, capability, knowledge, communication, evolution), seven-scope memory tagging (persona / project / env / domain / task / federation / public), the eight knowledge artefacts (Tactic, Skill, Tool, Rubric, Lesson, K-line, ProvenFact, Meta-prompt), the four-tier memory model (working / episodic / semantic / archival) with full provenance, hybrid retrieval (6-stage pipeline: BM25 sparse + dense vector + graph traversal + cross-encoder rerank + recency + diversity), hierarchical graph memory, CLS-grounded consolidation, DSPy GEPA + MIPROv2 prompt evolution, anti-degradation safeguards, and the five-layer prompt assembly.

**Out of scope.** The kernel signing primitives that sign every artefact mutation (see [`01_KERNEL.md §4`](01_KERNEL.md#4-signing-infrastructure--3-custody-tiers--key-hierarchy)); persona evolution dynamics that consume the knowledge artefacts (see [`02_PERSONA.md §10`](02_PERSONA.md#10-anti-goodhart-for-emergence--reflection)); domain emergence that populates the domain-scope memory tier (see [`06_DOMAIN.md`](06_DOMAIN.md)); the schema-registry entries for memory / retrieval / prompt entities (see [`09_PROTOCOLS.md §7`](09_PROTOCOLS.md#7-schema-registry)).

**Supersession.** Subsumes the prior-version knowledge / memory / prompt-evolution designs into one coherent reference.

**Structural deviation.** Follows the compressed-opening pattern of [`SPEC_CONVENTIONS.md §3.3`](SPEC_CONVENTIONS.md#33-compressed-opening-permitted): Background, Goals, and Definitions are folded into §1 ("The five-tier ontology"). The three §3.1 bookends (this section, the Risks table, and Open Questions) are present.

## 0a. Plain-Language Guide

*Here's how memory, retrieval, and learning work in PersonaOS, explained without jargon.*

**What this document is about**

This document describes how PersonaOS manages knowledge, memory, and learning. Every AI Persona ("persona") needs to remember things, find relevant information, and improve over time. This document specifies all three.

**The five-tier knowledge ontology**

Everything in PersonaOS belongs to exactly one of five tiers. Coordination tracks where work happens (projects, tasks, teams). Product holds what gets produced (verified facts, feedback). Capability contains tools and skills used to act. Knowledge stores what gets read to inform decisions (memories, lessons, references). Context captures relationships, presence, mood, and attention. A few things live in two tiers -- for example, a Skill is both a capability (it runs) and knowledge (it was learned).

**Memory types: episodic, semantic, and reflective**

Personas have three kinds of memory. Episodic memory records raw events -- what happened, when, who was involved, what was said. Semantic memory distils facts and patterns from episodes, stripping raw quotes. Reflective memory captures higher-level self-insight: what the persona has learned about its own strengths and working patterns. Episodic memories fade over time unless useful. Semantic memories persist unless contradicted. Reflective memories stay until explicitly retired.

**K-lines: topology and skill replay patterns**

A K-line records how a type of task was successfully solved before -- which team, which skills, what task shape. When a matching new task arrives, the system can replay a proven approach instead of deliberating from scratch. K-lines are authored by Historian personas.

**Lessons: distilled insights from experience**

A Lesson captures a useful work pattern: trigger, action, and rationale. Lessons gain strength each time they are cited in successful work. When a Lesson accumulates enough citations across enough distinct tasks, it can be promoted into a permanent tactic -- a standing instruction the persona follows.

**Proven facts: verified truths with evidence chains**

A ProvenFact is a statement verified by the system's verification pipeline, backed by evidence and signed by the kernel. Proven facts are append-only and can be promoted across wider scopes as they accumulate independent citations.

**Knowledge retrieval: the six-stage pipeline**

Retrieval runs through six stages: (1) structured filtering narrows millions of entries to a relevant subset using scope tags, memory type, and trust thresholds; (2) vector search finds semantically similar entries; (3) graph traversal walks a knowledge graph for multi-hop connections; (4) fusion merges vector and graph results; (5) a cross-encoder reranker scores top candidates; (6) per-persona composition filters results by role, charter, and observation permissions. The result is a tailored set of memories specific to that persona for that task.

**Memory scoping: seven scopes**

Every memory is tagged with up to seven scopes controlling visibility: user, persona, session, project, environment, application, and organization. A memory tagged to one user never crosses to another without explicit consent. Cross-scope transfer requires a promotion event.

**Prompt evolution: GEPA and MIPROv2**

Two optimization systems improve persona prompts over time. GEPA (Genetic-Pareto) reflects on recent execution traces, identifies what worked and failed, and proposes mutations to the persona's tactics. It optimizes across multiple objectives at once (accuracy, cost, speed, safety). MIPROv2 (Bayesian instruction search) handles cold starts -- generating brand-new tactics from scratch. Together they form a closed loop: work produces outcomes, outcomes produce reflections, reflections produce better tactics, better tactics produce better work.

**Citations: tracking where knowledge came from**

Every memory carries provenance -- where it came from, how trustworthy it is, how often successfully used. The provenance score decays with age and rises with use, feeding both retrieval ranking and tier transitions.

**Supersession: when new knowledge replaces old**

When a source is superseded (contradicted or retracted), the system automatically degrades trust scores of every claim that cited it. Claims are flagged for re-evaluation, not deleted. The cascade is depth-bounded (three hops) and rate-limited (one cascade per source per day).

**Cross-org memory: sharing knowledge between organizations safely**

In multi-tenant deployments, the system tracks which organization's memory influenced each contribution via provenance edges. This creates an audit trail so cross-organization information flow is visible and reviewable, without blocking the work.

**Memory power asymmetry: safeguards for users**

A persona remembers everything by default; users do not. To balance this, memories involving users are consent-gated (the user controls what is stored), provenance-tracked (the user can ask where a memory came from), and scope-bounded (one user's memories never leak to another).

## 1. The five-tier ontology

Every entity in v1.0 fits exactly one tier. [Memory](12_GLOSSARY.md#m), [KnowledgeRef](12_GLOSSARY.md#k)s, and capability assets each have a designated home.

*The five tiers are: (1) Coordination -- where work happens and who does it; (2) Product -- what is produced; (3) Capability -- what is used to act; (4) Knowledge -- what is read to inform; (5) Context -- state about who, where, and relationships. Each entity belongs to exactly one tier, with two named exceptions.*

**Technical detail:** See [A.1](#appendix-a1).

Skills span Capability + Knowledge (learned-as-code is both). ProvenFacts span Product + Knowledge (produced by verification, retrieved by reasoning).

## 2. The eight knowledge artefact types

*Eight artefact types carry knowledge in v1.0: Tactic (standing heuristic rules), Skill (executable code), Tool (promoted code in four classes), Rubric (judgment criteria), Lesson (work-pattern reflection), K-line (task topology replay pattern), ProvenFact (verified statement with evidence), and Meta-prompt (tactic-generation template). Each has a distinct lifecycle and scope.*

**Technical detail:** See [A.2](#appendix-a2).

### 2.1 K-line vs Skill vs ProvenFact vs Lesson — distinction matrix

v1.0 disambiguates these four "things learned." Four-way comparison:

| dimension       | K-LINE                                  | SKILL                                | PROVENFACT                          | LESSON                              |
|-----------------|------------------------------------------|---------------------------------------|--------------------------------------|--------------------------------------|
| origin          | Historian assembles from prior wins      | Persona authors via skill_synthesise  | Kernel signs on verifier verdict     | Reflector mode; or promoted reflective |
| about           | task topology + skill replay pattern     | executable code (Voyager-style)       | verified statement (evidence-bound)  | work pattern (trigger / action / rationale) |
| scope           | global (Historian-keyed); env / project K-lines | per-persona skill_library | task / project / env (G-set CRDT)    | global lesson_index; project-scoped if tagged |
| persistence     | success/failure replay counters drive retention | until skill_retire             | append-only; never decays           | provenance-decayed; cited→strengthened |
| evolution       | new wins extend; tau-matched fingerprints accumulate | mutates via skill_compose, MIPROv2 | promoted across scopes on K≥3 cites  | citation count ≥ N (default 5) over M ≥ 3 tasks → Lesson → Tactic promotion |
| retrieval rank  | orient-time fast-path (skip collaborative rounds if τ-matched) | tool-listing at envelope mint | top-K cited as evidence in reasoning | top-K advisory at envelope mint via find_lesson |
| dual tier       | KNOWLEDGE only                           | CAPABILITY + KNOWLEDGE                | PRODUCT + KNOWLEDGE                  | KNOWLEDGE only                       |

Mental model: **K-lines are task templates; Skills are operational atoms; ProvenFacts are evidence atoms; Lessons are work-pattern atoms.** A K-line may reference Skills + ProvenFacts as its content; a Lesson may cite Skills + ProvenFacts in its rationale.

## 3. Three memory types

*Three memory types model persona recall. Episodic memory stores raw events with timestamps and original wording (decays by usage frequency, emotional weight, and recency). Semantic memory stores consolidated facts abstracted from episodes (persists unless contradicted). Reflective memory stores higher-level self-insight (persists until explicitly retired).*

**Technical detail:** See [A.3](#appendix-a3).

### 3.1 Consolidation pipeline (CLS-inspired)

*Events are first written as episodic memory. Periodic sweeps (hourly or on idle) consolidate episodics into semantic memory by summarizing and dropping raw quotes. Weekly reflective consolidation generates higher-level inferences. An importance-weighting formula (combining verifier signals, cross-references, salience, and recency) drives selective forgetting: memories that fall below threshold are demoted to colder tiers.*

**Technical detail:** See [A.4](#appendix-a4).

Bounded memory architecture: total tier sizes bounded; importance-weighted demotion outperforms unbounded retention (CraniMem 2026).

### 3.2 Reflection retrieval path and Lesson → Tactic promotion

Reflective memory MUST be both stored AND retrieved AND promotable.

**Storage:** reflections persist as `Lesson` records in `soul.state.json.reflection_archive`.

*Each Lesson record carries a schema identifier, persona id, task context, a measurable trigger and action, a rationale, a confidence score (rising with citations), and a signed parent lineage chain.*

**Technical detail:** See [A.5](#appendix-a5).

A Lesson is distinct from a Tactic: Tactic is a SOUL.md EVOLVE-BLOCK line scoped to one persona; Lesson is free-floating, citable by any persona's tactic via `parent_lineage`.

**Retrieval at envelope-mint:** Historian fetches top-K lessons by embedding the task statement and searching with tier and provenance filters.

*The retrieval call searches the vector index for the 8 most relevant lessons in RECENT or WARM tiers with minimum provenance of 0.3.*

**Technical detail:** See [A.6](#appendix-a6).

Kernel renders into LAYER 4 (RETRIEVED) of the 5-layer prompt assembly (§10) as advisory context — separate from EVOLVE-BLOCK tactics (LAYER 2), which are commands. Personas may use or ignore; a lesson cited in an accepted candidate's lineage gets `+1` citation, raising `base_confidence`.

**Lesson → Tactic promotion:** when a lesson accumulates ≥ N (default 5) citations across ≥ M (default 3) distinct tasks, the kernel **proposes** it as a tactic in the citing persona's EVOLVE-BLOCK. Promotion gate requires: citation threshold met, operationality check (measurable trigger and action, no contradiction with ProvenFacts, no paraphrase of existing tactic), charter-conformance check, kernel-emitted proposal, and persona sign-off.

*The five-step promotion gate ensures lessons earn their way into standing instructions through repeated real-world success, not automatic promotion.*

**Technical detail:** See [A.7](#appendix-a7).

Promotion is a proposal, not auto-write. The closing loop: produce → reflect → cite → promote.

**Tests:** A-TX1 (5-tier ontology — every entity classified once), A-TX2 (Skill dual-tier), A-TX3 (4 tool classes composable), A-TX4 (Lesson/Reflective/ProvenFact distinct lifecycles), A-TX5 (K-line / Skill / ProvenFact distinction). See [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md).

## 4. Four memory tiers

*Memories move through four tiers based on age and importance: RECENT (0-14 days, weight 1.0), WARM (14-90 days, weight 0.7), COLD (90 days to 1 year, weight 0.3), and ARCHIVE (over 1 year, weight 0.05). Each tier has a minimum provenance threshold.*

**Technical detail:** See [A.8](#appendix-a8).

Tier transitions are signed events. Retrievals compose tier × scope × type.

## 5. Seven-scope memory tagging

The 2026 production pattern (Mem0/Zep/Letta/Cognee), extended.

*Every memory is tagged with up to eight scope identifiers: user, persona, session, project, environment, app, org, and relationship. These compose with a type axis (episodic, semantic, reflective, lesson, k-line, proven fact, knowledge ref, standard ref, notation convention, ambient event) and a tier axis (RECENT/WARM/COLD/ARCHIVE). Five cross-scope boolean flags control whether a memory may be transferred across project, environment, persona, domain, or relationship boundaries. All default to false; promotion requires a consolidation event.*

**Technical detail:** See [A.9](#appendix-a9).

Defaults: false. Promotion requires consolidation event.

**Pair-scoped memory.** When two personas form a `PersonaRelationshipEdge` (`02_PERSONA §11.4`), co-signed summaries and joint-event reflections may be tagged with the edge's `edge_id` as `relationship_id`. Both personas observe such memories in their own retrieval views; neither persona alone may unilaterally delete them (delete requires the same counter-sign as edge mutation). On edge `ended`, pair-scoped memories with `cross_relationship_transferable = False` enter `ARCHIVE` tier; with the flag set, they remain available to either persona's recall under that pair's history.

**Tests:** A-TX6 (seven-scope tagging composes scope context), A-TX7 (retrieval-score formula deterministic + tie-breaking), A-TX8 (cross-scope transferable flag; anti-leakage blocks differing user_id), A-TX9 (per-persona projection: same task → different envelope context). See [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md).

## 6. Unified provenance score

*The provenance score is the product of four factors: base confidence (initial trust at creation), age decay (diminishes over time with a half-life), verifier consistency (ratio of verified to contradicted uses), and usage signal (logarithmic count of citations in successful work). This composite score feeds both tier transitions and retrieval ranking.*

**Technical detail:** See [A.10](#appendix-a10).

Provenance feeds tier transitions and retrieval ranking.

### 6.3 SupersessionCascade

When a `KnowledgeRef` is marked `superseded_by` (a newer publication contradicts, retracts, or supersedes it), all claims that cited the superseded `KnowledgeRef` as primary evidence should have their `provenance_score` automatically degraded. Without cascade, stale evidence silently props up dependent claims — unsustainable in frontier domains where ~15% of ingested refs are superseded within 6 months.

*The SupersessionCascade schema links the superseded and superseding references, applies a direct discount (0.5) to claims citing the superseded ref and a transitive discount (0.25) to claims at depth 2+, bounded to depth 3. A companion CascadeAffectedClaim schema tracks each claim's prior and discounted provenance scores and its re-evaluation status. Rate-limited to one cascade per reference per 24-hour window.*

**Technical detail:** See [A.11](#appendix-a11).

**Constraints.**

- **Cascade is automatic, not destructive.** The kernel traverses the citation/evidence graph (`ProvenFact.evidence_refs`, `ProposedKind.evidence_refs`, `ArtifactBundle.citation_refs`) and applies the discount to each dependent claim's `provenance_score`. Claims are NOT deleted, retracted, or tombstoned — they are flagged for re-evaluation with degraded provenance.
- **Persona override.** After cascade, a persona MAY re-evaluate each affected claim. Re-confirmation (the claim stands on other evidence) restores `provenance_score` to pre-cascade level with `status = "re_confirmed"`. Further downgrade sets `status = "further_downgraded"`. Both are signed lineage events.
- **Depth-bounded.** `max_cascade_depth = 3` prevents unbounded graph traversal. Claims at depth >3 are not affected; if their provenance depends on deeply-nested superseded evidence, the persona must audit manually.
- **Rate-limited.** Max 1 cascade per `KnowledgeRef` per `rate_limit_window_hours`. If the same ref receives multiple supersession events within 24h (e.g., two independent retractions), only the first triggers a cascade; subsequent ones update `superseding_ref_id` but do not re-cascade.

**Tests:** A-SC1 (cascade triggers on KnowledgeRef supersession), A-SC2 (direct discount applied correctly), A-SC3 (transitive discount at depth 2), A-SC4 (max_cascade_depth respected), A-SC5 (rate limit enforced), A-SC6 (persona re-confirmation restores provenance), A-SC7 (cascade does not delete or tombstone claims). See [`11_ACCEPTANCE_TESTS.md §9l`](11_ACCEPTANCE_TESTS.md).

**Lineage:** `supersession_cascade_triggered`, `supersession_cascade_applied`, `supersession_cascade_claim_re_confirmed`, `supersession_cascade_claim_further_downgraded`.

## 7. Hybrid retrieval — six-stage pipeline

*A query enters the six-stage pipeline with scope context, intent, and persona context. Stage 1 (structured filter) eliminates ~99% of the corpus using scope tags, type, tier, provenance threshold, and charter compatibility. Stage 2 (vector retrieval) finds the top-50 semantically similar entries. Stage 3 (graph retrieval) walks the hierarchical graph for multi-hop connections, returning the top-20 graph-relevant entries. Stage 4 (fusion) merges vector and graph results via reciprocal rank fusion. Stage 5 (cross-encoder rerank) scores the fused candidates and returns the top-10. Stage 6 (per-persona composition) applies observation surface and role/charter filters, then composes the result into the envelope context block.*

**Technical detail:** See [A.12](#appendix-a12).

### 7.1 Composition formula

*The final retrieval score is the product of ten factors: base vector similarity, tier weight, scope match (product across all scopes), cross-encoder relevance, graph boost, reuse signal, recency penalty, promotion stage weight, charter compatibility (binary gate), and observation surface access (binary gate). Differing user_id hard-blocks retrieval (one user's memory never crosses without consent).*

**Technical detail:** See [A.13](#appendix-a13).

Anti-leakage: differing `user_id` hard-blocks (one user's memory never crosses without consent).

### 7.2 Stage-aware ranking

*Stage weights map promotion stages to retrieval multipliers: EMERGENT (0.5), RECOGNISED (0.7), AUTHORITATIVE (0.9), STANDARDISED (1.0), DEPRECATED (0.2), TOMBSTONED (0.0).*

**Technical detail:** See [A.14](#appendix-a14).

Higher-trust entries dominate; emergent entries returned with stage indicator surfaced to persona.

**Tests:** A-TX14 (retrieval latency: hot ≤ 50 ms, warm ≤ 100 ms, cold ≤ 500 ms), A-TX15 (six-stage pipeline produces deterministic ranking on same query + corpus). See [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md).

## 8. Hierarchical Graph Memory

Three-tier graph.

*Three graph tiers organize knowledge connections. Tier 1 is a global topic associative network -- an entity-level graph of domain concepts persistent across all projects, updated nightly. Tier 2 comprises local event progression graphs per project and environment, with temporal and relationship edges (preceded_by, caused_by, contradicts, supports, etc.) for multi-hop and causal reasoning. Tier 3 is a per-membership observation subgraph, filtered by the persona's role and charter, composed at envelope mint for persona-specific situational awareness.*

**Technical detail:** See [A.15](#appendix-a15).

Storage: graph database (Neo4j-compatible) for Tier 1+2; in-memory subgraph for Tier 3. Embedding index alongside.

## 9. Per-persona retrieval composition

The kernel composes persona's context at envelope mint.

*The build_persona_view function assembles a PersonaProjectedView containing: filtered project state (open problems by role, obligations owed and owing, active disagreements, relevant conjectures, pending peer reviews), filtered ambient environment state (recent events, observable co-members), the persona's own top-20 relevant memories, shared proven facts (top-15), conventions, and operational state (attention budget, energy, active mode, acceptance pathway).*

**Technical detail:** See [A.16](#appendix-a16).

### 9.1 Two personas, same project, different views

Same task arriving to Volt (lead, experimenter_leaning) and Sage (historian, historian_leaning).

*Volt sees experimenter mode, VERIFIER_ACCEPT pathway, 3 obligations, his own design edits and buck-compensation skills. Sage sees historian mode, INTERACTIVE pathway, 1 obligation, cited literature, and K-lines on compensation design problems. Same project, same task skeleton, but each persona gets a view filtered by its role, mode, and memory.*

**Technical detail:** See [A.17](#appendix-a17).

**Same project; two personas; two views.** Kernel projects per-persona.

### 9.2 Persona's own curation

Personas curate things they personally own.

*Eight categories of persona-owned knowledge: personal episodic memory (consent-gated), personal semantic memory (kernel-consolidated), personal reflective memory (Reflector-produced), skill library (persona-authored), tactic EVOLVE-BLOCK (signal-weighted mutations), mode proficiencies, personal goals (charter-checked), and observation surface evolution (proposed via env admin). All are kernel-signed on mutation.*

**Technical detail:** See [A.18](#appendix-a18).

These are persona-owned, kernel-signed on mutation.

### 9.3 ScopedKnowledgeQuery — first-class scope-bounded retrieval API

The six-stage retrieval pipeline (§7) and the per-persona composition (§9) build views internally at envelope mint. Some callers — UI surfaces showing "what does this persona remember in this project," audit tools, federation peers, scoped consent dialogs — need an explicit query interface that takes a scope spec and returns the matching index, not a composed envelope context block.

*The ScopedKnowledgeQuery schema provides an externally-callable retrieval interface accepting scope tags, type and tier filters, cross-scope inclusion flags, result-shape parameters (top-k, provenance, lineage refs), and a consent-check flag. Four admission rules govern its results: (1) consent gate -- user-scoped entries require consent; (2) scope intersection -- results are the strict intersection of supplied scope tags; (3) cross-scope flags honoured -- only entries carrying the matching cross-flag are included; (4) relationship scope -- pair-scoped memory accessible to both pair members, non-pair callers require operator scope.*

**Technical detail:** See [A.19](#appendix-a19).

**Composition with §9 envelope mint.** `ScopedKnowledgeQuery` is the externally-callable shape of the same machinery `build_persona_view` (§9) uses internally. The two share the index, the consent gates, and the provenance score; they differ in result shape (composed envelope context block vs queryable entry list) and admission (envelope mint trusts the kernel; external query passes consent + scope gates).

**Why this is substrate-shape.** The query has no domain branches — it composes over scope tags, type axis, tier axis, cross-flags, and the relationship-id extension. Everything is topology; nothing names an industry or knowledge field.

**Honest limits.**

1. **Cross-encoder rerank is skipped.** `ScopedKnowledgeQuery` runs stages 1–3 (filter, vector, graph fusion) and returns ranked results without the cross-encoder rerank stage — that stage is task-context-aware and not appropriate for ad-hoc queries.
2. **Audit callers see redacted lineage refs.** When `return_lineage_refs = True` and the caller is not the persona who owns the entries, lineage refs are redacted to event hashes only (no payload). Full lineage requires operator scope.
3. **The query is read-only.** It never mutates the index, never advances tier transitions, never marks entries as accessed. Mutation requires the existing kernel-mediated paths.

**Acceptance tests.** A-SQ1 (consent gate refuses user-scope entries when may_share = False), A-SQ2 (scope intersection strict; empty scope refused), A-SQ3 (cross-flag honoured; non-transferable entries omitted under cross-scope request), A-SQ4 (relationship_id scope returns only pair-tagged entries), A-SQ5 (lineage refs redacted for non-owner caller), A-SQ6 (cross-encoder rerank skipped vs §7 full pipeline).

## 10. Five-layer prompt assembly

v1.0 envelopes assemble system prompts in five layers.

*Layer 1 (FROZEN, cacheable) carries persona identity, charter, voice, and disposition. Layer 2 (EVOLVABLE, cacheable if stable) carries evolved tactics and communication style. Layer 3 (CONTEXTUAL, not cacheable) carries project, environment, relationship, mood, and presence state. Layer 4 (RETRIEVED, not cacheable) carries the persona's own memory, relevant skills/lessons/K-lines, domain knowledge, and recent ambient events. Layer 5 (TASK, not cacheable) carries the task statement, acceptance pathway hint, active mode hint, and output schema constraints.*

**Technical detail:** See [A.20](#appendix-a20).

Layers 1, 2, and stable parts of 3 cacheable. **Target ≥ 80% cache hit rate** for cost amortisation.

**Tests:** A-TX12 (`cache_control` layers 1-2; hit rate ≥ 80%), A-P22 (prompt-block rendering deterministic; blocks 0-4 cached; per-task suffix blocks never cached). See [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md).

## 11. DSPy GEPA — reflective prompt optimization

v1.0 integrates DSPy GEPA as primary prompt optimizer for evolution.

*GEPA (Genetic-Pareto, 2025) reflects on execution traces, uses natural language feedback to evolve prompts, and performs multi-objective Pareto search across verifier pass rate, cost, latency, and charter conformance. It outperforms MIPROv2 by 10%, GRPO by 20%, with 35x fewer rollouts.*

**Technical detail:** See [A.21](#appendix-a21).

### 11.1 v1.0 GEPA integration

*The GEPA optimizer gathers execution traces from the persona's recent 100 tasks, extracts per-trace feedback (tactic, outcome, signal weight, natural language reflection), evolves the EVOLVE-BLOCK via Pareto search with 10 rollouts, and promotes candidates that improve the Pareto front with a 0.05 signal threshold.*

**Technical detail:** See [A.22](#appendix-a22).

GEPA is the **primary mechanism for tactic mutation**.

**Tests:** A-P16 (rollback on degradation — GEPA-evolved tactics revertable), A-P17 (eight evolution signals + v1.1 additions flow to credit formula), A-P18 (22 mutation operators all gated, signed, rate-limited). See [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md).

## 12. MIPROv2 — Bayesian instruction + demo search

For cold-start tactic generation.

*MIPROv2 operates in two phases: Phase 1 generates 12 instruction candidates per tactic (LLM-generated, cost-bounded). Phase 2 performs Bayesian search over instruction-demonstration combinations, testing each against held-out signals, and selects the best candidate as the new tactic.*

**Technical detail:** See [A.23](#appendix-a23).

### 12.1 v1.0 MIPROv2 integration

*The MIPROv2 optimizer generates 12 instruction candidates from recent traces and the persona's charter, selects 4 demonstrations from the skill library, then runs Bayesian optimization over 50 iterations to find the best tactic.*

**Technical detail:** See [A.24](#appendix-a24).

### 12.2 MIPROv2 vs GEPA in v1.0

| Use case | Optimizer |
|---|---|
| Frequent tactic refinement | GEPA (sample-efficient; reflective) |
| Cold-start tactic generation | MIPROv2 (Bayesian; broad space) |
| High-stakes prompt rewrite | MIPROv2 + GEPA combined |
| Per-persona daily evolution | GEPA |

## 13. Reflection-driven refinement

Reflector mode + reflection loop drive prompt evolution.

*Reflection runs on a four-level schedule: per-persona every 20 tasks, per-session at boundaries, at project milestones, and at multi-project horizons. Outputs include candidate tactic mutations (fed to GEPA), skill promotions, charter refinements (operator-reviewed), and meta-prompt updates. All candidates are marked, not auto-promoted; promotion requires signal confirmation over at least 5 subsequent tasks, charter conformance, cross-persona similarity audit, and kernel/operator sign-off.*

**Technical detail:** See [A.25](#appendix-a25).

## 14. Per-persona prompt evolution

*The evolution cycle flows: task produces outcome, outcome produces signals, GEPA reflects and proposes tactic mutations, mutations pass through a confirmation gate (signal corroboration over time), promoted tactics enter the EVOLVE-BLOCK, and the next envelope mint uses the new tactics. The cycle continues indefinitely.*

**Technical detail:** See [A.26](#appendix-a26).

### 14.1 Anti-degradation safeguards

*Six safeguards prevent evolution from going wrong: MAP-Elites maintains tactic diversity; a diversity penalty disfavours parents with similar children; cross-persona audit checks pairwise similarity and rolls back if convergence exceeds threshold; charter conformance must remain at or above 0.95; voice consistency must remain at or above 0.9; and refusal rates must stay in expected ranges. If evolution degrades, the kernel rolls back to the previous EVOLVE-BLOCK version.*

**Technical detail:** See [A.27](#appendix-a27).

### 14.2 Per-channel tactic evolution

Communication tactics evolve **per channel**, not as a single undifferentiated set. Each persona's SOUL.md permits an EVOLVE-BLOCK region per channel.

*Seven channel-specific EVOLVE-BLOCKs cover: blackboard (team broadcast), direct message (persona pair), proven facts (project CRDT writes), candidate table (task-scoped candidate authoring), goal stack (task-scoped coordination), ambient stream (env-scoped event emission), and presence (env-scoped presence updates). Each tactic line carries confidence and fertility scores. Six mutation rules govern evolution: measurable trigger, measurable action, no contradiction with ProvenFacts, no cosine-similar paraphrase in the same channel, signed mutation with lineage, and per-channel signal corroboration.*

**Technical detail:** See [A.28](#appendix-a28).

The principle: **a persona gets better at coordinating in each channel independently**, not just better at the cognitive function. A persona may have strong blackboard tactics and weak DM tactics; evolution per channel preserves the distinction.

## 15. Anti-Goodhart for signal corroboration

Anti-Goodhart rule for soft signals.

*Tactic promotion rules vary by mode. Convergent/Divergent modes: verified outcome alone or judged outcome alone suffice. Relational/Pedagogic/Performative modes: engagement signal alone never promotes; user feedback alone does not promote; judged outcome plus user feedback promotes; engagement plus user feedback plus audit clearance promotes with a note. Universal: reflection alone never promotes -- it must await corroboration.*

**Technical detail:** See [A.29](#appendix-a29).

The kernel's audit pass clears recent interactions for known anti-patterns (dependency cultivation, sycophancy, manipulation language) before engagement-signal-driven promotion. Audit clearance is the **Goodhart canary** at evolution layer.

## 16. Mutation operators (22 total)

*Twenty-two mutation operators span four groups: core (9: tactic_propose, tactic_retire, skill_synthesise, skill_compose, meta_prompt_mutate, crossover, fork_clone, fork_compose, retire_proposal), relational/evolution (6: relational_style_propose, mode_proficiency_update, reflection_synthesise, trust_signal_apply, consolidation, forgetting), domain emergence (5: probe_initiate, knowledge_ingest, recipe_infer, convention_propose, cross_domain_transfer), and v1.0 additions (2: project_role_propose, domain_skill_propose).*

**Technical detail:** See [A.30](#appendix-a30).

All gated by kernel checks, signed, lineage-linked, rate-limited per persona per task.

## 16a. MeasurementFact + UncertaintyEnvelope

Per the design goals ("numerical data summarisation, uncertainty as first-class, statistical reproducibility"), numerical claims are currently free-form ProvenFacts — a bare float carries no uncertainty, no calibration trace, no replication context. For any measurement-heavy domain (any field where a number with uncertainty is load-bearing — physics, chemistry, biology, engineering, clinical care, manufacturing QA), this hides exactly the structure that matters. v1.0 promotes uncertainty to first-class with two schemas.

### 16a.1 UncertaintyEnvelope

*The UncertaintyEnvelope schema wraps a numerical measurement with its statistical distribution (gaussian, lognormal, uniform bounded, interval only, empirical samples, or custom), central value, standard deviation, sample list, confidence interval bounds, systematic error floor, calibration chain reference, and KindRegistry-resolved units. Distribution kinds are mathematical shapes, not domain categories -- math is universal across domains.*

**Technical detail:** See [A.31](#appendix-a31).

**Mathematical primitive vs. domain primitive.** The Literal here lists *mathematical distribution shapes*, not domain categories — substrate purity is preserved because math is universal across domains. Domain-specific quantity meanings (T1, transmittance, blood glucose) live in `units_kind` which is KindRegistry-resolved.

### 16a.2 MeasurementFact

*The MeasurementFact schema records what was measured (KindRegistry-resolved quantity kind), the value (a typed reference to an UncertaintyEnvelope -- bare floats are refused at admission), what instrument was used, the measurement protocol, when and where the measurement was taken, calibration provenance (whether calibration was expired at measurement time), replication status (single observation through blind replicated), external attestation references, and a cross-reference to a legacy ProvenFact.*

**Technical detail:** See [A.32](#appendix-a32).

### 16a.3 Composition rules

*Four J4 rules govern measurement admission: J4-MEASUREMENT requires an UncertaintyEnvelope for VERIFIER_ACCEPT grade (bare floats are capped at PANEL grade). J4-CALIBRATION caps expired-calibration measurements at PANEL grade and refuses measurements from out-of-tolerance/quarantined/decommissioned instruments. J4-REPLICATION reads trust uplift from ReplicatedAttestation. J4-UNITS requires units_kind to resolve in KindRegistry at admission.*

**Technical detail:** See [A.33](#appendix-a33).

### 16a.4 Aggregation and statistical reproducibility

When N MeasurementFact entries describe replications of the same `quantity_kind` over disjoint conditions, the kernel exposes a **read-only aggregation view**.

*The aggregate_measurements function takes a list of MeasurementFact references and a KindRegistry-resolved aggregation kind, and returns a combined UncertaintyEnvelope. The aggregator is a persona-authored skill; the substrate provides the view and signing, not the algorithm. Aggregated views carry a reproducibility class: fully reproducible (all legs have protocol, calibration, and disjoint-instrument replication), partially reproducible, single observation only, or underspecified (missing calibration or protocol, capped at PANEL grade).*

**Technical detail:** See [A.34](#appendix-a34).

The reproducibility class itself is computed by a classifier in INV-6 rotation; the kernel signs the classifier identity for audit reproducibility.

### 16a.5 Honest limits

1. **Aggregation algorithms are persona-authored.** The substrate provides the view + signing; the algorithm is a Skill (Voyager class C) the domain catalogs. Different domains may prefer different aggregators for the same `quantity_kind`.

2. **Uncertainty type-mismatch.** Combining a `gaussian` envelope with an `interval_only` envelope requires policy. The aggregator MUST declare its policy (e.g., conservative bounds intersection); the substrate enforces only that the policy is *signed and declared*, not which policy is correct.

3. **Systematic floor opacity.** `systematic_error_floor` is operator/instrument-declared; the substrate cannot independently verify it. Lineage records the declaration source so audit can challenge.

4. **No statistical theorem proving.** The substrate does not validate that an aggregation respects, e.g., the central limit theorem's preconditions. Personas may import formal verification of statistical claims via `lean_verify` or equivalent in domains that catalog such tools.

## 16b. DerivationProvenanceEdge — memory-to-contribution provenance

The 7-scope memory tagging (§5) carries `org_id` (and other scopes) on every `KnowledgeRef`, episodic memory entry, semantic fact, K-line, lesson, and proven fact. `06_DOMAIN §11.1 RISK A-E` filters *named-artifact* transfers across scopes (e.g., a `CrossDomainTransfer` carrying an artifact id refuses if the artifact's `org_id` differs from the target). What `§11.1` does **not** cover is the case where a persona *consults* a scope-tagged memory during normal retrieval (per §7 hybrid retrieval) and then *contributes derived work* in a different scope — the derived contribution carries no edge back to the consulted source, and the RISK filter has nothing to act on at contribution time.

For single-tenant deployments this is a non-issue (everything is one tenant). For multi-tenant deployments (`01_KERNEL §2.4.3` `PrincipalAttribution.multi_principal_attribution_enabled = True`), the substrate must trace which scope-tagged memories *materially shaped* each contribution, so audit can answer "did this joint-project artefact derive from one principal's internal memory in a way the other principal could not have predicted?"

`DerivationProvenanceEdge` (DPE) is the substrate-shape edge that records this. It is **soft-bound** — it does not block retrieval and does not refuse contribution — but is visible in `EnvironmentLineage` and queryable through standard graph traversal.

*The DerivationProvenanceEdge schema links a contribution event to each consulted memory, recording the contribution's signed event id and kind, the contributing persona, the consulted memory's id and scope tags (snapshot at consultation time), the persona-declared influence kind (direct quote, paraphrased, structural basis, negative example, or background context), influence strength (0 to 1), and the retrieval span id for replay. A companion DerivationProvenancePolicy schema sets enforcement mode per environment or project: off, opportunistic, mandatory for cross-principal, or mandatory for all. The admission rule resolves the policy on each contribution event mint and, in mandatory modes, refuses cross-principal contributions that lack a corresponding DPE.*

**Technical detail:** See [A.35](#appendix-a35).

**Lineage.** Each DPE is appended to the contribution's hosting `EnvironmentLineage` as `DERIVATION_PROVENANCE_EDGE_DECLARED`. Graph traversal from a contribution to its consulted memories runs `MATCH (c)-[r:DerivationProvenanceEdge]->(m)` against the lineage's edge log. Cross-principal audit queries follow the existing per-env query path (no new index required).

**Composition with `§11.1` RISK E.** RISK E mitigates explicit cross-org artifact transfer (`org_share_policy per artifact`); DPEs mitigate implicit cross-org *derivation*. Together they cover both directions: an explicit transfer with no DPE has `RISK E` to refuse it; an implicit derivation with no transfer has DPE enforcement to surface it. Neither is a hard guarantee against information leakage (the tacit-recall limit below); both raise the cost of un-audited cross-principal flow.

**Honest limits.**

1. **Tacit recall is untraceable.** A persona who internalises a fact through repeated retrieval and later contributes from "memory" without an explicit retrieval call leaves no DPE. The substrate cannot inspect persona cognition; it can only inspect the retrieval pipeline. Operators should pair DPE enforcement with frequent in-context recall checkpoints when cross-principal sensitivity is high.
2. **Persona-declared influence is not adversarially robust.** A persona could declare `influence_kind = "background_context"` for a derivation that was structurally a `direct_quote`. The lineage records the declaration; downstream audit may challenge. Substrate is robust against accidental mis-attribution, not against deliberate misrepresentation.
3. **Retrieval-span scope is limited to v1.0 OTel coverage.** Memories retrieved through non-standard paths (a Skill that bypasses the §7 pipeline; an MCP tool that fetches memory directly) may not produce a span the policy can inspect. Operators tightening enforcement should also restrict bypass paths.
4. **No automatic redaction of cross-principal contributions.** When DPE enforcement refuses a contribution, the persona must explicitly re-author without the cross-principal memory OR emit the DPE and accept the lineage record. The substrate does not auto-redact (auto-redaction would be a domain-shaped choice; substrate stays domain-neutral per C4).

**Acceptance tests.** A-DP1 (DPE schema mints cleanly), A-DP2 (opportunistic mode: contribution proceeds with or without DPE), A-DP3 (mandatory_for_cross_principal: cross-principal consultation without DPE refuses), A-DP4 (mandatory_for_cross_principal: same-principal consultation proceeds without DPE), A-DP5 (DPE graph traversal finds all consulted memories for a contribution), A-DP6 (background_context with influence_strength = 0 admitted with audit record).

## 17. Cost and latency

*Retrieval pipeline total latency target is at most 250 ms p95, with individual stage budgets ranging from 5 ms (fusion) to 100 ms (graph retrieval). Memory operations target at most 50 ms for hot tier, 100 ms for warm, 500 ms for cold, with consolidation running overnight or on idle. Prompt evolution costs $1-10 per persona per GEPA cycle and $5-30 per MIPROv2 cold-start tactic. Reflection latencies range from 200 ms per task to minutes per project. Cache hit rate target is at least 80% on layers 1-2, yielding approximately 10x cost savings at scale.*

**Technical detail:** See [A.36](#appendix-a36).

## 18. Risks & known limitations

Per [`SPEC_CONVENTIONS.md §7`](SPEC_CONVENTIONS.md#7-risks--known-limitations).

| ID | Risk | Severity | Likelihood | Mitigation | Target release |
|----|------|----------|------------|------------|----------------|
| R-KNOWLEDGE-1 | Retrieval is the bottleneck at scale. Multi-scope tag filtering across millions of entries × 7 tags × 4 tiers × top-K requires fast vector stores; cost grows with corpus. | High | High | Tiered index (HOT in-mem; WARM SSD; COLD object store); pre-filtered shards per persona; A-TX14 latency targets. | v1.0 (tiers); v1.1 (sharding). |
| R-KNOWLEDGE-2 | Per-persona projection cost at envelope mint. First envelope slower; cache mitigates subsequent. | Medium | High | Per-task persona-context cache; A-TX9 acceptance test; prompt layers 1-2 cacheable per Anthropic `cache_control`. | v1.0 (cache); v1.1 (warm-up policy). |
| R-KNOWLEDGE-3 | Cross-tier confusion at ontology boundaries. Skill spans Capability + Knowledge; ProvenFact spans Product + Knowledge. | Low | Low | Five-tier ontology with explicit dual-tier markers (A-TX1, A-TX2); query APIs handle both. | v1.0 (resolved). |
| R-KNOWLEDGE-4 | Standards alignment by convention, not enforcement. Adapter authors must follow `09_PROTOCOLS.md §8` mappings for interoperability. | Medium | Medium | Documented mapping tables; cross-adapter parity tests (A-P10); ConformanceProbe in adapter test suite. | v1.0 (docs); v1.1 (enforcement harness). |
| R-KNOWLEDGE-5 | GEPA + MIPROv2 evolution cost. $1–10 per persona per cycle. | Medium | High | Operator-tunable cadence; per-persona evolution budget; reflection gating. | v1.0 (budgets). |
| R-KNOWLEDGE-6 | Reflection latency. Per-task 200 ms; per-session seconds; per-project minutes. | Low | High | Async post-task reflection; ROI improves as track record builds; per-tier reflection windows. | v1.0 (async). |
| R-KNOWLEDGE-7 | Cross-encoder reranker quality. Off-the-shelf models may miss domain-specific patterns. | Medium | Medium | Domain operators may fine-tune; rerank stage is replaceable; rubric-judged retrieval audits. | v1.1 (fine-tune surface). |
| R-KNOWLEDGE-8 | Memory consolidation is batch. In-task consolidation infeasible; in-moment reasoning relies on Tier 1+2 only. | Low | High | Explicit query path for Tier 3 + Archive; consolidation cadence operator-tunable; lineage replay for cold facts. | v1.0 (baseline). |
| R-KNOWLEDGE-9 | Graph + presence overhead at scale. Every ambient event as a graph node may explode storage. | High | Medium | Pruning policy per tier; ambient-event tier transitions; per-env retention cap. | v1.0 (pruning); v1.1 (auto-tuning). |
| R-KNOWLEDGE-10 | GEPA reliability. Genetic search can produce regressions on non-stationary signals. | High | Medium | Anti-degradation safeguards (`02_PERSONA §9`); rollback discipline; human review gate for high-stakes domains; A-P16 acceptance test. | v1.0 (rollback); v1.1 (deeper anti-degradation). |
| R-KNOWLEDGE-11 | MeasurementFact + UncertaintyEnvelope rely on bridge calibration. Stale calibrations propagate wrong uncertainty. | High | Medium | CalibrationChain provenance (`§16a`); calibration interval enforcement at MeasurementFact admission; A-GF-MF acceptance test. | v1.0 (provenance); v1.1 (auto-renewal warnings). |

## 18a. Open questions

Per [`SPEC_CONVENTIONS.md §8`](SPEC_CONVENTIONS.md#8-open-questions).

| ID | Question | Owner | Resolves into |
|----|----------|-------|---------------|
| OQ-KNOWLEDGE-1 | Adapter conformance enforcement (R-KNOWLEDGE-4): docs-only, CI harness, or both? v1.1 ships harness — what's the test surface? | — | v1.1 harness design. |
| OQ-KNOWLEDGE-2 | Cross-encoder reranker fine-tuning (R-KNOWLEDGE-7): per-domain weights, or per-persona personalisation? Trade-off: storage cost vs retrieval precision. | — | v1.1 fine-tune scheme. |
| OQ-KNOWLEDGE-3 | Memory consolidation cadence: per-task, per-session, per-cohort sweep, or driven by retrieval-rate signals? v1.0 ships batch; v1.1 may add adaptive. | — | v1.1 cadence policy. |
| OQ-KNOWLEDGE-4 | Graph-memory pruning policy (R-KNOWLEDGE-9): time-based, importance-based, retrieval-frequency-based, or composite? | — | v1.1 pruning. |
| OQ-KNOWLEDGE-5 | GEPA + MIPROv2 budget per persona (R-KNOWLEDGE-5): operator-tunable, or per-persona maturity-scaled? | Prompt engineers | v1.1 budget policy. |
| OQ-KNOWLEDGE-6 | MeasurementFact + UncertaintyEnvelope: do we ship a small standard library of common uncertainty distributions (Gaussian, lognormal, uniform, Student's t), or leave to per-domain plugins? | Domain curators | v1.1 distribution library. |
| OQ-KNOWLEDGE-7 | Hierarchical Graph Memory (`§7`): what's the canonical node-merge protocol when two personas independently observe the same entity? Currently one-shot dedup; would semantic clustering help? | — | v1.2 cluster merge. |

## 19. Acceptance tests

```text
A-TX1   Five-tier ontology: every entity classified exactly once.
A-TX2   Skill spans Capability + Knowledge; retrievable via both
        find_skill (knowledge) and tool listing (capability) APIs.
A-TX3   Four tool classes (kernel-native, domain-required,
        persona-learned, human-bridged) composable; allowed_tools
        intersection works.
A-TX4   Lesson vs Reflective vs ProvenFact: distinct lifecycles
        and indexing; promotion from reflective → Lesson signed.
A-TX5   K-line / Skill / ProvenFact distinction enforced.
A-TX6   Seven-scope memory tagging; retrieval composes scope context.
A-TX7   Retrieval score formula deterministic; tie-breaking documented.
A-TX8   Cross-scope transferable flag enables retrieval; anti-leakage
        blocks differing user_id.
A-TX9   Per-persona projection: same task, two personas, different
        envelope context.
A-TX10  MCP alignment: every v1.0 tool invokable as MCP tool.
A-TX11  A2A alignment: PersonaCard projects to AgentCard with
        skills[], project_summary, env_summary populated.
A-TX12  Anthropic cache_control: layers 1-2 cacheable=True;
        cache hit rate ≥ 80% at runtime.
A-TX13  OTel: spans with personaos.* on every kernel operation;
        cross-boundary propagation.
A-TX14  Retrieval latency: hot ≤ 50 ms, warm ≤ 100 ms,
        multi-scope composition ≤ 100 ms p95.
A-TX15  Adapter compat: all 12 adapters accept v1.0 envelopes;
        ignore unknown fields; prior-shape outputs.
A-TX16  GEPA produces Pareto-improving tactic candidates within
        10 rollouts.
A-TX17  MIPROv2 cold-start: converges within 50 Bayesian iterations.
A-TX18  Reflection promotion: requires M=5 future tasks corroboration.
A-TX19  Anti-degradation: MAP-Elites diversity (v1.3+) prevents
        homogenisation.
A-TX20  Hierarchical Graph Memory: Tier 1 topic + Tier 2 events +
        Tier 3 subgraph; replay reproducible.
A-TX21  K-line / Skill / ProvenFact / Lesson distinction matrix
        enforced; each entity classified by exactly one origin and
        tier-dual flag.
A-TX22  Reflection retrieval: top-K lessons fetched at envelope-mint
        via vector_index with tier+provenance filter; rendered into
        LAYER 4 of 5-layer prompt assembly.
A-TX23  Lesson → Tactic promotion: ≥ N=5 citations across ≥ M=3
        distinct tasks triggers tactic_propose; operationality +
        charter-conformance gate; kernel signs.
A-TX24  Per-channel tactic evolution: separate EVOLVE-BLOCK regions
        for blackboard, DM, provenfacts, candidatetable, goalstack,
        ambient_stream, presence; signal corroboration per channel.
A-TX25  Per-channel cosine-similarity check refuses paraphrase
        within same channel; allows similar trigger in different
        channels.
```

## 20. Where to read next

- Persona that uses knowledge: [`02_PERSONA.md`](02_PERSONA.md)
- Project where knowledge is applied: [`04_PROJECT.md`](04_PROJECT.md)
- Domain (knowledge ingestion + tool discovery): [`06_DOMAIN.md`](06_DOMAIN.md)
- Protocols (MCP for retrieval): [`09_PROTOCOLS.md`](09_PROTOCOLS.md)

## Technical Appendix

The appendices below contain the full technical schemas, data structures, diagrams, and specification tables referenced throughout this document. Each appendix is referenced from the section where it applies.

### A.1 Five-tier ontology listing

<a id="appendix-a1"></a>

```text
1. COORDINATION TIER  — where work happens, who does it
   Environment, Project, Task, Cohort, OpenProblem, Milestone

2. PRODUCT TIER       — what is produced
   Artefact, ArtifactBundle, ProvenFact, Conjecture, Reflection,
   InternalCredit, ExternalCitation, StructuredFeedback

3. CAPABILITY TIER    — what is used to act
   Tool (4 classes), Skill (Voyager; both Capability + Knowledge),
   Tactic (EVOLVE-BLOCK), Meta-prompt, Rubric, VerifierRecipe,
   JudgePanelTemplate

4. KNOWLEDGE TIER     — what is read to inform
   Memory (episodic/semantic/reflective), Lesson, K-line, KnowledgeRef,
   StandardRef, NotationConvention, AmbientEvent, ProvenFact (dual)

5. CONTEXT TIER       — state about who/where/relationship
   Persona, RelationshipRecord, ProjectMember, EnvironmentMembership,
   Obligation, Disagreement, PeerReview, Consent/Boundary,
   PresenceState, MoodState, AttentionBudget, DomainContext,
   ConversationThread
```

### A.2 Eight knowledge artefact types

<a id="appendix-a2"></a>

```text
TACTIC               EVOLVE-BLOCK heuristic in SOUL.md
                     "When X happens, do Y."
                     Per-persona; signed mutations.

SKILL                Voyager-style executable code in soul.state.json
                     skill_library. Both Capability (runs) and Knowledge
                     (learned).

TOOL (ToolArtifact)  Promoted code via FSM:
                     PROPOSED → SANDBOXED → VERIFIED → PROMOTED → REVOKED
                     Four classes (§5.5):
                       A. kernel-native (mcp__personaos__*)
                       B. domain-required (in DomainContext)
                       C. persona-learned (Voyager; per-persona)
                       D. human-bridged (BridgeAsset; v1.0)

RUBRIC (RubricBundle) Judgment criteria with dimensions and weights.
                     Used by JudgePanel for PANEL_ACCEPT pathway.

LESSON               Work-pattern reflection.
                     About: a tactic or pattern that worked.
                     Structure: trigger / action / rationale / base_confidence /
                                citations.
                     Indexed globally; retrievable via find_lesson.

K-LINE               Topology + skill replay pattern.
                     "Tasks like X have been solved by team Y + skill Z."
                     Historian persona authors.
                     Used at orient time for fast-path replay.

PROVENFACT           Verified statement.
                     Author: kernel (on verifier verdict).
                     Structure: statement + evidence + verifier_id +
                                provenance.
                     CRDT G-set; task-scope, project-scope, env-scope.
                     Both Product AND Knowledge tier.

META-PROMPT          Tactic-generation template.
                     Operator-curated in v1.0; auto-mutated in v1.3+.
```

### A.3 Three memory types

<a id="appendix-a3"></a>

```text
EPISODIC          Raw events with timestamp, context, counterparty,
                  mood, original wording.
                  e.g., "On 2026-05-12, user01ABC said 'I'm exhausted'
                  before asking about migration."
                  Decay: τ-half-life by usage_frequency ×
                         emotional_weight × recency.

SEMANTIC          Consolidated facts and lessons abstracted from
                  episodics.
                  No raw quotes; facts and consents.
                  e.g., "user01ABC tends to work tired on Tuesdays.
                  He prefers concrete examples to abstractions."
                  Decay: only on contradiction; otherwise persistent.

REFLECTIVE        Park-style higher-level inferences.
                  e.g., "I have been most useful to user01ABC when
                  I stop falsifying and ask about state first."
                  Decay: only via explicit retirement.
```

### A.4 Consolidation pipeline and importance weighting

<a id="appendix-a4"></a>

```text
event happens
    ▼
episodic memory written (always; timestamped; signed)
    ▼
PERIODIC SWEEP (kernel: hourly or on idle)
    ▼
semantic consolidation
    LLM-summarise N episodics about same counterparty/topic
    drop original quotes; keep facts and consents
    ▼
REFLECTIVE CONSOLIDATION (weekly or after K tasks)
    LLM-reflect over recent semantics
    generate higher-level inferences about self/others/work
    each reflection signed; counts toward Reflector mode credit
```

```python
def importance(memory):
    return (
        memory.verifier_signal_count * 0.4 +
        memory.cross_reference_count * 0.3 +
        memory.salience_score        * 0.2 +
        memory.recency_score         * 0.1
    )

# Nightly batch:
for memory in tier:
    if memory.tier == "RECENT" and memory.age > RECENT_TTL:
        memory.tier = "WARM"
    elif memory.tier == "WARM" and memory.importance() < FORGET_THRESHOLD:
        memory.tier = "COLD"   # essentially forgotten
        emit_signed(MEMORY_DEMOTED)
    elif memory.tier == "COLD" and memory.importance() < ARCHIVE_THRESHOLD:
        memory.tier = "ARCHIVE"
```

### A.5 Lesson dataclass

<a id="appendix-a5"></a>

```python
@dataclass(frozen=True)
class Lesson:
    schema: Literal["lesson/1"]
    id: str
    persona_id: str
    authored_at_task: str             # task_id
    role_at_authoring: str            # role_slot
    fingerprint: bytes                # embed(triggering task)
    trigger: str                      # measurable trigger
    action: str                       # measurable action
    rationale: str                    # one-line "why"
    base_confidence: float            # (cited_in_accepted + 1) /
                                      # (cited + 2)
    citations: list[str]              # task_ids that cited this lesson
    parent_lineage: list[str]         # lessons it derives from
    signed: bytes
```

### A.6 Lesson retrieval at envelope-mint

<a id="appendix-a6"></a>

```python
candidate_lessons = vector_index.search(
    embedding = embed(task.statement + task.invariant_set),
    filter    = {tier: ["RECENT", "WARM"], min_provenance: 0.3},
    k         = 8,
)
```

### A.7 Lesson to Tactic promotion gate

<a id="appendix-a7"></a>

```text
1. Citation threshold met (N≥5, M≥3 distinct tasks).
2. Operationality check passes (02_PERSONA.md §8):
   - measurable trigger
   - measurable action
   - no contradiction with active ProvenFacts
   - not cosine-similar paraphrase of existing tactic
3. Charter-conformance check passes (v1.0 §14.1).
4. Kernel emits PROPOSED tactic_propose mutation; persona signs.
5. EVOLVE-BLOCK admits the tactic; future envelopes carry it as command.
```

### A.8 Four memory tiers

<a id="appendix-a8"></a>

```text
RECENT   (0-14 days)     provenance ≥ 0.6   weight 1.0
WARM     (14-90 days)    provenance ≥ 0.3   weight 0.7
COLD     (90 d - 1 yr)   provenance ≥ 0.1   weight 0.3
ARCHIVE  (> 1 yr)        any                 weight 0.05
```

### A.9 ScopeTags dataclass and cross-scope flags

<a id="appendix-a9"></a>

```python
@dataclass
class ScopeTags:
    user_id: str | None             # which user (privacy-bounded)
    persona_id: str                  # whose memory it is
    session_id: str | None           # session-bound (rare for knowledge)
    project_id: str | None           # project-scoped
    environment_id: str | None       # env-scoped
    app_id: str | None               # deployment-scoped
    org_id: str | None               # organisation-scoped
    relationship_id: str | None      # — pair-scoped
                                     # memory tied to a
                                     # PersonaRelationshipEdge
                                     # (02_PERSONA §11.4); null for
                                     # non-pair memories
```

```text
cross_project_transferable: bool
cross_env_transferable: bool
cross_persona_transferable: bool
cross_domain_transferable: bool
cross_relationship_transferable: bool  joint memory survives
                                                  edge `ended`; default
                                                  false
```

### A.10 Unified provenance score formula

<a id="appendix-a10"></a>

```text
provenance_score = base_confidence × age_decay × verifier_consistency × usage_signal

where:
  base_confidence       initial trust at creation
  age_decay             1 / (1 + days_since_created/half_life)
  verifier_consistency  ratio of verified vs contradicted uses
  usage_signal          log1p(times_cited_in_successful_work)
```

### A.11 SupersessionCascade and CascadeAffectedClaim schemas

<a id="appendix-a11"></a>

```python
@dataclass
class SupersessionCascade:
    schema: str = "supersession-cascade/1"
    cascade_id: str                           # ULID
    superseded_ref_id: str                    # KnowledgeRef that was
                                              # superseded
    superseding_ref_id: str                   # KnowledgeRef that
                                              # supersedes it
    triggered_at: datetime

    # DISCOUNT FACTORS
    direct_discount: float = 0.5              # provenance_score *= 0.5
                                              # for claims citing the
                                              # superseded ref directly
    transitive_discount: float = 0.25         # for claims citing claims
                                              # that cite the superseded
                                              # ref (depth 2+)
    max_cascade_depth: int = 3                # prevent unbounded graph
                                              # traversal

    # AFFECTED CLAIMS (populated by kernel on execution)
    affected_claims: list[CascadeAffectedClaim] = field(
        default_factory=list
    )
    affected_count: int = 0

    # RATE LIMITING
    # Max 1 cascade per KnowledgeRef per 24h window; prevents
    # cascade storms when multiple supersession events fire
    # for the same ref in rapid succession.
    rate_limit_window_hours: int = 24

    signed_by: bytes = b""


@dataclass
class CascadeAffectedClaim:
    schema: str = "cascade-affected-claim/1"
    claim_ref: str                            # ProvenFact, ProposedKind,
                                              # VerifierRecipe, etc.
    claim_kind: str                           # "proven_fact",
                                              # "proposed_kind", etc.
    prior_provenance_score: float
    discounted_provenance_score: float
    cascade_depth: int                        # 1 = direct, 2+ =
                                              # transitive
    status: Literal["discounted",
                     "re_confirmed",
                     "further_downgraded"] = "discounted"
    re_evaluated_by: str | None = None        # persona_id if manually
                                              # re-evaluated
    re_evaluated_at: datetime | None = None
```

### A.12 Hybrid retrieval six-stage pipeline diagram

<a id="appendix-a12"></a>

```text
┌────────────────────────────────────────────────────────────────────┐
│                  v1.0 HYBRID RETRIEVAL STACK                         │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Query (with scope context + intent + persona context)              │
│         │                                                            │
│         ├──► STAGE 1: Structured filter                              │
│         │     - seven-scope tag filter                               │
│         │     - type filter                                          │
│         │     - tier filter                                          │
│         │     - provenance threshold                                 │
│         │     - charter-compatibility filter                         │
│         │     (cheap; eliminates 99% of corpus)                      │
│         │                                                            │
│         ├──► STAGE 2: Vector retrieval                               │
│         │     - dense embedding similarity (top-K=50)                │
│         │     - over filtered corpus                                 │
│         │     - per-type embedding index                             │
│         │                                                            │
│         ├──► STAGE 3: Graph retrieval                                │
│         │     - multi-hop traversal over hierarchical graph memory   │
│         │     - global Topic Associative Network +                   │
│         │       local Event Progression Graphs                       │
│         │     - returns top-K_g (20) graph-relevant entries          │
│         │                                                            │
│         ├──► STAGE 4: Fusion                                         │
│         │     - reciprocal rank fusion (RRF) over vector + graph     │
│         │                                                            │
│         ├──► STAGE 5: Cross-encoder rerank                           │
│         │     - small cross-encoder over top-K_fused                 │
│         │     - returns top-K_final (10) with relevance scores       │
│         │                                                            │
│         └──► STAGE 6: Per-persona composition                        │
│               - apply observation surface filter                     │
│               - apply role/charter compatibility filter              │
│               - compose into envelope context block                  │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### A.13 Retrieval composition formula

<a id="appendix-a13"></a>

```text
final_score = base_vector_similarity
            × tier_weight
            × Π scope_match[scope]
            × cross_encoder_relevance
            × graph_boost
            × (1 + reuse_signal)
            × (1 - recency_penalty)
            × stage_weight                          # promotion stage
            × (1 if charter_compatible else 0)
            × (1 if observation_surface_allows else 0)
```

### A.14 Stage-aware ranking weights

<a id="appendix-a14"></a>

```python
stage_weight = {
    "EMERGENT":      0.5,
    "RECOGNISED":    0.7,
    "AUTHORITATIVE": 0.9,
    "STANDARDISED":  1.0,
    "DEPRECATED":    0.2,
    "TOMBSTONED":    0.0
}[entry.stage]
```

### A.15 Hierarchical Graph Memory tiers

<a id="appendix-a15"></a>

```text
TIER 1: GLOBAL TOPIC ASSOCIATIVE NETWORK
  Entity-level graph of domain concepts.
  Persistent across all projects + envs in deployment.
  Updated nightly via community detection over recent ambient streams.
  Used for: cross-domain transfer queries, novelty checks, broad
            topic exploration.
  
  Example: "power_electronics" topic node connects to: "buck", "boost",
  "flyback", "controller", "feedback_compensation", "thermal", "EMI",
  ... Edges weighted by co-occurrence in verified outcomes.

TIER 2: LOCAL EVENT PROGRESSION GRAPHS
  Per-project + per-env subgraphs.
  Entity-level: artifacts, conjectures, obligations, members.
  Temporal edges: "preceded_by", "caused_by", "responded_to",
                  "co-edited_with".
  Relationship edges: "contradicts", "supports", "extends", "cites".
  Used for: multi-hop reasoning ("the conjecture's evidence chain"),
            temporal queries ("what changed in this env over the last
            month?"), causal reasoning.

TIER 3: PER-MEMBERSHIP OBSERVATION SUBGRAPH
  Each persona's view of project + env.
  Filtered by observation surface + role + charter.
  Kernel-composed at envelope mint.
  Used for: persona-specific situational awareness.
```

### A.16 Per-persona retrieval composition (build_persona_view)

<a id="appendix-a16"></a>

```python
def build_persona_view(persona, task, project, env):
    membership_project = project.members.get(persona.persona_id)
    membership_env = env.members.get(persona.persona_id)
    surface = membership_env.observation_surface if membership_env else None
    
    return PersonaProjectedView(
        # Filtered project state
        open_problems_summary = filter_by_role(
            project.open_problems, role=membership_project.role,
            relevance_to=task.fingerprint
        ),
        active_obligations_self = [
            o for o in project.obligations
            if o.obligor_persona_id == persona.persona_id
        ],
        active_obligations_owed_to_self = [
            o for o in project.obligations
            if o.obligee == persona.persona_id
        ],
        active_disagreements_relevant = [
            d for d in project.disagreements
            if persona.persona_id in d.positions_held_by_any
        ],
        relevant_conjectures = [
            c for c in project.conjectures
            if persona.persona_id in c.contributors
            or persona.persona_id in c.assigned_proof_gaps
        ],
        open_peer_reviews_self_is_author = ...,
        open_peer_reviews_self_is_reviewer = ...,
        
        # Filtered ambient (env)
        recent_ambient_summary = condense(
            env.ambient_event_stream.recent(),
            filter=surface,
            relevance_to=task.fingerprint
        ),
        other_present_members = [
            MemberSummary(m) for m in env.members.values()
            if m.persona_id != persona.persona_id
            and m.observable_to(persona)
        ],
        
        # Persona's OWN memory
        relevant_memory = retrieve(
            scope_context={
                "persona_id": persona.persona_id,
                "project_id": project.project_id if project else None,
                "environment_id": env.environment_id if env else None,
            },
            relevance_to=task.fingerprint,
            top_k=20
        ),
        
        # Shared substrate
        relevant_proven_facts = retrieve_proven_facts(
            scopes=["project", "env"],
            relevance_to=task.fingerprint,
            top_k=15
        ),
        relevant_conventions = (env.conventions | project.conventions),
        
        # Operational state
        attention_budget_remaining = persona.attention_budget.in_env(env),
        energy_remaining = membership_env.presence_state.energy_remaining,
        active_mode = task.active_mode,
        active_pathway = task.acceptance_pathway,
    )
```

### A.17 Two personas, same project, different views

<a id="appendix-a17"></a>

```text
VOLT'S VIEW:
  active_mode = experimenter
  pathway = VERIFIER_ACCEPT
  obligations_self: 3 (topology, BOM, EMI compliance)
  recent_ambient: design_v3 in draft; Volt's edits yesterday
  relevant_conjectures: phase margin claim (Volt proposed; challenged)
  relevant_memory: Volt's lessons from prior buck designs;
                    skill: buck_compensation_type2
  open_problems_shown: topology selection, EMI compliance

SAGE'S VIEW:
  active_mode = historian
  pathway = INTERACTIVE (Sage informs)
  obligations_self: 1 (literature survey by Thursday)
  recent_ambient: design_v3 + cited Vishay AN-1234 yesterday
  relevant_conjectures: same compensation conjecture (Sage's lens:
                          prior art)
  relevant_memory: Sage's lessons from compensating power designs;
                    K-lines on compensation design problems
  open_problems_shown: same skeleton; Sage observes all
```

### A.18 Persona's own curation categories

<a id="appendix-a18"></a>

```text
Personal episodic memory       persona writes (consent-gated for user
                                involving); kernel signs
Personal semantic memory       kernel-consolidated from episodics;
                                persona may request consolidation
Personal reflective memory     Reflector mode produces; confirmed by
                                future signals
Skill library                  persona-authored via skill_synthesise
                                / skill_compose
Tactic EVOLVE-BLOCK            mutation operators; signal-weighted
                                promotion
Mode proficiencies             update_mode_proficiency operator
Personal goals                 persona-proposed; charter-checked
Observation surface evolution  persona-proposed via env admin
```

### A.19 ScopedKnowledgeQuery schema and admission rules

<a id="appendix-a19"></a>

```python
@dataclass
class ScopedKnowledgeQuery:
    schema: str = "scoped-knowledge-query/1"
    query_id: str
    requested_by: str                            # caller persona / operator /
                                                 # external surface

    # Scope spec — explicit subset of ScopeTags (§5).  Each set field
    # narrows the query; null fields are unconstrained.
    scope: ScopeTags

    # Type + tier filters
    type_filter: list[str] | None                # type axis values (§5)
    tier_filter: list[Literal[
        "RECENT", "WARM", "COLD", "ARCHIVE"]] | None

    # Cross-scope inclusions
    include_cross_project_transferable: bool = False
    include_cross_env_transferable: bool = False
    include_cross_persona_transferable: bool = False
    include_cross_domain_transferable: bool = False
    include_cross_relationship_transferable: bool = False

    # Result shape
    top_k: int = 50
    return_provenance: bool = True               # include unified provenance
                                                 # score (§6) per entry
    return_lineage_refs: bool = False            # include LineageGraph
                                                 # back-refs (audit use)

    # Admission
    requires_consent_check: bool = True          # honour user consent /
                                                 # operator policy on
                                                 # scope-tagged memories
    signed_by: bytes
```

```text
1. CONSENT GATE
   For any scope tag containing a user_id, the kernel runs the
   §11 consent check before returning entries (memory transparency
   is consent-gated; sharing with non-self callers requires the
   user's may_share_with_other_personas consent).

2. SCOPE INTERSECTION
   The returned set is the strict intersection of scope tags
   supplied.  Empty-scope queries are refused (null scope ≠ empty
   scope — omit the field to leave it unconstrained).

3. CROSS-SCOPE FLAGS HONOURED
   include_cross_*_transferable expands the result set only to
   entries that carry the matching cross-flag (§5 promotion).
   The substrate never returns an entry whose cross-flag is False
   under a cross-scope inclusion request.

4. RELATIONSHIP SCOPE
   scope.relationship_id (§5) returns entries
   tagged with that relationship_id — the pair-scoped memory
   carved out in PersonaRelationshipEdge (02_PERSONA §11.4)
   co-signed summaries and joint-event reflections.  Both pair
   members may query the same relationship_id; non-pair callers
   require operator scope.
```

### A.20 Five-layer prompt assembly

<a id="appendix-a20"></a>

```text
LAYER 1 (FROZEN; cacheable=True)
  - Persona identity (SOUL.md frozen sections)
  - Charter
  - Voice + style
  - Primary disposition

LAYER 2 (EVOLVABLE; per EVOLVE-BLOCK; cacheable=True if stable)
  - Evolved tactics
  - Communication style preferences
  - Mode-specific patterns

LAYER 3 (CONTEXTUAL; cacheable=False)
  - Project context block
  - Env context block
  - Relationship context block
  - Mood + presence state

LAYER 4 (RETRIEVED; cacheable=False)
  - Own memory (top-K)
  - Relevant skills / lessons / K-lines
  - Domain knowledge (top-K)
  - Recent ambient events

LAYER 5 (TASK; cacheable=False)
  - Task statement
  - Acceptance pathway hint
  - Active mode hint
  - Output schema constraints
```

### A.21 GEPA overview

<a id="appendix-a21"></a>

```text
GEPA (Genetic-Pareto, 2025):
  - Reflects on execution traces (reasoning paths, tool outputs,
    compiler errors)
  - Uses natural language feedback to evolve prompts
  - Multi-objective Pareto search across:
      verifier pass rate
      cost
      latency
      charter conformance
  - Outperforms MIPROv2 by 10%, GRPO by 20%, 35× fewer rollouts
```

### A.22 v1.0 GEPA integration

<a id="appendix-a22"></a>

```python
class GEPA:
    def optimize(self, persona, evolve_block_section, observed_failures):
        # 1. Gather execution traces from recent task lineages
        traces = collect_traces(persona, recent_tasks=100)
        
        # 2. Extract per trace:
        feedback = []
        for trace in traces:
            feedback.append({
                "tactic": trace.tactic,
                "outcome": trace.outcome,
                "signal_weight": signal_weight(trace.outcome.kind),
                "natural_language_reflection": reflector_mode.reflect(trace),
            })
        
        # 3. GEPA mutates the EVOLVE-BLOCK
        proposed_tactics = gepa.evolve(
            current=evolve_block_section,
            traces=traces,
            feedback=feedback,
            objectives=[
                "verifier pass rate ↑",
                "cost ↓",
                "latency ↓",
                "charter conformance ≥ 0.95",
            ],
            pareto_front=True,
            rollouts=10,  # GEPA is sample-efficient
        )
        
        # 4. Promote candidates that improve Pareto front
        for tactic in proposed_tactics:
            if tactic.improves_pareto(current, signal_threshold=0.05):
                kernel.propose_tactic_mutation(
                    persona, tactic,
                    operator="dspy_gepa@v3",
                    evidence=feedback
                )
```

### A.23 MIPROv2 two-phase overview

<a id="appendix-a23"></a>

```text
PHASE 1 (PROPOSAL):
  Generate K=12 instruction candidates per tactic / skill
  (LLM-generated; cost-bounded).

PHASE 2 (BAYESIAN OPTIMIZATION):
  Bayesian search over (instruction, demonstration) combinations.
  Each combination tested against held-out signals.
  Best candidate becomes new tactic.
```

### A.24 v1.0 MIPROv2 integration

<a id="appendix-a24"></a>

```python
class MIPROv2:
    def optimize_tactic(self, persona, tactic_id):
        candidates = []
        for k in range(12):
            instruction = llm.propose_instruction(
                base_tactic=tactic,
                feedback=recent_traces,
                charter=persona.charter,
            )
            candidates.append(instruction)
        
        demos = select_demos(persona.skill_library, tactic, n=4)
        
        best = bayesian_optimize(
            candidates=candidates,
            demos=demos,
            objective_fn=lambda cfg: hold_out_eval(persona, cfg),
            iterations=50,
        )
        return best
```

### A.25 Reflection-driven refinement schedule and confirmation

<a id="appendix-a25"></a>

```text
SCHEDULE:
  - every N tasks (default 20): per-persona task-level reflection
  - per-session at boundary: synthesize patterns
  - at project milestones: project-level reflection
  - at multi-project horizon: cross-project insight

OUTPUTS:
  - candidate tactic mutations (handed to GEPA)
  - candidate skill promotions
  - candidate charter refinement (NOT auto-applied; operator review)
  - meta-prompts (template updates)

CONFIRMATION:
  Candidates MARKED, not auto-promoted.
  Promotion requires:
    - signal confirmation over next M tasks (M ≥ 5)
    - charter conformance check
    - cross-persona similarity audit (anti-collapse)
    - sign-off by kernel + operator (if material)
```

### A.26 Per-persona evolution cycle

<a id="appendix-a26"></a>

```text
EVOLUTION CYCLE:

task → outcome → signal extraction
    ▼
GEPA reflects → proposes tactic mutations
    ▼
confirmation gate (signal corroboration over time)
    ▼
promoted into EVOLVE-BLOCK
    ▼
next envelope mint uses new tactics
    ▼
(cycle continues)
```

### A.27 Anti-degradation safeguards

<a id="appendix-a27"></a>

```text
MAP-Elites (v1.3+)         Tactic archive maintains diverse cells.

Diversity penalty           weight *= (1 - max_cosine_to_recent_children)
in parent sampling          Disfavours parents with similar children.

Cross-persona audit         Every N tasks: pairwise similarity.
                            If converged > τ, roll back.

Charter conformance scan    ≥ 0.95 across sampled actions.
                            Else CHARTER_DRIFT_DETECTED.

Voice consistency scan      ≥ 0.9 vs declared voice.
                            Else VOICE_DRIFT_DETECTED.

Refusal rate                in expected range; outliers flagged.

REINSTATEMENT
  If evolution degrades, kernel rolls back to previous EVOLVE-BLOCK
  version (signed signature; tactic_retire operator).
```

### A.28 Per-channel tactic evolution blocks and mutation rules

<a id="appendix-a28"></a>

```text
EVOLVE-BLOCK: communication.blackboard    [scope=team_clinic]
  - tactics about broadcast: when to write events, addressing,
    threading, summarisation cadence.

EVOLVE-BLOCK: communication.directmessage [scope=persona_pair]
  - tactics about direct messaging: when to DM vs broadcast,
    target selection, back-pressure handling.

EVOLVE-BLOCK: communication.provenfacts   [scope=project]
  - tactics about CRDT writes: assertion phrasing, evidence-attachment
    discipline, when to propose vs cite.

EVOLVE-BLOCK: communication.candidatetable [scope=task]
  - tactics about candidate authoring: dimension addressing, when to
    RESAMPLE_REQUEST vs propose new candidate.

EVOLVE-BLOCK: communication.goalstack     [scope=task]
  - tactics about goal-mediated coordination: when to push sub-goals,
    pop completion, observe pressure.
```

```text
EVOLVE-BLOCK: communication.ambient_stream [scope=env]
  - tactics about ambient event emission: cadence, summarisation,
    cross-env link assertions.

EVOLVE-BLOCK: communication.presence       [scope=env]
  - tactics about presence updates: when to enter, when to depart,
    energy-budget signalling.
```

```text
1. Measurable trigger (the line says WHEN).
2. Measurable action (the line says WHAT).
3. No contradiction with ProvenFacts in the same scope.
4. No cosine-similar paraphrase of an existing tactic in the
   same channel block.
5. Signed mutation, lineage-linked.
6. Per-channel signal corroboration:
   - blackboard tactics signal-weighted by addressed-persona acceptance
     of subsequent events.
   - DM tactics signal-weighted by reply latency + recipient acceptance.
   - ProvenFacts tactics signal-weighted by CRDT-merge acceptance.
   - CandidateTable tactics signal-weighted by acceptance pathway result.
```

### A.29 Anti-Goodhart tactic promotion rules

<a id="appendix-a29"></a>

```text
TACTIC PROMOTION (into EVOLVE-BLOCK):

Convergent / Divergent modes:
  - verified outcome alone (weight ≥ 1.0) → promote.
  - judged outcome alone (weight ≥ 0.7) → promote.

Relational / Pedagogic / Performative modes:
  - verified outcome alone → promote (rare).
  - judged outcome + user feedback → promote.
  - user feedback alone → DO NOT PROMOTE (insufficient diversity).
  - engagement signal alone → DO NOT PROMOTE under any circumstance.
  - engagement + user feedback + audit clearance → PROMOTE WITH NOTE.

Universal:
  - reflection alone → do not promote; awaiting corroboration.
```

### A.30 Mutation operators listing (22 total)

<a id="appendix-a30"></a>

```text
Core (9):
  tactic_propose       tactic_retire        skill_synthesise
  skill_compose        meta_prompt_mutate   crossover
  fork_clone           fork_compose         retire_proposal

Relational/evolution (6):
  relational_style_propose   mode_proficiency_update
  reflection_synthesise      trust_signal_apply
  consolidation              forgetting

Domain emergence (5):
  probe_initiate             knowledge_ingest
  recipe_infer               convention_propose
  cross_domain_transfer

v1.0 (2):
  project_role_propose       domain_skill_propose
```

### A.31 UncertaintyEnvelope schema

<a id="appendix-a31"></a>

```python
@dataclass
class UncertaintyEnvelope:
    schema: str = "uncertainty-envelope/1"
    envelope_id: str

    # Substrate-shape Literal: these are mathematical distribution shapes,
    # NOT domain categories.  Math is universal; the substrate may name
    # them.  Additional shapes proposable via ProposedFactKind →
    # MetaRegistry promotion (e.g. heavy-tailed, multi-modal).
    distribution_kind: Literal["gaussian",
                                 "lognormal",
                                 "uniform_bounded",
                                 "interval_only",
                                 "empirical_samples",
                                 "custom_kind"]
    custom_distribution_kind: str | None    # KindRegistry-resolved when
                                            # distribution_kind = "custom_kind"

    central_value: float

    # Distribution-specific fields; only the relevant ones are populated.
    std_dev: float | None
    samples: list[float] | None             # for empirical
    interval_low: float | None              # for uniform_bounded / interval_only
    interval_high: float | None
    confidence_level: float | None          # e.g. 0.95 for CI / coverage interval

    # Systematic error floor — "we cannot measure below this regardless
    # of statistical noise".  Calibration-driven.
    systematic_error_floor: float | None
    calibration_chain_ref: str | None       # CalibrationChain (04_PROJECT §26a.7)

    units_kind: str                         # KindRegistry-resolved unit
                                            # (substrate names no units;
                                            # operator / domain catalog).
                                            # Examples (illustrative): "us",
                                            # "MHz", "kPa", "mg/dL", "kg".

    signed_by: bytes
```

### A.32 MeasurementFact schema

<a id="appendix-a32"></a>

```python
@dataclass
class MeasurementFact:
    schema: str = "measurement-fact/1"
    fact_id: str
    proposed_by_persona_id: str
    proposed_at: datetime
    domain_id: str

    # WHAT was measured.  Substrate names no quantities.
    quantity_kind: str                      # KindRegistry-resolved
                                            # quantity_kind (06_DOMAIN §7.6).
                                            # Examples (illustrative, NOT
                                            # substrate enums) per-domain:
                                            #   "qubit_t1"
                                            #   "transmittance_at_wavelength"
                                            #   "blood_glucose_concentration"
                                            #   "tensile_strength"
                                            #   "switching_frequency"

    value: UncertaintyEnvelopeRef           # MUST be a typed reference to
                                            # an UncertaintyEnvelope (16a.1);
                                            # admission validates the ref
                                            # resolves and the envelope's
                                            # schema is "uncertainty-envelope/1".
                                            # A bare-float claim for the same
                                            # quantity is REFUSED at admission
                                            # — file the claim as a plain
                                            # ProvenFact instead, which downstream
                                            # J4 treats at PANEL-grade.

    # WITH WHAT was it measured
    measurement_instrument_ref: str | None  # InstrumentAsset ref
                                            # (04_PROJECT §26a.7);
                                            # None when no specific
                                            # instrument applies (e.g.,
                                            # theoretical bound)
    measurement_protocol_ref: str           # ArtifactBundle ref describing
                                            # how the measurement was taken
    measurement_taken_at: datetime
    measurement_location_ref: str | None    # where (lab id, site)

    # Calibration provenance — derived from the instrument's chain
    calibration_expired_at_measurement: bool = False
                                            # set True when the instrument's
                                            # next_calibration_due was past
                                            # at measurement_taken_at; the
                                            # MeasurementFact is admissible
                                            # but downstream J4 caps at
                                            # PANEL-grade
    calibration_chain_ref: str | None       # the chain in effect at
                                            # measurement time

    # Replication status — links to §5.6.1 ReplicatedAttestation when
    # the measurement has been replicated
    replication_status: Literal["single_observation",
                                  "replicated_same_instrument",
                                  "replicated_disjoint_instruments",
                                  "blind_replicated"]
    replicated_attestation_ref: str | None  # ReplicatedAttestation ref

    # External attestation (engineer stamp / lab director sign-off)
    external_attestation_refs: list[str]    # ExternalAttestation refs
                                            # (04_PROJECT §26a.3)

    # Cross-reference to plain ProvenFact for legacy queries
    backed_proven_fact_ref: str | None

    signed_by: bytes
```

### A.33 MeasurementFact composition rules (J4)

<a id="appendix-a33"></a>

```text
J4-MEASUREMENT  Any candidate output whose claim is a numerical
                measurement MUST be backed by a MeasurementFact with
                a non-degenerate UncertaintyEnvelope to be admissible
                at VERIFIER_ACCEPT grade.  A bare-float claim is
                admissible only at PANEL_ACCEPT grade (judges weigh
                the absence of declared uncertainty).

J4-CALIBRATION  When measurement_instrument_ref is set:
                  - if calibration_expired_at_measurement = True:
                    PANEL-grade max; never VERIFIER-grade
                  - if instrument.current_operational_state ∈
                    {out_of_tolerance, quarantined, decommissioned}:
                    REFUSAL at admission (no MeasurementFact admitted)

J4-REPLICATION  Trust uplift on a MeasurementFact is read from its
                ReplicatedAttestation (when present) per the uplift
                schedule in 06_DOMAIN §5.6.1.  No replication ⇒
                trust capped by base attestation chain.

J4-UNITS        units_kind MUST resolve in KindRegistry at admission.
                Unresolved units emit `units_kind_unresolved` refusal;
                this prevents unit ambiguity from poisoning aggregation.
```

### A.34 Aggregation view and reproducibility classes

<a id="appendix-a34"></a>

```python
def aggregate_measurements(fact_refs: list[str],
                            aggregation_kind: str) -> UncertaintyEnvelope:
    """
    aggregation_kind resolves against KindRegistry.aggregation_kinds.
    Substrate names no aggregations.  Examples (illustrative):
      "weighted_mean", "median_with_iqr", "meta_analysis_random_effects",
      "best_estimate_with_systematic_floor".
    
    The aggregator is a persona-authored skill registered against the
    KindRegistry entry; substrate provides the view, not the algorithm.
    """
    ...
```

```text
reproducibility_class             criteria
─────────────────────             ─────────
  fully_reproducible              all constituents have
                                  measurement_protocol_ref + calibration_chain
                                  + replicated_disjoint_instruments
  partially_reproducible           ≥ 1 leg replicated; calibration present
  single_observation_only          no replication; one calibrated measurement
  underspecified                   missing calibration OR protocol;
                                   PANEL-grade max
```

### A.35 DerivationProvenanceEdge, DerivationProvenancePolicy, and admission rule

<a id="appendix-a35"></a>

```python
@dataclass
class DerivationProvenanceEdge:
    schema: str = "derivation-provenance-edge/1"
    edge_id: str

    # SOURCE — the contribution event that this edge originates from.
    # Any signed event that produces a new artefact, K-line, lesson,
    # ProjectItem, ProvenFact, OutcomeFeedback, or PeerReview turn
    # MAY emit DPE(s) per consulted memory.
    contribution_event_ref: str                  # signed event id
    contribution_event_kind: str                 # KindRegistry-resolved
                                                 # against derivation_event_kinds
                                                 # (MetaRegistry seeds:
                                                 # "artifact_minted",
                                                 # "kline_authored",
                                                 # "project_item_proposed",
                                                 # "proven_fact_authored",
                                                 # "peer_review_turn_authored").
    contribution_persona_id: str                 # who authored the contribution

    # TARGET — the memory that materially shaped the contribution.
    # MAY be any retrievable memory: KnowledgeRef, episodic memory entry,
    # semantic fact, K-line, lesson, ProvenFact, StandardRef.
    consulted_memory_ref: str                    # the source memory id
    consulted_memory_scope_tags: ScopeTags       # snapshot of the source's
                                                 # ScopeTags at consultation
                                                 # time (so audit answers
                                                 # "was the source org-tagged
                                                 # at the moment of consultation")

    # INFLUENCE — substrate-shape, persona-declared.  The persona
    # who authored the contribution declares the influence kind at edge
    # mint time.  No automated discovery is attempted (a persona who
    # recalled something tacitly cannot have it tagged — see honest limits).
    influence_kind: Literal["direct_quote",      # source text appears verbatim
                            "paraphrased",       # source claim restated
                            "structural_basis",  # source's method / structure used
                            "negative_example",  # source rejected; informs by contrast
                            "background_context"]
    influence_strength: float                    # 0..1; persona-declared

    # RETRIEVAL CONTEXT — the retrieval call that surfaced the memory.
    # When the retrieval went through §7 hybrid pipeline, the call is
    # OTel-spanned; the span id is recorded here for replay.
    retrieval_span_id: str | None                # null when the consultation
                                                 # was through in-context recall
                                                 # rather than retrieval call

    drafted_at: datetime
    signed_by: bytes                             # contribution_persona_id's kernel


@dataclass
class DerivationProvenancePolicy:
    schema: str = "derivation-provenance-policy/1"
    policy_id: str
    bound_to_env_id: str | None
    bound_to_project_id: str | None

    # Whether DPEs are mandatory or opportunistic.  Single-tenant envs default
    # to opportunistic (no enforcement); multi-tenant envs default to
    # mandatory_for_cross_principal (the substrate refuses to mint a
    # contribution that consulted a memory tagged with a different
    # principal_attribution_id without an accompanying DPE).
    enforcement_mode: Literal["off",
                              "opportunistic",
                              "mandatory_for_cross_principal",
                              "mandatory_all"]

    # Soft-bind on retrieval: when a memory is retrieved that would trigger
    # mandatory DPE on derivation, the kernel adds a span attribute marking
    # the memory; the persona's body sees the marker but is not blocked.
    soft_bind_attribute_kind: str = "dpe_required_on_derivation"

    declared_at: datetime
    declared_by_operator_id: str
    signed_by: bytes
```

```text
On contribution event mint (artifact_minted, kline_authored, etc.):
  1. Resolve the env's DerivationProvenancePolicy (or default per env type).
  2. If enforcement_mode = "off": no DPE check; proceed.
  3. If enforcement_mode = "opportunistic": persona may emit DPEs; no
     enforcement.
  4. If enforcement_mode = "mandatory_for_cross_principal":
       a. Inspect the contribution event's retrieval span list (OTel) for
          memories returned during the authoring session.
       b. For any memory whose ScopeTags include a principal_attribution_id
          (or org_id under operator policy mapping) DIFFERENT from the
          contribution's own principal_attribution_id:
            REFUSE the contribution event unless the persona has emitted
            a DerivationProvenanceEdge naming that memory, with refusal
            kind `dpe_required_for_cross_principal_derivation`.
       c. The persona may reply with influence_kind = "background_context"
          and influence_strength = 0 — substrate accepts the declaration
          but the lineage carries it for audit.
  5. If enforcement_mode = "mandatory_all":
       Step 4 applies regardless of cross-principal status.
```

### A.36 Cost and latency targets

<a id="appendix-a36"></a>

```text
RETRIEVAL PIPELINE
Stage 1 structured filter (100K corpus)              ≤ 10 ms p95
Stage 2 vector retrieval (top-K=50)                  ≤ 50 ms p95
Stage 3 graph retrieval (2-hop)                       ≤ 100 ms p95
Stage 4 fusion (RRF)                                  ≤ 5 ms
Stage 5 cross-encoder rerank                          ≤ 50 ms
Stage 6 persona composition                            ≤ 30 ms
TOTAL retrieval latency p95                           ≤ 250 ms

MEMORY OPERATIONS
Hot-tier retrieval (RECENT, 100K entries)             ≤ 50 ms p95
Warm-tier retrieval (WARM, 1M entries)                ≤ 100 ms p95
Cold-tier retrieval (full-corpus)                      ≤ 500 ms p95
Memory consolidation batch                             overnight / idle

PROMPT EVOLUTION
GEPA per-mutation cycle                                ~$1-10 / persona
                                                        / cycle
MIPROv2 cold-start tactic generation                  ~$5-30 per tactic
Reflection latency (per-task)                          ≤ 200 ms
Reflection latency (per-session)                       seconds
Reflection latency (per-project)                       minutes

CACHE HIT RATE (cache_control on layers 1-2)
Target                                                  ≥ 80%
Cost amortisation vs uncached                         ~10× savings
                                                        at scale
```
