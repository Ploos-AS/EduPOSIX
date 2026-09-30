#!/usr/bin/env python3
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

required = [
    "README.md",
    "CONTRIBUTING.md",
    "docs/ROADMAP.md",
    "docs/PUBLISHING.md",
    "docs/TEACHING-STANDARD.md",
    "docs/DEFINITION-OF-DONE.md",
    "course/SYLLABUS.md",
    "student-oci.json",
    "student-oci/student-env-info",
    "student-oci/student-check",
]

errors = []
for rel in required:
    p = ROOT / rel
    if not p.is_file():
        errors.append(f"missing required file: {rel}")
    elif not p.read_text(encoding="utf-8").strip():
        errors.append(f"empty required file: {rel}")


# PLOOS-STUDENT-OCI-1 machine-readable contract.
manifest_path = ROOT / "student-oci.json"
if manifest_path.is_file():
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        errors.append(f"invalid student-oci.json: {exc}")
    else:
        expected = {
            "schema": 1,
            "contract": "PLOOS-STUDENT-OCI-1",
            "course": "EduPOSIX",
            "workspace": "/course",
            "image": "ghcr.io/ploos-as/eduposix-student",
        }
        for key, value in expected.items():
            if manifest.get(key) != value:
                errors.append(f"student-oci.json: {key} must be {value!r}")
        commands = manifest.get("commands", {})
        if commands.get("info") != "student-env-info":
            errors.append("student-oci.json: commands.info must be 'student-env-info'")
        if commands.get("check") != "student-check":
            errors.append("student-oci.json: commands.check must be 'student-check'")
        if manifest.get("requires_private_infrastructure") is not False:
            errors.append("student-oci.json: private infrastructure must not be required")
        if manifest.get("restricted_payloads") is not False:
            errors.append("student-oci.json: restricted payloads must be false")

course_files = sorted((ROOT / "course").glob("[0-9][0-9]-*.md"))
if not course_files:
    errors.append("no numbered course chapter found")

for p in course_files:
    text = p.read_text(encoding="utf-8").lower()
    for heading in ("learning objectives", "checkpoint"):
        if heading not in text:
            errors.append(f"{p.relative_to(ROOT)}: missing {heading!r}")

for forbidden in ("kickstart.rom", "amigaos.rom", "workbench.adf"):
    if any(p.name.lower() == forbidden for p in ROOT.rglob("*") if p.is_file()):
        errors.append(f"forbidden redistributable-sensitive file name present: {forbidden}")

if errors:
    print("course validation: FAIL")
    for e in errors:
        print(f" - {e}")
    sys.exit(1)

print(f"course validation: PASS ({len(course_files)} chapter seed(s))")
