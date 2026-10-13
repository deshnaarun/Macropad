# my_macropad rules.mk
# Pins verified against Macropad_v1 schematic (Seeed XIAO RP2040):
#   SW1 = D10 = GP3    SW2 = D9 = GP4    SW3 = D8 = GP2    SW5 = D3 = GP29
#   Encoder A = D2 = GP28, B = D6 = GP0, push (S1) = D7 = GP1
#   OLED SDA = D4 = GP6, SCL = D5 = GP7 (RP2040 I2C1)

ENCODER_ENABLE = yes
OLED_ENABLE = yes
OLED_DRIVER = ssd1306

# Encoder push-button is wired in as a normal switch on the matrix,
# NOT defined here -- see keymap.c matrix position for the encoder click.
