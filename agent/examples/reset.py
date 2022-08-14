import time
from PIL import Image, ImageDraw
from ST7789 import ST7789


def reset_display():
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
    image = Image.new("RGB", (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(image)

    disp.reset()

    # `reset` sets each pixel to a random color, so let's blank it out
    draw.rectangle((0, 0, 240, 240), (0, 0, 0))
    disp.display(image)

    time.sleep(1.0)

    disp.set_backlight(0)


if __name__ == "__main__":
    reset_display()
