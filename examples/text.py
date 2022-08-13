import sys
import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import ST7789

SPI_SPEED_MHZ = 80


def text(message="Hello, world!"):
    disp = ST7789(
        rotation=90,  # Needed to display the right way up on Pirate Audio
        port=0,  # SPI port
        cs=1,  # SPI port Chip-select channel
        dc=9,  # BCM pin used for data/command
        backlight=13,
        spi_speed_hz=SPI_SPEED_MHZ * 1000 * 1000,
    )
    disp.begin()

    WIDTH = disp.width
    HEIGHT = disp.height

    img = Image.new("RGB", (WIDTH, HEIGHT), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30
    )

    size_x, size_y = draw.textsize(message, font)
    text_x = disp.width
    text_y = (disp.height - size_y) // 2

    # for scrolling:
    # t_start = time.time()
    # while True:
    #     x = (time.time() - t_start) * 100
    #     x %= size_x + disp.width
    draw.rectangle((0, 0, disp.width, disp.height), (0, 0, 0))
    draw.text((int(text_x), text_y), message, font=font, fill=(255, 255, 255))
    disp.display(img)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        text(sys.argv[1])
    else:
        text()
