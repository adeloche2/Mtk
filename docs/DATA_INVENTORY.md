# Data inventory and coverage

Counts are tied to upstream snapshots, not an assertion of all commercially manufactured parts.

## SPI NOR and SPI NAND

Upstream: [mithro/spiflash](https://github.com/mithro/spiflash). Its inspected documentation reports **1,347 distinct IDs**: **1,056 SPI NOR**, **291 SPI NAND**, across **64 manufacturers**. It retains multiple upstream claims per ID and records source disagreements rather than silently choosing one. The upstream file `records.json` is approximately 6.1 MB and is downloaded with `tools/sync_spiflash.py`; this initial commit does not fabricate or truncate it.

## JEP106 manufacturers

`data/flash/jep106/manufacturers.json` contains 2306 manufacturer records. It is a manufacturer-ID dictionary, not a flash-part list.

## Raw NAND

`data/flash/raw_nand/nand_ids.json` contains 13 explicitly named full-ID records parsed from the Linux table. The original C table is also preserved. Legacy macro-based entries are not expanded in this JSON yet; therefore this is a documented subset, not a complete normalized Linux NAND dictionary.

## MediaTek DRAM / EMI

The MTKPreloaderParser README advertises these BLoader versions: v08, v10, v11, v12, v13, v14, v15, v16, v17, v20, v21, v22, v24, v25, v27, v28, v30, v31, v32, v35, v36, v38, v39, v40, v45, v46, v47, v49, v51, v52, v54.

The inspected `emi_structures.h` declares version-specific structures for: v08, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v27, v28, v30, v31, v32, v35, v36, v38, v39, v46, v49, v51.

The README list and header declarations differ. Both are stored separately in `data/dram/memory_catalog.json`. The inspected EMI schema explicitly contains LPDDR1, LPDDR2, LPDDR3 and PC DDR3 register layouts in its v12 DDR union. This is not a global part-number catalogue and does not prove absence of other DRAM generations.

## eMMC and UFS

Penumbra provides storage-type enums and device-reported eMMC/UFS structures. These are useful protocol metadata, not a complete manufacturer part-number database. A unified eMMC/UFS vendor catalogue remains pending.

## Data interpretation

- Manufacturer ID alone does not uniquely identify a part.
- A JEDEC ID can map to several commercial variants.
- DRAM generation is not a timing profile.
- EMI configuration is platform/board-specific; never transplant timings based only on a similar chip name.
- Preserve source, revision, raw identifier, units, and whether a value is observed, reported, or inferred.
