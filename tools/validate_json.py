#!/usr/bin/env python3
"""Validate every JSON file below data/."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
paths=sorted((root/"data").rglob("*.json"))
for p in paths:
    json.loads(p.read_text(encoding="utf-8"))
    print("OK", p.relative_to(root))
print(f"Validated {len(paths)} JSON files.")
