# Upstream sources and licensing

| Dataset | Upstream | Purpose | License / handling |
|---|---|---|---|
| SPI NOR / SPI NAND | https://github.com/mithro/spiflash | Aggregated IDs, part names, geometry, capabilities, conflicts and provenance | Upstream project Apache-2.0; generated records incorporate source datasets under their respective licenses. Preserve its source manifest. |
| JEP106 manufacturer IDs | https://github.com/openocd-org/openocd | Manufacturer bank/ID/name table | GPL-2.0-or-later source lineage; attribution and applicable terms must be retained. |
| Raw NAND | https://github.com/torvalds/linux/blob/master/drivers/mtd/nand/raw/nand_ids.c | Raw NAND IDs and geometry | GPL-2.0-only (SPDX identifier in source). |
| MediaTek BLoader/EMI schemas | https://github.com/mfdl/MTKPreloaderParser | BLoader version inventory and DRAM register-layout evidence | Upstream repository GPL-3.0; this repository stores extracted factual metadata and links, not its parser implementation. |
| BLoader extractor | https://github.com/iscle/mtk_bloader_info_extractor | Independent extraction approach for EMI/timing data | Referenced only; verify license before copying code or sample output. |
| Penumbra | https://github.com/shomykohai/penumbra | MediaTek protocol, SoC, storage and error metadata | Consult the upstream AGPL-3.0-or-later license before copying source code. |

## Reproducibility

The SPI flash sync utility downloads the generated JSON dictionaries from mithro/spiflash. Its `sources.json` records the exact upstream commits used to generate the imported source records. Record the sync date and SHA-256 hashes after each import.

Do not combine records from different upstream snapshots without preserving per-record provenance.

| DRAM / eMMC / UFS part-number indexes | https://github.com/iTXTech/fdnext | Part-number presence indexes (3,169 DRAM; 891 managed NAND/MCP) and vendor-specific decoding reference documents | AGPL-3.0-or-later. Exact source commit pinned in `sources/PART_NUMBER_DATASETS.md`; license text is stored in `LICENSES/AGPL-3.0-or-later.txt`. |
| LPDDR MR5 / JEP166 | https://store.accuristech.com/standards/jedec-jep166e?product_id=2569215 and https://blog.armsom.org/articles/037-rockchip-ddr/ | Generation-specific low-power DRAM manufacturer identifiers | JEDEC JEP166E is normative; public secondary table is used as a cross-reference and may be incomplete. |
| eMMC CID MID | https://github.com/CTCaer/hekate/blob/45cd81ed08e30a26ba380958c7e20b55c342834b/nyx/nyx_gui/frontend/gui_info.c | eMMC CID manufacturer field and known mappings | Hekate GPL-2.0; unofficial IDs remain labelled. Micron CID datasheet independently confirms MID 0x13. |
| Coreboot DRAM topology | https://github.com/coreboot/coreboot/blob/99ba9d7525c8a18d6b46cf4370467cf249039d47/src/commonlib/bsd/include/commonlib/bsd/mem_chip_info.h | MR5/MR6/MR7/MR8 and LPDDR5 serial-register field model | BSD-3-Clause (SPDX in source); facts/schema meanings are attributed. |

| MediaTek SoC HW-code and DA-code mapping | https://github.com/shomykohai/acon/tree/e1965e02f4a8e54d9fad3799da67fc7a2459d389 | Explicit SoC enum, HW code, silicon aliases, marketing family, and DA-code crosswalk | Source commit pinned in `data/mediatek/soc_hw_codes.json`; AGPL project source. |
| MediaTek platform hwconfig | https://github.com/bkerler/mtkclient/blob/118a000a83ea31c4f427fe5225abfe964546e05e/mtkclient/config/brom_config.py | 89 configured HW-code keys, names, DA codes/modes, including older modem/IoT and tablet platforms | GPL-3.0 project source; facts attributed and commit pinned. |

| Legacy MediaTek BBCHIP_TYPE names | https://github.com/cuu/SP-Flash-Tool-src/blob/master/BootRom/mtk_mcu.h | Historical SP Flash Tool chip-name enum and tool-specific numeric IDs | The source file carries a MediaTek copyright/confidentiality notice; only factual names/values are recorded with attribution, not implementation code. Never interpret these values as raw HW Codes. |
