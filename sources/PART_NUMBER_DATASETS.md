# Part-number datasets and licensing

The two raw part-number lists in this directory are imported from the public resource files in [iTXTech/fdnext](https://github.com/iTXTech/fdnext), pinned to commit `15e2dcc75aa5efd80223f2889e210e889c9fa196`.

- `data/dram/part_numbers.json`: 3,169 DRAM part-number records.
- `data/storage/managed_nand_part_numbers.json`: 891 managed NAND / eMMC / UFS / MCP part-number records.

The upstream project is licensed under **GNU Affero General Public License v3 or later (AGPL-3.0-or-later)**. The imported lists are redistributed with the upstream license text in `LICENSES/AGPL-3.0-or-later.txt`, and the source commit is recorded here. These lists are part-number presence indexes; they do not independently prove capacity, interface, die count, package, or lifecycle status.

Vendor distribution in the pinned snapshot:

## DRAM
- winbond: 799
- nanya: 492
- issi: 409
- samsung: 343
- etron: 314
- skhynix: 298
- esmt: 267
- micron: 95
- cxmt: 62
- gigadevice: 54
- biwin: 23
- elpida: 7
- longsys: 6

## Managed NAND / eMMC / UFS / MCP
- sndk: 199
- samsung: 134
- skhynix: 132
- micron: 75
- biwin: 67
- siliconmotion: 64
- longsys: 60
- kioxia: 59
- kingston: 35
- ymtc: 35
- issi: 25
- esmt: 4
- spectek: 2

Vendor-specific public references and encoding guides are indexed in [fdnext PN documentation](https://github.com/iTXTech/fdnext/tree/15e2dcc75aa5efd80223f2889e210e889c9fa196/docs/pn_code). The source material is multilingual and includes vendor datasheet citations. The knowledge base will only populate decoded technical fields when supported by a primary datasheet, official product catalogue, or clearly identified corroborating source.

## Important field policy

- `capacity` is null in the bulk indexes until independently decoded and verified.
- The verified sample table is maintained separately in `verified_products.json`.
- DRAM capacity is stored in Gb when it is component density; managed storage capacity is stored in GB when it is user-addressable storage capacity.
- NAND raw-die density and packaged managed-storage capacity are not interchangeable.
- eMCP/uMCP records may contain multiple storage and DRAM components; they must not be flattened into one capacity field.
