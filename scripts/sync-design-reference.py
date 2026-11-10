#!/usr/bin/env python3
"""Bundle the canonical visual guidance into every independently installable skill."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
source = (root / "docs/design-system.md").read_bytes()
for entry in sorted((root / "skills").glob("*/SKILL.md")):
    target = entry.parent / "references/design-system.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(source)
    print(f"Synced {target.relative_to(root)}")
