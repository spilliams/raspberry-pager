import time
from PIL import Image, ImageDraw
from ST7789 import ST7789

SPI_SPEED_MHZ = 80

image = Image.new("RGB", (240, 240), (0, 0, 0))
draw = ImageDraw.Draw(image)

st7789 = ST7789(
    rotation=90,  # Needed to display the right way up on Pirate Audio
    port=0,  # SPI port
    cs=1,  # SPI port Chip-select channel
    dc=9,  # BCM pin used for data/command
    backlight=13,
    spi_speed_hz=SPI_SPEED_MHZ * 1000 * 1000,
)


st7789.reset()

# `reset` sets each pixel to a random color, so let's blank it out
draw.rectangle((0, 0, 240, 240), (0, 0, 0))
st7789.display(image)

time.sleep(1.0)

st7789.set_backlight(0)
