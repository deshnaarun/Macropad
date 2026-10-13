# KiCad V6+ SSD1306 0.96" OLED Library

KiCad V6+ symbol and footprint for the common **SSD1306 0.96 inch 128x64 I2C OLED display module** (the blue/white 4-pin breakout sold everywhere on AliExpress, Amazon, etc).

This is a conversion of [pforrmi/KiCad-SSD1306-128x64](https://github.com/pforrmi/KiCad-SSD1306-128x64) to native KiCad 9 format (`.kicad_sym` / `.kicad_mod`). No legacy `.lib` files, no conversion prompts.

---

## What's included

```
SSD1306-128x64_OLED.kicad_sym   — Symbol library (GND, VCC, SCL, SDA)
SSD1306.pretty/
└── 128x64OLED.kicad_mod        — Footprint with pads, module outline, courtyard
```

---

## The module this targets

| Property | Value |
|---|---|
| Driver IC | SSD1306 |
| Screen size | 0.96 inch |
| Resolution | 128 x 64 px |
| Interface | I2C |
| Connector | 4-pin 2.54mm header (GND, VCC, SCL, SDA) |
| Default I2C address | 0x3C (7-bit) / 0x78 (8-bit) |
| Board dimensions | ~27.3 x 27.8 mm |

This is the standard 4-pin I2C variant. If you have the 7-pin SPI version, this library does not apply.

---

## Installation

### 1. Clone or download

```bash
git clone https://github.com/V01Ddev/kicad-ssd1306-oled-library.git
```

Or download the ZIP from the green **Code** button above.

### 2. Add the symbol library

In KiCad: **Preferences > Manage Symbol Libraries > Add existing library**

Point it to:
```
/path/to/kicad-ssd1306-oled-library/SSD1306-128x64_OLED.kicad_sym
```

### 3. Add the footprint library

In KiCad: **Preferences > Manage Footprint Libraries > Add existing library**

Point it to the `.pretty` folder:
```
/path/to/kicad-ssd1306-oled-library/SSD1306.pretty
```

---

## Usage

In the schematic editor, search for `SSD1306`. Place the symbol and connect:

| Pin | Connect to |
|---|---|
| VCC | 3.3V or 5V power rail |
| GND | Ground |
| SCL | I2C clock (e.g. GPIO22 on ESP32) |
| SDA | I2C data (e.g. GPIO21 on ESP32) |

The footprint will be automatically assigned. If you need to assign it manually, look for `SSD1306:128x64OLED`.

---

## Footprint details

- 4x THT pads at 2.54mm pitch
- Pin 1 (GND) has a square pad for orientation
- Full module outline on `F.Fab`
- Courtyard on `F.CrtYd` covers the entire board area including the display
- Silkscreen outline around the PCB edge

---

## Tested with

- KiCad 10 on Arch Linux
- The generic SSD1306 0.96" I2C module (blue PCB, 4-pin yellow header) widely available from AliExpress and similar

---

## License

[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) — Attribution-NonCommercial-ShareAlike 4.0 International.

This is a derivative work. The original library by pforrmi was shared under CC BY-NC-SA 4.0. Modifications (conversion to KiCad V6+ native `.kicad_sym` / `.kicad_mod` format) are by v01d.dev and are distributed under the same license.

---

## Credits

Original KiCad 4/5 library by [pforrmi](https://github.com/pforrmi/KiCad-SSD1306-128x64), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). This repo converts that work to KiCad V6+ native format.
