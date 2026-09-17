"""Render the extracted Mermaid diagrams with a caller-supplied CLI."""
from pathlib import Path
import argparse
import json
import subprocess

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--mmdc", required=True)
args = parser.parse_args()
manifest = json.loads((root / ".qa/diagram-manifest.json").read_text())
output = root / ".qa/rendered"
output.mkdir(parents=True, exist_ok=True)
# This is only a throwaway documentation-rendering browser on CI, never product isolation.
puppeteer = root / ".qa/puppeteer.json"
puppeteer.write_text(json.dumps({"args": ["--no-sandbox"]}))
rendered = []
for item in manifest:
    for extension in ("svg", "png"):
        path = output / f"{item['stem']}.{extension}"
        subprocess.run([args.mmdc, "-i", str(root / item["source"]), "-o", str(path), "-p", str(puppeteer), "-c", str(root / "scripts/mermaid-config.json"), "-b", "white", "-w", "1400"], check=True, timeout=90, cwd=root)
        if not path.is_file() or path.stat().st_size == 0:
            raise RuntimeError(f"Missing rendered diagram: {path}")
    rendered.append({**item, "svg": f"rendered/{item['stem']}.svg", "png": f"rendered/{item['stem']}.png"})
report = {"status": "passed", "scope": "Mermaid CLI rendering only, not runtime behavior or GitHub-specific layout certification", "count": len(rendered), "diagrams": rendered}
(root / ".qa/diagram-checks.json").write_text(json.dumps(report, indent=2) + "\n")
print(f"Rendered {len(rendered)} Mermaid diagrams to SVG and PNG.")
