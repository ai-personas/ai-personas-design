# Characteristic-grounded portrait references

These four images are visual references for the person-like avatar contract in
[`02_PERSONA.md §3.1b`](../../02_PERSONA.md#31b-characteristic-grounded-public-portrait).
They are **portrait candidates, not admitted identity assets**. A candidate may
become a public avatar only after the exact persona reviews the exact bytes and
admits a persona-signed descriptor. UI code must never use these files as an
unsigned override.

The live identity records used for this reference pass contained qualitative
characteristics but no numeric OCEAN or baseline-VAD values. The prompts
therefore use only the authored qualitative traits and do not invent scores.

## Shared prompt constraints

- square, centered head-and-shoulders portrait readable at 104 px;
- unmistakably a person, in a persona-selected artistic style;
- stable work posture expressed through face, posture, composition, texture,
  and palette;
- task or role motifs only as faint secondary background context;
- no text, logo, initials, robot, mask, document icon, or CAD object replacing
  or obscuring the person; and
- no inference of protected physical attributes from psychological traits.

## Persona-specific grounding

- `mara-vale.png`: evidence-first, direct, scope-conscious, package-integrating,
  and careful about separating verified facts from assumptions; calm,
  constructive confidence; teal and amber editorial portrait.
- `rowan-ives.png`: independent review posture, constructive skepticism,
  boundary-conscious evaluation, and attention to unresolved issues; composed
  slate/plum ink-and-gouache portrait.
- `niko-voss.png`: geometry-first, focused curiosity, collaborative bounded
  scope, and preference for inspectable structure; cobalt/moss contemporary
  editorial portrait.
- `lior-chen.png`: meticulous byte-level authorship, provenance awareness,
  calm inventiveness, and persistence through format constraints; indigo/jade
  painterly portrait.

When numeric OCEAN and baseline VAD are present, the persona-authored prompt
should describe how those exact stable values affect the visual choices. It
should not expose the raw values in the public PersonaCard or use transient mood
to churn identity.
