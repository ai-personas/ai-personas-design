#!/usr/bin/env python3
"""Validate the visual edition without application dependencies.

Use --render-dir with CairoSVG installed for PNG previews. Rendering and
structural checks are not product acceptance or a semantic proof.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SVG_NS = "http://www.w3.org/2000/svg"
EXPECTED_IDS = {f"P{i:02d}" for i in range(1, 6)} | {f"D{i:02d}" for i in range(1, 8)}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def local_path(value: str) -> Path:
    path = (ROOT / value).resolve()
    require(path.is_relative_to(ROOT), f"Path escapes repository: {value}")
    return path


def validate(render_dir: Path | None, check_source: bool) -> dict:
    manifest = json.loads((ROOT / "visual-manifest.json").read_text(encoding="utf-8"))
    artworks = manifest["artworks"]
    require(len(artworks) == 12, "Expected five posters and seven diagrams")
    require({a["id"] for a in artworks} == EXPECTED_IDS, "Missing or duplicate artwork IDs")
    paths = [a["file"] for a in artworks]
    require(len(set(paths)) == 12, "Duplicate artwork paths")
    actual = {str(p.relative_to(ROOT)) for p in (ROOT / "assets/visuals").glob("*.svg")}
    require(set(paths) == actual, "Manifest and SVG directory differ")
    guide = (ROOT / "VISUAL-GUIDE.md").read_text(encoding="utf-8")
    render = None
    if render_dir is not None:
        try:
            import cairosvg
        except ImportError as exc:
            raise ValueError("Optional rendering requires CairoSVG") from exc
        render = cairosvg.svg2png
        render_dir.mkdir(parents=True, exist_ok=True)

    results = []
    for item in artworks:
        path = local_path(item["file"])
        raw = path.read_bytes()
        xml = raw.decode("utf-8")
        require("<!DOCTYPE" not in xml.upper() and "<!ENTITY" not in xml.upper(), f"DTD/entity in {path.name}")
        root = ET.fromstring(xml)
        require(root.tag == f"{{{SVG_NS}}}svg", f"Not a namespaced SVG: {path.name}")
        width, height = item["width"], item["height"]
        require(width > 0 and height > 0, f"Invalid dimensions: {path.name}")
        require(root.get("viewBox") == f"0 0 {width} {height}", f"viewBox mismatch: {path.name}")
        require(float(root.get("width", "0")) == width and float(root.get("height", "0")) == height, f"Size mismatch: {path.name}")
        require(root.get("role") == "img", f"Missing image role: {path.name}")
        ids = [e.get("id") for e in root.iter() if e.get("id")]
        require(len(ids) == len(set(ids)), f"Duplicate XML IDs: {path.name}")
        labelled = root.get("aria-labelledby", "").split()
        require(len(labelled) == 2 and all(i in ids for i in labelled), f"Missing accessible labels: {path.name}")
        for tag in ("title", "desc"):
            element = root.find(f"{{{SVG_NS}}}{tag}")
            require(element is not None and "".join(element.itertext()).strip(), f"Missing {tag}: {path.name}")
            require(element.get("id") in labelled, f"Unlinked {tag}: {path.name}")
        for element in root.iter():
            tag = element.tag.rsplit("}", 1)[-1].lower()
            require(tag not in {"script", "foreignobject", "image", "iframe", "animate", "set"}, f"Non-static content in {path.name}")
            for key, value in element.attrib.items():
                attr = key.rsplit("}", 1)[-1].lower()
                require(not attr.startswith("on"), f"Event handler in {path.name}")
                if attr == "href":
                    require(value.startswith("#") and value[1:] in ids, f"External or broken reference in {path.name}")
            if tag == "style":
                css = "".join(element.itertext())
                require("@import" not in css.lower() and "@font-face" not in css.lower(), f"External style/font in {path.name}")
            if tag in {"rect", "circle"}:
                if tag == "rect":
                    x, y, w, h = [float(element.get(k, "0")) for k in ("x", "y", "width", "height")]
                else:
                    cx, cy, radius = [float(element.get(k, "0")) for k in ("cx", "cy", "r")]
                    x, y, w, h = cx - radius, cy - radius, 2 * radius, 2 * radius
                require(x >= 0 and y >= 0 and w >= 0 and h >= 0 and x + w <= width and y + h <= height, f"Shape outside viewBox: {path.name}")
        for target in re.findall(r"url\(\s*['\"]?([^)'\"\s]+)", xml):
            require(target.startswith("#") and target[1:] in ids, f"External or broken URL in {path.name}")
        require(item["file"] in guide, f"Artwork absent from guide: {path.name}")
        require(item["source_anchor"] in guide, f"Source link absent from guide: {path.name}")
        require("PROPOSED DESIGN" in xml and "NOT IMPLEMENTATION EVIDENCE" in xml, f"Missing evidence status: {path.name}")
        if render is not None:
            render(bytestring=raw, write_to=str(render_dir / (path.stem + ".png")), output_width=1600)
        results.append({"id": item["id"], "file": item["file"], "sha256": hashlib.sha256(raw).hexdigest(), "xml_and_structure": "pass", "raster_render": "pass" if render else "not_run"})

    source_result = "not_run"
    if check_source:
        source = local_path(manifest["source_file"]).read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(source)).encode("ascii") + b"\0" + source).hexdigest()
        require(blob == manifest["source_blob_sha"], "Proposal changed; review visual mappings and update the manifest")
        require(len(re.findall(rb"^```mermaid\s*$", source, re.MULTILINE)) == 7, "Expected seven original Mermaid blocks")
        source_result = "pass"
    return {"artwork_count": len(results), "source_integrity_check": source_result, "product_acceptance_executed": False, "results": results}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--render-dir", type=Path, help="Optional PNG output directory; requires CairoSVG")
    parser.add_argument("--check-source", action="store_true", help="Verify original proposal blob and Mermaid count on a full checkout")
    parser.add_argument("--json-report", type=Path, help="Write a machine-readable result")
    args = parser.parse_args()
    try:
        report = validate(args.render_dir, args.check_source)
        if args.json_report:
            args.json_report.parent.mkdir(parents=True, exist_ok=True)
            args.json_report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    except (OSError, ValueError, KeyError, TypeError, ET.ParseError) as exc:
        print(f"Visual validation failed: {exc}", file=sys.stderr)
        return 1
    print(f"PASS: {report['artwork_count']} self-contained SVG artworks; source integrity: {report['source_integrity_check']}.")
    print("Structural validation is not a layout, semantic, or product acceptance test.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
