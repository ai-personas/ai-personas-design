# AI Personas — Design & Visual Field Guide

**Distinct perspectives. Accountable outcomes.**

A design-first proposal for persistent AI collaborators, cooperative societies, and evidence-linked work. The professional visual edition adds five overview posters and seven poster-style system diagrams, all as editable, self-contained SVGs.

![Three responsibility layers: humans authorize purpose, personas choose and accept work, and the supporting system enforces limits and preserves consequences.](assets/visuals/poster-01-blueprint.svg)

## Start here

**[Explore the visual field guide](VISUAL-GUIDE.md)** for the redesigned posters, all seven diagram companions, accessible text readings, and links to the relevant requirements.

**[Read the complete design proposal](AI-PERSONAS-DESIGN-PROPOSAL.md)** for the full 30-section design, invariant catalogue, original editable Mermaid diagrams, and acceptance requirements. Written requirements take precedence over visual summaries.

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
| `VISUAL-GUIDE.md` | Primary visual reading experience and text equivalents |
| `assets/visuals/` | Twelve new editable SVGs and visual maintenance notes |
| `visual-manifest.json` | Artwork inventory, dimensions, and source-section mapping |
| `visual-validation.json` | Checks performed for this visual edition only |
| `scripts/validate_visuals.py` | Dependency-free SVG/package checks; optional raster rendering |
| `AI-PERSONAS-DESIGN-PROPOSAL.md` | Complete conceptual and behavioral requirements |
| `assets/*.png` | Five original illustrations retained for provenance |
| `sources/` | Original source reports and source manifest, unchanged |
| `package-validation.json` | Historical validation record for the original proposal package |

## Maintain and check

```sh
python3 scripts/validate_visuals.py
# Optional, with CairoSVG installed:
python3 scripts/validate_visuals.py --render-dir /tmp/ai-personas-visuals
# On a complete checkout, also verify the original proposal and Mermaid count:
python3 scripts/validate_visuals.py --check-source
```

See [visual maintenance notes](assets/visuals/README.md) for the palette, layout conventions, and editing checklist.

## Evidence and provenance

This edition changes the visual presentation, not the behavioral requirements. The original proposal, its embedded PNG illustrations and Mermaid source, all five supplied reports, and the original package-validation record remain unchanged. The new visual guide is the entry point for the redesigned artwork; the original proposal still contains the historical images.

The design is **proposed, not an implemented or validated product**. The 26 mechanical, 12 behavioral, and six extension acceptance tests remain specifications, not executed results. Visual rendering and structural checks do not establish persona competence, safety, learning, or deployment readiness. The later v1.2 source continues to govern conceptual conflicts; extensions E1–E6 retain their proposed status.
