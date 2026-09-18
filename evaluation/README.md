# Evaluation: show what works, not only what exists

[Home](../README.md) · [Acceptance scenarios](ACCEPTANCE.md) · [Requirements](../implementation/REQUIREMENTS.md)

A readable design, a working mechanism, a useful persona, and a safe deployment are different achievements. This repository specifies an evaluation plan; it does not report a completed product evaluation.

## Match the claim to the evidence

| Claim | Evidence needed | Insufficient substitute |
|---|---|---|
| Operational reliability | Tests of authority, resource accounting, isolation, version integrity, delivery, and recovery under declared failures. | A plausible diagram or a successful demonstration with no disturbances. |
| Individuality | Controlled differences in consequential choices attributable to relevant persistent state. | Different names, portraits, writing styles, or random variation. |
| Cooperation | A participant's evidence changes another's actual work, followed by appropriate checking. | Several personas saying that they agree. |
| Adaptation | Changed inputs or new findings alter commitments, methods, or outputs without losing the accepted goal. | An updated plan followed by the same stale action. |
| Learning benefit | Later matched comparisons with relevant memory retained and withheld. | Memory writes, retrieval counts, or stronger tools in the later attempt. |
| Accomplishment | Exact agreed deliverables, current relevant checks, scope coverage, and explicit limitations. | Successful execution, attractive previews, or all self-selected tasks marked closed. |
| Deployment suitability | Evidence for the particular users, domain, operating environment, and effect boundaries. | Passing a general software test or accepting a conditional digital artifact. |

## Before an evaluation

Freeze the task information, original request, accepted criteria, evaluator version, initial persona state, permitted tools, inference configurations, access boundaries, and total resource allowance. Declare repeat counts, quality criteria, failure definitions, cost and robustness thresholds, and conditions for stopping before examining the results.

A test fixture is a controlled example with known inputs and a declared assessment method. Start external-effect tests with synthetic identities, accounts, destinations, and data rather than uncontrolled real-world consequences. A house fixture supplies explicitly synthetic site inputs unless appropriately sourced real data is intentionally within scope.

Independent evaluators must not leak successful solutions or protected assessment material into the learner's context. Reviewers may use declared domain tools; the persona must not be given the hidden expected answer merely to appear competent.

## Comparisons that matter

Compare a single continuing persona, a fixed group, and an adaptive group under comparable **total** resources, not an equal allowance per persona. Test simple work that should finish without recruitment as well as substantial work where cooperation may help.

Separately vary retained memory, character context, relationship history, and inference configuration. Keep task information, tools, and evaluation opportunities appropriately comparable. Counterbalance ordering and presentation effects where practicable, preserve unsuccessful attempts, and use blinded quality assessment where possible.

Do not prescribe professions, tool brands, exact dialogue, or birth counts in order to manufacture the behavior being evaluated. Identical choices may be appropriate when the evidence is decisive. Differences are not inherently better.

## How to run the catalogue

The [acceptance catalogue](ACCEPTANCE.md) contains 26 mechanical checks, 12 behavioral checks, and six proposed extension checks. Each entry identifies a situation, a disturbance or comparison, and an observable result. Turn applicable entries into tests in the implementation repository; no programming language or test runner is required by this handbook.

Mechanical checks can use deterministic controlled fixtures. Behavioral checks require actual observed persona work and a declared assessment method. Extension checks apply when the feature is enabled. A disabled feature is reported as not applicable with a reason, not as passed.

A narrow conformance claim names the supported profile, exact configuration, applicable requirements, evidence, and exclusions. No universal numerical success threshold is implied here. Deployments choose and justify thresholds in their [decision register](../implementation/DEPLOYMENT-DECISIONS.md).

## Reporting a result

| Report field | What to record |
|---|---|
| Claim | The exact capability or guarantee being assessed, with requirement and test identifiers. |
| Configuration | Design revision, implementation revision, models, tools, environment, grants, and initial persona state. |
| Fixture | Task, allowed information, criteria, evaluator version, disturbances, and predeclared thresholds. |
| Observations | Actual actions, receipts, exact artifacts, reviews, feedback dispositions, and recovery events. |
| Resources | Total used, remaining reservations, uncertain exposure, and relevant comparisons. |
| Outcome | Passed, failed, inconclusive, not run, or not applicable, with the reason and evidence. |
| Limitations | Untested threats, unavailable evidence, scope exclusions, outside assurance, and possible confounding factors. |
| History | Earlier failures and any later changes to methods, criteria, or evaluator behavior. |

Changing an evaluator is not the same as improving the system. Preserve prior results under their original criteria. A one-off success supports a claim about that attempt, not universal expertise.

## Evidence boundary for this edition

The historical stress report described authored scenarios and sixteen small abstract protocol checks. It did not establish live persona behavior, a native house-design result, or production safety. This edition does not rerun or upgrade those historical checks. Documentation link and inventory checks are separate from every product acceptance check below.
