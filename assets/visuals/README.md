# Visual edition 01 — maintenance notes

[Visual field guide](../../VISUAL-GUIDE.md) · [Written requirements](../../AI-PERSONAS-DESIGN-PROPOSAL.md)

## Editable artwork

These twelve SVG files are the editable sources. They contain native shapes, connectors, and selectable text; no raster illustrations, external dependencies, executable scripts, or embedded font files. Each SVG supplies an accessible title and description. The guide provides full text readings because an image viewer may not expose SVG accessibility metadata.

Most sheets use a `1600 × 1000` viewBox. D04 uses `1600 × 1100`; D07 uses `1600 × 1500` so its complete flow remains readable. Dimensions are logical drawing units, not a claim about print resolution. Vector geometry scales; verify font substitution and printer margins before producing a physical poster.

## Design tokens

| Role | Value |
|---|---|
| Paper | `#F7F5EF` |
| Primary ink / emphasis panels | `#102D3C` |
| Body ink | `#173443` |
| Secondary text | `#526976` |
| Connectors / accents | `#00786D` |
| Bounded or adopted state | `#E2F2EA` |
| Decision gate | `#FFF0D8` |
| Rules / borders | `#CAD6D5` |
| Typography | `Lato, Arial, sans-serif` |

The 72-unit page margin, repeated header/footer, concise labels, and restrained palette unify the series. No font binaries are distributed. Teal arrows indicate direction; double-headed arrows indicate exchange. Structural lines in P03 indicate components, not causal direction. Amber gates always carry a question or explicit check. A dark panel is visual emphasis, not a success indicator.

## Safe editing workflow

Edit an SVG in a text or vector editor. Preserve the root viewBox, `role="img"`, linked title/description IDs, and internal arrow marker. Keep textual labels and source references accurate. Reflow long labels rather than shrinking all text. Use the full text reading for nuance that would make a poster crowded.

Update `../../visual-manifest.json`, the matching proposal caption, and the text reading in `../../VISUAL-GUIDE.md` after a semantic change. Run `python3 scripts/validate_visuals.py` from the repository root. With CairoSVG installed, add `--render-dir /tmp/ai-personas-visuals` and inspect every output at full size. The validator catches structural regressions; it does not prove semantic equivalence or detect every visual collision. On a full checkout, `--check-source` checks the proposal against the manifest's `source_blob_sha` and confirms that seven Mermaid blocks remain. Review the changes before updating that fingerprint; it is an integrity reference, not an approval of the content.

Do not change proposal requirements merely to simplify a diagram. Preserve refusal, negotiation, revalidation, and honest-stop paths. Keep source-derived requirements separate from proposed extensions. The professional SVGs are now the default visuals in the proposal; the original Mermaid blocks remain in expandable source sections, and the original raster artwork remains in `assets/` for provenance.

## Presentation revision 02

Proposal version 1.1 integrates the existing artwork edition 01 without changing these twelve SVG files. Keep the artwork's historical source commit distinct from the current proposal fingerprint in the manifest. The earlier `visual-validation.json` and `package-validation.json` are historical records, not fresh test results for this presentation revision.
