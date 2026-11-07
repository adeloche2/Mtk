# SPI NOR and SPI NAND

Canonical upstream: [mithro/spiflash](https://github.com/mithro/spiflash).

The upstream project documents 1,056 SPI NOR IDs and 291 SPI NAND IDs (1,347 distinct IDs total), sourced from Linux, U-Boot, flashrom, flashprog, Dediprog, Rockchip, MediaTek, OpenOCD, QEMU, Zephyr, IMSProg and others.

Run `python tools/sync_spiflash.py` to import the generated `records.json`, `manufacturers.json`, and `sources.json`. The upstream records are generated and should not be hand-edited. SPI NAND does not necessarily provide the same opcode/SFDP metadata as SPI NOR.

The importer pins spiflash commit `bd21b65e79e4d1fdc2d0bd1d22a9b8018715178e`.
