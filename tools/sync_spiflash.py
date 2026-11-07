#!/usr/bin/env python3
"""Import upstream-generated SPI flash JSON while preserving source provenance."""
from __future__ import annotations
import hashlib, json, urllib.request
from pathlib import Path

UPSTREAM_COMMIT = "bd21b65e79e4d1fdc2d0bd1d22a9b8018715178e"
BASE = f"https://raw.githubusercontent.com/mithro/spiflash/{UPSTREAM_COMMIT}/src/spiflash/data"
DEST = Path(__file__).resolve().parents[1] / "data" / "flash" / "spi"
FILES = ("records.json", "manufacturers.json", "sources.json")

def main() -> None:
    DEST.mkdir(parents=True, exist_ok=True)
    manifest = {"upstream": "mithro/spiflash", "commit": UPSTREAM_COMMIT, "files": {}}
    for name in FILES:
        req = urllib.request.Request(f"{BASE}/{name}", headers={"User-Agent": "Mtk-Knowledge-Base"})
        with urllib.request.urlopen(req, timeout=90) as response:
            raw = response.read()
        obj = json.loads(raw)
        if not isinstance(obj, dict) or "format" not in obj:
            raise ValueError(f"Unexpected upstream JSON structure: {name}")
        (DEST / name).write_bytes(raw)
        manifest["files"][name] = {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "format": obj["format"]}
        print(f"{name}: {len(raw):,} bytes")
    (DEST / "download_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print("Import completed; review upstream licenses in sources/SOURCES.md.")

if __name__ == "__main__":
    main()
