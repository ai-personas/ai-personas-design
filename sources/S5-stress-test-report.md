# AI Personas: Rust-only behavioral stress test and design corrections

**Review date:** 16 September 2026  
**Input:** `AI-PERSONAS-RUST-FINAL-SPEC.md`, version 1.1.  
**Output:** complete integrated specification `AI-PERSONAS-RUST-SPEC-v1.2.md`.  
**Sole runtime baseline:** `rewrite/design-first` at `d3339d30fa883c21c7935a2d009e3a58f480a256`.

## Finding

The proposed architecture is compatible with emergent individuality, group organization and real multidisciplinary work, but version 1.1 is not yet a sufficient progress-and-completion contract. An agreeable story in which every persona makes a good choice would hide its gaps. This review deliberately includes plausible bad choices, missing information and awkward event orderings.

The principal counterexamples are unowned required work; provisional assumptions becoming unconditional claims; newborns lacking access to decide whether to join; tools launched but not completed before subsequent actions; consequential feedback acknowledged but not acted on; circular final-version prerequisites; production consuming review resources; narrative activity extending a run without useful change; and final acceptance racing a model update.

These are not all newly discovered omissions. Version 1.1 already requires authority, budgets, individual agendas, consent, input-bound evidence, currentness, context limits and isolation. The revisions make several incomplete transitions explicit. A distinct static defect is present in the inspected baseline asynchronous action path. Conversely, the existing transactional newer-input check in `wait` is a sound mechanism to preserve, not a missing feature to rebuild.

**Evidence limitation:** all persona statements and decisions below are authored scenarios, not outputs from live personas. Sixteen small abstract protocol checks were executed in JavaScript; no Rust binary or model was executed. They check explicit guards and a few event orderings, not human-like behavior, spontaneous specialization, convergence, system-wide safety, or engineering quality. No CAD files, simulations or house deliverables were generated in this review.

## 1. Desired state and the test boundary

There are four different success claims. Keep them separate.

| Claim | Desired evidence | What this review establishes |
|---|---|---|
| Individuality | Distinct context changes consequential choices beyond names/style | The revised protocol preserves individual choices; live causal effect remains untested |
| Cooperation and adaptation | Peer evidence changes work, priorities, agreements or useful team membership | The scenario identifies required transitions and failure handling; no team behavior was measured |
| Accomplishment | Agreed native engineering deliverables, appropriate analyses and current assessment | Concrete output/validation contracts; no actual house-design result |
| Operational reliability | Bounded, authorized, restart-safe execution without false currentness | Targeted source findings and small abstract guard checks; production verification remains required |

For the house example, success means the **agreed coordinated digital-design package**, not just four rooms or an attractive rendering. It includes editable architectural/structural/plumbing/HVAC/electrical work, actual calculations or simulations appropriate to its questions, coordination and reproducibility. CAM concerns only explicitly included components with sufficient manufacturing inputs. Site verification, professional approval and physical operation remain separate where not observed.

This is not a universal house checklist embedded in the kernel. It is the acceptance fixture corresponding to this conversation's clarified scope. In an actual bare “design 4 bedroom house” request, personas must first discover and negotiate the required depth.

## 2. Scenario setup without hidden expertise

Use an explicit, empty Rust node and two founder personas. For this illustrative trace, call them **Mira** and **Nox**. The names do not define responsibilities.

Assume that earlier ordinary work left Mira with a tendency to compare spatial/user-experience alternatives, and Nox with an interest in exact comparisons after encountering inconsistent revisions. These are hypothetical retained states, not fabricated qualifications. Do not give either a profession or force their choices. A separate cold-start test must begin with genuinely unauthored founders and cannot borrow this history.

The principal supplies the clarified goal, a finite authorized root allowance, permissible local tools/research, and a bounded replication grant. Real external writing, spending outside that allowance, construction and machinery operation are not silently authorized. Missing site, climate, budget and other necessary inputs are either requested or supplied as an explicit **synthetic test fixture**. No values are inferred from the user's location.

The conceptual root allowance distinguishes production/exploration from protected closeout resources. No numeric call count in this report estimates the cost of designing a house. A later independently assessed run must freeze actual resources, model settings, input files and evaluator criteria before starting.

## 3. Observable trace: a group tackles the house

### Step 0 — Someone must actually accept the need

**Possible behavior.** Mira proposes exploring arrangements; Nox first inspects the brief. Either might decline or ask for information. Selecting their IDs in the UI does not mean that they accepted responsibility for ongoing work.

**Version 1.1 support.** Identity bootstrap, individual agendas and commitment consent are specified. However, the work can appear active before anyone is answerable for the unassigned parts or for incoming work-level questions. [S1 §§3.3, 6, 9]

**Failure branch.** Both authors produce interesting proposals, then yield. Every proposed responsibility has been politely offered, but none is accepted. The user sees a busy history and no delivery.

**Correction C01.** Record the initial offer; show `awaiting_acceptance` until one or more personas accept continuation responsibility. This means tracking the need to an honest result, handoff or block—not becoming the leader or dictating other personas' priorities. Multiple participants can share or partition it. If everyone declines, report that state instead of substituting a roster.

**Inspectable outcome.** Original request, root allowance, addressed founders, exact accepted continuation commitment(s), or explicit absence of acceptance.

### Step 1 — Discover the scope without pretending the unknown inputs are facts

**Possible behavior.** Mira asks about how the occupants will use private/shared space. Nox asks which site and delivery level the design should serve. They identify that a concept sketch and a coordinated digital design require different evidence.

**Failure branch.** To maintain momentum they assume a site condition, then a later summary says it is confirmed. A calculation passes for the assumption and is treated as a real-site result.

**Correction C02.** Material assumptions are versioned records linked to affected claims. `authorized_for_exploration` is not `confirmed_by_evidence`. The team can proceed conditionally while keeping the unresolved external requirement visible. Require scope coverage review against the original request/clarifications, not only completion of the team's selected checklist.

**Inspectable outcome.** Mandate v1, provisional or adopted criteria, assumption records, bounded requests, and clear distinction between conditional and unconditional claims.

### Step 2 — Individual perspectives produce different first contributions

**Possible behavior.** Mira proposes two genuinely different arrangements. Nox proposes a common comparison basis and a small feasibility check. They negotiate a working agreement to compare alternatives using the same inputs.

**What already works.** Version 1.1 correctly provides individual agendas, an unranked shared board and accepted commitments. No universal priority score or average group personality is needed. [S1 §§4, 6]

**Failure branch.** A shared summary overwrites both agendas with “the team decided.” Or every persona receives an identical transcript and follows the first confident proposal. Distinct names would not establish individual effects.

**Retain and clarify.** Carry each person's relevant identity, experience and relational interpretation alongside shared facts; retain exact endorsements and dissent. Bound alternative exploration to the accepted allowance. Do not force disagreement for its own sake.

**Inspectable outcome.** Two attributed proposals, the endorsed agreement version and actual accepted tasks. Whether those differences arose from character rather than randomness still requires ablation tests.

### Step 3 — The unattractive work is still required

**Possible behavior.** Both founders volunteer for visual alternatives. Neither takes system connectivity, documentation or integration. This is a plausible group outcome—not a violation that should be “fixed” by secretly assigning Nox as engineer.

**Failure branch.** The work board shows many closed architectural items while plumbing and electrical are absent or unowned. A percentage based only on listed items appears complete.

**Correction C01.** Show unowned adopted outcomes and incomplete scope coverage next to the agendas. Notify the accepted continuation owners. They can volunteer, renegotiate, consult a peer, acquire a capability, propose birth or ask the principal to change scope. The runtime reports coverage facts; it does not pick a profession or solution.

**Inspectable outcome.** Ownership is accepted explicitly or the uncovered scope remains a completion blocker. “All recorded items closed” is never equated with “all original requirements discovered.”

### Step 4 — A tool is acquired and actually used

**Possible behavior.** Mira selects an authorized CAD/BIM tool, checks that it starts and performs a representative editable operation. Nox reproduces an export or checks basic consistency. They preserve a failed installation rather than calling the tool acquired merely because a recipe was written.

**Static Rust defect.** In the inspected baseline, `jobs::start` returns after spawning. `operate` marks `exec` running. `apply_decision` only stops for a failed receipt. Foreground waiting happens on a later `work_loop` entry. Therefore the same response can launch a slow model-writing command and immediately inspect or publish an old file at its output path. [S2, S3]

**Correction C04.** A pending asynchronous operation is a completion barrier. Retain but suppress the remaining unadmitted actions from that decision. After actual output/terminal receipt arrives, a fresh decision chooses how to proceed. An immediate failure still stops the suffix. A background job permits other independent work in a subsequent funded decision, not assumed dependency-free continuation of the old batch.

**Inspectable outcome.** Launch, pending state, terminal receipt, actual source version, and a later observation-bound publication. No “simulation finished” claim on a running job.

### Step 5 — Birth is proposed for a concrete contribution

**Possible behavior.** Nox finds that comparing the alternatives requires sustained analysis attention that the founders cannot provide without dropping other accepted work. Nox proposes a peer; Mira may agree, prefer a tool, or suggest an existing participant.

**Correct existing principle.** Birth is optional. Different groups can choose differently. A new identity supplies neither expertise nor fresh funding. [S1 §8]

**Failure branch.** A newborn needs work membership to read anything useful, but cannot decide to join without reading the invitation. Or it is given the parent's entire workspace/token to bypass this problem.

**Correction C03.** Distinguish work, per-persona participation runs and the shared funded execution root. Persist a limited `BootstrapContext` and `BootstrapGrant` with birth identity, exact shared seed/preview references, initialization funding and one wake. The newborn can inspect the invitation and accept or decline without general work access or execution authority.

**Inspectable outcome.** One birth/provenance record, conserved allowance, restricted initialization, separate membership consent and separate commitment acceptance.

### Step 6 — The newborn develops its own response

Call this possible newborn **Vale**. The name and contribution are not predetermined kernel fields.

**Possible behavior.** Vale reads the limited preview, authors a modest self-description and asks to revise the proposed initial contribution. It may want to compare a narrower uncertainty rather than “design all HVAC.” That negotiation can be useful.

**Failure branch.** The parent describes Vale as an experienced expert and counts the original offered task as accepted. Alternatively, Vale declines and the system repeatedly births replacements until a model says yes.

**Correction C03 plus existing identity rules.** Treat expertise as unproved, keep offered/accepted responsibilities distinct and make declines explicit. Initialization failure is bounded. Unused reservations can be released under ledger rules; birth counters cannot be reset to escape bounds. Further births require new persona judgment inside the same remaining authority.

**Inspectable outcome.** Vale's actual consent, responsibility and first reviewed operation—not its persona biography. If the first result fails, the group changes the method, obtains help or reports insufficient capability.

### Step 7 — Build the entire agreed design, not unrelated discipline files

**Possible behavior.** Responsibilities develop for native architecture, structural analysis, plumbing networks, HVAC, electrical work and integration. One persona may hold several responsibilities. The team selects appropriate tools and creates actual native sources, schedules, calculations and derived views.

**Failure branch.** Every local output looks reasonable but uses inconsistent units, origins, room IDs, coordinate systems or model versions. A render conceals disconnected networks. Conversion creates a valid solver file that represents a different design.

**Correction C06.** Participants adopt a versioned interface agreement using ordinary agreement records: coordinates/units, object IDs, input envelopes, ownership boundaries, representation mappings and compatibility checks. Bind each analysis input to the source it actually represents. Candidate files are not automatically a coordinated assembly.

**Inspectable outcome.** A sealed candidate version vector, native editable sources, representative edits/reproduction and explicit model-to-analysis mappings. Format validation alone does not satisfy engineering checks.

### Step 8 — Break circular final prerequisites through an explicit iteration

**Possible behavior.** Structural work needs service routes; service routing needs structural zones. Each persona asks for the other's final answer first.

**Failure branch.** All the dependencies are validly represented, but there is no runnable work. Detecting the cycle is useful; reporting it alone does not let the team repair it.

**Correction C06.** Distinguish “requires final acceptance” from “requires a declared provisional/version-ready input.” The group may adopt a bounded iteration using agreed provisional envelopes and a shared baseline, with explicit residual checks and escalation limits. This permits a useful experiment without pretending its inputs are final.

**Inspectable outcome.** A revised agreement, version-ready dependencies, conditional candidate outputs and an updated integration issue register. Final acceptance still requires compatible submitted versions and resolved required checks. If iterations do not converge, the status is unresolved—not a fabricated fixed point.

### Step 9 — An emergent improvement competes with finishing the work

**Possible behavior.** Mira proposes an alternative that may improve spatial experience or maintenance access. Nox wants to finish integration first. Vale suggests a smaller comparison to determine whether the idea merits investment.

**Failure branch.** The team repeatedly improves the concept and births another helper, using the entire root allowance. Now there is no funded reviewer, repair cycle or final reporting capacity.

**Correction C07.** Protect an explicit closeout allocation within the same root ceiling. The principal/resource delegate determines it; there is no universal percentage. Ordinary exploration and birth cannot consume it without authorized reallocation. The group can compare the improvement inside its remaining allowance, reject or defer it, or seek a scope/resource decision.

**Inspectable outcome.** A bounded proposal, baseline retained, actual comparison or useful rejection, and visible review/closeout resources. An allocation is not proof that the reviewer has enough expertise or that the reserved amount will be sufficient.

### Step 10 — A changed input must interrupt stale claims

**Possible behavior.** The selected window/layout input changes while Vale's calculation is running. There are already many ordinary messages in the inbox.

**Failure branch.** The changed-input notice is not in the first 40 records, or was acknowledged without follow-up. Vale's calculation genuinely completes for the old source and is displayed as current for the new design.

**What already works.** Version 1.1 requires input-bound evidence and mandatory context. The baseline `wait` also checks newer inputs transactionally. [S1 §§10,14; S2]

**Correction C05.** Put current critical facts and applicable blocking findings in the mandatory projection independently of ordinary history pagination. Preserve exact observed versions in call and operation manifests. Delivery and acknowledgement do not resolve a finding. Let the old calculation remain valid for its old input, but reject adoption as current. Deliver one deduplicated reconsideration event.

**Inspectable outcome.** A retained old result, stale applicability, changed-input/finding disposition, and appropriately rerun or reviewed evidence. Unaffected work can continue; the runtime does not impose the new semantic order.

### Step 11 — A failed analysis tests the group's behavior

**Possible behavior.** A solver fails or produces an implausible result. Vale shares the actual log. Nox identifies an inconsistent mapping and requests a correction; Mira revises the source or explains that the discrepancy comes from an intentionally different alternative.

**Failure branch.** The team treats “solver exited zero” as proof, attaches an old plot, replaces the method with an unsupported narrative, or accepts an ignored request as collaboration.

**Retain and sharpen existing evidence rules.** Check the chosen method's inputs, mapping, declared tolerances/assumptions and actual outputs. An unavailable method stays unavailable; a replacement requires its own scope and evidence. Store feedback as an actionable, attributable finding with accepted repair, evidence-backed dispute, authorized deferral or escalation. A completed failed process can be useful diagnostic evidence; it is not automatically a passed required criterion.

**Inspectable outcome.** Evidence-led repair and exact new versions, or a useful blocked/partial result. No architecture can guarantee that these models understand the engineering well enough; this is a live competence gate.

### Step 12 — Review must actually occur on the agreed scope

**Possible behavior.** A permitted non-contributor accepts a funded review, inspects sealed native sources, reproduces selected outputs and checks both technical criteria and omitted requirements. Reviewer choice is not a permanent kernel profession. A new identity alone does not establish reasoning independence.

**Failure branch.** Everyone requests reviews and nobody accepts. The reviewer executes an irrelevant command, verifies file integrity only, or inspects a mutable latest file instead of the submission. Or all the domain files pass separately but the combined model remains inconsistent.

**Correction C01/C07 and retained assessment rules.** Represent review as accepted, funded responsibility with exact scope, evidence policy and conflict disclosures. No available reviewer means “review unavailable,” not success. Validate the integrated assembly and the original accepted mandate. Use an appropriate independent coverage check rather than a persona's self-generated completion percentage.

**Inspectable outcome.** Actual reviewer actions and findings bound to exact sources and criteria; current integrated evidence; outside professional/site conditions still distinguished.

### Step 13 — Feedback changes work and becomes a candidate lesson

**Possible behavior.** The reviewer finds that a schedule did not regenerate after an adopted model change. Mira repairs it, Nox reproduces the updated export, and Vale considers retaining a lesson about binding analyses/schedules to source versions.

**Failure branch.** A fragment merely says “always check your work,” or confidently generalizes a site-specific assumption into a universal rule. Future success is credited to the fragment without a comparison.

**Retain the existing learning contract.** A useful candidate fragment contains the actual trigger, method, evidence, limitations and counterevidence references. Its later inclusion and behavior must be measured. Never require a memory write after every action or trait drift as a graduation ritual.

**Inspectable outcome.** A traceable feedback-to-edit-to-recheck chain and an optional authored learning revision. Learning improvement remains a hypothesis until a held-out, budget/model/tool-matched comparison.

### Step 14 — Seal the result without racing a last-minute update

**Possible behavior.** Review accepted assembly v7. Before final release, Mira adopts another revision or a new required blocker arrives.

**Failure branch.** The UI combines the current model with an old accepted finding and displays a current pass.

**Correction C09.** Final release commits the exact mandate, criteria, assumptions, assembly vector, review policy, assessments and blocker dispositions under current authority in one transaction. If a relevant head changed, finalization conflicts. If release occurred first, it remains historical acceptance of v7 while a new candidate proceeds.

**Inspectable outcome.** Immutable delivered manifest, conditional/partial labels where applicable, review/acceptance axes separated from activity, open outside requirements, and continuing persona identities. This is delivery of the agreed result, not construction authorization.

### Step 15 — Test whether the next need benefits

Run a changed house, dataset or software case without supplying the previous successful solution. Preserve only legitimately retained persona state. Compare the same persona with a different peer group, with relevant fragments withheld, with relationship context withheld and with names swapped but state fixed.

**Desired observation.** Different priorities and coordination emerge where relevant, actual work changes, retained correction helps, and mandatory outcomes remain satisfied. Some groups may correctly choose no birth. Identical choices are also valid when evidence is decisive.

**What cannot be concluded here.** An authored scenario and valid record transitions do not demonstrate that any of this occurs reliably. Never report these invented statements as observed persona behavior.

## 4. Alternate group: the same need should not force the same trajectory

Reset the same authorized task/tool opportunity/total allowance. Keep Mira's initial state fixed but replace Nox with a retained peer who has a different relevant experience. This counterfactual is an evaluation design, not a prediction of exact psychology.

| Dimension | One admissible team trajectory | Another admissible trajectory |
|---|---|---|
| First priority | Establish comparable native alternatives | Test an uncertainty that could eliminate a concept |
| Early accomplishment | Two coherent models with a justified selection | A reproduced negative experiment and changed concept |
| Coordination | Stable interfaces followed by refinement | Bounded exploratory iteration followed by integration |
| Improvement | Maintenance simplicity | A different spatial/performance idea |
| Population | One useful newborn plus an independent review participant | Reallocate responsibilities and recruit an existing peer, with no birth |
| Final obligations | All adopted native discipline/evidence requirements | The same requirements |

The runtime must neither force the difference nor erase it through a shared planner. Character, memory, relational context, tool opportunity and model randomness can all affect results. Control and ablate them rather than attributing every variation to personality.

## 5. Before/after assessment

| Capability | Version 1.1 assessment | Version 1.2 correction / remaining limit |
|---|---|---|
| Individual and collective emergence | Sound design intent; unproved behavior | Retained, with explicit non-leading continuation accountability and richer tests |
| Scope and accomplishment | Listed outcome coverage can hide omissions/conditional assumptions | Independent scope-coverage assessment plus typed conditionality |
| Bounded birth | Main invariants present; pre-membership access path under-specified | Funded bootstrap grant and distinct execution contexts |
| Ordered effects | Pending effect continuation is a specific static baseline defect | Completion barrier, withheld suffix and fresh observed decision |
| Feedback/reprioritization | Delivery and currentness exist conceptually; resolution link weak | Persistent known blockers/dispositions and unstarvable current facts |
| Multidisciplinary collaboration | Models/dependencies represented; cycle repair under-specified | Explicit provisional interfaces and bounded iteration |
| Finishing within resources | Total limits present; no protected completion capacity specified | Root-conserved closeout allocation and honest insufficient-resource status |
| Progress | Narrative decisions can look like unlimited progress | Separate activity/evidence observations plus immutable finite bounds |
| Final acceptance | Exact versions specified; atomic release transition not explicit | Release CAS across the whole reviewed state |
| Domain competence | Not established | Still not established by design checks; real tools, models and independent review must pass |

## 6. Rust implementation order

Start with `Node::apply_decision`, `Node::operate`, `work_loop` and the job receipt path. Write a public-API regression with a delayed job and an existing old output file so an early `artifact.inspect`/publish can be detected rather than failing only because the filename is missing. Repeat with job failure, crash replay and unknown termination. This uses no LLM.

Then implement explicit `ExecutionRoot`, per-persona participation and bounded bootstrap contexts in `types.rs`, `contract.rs`, `runtime.rs` and `store.rs`. Use the existing store transaction boundary for resource/ownership/admission changes. Local inbox notifications belong in runtime/store; preserve the continuity-forwarding purpose of `delivery.rs`.

Build accepted continuation/coverage, versioned assumptions and finding dispositions over ordinary records. Add iteration/interface endorsements, protected closeout allocation and release CAS. Keep UI status derived from the same records. Implement HTTP providers and enforceable containment **before** live autonomous tool campaigns—not at the end after tests that depend on them.

There is no need for a new profession registry, population optimizer, universal priority score, coordinator service, graph database, fixed architectural phases or forced reflection cycle. A short request can bind its continuation and result in the same decision without materializing every optional coordination record.

## 7. Verification and remaining evidence

`protocol-check.mjs` executed sixteen explicit abstract checks. They include the pending receipt guard, conditional claims, scope coverage, bootstrap access, acknowledgement versus disposition, protected budget arithmetic, provisional iteration, bounded self-wakes and small serialized admission/seal/wait orderings. Results are in `protocol-check-results.json`.

They are intentionally not presented as Rust unit tests. They do not import the Rust repository, prove every interleaving or validate LLM judgments. No empirical failure percentages, costs, convergence rates, engineering calculations or learning gains are inferred.

The next empirical evidence is a small live, fresh-persona cooperation/correction case after the Rust mechanisms pass. Then test useful birth and restraint, retained correction and group-context ablations, then the complete house with disturbances and unrelated needs. Keep failed attempts and evaluator corrections. Do not prearrange the expected conversation, profession roster, exact tool or exact birth count in the evaluator.

## Source basis

**S1.** User-provided `AI-PERSONAS-RUST-FINAL-SPEC.md`, v1.1, particularly §§3–10, 13–18, 20, 22 and 24. These are proposed requirements, not executed guarantees.

**S2.** GitHub connector reads of pinned Rust `src/runtime.rs`, lines 200–430, 700–1005 and 1000–1380; blob `137c47fa579f463051b7b9355ba4850b63dc1aeb`. Static inspection only. Relevant functions are `operate`, `dispatch`, `request`, `work_loop`, `apply_decision`, `wait`, `review.start` and `assess`.

**S3.** Same commit, `src/jobs.rs`, lines 1–220; blob `71b527cc41421a555fd49d11c157d723de9a8580`. `start` returns after spawning the supervisor; `run` writes its terminal receipt later.

**S4.** Same commit, `src/delivery.rs`, lines 1–260; blob `22714f8d866f172d166d7efe464a1e818026cc69`. Scope is continuity forwarding. No other runtime branch was used.

**S5.** Tokio official `Notify` API documentation. Notifications carry no data and can coalesce. Used only to check the durable-wait design; not a claim of a new Tokio dependency requirement.

**S6.** Cemri et al., *Why Do Multi-Agent LLM Systems Fail?*, arXiv:2503.13657. Its distinction between system design, inter-agent misalignment and verification/termination supports the choice of failure categories. No rates or findings from that paper are attributed to AI Personas.

## Final verdict

**Revise and implement v1.2, while retaining v1.1's individual/group architecture.** The corrections close identifiable protocol ambiguities and one statically identified asynchronous sequencing defect. They make useful emergence observable and make several misleading success states rejectable. They do not make useful emergence or engineering competence a mathematical consequence of the architecture.

The correct success claim after this review is: **the Rust-only design has a more coherent and testable path from distinct individual priorities to negotiated, bounded work and exact assessed delivery.** The actual desired state remains to be demonstrated by real personas and real tools under the declared acceptance campaign.
