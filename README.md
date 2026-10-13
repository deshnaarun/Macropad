# Macropad v1

A 4-key macropad with a rotary encoder and OLED display, built around the Seeed XIAO RP2040.

## Features

- 4 Cherry MX-style mechanical switches
- Rotary encoder with push-button (volume up/down + mute by default)
- 0.96" 128x64 SSD1306 OLED display showing a pixel-art cat that reacts to typing speed (sleeps when idle, walks at normal pace, runs when typed quickly)
- Custom 3D-printed two-part case (base + lid)

## Repo structure

- **`cad/`** — Complete assembled 3D model of the case + PCB (STEP)
- **`pcb/`** — KiCad schematic and PCB design source files
- **`firmware/`** — QMK firmware source (keymap, config, OLED animation)
- **`production/`** — Ready-to-manufacture/flash files: Gerbers, individual case part STEPs, and compiled `firmware.uf2`

## Hardware

| Part | Pin (XIAO D-label) | GPIO |
|---|---|---|
| Switch 1 | D10 | GP3 |
| Switch 2 | D9 | GP4 |
| Switch 3 | D8 | GP2 |
| Switch 4 | D3 | GP29 |
| Encoder A | D2 | GP28 |
| Encoder B | D6 | GP0 |
| Encoder push | D7 | GP1 |
| OLED SDA | D4 | GP6 |
| OLED SCL | D5 | GP7 |

## Firmware

Built with QMK. To flash: put the board in bootloader mode (double-tap reset on the XIAO) and drag `production/firmware.uf2` onto the RPI-RP2 drive that appears.

## License

MIT — see [LICENSE](LICENSE).
