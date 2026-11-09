# Macropad v1

A 4-key macropad with a rotary encoder and OLED display 

I started this project as a way to experiment with hardware. 

## Features

- 4 Cherry MX-style mechanical switches
- Rotary encoder with push-button (volume up/down + mute by default)
- 0.96" 128x64 SSD1306 OLED display showing a pixel-art cat that reacts to typing speed (sleeps when idle, walks at normal pace, runs when typed quickly)
- Custom 3D-printed two-part case (base + lid)

## CAD Model
The case is two printed parts with a base that holds the PCB and a lid that screws on top. 
Made in Fusion360


## Repo structure

- **`cad/`** — Complete assembled 3D model of the case + PCB (STEP)
- **`pcb/`** — KiCad schematic and PCB design source files
- **`firmware/`** — QMK firmware source (keymap, config, OLED animation)
- **`production/`** — Ready-to-manufacture/flash files: Gerbers, individual case part STEPs, and compiled `firmware.uf2`



MIT — see [LICENSE](LICENSE).
