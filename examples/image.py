import sys
from PIL import Image
from ST7789 import ST7789


def image(filename="IMG_5292.jpeg"):
    disp = ST7789(
        rotation=90,  # Needed to display the right way up on Pirate Audio
        port=0,  # SPI port
        cs=1,  # SPI port Chip-select channel
        dc=9,  # BCM pin used for data/command
        backlight=13,
        spi_speed_hz=80 * 1000 * 1000,
    )
    disp.begin()

    width = disp.width
    height = disp.height

    image = Image.open(filename)
    image = image.resize((width, height))
    disp.display(image)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        image(sys.argv[1])
    else:
        image()
