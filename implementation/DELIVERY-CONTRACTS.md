# Delivery addendum compatibility and requirement mapping

[Implementation guide](README.md) · [Active requirements](REQUIREMENTS.md) · [Core contracts](CONTRACTS.md) · [Review finding](../design/DELIVERABLE-PRODUCTION.md)

## Status and authority

**Superseded as a separate normative contract, 18 September 2026.** The earlier delivery addendum duplicated or specialized obligations already present in the handbook. Its DLV-01–DLV-10 identifiers are retained below for historical traceability, not as ten additional active requirements. Do not reuse these identifiers for unrelated rules or silently relabel an old evaluation as passing the current design.

The authoritative design remains the 21 invariants, 45 requirement identifiers, detailed chapters, and [core contracts](CONTRACTS.md). The clarified [persona-owned organization boundary](../design/03-work-and-cooperation.md#how-organization-emerges) belongs to those existing rules. Historical wording remains available in Git history; the [changelog](../CHANGELOG.md) records the correction.

## Retired identifier mapping

| Historical identifier | Earlier concern | Existing requirements and interpretation |
|---|---|---|
| DLV-01 | Concrete deliverables, result levels, unknowns, scope changes | NED-01–NED-04: retain the original need and adopted scope, criteria, assumptions, and coverage. |
| DLV-02 | Production capability and missing operations | ACT-01–ACT-03; I10: require relevant operation evidence or expose the gap. Tool availability is not successful production. |
| DLV-03 | Method briefs and protected evaluation | MEM-01–MEM-04, ACT-02, GOV-01; I03: methods are ordinary sourced work content or permitted memory, never authority or a hidden domain router. |
| DLV-04 | Meaningful editable artifacts | EVD-01–EVD-02, NED-04: support promised native content and editability with appropriate checks; B11 already includes native edit and reproduction evidence. |
| DLV-05 | Mappings and cross-artifact consistency | COL-05, EVD-01, EVD-03–EVD-04: check the particular work's interfaces, transformations, and exact assembly. |
| DLV-06 | Claim-specific checks and negative states | EVD-02–EVD-05: preserve appropriate review, missing evidence, findings, current applicability, and limits; do not average away a mandatory failure. |
| DLV-07 | Bounded repair and dependency revalidation | COL-04–COL-05, GOV-02–GOV-04, EVD-03: retain failures, bound iteration, protect finishing, and invalidate affected claims. |
| DLV-08 | Retrievable delivery and reproduction | EVD-01–EVD-05, NED-01, NED-04: supply the actual promised sources, dependencies, delivery, and reproduction evidence at the adopted scope. |
| DLV-09 | Digital artifacts versus external effects and outcomes | ACT-03–ACT-04, GOV-01, EVD-05, PHY-01 where enabled: delivery does not establish permission, execution, measurement, or certification of another effect. |
| DLV-10 | Cross-domain ability and proportional simple work | I03, PER-02, COL-06, EVD-05; B08 and B11–B12: demonstrate the claimed scopes without forcing a roster, birth, or workflow. |

The corresponding meanings remain required when applicable; the redundant layer does not. A migration must check its actual design revision and evidence, not infer that similarly named records guarantee conformance.

## No mandatory new record family

A deliverable specification is part of the mandate and relevant commitments. A method brief is ordinary work content or a sourced fragment. A production binding is a relation between the required operation, its capability, and actual evidence. A dependency plan uses work, interface agreements, and accepted commitments. Check specifications and results use criteria and assessments. A delivery manifest is an inventory within the submission and release when a package needs one.

An implementation may use those names for convenience. It must not require seven extra objects, a universal file bundle, or a fixed sequence for a simple response. Conversely, simplifying record structure does not permit missing promised artifacts, unsupported claims, lost dependencies, or absent recipient access. Reproduction checks should state suitable semantic or numerical equivalence when identical bytes are not the relevant criterion.

## Evaluation compatibility

[D01–D16](../evaluation/DELIVERY-ACCEPTANCE.md) remain separately identified supplemental scenarios, now mapped directly to the original requirements and expressed without a compulsory task pipeline. Their revision and selected concrete inputs must be recorded with any result. Historical scenario results, if any are later supplied, keep their original revision; no results are asserted here. Core M01–M26, B01–B12, and X01–X06 identifiers remain unchanged.
