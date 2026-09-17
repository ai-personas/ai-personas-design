"""Check the core planning manifest; never infer runtime acceptance from it."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path, PurePosixPath
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MECHANICAL = {f"M{i:02d}" for i in range(1, 27)} - {"M14"}
BEHAVIORAL = {f"B{i:02d}" for i in range(1, 13)}
INVARIANTS = {f"I{i:02d}" for i in range(1, 22)}
SHA = re.compile(r"[0-9a-f]{40}\Z")


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_plan(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    if len(raw) > 1_048_576:
        raise ValueError("plan exceeds the one MiB document limit")
    value = json.loads(raw, object_pairs_hook=unique_object)
    if not isinstance(value, dict):
        raise ValueError("plan must be a JSON object")
    return value


def validate(plan: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    def rows(name: str) -> list[dict[str, Any]]:
        value = plan.get(name)
        if not isinstance(value, list) or not all(isinstance(x, dict) for x in value):
            errors.append(f"{name} must be an array of objects")
            return []
        return value

    def obj(name: str) -> dict[str, Any]:
        value = plan.get(name)
        if not isinstance(value, dict):
            errors.append(f"{name} must be an object")
            return {}
        return value

    def text(value: Any) -> bool:
        return isinstance(value, str) and bool(value.strip())

    require(plan.get("schema") == "ai-personas/core-implementation-plan/1", "unexpected planning schema")
    require(plan.get("not_backend_schema") is True, "plan must not impersonate a backend schema")
    require(obj("normative_design") == {"path": "technical/SPEC.md", "version": "1.2"}, "normative design must remain SPEC.md v1.2")
    scope = obj("scope")
    require(scope.get("design_repository") == "ai-personas/ai-personas-design", "wrong design target")
    require(scope.get("runtime_repository") == "ai-personas/ai-personas", "wrong runtime target")
    require(scope.get("branch") == "rewrite/design-first", "wrong implementation branch")
    for key in ("ui_changes", "runtime_source_changes_in_this_increment", "federation_transport_redesign"):
        require(scope.get(key) is False, f"scope must explicitly exclude {key}")
    baseline = obj("baseline")
    for key in ("design_commit", "runtime_commit", "historical_runtime_commit"):
        value = baseline.get(key)
        require(isinstance(value, str) and SHA.fullmatch(value) is not None, f"{key} must be a full commit SHA")
    require(baseline.get("runtime_contract") == "ai-personas/1", "do not advertise unimplemented v2 authoring")
    require(baseline.get("proposed_authoring_contract") == "ai-personas/2", "target authoring contract must be explicitly proposed")
    require(baseline.get("evidence") == "source_report_only", "baseline is not executed runtime evidence")
    invariants = plan.get("invariants")
    require(isinstance(invariants, list) and all(isinstance(x, str) for x in invariants)
            and len(invariants) == len(INVARIANTS) and set(invariants) == INVARIANTS,
            "all I01-I21 invariants must appear exactly once")

    gate_ids: set[str] = set()
    for family, expected in (("mechanical_gates", MECHANICAL), ("behavioral_gates", BEHAVIORAL)):
        entries = rows(family)
        ids = [entry.get("id") for entry in entries]
        valid_ids = [x for x in ids if isinstance(x, str)]
        require(len(valid_ids) == len(ids) == len(expected) and set(valid_ids) == expected,
                f"{family} must have its complete, unique source-aligned ID set")
        gate_ids.update(valid_ids)
        for entry in entries:
            label = entry.get("id", family)
            require(text(entry.get("title")), f"{label}: missing title")
            require(text(entry.get("required_evidence")), f"{label}: missing evidence requirement")
            require(entry.get("verification") == "not_verified", f"{label}: planning checks cannot claim a runtime pass")
    deferred = rows("deferred_gates")
    require(len(deferred) == 1 and deferred[0].get("id") == "M14"
            and text(deferred[0].get("reason")), "M14 must remain explicitly deferred, not dropped or passed")

    streams = rows("workstreams")
    stream_ids = [s.get("id") for s in streams]
    require(all(isinstance(x, str) for x in stream_ids) and len(stream_ids) == 8
            and set(x for x in stream_ids if isinstance(x, str)) == {f"K{i}" for i in range(8)},
            "workstreams must contain K0-K7 exactly once")
    by_id = {s["id"]: s for s in streams if isinstance(s.get("id"), str)}
    coverage: set[str] = set()
    edges: dict[str, list[str]] = {}
    for key, stream in by_id.items():
        require(text(stream.get("title")), f"{key}: missing title")
        require(stream.get("source_status") in {"required", "reported_unverified"}, f"{key}: unsupported source status")
        dependencies = stream.get("requires")
        if not isinstance(dependencies, list) or not all(isinstance(x, str) for x in dependencies):
            errors.append(f"{key}: requires must be an ID array")
            dependencies = []
        require(len(dependencies) == len(set(dependencies)), f"{key}: duplicate dependency")
        require(all(x in by_id and x != key for x in dependencies), f"{key}: unknown/self dependency")
        edges[key] = dependencies
        sections = stream.get("spec_sections")
        require(isinstance(sections, list) and bool(sections)
                and all(type(x) is int and 0 <= x <= 25 for x in sections), f"{key}: invalid source section")
        paths = stream.get("runtime_paths")
        if not isinstance(paths, list) or not paths:
            errors.append(f"{key}: runtime paths required")
            paths = []
        for path in paths:
            if not isinstance(path, str):
                errors.append(f"{key}: invalid runtime path")
                continue
            parts = PurePosixPath(path).parts
            require(bool(parts) and not PurePosixPath(path).is_absolute() and ".." not in parts
                    and "\\" not in path and parts[0] in {"src", "tests", "integtest", "curricula", "docs"},
                    f"{key}: non-core or unsafe runtime path {path!r}")
        gates = stream.get("gates")
        if not isinstance(gates, list) or not all(isinstance(x, str) for x in gates):
            errors.append(f"{key}: gates must be an ID array")
            gates = []
        require(bool(gates) and all(x in gate_ids for x in gates), f"{key}: missing/unknown gate")
        coverage.update(gates)
    require(coverage == MECHANICAL | BEHAVIORAL, "workstreams must cover every core gate without including M14")

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(key: str) -> None:
        if key in visiting:
            errors.append("implementation dependency cycle")
            return
        if key in visited:
            return
        visiting.add(key)
        for dependency in edges.get(key, []):
            if dependency in edges:
                visit(dependency)
        visiting.remove(key)
        visited.add(key)

    for key in edges:
        visit(key)
    safety = obj("safety")
    require(safety.get("live_tool_campaign_requires") == ["K1", "K2"], "live work needs both authority and provider/isolation prerequisites")
    require(safety.get("private_runtime_source_must_not_be_published") is True, "private runtime publication guard required")
    require(safety.get("runner_implies_full_acceptance") is False, "existing suite execution is not full acceptance")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, default=ROOT / "technical/core-gates.json")
    args = parser.parse_args()
    try:
        errors = validate(load_plan(args.plan))
    except (OSError, ValueError, TypeError) as exc:
        errors = [str(exc)]
    report = {"status": "failed" if errors else "passed", "scope": "Planning manifest consistency only; no Rust, model, security or engineering verification.",
              "core_mechanical_requirements": len(MECHANICAL), "behavioral_requirements": len(BEHAVIORAL), "deferred": ["M14"], "errors": errors}
    print(json.dumps(report, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
