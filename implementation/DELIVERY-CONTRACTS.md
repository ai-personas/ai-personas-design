# Deliverable contracts and production requirements

[Implementation guide](README.md) · [Core contracts](CONTRACTS.md) · [Requirement index](REQUIREMENTS.md) · [Design rationale](../design/DELIVERABLE-PRODUCTION.md) · [Acceptance fixtures](../evaluation/DELIVERY-ACCEPTANCE.md)

These normative contracts supplement the core contracts for accepted deliverable-producing work. They specify meanings and failure behavior, not a wire schema, application interface, required provider, or fixed domain workflow. Records may be combined for small work. All applicable authority, privacy, resource, recovery, and evidence rules remain in force.

## Required information

| Record | Minimum recoverable meaning |
|---|---|
| Deliverable contract | Original mandate and revision; result level; required and optional outputs; intended consumer; format and native editability; units and conventions; dependencies; acceptance criteria and tolerances where applicable; exclusions; unknowns; accepted owners or gaps; delivery destination; authority for changes. |
| Method brief | Author and sources; version; relevant domain concepts; assumptions and applicability; candidate methods and alternatives; artifact relationships; hazard and limitation notes; proposed checks. It is not authority or a trusted verdict. |
| Production binding | Deliverable and required operation; selected capability and exact version; environment; supported input and output formats; native libraries or models; rights and acquisition conditions; preparation and representative operation evidence; observation limits; estimated and reserved resources; fallback or block. |
| Dependency plan | Work-scoped operations and commitments; exact consumed and produced versions; provisional versus accepted inputs; units and interface mappings; permitted independence; integration checks; iteration budget; stopping condition; current findings. |
| Check specification | Criterion and claim; method or reviewer; exact checker version and configuration; inputs; thresholds or human rubric; preconditions; expected coverage; independence and conflict policy; raw evidence required; limitations; accepted check owner. |
| Check result | Actual run or review identity; input and output versions; diagnostics and observations; measured values and units where relevant; verdict; limitations; findings; historical result and separately derived current applicability. |
| Delivery manifest | Exact mandate and contract revisions; source and derived artifact identities; sizes and fingerprints where files exist; formats, units, and retrieval locations; necessary libraries and models; actual producing actions; checks and dispositions; reproduction and editability evidence; current acceptance; missing scope; authority; external obligations. |

A path, filename extension, checksum, or producer's assertion is not proof of semantic content. A dependency link is not proof of a faithful transformation. Personal or proprietary material retains its access and redistribution restrictions in every derivative and package.

## Intake and production feasibility

**Inputs:** original need, requested result level, supplied facts, material unknowns, available authority, resources, and candidate capabilities.

**Accepted result:** an adopted deliverable contract at appropriate depth and a capability coverage assessment. Every required operation and check has a demonstrated binding, a bounded preparation commitment, or a visible gap. An uncertain estimate remains uncertain; accepting discovery is not promising full production.

**Failure behavior:** absent specifications block affected claims, not all useful conversation. Missing tools, source data, libraries, models, access, or reviewers produce a scoped block, approved alternative, or explicit partial delivery. A downgrade from native design to a written suggestion requires an authorized scope change. Discovery and preparation cannot consume protected closeout capacity without authorized reallocation.

**Evidence:** material questions and assumptions; accepted output list; actual capability probe receipts; preparation failures; supported and unproven operations; accepted owners; continuing gap dispositions.

## Production and semantic validation

**Inputs:** adopted contract, current source versions, method brief, accepted commitments, production bindings, and current grants.

**Accepted result:** actual artifacts with typed input/output relationships and observations. For native deliverables, evidence covers meaningful content, reopening, a representative persistent edit on a copy, and regeneration of affected outputs. Source-to-analysis and source-to-export transformations preserve their mapping and limitations.

**Failure behavior:** empty or mislabeled files, unresolved references, stale outputs, unsupported formats, lost units, missing dependencies, or unavailable inspection cannot fulfill the corresponding obligation. A tool that exports cannot be assumed to author or route. A simulation with incomplete models may support a narrower model-based claim, never an unsupported full-system pass.

**Evidence:** operation receipts, exact native sources and exports, dependency identities, parse and semantic checks, actual renders when inspected, warnings, and reproduction observations. Necessary licensed dependencies may be resolved through an authorized reproducible acquisition path; a broken or inaccessible dependency blocks the promised portability claim.

## Checking and bounded repair

**Inputs:** frozen criterion-to-check matrix, exact candidate assembly, accepted reviewers or validators, independence policy, resources, and relevant observations.

**Accepted result:** each applicable criterion records pass, fail, not run, unavailable, or inconclusive; applicability independently records current, stale, pending, or unverifiable. No weighted average or majority vote overrides an unmet mandatory criterion. Subjective work may use an authorized human rubric without invented numerical certainty.

**Failure behavior:** missing checks, a clean file parser, successful process exit, nominal-only simulation, or another persona's approval cannot stand in for the agreed check. Criteria may change only through authorized versioned scope decisions, not producer convenience. Reviewers retain unresolved findings and may identify omissions from the original mandate.

**Evidence:** exact checker and input versions, observations, threshold comparisons or human assessment, warnings and exclusions, repair decisions, actual changed artifacts, and current rechecks. The checker must not trust a producer-written success flag. Material changes invalidate affected descendants and evidence; uncertainty requires conservative coverage.

Repair stops, seeks a permitted alternative, or reports a scoped block when its bounds are reached. It does not fabricate convergence, refresh budgets by creating personas, or promote a best-effort draft into a validated release.

## Package and release

**Inputs:** exact delivery manifest, adopted contract, coherent assembly, current qualifying checks, blocker dispositions, authority, and acceptance where required.

**Accepted result:** the intended authorized recipient can retrieve the actual promised package. All mandatory outcomes at the adopted level have current evidence. The release binds one exact state, not paths that may later change. Reproduction may use a declared semantic or numerical equivalence rule when byte-identical regeneration is inappropriate; raw original outputs remain intact and normalization cannot conceal meaningful differences.

**Failure behavior:** missing artifacts, required libraries, models, drill files, approvals, or failed mandatory checks prevent a full release. An explicitly labeled partial package preserves missing scope and owners. Relevant changes racing release follow I21 and M24. Releasing files does not grant permission for external effects or assert physical, commercial, or regulatory success.

**Evidence:** recipient retrieval, manifest integrity, native round-trip checks, independent reproduction appropriate to the claim, current reviews, exact acceptance, and any separately authorized external receipt or measurement. Public claims must name the task family, scope, configuration, conditions, and untested boundaries actually demonstrated.

## Additional requirement catalogue

These ten identifiers supplement the 45 original requirements without renaming them. All D fixtures below are specified, not executed by this handbook.

| ID | Required behavior | Primary delivery fixtures |
|---|---|---|
| DLV-01 | Adopt concrete deliverables and result levels; preserve unknowns and authorized scope changes. | D01; D02 |
| DLV-02 | Bind required production and checking operations to actual capabilities; expose preparation and coverage gaps. | D03; D14 |
| DLV-03 | Keep domain method briefs versioned, evidence-linked, work-scoped, and separate from authority and protected evaluation. | D04; D14 |
| DLV-04 | Produce meaningful native artifacts and demonstrate promised reopening, editing, and regeneration. | D05; D08 |
| DLV-05 | Preserve and check semantic mappings and package consistency across exact source, analysis, and export versions. | D06; D07; D09 |
| DLV-06 | Use claim-specific checks, explicit negative or missing states, and risk-appropriate independent review. | D07; D10; D11 |
| DLV-07 | Bound evidence-led repair and revalidate changed dependencies without erasing failures. | D09; D15 |
| DLV-08 | Deliver a retrievable, coherent manifest and reproduce required outputs under declared equivalence rules. | D08; D10 |
| DLV-09 | Separate digital delivery, external effects, and observed outcomes; preserve their distinct authority and evidence. | D12; D13; D16 |
| DLV-10 | Demonstrate scoped cross-domain capability, including unfamiliar-task behavior and proportional simple work. | D11; D12; D13; D14 |

The design rationale is in [deliverable production](../design/DELIVERABLE-PRODUCTION.md). The [inverter and business walkthroughs](../examples/5W-INVERTER-AND-CROSS-DOMAIN.md) illustrate adoption of these contracts; they are not a core task router or proof of runtime success.
