
# MediaTek HW Code database

The primary lookup is `data/mediatek/soc_hw_codes.json` (schema v2). It merges two independently pinned sources:

- **acon**: 45 explicit SoC-to-HW-code mappings, with silicon/platform aliases, marketing family and DA-code crosswalk where available.
- **mtkclient**: 89 keys in its `hwconfig` dictionary, covering older MT65xx families, modem/IoT, tablet/TV, and newer Helio/Dimensity platforms.

The merged database currently has **93 unique HW-code values**:
- 45 explicit SoC mappings from acon.
- 48 additional named platform mappings from mtkclient.
- 0 observed codes not safely named by the selected source set.

The raw mtkclient observations are preserved separately in `data/mediatek/hw_code_observations.json`.

## Important interpretation rules

1. **HW Code is not DA Code.** A device reports HW Code; the DA package selection can use a normalized DA code. Both values are retained separately.
2. **HW Code is not a marketing name.** A single silicon family can appear under multiple Helio, Dimensity, Kompanio, tablet, modem, or IoT names.
3. **Silicon aliases are not guaranteed to be separate chips.** The alias list preserves the source's platform names; it does not assert identical die revisions.
4. **HW Sub Code / HW Version / SW Version are runtime device fields.** They belong in device observations, not as one global value per SoC.
5. **Conflicting DA-code observations are preserved and flagged**, not silently resolved.
6. **Coverage is not exhaustive.** The sources contain known software-supported codes; additional vendor-only, unreleased, and device-specific values may exist.

## Selected examples

| HW Code | SoC/platform | DA Code | Notes |
|---|---|---|---|
| `0x0633` | MT6570 | `0x6570` | Legacy code differs from DA code |
| `0x0321` | MT6735 | `0x6735` | Explicit acon crosswalk |
| `0x0601` | MT6750 | `0x6755` | mtkclient platform mapping |
| `0x1066` | MT6781 / Helio G96 | `0x6781` | mtkclient mapping |
| `0x0989` | MT6833 / Dimensity 700 family | `0x6833` | Explicit acon crosswalk |
| `0x1209` | MT6835 / Dimensity 6100+ family | `0x1209` | HW and DA code coincide in source |
| `0x1357` | MT6991 / Dimensity 9400 family | `0x1357` | Newer flagship family |
| `0x8163` | MT8163 | `0x8163` | Tablet/embedded family |
| `0x0992` | MT6880/MT6890 modem | `0x0992` | Modem/platform identifier, not necessarily AP SoC |

## Next expansion sources

The next research pass should add:
- MT6737/MT6737T and other variants from verified preloader/device logs.
- MT6750/MT6758/MT6759 and MT6781 variants.
- MT819x Kompanio families, MT83xx tablet/TV SoCs, MT86xx automotive/TV.
- Older MT62xx/MT25xx modem and IoT platforms.
- Per-code HW subcode/HW version observations with device model and source evidence.

Each new mapping should carry the raw value, exact source, confidence, and whether it is an SoC, modem, connectivity controller, or platform code.
