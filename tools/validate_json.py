#!/usr/bin/env python3
"""Validate JSON syntax and the integrity of the imported part-number indexes."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data_root = ROOT / "data"
errors: list[str] = []
json_files = sorted(data_root.rglob("*.json"))

def load(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
        return None

for path in json_files:
    obj = load(path)
    if obj is not None:
        print(f"JSON OK  {path.relative_to(ROOT)}")

def validate_index(relative_path: str) -> None:
    path = ROOT / relative_path
    obj = load(path)
    if obj is None:
        return
    records = obj.get("records")
    if not isinstance(records, list):
        errors.append(f"{relative_path}: records must be an array")
        return
    if obj.get("record_count") != len(records):
        errors.append(f"{relative_path}: record_count does not match records length")
    seen: set[str] = set()
    for index, record in enumerate(records):
        if not isinstance(record, dict) or not record.get("vendor") or not record.get("part_number"):
            errors.append(f"{relative_path}: record {index} is missing vendor or part_number")
            continue
        key = record["part_number"].strip().upper()
        if key in seen:
            errors.append(f"{relative_path}: duplicate part number {key}")
        seen.add(key)

def validate_hw_codes() -> None:
    relative_path = "data/mediatek/soc_hw_codes.json"
    obj = load(ROOT / relative_path)
    if obj is None:
        return
    records = obj.get("records")
    if not isinstance(records, list):
        errors.append(f"{relative_path}: records must be an array")
        return
    if obj.get("record_count") != len(records):
        errors.append(f"{relative_path}: record_count mismatch")
    seen: set[str] = set()
    for index, record in enumerate(records):
        code = record.get("hw_code", "").upper()
        if not code.startswith("0X"):
            errors.append(f"{relative_path}: record {index} has invalid HW code")
        if code in seen:
            errors.append(f"{relative_path}: duplicate HW code {code}")
        seen.add(code)
        decimal = record.get("hw_code_decimal")
        try:
            if int(code, 16) != decimal:
                errors.append(f"{relative_path}: decimal/hex mismatch for {code}")
        except ValueError:
            errors.append(f"{relative_path}: malformed HW code {code}")
        da_code = record.get("da_code")
        if da_code is not None and not str(da_code).startswith("0x"):
            errors.append(f"{relative_path}: invalid DA code for {code}")
        if record.get("da_code_conflict") and not record["da_code_conflict"].get("review_required"):
            errors.append(f"{relative_path}: DA code conflict not flagged for {code}")

validate_hw_codes()

def validate_bbchip_ids() -> None:
    relative_path = "data/mediatek/bbchip_type_ids.json"
    obj = load(ROOT / relative_path)
    if obj is None:
        return
    records = obj.get("records", [])
    if obj.get("record_count") != len(records):
        errors.append(f"{relative_path}: record_count mismatch")
    seen_symbols: set[str] = set()
    for index, record in enumerate(records):
        symbol = record.get("symbol")
        value = record.get("value")
        if not symbol or not isinstance(value, int):
            errors.append(f"{relative_path}: record {index} missing symbol or integer value")
            continue
        if symbol in seen_symbols:
            errors.append(f"{relative_path}: duplicate symbol {symbol}")
        seen_symbols.add(symbol)
        if record.get("alias_of") and record.get("value") is None:
            errors.append(f"{relative_path}: unresolved alias {symbol}")

validate_bbchip_ids()

validate_index("data/dram/part_numbers.json")
validate_index("data/storage/managed_nand_part_numbers.json")

verified_path = ROOT / "data/storage/verified_products.json"
verified = load(verified_path)
if isinstance(verified, dict):
    records = verified.get("records", [])
    if verified.get("record_count") != len(records):
        errors.append("data/storage/verified_products.json: record_count mismatch")
    for index, record in enumerate(records):
        if not record.get("vendor") or not record.get("part_number") or not record.get("technology"):
            errors.append(f"data/storage/verified_products.json: record {index} missing identity fields")
        capacity = record.get("capacity")
        if capacity is not None and (not isinstance(capacity, (int, float)) or capacity <= 0):
            errors.append(f"data/storage/verified_products.json: record {index} has invalid capacity")

if errors:
    print("\n".join("ERROR " + error for error in errors))
    raise SystemExit(1)

print(f"Validated {len(json_files)} JSON files; part-number indexes and verified product records are consistent.")
