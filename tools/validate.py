#!/usr/bin/env python3
from pathlib import Path
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
]

errors = []
for rel in required:
    p = ROOT / rel
    if not p.is_file():
        errors.append(f"missing required file: {rel}")
    elif not p.read_text(encoding="utf-8").strip():
        errors.append(f"empty required file: {rel}")

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
