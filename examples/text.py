import sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from ST7789 import ST7789


def text(message="Hello, world!"):
    disp = ST7789(
        rotation=90,  # Needed to display the right way up on Pirate Audio
        port=0,  # SPI port
        cs=1,  # SPI port Chip-select channel
        dc=9,  # BCM pin used for data/command
        backlight=13,
        spi_speed_hz=80 * 1000 * 1000,
    )
    disp.begin()

    WIDTH = disp.width
    HEIGHT = disp.height

    img = Image.new("RGB", (WIDTH, HEIGHT), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30
    )

    _, size_y = draw.textsize(message, font)
    text_y = (disp.height - size_y) // 2

    draw.rectangle((0, 0, disp.width, disp.height), (0, 0, 0))
    draw.text((0, text_y), message, font=font, fill=(255, 255, 255))
    disp.display(img)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        text(sys.argv[1])
    else:
        text()
