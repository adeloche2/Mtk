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
