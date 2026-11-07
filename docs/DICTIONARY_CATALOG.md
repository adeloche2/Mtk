# Dictionary catalogue

This page lists the structured dictionaries currently committed.

| Area | File | Coverage / caveat |
|---|---|---|
| SoC identity | `data/mediatek/soc_hw_codes.json` | HW-code mappings collected from acon; DA code is separate and only populated where explicitly established. |
| SPI NOR / SPI NAND | `data/flash/spi/` | Upstream importer and dataset description committed; full generated records are fetched with the sync script. |
| JEP106 | `data/flash/jep106/manufacturers.json` | 2,306 bank/ID manufacturer records. |
| Raw NAND | `data/flash/raw_nand/nand_ids.json` | Explicit named full-ID subset plus original Linux C table; legacy macro expansion remains pending. |
| DRAM / EMI | `data/dram/memory_catalog.json` | BLoader schema versions and DRAM layout families observed in MTKPreloaderParser; not a universal part database. |
| Storage types | `data/storage/storage_types.json` | Penumbra storage type enum. |
| eMMC regions | `data/storage/emmc_partition_ids.json` | eMMC partition/region identifiers. |
| UFS LUNs | `data/storage/ufs_lun_ids.json` | LUN identifiers; semantics are device-dependent. |
| Preloader commands | `data/protocol/preloader_commands.json` | Command byte names from Penumbra. |
| XFlash commands | `data/protocol/xflash_commands.json` | Command IDs and little-endian wire bytes. |
| GFH types | `data/protocol/gfh_types.json` | GFH record type identifiers from HACC definitions. |
| Preloader errors | `data/protocol/preloader_errors.json` | Known mapped status codes; not exhaustive. |
| XFlash error format | `data/protocol/xflash_error_format.json` | Severity/domain bit layout, not a complete code catalogue. |
| USB IDs | `data/protocol/usb_ids.json` | Known MediaTek VID/PID modes from Penumbra. |

## Still requiring dedicated research

1. Complete eMMC manufacturer/product catalogue based on CID fields and vendor part numbers.
2. UFS manufacturer/product catalogue based on descriptors and JEDEC identifiers.
3. LPDDR4/4X/5/5X vendor IDs, Mode Register decoding, density and package identification.
4. Full DRAM timing/EMI corpus with exact SoC + Preloader + memory-ID provenance.
5. Complete Raw NAND parser including legacy macro expansion and additional vendor sources.
6. Exhaustive XFlash error-code tables across DA versions.
7. Full GFH field schemas and version compatibility, beyond the type IDs.

| DRAM part-number index | `data/dram/part_numbers.json` | 3,169 part numbers, 13 vendors; capacity deliberately null until verified. |
| LPDDR MR5 manufacturer IDs | `data/dram/lpddr_mr5_manufacturer_ids.json` | Separate LPDDR2/3, LPDDR4 and LPDDR5 ID tables. |
| Managed flash PN index | `data/storage/managed_nand_part_numbers.json` | 891 part numbers across 13 vendors; includes mixed eMMC/UFS/MCP categories not yet individually classified. |
| eMMC CID manufacturers | `data/storage/emmc_cid_manufacturers.json` | CID MID map with source-quality labels. |
| Verified product subset | `data/storage/verified_products.json` | 79 sourced examples: 21 DRAM/LPDDR, 22 eMMC and 36 UFS; unresolved fields remain null. |
| Raw NAND verified PN | `data/flash/raw_nand/verified_part_numbers.json` | 24 raw NAND commercial part numbers with capacity and ID evidence where available. |

| LPDDR mode registers | `data/dram/lpddr_mode_registers.json` | MR5 vendor, MR6/MR7 revision, MR8 density/width (LPDDR4), MR47-MR54 serial ID (LPDDR5), with generation caveats. |
| Coreboot DRAM type enum | `data/dram/coreboot_memory_type_codes.json` | Coreboot-specific codes for DDR3/4/5 and LPDDR3/4/4X/5/5X; not universal JEDEC codes. |
| DRAM vendor decoding index | `data/dram/vendor_reference_index.json` | 13 vendor-specific decoding guides. |
| Managed-storage vendor index | `data/storage/vendor_reference_index.json` | 12 vendor-specific eMMC/UFS reference documents. |
| Raw NAND vendor index | `data/flash/raw_nand/vendor_reference_index.json` | 10 vendor-specific raw NAND reference documents. |

| UFS manufacturer IDs | `data/storage/ufs_manufacturer_ids.json` | UFS-specific 16-bit values observed in a Preloader parser; source subset, not complete JEDEC allocation. |
| Raw NAND manufacturer IDs | `data/flash/raw_nand/manufacturer_ids.json` | Common first-byte manufacturer mappings, not unique part identifiers. |
