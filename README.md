---
title: PersonaOS v1.0 — README
status: Stable
---

# PersonaOS v1.0 — Design Specification

**PersonaOS gives AI agents persistent identity, memory, safety, and coordination — so they can work in any domain, remember across sessions, and stay safe at scale.**

This document is your starting point. It orients you to the 14-file v1.0 specification and helps you find the right entry path for your background. Detailed conventions for documentation style are in [`SPEC_CONVENTIONS.md`](SPEC_CONVENTIONS.md); the normative specifications themselves live in `00_VISION.md` through `13_DESIGN_VALIDATION.md`.

v1.0 is the single, self-contained reference for PersonaOS. **Read v1.0 alone** — it is the authoritative design specification.

---

## What is PersonaOS?

PersonaOS is an **operating system for AI Personas**. Just as a traditional OS manages applications and files, PersonaOS manages *personas* — named AI characters that think, learn, remember, and collaborate. Each persona has a stable identity, skills that grow over time, and relationships with users and other personas.

**The problem it solves.** Today's AI agents are stateless, domain-rigid, and unsafe at scale. They forget between sessions, can't coordinate with other agents, have no verifiable safety boundaries, and require hand-coded logic for each new domain. PersonaOS addresses all four:

| Challenge | How PersonaOS solves it |
|---|---|
| **Agents forget between sessions** | Each AI Persona (a *persona*) has a stable identity, accumulated skills, and relationships that survive across sessions. Swap the underlying AI model — the persona's memory and skills transfer intact. |
| **Agents can't coordinate** | Personas work in *environments* — persistent shared workspaces where they discover how to coordinate through experience. A chip design lab develops tape-out ceremonies; a research lab develops peer-review processes. |
| **Agents can't handle new domains** | When a persona encounters an unfamiliar field, it bootstraps knowledge through structured discovery — ingesting sources, proposing domain-specific types, and accumulating trust through use. No one needs to pre-program "what a structural engineer does." |
| **Agents lack safety guarantees** | Eight safety checks run before every action. The strictest rule always wins. Every action is digitally signed and recorded in a tamper-proof audit trail. |

**Who is PersonaOS for?**

- **Researchers** building multi-agent systems
- **Framework developers** integrating AI Personas into existing tools (LangGraph, CrewAI, Claude Code, etc.)
- **Operators** deploying AI-assisted workflows in regulated or safety-critical domains
- **Anyone** who needs AI agents that remember, learn, coordinate, and stay safe over months of continuous work

## How it works (technical summary)

PersonaOS is built around five key mechanisms:

| Mechanism | What it does |
|---|---|
| **Personas** | Named AI Personas with seven layers (identity, capability, experience, relationships, mood, goals, voice) and 14 thinking styles. They produce work, learn from experience, and maintain relationships over time. |
| **The kernel** | The trusted core — a referee that owns identity, enforces safety, signs every action, and maintains a tamper-proof audit trail. The kernel never does creative work; it ensures that creative work is safe and accountable. |
| **Environments** | Persistent shared workspaces where personas live and coordinate. A *project workspace* is one type; others include solo desks, team rooms, research labs, debate forums, and companion chats. |
| **Domains** | Bodies of knowledge that personas build up for specific fields (chip design, medicine, construction). Domains emerge through use — no one hardcodes "what a structural engineer does." |
| **Knowledge & memory** | Structured memory (episodic, semantic, reflective) across four tiers with hybrid retrieval. Prompts evolve automatically to improve at specific tasks. |

**Standards.** PersonaOS speaks standard protocols — MCP for tools, A2A for agent-to-agent federation, OpenTelemetry for observability — and works inside 12 AI frameworks (Claude Code, OpenAI Agents SDK, LangGraph, CrewAI, and others) without losing identity or safety.

---

## Reading order

| # | File | What you'll learn | Read time |
|---|---|---|---|
| 0 | [`SPEC_CONVENTIONS.md`](SPEC_CONVENTIONS.md) | How these documents are written — formatting rules, normative language, and schema conventions. *Read this only if you are writing or reviewing the spec.* | 6 min |
| 1 | [`00_VISION.md`](00_VISION.md) | The big picture — what PersonaOS is trying to be, its non-negotiable design principles, and what is explicitly out of scope. | 12 min |
| 2 | [`01_KERNEL.md`](01_KERNEL.md) | The trusted core — safety checks, audit trail, digital signatures, and the rules enforced on every action. | 14 min |
| 3 | [`02_PERSONA.md`](02_PERSONA.md) | How AI Personas are structured — seven identity layers, 14 thinking styles, how personas learn and evolve over time. | 18 min |
| 4 | [`03_TASKS.md`](03_TASKS.md) | How work gets done — 10 types of work, 8 ways to decide when work is "done," and how tasks are routed. | 14 min |
| 5 | [`04_PROJECT.md`](04_PROJECT.md) | Long-running team work — milestones, obligations, peer review, physical assets, and multi-session collaboration. | 16 min |
| 6 | [`05_ENVIRONMENT.md`](05_ENVIRONMENT.md) | Shared workspaces — 9 room types, how personas join and leave, presence and attention, notifications, and event streams. | 16 min |
| 7 | [`06_DOMAIN.md`](06_DOMAIN.md) | How personas learn new fields — domain discovery, knowledge ingestion, tool discovery, safety extensions, and the four-stage trust ladder. | 18 min |
| 8 | [`07_ARTIFACTS.md`](07_ARTIFACTS.md) | Work products — how files and deliverables are structured, co-edited, verified, and shipped. | 12 min |
| 9 | [`08_KNOWLEDGE.md`](08_KNOWLEDGE.md) | Memory and learning — how personas remember, find relevant information, and improve their own prompts over time. | 18 min |
| 10 | [`09_PROTOCOLS.md`](09_PROTOCOLS.md) | Connecting to the outside world — MCP for tools, A2A for federation, 12 framework adapters, and cryptographic key management. | 14 min |
| 11 | [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md) | The test catalog — ~460 pass/fail criteria that prove the system works as specified. | 8 min |
| 12 | [`12_GLOSSARY.md`](12_GLOSSARY.md) | Reference dictionary — every PersonaOS term defined in one place. | 6 min |
| 13 | [`13_DESIGN_VALIDATION.md`](13_DESIGN_VALIDATION.md) | Real-world scenarios — concrete examples (build a house, design a chip, run a study) walked end-to-end against the design. | 8 min |
| 14 | [`14_DECISIONS.md`](14_DECISIONS.md) | Why the design is the way it is — 40+ architectural decision records explaining the trade-offs behind each major choice. | 10 min |
| 15 | [`15_COORDINATION_SHAPES.md`](15_COORDINATION_SHAPES.md) | *(v1.1 draft)* How AI Personas organise themselves — 5 building blocks for self-organising coordination within environments. | 12 min |

**Short on time?** Read just `00_VISION.md` (12 min) for the complete overview. Add `02_PERSONA.md` for how AI Personas are built. For a third file, pick the one closest to your interest: projects → `04_PROJECT.md`; shared workspaces → `05_ENVIRONMENT.md`; new domains → `06_DOMAIN.md`; memory → `08_KNOWLEDGE.md`.

---

---

## Start here (by role)

Pick the path that matches your background. Each gives you a focused reading list with estimated time.

---

### Researcher
*Understanding the theoretical model behind PersonaOS.*

1. This README (5 min)
2. [`02_PERSONA.md`](02_PERSONA.md) — how AI Personas are structured, learn, and evolve (18 min)
3. [`08_KNOWLEDGE.md`](08_KNOWLEDGE.md) — memory, retrieval, and prompt evolution (18 min)
4. [Research grounding](#research-grounding) below for source papers

### Framework developer
*Integrating PersonaOS into LangGraph, CrewAI, Claude Code, or another framework.*

1. This README (5 min)
2. [`09_PROTOCOLS.md`](09_PROTOCOLS.md) — protocols, 12 framework adapters, schema registry (14 min)
3. [`01_KERNEL.md`](01_KERNEL.md) — what the kernel guarantees and how signing works (14 min)

### Operator / deployment manager
*Running PersonaOS in a hospital, factory, school, or enterprise.*

1. This README (5 min)
2. [`00_VISION.md`](00_VISION.md) — design principles, safety commitments, scope (12 min)
3. [`05_ENVIRONMENT.md`](05_ENVIRONMENT.md) — setting up workspaces, charters, safety constraints (16 min)
4. [`01_KERNEL.md §2`](01_KERNEL.md) — the 8 safety checks (operator policy = check #4)

### Contributor / student
*Extending the spec, writing tests, or understanding the design by example.*

1. This README (5 min)
2. [`13_DESIGN_VALIDATION.md`](13_DESIGN_VALIDATION.md) — real-world scenarios walked end-to-end (8 min; start with SCENARIO 01)
3. [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md) — test structure and pass/fail criteria (8 min)
4. [Contributing](#contributing) below for your first contribution

### Executive / stakeholder
*Deciding whether PersonaOS fits your needs.*

1. [What is PersonaOS?](#what-is-personaos) and [How it works](#how-it-works-technical-summary) above (5 min)
2. [What v1.0 is not](#what-v10-is-not) below for scope boundaries

---

## Contributing

**Easiest first contribution: walk a new validation scenario.**

The design validation catalog ([`13_DESIGN_VALIDATION.md`](13_DESIGN_VALIDATION.md)) has a [backlog of scenario topologies](13_DESIGN_VALIDATION.md#scenario-candidates-worth-walking-next) not yet walked. Pick one, walk it end-to-end against the spec using the [scenario template](13_DESIGN_VALIDATION.md), and submit a PR with your findings. This is how most v1.0 design improvements originate.

**How to write a new acceptance test:**

Each test in [`11_ACCEPTANCE_TESTS.md`](11_ACCEPTANCE_TESTS.md) follows this pattern:

```text
A-XX1     One-sentence description of what is being tested.
          Setup: what state must exist before the test runs.
          Action: what the test does (e.g., "propose a coordination
          shape with composition_depth > 3").
          Expected: what should happen (e.g., "REFUSED with
          'max_composition_depth_exceeded'").
```

Find the test family matching your area (A-K* for kernel, A-P* for persona, etc.), write the test in the same format, and add it to the appropriate section.

**Contribution path:**
1. Fork the repo
2. Read your [role-specific entry path](#start-here-by-role) (~30-45 min)
3. Pick a scenario from the backlog or a gap from the open questions (each doc's §9f or §10)
4. Make your changes on a branch
5. Submit a PR describing what you changed and why

---

## Implementation bootstrap

PersonaOS is a design specification. No reference implementation exists yet. Here is what an implementer would build first:

```text
MINIMAL VIABLE KERNEL (— the first release gate):

  Build these 5 components in order:

  1. IDENTITY STORE
     - SOUL.md parser (markdown + YAML frontmatter)
     - soul.state.json reader/writer
     - Ed25519 signing for identity mutations
     - Test: A-K1 (identity signed), A-J1 (kernel owns identity)

  2. SAFETY FLOOR (sources 1-4 only for MVP)
     - Source 1: universal harm classifier (use an LLM classifier)
     - Source 2: persona charter parser + enforcement
     - Source 3: user boundary store + check
     - Source 4: operator policy loader + check
     - Composition: most-restrictive-wins across all active sources
     - Test: A-S1 through A-S4

  3. LINEAGE
     - Append-only event log (task scope for MVP)
     - Event schema: who, what, when, signed_by
     - Test: A-J2 (lineage append-only), A-K2 (lineage signed)

  4. TASK ROUTING (3 classes for MVP)
     - CONVERGENT → VERIFIER_ACCEPT
     - RELATIONAL → OPEN_ENDED
     - INTERACTIVE → GOAL_PROGRESS_ACCEPT
     - Classifier: LLM call that returns task class + confidence
     - Test: A-T1 (classifier), A-T13 (routing mode A)

  5. ONE FRAMEWORK ADAPTER
     - Pick your framework (Claude Code, LangGraph, or CrewAI)
     - Implement: envelope minting, safety check, lineage recording
     - Test: run a persona through 3 tasks end-to-end

  Total: ~2,000-4,000 lines of Python. Achievable in 2-4 weeks
  by a small team familiar with the spec.

WHAT THIS GETS YOU:
  A persona that remembers across sessions, refuses unsafe actions,
  records an audit trail, and routes tasks correctly — inside your
  framework of choice. Not the full v1.0 vision, but a working kernel
  you can extend incrementally.

WHAT COMES NEXT (v1.0.2-v1.0.6):
  Environments, domain emergence, multi-persona coordination,
  knowledge retrieval, prompt evolution. Each release gate in
```


---

## What v1.0 is not

| | |
|---|---|
| **Not a tutorial** | v1.0 is a design specification, not a getting-started guide. Implementers should pair it with example code. |
| **Not a sales document** | v1.0 describes mechanisms, not benefits. Each section names what is, what isn't, and what is honestly limited. |
| **Not theoretical only** | Every entity has a schema; every mechanism has a code-organisation pointer; every test has a pass/fail criterion. |
| **Not tied to any AI provider** | The kernel signs identity and maintains the audit trail; the AI model is replaceable. Swap Claude for GPT or an open-weight model — the persona's identity, memory, and skills transfer intact. |
| **Not finished** | v1.0 has honest residuals. Future work includes population dynamics, federation hardening, and multi-language domain emergence. |

---

## Research grounding

v1.0 stands on the shoulders of:

- **Generative Agents** (Park et al., Stanford, UIST 2023 — [arXiv 2304.03442](https://arxiv.org/abs/2304.03442)) — observation → reflection → planning → action; reflection mechanism for self-knowledge.
- **Voyager** (Wang et al., 2023 — [arXiv 2305.16291](https://arxiv.org/abs/2305.16291)) — ever-growing skill library, automatic curriculum, lifelong learning; skills generalise.
- **MAP-Elites** (Mouret & Clune, 2015) — diversity preservation across multiple behaviour descriptors.
- **DGM (Darwin–Gödel Machine)** (Lehman et al., 2024) — fertility-weighted parent selection for open-ended evolution.
- **ALPS** (Hornby, 2006) — Age-Layered Population Structure for evolutionary diversity.
- **DSPy GEPA** (2025) — Genetic-Pareto reflective prompt optimization; outperforms MIPROv2 by 10%, GRPO by 20%, 35× fewer rollouts.
- **MIPROv2** — Bayesian instruction + demonstration search.
- **GraphRAG / Hierarchical Graph Memory** (2026) — Graph + vector hybrid retrieval; 35% precision improvement.
- **MCP-Zero** (2026 — [arXiv 2506.01056](https://arxiv.org/abs/2506.01056)) — Active tool discovery for autonomous LLM agents.
- **MCP Gateway & Registry** (2026) — Production dynamic tool discovery with FAISS semantic search.
- **CLS Theory (Complementary Learning Systems)** — Episodic + semantic memory consolidation; biological grounding.
- **Anthropic Persona Vectors + Constitutional Character Training** — Persistent character + safety-aligned behaviour.
- **EvoScientist, ARIA, CraniMem** (2026) — Self-improving agents; test-time learning; bounded memory.
- **SOTOPIA** (Zhou et al., ICLR 2024 — [arXiv 2310.11667](https://arxiv.org/abs/2310.11667)) — Social agent benchmark; goals, secrets, relationships.
- **Mem0, Zep, Letta, Cognee** (2026) — Production multi-scope memory frameworks.
- **A2A Protocol** (Anthropic 2025) — Agent-to-agent federation, signed AgentCards.
- **MCP** (Anthropic 2024) — Tool/resource/prompt protocol.
- **OpenTelemetry** — Industry-standard observability.
- **OWASP LLM Top 10** — Security threat model (LLM01 injection, etc.).

---

v1.0 is implementable.
Personas are persistent characters with seven layers and 14 modes.
Environments are persistent places with presence and responsive behavior.
Projects are multi-session work containers with collaboration mechanics.
Domains emerge from persona work through promotion gates.
Tasks route through 10 classes via 8 acceptance pathways.
Knowledge tags across 7 scopes, retrieves through hybrid pipeline, evolves through DSPy GEPA.
The kernel signs identity, owns lineage, holds the safety floor.
Bodies are interchangeable across MCP / A2A / OTel.
The persona is still a person.

---

