# AI Personas — Design & Visual Field Guide

**Distinct perspectives. Accountable outcomes.**

A design-first proposal for persistent AI collaborators, cooperative societies, and evidence-linked work. The complete proposal now presents five professional overview posters and seven poster-style system diagrams inline, all as editable, self-contained SVGs.

![Three responsibility layers: humans authorize purpose, personas choose and accept work, and the supporting system enforces limits and preserves consequences.](assets/visuals/poster-01-blueprint.svg)

## Start here

**[Read the complete design proposal](AI-PERSONAS-DESIGN-PROPOSAL.md)** for the full 30-section design with professional posters, the invariant catalogue, and acceptance requirements. Each of the seven system diagrams opens with its poster; expand **View editable Mermaid source** to inspect the original diagram markup. Written requirements take precedence over visual summaries.

**[Explore the visual field guide](VISUAL-GUIDE.md)** for a gallery of all twelve sheets, accessible text readings, and links to the relevant requirements.

## The visual edition

| Overview posters | Poster-style system diagrams |
|---|---|
| [Blueprint](assets/visuals/poster-01-blueprint.svg) | [Functional embodiment loop](assets/visuals/diagram-01-embodiment-loop.svg) |
| [End-to-end journey](assets/visuals/poster-02-end-to-end-flow.svg) | [Conceptual architecture](assets/visuals/diagram-02-conceptual-architecture.svg) |
| [Persona anatomy](assets/visuals/poster-03-persona-anatomy.svg) | [Identity lifecycle](assets/visuals/diagram-03-identity-lifecycle.svg) |
| [Persona society](assets/visuals/poster-04-persona-society.svg) | [Birth, membership, and commitment](assets/visuals/diagram-04-onboarding.svg) |
| [Embodiment requirements](assets/visuals/poster-05-embodiment-requirements.svg) | [Learning loop](assets/visuals/diagram-05-learning-loop.svg) |
| | [Evidence chain](assets/visuals/diagram-06-evidence-chain.svg) |
| | [Complete journey with return paths](assets/visuals/diagram-07-complete-journey.svg) |

The SVGs use selectable text, a consistent editorial grid, restrained color, explicit decision labels, and a source reference on every sheet. No external images, scripts, or font downloads are required. Open an individual SVG in a browser or vector editor to zoom, edit, or print it. Font substitution can change text metrics; check the render after editing.

## Package layout

| Item | Purpose |
|---|---|
| `AI-PERSONAS-DESIGN-PROPOSAL.md` | Complete requirements with twelve inline SVG posters and expandable Mermaid source |
| `VISUAL-GUIDE.md` | Poster gallery and full text equivalents |
| `assets/visuals/` | Twelve editable SVGs and visual maintenance notes |
| `visual-manifest.json` | Artwork inventory, dimensions, source-section mapping, and current proposal fingerprint |
| `visual-validation.json` | Historical checks performed when visual edition 01 was created |
| `scripts/validate_visuals.py` | Dependency-free SVG/package checks; optional raster rendering |
| `assets/*.png` | Five original illustrations retained for provenance, no longer embedded in the proposal |
| `sources/` | Original source reports and source manifest, unchanged |
| `package-validation.json` | Historical validation record for the original proposal package |

## Maintain and check

```sh
python3 scripts/validate_visuals.py
# Optional, with CairoSVG installed:
python3 scripts/validate_visuals.py --render-dir /tmp/ai-personas-visuals
# On a complete checkout, verify the current proposal fingerprint and Mermaid count:
python3 scripts/validate_visuals.py --check-source
```

See [visual maintenance notes](assets/visuals/README.md) for the palette, layout conventions, and editing checklist. Keep the manifest's `source_blob_sha` synchronized after reviewing changes to the proposal. The artwork edition remains 01; presentation revision 02 integrates that existing artwork into proposal version 1.1.

## Evidence and provenance

This revision changes the visual presentation, not the behavioral requirements. It replaces the proposal's embedded PNG illustrations with the professional SVG suite and makes the seven poster-style diagrams the default view. All seven original Mermaid blocks remain editable in expandable sections, with visible prose readings. The twelve SVG files, five original PNG files, supplied source reports, and historical validation records are unchanged.

The existing `visual-validation.json` describes checks performed for the earlier artwork edition, not a fresh validation run of this integration. Review the committed diff to inspect the presentation changes; run the commands above on a full checkout for current package checks.

The design is **proposed, not an implemented or validated product**. The 26 mechanical, 12 behavioral, and six extension acceptance tests remain specifications, not executed results. Visual rendering and structural checks do not establish persona competence, safety, learning, or deployment readiness. The later v1.2 source continues to govern conceptual conflicts; extensions E1–E6 retain their proposed status.
