#!/usr/bin/env python3
"""Validate release packaging, isolated references, and recommended contrast pairs.

Dependency-free. Frontmatter uses the collection's deliberately flat YAML subset;
this does not pretend to be a general YAML parser or a behavioral skill evaluation.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "expressive-mobile-design": None,
    "expressive-flutter": "flutter.md",
    "expressive-react-native": "react-native.md",
    "expressive-compose": "compose.md",
    "expressive-swiftui": "swiftui.md",
}
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def contrast(foreground, background):
    def luminance(value):
        rgb = [int(value[i:i + 2], 16) / 255 for i in (0, 2, 4)]
        linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb]
        return sum(c * w for c, w in zip(linear, (0.2126, 0.7152, 0.0722)))

    dark, light = sorted((luminance(foreground), luminance(background)))
    return (light + 0.05) / (dark + 0.05)


canonical = (ROOT / "docs/design-system.md").read_bytes()
actual = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
check(actual == set(EXPECTED), f"Unexpected skill set: {sorted(actual)}")

allowed = {
    ".gitignore", "LICENSE", "README.md", ".github/workflows/validate.yml",
    "docs/design-system.md", "docs/reference-analysis.md",
    "scripts/sync-design-reference.py", "scripts/validate.py", "scripts/publish.sh",
}
for name, framework in EXPECTED.items():
    allowed.update({f"skills/{name}/SKILL.md", f"skills/{name}/references/design-system.md"})
    if framework:
        allowed.add(f"skills/{name}/references/{framework}")

for path in ROOT.rglob("*"):
    relative = path.relative_to(ROOT)
    if any(part in {".git", "__pycache__"} for part in relative.parts):
        continue
    check(not path.is_symlink(), f"Symlink in public tree: {relative}")
    if path.is_file():
        check(relative.as_posix() in allowed, f"Unreviewed public file: {relative}")

for name, framework in EXPECTED.items():
    folder = ROOT / "skills" / name
    entry = folder / "SKILL.md"
    if not entry.is_file():
        check(False, f"Missing {name}/SKILL.md")
        continue
    text = entry.read_text()
    check(len(text.splitlines()) < 100, f"Entrypoint too long: {name}")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    check(match is not None, f"Missing frontmatter: {name}")
    if match:
        fields = {}
        for line in match[1].splitlines():
            pair = re.fullmatch(r"([a-z-]+): (.+)", line)
            check(pair is not None, f"Use a flat frontmatter field: {name}: {line}")
            if pair:
                key, value = pair.groups()
                check(key not in fields, f"Duplicate frontmatter key: {name}: {key}")
                fields[key] = value
        check(set(fields) == {"name", "description", "license"}, f"Unexpected metadata: {name}")
        check(fields.get("name") == name, f"Folder/name mismatch: {name}")
        description = fields.get("description", "")
        check(0 < len(description) <= 1024, f"Invalid description length: {name}")
        check("Use when" in description or "Use for" in description, f"Missing trigger: {name}")
    copy = folder / "references/design-system.md"
    check(copy.is_file() and copy.read_bytes() == canonical, f"Unsynced design reference: {name}")
    if framework:
        check((folder / "references" / framework).is_file(), f"Missing framework guide: {name}")

    for document in folder.rglob("*.md"):
        content = document.read_text()
        check(not re.search(r"/Users/|\[TODO:|BEGIN .*PRIVATE KEY|gh[pousr]_[A-Za-z0-9]{20,}", content),
              f"Private path, placeholder, or credential pattern: {document.relative_to(ROOT)}")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", content):
            if target.startswith(("https://", "http://", "#")):
                continue
            destination = (document.parent / target.split("#", 1)[0]).resolve()
            check(destination.is_relative_to(folder.resolve()), f"Skill depends on sibling files: {name}: {target}")
            check(destination.is_file(), f"Broken reference: {name}: {target}")

pairs = [
    ("F6F1EA", "1E1A16"), ("F6F1EA", "2A251F"), ("F6F1EA", "352F28"),
    ("9A9186", "2A251F"), ("1B1712", "F2ECE3"), ("1B1712", "E9E2D7"),
    ("62594F", "E9E2D7"), ("62594F", "DFD7CB"), ("14110E", "CCFF00"),
    ("CCFF00", "1B1712"),
]
pairs.extend(("14110E", color) for color in ("1B88F8", "F1228D", "E28E26", "D79BFB", "32E2DE"))
for foreground, background in pairs:
    ratio = contrast(foreground, background)
    check(ratio >= 4.5, f"Normal text contrast fails: #{foreground} / #{background}: {ratio:.2f}:1")

for relative in allowed:
    check((ROOT / relative).is_file(), f"Missing release file: {relative}")

if errors:
    print("\n".join(f"FAIL: {message}" for message in errors), file=sys.stderr)
    sys.exit(1)
print(f"Valid: {len(EXPECTED)} skills, isolated references, {len(allowed)} reviewed files, {len(pairs)} contrast pairs.")
print("This validates packaging and recommended contrast, not app builds or device behavior.")
