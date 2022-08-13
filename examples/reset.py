from ST7789 import ST7789

SPI_SPEED_MHZ = 80

st7789 = ST7789(
    rotation=90,  # Needed to display the right way up on Pirate Audio
    port=0,  # SPI port
    cs=1,  # SPI port Chip-select channel
    dc=9,  # BCM pin used for data/command
    backlight=13,
    spi_speed_hz=SPI_SPEED_MHZ * 1000 * 1000,
)


st7789.reset()
