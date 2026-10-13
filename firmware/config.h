#pragma once

/* OLED on the XIAO's SDA/SCL pins (D4/D5 = GP6/GP7), which are the RP2040's
 * I2C1 peripheral -> ChibiOS driver I2CD1. The GENERIC_PROMICRO_RP2040 board
 * already enables I2C1, but defaults to GP2/GP3 (your SW3/SW1 pins), so these
 * overrides are required. */
#define I2C_DRIVER   I2CD1
#define I2C1_SDA_PIN GP6
#define I2C1_SCL_PIN GP7

/* 0.96" 128x64 SSD1306 per the schematic. Remove this line if the module
 * you actually bought is the 0.91" 128x32 one. */
#define OLED_DISPLAY_128X64
