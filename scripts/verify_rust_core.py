"""Run existing Rust core suites on an exact private checkout, retaining local evidence.

This helper is not a sandbox and does not evaluate the complete v1.2 gate set.
Use only a disposable trusted Linux host without production credentials or nodes.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any

DESIGN_ROOT = Path(__file__).resolve().parents[1]
COMMANDS = (
    ("fixture_tests", ("python3", "-m", "unittest", "discover", "-s", "tests", "-p", "test_provider_fixtures.py", "-v")),
    ("fixture_syntax", ("python3", "-m", "py_compile", "integtest/provider_fixture.py", "integtest/completion_fixture.py")),
    ("format_check", ("cargo", "fmt", "--all", "--", "--check")),
    ("locked_build", ("cargo", "build", "--locked")),
    ("staged_receipts", ("cargo", "test", "--locked", "--lib", "decision_barrier_tests", "--", "--test-threads=1")),
    ("completion_barrier", ("cargo", "test", "--locked", "--test", "completion_barrier", "--", "--test-threads=1")),
    ("public_behavior", ("cargo", "test", "--locked", "--test", "behavior", "--", "--test-threads=1")),
    ("remaining_default_tests", ("cargo", "test", "--locked", "--", "--test-threads=1")),
)
# Explicit environment carriage reduces accidental token inheritance; this is
# NOT confidentiality from a program that can read the test account's files.
ENV_KEYS = {
    "PATH", "HOME", "USER", "LOGNAME", "TMPDIR", "LANG", "LC_ALL",
    "RUSTUP_HOME", "RUSTUP_TOOLCHAIN", "CARGO_HOME", "CARGO_TARGET_DIR",
    "CARGO_NET_OFFLINE", "CC", "CXX", "AR", "PKG_CONFIG_PATH",
    "LIBCLANG_PATH", "LD_LIBRARY_PATH", "SSL_CERT_FILE", "SSL_CERT_DIR",
}


def child_environment() -> dict[str, str]:
    env = {key: value for key, value in os.environ.items() if key in ENV_KEYS}
    env.update(CARGO_TERM_COLOR="never", PYTHONDONTWRITEBYTECODE="1")
    return env


def git_text(runtime: Path, *args: str) -> str:
    result = subprocess.run(["git", "-C", str(runtime), *args], capture_output=True,
                            text=True, check=True, timeout=30, env=child_environment())
    return result.stdout.strip()


def private_evidence_directory(requested: Path | None, runtime: Path) -> Path:
    if requested is None:
        # mkdtemp creates a new 0700 directory, never reusing earlier evidence.
        result = Path(tempfile.mkdtemp(prefix="ai-personas-core-evidence-")).resolve()
    else:
        result = requested.expanduser().resolve()
        if result.is_relative_to(DESIGN_ROOT.resolve()) or result.is_relative_to(runtime.resolve()):
            raise ValueError("evidence must remain outside both design and runtime repositories")
        result.mkdir(mode=0o700, parents=False, exist_ok=False)
    if result.is_relative_to(DESIGN_ROOT.resolve()) or result.is_relative_to(runtime.resolve()):
        # Do not remove an existing caller directory; this path is fresh only.
        result.rmdir()
        raise ValueError("temporary evidence path falls inside a repository; choose an explicit private path")
    return result


def save_report(directory: Path, report: dict[str, Any]) -> None:
    temporary = directory / "report.json.tmp"
    temporary.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    os.chmod(temporary, 0o600)
    temporary.replace(directory / "report.json")


def run_command(argv: tuple[str, ...], runtime: Path, log: Path, timeout: int) -> dict[str, Any]:
    started = time.time()
    row: dict[str, Any] = {"argv": list(argv), "started_unix": started, "log": log.name, "status": "running"}
    with log.open("wb") as output:
        os.chmod(log, 0o600)
        process = subprocess.Popen(argv, cwd=runtime, env=child_environment(), stdout=output,
                                   stderr=subprocess.STDOUT, start_new_session=True)
        try:
            row["exit_code"] = process.wait(timeout=timeout)
            row["status"] = "passed" if row["exit_code"] == 0 else "failed"
        except (subprocess.TimeoutExpired, KeyboardInterrupt) as exc:
            row["status"] = "timed_out" if isinstance(exc, subprocess.TimeoutExpired) else "interrupted"
            row["process_group_termination_attempted"] = True
            try:
                os.killpg(process.pid, signal.SIGTERM)
            except ProcessLookupError:
                pass
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                process.wait()
            row["exit_code"] = process.returncode
            row["detached_process_cleanup"] = "not_verified"
    row["elapsed_seconds"] = round(time.time() - started, 3)
    return row


def verify(runtime: Path, expected: str, evidence: Path, timeout: int) -> tuple[int, dict[str, Any]]:
    report: dict[str, Any] = {
        "schema": "ai-personas/existing-core-suite-run/1", "requested_revision": expected,
        "existing_suite_status": "not_run", "full_v1_2_acceptance": "not_evaluated",
        "mechanical_gate_verdicts": {}, "behavioral_gate_verdicts": {},
        "scope": "Existing fixture/build/barrier/behavior suites only. No live-provider campaign or full acceptance verdict.",
        "commands": [], "errors": [],
    }
    save_report(evidence, report)
    try:
        for tool in ("git", "python3", "cargo", "rustc"):
            if shutil.which(tool) is None:
                raise ValueError(f"missing required tool: {tool}")
        if git_text(runtime, "rev-parse", "--show-toplevel") != str(runtime):
            raise ValueError("--runtime must be the repository root")
        report["actual_revision"] = git_text(runtime, "rev-parse", "HEAD")
        if report["actual_revision"] != expected:
            raise ValueError("checkout revision differs from --expected-revision; no branch was changed")
        if git_text(runtime, "status", "--porcelain", "--untracked-files=all"):
            raise ValueError("runtime checkout must be clean; no user changes were discarded")
        for required in ("Cargo.toml", "Cargo.lock", "src/runtime.rs", "tests/completion_barrier.rs", "integtest/behavior.rs"):
            if not (runtime / required).is_file():
                raise ValueError(f"missing expected runtime file: {required}")
        for tool in ("cargo", "rustc", "python3"):
            result = subprocess.run([tool, "--version"], capture_output=True, text=True, check=True,
                                    timeout=30, env=child_environment())
            report.setdefault("toolchain", {})[tool] = result.stdout.strip()
        report["existing_suite_status"] = "running"
        save_report(evidence, report)
        for index, (name, argv) in enumerate(COMMANDS, 1):
            row = run_command(argv, runtime, evidence / f"{index:02d}-{name}.log", timeout)
            row["name"] = name
            report["commands"].append(row)
            save_report(evidence, report)
            if row["status"] != "passed":
                report["existing_suite_status"] = row["status"]
                break
        else:
            report["existing_suite_status"] = "passed"
        report["final_revision"] = git_text(runtime, "rev-parse", "HEAD")
        report["final_checkout_status"] = git_text(runtime, "status", "--porcelain", "--untracked-files=all")
        if report["final_revision"] != expected or report["final_checkout_status"]:
            report["errors"].append("checkout changed during verification; result is not for a stable clean revision")
            report["existing_suite_status"] = "failed"
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        report["errors"].append(str(exc))
        report["existing_suite_status"] = "failed"
    except KeyboardInterrupt:
        report["errors"].append("interrupted outside a running suite")
        report["existing_suite_status"] = "interrupted"
    finally:
        report["finished_unix"] = time.time()
        save_report(evidence, report)
    return (0 if report["existing_suite_status"] == "passed" else 1), report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime", type=Path, required=True)
    parser.add_argument("--expected-revision", required=True)
    parser.add_argument("--evidence-dir", type=Path)
    parser.add_argument("--command-timeout", type=int, default=1800)
    parser.add_argument("--trusted-test-host", action="store_true")
    args = parser.parse_args()
    if not args.trusted_test_host:
        parser.error("explicit --trusted-test-host required: these legacy process tests are not sandboxed")
    if sys.platform != "linux":
        parser.error("this process-suite runner requires Linux")
    if not re.fullmatch(r"[0-9a-f]{40}", args.expected_revision):
        parser.error("--expected-revision must be a full lowercase commit SHA")
    if args.command_timeout < 1:
        parser.error("--command-timeout must be positive")
    runtime = args.runtime.expanduser().resolve()
    if not runtime.is_dir():
        parser.error("runtime directory does not exist")
    try:
        evidence = private_evidence_directory(args.evidence_dir, runtime)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    code, report = verify(runtime, args.expected_revision, evidence, args.command_timeout)
    print(json.dumps({"existing_suite_status": report["existing_suite_status"],
                      "full_v1_2_acceptance": "not_evaluated", "private_report": str(evidence / "report.json")}, indent=2))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
