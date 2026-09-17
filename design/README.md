# AI Personas visual design preview

[UI specification](../technical/UI.md) · [Canonical Rust specification](../technical/SPEC.md) · [Implementation status](../STATUS.md)

This is an interactive reference for the seven supplied designs. It is intentionally independent of the production Preact UI and Rust node. It runs no personas, models, simulations, installations or external actions, and stores nothing outside the current page's memory.

## Open it

From the repository root:

```sh
python3 -m http.server 8080 --bind 127.0.0.1
```

Open `http://127.0.0.1:8080/design/index.html` in a browser. No npm installation or build is needed. The source uses only local HTML, CSS and JavaScript, system fonts, initials and inline line icons. GitHub's file viewer displays source; it is not a deployed application.

| Route after `index.html` | View |
|---|---|
| `#/work` | Desktop/mobile Work overview, search, filters and response dialog |
| `#/personas` | Continuing persona cards and local presentation drafts |
| `#/persona/mira` | Character, current attention, retained experience and explicit absence of capability/model evidence |
| `#/work/home` | Work detail with all six canonical views |
| `#/environments` | Compact environment references |
| `#/learning` | Attributed illustrative notes and their limitations |
| `#/settings` and `#/tools` | Explicit unconnected state; no fake authorization or installation controls |
| `#/workspace/house/3` | Evolving-work reference with the model-change/stale-evidence snapshot |
| `#/workspace/dataset/3` | Same renderer, one-person/no-birth example |
| `#/workspace/story/3` | Same renderer, creative work and author acceptance |

## What the interactions mean

Search and filters operate on the local records. New work records an unowned draft; it does not recruit people. New persona creates a presentation draft with no invented biography, learning or real birth. Pause/resume changes a preview activity label only. Recording an answer changes an open request to **answered**, never resolved or approved. Reload or an explicitly confirmed reset restores the starting records.

The scoped-approval dialog is explanatory only and has no Approve control. There is no artifact download because this fixture contains no native artifacts. Replay buttons select authored snapshots; they do not launch a simulation or prescribe a runtime workflow. Calls are illustrative root allowances, not dollars or quality percentages. Protected closeout is unknown where not supplied.

The FINAL family defines the application shell. The WORKSPACE family defines the standalone evolving-work composition. The six-view detail and explicit authored-priority labels are deliberate refinements explained in [UI.md](../technical/UI.md). Tools is grouped under Settings in the pictured compact fixture only; its first-class production destination remains specified.

## Source provenance

[Source image fingerprints](source-images.json) identify the seven original user-supplied PNGs by exact filename, dimensions, byte size and SHA-256. This manifest does not reclassify screenshots as generated persona portraits or runtime evidence. The original attachments are not fetched from an external service by the prototype.

The Rust-only v1.2 specification supersedes v1.1 and the older proposals for behavior. The [existing canonical repository specification](../technical/SPEC.md) is retained, not replaced by a screenshot interpretation. No runtime or sibling UI repository is modified by this preview.

## Validate

The state suite needs Node.js 22, with no packages:

```sh
node --check design/state.js
node --check design/app.js
node --test tests/design-state.test.cjs
```

The optional browser suite uses Python Playwright and Chromium. Install Playwright in your preferred isolated Python environment and install its Chromium, then run:

```sh
python3 tests/browser_design.py
# Or use an existing Chromium executable:
python3 tests/browser_design.py --chromium /path/to/chromium
# Optional rendered images:
python3 tests/browser_design.py --screenshots .qa/design-images
```

The browser harness injects the exact checked-in HTML/CSS/JS into an empty page, rather than testing HTTP hosting or file-origin policy. It covers 266, 320, 390, 700, 768, 1024 and 1440 px viewports, eight routes, request state, literal hostile-looking text, modal focus, short-viewport scrolling, filters/caret, drafts, keyboard tabs, replay and non-granting approval previews. Results are written to `.qa/design-browser-checks.json`.

The existing repository documentation checks remain applicable:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_docs.py
```

[verification.json](verification.json) records what was actually run for this publication and its limits. These are fixture checks, not Rust protocol tests, live behavioral evaluation, a complete accessibility audit or proof that all browser resources are leak-free.
