# Personal exploration: episode-wide limits and fair scheduling

[Design index](README.md) · [Persona development](PERSONA-DEVELOPMENT.md) · [Authority and resources](05-authority-and-resources.md)

This is a normative clarification of the personal-exploration rules. It describes required behavior, not an assertion that an implementation or live evaluation has passed.

## An episode is the funding boundary

An episode's call and time allowances apply to its whole work, not separately to each participation. Orientation, collaborators, later reviewers, nested model invocations, and failed admitted attempts share that allowance. Inviting someone must not multiply the available calls or create another deadline. The original operator-authorized policy remains controlling; a collaborator's consent and ordinary access and resource checks remain necessary.

A participant without an episode label in its presentation is not exempt. Funding classification follows the work's authoritative connection to its episode. The same connection distinguishes optional participation from foreground user work. A peer review must not be mistaken for new user work merely because it was created later.

Starting unrelated work is not a way to escape an episode's bounds. A distinct personal episode requires its own currently authorized scheduled opportunity. Methods, experiments, and collaboration can continue within the authorized episode; no profession, tool, domain solution, or mandatory sequence is imposed. An implementation that supports child work must preserve the same controlling limits rather than silently treating the child as unlimited foreground work.

Protected finishing capacity remains unavailable to optional production across every participation. An episode cannot be reported finished while a collaborator still has an accepted, unresolved responsibility in that work. Ending activity does not by itself undo an effect, establish acceptance, or resolve a finding. Necessary handoffs and dispositions remain explicit and attributed.

## A preview page must not control who can run

A page of opportunities is a bounded view, not a fixed eligibility ceiling. Future-dated opportunities must not hide an already due opportunity. Temporarily ineligible owners must not indefinitely prevent another eligible owner from being considered. Scheduling retains user-work priority and the authorized earliest start time without ranking domain solutions.

Imported, historical, erased, or withdrawn opportunities must not acquire local execution authority through queue discovery. A failed optional start must leave an inspectable blocked disposition, without consuming an episode or retaining provisional work as if creation had succeeded. Its failure must not roll back unrelated scheduling activity. Retrying requires an authorized trigger; repeatedly examining the same failed opportunity must not create an inference loop.

## Controls preserve the actual permission

The interface must represent every supported allowance without rounding it to a larger unit. A sub-minute duration or a duration that is not a whole number of minutes must remain editable and disableable. Opening a permission editor must not renew expiry, drop its precision, or reinterpret an unchanged time during a daylight-saving overlap. Invalid or nonexistent local times require correction, not silent normalization or a replacement grant.

Tests should separately cover queue pagination, due-time filtering, late collaborators, episode-wide charges, current policy and expiry, protected finishing resources, provisional-start rollback, and exact permission editing. Query tests and interface fixtures are not substitutes for runtime admission tests, live behavioral evidence, or a verified release.
