# Macropad v1

A 4-key macropad with a rotary encoder and OLED display 

I started this project as a way to experiment with hardware. 

## Features

- 4 Cherry MX-style mechanical switches
- Rotary encoder with push-button (volume up/down + mute by default)
- 0.91" 128x32 SSD1306 OLED display showing a pixel-art cat that reacts to typing speed (sleeps when idle, walks at normal pace, runs when typed quickly)
- Custom 3D-printed two-part case (base + lid)

## CAD Model
The case is two printed parts with a base that holds the PCB and a lid that screws on top. 
Made in Fusion360

<img width="472" height="496" alt="image" src="https://github.com/user-attachments/assets/cc051c33-91fe-4437-8264-a94d3663a20c" />


## PCB 
Made in KiCad. It's a 2 layer board, 80 X 84 mm. Each switch goes to its own key matrix, no diodes.
Schematic: <img width="734" height="438" alt="image" src="https://github.com/user-attachments/assets/f178b0fe-46b5-4ea4-a6c4-a2aa6506c8f0" />
PCB:<img width="741" height="666" alt="image" src="https://github.com/user-attachments/assets/725e4960-dae7-46f6-8a75-0a95c7cbb2a7" />

## Firmware

The encoder controls volume level. Press to mute.
The 4 keys are placeholders right now but I will set them up to use my most frequent apps (Still experimenting with this but building the case would help me better with this)
The OLED displays a cat. 

## BOM


4x Cherry MX-style switches 
4x 1u MX keycaps 
1x EC11 rotary encoder with push switch 
* 1x Encoder knob 
*  1x 0.91" 128x32 SSD1306 I2C OLED (pin order GND-VCC-SCL-SDA) 
*   1x Seeed XIAO RP2040 
*   4x M3 screws 
*   1x PCB 
*   1x Case (2 printed parts: body + lid)


## Repo structure

- **`cad/`** — Complete assembled 3D model of the case + PCB (STEP)
- **`pcb/`** — KiCad schematic and PCB design source files
- **`firmware/`** — QMK firmware source (keymap, config, OLED animation)
- **`production/`** — Ready-to-manufacture/flash files: Gerbers, individual case part STEPs, and compiled `firmware.uf2`



MIT — see [LICENSE](LICENSE).
