---
title: PersonaOS v1.0 Addendum - Learned Persona Pressure and Completion Readiness
status: Proposed
---

# 19 - Learned Persona Pressure and Completion Readiness

This addendum records a gap found in continuous refinement runs: the substrate can
preserve best-so-far artifacts and runtime observations, but a run may still close
as "done" without an acting persona learning and expressing whether the work
should continue.

The missing force is not a fixed artifact contract. In human work, pressure comes
from a worker's own standards, frustration, pride, peer challenge, obligations,
and memory of prior outcomes. PersonaOS needs the same shape: pressure that
emerges from the persona's characteristics, responses, interactions, task
history, and evolved lessons.

## 1. Problem

The current design has useful but incomplete signals:

- the refinement loop records blocked targets and budget state;
- the artifact layer records bundles, files, validation, and lifecycle state;
- persona drives can receive progress or blockage appraisals;
- candidate traces can feed later tactic and knowledge evolution.

Those pieces do not by themselves answer whether the acting persona believes the
work is complete. Exporting a package means "there is something inspectable";
it does not mean "the persona has exhausted its own learned pressure."

They also do not force a persona to notice when it has quietly narrowed the task
to a smaller completion claim than the user's requested outcome or the persona's
own quality bar would imply. That failure is generic: it can appear in design,
analysis, invention, implementation, research, or any other open-ended task. The
fix cannot be a list of deliverables. The persona must make the scope and quality
comparison itself from the facts it sees.

Hardcoding required artifact patterns, tool names, or a prompt-side pressure
rubric would solve only one observed failure mode while violating substrate
purity. The substrate must not tell a persona what pressure categories to use.
It may only present neutral facts and carry back the persona's own appraisal.

## 2. Design Addition

Add a `persona-pressure-appraisal/1` record emitted by the acting persona before a
candidate turn and, when possible, after materialized output is observed.

The runtime provides neutral round facts only:

- task text and task ids;
- prior action observations, including prior pressure appraisals;
- observed package shape and bounded package-content samples;
- current generic action surface;
- capability acquisition state;
- body-authored domain context, when present;
- budget headroom;
- live drive state and relevant need context.

The runtime may request a parseable envelope through an adapter-native structured
response schema. That schema is transport metadata, not prompt content. It names
only the top-level `persona-pressure-appraisal/1` fields required to parse the
persona's appraisal. It does not include a fixed pressure rubric, required
pressure dimensions, required deliverable names, or domain-specific tool advice
in the pressure prompt. The prompt is data: `task` and `round_facts`.

The persona may return bounded structured data:

- `ready_to_complete`: whether the persona judges completion acceptable now;
- `open_pressure`: unresolved items according to the persona;
- `closed_pressure_refs`: persona-authored evidence that previously open
  pressure items are now closed;
- `purpose_alignment`: the persona's own comparison between requested outcome,
  current completion claim, its quality bar, and evidence;
- `improvement_frontier`: the persona's distinction between the minimum floor it
  may have satisfied and the highest-value next improvement it can still see
  under budget and action capacity;
- `learned_pressure`: optional persona-authored pressure state in the persona's
  own vocabulary;
- `next_action_pressure`: optional generic action pressure, such as needing tool
  activity, materialized output, capability acquisition, or coordination;
- `pressure_sources`, `completion_block_reason`, `intended_next_action_bias`,
  and `drive_tags` when the persona finds them useful.

Only the envelope field names are substrate-defined. Provider transports may use
closed generic containers for schema compatibility, but the vocabulary and
lessons inside those containers are persona-authored and can change as the
persona learns.

`purpose_alignment` is a generic closure-basis check, not a domain checklist. It
exists because otherwise the runtime cannot distinguish a persona that truly
believes the requested outcome is satisfied from one that has completed a smaller
version of the task. The persona authors the requested-outcome reading, current
claim, quality bar, fit judgement, remaining tension, and evidence references in
its own terms. It also authors any self-limiting assumptions, the user/task facts
that authorize those limits, and any residual closure risk it notices. This lets
pressure emerge from the persona's own interpretation of ambiguity instead of
from runtime-authored deliverable rules.

`improvement_frontier` addresses a separate failure: a persona can satisfy a
minimum floor and still have a clearly valuable next pass available. Human work
often continues because pride, competence, peer expectation, or remaining budget
make the next pass worth doing. The persona authors that frontier itself: whether
the minimum floor is satisfied, whether the frontier is satisfied, what next
improvements remain, what action would pursue them, and why stopping now is
acceptable or not. The substrate does not convert those strings into a checklist;
the persona must still express a decision to continue the bounded run through
`ready_to_complete = false`. `open_pressure` records residual tension and may
coexist with either readiness decision.

## 3. Completion Semantics

`ready_to_complete = false` MUST NOT block artifact publication. A best-so-far
bundle can still be exported and made visible.

`ready_to_complete = false` SHOULD block the run from being marked complete and
SHOULD block the bundle from advancing to accepted for that bounded run. A
non-empty `open_pressure` list MUST NOT mechanically override the same signed
appraisal's `ready_to_complete = true`. Pressure is persona-authored context, not
a second host-owned readiness bit.

Each persona's latest signed appraisal is its current pressure snapshot. A later
snapshot supersedes the earlier snapshot for current-state decisions: pressure
items omitted from the latest snapshot are retired from current pressure. Every
prior appraisal remains immutable in lineage and available as learning history;
supersession never deletes or rewrites it. `closed_pressure_refs` are useful
persona-authored explanations and evidence links, but the substrate MUST NOT
require structural count-matching before accepting the persona's newer signed
state.

`learned_pressure` and arbitrary nested persona memory are not runtime gates by
themselves. They are replayed as evidence for the persona to interpret on later
turns. If that learned state should keep the run open, the persona must express
that explicitly through `ready_to_complete = false`; the substrate does not
parse key names or text values to infer hidden pressure.

The same rule applies to `purpose_alignment`. A non-empty tension, mismatch, or
ambition note inside that object is memory/evidence unless the persona also
expresses unresolved readiness through `ready_to_complete = false`. The
substrate does not parse that object to infer hidden artifact requirements or
scope gates.

The same rule applies to `improvement_frontier`. A listed possible improvement
is not itself a runtime gate. It is replayed to the persona and peers as
experience. If the persona judges the frontier unfinished and worth pursuing, it
must say so through `ready_to_complete = false`.

Another persona's pressure is signed peer evidence for the acting persona to
consider, not a host-enforced veto. The acting persona may seek a peer response,
revise its snapshot, or sign readiness while preserving the disagreement and
follow-up work in lineage.

`ready_to_complete` is readiness for the current bounded run. It does
not grant an external authority, certify an unavailable measurement, or advance
a real physical asset. Safety, consent, operator-cosign, credential, payment, and
physical-state gates remain independently enforced at the exact scoped action or
claim. A persona may therefore sign a useful design run ready while retaining
open pressure such as a future field measurement or permit review; the release
claim stays honestly limited without turning that external dependency into a
task-wide wait.

This preserves two truths at once:

- the user can inspect the best work currently produced;
- the persona's bounded-run readiness, residual pressure, and any external
  release authority remain separately visible.

## 4. Self-Improvement Path

Pressure appraisals are not one-off gates. They are action observations and must
enter the same learning path as other candidate outcomes:

- pressure appraisal facts are recorded on the round trajectory;
- pressure appraisal observations are carried into candidate action traces;
- `record_body_outcome` stores those traces for persona evolution;
- tactic and knowledge evolution can distill patterns from pressure, failures,
  peer reactions, and task outcomes;
- future `preview_persona_system` calls render the evolved lessons, tactics, and
  knowledge back into the persona's system context.

Appraisal turns and candidate turns may also receive a compact
`persona-learning-history/1` fact assembled from recent evolution traces. That
history may include the persona's prior pressure appraisals, prior tool or output
observations, prior failures, and bounded peer traces from the same environment.
It is still data, not instruction: the substrate does not explain what those
traces mean, does not score them, and does not convert them into a fixed pressure
rubric. The persona's own identity, drives, memory, evolved tactics, and live
model interpretation decide how those traces change future pressure.

The effect is self-improving pressure: a persona can learn when it tends to stop
too early, which peer objections matter, what task evidence it repeatedly misses,
and which actions actually reduce its own pressure. The substrate does not author
those lessons. It stores and replays the persona's experienced traces.

## 5. Why This Is Not an Artifact Contract

The pressure appraisal is not a list of required file patterns, tools, roles, or
domain artifacts. It is a persona-authored interpretation over facts. If a domain
needs particular deliverables, toolchains, calculations, or review roles, those
must emerge through the persona's domain context, tool discovery, peer
observation, and candidate work.

The substrate may interpret only generic readiness and action-control signals. It
must not inspect persona-authored strings for domain words, file extensions, tool
names, or required artifacts.

The same rule applies to package-content observations. Text excerpts can create
pressure only because the persona reads and appraises them. The substrate must
not scan them for magic strings.

## 6. Relationship to Drives and Peers

The runtime may carry the persona's own `drive_tags` with its pressure and
progress observations. It MUST NOT mint blockage or frustration merely because
`open_pressure` is non-empty; signed readiness and experienced outcomes remain
distinct inputs to the existing drive mechanism.

External pressure is represented as data from the environment: peer
observations, role obligations, project state, user amendments, and coordination
records. The runtime does not write "try harder" instructions. The persona
decides what pressure those facts create.

## 7. Tool Emergence

The appraisal sees the generic action surface and capability-acquisition state.
It may therefore notice that a needed capability has not been attempted,
provisioned, or invoked, but it must not receive a domain-specific tool
prescription from the substrate. Tool setup remains persona-authored through the
existing environment and tool mechanisms.

When persona-authored open pressure identifies available action, the persona may
choose a generic action/tool turn or materialized output. The runtime exposes the
action surface but neither requires continuation from pressure alone nor chooses
a domain tool from the pressure text.

## 8. Adapter Tool Transport

Tool emergence depends on the body adapter using the tool mechanism that its
backend actually supports. A generic `tools` argument is not enough as a design
contract.

Adapters must declare their tool transport shape:

- provider SDK adapters pass tools through the provider-native function/tool API;
- CLI adapters that lack provider-native function calls use a structured-output
  schema that includes tool names, descriptions, argument schemas, and any
  required artifact-package channel;
- CLI adapters that support native MCP or agent configuration must expose those
  configuration surfaces at the adapter boundary rather than hiding them behind a
  generic prompt convention.

Codex CLI configured MCP servers must not be hidden by default when the operator
expects Codex to select them. Claude Code adapter configuration must be able to
carry `mcp_config`, agent definitions, selected agent, and allowed tools because
those are Claude Code's native selection surfaces.

The same adapter boundary carries non-tool structured response schemas. For
pressure appraisal, Codex CLI uses `--output-schema`, Claude Code uses
`--json-schema`, and direct provider APIs use their native structured-response
surface when available. The schema is generic appraisal transport; it is not a
task-specific artifact contract.

PersonaOS environment MCP tools are currently an in-process kernel surface. Until
there is a live stdio or HTTP bridge for that kernel surface, CLI-native MCP can
only expose external configured servers. PersonaOS env tools therefore continue
through the provider-neutral structured tool loop, and that loop must keep
setup/provisioning tools selectable under persona-authored pressure and refresh
the tool surface immediately after a tool is mounted.

This is adapter-specific behavior, not domain behavior. The substrate still does
not name task-specific artifacts.

## 9. Reference Notes

The referenced body/tool-runner design shows a useful adapter-level pattern:
expose available tools, collect context, preserve task state, and return tool
receipts to later model turns. PersonaOS adopts that pattern only at the generic
action-surface level.

PersonaOS does not adopt fixed slash-command workflows, provider-specific plan
modes, body-owned task state, or hardcoded tool inventories from any one runner.
Those concepts are adapter affordances; making them substrate rules would reduce
emergent behavior and violate the body/soul split.

## 10. Required Tests

Conformance tests should verify:

- the pressure-appraisal prompt is JSON facts only;
- pressure structured-output schema is carried out-of-band by the adapter;
- pressure records are signed and stored on rounds;
- candidate prompts receive pressure appraisals as data;
- the latest signed appraisal is the current pressure snapshot while every prior
  appraisal remains in immutable lineage;
- a signed ready appraisal is not mechanically vetoed by non-empty current or
  historical pressure;
- persona-authored purpose/scope alignment is preserved and replayed without
  becoming a runtime-parsed gate;
- persona-authored floor/frontier appraisal is preserved and replayed without
  becoming a runtime-parsed gate;
- persona-authored learned pressure is preserved as memory, but only explicit
  `ready_to_complete = false` keeps the bounded run open;
- persona-authored next-action pressure can inform a persona-chosen generic tool
  or materialized-output action without becoming a host action gate;
- pressure appraisal observations enter the persona evolution trace path;
- post-package pressure can use bounded package-content observations to revise
  the latest current snapshot;
- bounded-run readiness remains distinct from external release and physical-state
  authority;
- artifact export still occurs when pressure remains open;
- adapter tool transport is explicit and provider-specific;
- CLI structured-output schemas include the generic tool catalog without adding
  domain pressure;
- CLI-native MCP or agent configuration is passed through adapter-native flags
  when supplied;
- setup/provisioning tools remain selectable under persona-authored pressure;
- newly mounted env tools are visible to the next body turn;
- no domain names, artifact patterns, or required file extensions are introduced
  by the substrate.
