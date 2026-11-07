# MTK Knowledge Base

A source-attributed knowledge base for MediaTek device identification, memory technologies, bootloader metadata, and storage components.

## Scope

This repository separates **observed identifiers**, **vendor part-number references**, **protocol constants**, and **derived interpretations**. It is intended for device diagnostics, firmware analysis, and research. It does not provide security bypasses or undocumented authentication circumvention.

## Repository layout

- `data/flash/` — SPI NOR, SPI NAND, raw NAND, and manufacturer identifiers.
- `data/dram/` — DRAM families and MediaTek BLoader/EMI schema inventory.
- `data/storage/` — eMMC/UFS storage type and partition metadata.
- `data/mediatek/` — SoC, HW-code and DA-code dictionaries.
- `data/protocol/` — USB identifiers, protocol commands, and status/error dictionaries.
- `sources/` — source inventory, versions, licensing and provenance.
- `docs/` — data model, coverage notes, and contribution guidance.
- `tools/` — reproducible import and validation utilities.

## Data quality rules

Every imported record should preserve, where available:

1. Original source and exact upstream revision.
2. Original identifier bytes/integers without lossy normalization.
3. Vendor and part number as reported by the source.
4. Units for capacities, timings, voltages and geometry.
5. Whether a field is directly observed, source-reported, or derived.
6. Conflicts between sources instead of silently discarding them.

A missing entry does not mean a component is unsupported. A match by a short identifier may be ambiguous; prefer the longest available ID and confirm against a datasheet or device-reported information.

## Current inventory

The curated product subset currently contains 79 sourced examples (21 DRAM/LPDDR, 22 eMMC, 36 UFS), in addition to the broader part-number indexes and 24 raw NAND part-number examples. Unknown capacities and interfaces are left unset rather than inferred.

The current repository includes source-attributed DRAM and managed-flash part-number indexes, LPDDR MR5 manufacturer IDs, eMMC CID manufacturer IDs, and a separately curated verified-product subset. See [docs/DICTIONARY_CATALOG.md](docs/DICTIONARY_CATALOG.md) and [sources/PART_NUMBER_DATASETS.md](sources/PART_NUMBER_DATASETS.md).

See [docs/DATA_INVENTORY.md](docs/DATA_INVENTORY.md) for the verified source inventory and coverage limitations.

## Licensing

This repository does not assume that all upstream data shares one license. Each dataset has its own provenance and license notes in [sources/SOURCES.md](sources/SOURCES.md). Do not redistribute imported source datasets unless their individual license permits it. The import tools may download upstream datasets at runtime.

## Status

The initial knowledge-base structure and source inventory are being established. Coverage is intentionally labelled as partial until datasets have been imported, normalized, counted, and validated.
