# my_macropad rules.mk
# NOTE: pin numbers used elsewhere (keyboard.json) are PLACEHOLDERS.
# Verify against your KiCad schematic (XIAO RP2040 -> switches / encoder / OLED)
# and update keyboard.json once you have access to it.

ENCODER_ENABLE = yes
OLED_ENABLE = yes
OLED_DRIVER = ssd1306

# Encoder push-button is wired in as a normal switch on the matrix,
# NOT defined here -- see keymap.c matrix position for the encoder click.
