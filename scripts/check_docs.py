"""Offline documentation checks. No provider calls or runtime acceptance claims."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^\]\n]*\]\(([^\s)]+)(?:\s+[\"'][^\n]*?[\"'])?\)")
FENCE = re.compile(r"^\s{0,3}(`{3,}|~{3,})(.*)$")


def slug(text: str) -> str:
    text = re.sub(r"<[^>]*>", "", text).lower().replace("`", "")
    text = re.sub(r"[^\w\-\s]", "", text, flags=re.UNICODE)
    return re.sub(r"\s", "-", text.strip())


def scan(text: str) -> tuple[str, set[str], list[dict], list[str]]:
    """Exclude fenced examples from link/anchor scanning; extract Mermaid source."""
    prose: list[str] = []
    diagrams: list[dict] = []
    errors: list[str] = []
    anchors: set[str] = set()
    counts: Counter = Counter()
    fence = None
    language = ""
    body: list[str] = []
    first_line = 0
    for number, line in enumerate(text.splitlines(), 1):
        match = FENCE.match(line)
        if fence is not None:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                if language == "mermaid":
                    diagrams.append({"line": first_line, "source": "\n".join(body) + "\n"})
                fence = None
                body = []
            else:
                body.append(line)
            continue
        if match:
            fence, language = match[1], match[2].strip()
            first_line = number
            continue
        prose.append(line)
        heading = re.match(r"^#{1,6}\s+(.+?)(?:\s+#+)?$", line)
        if heading:
            base = slug(heading[1])
            index = counts[base]
            counts[base] += 1
            anchors.add(base if index == 0 else f"{base}-{index}")
        anchors.update(re.findall(r'<(?:a|h[1-6])\s+[^>]*(?:id|name)=[\"\']([^\"\']+)[\"\']', line))
    if fence is not None:
        errors.append(f"unclosed code fence at line {first_line}")
    return "\n".join(prose), anchors, diagrams, errors


def link_errors(path: Path, prose: str, root: Path) -> tuple[int, list[str]]:
    checked = 0
    errors = []
    for raw in LINK.findall(prose):
        target = urlsplit(raw.strip("<>"))
        if target.scheme in {"https", "http", "mailto"} or target.netloc:
            continue  # Network availability is deliberately not claimed by this check.
        if target.scheme:
            errors.append(f"unsupported or local-only link: {raw}")
            continue
        checked += 1
        destination = (path.parent / unquote(target.path)).resolve() if target.path else path.resolve()
        if not destination.is_relative_to(root.resolve()):
            errors.append(f"link escapes repository: {raw}")
            continue
        if not destination.exists():
            errors.append(f"missing local target: {raw}")
            continue
        if target.fragment and destination.suffix.lower() == ".md":
            _, anchors, _, _ = scan(destination.read_text(encoding="utf-8"))
            if unquote(target.fragment) not in anchors:
                errors.append(f"missing local anchor: {raw}")
    return checked, errors


def main() -> int:
    output = ROOT / ".qa"
    diagram_dir = output / "diagrams"
    diagram_dir.mkdir(parents=True, exist_ok=True)
    for old in diagram_dir.glob("*.mmd"):
        old.unlink()
    errors: list[str] = []
    manifest = []
    files = sorted(p for p in ROOT.rglob("*.md") if not any(part in {".git", ".qa", "node_modules"} for part in p.relative_to(ROOT).parts))
    links = 0
    for path in files:
        text = path.read_text(encoding="utf-8")
        prose, _, figures, problems = scan(text)
        count, broken = link_errors(path, prose, ROOT)
        links += count
        name = path.relative_to(ROOT).as_posix()
        errors.extend(f"{name}: {e}" for e in problems + broken)
        if "sandbox:" in prose or "/mnt/data/" in prose:
            errors.append(f"{name}: chat-local path is not a repository reference")
        for figure in figures:
            index = len(manifest) + 1
            stem = f"{index:02d}-" + path.stem.lower()
            source_path = diagram_dir / f"{stem}.mmd"
            source_path.write_text(figure["source"], encoding="utf-8")
            if "In words" not in "\n".join(text.splitlines()[figure["line"]:figure["line"] + 65]):
                errors.append(f"{name}:{figure['line']}: diagram needs an adjacent prose equivalent")
            manifest.append({"document": name, "line": figure["line"], "source": str(source_path.relative_to(ROOT)), "stem": stem})
    spec = (ROOT / "technical/SPEC.md").read_text(encoding="utf-8")
    acceptance = (ROOT / "technical/ACCEPTANCE.md").read_text(encoding="utf-8")
    for number in range(26):
        if not re.search(rf"^## {number}\. ", spec, re.MULTILINE):
            errors.append(f"SPEC lacks source-aligned section {number}")
    for prefix, maximum, text in [("I", 21, spec), ("C", 9, spec), ("M", 26, acceptance), ("B", 12, acceptance)]:
        for number in range(1, maximum + 1):
            if f"| {prefix}{number:02d} |" not in text:
                errors.append(f"required traceability ID missing: {prefix}{number:02d}")
    api = (ROOT / "technical/API.md").read_bytes()
    blob = hashlib.sha1(f"blob {len(api)}\0".encode() + api).hexdigest()
    if blob != "367a31cc31e6e6283a8014eac3f7763d49b28188":
        errors.append("generated v1 API bytes changed; regenerate from Rust, do not hand-author v2 support")
    if len(manifest) < 8:
        errors.append("expected the explanatory architecture, people, execution and evidence diagrams")
    report = {"status": "failed" if errors else "passed", "scope": "Documentation structure, local links and source-ID coverage only. No runtime/model/engineering verification.", "markdown_files": len(files), "local_links_checked": links, "mermaid_diagrams": len(manifest), "generated_v1_api_blob": blob, "errors": errors}
    (output / "docs-checks.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    (output / "diagram-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
