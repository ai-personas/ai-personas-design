"""Planning/runner helper tests only; these do not execute the Rust runtime."""
from __future__ import annotations

import copy
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


core = load_module("check_core")
runner = load_module("verify_rust_core")


class CorePlanTests(unittest.TestCase):
    def setUp(self):
        self.plan = core.load_plan(ROOT / "technical/core-gates.json")

    def test_checked_in_plan_is_consistent_not_runtime_evidence(self):
        self.assertEqual([], core.validate(self.plan))
        self.assertEqual(25, len(self.plan["mechanical_gates"]))
        self.assertEqual(12, len(self.plan["behavioral_gates"]))

    def test_masquerading_as_generated_api_is_rejected(self):
        self.plan["not_backend_schema"] = False
        self.assertTrue(core.validate(self.plan))

    def test_unimplemented_wire_version_is_not_advertised(self):
        self.plan["baseline"]["runtime_contract"] = "ai-personas/2"
        self.assertTrue(core.validate(self.plan))

    def test_abbreviated_commit_is_rejected(self):
        self.plan["baseline"]["runtime_commit"] = "c2b7d89"
        self.assertTrue(core.validate(self.plan))

    def test_dropped_invariant_is_rejected(self):
        self.plan["invariants"].remove("I20")
        self.assertTrue(core.validate(self.plan))

    def test_missing_pending_effect_gate_is_rejected(self):
        self.plan["mechanical_gates"] = [g for g in self.plan["mechanical_gates"] if g["id"] != "M17"]
        self.assertTrue(core.validate(self.plan))

    def test_duplicate_gate_is_rejected(self):
        self.plan["mechanical_gates"][1] = copy.deepcopy(self.plan["mechanical_gates"][0])
        self.assertTrue(core.validate(self.plan))

    def test_unverified_gate_cannot_be_promoted_by_documentation(self):
        self.plan["behavioral_gates"][0]["verification"] = "passed"
        self.assertTrue(core.validate(self.plan))

    def test_ui_requirement_cannot_disappear(self):
        self.plan["deferred_gates"] = []
        self.assertTrue(core.validate(self.plan))

    def test_ui_requirement_cannot_be_claimed_by_core_stream(self):
        self.plan["workstreams"][0]["gates"].append("M14")
        self.assertTrue(core.validate(self.plan))

    def test_cycle_is_rejected(self):
        self.plan["workstreams"][0]["requires"] = ["K7"]
        self.assertTrue(core.validate(self.plan))

    def test_unknown_dependency_is_rejected(self):
        self.plan["workstreams"][0]["requires"] = ["missing"]
        self.assertTrue(core.validate(self.plan))

    def test_unmapped_gate_is_rejected(self):
        for stream in self.plan["workstreams"]:
            stream["gates"] = [gate for gate in stream["gates"] if gate != "M23"]
        self.assertTrue(core.validate(self.plan))

    def test_private_publication_guard_is_required(self):
        self.plan["safety"]["private_runtime_source_must_not_be_published"] = False
        self.assertTrue(core.validate(self.plan))

    def test_live_prerequisites_cannot_be_dropped(self):
        self.plan["safety"]["live_tool_campaign_requires"] = ["K1"]
        self.assertTrue(core.validate(self.plan))

    def test_path_traversal_is_rejected(self):
        self.plan["workstreams"][0]["runtime_paths"] = ["src/../../outside.rs"]
        self.assertTrue(core.validate(self.plan))

    def test_malformed_row_is_reported(self):
        self.plan["mechanical_gates"][0] = "not an object"
        self.assertTrue(core.validate(self.plan))

    def test_duplicate_json_keys_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "plan.json"
            source.write_text('{"scope": {}, "scope": {"ui_changes": true}}')
            with self.assertRaises(ValueError):
                core.load_plan(source)


class RunnerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.runtime = self.base / "runtime"
        self.runtime.mkdir()
        self.evidence = self.base / "evidence"
        self.evidence.mkdir(mode=0o700)
        self.revision = "a" * 40
        for name in ("Cargo.toml", "Cargo.lock", "src/runtime.rs", "tests/completion_barrier.rs", "integtest/behavior.rs"):
            target = self.runtime / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("helper fixture only\n")

    def fake_git(self, path, *args):
        if args == ("rev-parse", "--show-toplevel"):
            return str(self.runtime)
        if args == ("rev-parse", "HEAD"):
            return self.revision
        if args == ("status", "--porcelain", "--untracked-files=all"):
            return ""
        raise AssertionError(args)

    def call_verify(self, run_status="passed", git=None):
        version = subprocess.CompletedProcess([], 0, stdout="helper test tool version\n", stderr="")
        with patch.object(runner.shutil, "which", return_value="/fixture/tool"), \
             patch.object(runner, "git_text", side_effect=git or self.fake_git), \
             patch.object(runner.subprocess, "run", return_value=version), \
             patch.object(runner, "run_command", return_value={"status": run_status, "exit_code": 0 if run_status == "passed" else 1}) as command:
            code, report = runner.verify(self.runtime, self.revision, self.evidence, 1)
        return code, report, command.call_count

    def test_success_is_only_existing_suite_success(self):
        code, report, calls = self.call_verify()
        self.assertEqual(0, code)
        self.assertEqual(len(runner.COMMANDS), calls)
        self.assertEqual("passed", report["existing_suite_status"])
        self.assertEqual("not_evaluated", report["full_v1_2_acceptance"])
        self.assertEqual({}, report["mechanical_gate_verdicts"])
        self.assertEqual({}, report["behavioral_gate_verdicts"])

    def test_first_failure_stops_suite(self):
        code, report, calls = self.call_verify("failed")
        self.assertEqual(1, code)
        self.assertEqual(1, calls)
        self.assertEqual("failed", report["existing_suite_status"])
        self.assertEqual("not_evaluated", report["full_v1_2_acceptance"])

    def test_timeout_stops_suite(self):
        code, report, calls = self.call_verify("timed_out")
        self.assertEqual(1, code)
        self.assertEqual(1, calls)
        self.assertEqual("timed_out", report["existing_suite_status"])

    def test_missing_tool_retains_failed_report(self):
        with patch.object(runner.shutil, "which", return_value=None):
            code, report = runner.verify(self.runtime, self.revision, self.evidence, 1)
        self.assertEqual(1, code)
        self.assertEqual([], report["commands"])
        self.assertIn("missing required tool", report["errors"][0])
        self.assertEqual("failed", json.loads((self.evidence / "report.json").read_text())["existing_suite_status"])

    def test_wrong_revision_runs_no_suite(self):
        def wrong(path, *args):
            return "b" * 40 if args == ("rev-parse", "HEAD") else self.fake_git(path, *args)
        code, report, calls = self.call_verify(git=wrong)
        self.assertEqual(1, code)
        self.assertEqual(0, calls)
        self.assertIn("revision differs", report["errors"][0])

    def test_dirty_checkout_runs_no_suite(self):
        def dirty(path, *args):
            return " M Cargo.toml" if args[0] == "status" else self.fake_git(path, *args)
        code, report, calls = self.call_verify(git=dirty)
        self.assertEqual(1, code)
        self.assertEqual(0, calls)
        self.assertIn("must be clean", report["errors"][0])

    def test_mutation_during_verification_invalidates_success(self):
        status_calls = 0
        def changed(path, *args):
            nonlocal status_calls
            if args[0] == "status":
                status_calls += 1
                return "" if status_calls == 1 else " M src/runtime.rs"
            return self.fake_git(path, *args)
        code, report, _ = self.call_verify(git=changed)
        self.assertEqual(1, code)
        self.assertEqual("failed", report["existing_suite_status"])
        self.assertIn("checkout changed", report["errors"][0])

    def test_existing_evidence_is_not_overwritten(self):
        with self.assertRaises(FileExistsError):
            runner.private_evidence_directory(self.evidence, self.runtime)

    def test_evidence_cannot_be_inside_runtime(self):
        with self.assertRaises(ValueError):
            runner.private_evidence_directory(self.runtime / "logs", self.runtime)
        self.assertFalse((self.runtime / "logs").exists())

    def test_evidence_cannot_be_inside_public_design(self):
        with patch.object(runner, "DESIGN_ROOT", self.base):
            with self.assertRaises(ValueError):
                runner.private_evidence_directory(self.base / "public-logs", self.runtime)

    def test_evidence_is_private_and_report_atomic(self):
        path = runner.private_evidence_directory(self.base / "new-evidence", self.runtime)
        runner.save_report(path, {"test": "helper only"})
        self.assertEqual(0o700, path.stat().st_mode & 0o777)
        self.assertEqual(0o600, (path / "report.json").stat().st_mode & 0o777)
        self.assertFalse((path / "report.json.tmp").exists())

    def test_provider_tokens_are_not_explicitly_carried(self):
        with patch.dict(os.environ, {"OPENAI_API_KEY": "helper-fake-token", "GH_TOKEN": "helper-fake-token", "PATH": "/bin"}):
            env = runner.child_environment()
        self.assertNotIn("OPENAI_API_KEY", env)
        self.assertNotIn("GH_TOKEN", env)
        self.assertEqual("/bin", env["PATH"])

    def test_real_helper_child_exit_is_recorded(self):
        row = runner.run_command((sys.executable, "-c", "print('helper test, not Rust')"), self.runtime, self.evidence / "child.log", 5)
        self.assertEqual("passed", row["status"])
        self.assertEqual(0, row["exit_code"])
        self.assertIn("helper test", (self.evidence / "child.log").read_text())

    @unittest.skipUnless(sys.platform == "linux", "Linux process-group helper")
    def test_real_helper_timeout_is_recorded(self):
        row = runner.run_command((sys.executable, "-c", "import time; time.sleep(30)"), self.runtime, self.evidence / "timeout.log", 1)
        self.assertEqual("timed_out", row["status"])
        self.assertTrue(row["process_group_termination_attempted"])
        self.assertEqual("not_verified", row["detached_process_cleanup"])


if __name__ == "__main__":
    unittest.main()
